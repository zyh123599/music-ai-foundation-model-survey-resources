# Music AI Foundation Model Survey Resources

Resources collected while writing **Music Foundation Models: A Survey of Recent Developments, Evaluation, and Open Problems**.

This repository keeps paper links, official project pages, release status, datasets, benchmarks, and evaluation tools in one place. It does not mirror third-party model weights or datasets.

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

## Snapshot

The source audit used for this version was locked on **2026-09-07**.

- 120 papers reviewed from 2024–2026
- 77 peer-reviewed CCF A/B core papers in the main source audit
- 62 paper/project records with an official code or project URL in the locked database

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
| SongBloom | long-form song generation | https://github.com/tencent-ailab/SongBloom |
| Music Flamingo | music understanding | https://huggingface.co/nvidia/music-flamingo-2601-hf |
| AudioX | multimodal audio generation | https://github.com/ZeyueT/AudioX |
| LLM2Fx | music post-production | https://github.com/SonyResearch/LLM2Fx |

## Reproducibility note

A public repository and a reproducible paper are not the same thing. Code, checkpoints, and data are recorded separately because a release may support inference without making the original training run reproducible.

If a row says that no official code was located, read it as **not verified by the audit date**, not as proof that no release exists.

## Small helper scripts

```bash
python scripts/filter_resources.py resources/papers/reviewed_papers_2026.csv --core
python scripts/check_urls.py resources/models/generation.csv --column Resource_URL
```

They use only the Python standard library.

## Contributing

Corrections and newly released official links are welcome. Please use author or organization project pages when possible; see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License and third-party material

External papers, code, weights, and datasets keep their own licenses and terms. This repository only stores metadata and small helper scripts.

## Citation

A BibTeX entry will be added when the survey has a public archival identifier.
