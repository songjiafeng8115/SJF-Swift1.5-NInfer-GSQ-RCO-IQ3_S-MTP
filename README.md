# SJF Swift1.5 NInfer GSQ-RCO IQ3_S MTP

This is an **unofficial format conversion**, not a newly trained model or an official release from UkisAI, WaveCut, or Alibaba. It converts UkisAI's `Swift-1.5-Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf` to the WaveCut NInfer v3 container while retaining the source GGUF tensor quantization and MTP head. `SJF` identifies this conversion and test release.

## Sources and credit

| Component | Source | Role |
|---|---|---|
| Base model | [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B), Alibaba Cloud | Base weights and architecture |
| Swift 1.5 | [UkisAI Swift 1.5 GSQ-RCO GGUF](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF) | Adapted weights and GGUF release |
| GSQ-related research | ISTA-DASLab, as credited by the source release | Quantization work |
| NInfer runtime | [WaveCut/ninfer-all](https://github.com/iamwavecut/ninfer-all) | Runtime and v3 container format |
| SJF release | Conversion, Windows compatibility patch, and local validation | This distribution |

The weights remain subject to the [Swift Open License v1.0](LICENSE), including its commercial-use terms. The Qwen base model's [Apache 2.0 license](LICENSE-APACHE-2.0) and the source [NOTICE](NOTICE) are included. The NInfer code and the separate Windows patch are under Apache 2.0. Read the licenses before redistribution or commercial use.

## Commercial use and authorization boundary

Redistribution of this conversion is allowed by Section 4 of the Swift Open License v1.0: keep the license, the attribution notices, and the Qwen base-model license with any copy.

Commercial use is limited by Section 5 of the same license:

- An organization is **not licensed** for commercial use of the Swift weights under this license if its gross revenue — together with every entity that controls it, is controlled by it, or is under common control with it — was **US$1,000,000 or more in the most recently completed fiscal year**.
- An organization above that threshold may obtain a separate written **Swift Enterprise License** from the Licensor, **UkisAI** (contact: <https://ukisai.com/contact>). **Only UkisAI can grant that permission.** This release is an unofficial conversion published under the name "SJF"; it **cannot grant, relicense, or waive** that upstream permission, and contacting SJF does not replace it.
- Below the threshold, commercial use is permitted under this license; non-profit and research use is unaffected.

Separately from the weights license, SJF can be engaged for paid **conversion, deployment, technical support, or managed-hosting** services, and can license additions it authored itself (the conversion tooling, `assemble_model.py`, the Windows compatibility patch, and this documentation), which are Apache-2.0. Those services cover SJF's own work only: they do **not** include and cannot include a commercial license for the upstream Swift weights or the Qwen base model. SJF can also **help you prepare and file a commercial-license request with UkisAI**, but it cannot decide or grant that request — that decision belongs to UkisAI alone.

For deployment, support, or help with a licensing request, open an issue in this repository.

## Download and verify

The model is distributed as ordered `.partNN` assets in the GitHub Release because it exceeds GitHub's per-asset limit. Download **all** parts into one directory, then run:

```powershell
python .\assemble_model.py --parts-dir . --output .\SJF-Swift1.5-NInfer-GSQ-RCO-IQ3_S-MTP.ninfer
```

The script checks every part's SHA-256, concatenates them in order, and checks the final model hash. It will not overwrite an existing output. The script and `SHA256SUMS.json` are in this repository and attached to the Release.

| File | Bytes | SHA-256 |
|---|---:|---|
| Source GGUF | 12,120,016,896 | `9aecf1cd41b2cb2f32a74e0d889e33855ebef43b26f43b43feb5720239e677e5` |
| Converted NInfer v3 | 12,494,820,096 | `152307059a0d9a7e31b9f9db63fd568d29160863c128bd92869d33d372ab0908` |

The source GGUF hash matches the [upstream checksum file](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF/blob/main/SHA256SUMS). This repository does not redistribute the GGUF.

## Build and compatibility

- Conversion/runtime source: WaveCut `ninfer-all` commit `8ed38f69670e7dfe2b5db18b1081a3b3085c4305` plus the included `ninfer-windows-compat.patch`.
- The patch records five Windows / RTX 5090 build compatibility changes. It does not include a copy of the upstream runtime or third-party binary dependencies.
- Model format: NInfer v3. Tested with the above runtime on Windows and an RTX 5090. Other NInfer forks, Linux builds, and other GPUs have not been validated with this file.
- The converted model is approximately 12.5 GB on disk. That is **not** the complete GPU memory requirement.

See [CONVERSION.md](CONVERSION.md) for the conversion record and [BENCHMARK.md](BENCHMARK.md) for test setup and results.

## Measured behavior

Three different, independently checked xhigh tasks were run on Windows / RTX 5090 with single concurrency, temperature 0, MTP 3, 262,144 configured context capacity, and 98,304 maximum output setting. The converted Swift + NInfer model answered all three correctly and averaged **230.6 output tokens/s** and **81.6 seconds per task** measured from request to completed response. Average output was 18,939 tokens per task. The complete per-task comparison with source Swift GGUF + llama.cpp and ordinary GSQ + NInfer is in [BENCHMARK.md](BENCHMARK.md).

The 256K setting was a capacity configuration, not a full 256K input test. The 96K output setting was an upper limit; no test generated 96K tokens continuously. The three-task result does not establish a fixed 400 tokens/s speed, 12 GB total VRAM use, or production stability.

## Changes from upstream

1. Converted UkisAI's named GGUF into the NInfer v3 container without retraining or re-quantizing the source tensors.
2. Added NInfer container resources and indices required by the WaveCut runtime.
3. Applied five Windows compatibility changes to the runtime build, provided separately as `ninfer-windows-compat.patch`.
4. Published conversion checksums, assembly utility, and local test results under this SJF release name.

`Swift`, `Qwen`, `WaveCut`, and other names identify their respective source projects; this release is not endorsed by those projects.
