#!/usr/bin/env python3
"""Clone a GitHub repository at the revision recorded by the resource audit."""
from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="owner/name")
    parser.add_argument("--audit", default="resource_audit/checked_revisions.csv")
    parser.add_argument("--dest", default="external")
    args = parser.parse_args()

    rows = list(csv.DictReader(Path(args.audit).open(encoding="utf-8")))
    row = next((r for r in rows if r["Repo"].lower() == args.repo.lower()), None)
    if row is None:
        raise SystemExit(f"repository not found in audit: {args.repo}")
    if row["Status"] != "LOCKED" or not row["Checked_revision"]:
        raise SystemExit(f"no checked revision recorded for {args.repo}")

    sha = row["Checked_revision"]
    target = Path(args.dest) / args.repo.replace("/", "__")
    target.parent.mkdir(parents=True, exist_ok=True)

    if not target.exists():
        subprocess.run(["git", "clone", "--filter=blob:none", f"https://github.com/{args.repo}.git", str(target)], check=True)
    subprocess.run(["git", "-C", str(target), "fetch", "origin", sha], check=True)
    subprocess.run(["git", "-C", str(target), "checkout", "--detach", sha], check=True)
    print(f"{args.repo}\t{sha}\t{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
