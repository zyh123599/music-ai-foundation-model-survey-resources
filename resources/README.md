# Resource files

The corpus and resource tables are kept as small CSV files so they are easy to inspect and update.

## Main crosswalk

`paper_resource_crosswalk.csv` has one row for each of the **119 unique works** in the public corpus. It records the paper URL, primary public resource, resource type, code status, checkpoint notes, data-access notes, benchmark flag and checked revision when available.

Every row has a resource status.

## Technical crosswalk

The files under `technical/` keep the task and model-side fields recorded during the source audit:

- `technical/paper_technical_crosswalk_2024.csv` — 10 works
- `technical/paper_technical_crosswalk_2025.csv` — 58 works
- `technical/paper_technical_crosswalk_2026.csv` — 51 works

Together they contain 119 unique works and cover task, input, output, architecture, parameter count, dataset and public-resource fields.

## Reviewed papers

- `papers/reviewed_papers_2024.csv`
- `papers/reviewed_papers_2025.csv`
- `papers/reviewed_papers_2026.csv`

## Models and project resources

The detailed resource registry is split by area under `models/`:

- `editing_control.csv`
- `evaluation_robustness.csv`
- `generation.csv`
- `multimodal.csv`
- `music_understanding_music_lm.csv`
- `representation_codec.csv`
- `separation_restoration_production.csv`
- `singing_transcription_performance.csv`
- `symbolic.csv`

## Other registries

- `datasets.csv`
- `benchmarks.csv`
- `evaluation_tools.csv`

Resource checks are dated. “No official code located” means no release was verified in that search, not that a release cannot exist.
