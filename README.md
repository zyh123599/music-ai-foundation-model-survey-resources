# Music AI Foundation Model Survey Resources

Resources collected while writing **Music Foundation Models: A Survey of Recent Developments, Evaluation, and Open Problems**.

This repository keeps paper links, official project pages, release status, datasets, benchmarks, evaluation tools, and reproducibility notes in one place. It does not mirror third-party model weights or datasets.

## What is here

### Review corpus

The 120-paper 2024–2026 corpus is split by year:

- [`resources/papers/reviewed_papers_2024.csv`](resources/papers/reviewed_papers_2024.csv)
- [`resources/papers/reviewed_papers_2025.csv`](resources/papers/reviewed_papers_2025.csv)
- [`resources/papers/reviewed_papers_2026.csv`](resources/papers/reviewed_papers_2026.csv)

### Models and official code/project links

The detailed registry is split by area under [`resources/models/`](resources/models/). A shorter readable index is in [`docs/models.md`](docs/models.md).

### Datasets, benchmarks, and evaluation

- [`resources/datasets.csv`](resources/datasets.csv) and [`docs/datasets.md`](docs/datasets.md)
- [`resources/benchmarks.csv`](resources/benchmarks.csv) and [`docs/benchmarks.md`](docs/benchmarks.md)
- [`resources/evaluation_tools.csv`](resources/evaluation_tools.csv) and [`docs/evaluation.md`](docs/evaluation.md)
- [`docs/status.md`](docs/status.md) explains the release/status fields

### Official repositories and reproducibility checks

The source audit contains 49 GitHub repositories associated with papers or project releases. They are listed in [`repro/official_repos.csv`](repro/official_repos.csv).

A representative set of 20 systems is pinned to exact revisions in [`repro/representative_source_locks.csv`](repro/representative_source_locks.csv). The current execution matrix is in [`repro/reproduction_matrix.csv`](repro/reproduction_matrix.csv).

All 20 source-locked systems have been checked for documented installation, inference, and evaluation entry points. The compact result is in [`repro/ENTRYPOINT_AUDIT.md`](repro/ENTRYPOINT_AUDIT.md); exact commands and notes are in [`repro/entrypoint_audit.csv`](repro/entrypoint_audit.csv). Each system also has a short page under [`repro/systems/`](repro/systems/).

Runtime fields remain `NOT_TESTED` until a command has actually been executed. A missing or changed repository URL is recorded separately in [`repro/repository_changes.csv`](repro/repository_changes.csv).

To fetch the audited repositories without copying third-party code into this repository:

```bash
python scripts/clone_official_repos.py --dest external
```

For a source-locked system, use the exact-revision helper instead of the moving default branch:

```bash
python scripts/checkout_locked_repo.py yuhui1038/Muse
```

The execution procedure is documented in [`repro/RUNBOOK.md`](repro/RUNBOOK.md).

## Snapshot

The main source audit used for this version was locked on **2026-09-07**. Repository reachability and source locks were checked again on **2026-09-17**.

- 120 papers reviewed from 2024–2026
- 77 peer-reviewed CCF A/B core papers in the main source audit
- 62 paper/project records with an official code or project URL in the locked database
- 49 records point to GitHub repositories
- 20 representative repositories pinned to exact commit SHAs
- 20/20 representative systems checked for documented install/inference/evaluation entry points

These numbers are a dated snapshot. Projects may release code, weights, or data after the audit date.

## A few useful starting points

| Project | Area | Official resource |
|---|---|---|
| Muse | long-form song generation / control | https://github.com/yuhui1038/Muse |
| SonicMaster | restoration / mastering | https://github.com/AMAAI-Lab/SonicMaster |
| BEAT | symbolic tokenization / generation | https://github.com/Lekai-Qian/BEAT-code |
| BeatEdit | symbolic editing | https://github.com/Haoyu-Gu/BeatEdit-code |
| PHALAR | music representation learning | https://github.com/gladia-research-group/phalar |
| YuE | long-form music generation | https://github.com/multimodal-art-projection/YuE |
| MusicDET | generated-music detection | https://github.com/Chaolei98/MusicDET |
| CMI-Bench | music instruction-following evaluation | https://github.com/nicolaus625/CMI-bench |
| AudioX | multimodal audio generation | https://github.com/ZeyueT/AudioX |
| LLM2Fx | music post-production | https://github.com/SonyResearch/LLM2Fx |

## Reproducibility note

A public repository and a reproducible paper are not the same thing. Code, checkpoints, data, documented entry points, and successful runtime checks are tracked separately.

If a row says that no official code was located, read it as **not verified by the audit date**, not as proof that no release exists. `NOT_TESTED` is also not a failure; it means the corresponding command has not yet been run in this project.

## Small helper scripts

```bash
python scripts/filter_resources.py resources/papers/reviewed_papers_2026.csv --core
python scripts/check_urls.py resources/models/generation.csv --column Resource_URL
python scripts/summarize_releases.py
python repro/verify_source_locks.py
python scripts/checkout_locked_repo.py yuhui1038/Muse
```

They use only the Python standard library.

## Contributing

Corrections and newly released official links are welcome. Please use author or organization project pages when possible; see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License and third-party material

External papers, code, weights, and datasets keep their own licenses and terms. This repository only stores metadata and small helper scripts.

## Citation

A BibTeX entry will be added when the survey has a public archival identifier.
