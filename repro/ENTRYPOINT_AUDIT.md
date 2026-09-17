# Entrypoint audit

This file records what the official repository documents at the locked revision. It is not an execution log.

Status terms:

- `YES` — a concrete command is documented.
- `PATH` — the repository identifies an implementation path, but not one generic command.
- `NO` — no clear entry point was found in the checked repository documentation.
- `NOT_RUN` — the command has not been executed by this survey project.

Current pass: **20 of 20** source-locked representative systems.

| System | Install | Inference | Evaluation | Run status |
|---|---|---|---|---|
| Muse | YES | YES | YES | NOT_RUN |
| YuE | YES | YES | YES | NOT_RUN |
| DiffRhythm 2 | YES | YES | NO | NOT_RUN |
| AudioX | YES | YES | NO | NOT_RUN |
| BeatEdit | YES | PATH | YES | NOT_RUN |
| MusicMagus | YES | YES | NO | NOT_RUN |
| CMI-Bench | YES | YES | YES | NOT_RUN |
| DeepResonance | YES | YES | NO | NOT_RUN |
| MCR-BENCH | NO | NO | NO | NOT_RUN |
| WildScore | YES | YES | YES | NOT_RUN |
| Jamendo-MT-QA | YES | YES | YES | NOT_RUN |
| BEAT | YES | YES | NO | NOT_RUN |
| PHALAR | YES | YES | PATH | NOT_RUN |
| ALMTokenizer | NO | NO | NO | NOT_RUN |
| AudioSep | YES | YES | YES | NOT_RUN |
| SonicMaster | YES | NO | NO | NOT_RUN |
| LLM2Fx | NO | NO | NO | NOT_RUN |
| MusicDET | YES | YES | YES | NOT_RUN |
| CMI-RewardBench | YES | YES | YES | NOT_RUN |
| Instruct-MusicGen | YES | YES | YES | NOT_RUN |

A few differences are worth keeping explicit. MCR-BENCH releases the benchmark data but states that it does not provide one evaluation implementation because the evaluated audio-language models require different environments. ALMTokenizer's checked repository revision contains the paper page and audio demos but no runnable setup instructions. SonicMaster documents training while the checked README does not expose a standalone inference command. LLM2Fx links the papers, demos, and datasets but does not give a runnable setup path in the checked README.

The detailed commands and notes are in `entrypoint_audit.csv`. Runtime results are kept separately in `reproduction_matrix.csv` so that documentation coverage is not confused with successful reproduction.
