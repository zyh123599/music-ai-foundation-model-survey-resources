#!/usr/bin/env python3
"""Clone official GitHub repositories listed in the paper-resource crosswalk."""
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
    parser.add_argument("--manifest", default="resources/paper_resource_crosswalk.csv")
    parser.add_argument("--dest", default="external")
    parser.add_argument("--area", default=None, help="substring match on Area")
    parser.add_argument("--depth", type=int, default=1)
    args = parser.parse_args()

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    selected = []
    seen = set()
    for row in rows(Path(args.manifest)):
        if row.get("Resource_type") != "GitHub":
            continue
        if args.area and args.area.lower() not in row.get("Area", "").lower():
            continue
        url = row.get("Primary_resource", "")
        if not url.startswith("https://github.com/"):
            continue
        repo = url.removeprefix("https://github.com/").rstrip("/").removesuffix(".git")
        if repo in seen:
            continue
        seen.add(repo)
        selected.append((repo, url))

    for i, (repo, url) in enumerate(selected, 1):
        target = dest / repo.replace("/", "__")
        print(f"[{i}/{len(selected)}] {repo}")
        if target.exists():
            print(f"  skip: {target} already exists")
            continue
        result = subprocess.run(
            ["git", "clone", "--depth", str(args.depth), url, str(target)],
            check=False,
        )
        if result.returncode != 0:
            print(f"  clone failed ({result.returncode})")


if __name__ == "__main__":
    main()
