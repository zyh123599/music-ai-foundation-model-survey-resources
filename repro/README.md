# Reproducibility checks

This directory tracks a representative subset of open systems from the survey. It separates four questions that are often collapsed into “open source”:

1. Is the official repository still reachable?
2. Can the software environment be installed?
3. Are the required checkpoints and data obtainable?
4. Does a minimal inference or evaluation command run at the locked source revision?

The first pass locks 20 repositories to exact commit SHAs. Runtime fields start as `NOT_TESTED`; they are updated only after a command has actually been run.

Files:

- `representative_source_locks.csv` — exact source revisions used by the audit.
- `reproduction_matrix.csv` — execution status for the selected systems.
- `repository_changes.csv` — URLs that changed or became unavailable after the earlier source audit.
- `systems/` — per-system notes and smoke-test entry points.

`NOT_TESTED` is intentionally different from `FAIL`. A failed install or inference attempt is recorded only after the corresponding command has been executed and its log retained.
