#!/usr/bin/env python3
"""
Sync the runtime copy of tt-social-experiment-wiki into a local cache.

Behavior:
- First run: shallow-clone the target repo's main branch.
- Later runs: reuse the cached repo and try to refresh it.
- If refresh fails but a valid cache exists, keep using the cache.
- If no valid cache exists, exit non-zero.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_REPO_URL = "https://code.byted.org/elaine.cui/tt-social-experiment-wiki"
DEFAULT_BRANCH = "main"
DEFAULT_CACHE_DIRNAME = "runtime_cache/tt-social-experiment-wiki"
REQUIRED_FILES = (
    "wiki/index.md",
    "wiki/core-metrics.md",
    "wiki/metric_groups/index.md",
)


def _skill_root() -> Path:
    # In both the source repo and the installed skill bundle, `scripts/` lives under
    # the skill root, so the parent directory is the right anchor.
    return Path(__file__).resolve().parents[1]


def _run_git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        check=False,
        text=True,
        capture_output=True,
    )


def _is_valid_cache(repo_dir: Path) -> bool:
    if not (repo_dir / ".git").exists():
        return False
    return all((repo_dir / rel).exists() for rel in REQUIRED_FILES)


def _current_commit(repo_dir: Path) -> str:
    proc = _run_git(["rev-parse", "HEAD"], cwd=repo_dir)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "failed to resolve HEAD")
    return proc.stdout.strip()


def _remote_url(repo_dir: Path) -> str:
    proc = _run_git(["remote", "get-url", "origin"], cwd=repo_dir)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "failed to read origin url")
    return proc.stdout.strip()


def _clone_fresh(repo_url: str, branch: str, repo_dir: Path) -> None:
    repo_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="tt-social-experiment-wiki-", dir=str(repo_dir.parent)) as tmp_root:
        tmp_dir = Path(tmp_root) / "repo"
        proc = _run_git(
            ["clone", "--depth", "1", "--branch", branch, repo_url, str(tmp_dir)],
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "git clone failed")
        if repo_dir.exists():
            shutil.rmtree(repo_dir)
        shutil.move(str(tmp_dir), str(repo_dir))


def _refresh_existing(repo_url: str, branch: str, repo_dir: Path) -> None:
    origin = _remote_url(repo_dir)
    if origin != repo_url:
        raise RuntimeError(f"cache origin mismatch: expected {repo_url}, got {origin}")

    fetch = _run_git(["fetch", "origin", branch, "--depth", "1"], cwd=repo_dir)
    if fetch.returncode != 0:
        raise RuntimeError(fetch.stderr.strip() or fetch.stdout.strip() or "git fetch failed")

    checkout = _run_git(["checkout", "-B", branch, f"origin/{branch}"], cwd=repo_dir)
    if checkout.returncode != 0:
        raise RuntimeError(checkout.stderr.strip() or checkout.stdout.strip() or "git checkout failed")


def sync_repo(repo_url: str, branch: str, repo_dir: Path) -> tuple[Path, str, list[str]]:
    warnings: list[str] = []
    valid_before = _is_valid_cache(repo_dir)

    if not repo_dir.exists():
        _clone_fresh(repo_url, branch, repo_dir)
    elif not valid_before:
        warnings.append(f"existing cache at {repo_dir} is invalid; rebuilding it")
        _clone_fresh(repo_url, branch, repo_dir)
    else:
        try:
            _refresh_existing(repo_url, branch, repo_dir)
        except Exception as exc:  # noqa: BLE001 - keep cache fallback simple
            warnings.append(f"refresh failed, using cached repo: {exc}")

    if not _is_valid_cache(repo_dir):
        raise RuntimeError(
            "wiki cache is unavailable or missing required entry files: "
            + ", ".join(REQUIRED_FILES)
        )

    return repo_dir, _current_commit(repo_dir), warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="Sync tt-social-experiment-wiki into the local runtime cache.")
    ap.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="Codebase repo URL to sync")
    ap.add_argument("--branch", default=DEFAULT_BRANCH, help="Branch to sync")
    ap.add_argument(
        "--cache-dir",
        help="Override cache directory. Defaults to <skill_root>/runtime_cache/tt-social-experiment-wiki",
    )
    ap.add_argument("--json", action="store_true", help="Print machine-readable JSON output")
    args = ap.parse_args()

    skill_root = _skill_root()
    cache_dir = Path(args.cache_dir) if args.cache_dir else (skill_root / DEFAULT_CACHE_DIRNAME)
    cache_dir = cache_dir.resolve()

    try:
        repo_dir, commit, warnings = sync_repo(args.repo_url, args.branch, cache_dir)
    except Exception as exc:  # noqa: BLE001 - surface a single user-facing error line
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=True))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    payload = {
        "ok": True,
        "repo_url": args.repo_url,
        "branch": args.branch,
        "cache_dir": str(repo_dir),
        "commit": commit,
        "entry_files": [str((repo_dir / rel).resolve()) for rel in REQUIRED_FILES],
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=True))
        return 0

    for warning in warnings:
        print(f"WARNING: {warning}")
    print(f"CACHE_DIR={payload['cache_dir']}")
    print(f"COMMIT={payload['commit']}")
    for rel, full_path in zip(REQUIRED_FILES, payload["entry_files"], strict=True):
        print(f"{rel}={full_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
