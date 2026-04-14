#!/usr/bin/env python3
"""
Build Mira upload zips with the required "zip root" layout:

- SKILL.md at zip root
- README.md, CHANGELOG.md at zip root
- references/, userdata/, and scripts/ at zip root

We intentionally keep the packaging logic extremely small and dependency-free.
"""

from __future__ import annotations

import os
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RELEASE_DIR = REPO / "release"


def _add_dir(
    zf: zipfile.ZipFile,
    src_dir: Path,
    arc_prefix: str,
    *,
    exclude_names: set[str] | None = None,
) -> None:
    """
    Add a directory tree into the zip.

    Notes:
    - We add explicit directory entries so empty dirs survive (e.g. .gitkeep dirs).
    - We sort dirs/files for deterministic zip ordering.
    - `exclude_names` is a simple basename filter used to drop large duplicated content
      from the packaged "reading layer" when needed.
    """
    exclude_names = exclude_names or set()

    for root, dirs, files in os.walk(src_dir):
        dirs.sort()
        files.sort()

        # Drop excluded subdirectories early so os.walk won't traverse them.
        # IMPORTANT: apply this filter only at the src_dir root level.
        # Otherwise a basename filter like {"glossary","kb"} would also drop
        # nested subtrees such as references/knowledge/userdata_snapshot/**/glossary.
        if Path(root) == src_dir:
            dirs[:] = [d for d in dirs if d not in exclude_names]

        root_p = Path(root)
        rel_root = root_p.relative_to(src_dir)
        dir_arc = (Path(arc_prefix) / rel_root).as_posix()
        if dir_arc and not dir_arc.endswith("/"):
            dir_arc += "/"
        if dir_arc:
            zf.writestr(dir_arc, "")

        for f in files:
            if f in exclude_names:
                continue
            p = root_p / f
            arc = (Path(arc_prefix) / rel_root / f).as_posix()
            zf.write(p, arc)


def build_zip(
    zip_path: Path,
    *,
    skill_md_path: Path,
    readme_path: Path,
    include_references_core: bool,
) -> None:
    if not skill_md_path.exists():
        raise FileNotFoundError(skill_md_path)
    if not readme_path.exists():
        raise FileNotFoundError(readme_path)

    tmp_path = zip_path.with_suffix(".zip.tmp")
    if tmp_path.exists():
        tmp_path.unlink()

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(skill_md_path, "SKILL.md")
        zf.write(readme_path, "README.md")
        zf.write(REPO / "CHANGELOG.md", "CHANGELOG.md")

        # references/
        if include_references_core:
            _add_dir(zf, REPO / "references" / "core", "references/core")

        # Keep references/knowledge as the "reading layer" only (guides/index/patterns),
        # and keep the live entity content in userdata/.
        _add_dir(
            zf,
            REPO / "references" / "knowledge",
            "references/knowledge",
            exclude_names={"glossary", "kb"},
        )
        # Add back the slim subtrees explicitly (after repository cleanup, these are small).
        if (REPO / "references" / "knowledge" / "glossary").exists():
            _add_dir(zf, REPO / "references" / "knowledge" / "glossary", "references/knowledge/glossary")
        if (REPO / "references" / "knowledge" / "kb").exists():
            _add_dir(zf, REPO / "references" / "knowledge" / "kb", "references/knowledge/kb")

        # userdata/ is the writable/live content layer.
        _add_dir(zf, REPO / "userdata", "userdata")

        # scripts/ contains packaged helper tools referenced by SKILL.md/runbook
        # (for example beautification post-processing and skill-root detection).
        _add_dir(zf, REPO / "scripts", "scripts")

    tmp_path.replace(zip_path)


def main() -> None:
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)

    build_zip(
        RELEASE_DIR / "ab-analysis-framework-beta.zip",
        skill_md_path=REPO / "SKILL.md",
        readme_path=REPO / "README.md",
        include_references_core=True,
    )
    build_zip(
        RELEASE_DIR / "ab-knowledge-builder-beta.zip",
        skill_md_path=REPO / "skills" / "ab-knowledge-builder-beta" / "SKILL.md",
        readme_path=REPO / "skills" / "ab-knowledge-builder-beta" / "README.md",
        include_references_core=False,
    )

    print("OK: rebuilt release zips in", RELEASE_DIR)


if __name__ == "__main__":
    main()
