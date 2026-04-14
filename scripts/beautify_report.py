#!/usr/bin/env python3
"""
Enhanced Layer post-processing via Feishu Doc Block API.

This script is intentionally conservative:
- It should NEVER block report delivery if it fails.
- It should keep "V3 Clean": do not add/remove/reorder chapters; only overlay styling.

Canonical spec:
- references/core/beautification_spec_v1.2.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


DOCX_BASE = "https://open.feishu.cn/open-apis/docx/v1/documents"


def _get_token() -> str:
    token = os.environ.get("LARK_USER_ACCESS_TOKEN") or os.environ.get("MIRA_LARK_USER_ACCESS_TOKEN", "")
    token = token.replace("Bearer ", "").strip()
    if not token:
        raise RuntimeError("Missing Block API token. Set LARK_USER_ACCESS_TOKEN or MIRA_LARK_USER_ACCESS_TOKEN.")
    return token


def _api(token: str, method: str, url: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Keep error payload small to avoid logging secrets.
        return {"code": e.code, "msg": e.read().decode("utf-8")[:300]}


def _post_children(token: str, doc_id: str, parent_block_id: str, children: list[dict[str, Any]], index: int = -1) -> dict[str, Any]:
    url = f"{DOCX_BASE}/{doc_id}/blocks/{parent_block_id}/children"
    return _api(token, "POST", url, {"children": children, "index": index})


@dataclass(frozen=True)
class TextRun:
    content: str
    bold: bool = False
    italic: bool = False
    text_color: int | None = None  # 1-7 only
    background_color: int | None = None  # 1-15+


def _text_run(run: TextRun) -> dict[str, Any]:
    style: dict[str, Any] = {}
    if run.bold:
        style["bold"] = True
    if run.italic:
        style["italic"] = True
    if run.text_color is not None:
        if not (1 <= run.text_color <= 7):
            raise ValueError(f"text_color must be 1-7, got {run.text_color}")
        style["text_color"] = run.text_color
    if run.background_color is not None:
        style["background_color"] = run.background_color
    return {"text_run": {"content": run.content, "text_element_style": style}}


def make_text(runs: list[TextRun]) -> dict[str, Any]:
    return {"block_type": 2, "text": {"elements": [_text_run(r) for r in runs], "style": {}}}


def sig_tr(value: str, sig: str) -> TextRun:
    """
    L1 significance style (Block API).
    Sig values: pos / neg / marginal / ns.
    """
    if sig == "pos":
        return TextRun(value, bold=True, text_color=4, background_color=4)
    if sig == "neg":
        return TextRun(value, bold=True, text_color=1, background_color=1)
    if sig == "marginal":
        return TextRun(value, bold=True, text_color=2)
    return TextRun(value, text_color=7)


def create_color_legend(token: str, doc_id: str, parent_id: str, index: int = -1) -> None:
    """Color legend using quote_container (block_type=34), per v1.2 spec."""
    r = _post_children(token, doc_id, parent_id, [{"block_type": 34, "quote_container": {}}], index=index)
    if str(r.get("code", "0")) not in ("0", "None"):
        return
    qid = r["data"]["children"][0]["block_id"]
    _post_children(
        token,
        doc_id,
        qid,
        [
            make_text([TextRun("阅读指引 | Color Legend", bold=True)]),
            make_text(
                [
                    sig_tr("+X.XX%", "pos"),
                    TextRun(" 正向显著（绿色粗体+绿色底色）"),
                    TextRun("    "),
                    sig_tr("-X.XX%", "neg"),
                    TextRun(" 负向显著（红色粗体+红色底色）"),
                    TextRun("    "),
                    sig_tr("+X.XX%", "marginal"),
                    TextRun(" 边际显著（橙色粗体）"),
                    TextRun("    "),
                    sig_tr("---", "ns"),
                    TextRun(" 不显著（灰色）"),
                ]
            ),
        ],
    )


def create_experiment_info(token: str, doc_id: str, parent_id: str, info: dict[str, str]) -> None:
    """Experiment info inline text (bold key + value)."""
    blocks: list[dict[str, Any]] = []
    for k, v in info.items():
        blocks.append(make_text([TextRun(k, bold=True), TextRun(f"：{v}")]))
    _post_children(token, doc_id, parent_id, blocks)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc-id", required=True, help="Target docx document_id")
    ap.add_argument("--parent-id", default=None, help="Parent block_id to insert legend (default: doc root)")
    ap.add_argument("--dry-run", action="store_true", help="Do not call API; only validate inputs")
    args = ap.parse_args()

    if args.dry_run:
        return 0

    token = _get_token()
    doc_id = args.doc_id
    parent_id = args.parent_id or doc_id

    # Minimal proof-of-life: insert a color legend at the top.
    # Full beautification pipeline is intentionally left as a follow-up once
    # integration points (doc reading, block tree mapping) are wired in.
    create_color_legend(token, doc_id, parent_id, index=0)
    time.sleep(0.3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

