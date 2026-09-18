# Status fields

The files record what was checked at a particular date. They are not permanent statements about a project.

- `OFFICIAL_CODE_LOCKED` — an author or organization code/project URL was verified in the original source audit.
- `OFFICIAL_CODE_VERIFIED_2026-09-18` — an official code/project URL was verified during the later targeted resource pass.
- `NO_OFFICIAL_CODE_LOCATED...` — no official release was confirmed in the targeted search by the recorded audit date.
- `NOT_INDEXED` / blank release status — the resource field still needs a targeted check.
- `Weights` / `Weights_status` — notes on released model artifacts where they were checked.
- `Dataset_public` / `Data_access_status` — notes on whether relevant data are public, partial, licensed, restricted, or not yet verified.
- `Source_Checked_Date` / `Resource_checked` — date of the resource check.
- `Checked_revision` — Git commit observed during a dated repository check. This pins what was inspected; it does not mean the code was executed.
- `UNRESOLVED_AT_CHECK` — an earlier GitHub URL returned 404 during a later check. The historical entry is retained rather than silently removed.
- `DUPLICATE_CANDIDATE_REVIEW_BEFORE_CORPUS_CHANGE` — two corpus rows may refer to the same work; they remain untouched until manually reviewed.

A blank field means “not indexed here,” not “does not exist.”
