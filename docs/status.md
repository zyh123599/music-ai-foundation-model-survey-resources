# Status fields

The files record what was checked at a particular date. They are not permanent statements about a project.

- `OFFICIAL_CODE_LOCKED` — an author or organization code/project URL was verified in the source audit.
- `NO_OFFICIAL_CODE_LOCATED...` — no official release was confirmed in the targeted search by the audit date.
- `Weights` — notes on released model artifacts where they were checked.
- `Dataset_public` — notes on whether relevant data are public, partial, licensed, or unavailable.
- `Source_Checked_Date` — date of the resource check.
- `Checked_revision` — Git commit observed during the later GitHub link check. This pins what was inspected; it does not mean the code was executed.
- `UNRESOLVED_AT_CHECK` — an earlier GitHub URL returned 404 during the later check. The historical entry is retained rather than silently removed.

A blank field means “not indexed here,” not “does not exist.”
