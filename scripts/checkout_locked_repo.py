#!/usr/bin/env python3
"""Clone one source-locked repository and check out the audited revision."""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path


def slug(repo: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "__", repo)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="owner/name from repro/representative_source_locks.csv")
    parser.add_argument("--locks", default="repro/representative_source_locks.csv")
    parser.add_argument("--dest", default="external")
    args = parser.parse_args()

    rows = list(csv.DictReader(Path(args.locks).open(encoding="utf-8")))
    row = next((r for r in rows if r["Repo"] == args.repo), None)
    if row is None:
        raise SystemExit(f"repo not found in source locks: {args.repo}")

    dest = Path(args.dest) / slug(args.repo)
    sha = row["Locked_SHA"]
    url = f"https://github.com/{args.repo}.git"

    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--filter=blob:none", url, str(dest)], check=True)

    subprocess.run(["git", "-C", str(dest), "fetch", "origin", sha], check=True)
    subprocess.run(["git", "-C", str(dest), "checkout", "--detach", sha], check=True)
    head = subprocess.check_output(["git", "-C", str(dest), "rev-parse", "HEAD"], text=True).strip()
    if head != sha:
        raise SystemExit(f"checkout mismatch: expected {sha}, got {head}")

    print(f"checked out {args.repo} at {sha}")
    print(f"path: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
