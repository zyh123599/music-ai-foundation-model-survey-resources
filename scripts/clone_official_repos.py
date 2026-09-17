#!/usr/bin/env python3
"""Clone official repositories listed in repro/official_repos.csv.

This script does not install dependencies, download model weights, or accept
third-party licenses on the user's behalf.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path


def rows(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="repro/official_repos.csv")
    parser.add_argument("--dest", default="external")
    parser.add_argument("--domain", default=None, help="substring match on Evidence_Domain")
    parser.add_argument("--depth", type=int, default=1)
    args = parser.parse_args()

    manifest = Path(args.manifest)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    selected = []
    for row in rows(manifest):
        if args.domain and args.domain.lower() not in row["Evidence_Domain"].lower():
            continue
        selected.append(row)

    for i, row in enumerate(selected, 1):
        repo = row["Repo"]
        url = row["Resource_URL"]
        target = dest / repo.replace("/", "__")
        print(f"[{i}/{len(selected)}] {repo}")
        if target.exists():
            print(f"  skip: {target} already exists")
            continue
        cmd = ["git", "clone", "--depth", str(args.depth), url, str(target)]
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            print(f"  clone failed ({result.returncode})")


if __name__ == "__main__":
    main()
