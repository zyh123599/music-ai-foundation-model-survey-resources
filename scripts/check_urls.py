#!/usr/bin/env python3
"""Check HTTP links in a resource CSV file."""

import argparse
import csv
import urllib.error
import urllib.request


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="CSV file to check")
    parser.add_argument("--column", default=None, help="URL column; auto-detected when omitted")
    parser.add_argument("--timeout", type=float, default=12.0)
    args = parser.parse_args()

    with open(args.file, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    if not rows:
        return

    column = args.column
    if column is None:
        for candidate in ("Resource_URL", "URL", "Official_URL", "Official_Code_URL", "Exact_Paper_URL"):
            if candidate in rows[0]:
                column = candidate
                break
    if column is None:
        raise SystemExit("No URL column found. Pass --column explicitly.")

    for row in rows:
        url = (row.get(column) or "").strip()
        if not url.startswith(("http://", "https://")):
            continue
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "music-ai-survey-resource-checker"})
        try:
            with urllib.request.urlopen(request, timeout=args.timeout) as response:
                print(response.status, url)
        except urllib.error.HTTPError as exc:
            print(exc.code, url)
        except Exception as exc:
            print("ERR", url, type(exc).__name__)


if __name__ == "__main__":
    main()
