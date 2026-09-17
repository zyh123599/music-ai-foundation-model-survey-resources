# Status fields

The registry records what was verified at a particular date. It is not a permanent statement about a project.

- `OFFICIAL_CODE_LOCKED` — an author or organization project/repository URL was verified.
- `NO_OFFICIAL_CODE_LOCATED...` — no official release was confirmed in the targeted search by the audit date.
- `Weights` — whether pretrained model artifacts were found and what part of the stack they cover.
- `Dataset_public` — whether the relevant training or evaluation data are public, partial, licensed, or unavailable.
- `Source_Checked_Date` — date used for the resource check.

For reproduction work, check the exact checkpoint, tokenizer or codec, data version, preprocessing, package versions, and metric implementation. A paper may be reproducible at inference time without being reproducible at training time.
