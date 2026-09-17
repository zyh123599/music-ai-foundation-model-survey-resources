# Music AI Foundation Model Survey Resources

Resources collected while writing **Music Foundation Models: A Survey of Recent Developments, Evaluation, and Open Problems**.

The repository keeps paper links, official code/project pages, model-release status, datasets, benchmarks, and evaluation tools in one place. It does not mirror third-party model weights or datasets.

## Contents

- [`resources/reviewed_papers.csv`](resources/reviewed_papers.csv) — 120 papers in the 2024–2026 review corpus
- [`resources/models_and_code.csv`](resources/models_and_code.csv) — official code/project links and release status
- [`resources/datasets.csv`](resources/datasets.csv) — datasets used across current Music AI research
- [`resources/benchmarks.csv`](resources/benchmarks.csv) — benchmark releases covered by the survey
- [`resources/evaluation_tools.csv`](resources/evaluation_tools.csv) — shared evaluation tools
- [`docs/models.md`](docs/models.md) — readable model/code index
- [`docs/datasets.md`](docs/datasets.md) — readable dataset index
- [`docs/benchmarks.md`](docs/benchmarks.md) — readable benchmark index
- [`docs/evaluation.md`](docs/evaluation.md) — evaluation tools
- [`docs/status.md`](docs/status.md) — meaning of the release/status fields

## Snapshot

The source audit used for this version was locked on **2026-09-07**.

- 120 papers reviewed from 2024–2026
- 77 peer-reviewed CCF A/B core papers in the main source audit
- 62 paper/project records with an official code or project URL in the locked database

The numbers are a dated snapshot. Projects may release code, weights, or data after the audit date.

## Quick links

| Project | Area | Official resource |
|---|---|---|
| Muse | long-form song generation | https://github.com/yuhui1038/Muse |
| SonicMaster | restoration / mastering | https://github.com/AMAAI-Lab/SonicMaster |
| BEAT | symbolic tokenization / generation | https://github.com/Lekai-Qian/BEAT-code |
| BeatEdit | symbolic editing | https://github.com/Haoyu-Gu/BeatEdit-code |
| PHALAR | music representation learning | https://github.com/gladia-research-group/phalar |
| YuE | long-form music generation | https://github.com/multimodal-art-projection/YuE |
| SongBloom | long-form song generation | https://github.com/tencent-ailab/SongBloom |
| Instruct-MusicGen | text-guided music editing | https://github.com/ldzhangyx/instruct-MusicGen |
| AudioX | multimodal audio generation | https://github.com/ZeyueT/AudioX |

## Notes on reproducibility

A public repository and a reproducible paper are not the same thing. The registries keep code, weights, and data as separate fields. Some releases support exact inference but not original-data training; some datasets provide annotations while the audio has to be obtained separately.

If a row says that no official code was located, read it as “not verified by the audit date,” not as proof that no release exists.

## Scripts

```bash
python scripts/filter_resources.py --help
python scripts/check_urls.py --help
```

The scripts only work on the small metadata files in this repository.

## License and third-party material

External papers, code, weights, and datasets keep their own licenses and terms. This repository only stores metadata and small helper scripts.

## Citation

A BibTeX entry will be added when the survey has a public archival identifier.
