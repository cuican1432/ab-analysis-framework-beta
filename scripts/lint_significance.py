#!/usr/bin/env python3
"""
Minimal lint for report significance claims.

Rule (base layer):
- Any line containing a significant marker (✅ or 🔻) must contain an explicit p-value signal
  (e.g. 'p=' or 'p值' or 'P 值') in the same line.

This is a heuristic guardrail, not a statistical verifier.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SIG_MARKERS = ("✅", "🔻")
PVAL_PAT = re.compile(r"(p\s*=\s*0?\.\d+|p值|P\s*值|p-value)", re.IGNORECASE)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to report markdown file")
    args = ap.parse_args()

    p = Path(args.path)
    if not p.exists():
        print(f"FAIL: file not found: {p}")
        return 2

    bad: list[tuple[int, str]] = []
    for i, line in enumerate(p.read_text().splitlines(), start=1):
        if any(m in line for m in SIG_MARKERS):
            if not PVAL_PAT.search(line):
                bad.append((i, line))

    if bad:
        print("FAIL: significant markers without p-value evidence on the same line:")
        for i, line in bad[:50]:
            print(f"- L{i}: {line[:200]}")
        if len(bad) > 50:
            print(f"... and {len(bad) - 50} more")
        return 1

    print("OK: significance lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

