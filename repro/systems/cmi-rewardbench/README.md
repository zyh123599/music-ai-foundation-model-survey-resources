# CMI-RewardBench

- Official repo: `Haiwen-Xia/CMI-RewardBench`
- Locked revision: `9235ef5c34106b63669958adfaa2eab61bd0e2cd`
- Checked: 2026-09-17

## Documented setup
`pip install -r requirements.txt`; baseline inference additionally uses `baselines/requirements.txt`.

## Minimal entry point
`python inference_benchmark.py -c baselines/model/model.safetensors --dataset_jsonl data/all_test.jsonl --dataset_root data/ --device cuda:0`

## Evaluation
The benchmark runner invokes `evaluate_results.py` by default and writes structured metric files.

## Runtime status
`NOT_TESTED`
