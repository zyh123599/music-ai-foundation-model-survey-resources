# Resource audit

This directory records which public resources were checked for the survey and when.

- `checked_revisions.csv` lists the GitHub revision seen during the 2026-09-17 link check. It is a dated reference, not a claim that the code was reproduced.
- `repository_changes.csv` keeps links that were present in the earlier audit but could not be resolved at the later check.
- `coverage_by_year.csv` and `coverage_by_area.csv` summarize how many papers have a checked release entry, a GitHub resource, a targeted no-code result, or an unfilled release field.

The main paper-to-resource table is `../resources/paper_resource_crosswalk.csv`. The task/model-side fields are under `../resources/technical/`.

The repository does not copy third-party model code, checkpoints, or datasets. Their own licenses and access terms still apply.
