#!/usr/bin/env python3
"""
Minimal repository checks for packaging and knowledge-layer discipline.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RELEASE = REPO / "release"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def check_exists(path: Path) -> None:
    if not path.exists():
        fail(f"missing required path: {path}")


def check_zip_entries(zip_path: Path, *, must_have: list[str], must_not_have_prefixes: list[str]) -> None:
    check_exists(zip_path)
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())

    for item in must_have:
        if item not in names:
            fail(f"{zip_path.name} missing entry: {item}")

    for prefix in must_not_have_prefixes:
        hits = [name for name in names if name.startswith(prefix)]
        if hits:
            fail(f"{zip_path.name} must not contain {prefix}, found: {hits[:5]}")


def check_file_contains(path: Path, needle: str) -> None:
    check_exists(path)
    text = path.read_text()
    if needle not in text:
        fail(f"{path} missing required text: {needle}")


def check_knowledge_layer() -> None:
    glossary_dir = REPO / "references" / "knowledge" / "glossary"
    kb_dir = REPO / "references" / "knowledge" / "kb"

    allowed_glossary = {"index.md"}
    actual_glossary = {p.name for p in glossary_dir.iterdir()}
    extra_glossary = actual_glossary - allowed_glossary
    if extra_glossary:
        fail(f"references/knowledge/glossary should only keep reading-layer files, found extras: {sorted(extra_glossary)}")

    allowed_kb = {"index.md", "metric_caliber_patterns.md", "metric_caliber_metric_inventory.md", "platform_terms_outline.md"}
    actual_kb = {p.name for p in kb_dir.iterdir()}
    extra_kb = actual_kb - allowed_kb
    if extra_kb:
        fail(f"references/knowledge/kb contains unexpected files: {sorted(extra_kb)}")


def main() -> None:
    check_exists(REPO / "references" / "core" / "report_output_rules.md")
    check_exists(REPO / "scripts" / "sync_social_experiment_wiki.py")
    check_file_contains(REPO / "references" / "core" / "index.md", "report_output_rules.md")
    check_file_contains(REPO / "SKILL.md", "report_output_rules.md")
    check_file_contains(REPO / "SKILL.md", "sync_social_experiment_wiki.py")
    check_file_contains(REPO / "references" / "core" / "workflow.md", "sync_social_experiment_wiki.py")

    check_knowledge_layer()

    check_zip_entries(
        RELEASE / "ab-analysis-framework-beta.zip",
        must_have=[
            "SKILL.md",
            "README.md",
            "CHANGELOG.md",
            "references/core/report_output_rules.md",
            "scripts/sync_social_experiment_wiki.py",
        ],
        must_not_have_prefixes=[],
    )
    check_zip_entries(
        RELEASE / "ab-knowledge-builder-beta.zip",
        must_have=[
            "SKILL.md",
            "README.md",
            "CHANGELOG.md",
        ],
        must_not_have_prefixes=["references/core/"],
    )

    print("OK: repository checks passed")


if __name__ == "__main__":
    main()
