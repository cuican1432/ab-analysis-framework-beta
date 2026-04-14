#!/usr/bin/env python3
"""
Compute a stable run signature hash for an experiment analysis run.

This is a helper to reduce cross-run context contamination:
- Hash normalized source URLs + a header/config snapshot (verbatim text).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def _normalize_url(u: str) -> str:
    u = u.strip()
    u = re.sub(r"\s+", "", u)
    return u


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prd-url", required=True)
    ap.add_argument("--raw-url", required=True)
    ap.add_argument("--header-snapshot", help="Path to a text file containing extracted header/config snapshot")
    ap.add_argument("--out", help="Write JSON signature to path")
    args = ap.parse_args()

    prd = _normalize_url(args.prd_url)
    raw = _normalize_url(args.raw_url)

    snapshot = ""
    if args.header_snapshot:
        snapshot = Path(args.header_snapshot).read_text()

    payload = {
        "prd_url": prd,
        "raw_data_url": raw,
        "header_snapshot": snapshot,
    }
    source_hash = sha256_hex(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8"))

    out = {
        "prd_url": prd,
        "raw_data_url": raw,
        "source_hash": source_hash,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    if args.out:
        Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

