# Music AI Foundation Model Survey Resources

Companion resources for **Music Foundation Models: A Survey of Recent Developments, Evaluation, and Open Problems**.

The repository keeps the paper corpus and the public resources that were checked while writing the survey. The aim is simple: make it easy to move from a paper to its code, model release, dataset, benchmark, demo, or project page without hiding uncertainty behind a single “open source” label.

## At a glance

| Item | Count |
|---|---:|
| unique works in the 2024–2026 review corpus | 119 |
| peer-reviewed CCF A/B core papers | 77 |
| works with a checked public resource | 93 |
| targeted searches with no official code located | 26 |
| primary resource entries pointing to GitHub | 72 |
| concrete Git revisions recorded | 71 |
| older GitHub links unresolved at later check | 2 |
| dataset entries | 11 |
| benchmark entries | 10 |
| shared evaluation-tool entries | 5 |

The initial Phase-1 database contained 120 rows. A later source check found that **Affective and Controllable Symbolic Music Performance** and **SyMuPe: Affective and Controllable Symbolic Music Performance** were the same ACM MM 2025 paper, so the public corpus now contains **119 unique works**. The correction is recorded in [`resource_audit/corpus_corrections.csv`](resource_audit/corpus_corrections.csv).

Every remaining corpus row has a resource status. There are no `NOT_INDEXED` rows.

The Phase-1 source audit was locked on **2026-09-07**. Repository links and later releases were checked again on **2026-09-17–18**.

## Start here

- [`resources/paper_resource_crosswalk.csv`](resources/paper_resource_crosswalk.csv) — all 119 works with code/project/model/data status
- [`resources/technical/`](resources/technical/) — task, input/output, architecture, parameter count and dataset fields
- [`resources/papers/`](resources/papers/) — review corpus split by year
- [`resources/models/`](resources/models/) — resource records split by area
- [`resources/datasets.csv`](resources/datasets.csv) — datasets
- [`resources/benchmarks.csv`](resources/benchmarks.csv) — benchmarks
- [`resources/evaluation_tools.csv`](resources/evaluation_tools.csv) — shared evaluation tools
- [`resource_audit/AUDIT_STATUS.md`](resource_audit/AUDIT_STATUS.md) — current audit totals
- [`resource_audit/checked_revisions.csv`](resource_audit/checked_revisions.csv) — dated Git revisions
- [`resource_audit/no_official_code_after_search_2026-09-18.csv`](resource_audit/no_official_code_after_search_2026-09-18.csv) — final targeted no-code searches
- [`docs/resource_coverage.md`](docs/resource_coverage.md) — coverage by year and area
- [`docs/status.md`](docs/status.md) — field meanings

## What the status means

Code, checkpoints, data, benchmarks and project pages are recorded separately. A paper with a demo page but no verified code is not marked as an open-source implementation. An empty official repository is also kept distinct from a released implementation.

Likewise, “no official code located” is a dated search result. It does not mean that code can never appear later.

The Git revision field records the version inspected during the resource check. It is not a reproduction claim.

## Repository layout

```text
resources/
  papers/
  models/
  technical/
  paper_resource_crosswalk.csv
  datasets.csv
  benchmarks.csv
  evaluation_tools.csv

resource_audit/
  AUDIT_STATUS.md
  corpus_corrections.csv
  checked_revisions.csv
  repository_changes.csv
  resource_updates_2026-09-18*.csv
  no_official_code_after_search_2026-09-18.csv
  duplicate_title_candidates.csv
  title_corrections.csv
  coverage_by_year.csv
  coverage_by_area.csv

docs/
  models.md
  datasets.md
  benchmarks.md
  evaluation.md
  resource_crosswalk.md
  technical_crosswalk.md
  resource_coverage.md
  status.md

scripts/
  check_urls.py
  filter_resources.py
  summarize_releases.py
  summarize_technical_crosswalk.py
  clone_official_repos.py
  checkout_checked_revision.py
```

## Small helper scripts

The scripts operate on metadata or fetch upstream repositories. They do not install models or download checkpoints.

```bash
python scripts/filter_resources.py resources/papers/reviewed_papers_2026.csv --core
python scripts/check_urls.py resources/models/generation.csv --column Resource_URL
python scripts/summarize_technical_crosswalk.py
python scripts/clone_official_repos.py --dest external
python scripts/checkout_checked_revision.py yuhui1038/Muse
```

## Corrections

Corrections and newly released official links are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Third-party material

Papers, code, model weights, datasets and demos linked here keep their own licenses and terms. This repository stores metadata and small helper scripts; it does not mirror third-party assets.

## Citation

A BibTeX entry will be added when the survey has a public archival identifier.
