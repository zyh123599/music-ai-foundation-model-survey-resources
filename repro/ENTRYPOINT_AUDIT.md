# Entrypoint audit

This file records what the official repository documents at the locked revision. It is not an execution log.

Status terms:

- `YES` — a concrete command is documented.
- `PATH` — the repository identifies an implementation path, but not one generic command.
- `NO` — no clear entry point was found in the checked README.
- `NOT_RUN` — the command has not been executed by this survey project.

Current pass: 14 of the 20 source-locked representative systems.

| System | Install | Inference | Evaluation | Run status |
|---|---|---|---|---|
| Muse | YES | YES | YES | NOT_RUN |
| YuE | YES | YES | YES | NOT_RUN |
| DiffRhythm 2 | YES | YES | NO | NOT_RUN |
| AudioX | YES | YES | NO | NOT_RUN |
| BeatEdit | YES | PATH | YES | NOT_RUN |
| CMI-Bench | YES | YES | YES | NOT_RUN |
| BEAT | YES | YES | NO | NOT_RUN |
| PHALAR | YES | YES | PATH | NOT_RUN |
| AudioSep | YES | YES | YES | NOT_RUN |
| SonicMaster | YES | NO | NO | NOT_RUN |
| LLM2Fx | NO | NO | NO | NOT_RUN |
| Jamendo-MT-QA | YES | YES | YES | NOT_RUN |
| MusicDET | YES | YES | YES | NOT_RUN |
| Instruct-MusicGen | YES | YES | YES | NOT_RUN |

The remaining source-locked systems will be added after their official entry points are checked. Runtime results are kept separate so that documentation coverage is not confused with successful reproduction.
