# Status fields

The files record what was checked at a particular date. They are not permanent statements about a project.

- `OFFICIAL_CODE_LOCKED` — an author or organization code/project URL was verified in the original source audit.
- `OFFICIAL_CODE_VERIFIED_2026-09-18` — an official code repository was verified during the later targeted resource pass.
- `OFFICIAL_MODEL_RELEASE_VERIFIED_2026-09-18` — an official model release was verified without treating it as a code release.
- `OFFICIAL_DATASET_REPO_VERIFIED_2026-09-18` — an official dataset repository was verified.
- `OFFICIAL_BENCHMARK_DATASET_VERIFIED_2026-09-18` — an official benchmark dataset was verified.
- `OFFICIAL_EMPTY_REPOSITORY_VERIFIED_2026-09-18` — an official repository exists, but it had no code/content at the check date.
- `PROJECT_PAGE_VERIFIED_NO_OFFICIAL_CODE_LINK_2026-09-18` — an official project/demo page was verified, but no code link was found there or in the targeted search.
- `NO_OFFICIAL_CODE_LOCATED_AFTER_TARGETED_SEARCH_YYYY-MM-DD` — no official code release was confirmed in the targeted search by that date.
- `DUPLICATE_CANDIDATE_SEE_SYMUPE` — this corpus row may refer to the same paper as the SyMuPe row and is held for manual review.
- `UNRESOLVED_AT_CHECK` — a previously indexed GitHub URL stopped resolving during a later link check.

Other fields:

- `Weights` / `Weights_status` — notes on released model artifacts where they were checked.
- `Dataset_public` / `Data_access_status` — notes on whether relevant data are public, partial, licensed, restricted, or not yet verified.
- `Source_Checked_Date` / `Resource_checked` — date of the resource check.
- `Checked_revision` — Git commit observed during a dated repository check. It records what was inspected; it does not mean the code was executed.

There are currently no `NOT_INDEXED` rows in the 120-row resource crosswalk.
