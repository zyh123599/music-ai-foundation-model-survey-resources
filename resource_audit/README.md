# Resource audit

This directory records which public resources were checked for the survey and when.

- `checked_revisions.csv` lists dated GitHub revisions that were inspected. A checked revision is not a claim that the code was run or reproduced.
- `resource_updates_2026-09-18.csv` records the 11 papers whose resource status was resolved after the original Phase-1 source lock.
- `repository_changes.csv` keeps links that were present in an earlier audit but could not be resolved at a later check.
- `coverage_by_year.csv` and `coverage_by_area.csv` summarize the current resource-index coverage.
- `duplicate_title_candidates.csv` keeps possible duplicate corpus entries for manual review; it does not remove papers automatically.

The main paper-to-resource table is `../resources/paper_resource_crosswalk.csv`. The task/model-side fields are under `../resources/technical/`.

The repository does not copy third-party model code, checkpoints, or datasets. Their own licenses and access terms still apply.
