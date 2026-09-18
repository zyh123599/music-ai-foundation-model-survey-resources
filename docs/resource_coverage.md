# Resource coverage

These counts describe the companion resource index. They do not score model quality and they do not imply that linked code was executed.

The original source audit was locked on **2026-09-07**. Additional resource checks on **2026-09-17–18** resolved repository revisions and filled the release status for every corpus row.

## Current corpus status

| Status | Count |
|---|---:|
| reviewed corpus rows | 120 |
| checked public resource entry | 93 |
| targeted search found no official code | 26 |
| duplicate-title candidate | 1 |
| not indexed | 0 |

A checked resource can be code, a model release, a dataset, a benchmark, a challenge page, or an official project/demo page. The exact type is recorded in the crosswalk.

## By year

| Year | Papers | CCF A/B core | Checked resource | GitHub resource | No official code located | Duplicate candidate | Not indexed |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2024 | 10 | 4 | 9 | 6 | 1 | 0 | 0 |
| 2025 | 59 | 35 | 45 | 36 | 13 | 1 | 0 |
| 2026 | 51 | 38 | 39 | 30 | 12 | 0 | 0 |

## By area

| Area | Papers | CCF A/B core | Checked resource | GitHub resource | No official code located | Duplicate candidate | Not indexed |
|---|---:|---:|---:|---:|---:|---:|---:|
| Editing / control | 20 | 11 | 16 | 10 | 3 | 1 | 0 |
| Music understanding / Music-LM | 12 | 12 | 11 | 10 | 1 | 0 | 0 |
| Separation / restoration / production | 11 | 7 | 8 | 8 | 3 | 0 | 0 |
| Representation / codec | 15 | 7 | 13 | 10 | 2 | 0 | 0 |
| Evaluation / robustness | 17 | 14 | 14 | 10 | 3 | 0 | 0 |
| Symbolic | 8 | 3 | 4 | 4 | 4 | 0 | 0 |
| Generation | 16 | 10 | 11 | 9 | 5 | 0 | 0 |
| Multimodal | 12 | 11 | 9 | 6 | 3 | 0 | 0 |
| Singing / transcription / performance | 9 | 2 | 7 | 5 | 2 | 0 | 0 |

The 26 no-code rows are dated search results, not permanent claims that code does not exist. The duplicate candidate is kept in the corpus until the title/identity issue is manually resolved.

Machine-readable versions are in [`resource_audit/coverage_by_year.csv`](../resource_audit/coverage_by_year.csv) and [`resource_audit/coverage_by_area.csv`](../resource_audit/coverage_by_area.csv).
