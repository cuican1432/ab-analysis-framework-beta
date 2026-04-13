#!/usr/bin/env python3
"""
Build Mira upload zips with the required "zip root" layout:

- SKILL.md at zip root
- README.md, CHANGELOG.md at zip root
- references/ and userdata/ at zip root

We intentionally keep the packaging logic extremely small and dependency-free.
"""

from __future__ import annotations

import os
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RELEASE_DIR = REPO / "release"


def _add_dir(zf: zipfile.ZipFile, src_dir: Path, arc_prefix: str) -> None:
    # Add explicit directory entries so empty dirs survive (e.g. .gitkeep dirs).
    for root, dirs, files in os.walk(src_dir):
        root_p = Path(root)
        rel_root = root_p.relative_to(src_dir)
        dir_arc = (Path(arc_prefix) / rel_root).as_posix()
        if dir_arc and not dir_arc.endswith("/"):
            dir_arc += "/"
        if dir_arc:
            zf.writestr(dir_arc, "")

        for f in files:
            p = root_p / f
            arc = (Path(arc_prefix) / rel_root / f).as_posix()
            zf.write(p, arc)


def build_zip(zip_path: Path, skill_md_path: Path) -> None:
    if not skill_md_path.exists():
        raise FileNotFoundError(skill_md_path)

    tmp_path = zip_path.with_suffix(".zip.tmp")
    if tmp_path.exists():
        tmp_path.unlink()

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(skill_md_path, "SKILL.md")
        zf.write(REPO / "README.md", "README.md")
        zf.write(REPO / "CHANGELOG.md", "CHANGELOG.md")
        _add_dir(zf, REPO / "references", "references")
        _add_dir(zf, REPO / "userdata", "userdata")

    tmp_path.replace(zip_path)


def main() -> None:
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)

    build_zip(
        RELEASE_DIR / "ab-analysis-framework-beta.zip",
        REPO / "SKILL.md",
    )
    build_zip(
        RELEASE_DIR / "ab-knowledge-builder-beta.zip",
        REPO / "skills" / "ab-knowledge-builder-beta" / "SKILL.md",
    )

    print("OK: rebuilt release zips in", RELEASE_DIR)


if __name__ == "__main__":
    main()

