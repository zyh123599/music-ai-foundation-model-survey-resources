#!/usr/bin/env python3
"""Filter one of the resource CSV files."""

import argparse
import csv
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="CSV file to filter")
    parser.add_argument("--domain", help="case-insensitive substring match on Evidence_Domain")
    parser.add_argument("--year", type=int)
    parser.add_argument("--core", action="store_true", help="keep only Peer_Reviewed_CCF_Core == YES")
    args = parser.parse_args()

    with open(args.file, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fields = reader.fieldnames or []

    def keep(row: dict[str, str]) -> bool:
        if args.domain and args.domain.lower() not in (row.get("Evidence_Domain") or "").lower():
            return False
        if args.year and str(args.year) != (row.get("Year") or ""):
            return False
        if args.core and (row.get("Peer_Reviewed_CCF_Core") or "") != "YES":
            return False
        return True

    writer = csv.DictWriter(sys.stdout, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(row for row in rows if keep(row))


if __name__ == "__main__":
    main()
