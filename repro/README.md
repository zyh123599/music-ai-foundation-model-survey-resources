# Reproduction layer

This directory tracks the official repositories used in the survey resource audit.

`official_repos.csv` contains 49 GitHub repositories associated with papers or project releases in the locked 2024–2026 source audit. The table keeps code, weights and data status separate because a public repository does not necessarily reproduce the training setup or the reported results.

## Fetch the repositories

```bash
python scripts/clone_official_repos.py --dest external
```

The script clones each official repository into `external/<owner>__<repo>/`. It does not copy those projects into this repository and does not change their licenses.

Use `--domain` to fetch one part of the survey at a time:

```bash
python scripts/clone_official_repos.py --domain "Generation" --dest external
```

## What we still want to record

The next pass will add an exact commit or release identifier for repositories used in reproducibility checks, plus a small smoke-test record for selected systems. A repository that cannot be installed or run will be reported as such; it will not be treated as evidence that the underlying scientific method failed.
