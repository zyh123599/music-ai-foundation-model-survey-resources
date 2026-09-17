#!/usr/bin/env python3
"""Print simple release-status counts from the official-repository manifest."""

import csv
from collections import Counter
from pathlib import Path


def main() -> None:
    path = Path("repro/official_repos.csv")
    with path.open(newline="", encoding="utf-8") as f:
        status = Counter(row["Code_Status"] for row in csv.DictReader(f))

    print("Official GitHub repositories:", sum(status.values()))
    for key, value in status.most_common():
        print(f"{value:>3}  {key}")


if __name__ == "__main__":
    main()
