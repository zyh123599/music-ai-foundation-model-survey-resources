# Reproducibility status

Checked on 2026-09-17.

## Source snapshot

- 49 GitHub repository links were present in the earlier source audit.
- 47 are currently reachable and pinned to exact commit SHAs.
- 2 older URLs currently return 404 and remain listed as unresolved rather than being removed.

See `all_repo_source_locks.csv` and `repository_changes.csv`.

## Representative subset

20 systems were selected for deeper checks across generation, editing, representation, understanding, evaluation, separation/restoration, and production.

Documentation found at the locked revisions:

- installation entry point: **17 / 20**
- inference or runnable model/benchmark entry point: **16 / 20**
- evaluation command or explicit evaluation implementation path: **11 / 20**

See `ENTRYPOINT_AUDIT.md` for the per-system result and `entrypoint_audit.csv` for the exact commands.

## Runtime status

No system is marked `PASS` merely because its README contains a command. Runtime stages in `reproduction_matrix.csv` remain `NOT_TESTED` until they are actually executed.

The next pass is minimal execution: clone the locked revision, install the documented environment, obtain the required checkpoint/data if permitted, and produce one valid output or benchmark prediction. Full paper-metric reproduction comes later.
