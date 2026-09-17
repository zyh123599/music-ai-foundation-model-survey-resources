#!/usr/bin/env python3
"""Check whether locked GitHub revisions are still reachable.

Uses `git ls-remote`; it does not clone model weights or datasets. Rows whose
Source_Status is explicitly UNRESOLVED_AT_CHECK are reported and skipped.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="repro/representative_source_locks.csv")
    args = parser.parse_args()

    rows = list(csv.DictReader(Path(args.file).open(encoding="utf-8")))
    failures = 0
    checked = 0
    skipped = 0

    for row in rows:
        repo = row["Repo"]
        sha = row.get("Locked_SHA", "").strip()
        status = row.get("Source_Status", "LOCKED").strip()

        if status == "UNRESOLVED_AT_CHECK" or not sha:
            print(f"SKIP\t{repo}\t{status or 'NO_SHA'}")
            skipped += 1
            continue

        url = f"https://github.com/{repo}.git"
        proc = subprocess.run(["git", "ls-remote", url, sha], capture_output=True, text=True)
        ok = proc.returncode == 0 and sha in proc.stdout
        print(f"{'OK' if ok else 'MISSING'}\t{repo}\t{sha[:12]}")
        failures += 0 if ok else 1
        checked += 1

    print(f"checked={checked} skipped={skipped} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
