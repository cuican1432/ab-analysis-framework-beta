#!/usr/bin/env python3
"""
Minimal validator for a Recall Manifest against a golden benchmark case.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", default="references/core/recall_benchmark.json")
    ap.add_argument("--case-id", required=True)
    ap.add_argument("--manifest", required=True, help="Path to a generated recall manifest JSON")
    args = ap.parse_args()

    bench = json.loads(Path(args.benchmark).read_text())
    case = next((x for x in bench if x["case_id"] == args.case_id), None)
    if case is None:
        print(f"FAIL: case_id not found: {args.case_id}")
        return 2

    manifest = json.loads(Path(args.manifest).read_text())
    recalled = manifest.get("recalled_groups", [])
    unmatched = manifest.get("unmatched_groups", [])

    exp_recall = case["expected_recall_order"]
    exp_unmatched = case["expected_unmatched"]

    ok = True
    if recalled[: len(exp_recall)] != exp_recall:
        print("FAIL: recalled_groups prefix mismatch")
        print(" expected:", exp_recall)
        print(" actual  :", recalled)
        ok = False

    if unmatched != exp_unmatched:
        print("FAIL: unmatched_groups mismatch")
        print(" expected:", exp_unmatched)
        print(" actual  :", unmatched)
        ok = False

    if ok:
        print("OK: recall manifest matches benchmark")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

