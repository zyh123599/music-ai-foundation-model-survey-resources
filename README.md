# Music AI Foundation Model Survey Resources

Companion resources for **Music Foundation Models: A Survey of Recent Developments, Evaluation, and Open Problems**.

This repository is the resource index behind the survey. It is mainly for answering practical questions: which papers have an official release, where the code or project page is, whether checkpoints or data were found, which benchmark belongs to which paper, and when a link was last checked.

## At a glance

| Item | Count |
|---|---:|
| papers in the 2024–2026 review corpus | 120 |
| peer-reviewed CCF A/B core papers | 77 |
| paper/project records with a checked resource entry | 62 |
| GitHub repositories in the resource audit | 49 |
| GitHub revisions resolved on 2026-09-17 | 47 |
| GitHub links unresolved on that check | 2 |
| dataset entries | 10 |
| benchmark entries | 10 |
| shared evaluation-tool entries | 5 |

The counts are a dated snapshot. New releases after the audit date may not be included yet.

## Start here

- [`resources/paper_resource_crosswalk.csv`](resources/paper_resource_crosswalk.csv) — 120-paper paper/resource crosswalk
- [`resources/papers/`](resources/papers/) — reviewed papers split by year
- [`resources/models/`](resources/models/) — detailed model/code records split by area
- [`resources/datasets.csv`](resources/datasets.csv) — datasets
- [`resources/benchmarks.csv`](resources/benchmarks.csv) — benchmark releases
- [`resources/evaluation_tools.csv`](resources/evaluation_tools.csv) — shared evaluation tools
- [`resource_audit/checked_revisions.csv`](resource_audit/checked_revisions.csv) — dated GitHub revisions
- [`resource_audit/repository_changes.csv`](resource_audit/repository_changes.csv) — links that changed or stopped resolving
- [`docs/resource_crosswalk.md`](docs/resource_crosswalk.md) — how to read the crosswalk
- [`docs/status.md`](docs/status.md) — field meanings

## What “checked” means

The main source audit was locked on **2026-09-07**. GitHub repository reachability and revisions were checked again on **2026-09-17**.

A public repository, a released checkpoint, and public training data are separate things, so the tables keep them separate. If a row says that no official code was located, that means no release was verified in the targeted search by the audit date. It is not proof that no release exists.

The checked Git revision is only a record of what was inspected. We do not claim that those repositories were installed or reproduced.

## Repository layout

```text
resources/
  papers/
  models/
  paper_resource_crosswalk.csv
  datasets.csv
  benchmarks.csv
  evaluation_tools.csv
resource_audit/
  checked_revisions.csv
  repository_changes.csv
docs/
  models.md
  datasets.md
  benchmarks.md
  evaluation.md
  resource_crosswalk.md
  status.md
scripts/
  check_urls.py
  filter_resources.py
  summarize_releases.py
  clone_official_repos.py
  checkout_checked_revision.py
```

## Helper scripts

The scripts work on metadata or fetch official repositories. They do not install models or download checkpoints.

```bash
python scripts/filter_resources.py resources/papers/reviewed_papers_2026.csv --core
python scripts/check_urls.py resources/models/generation.csv --column Resource_URL
python scripts/summarize_releases.py
python scripts/clone_official_repos.py --dest external
python scripts/checkout_checked_revision.py yuhui1038/Muse
```

## Corrections

Corrections and newly released official links are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Third-party material

Papers, code, model weights, datasets, and demos linked here keep their own licenses and terms. This repository stores metadata and small helper scripts; it does not mirror those third-party assets.

## Citation

A BibTeX entry will be added when the survey has a public archival identifier.
