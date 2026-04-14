#!/usr/bin/env python3
"""
Find the installed skill root directory.

Why:
- In Mira, the sandbox/workspace `pwd` is not the same as the installed skill root.
- Paths like `userdata/...` and `references/...` are relative to the skill root (zip root).
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def _looks_like_skill_root(p: Path) -> bool:
    return (p / "SKILL.md").is_file() and (p / "references" / "core").is_dir()


def _search_upwards(start: Path) -> Path | None:
    cur = start.resolve()
    for _ in range(20):
        if _looks_like_skill_root(cur):
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def _search_common_install_roots(skill_name: str) -> Path | None:
    # Common Mira install roots (Linux). This is best-effort.
    candidates = [
        Path("/opt/tiger/mira_nas/plugins"),
        Path("/opt/tiger/mira/plugins"),
        Path("/opt/mira/plugins"),
        Path("/opt/plugins"),
    ]
    for base in candidates:
        if not base.exists():
            continue
        # Typical path: .../plugins/prod/custom/<id>/skills/<skill_name>/
        for p in base.glob(f"**/skills/{skill_name}"):
            if _looks_like_skill_root(p):
                return p
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", default="ab-analysis-framework-beta", help="Skill directory name")
    args = ap.parse_args()

    env_root = os.environ.get("MIRA_SKILL_ROOT") or os.environ.get("SKILL_ROOT")
    if env_root:
        p = Path(env_root)
        if _looks_like_skill_root(p):
            print(str(p))
            return 0

    up = _search_upwards(Path.cwd())
    if up:
        print(str(up))
        return 0

    common = _search_common_install_roots(args.skill)
    if common:
        print(str(common))
        return 0

    print("NOT_FOUND")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

