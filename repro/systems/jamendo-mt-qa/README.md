# Jamendo-MT-QA

- Official repo: `MAAP-LAB/Jamendo-MT-QA`
- Locked revision: `49735add63136ddd997ee53ed9c0404e60ece42b`
- Checked: 2026-09-17

## Documented setup
`pip install -r requirements.txt`. The audio dataset is gated on Hugging Face and its terms must be accepted first.

## Minimal entry point
`python run_benchmark.py --mode multi --adapter my_adapter:MyModel --output predictions/my_model_multi.json`

## Evaluation
`python evaluate.py --predictions predictions/my_model_multi.json --output eval_results/my_model_multi.json`

## Runtime status
`NOT_TESTED`
