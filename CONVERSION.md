# Conversion record

Release name: **SJF Swift1.5 NInfer GSQ-RCO IQ3_S MTP**.

The input is `Swift-1.5-Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf` from [UkisAI](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF). Its SHA-256 matches the upstream `SHA256SUMS`. The output is an NInfer v3 `.ninfer` container made with [WaveCut/ninfer-all](https://github.com/iamwavecut/ninfer-all) commit `8ed38f69670e7dfe2b5db18b1081a3b3085c4305` and the attached Windows compatibility patch. The model tensors were mapped into the NInfer container without retraining or another quantization pass. The container adds the runtime resources and indices, so its byte size differs from the GGUF.

| Property | Input GGUF | Output NInfer |
|---|---:|---:|
| Size | 12,120,016,896 bytes | 12,494,820,096 bytes |
| SHA-256 | `9aecf1cd41b2cb2f32a74e0d889e33855ebef43b26f43b43feb5720239e677e5` | `152307059a0d9a7e31b9f9db63fd568d29160863c128bd92869d33d372ab0908` |

The NInfer runtime was built on Windows for the local RTX 5090. The patch changes five upstream source files to enable that build path. Apply it to the exact source commit if reproducing the local build; other build environments may need different changes. The model file and patch are distinct artifacts and have distinct licenses.

This file records a successful local conversion and load test. It does not establish bitwise equivalence between every GGUF and NInfer computation or support for all hardware. See [BENCHMARK.md](BENCHMARK.md) for the observed behavior and limits.
