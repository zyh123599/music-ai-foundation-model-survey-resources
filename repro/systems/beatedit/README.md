# BeatEdit

- Official repo: `Haoyu-Gu/BeatEdit-code`
- Locked revision: `dc5e6a869bcf464f33270eac035feda9b6f782eb`
- Checked: 2026-09-17

## Documented setup
`pip install -r requirements.txt` followed by `bash scripts/00_setup.sh`.

## Minimal entry point
Inference implementations are under `src/iteredit/inference/` and `src/tagfill/*/inference/`; the README does not give one universal inference command.

## Evaluation
`bash scripts/06_evaluate_all.sh` and `bash scripts/07_generate_tables.sh`.

The repository also documents a small CPU pilot configuration for checking the pipeline before GPU training.

## Runtime status
`NOT_TESTED`
