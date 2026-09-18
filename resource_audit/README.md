# Resource audit

This directory records which public resources were checked for the survey and when.

The original Phase-1 source lock is dated **2026-09-07**. GitHub revisions and later release checks were added on **2026-09-17–18**. The dated update files are kept instead of rewriting the history of the original audit.

## Files

- `checked_revisions.csv` — GitHub revisions inspected during the resource checks. A revision lock is not a claim that the code was run.
- `repository_changes.csv` — links that were present in an earlier audit but stopped resolving later.
- `resource_updates_2026-09-18*.csv` — successive batches that filled previously unresolved resource fields.
- `no_official_code_after_search_2026-09-18.csv` — final targeted searches that did not locate official code.
- `coverage_by_year.csv` and `coverage_by_area.csv` — current coverage counts.
- `duplicate_title_candidates.csv` — possible duplicate corpus entries held for manual review.
- `title_corrections.csv` — canonical-title corrections kept separate from the stable corpus join key.

## Current state

All 120 corpus rows now have a resource status:

- 93 have a checked public resource entry;
- 26 have a dated targeted-search result with no official code located;
- 1 is a duplicate-title candidate;
- 0 remain unindexed.

The main paper-to-resource table is [`../resources/paper_resource_crosswalk.csv`](../resources/paper_resource_crosswalk.csv). Task, architecture, input/output, parameter-count and dataset fields are under [`../resources/technical/`](../resources/technical/).

Third-party code, checkpoints and datasets are not copied into this repository. Their own licenses and access terms apply.
