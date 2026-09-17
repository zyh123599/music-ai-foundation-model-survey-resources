# Models and code

The full machine-readable registry is in [`resources/models_and_code.csv`](../resources/models_and_code.csv). This page is a shorter index of projects that are useful starting points for reproducing or extending recent Music AI work.

Release status changes quickly. Check the project page before treating code, checkpoints, or data as complete.

## Generation

- [YuE](https://github.com/multimodal-art-projection/YuE) — long-form music generation
- [SongBloom](https://github.com/tencent-ailab/SongBloom) — coherent song generation
- [LeVo / SongGeneration](https://github.com/tencent-ailab/songgeneration) — song generation with preference alignment
- [Live Music Models](https://github.com/magenta/magenta-realtime) — real-time music generation
- [PADS-TAL](https://github.com/PADS-TAL/PADS-TAL) — diverse text-to-music sampling

## Editing and control

- [Muse](https://github.com/yuhui1038/Muse) — long-form song generation with fine-grained style control
- [BeatEdit](https://github.com/Haoyu-Gu/BeatEdit-code) — symbolic music editing
- [MIDILM](https://github.com/Large-Multimodal-Model-Lab/MIDILM) — controllable text-to-MIDI generation
- [MusicMagus](https://github.com/ldzhangyx/MusicMagus) — text-guided music editing
- [Instruct-MusicGen](https://github.com/ldzhangyx/instruct-MusicGen) — instruction-tuned music editing
- [FGG-music](https://github.com/huajianduzhuo-code/FGG-music-code) — fine-grained guidance for symbolic generation
- [SyMuPe](https://github.com/ilya16/SyMuPe) — affective symbolic performance control
- [Polyphonia](https://github.com/Ltx-Leif/polyphonia) — zero-shot polyphonic timbre transfer

## Representation and tokenization

- [BEAT](https://github.com/Lekai-Qian/BEAT-code) — symbolic tokenization and generation
- [PHALAR](https://github.com/gladia-research-group/phalar) — learned musical audio representations
- [ALMTokenizer](https://github.com/yangdongchao/ALMTokenizer) — low-bitrate audio tokenizer
- [CultureMERT](https://huggingface.co/ntua-slp/CultureMERT-95M) — cross-cultural music representation learning
- [MusGConv](https://github.com/manoskary/musgconv) — graph representation for symbolic music understanding

## Music understanding and benchmarks

- [Music Flamingo](https://huggingface.co/nvidia/music-flamingo-2601-hf) — music-specialized audio-language model
- [Auden](https://github.com/AudenAI/Auden) — audio-language pretraining
- [CMI-Bench](https://github.com/nicolaus625/CMI-bench) — music instruction-following benchmark
- [Jamendo-MT-QA](https://github.com/MAAP-LAB/Jamendo-MT-QA) — multi-track comparative music QA
- [WildScore](https://github.com/GaganVM/WildScore) — symbolic music reasoning benchmark
- [MuChin](https://github.com/CarlWangChina/MuChin) — Chinese colloquial music-language benchmark
- [DeepResonance](https://github.com/sony/DeepResonance) — music-centric multimodal instruction tuning
- [MCR-BENCH](https://github.com/WangCheng0116/MCR-BENCH) — audio/text conflict and text-bias evaluation
- [MSA-bench](https://github.com/sony/MSA-bench) — music structure analysis with foundational audio encoders

## Production, restoration, and separation

- [SonicMaster](https://github.com/AMAAI-Lab/SonicMaster) — music restoration and mastering
- [LLM2Fx](https://github.com/SonyResearch/LLM2Fx) — tool calling for music post-production
- [MEGAMI](https://github.com/SonyResearch/MEGAMI) — generative effect embeddings for automatic mixing
- [Music Source Restoration](https://github.com/yongyizang/music-source-restoration) — source restoration
- [AudioSep](https://github.com/Audio-AGI/AudioSep) — text-queried source separation
- [MMAudioSep](https://github.com/sony/mmaudiosep) — video/text-queried sound separation

## Multimodal generation

- [AudioX](https://github.com/ZeyueT/AudioX) — unified anything-to-audio generation
- [ControlFoley](https://github.com/xiaomi-research/controlfoley) — controllable video-to-audio generation
- [SALSA-V](https://github.com/ETH-DISCO/SALSA-V) — long-form synchronized audio from video
- [GVMGen](https://github.com/chouliuzuo/GVMGen) — video-to-music generation
- [ControllableV2M](https://github.com/chouliuzuo/ControllableV2M) — spatial-temporal video-to-music alignment

## Evaluation and robustness

- [CMI-RewardBench](https://github.com/Haiwen-Xia/CMI-RewardBench) — music reward-model benchmark
- [MusicDET](https://github.com/Chaolei98/MusicDET) — AI-generated music detection
- [MAD / MusicPrefs](https://github.com/i-need-sleep/mad) — text-to-music evaluation aligned with human preferences
- [ISMIR 2025 AI-music detector](https://github.com/deezer/ismir25-ai-music-detector) — Fourier-artifact analysis and detection
- [TTA-Bench tools](https://github.com/NKU-HLT/TTA-Bench-tools) — text-to-audio benchmark tooling

For every entry, use the original project license and data terms. This repository only points to upstream resources; it does not redistribute model weights or datasets.
