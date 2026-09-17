# AudioSep

- Official repo: `Audio-AGI/AudioSep`
- Locked revision: `944583f18b84589dc965de3ad77525c945334252`
- Checked: 2026-09-17

## Documented setup
`conda env create -f environment.yml` and `conda activate AudioSep`; official checkpoint path is documented.

## Minimal entry point
The README shows `pipeline.build_audiosep(...)` followed by `pipeline.inference(...)` for text-conditioned separation.

## Evaluation
`python benchmark.py --checkpoint_path audiosep_base_4M_steps.ckpt`

## Runtime status
`NOT_TESTED`
