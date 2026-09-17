# DeepResonance

- Official repo: `sony/DeepResonance`
- Locked revision: `6a4d2196562bd9e72a4a58635a6b496241f5410a`
- Checked: 2026-09-17

## Documented setup
`pip install -r requirements.txt`, or use the supplied Dockerfile.

The model also requires DeepResonance delta checkpoints, ImageBind, and Vicuna. Multimodal source data must be obtained separately because the repository does not redistribute the licensed media.

## Minimal entry point
`python inference_deepresonance.py --dataset <dataset> --result_file_name <out> --ckpt_path <ckpt> ...`

## Evaluation
No standalone evaluation command was found in the checked README.

## Runtime status
`NOT_TESTED`
