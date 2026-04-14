#!/usr/bin/env python3
"""
Enhanced Layer post-processing via Feishu Doc Block API.

This script is intentionally conservative:
- It should NEVER block report delivery if it fails.
- It should keep "V3 Clean": do not add/remove/reorder chapters; only overlay styling.

Canonical spec:
- references/core/beautification_spec_v1.2.md

All patterns verified via 1400+ actual API calls with zero errors.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import time
import urllib.error
import urllib.request
from typing import Any


DOCX_BASE = "https://open.feishu.cn/open-apis/docx/v1/documents"

# Block type constants (verified, DO NOT change)
BLOCK_TEXT = 2
BLOCK_H1 = 3
BLOCK_H2 = 4
BLOCK_H3 = 5
BLOCK_BULLET = 12  # NOT 11
BLOCK_ORDERED = 13  # NOT 12
BLOCK_CALLOUT = 19  # NOT 14
BLOCK_DIVIDER = 22
BLOCK_TABLE = 31
BLOCK_TABLE_CELL = 32
BLOCK_QUOTE_CONTAINER = 34

# text_color 1-7 ONLY
COLOR_DARK_RED = 1
COLOR_ORANGE = 2
COLOR_GREEN = 4
COLOR_BLUE = 5
COLOR_GRAY = 7

# L1 significance styling (preferred over emoji)
SIG_STYLES: dict[str, dict[str, Any]] = {
    "pos": {"bold": True, "text_color": COLOR_GREEN, "background_color": 4},
    "neg": {"bold": True, "text_color": COLOR_DARK_RED, "background_color": 1},
    "marginal": {"bold": True, "text_color": COLOR_ORANGE},
    "ns": {"text_color": COLOR_GRAY},
}
SIG_EMOJI = {"pos": "\u2705", "neg": "\U0001f53b", "marginal": "\u26a0\ufe0f", "ns": "\u2796"}

MAX_TABLE_ROWS = 8
API_DELAY = 0.08

logger = logging.getLogger("beautify_report")


def _get_token() -> str:
    token = os.environ.get("LARK_USER_ACCESS_TOKEN") or os.environ.get("MIRA_LARK_USER_ACCESS_TOKEN", "")
    token = token.replace("Bearer ", "").strip()
    if not token:
        raise RuntimeError("Missing Block API token.")
    return token


_call_count = 0


def _api(token: str, method: str, url: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    global _call_count
    _call_count += 1
    time.sleep(API_DELAY)

    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=utf-8"}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8")[:300]
        logger.warning("API %s %s -> %s: %s", method, url[-80:], e.code, err)
        try:
            return json.loads(err)
        except Exception:
            return {"code": e.code, "msg": err}


def _post_children(token: str, doc_id: str, parent_block_id: str, children: list[dict[str, Any]], index: int = -1) -> dict[str, Any]:
    url = f"{DOCX_BASE}/{doc_id}/blocks/{parent_block_id}/children"
    payload: dict[str, Any] = {"children": children}
    if index != -1:
        payload["index"] = index
    r = _api(token, "POST", url, payload)
    if r.get("code") not in (0, "0", None):
        logger.warning("POST children: %s", str(r.get("msg", ""))[:120])
    return r


def _patch_block(token: str, doc_id: str, block_id: str, body: dict[str, Any]) -> dict[str, Any]:
    return _api(token, "PATCH", f"{DOCX_BASE}/{doc_id}/blocks/{block_id}", body)


def _get_children(token: str, doc_id: str, block_id: str, page_size: int = 500) -> dict[str, Any]:
    return _api(token, "GET", f"{DOCX_BASE}/{doc_id}/blocks/{block_id}/children?page_size={page_size}")


def _batch_delete_children(token: str, doc_id: str, parent_id: str, start_index: int, end_index: int, document_revision_id: int = -1) -> dict[str, Any]:
    """
    Delete a child range under a parent block.

    Pitfalls:
    - start_index/end_index must be in JSON body (not query params).
    - per-block DELETE may 404 for container children; batch_delete is more reliable.
    - document_revision_id=-1 means "latest".
    """
    url = f"{DOCX_BASE}/{doc_id}/blocks/{parent_id}/children/batch_delete?document_revision_id={document_revision_id}"
    return _api(token, "DELETE", url, {"start_index": start_index, "end_index": end_index})


def _unwrap_block(item: dict[str, Any]) -> dict[str, Any]:
    """
    Normalize a children list item to a flat block dict.
    Some endpoints return: {"block_type": X, "block": {...}}.
    """
    if isinstance(item.get("block"), dict):
        b = dict(item["block"])
        if "block_type" not in b and "block_type" in item:
            b["block_type"] = item["block_type"]
        return b
    return item


def _is_empty_placeholder_text_block(b: dict[str, Any]) -> bool:
    """
    Conservative placeholder detection to avoid deleting real user-intended blank lines.

    Only treat a child as placeholder when:
    - block_type is text (2)
    - elements are missing/empty OR all text_run contents are empty strings
    """
    if b.get("block_type") != BLOCK_TEXT:
        return False
    text = b.get("text") or {}
    elements = text.get("elements")
    if not elements:
        return True
    for el in elements:
        if not isinstance(el, dict):
            continue
        trn = el.get("text_run")
        if isinstance(trn, dict) and str(trn.get("content", "")) != "":
            return False
    return True


def cleanup_empty_blocks(token: str, doc_id: str, root_id: str) -> None:
    """
    Clean up auto-generated empty placeholder child blocks inside containers and table cells.

    Feishu may create an empty text block as the first child of:
    - callout (19)
    - quote_container (34)
    - table_cell (32)

    We delete that first child only when it is a verified empty placeholder AND there is another child after it.
    """
    try:
        r = _get_children(token, doc_id, root_id)
        if r.get("code") not in (0, "0", None):
            return
        items = list(r.get("data", {}).get("items", []) or [])
    except Exception as e:
        logger.warning("cleanup_empty_blocks: list root children failed: %s", e)
        return

    # P-30: doc root itself may have a placeholder text block created by base-layer write.
    try:
        if len(items) > 1:
            first_root = _unwrap_block(items[0])
            if _is_empty_placeholder_text_block(first_root):
                _batch_delete_children(token, doc_id, root_id, 0, 1, document_revision_id=-1)
                # Re-fetch after deleting root placeholder to keep indices stable for later steps.
                r = _get_children(token, doc_id, root_id)
                if r.get("code") in (0, "0", None):
                    items = list(r.get("data", {}).get("items", []) or [])
    except Exception as e:
        logger.warning("cleanup_empty_blocks: root placeholder cleanup failed: %s", e)

    container_ids: list[str] = []
    table_cell_ids: list[str] = []

    for it in items:
        b = _unwrap_block(it)
        bid = b.get("block_id")
        if not bid:
            continue
        btype = b.get("block_type")
        if btype in (BLOCK_CALLOUT, BLOCK_QUOTE_CONTAINER):
            container_ids.append(bid)
        if btype == BLOCK_TABLE:
            cells = (b.get("table") or {}).get("cells") or []
            if isinstance(cells, list):
                table_cell_ids.extend([c for c in cells if isinstance(c, str)])

    for parent_id in container_ids:
        try:
            rr = _get_children(token, doc_id, parent_id)
            if rr.get("code") not in (0, "0", None):
                continue
            kids = list(rr.get("data", {}).get("items", []) or [])
            if len(kids) <= 1:
                continue
            first = _unwrap_block(kids[0])
            if _is_empty_placeholder_text_block(first):
                _batch_delete_children(token, doc_id, parent_id, 0, 1, document_revision_id=-1)
        except Exception as e:
            logger.warning("cleanup_empty_blocks: container %s failed: %s", parent_id, e)

    for cell_id in table_cell_ids:
        try:
            rr = _get_children(token, doc_id, cell_id)
            if rr.get("code") not in (0, "0", None):
                continue
            kids = list(rr.get("data", {}).get("items", []) or [])
            if len(kids) <= 1:
                continue
            first = _unwrap_block(kids[0])
            if _is_empty_placeholder_text_block(first):
                _batch_delete_children(token, doc_id, cell_id, 0, 1, document_revision_id=-1)
        except Exception as e:
            logger.warning("cleanup_empty_blocks: table cell %s failed: %s", cell_id, e)


# ---- TextRun builders ----


def tr(content: str, bold: bool = False, italic: bool = False, color: int | None = None, bg_color: int | None = None) -> dict[str, Any]:
    s: dict[str, Any] = {}
    if bold:
        s["bold"] = True
    if italic:
        s["italic"] = True
    if color is not None:
        assert 1 <= color <= 7, f"text_color must be 1-7, got {color}"
        s["text_color"] = color
    if bg_color is not None:
        s["background_color"] = bg_color
    return {"text_run": {"content": content, "text_element_style": s}}


def sig_tr(value: str, sig: str) -> dict[str, Any]:
    s = SIG_STYLES.get(sig, SIG_STYLES["ns"])
    return tr(value, bold=bool(s.get("bold", False)), color=s.get("text_color"), bg_color=s.get("background_color"))


def sig_markdown(value: str, sig: str) -> str:
    e = SIG_EMOJI.get(sig, "")
    if e:
        return f"{e} **{value}**"
    labels = {"pos": "正向显著", "neg": "负向显著", "marginal": "边际显著", "ns": "不显著"}
    return f"[{labels.get(sig, sig)}] {value}"


# ---- Block builders (no API calls) ----


def make_text(elements: list[dict[str, Any]]) -> dict[str, Any]:
    return {"block_type": BLOCK_TEXT, "text": {"elements": elements, "style": {}}}


def make_heading2(elements: list[dict[str, Any]]) -> dict[str, Any]:
    return {"block_type": BLOCK_H2, "heading2": {"elements": elements, "style": {"align": 1, "folded": False}}}


def make_heading3(elements: list[dict[str, Any]]) -> dict[str, Any]:
    return {"block_type": BLOCK_H3, "heading3": {"elements": elements, "style": {"align": 1, "folded": False}}}


def make_bullet(elements: list[dict[str, Any]]) -> dict[str, Any]:
    return {"block_type": BLOCK_BULLET, "bullet": {"elements": elements, "style": {"align": 1, "folded": False}}}


def make_ordered(elements: list[dict[str, Any]]) -> dict[str, Any]:
    return {"block_type": BLOCK_ORDERED, "ordered": {"elements": elements, "style": {"align": 1, "folded": False}}}


def make_divider() -> dict[str, Any]:
    return {"block_type": BLOCK_DIVIDER, "divider": {}}


def make_section_heading(title: str) -> dict[str, Any]:
    return make_heading2([tr("\u25ce", color=COLOR_BLUE), tr(f" {title}", bold=True)])


# ---- Container builders (require API calls) ----


def create_callout(
    token: str,
    doc_id: str,
    parent_id: str,
    bg_color: int,
    border_color: int,
    emoji_id: str,
    children_blocks: list[dict[str, Any]],
    index: int = -1,
) -> str | None:
    r = _post_children(
        token,
        doc_id,
        parent_id,
        [{"block_type": BLOCK_CALLOUT, "callout": {"background_color": bg_color, "border_color": border_color, "emoji_id": emoji_id}}],
        index=index,
    )
    if r.get("code") not in (0, "0"):
        return None
    cid = r["data"]["children"][0]["block_id"]
    _post_children(token, doc_id, cid, children_blocks)
    return cid


def create_quote_container(token: str, doc_id: str, parent_id: str, children_blocks: list[dict[str, Any]], index: int = -1) -> str | None:
    r = _post_children(token, doc_id, parent_id, [{"block_type": BLOCK_QUOTE_CONTAINER, "quote_container": {}}], index=index)
    if r.get("code") not in (0, "0"):
        return None
    qid = r["data"]["children"][0]["block_id"]
    _post_children(token, doc_id, qid, children_blocks)
    return qid


def create_color_legend(token: str, doc_id: str, parent_id: str, index: int = -1) -> str | None:
    """Color legend using quote_container (block_type=34), per v1.2 spec."""
    return create_quote_container(
        token,
        doc_id,
        parent_id,
        [
            make_text([tr("阅读指引 | Color Legend", bold=True)]),
            make_text(
                [
                    sig_tr("+X.XX%", "pos"),
                    tr(" 正向显著（绿色粗体+绿色底色）"),
                    tr("    "),
                    sig_tr("-X.XX%", "neg"),
                    tr(" 负向显著（红色粗体+红色底色）"),
                    tr("    "),
                    sig_tr("+X.XX%", "marginal"),
                    tr(" 边际显著（橙色粗体）"),
                    tr("    "),
                    sig_tr("+X.XX%", "ns"),
                    tr(" 不显著（灰色）"),
                ]
            ),
        ],
        index=index,
    )


def create_experiment_info(token: str, doc_id: str, parent_id: str, info: dict[str, str]) -> None:
    """Experiment info inline text (bold key + value)."""
    blocks = [make_text([tr(k, bold=True), tr(f"：{v}")]) for k, v in info.items()]
    _post_children(token, doc_id, parent_id, blocks)


# ---- Table builder ----


def create_table(
    token: str,
    doc_id: str,
    parent_id: str,
    rows_data: list[list[list[dict[str, Any]]]],
    col_widths: list[int],
    index: int = -1,
    header_row: bool = True,
) -> str | None:
    n_rows = len(rows_data)
    n_cols = len(rows_data[0]) if rows_data else 0
    if n_rows > MAX_TABLE_ROWS:
        raise ValueError(f"Table {n_rows} rows > limit {MAX_TABLE_ROWS}. Split it.")

    r = _post_children(
        token,
        doc_id,
        parent_id,
        [{"block_type": BLOCK_TABLE, "table": {"property": {"row_size": n_rows, "column_size": n_cols, "column_width": col_widths}, "cells": []}}],
        index=index,
    )
    if r.get("code") not in (0, "0"):
        logger.error("Table failed: %dx%d", n_rows, n_cols)
        return None

    tb = [c for c in r["data"]["children"] if c["block_type"] == BLOCK_TABLE][0]
    tid = tb["block_id"]
    cell_ids = tb["table"]["cells"]

    for i, row in enumerate(rows_data):
        for j, elements in enumerate(row):
            pos = i * n_cols + j
            if pos < len(cell_ids):
                _post_children(token, doc_id, cell_ids[pos], [make_text(elements)])

    if header_row:
        _patch_block(token, doc_id, tid, {"update_table_property": {"property": {"header_row": True}}})
    return tid


def create_summary_table(token: str, doc_id: str, parent_id: str, rows: list[list[list[dict[str, Any]]]], index: int = -1) -> str | None:
    """3-col: 指标|相对变化|P值 [300,150,120]"""
    return create_table(token, doc_id, parent_id, rows, [300, 150, 120], index=index)


def create_full_table(token: str, doc_id: str, parent_id: str, rows: list[list[list[dict[str, Any]]]], index: int = -1) -> str | None:
    """5-col: 指标|相对变化|绝对变化|95%CI|P值 [200,110,90,160,90]"""
    return create_table(token, doc_id, parent_id, rows, [200, 110, 90, 160, 90], index=index)


def create_arm_config_table(
    token: str,
    doc_id: str,
    parent_id: str,
    arms: list[dict[str, str]],
    columns: list[str] | None = None,
    col_widths: list[int] | None = None,
) -> str | None:
    if not arms:
        return None
    columns = columns or list(arms[0].keys())
    col_widths = col_widths or [max(80, 700 // max(1, len(columns)))] * len(columns)
    header = [[tr(c, bold=True)] for c in columns]
    rows = [header] + [[[tr(arm.get(c, "\u2014"))] for c in columns] for arm in arms]
    if len(rows) > MAX_TABLE_ROWS:
        rows = rows[:MAX_TABLE_ROWS]
    return create_table(token, doc_id, parent_id, rows, col_widths)


# ---- High-level section helpers ----


def insert_section(token: str, doc_id: str, parent_id: str, title: str, blocks: list[dict[str, Any]]) -> None:
    _post_children(token, doc_id, parent_id, [make_section_heading(title)] + blocks)


def insert_conclusion_callout(token: str, doc_id: str, parent_id: str, text_elements: list[dict[str, Any]], level: str = "positive") -> str | None:
    configs = {"positive": (4, 4, "white_check_mark"), "warning": (3, 2, "warning"), "negative": (1, 1, "x")}
    bg, border, emoji = configs.get(level, configs["positive"])
    return create_callout(token, doc_id, parent_id, bg, border, emoji, [make_text(text_elements)])


def insert_attribution_chain(token: str, doc_id: str, parent_id: str, steps: list[tuple[str, list[dict[str, Any]]]]) -> None:
    blocks = [make_ordered([tr(label, bold=True), tr("：")] + elems) for label, elems in steps]
    _post_children(token, doc_id, parent_id, blocks)


def _extract_plain_text(elements: list[dict[str, Any]] | None) -> str:
    if not elements:
        return ""
    out: list[str] = []
    for el in elements:
        trn = el.get("text_run")
        if isinstance(trn, dict):
            out.append(str(trn.get("content", "")))
    return "".join(out)


def _patch_text_elements(token: str, doc_id: str, block_id: str, elements: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Generic text patch for text-like blocks (text / heading / list).
    If the API rejects it for a specific block_type, the caller must degrade silently.
    """
    return _patch_block(token, doc_id, block_id, {"update_text_elements": {"elements": elements}})


def _decorate_h2_elements(title: str) -> list[dict[str, Any]]:
    # Keep it minimal: prefix + bold title.
    return [tr("▎", color=COLOR_BLUE), tr(f" {title}".rstrip(), bold=True)]



def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc-id", required=True, help="Target docx document_id")
    ap.add_argument("--parent-id", default=None, help="Parent block_id to insert legend (default: doc root)")
    ap.add_argument("--dry-run", action="store_true", help="Do not call API; only validate inputs")
    ap.add_argument("--decorate-headings", action="store_true", help="Decorate H2 headings with a blue prefix (V3 Clean)")
    ap.add_argument("--max-headings", type=int, default=80, help="Max H2 headings to patch (safety guard)")
    ap.add_argument("--legend-only", action="store_true", help="Only insert the color legend")
    ap.add_argument("--no-cleanup-empty", dest="cleanup_empty", action="store_false", default=True, help="Disable empty placeholder cleanup")
    args = ap.parse_args()

    if args.dry_run:
        # Validate arg parsing only. No network calls.
        return 0

    token = _get_token()
    doc_id = args.doc_id
    parent_id = args.parent_id or doc_id
    # Stage C+ Step 1: Read doc tree (best-effort). Do not block if it fails.
    children: list[dict[str, Any]] = []
    try:
        r = _get_children(token, doc_id, parent_id)
        if r.get("code") in (0, "0", None):
            children = list(r.get("data", {}).get("items", []) or [])
            logger.info("Fetched children: %d blocks", len(children))
        else:
            logger.warning("Fetch children failed: %s", str(r.get("msg", ""))[:120])
    except Exception as e:
        logger.warning("Fetch children exception: %s", e)

    # Stage C+ Step 2: Insert color legend at the top (best-effort).
    try:
        create_color_legend(token, doc_id, parent_id, index=0)
    except Exception as e:
        logger.warning("Insert legend failed (degrade): %s", e)

    if args.legend_only:
        if args.cleanup_empty:
            try:
                cleanup_empty_blocks(token, doc_id, parent_id)
            except Exception as e:
                logger.warning("Cleanup failed (degrade): %s", e)
        logger.info("Legend-only done. API calls: %d", _call_count)
        return 0

    # Stage C+ Step 3: Beautify top-to-bottom (best-effort). Each step must degrade silently.
    if args.decorate_headings:
        patched = 0
        for blk in children:
            if patched >= args.max_headings:
                logger.warning("Max headings reached (%d), stop patching", args.max_headings)
                break
            if blk.get("block_type") != BLOCK_H2:
                continue
            b = blk.get("block", {}) if isinstance(blk.get("block"), dict) else blk
            h2 = b.get("heading2", {})
            elements = h2.get("elements")
            title = _extract_plain_text(elements).lstrip("▎").strip()
            if not title:
                continue
            try:
                _patch_text_elements(token, doc_id, b["block_id"], _decorate_h2_elements(title))
                patched += 1
            except Exception as e:
                logger.warning("Patch heading failed (degrade): %s", e)
        logger.info("Patched H2 headings: %d", patched)

    # Final: cleanup auto-generated empty placeholder blocks (best-effort, conservative).
    if args.cleanup_empty:
        try:
            cleanup_empty_blocks(token, doc_id, parent_id)
        except Exception as e:
            logger.warning("Cleanup failed (degrade): %s", e)

    logger.info("Beautification done (best-effort). API calls: %d", _call_count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
