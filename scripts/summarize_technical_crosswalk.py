#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = sorted((root / "resources" / "technical").glob("paper_technical_crosswalk_*.csv"))

rows = []
for path in files:
    with path.open(encoding="utf-8", newline="") as f:
        rows.extend(csv.DictReader(f))

print(f"papers\t{len(rows)}")
print(f"ccf_ab_core\t{sum(r['CCF_AB_core'] == 'YES' for r in rows)}")
print(f"checked_release_entry\t{sum(r['Release_status'] not in {'not indexed', 'no official code located in targeted search'} for r in rows)}")
print(f"github_resource\t{sum('github.com' in r['Official_code_or_project_URL'] for r in rows)}")
print(f"benchmark_registry\t{sum(r['Benchmark_registry'] == 'YES' for r in rows)}")

print("\nby area")
for area, n in Counter(r["Area"] for r in rows).most_common():
    print(f"{area}\t{n}")
