# Reproduction runbook

The repository keeps documentation checks and runtime checks separate.

## 1. Lock the source revision

Use `repro/representative_source_locks.csv`. Each selected repository has a commit SHA recorded on 2026-09-17.

```bash
python scripts/checkout_locked_repo.py yuhui1038/Muse
```

This checks out the exact revision instead of the current moving default branch.

## 2. Read the documented entry point

`repro/entrypoint_audit.csv` records the install, inference, and evaluation commands that were present in the official repository at the locked revision.

A documented command is not counted as a successful run.

## 3. Record runtime stages separately

Update `repro/reproduction_matrix.csv` only after the corresponding step is attempted:

- `Code_Clone`
- `Environment_Setup`
- `Checkpoint_Access`
- `Minimal_Inference`
- `Evaluation_Entry_Point`
- `Dataset_Access`
- `Paper_Metric_Reproduction`

Use `PASS`, `FAIL`, `PARTIAL`, `BLOCKED`, or `NOT_TESTED`. Keep the raw log for failed and partial runs.

## 4. Do not turn setup failures into model claims

A broken dependency, missing checkpoint, or inaccessible dataset is a reproducibility result. It is not evidence that the model itself fails scientifically.

## 5. Minimum smoke test

The first execution pass stops after a minimal valid output or benchmark prediction is produced. Full paper-metric reproduction is a later and more expensive stage.
