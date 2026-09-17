#!/usr/bin/env python3
"""Check whether locked GitHub revisions are still reachable.

Uses `git ls-remote`; it does not clone model weights or datasets.
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
    for row in rows:
        repo = row["Repo"]
        sha = row["Locked_SHA"]
        url = f"https://github.com/{repo}.git"
        proc = subprocess.run(["git", "ls-remote", url, sha], capture_output=True, text=True)
        ok = proc.returncode == 0 and sha in proc.stdout
        print(f"{'OK' if ok else 'MISSING'}\t{repo}\t{sha[:12]}")
        failures += 0 if ok else 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
