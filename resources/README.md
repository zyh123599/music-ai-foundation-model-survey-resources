# Resource files

The paper corpus and resource registries are split into small CSV files so they are easy to inspect and update.

## Main crosswalk

- `paper_resource_crosswalk.csv` joins all 120 reviewed papers with the resource audit: official code/project link, release status, checkpoint notes, data notes, benchmark flag, and checked Git revision when available.

## Technical crosswalk

The files under `technical/` keep the task and model-side fields recorded during the source audit:

- `technical/paper_technical_crosswalk_2024.csv`
- `technical/paper_technical_crosswalk_2025.csv`
- `technical/paper_technical_crosswalk_2026.csv`

Together they contain 120 rows. They include task, input, output, model architecture, parameter count, dataset, benchmark flag, code/project link, checkpoint notes, data-access notes, and checked revision when applicable.

## Reviewed papers

- `papers/reviewed_papers_2024.csv`
- `papers/reviewed_papers_2025.csv`
- `papers/reviewed_papers_2026.csv`

Together they contain the 120-paper 2024–2026 review corpus used by the survey.

## Models and official project links

The detailed resource registry is split by area under `models/`:

- `editing_control.csv`
- `evaluation_robustness.csv`
- `generation.csv`
- `multimodal.csv`
- `music_understanding_music_lm.csv`
- `representation_codec.csv`
- `separation_restoration_production.csv`
- `singing_transcription_performance.csv`

These files keep the longer checkpoint and data notes that would make the main crosswalk unwieldy.

## Other registries

- `datasets.csv`
- `benchmarks.csv`
- `evaluation_tools.csv`

The audit date is stored in the rows. A missing release should be read as “not verified by that date,” not as proof that a release does not exist.
