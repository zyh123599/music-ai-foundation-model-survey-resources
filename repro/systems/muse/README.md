# Muse

- Official repo: `yuhui1038/Muse`
- Locked revision: `dbc22f83eac3e3e3a6bd44eba2e1c774588c5ff1`
- Checked: 2026-09-17

## Documented setup
`pip install vllm` plus the MuCodec and evaluation requirements listed in the official README.

## Minimal entry point
`python infer/batch_multi_generate.py --input_path infer/test.jsonl --output_dir <out> --ckpt_dir <Muse-0.6b> --repetition_penalty 1.1 --batch_size 8`

## Evaluation
The repository includes `eval_pipeline/` and separate evaluation dependencies.

## Runtime status
`NOT_TESTED`
