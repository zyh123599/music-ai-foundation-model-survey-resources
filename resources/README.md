# Resource files

The paper corpus and model/code registries are split into smaller CSV files so they are easier to inspect and update.

## Reviewed papers

- `papers/reviewed_papers_2024.csv`
- `papers/reviewed_papers_2025.csv`
- `papers/reviewed_papers_2026.csv`

Together they contain the 120-paper 2024–2026 review corpus used by the survey.

## Models and official project links

The code/resource registry is split by evidence domain under `models/`:

- `editing_control.csv`
- `evaluation_robustness.csv`
- `generation.csv`
- `multimodal.csv`
- `music_understanding_music_lm.csv`
- `representation_codec.csv`
- `separation_restoration_production.csv`
- `singing_transcription_performance.csv`

These files record the official project or repository URL found during the source audit, along with the checkpoint/data status that was verified at the time.

## Other registries

- `datasets.csv`
- `benchmarks.csv`
- `evaluation_tools.csv`

The audit date is stored in the CSV rows. A missing release should be read as “not verified by that date,” not as proof that a release does not exist.
