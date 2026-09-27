# Windows RTX 5090 validation, 2026-09-27

Three different xhigh tasks compared the original Swift GGUF under llama.cpp, ordinary GSQ under NInfer, and this converted Swift GSQ under NInfer. Each backend was cold-started in turn and ran alone on the GPU. All runs used one concurrent request, greedy decoding (temperature 0), MTP 3, a configured 262,144-token context capacity, and a 98,304-token maximum response. Request time starts when the request was sent and ends when the complete response arrived; model loading time is excluded. Output tokens divided by request time gives the listed effective speed. Pure decode speed comes from server logs; both speed columns count output tokens only.

## Test computer

| Component | Verified configuration |
|---|---|
| CPU | Intel Core Ultra 9 285K, 24 cores / 24 logical processors |
| RAM | 102,298,955,776 bytes installed (approximately 95.3 GiB) |
| GPU | NVIDIA GeForce RTX 5090, 32,607 MiB reported VRAM |
| NVIDIA driver | 616.56 |
| OS | Windows 11 Pro, version 10.0.26200, build 26200 |
| Converted backend | WaveCut `ninfer-all` commit `8ed38f69670e7dfe2b5db18b1081a3b3085c4305` with included Windows compatibility patch |

| Task | Backend | Output tokens | Seconds | Effective output tok/s | Pure decode tok/s | Result |
|---|---|---:|---:|---:|---:|---|
| Shortest subarray | Swift GGUF + llama.cpp | 16,434 | 134.225 | 122.44 | 122.75 | Correct |
| Shortest subarray | Ordinary GSQ + NInfer | 13,985 | 67.047 | 208.59 | 209.40 | Correct |
| Shortest subarray | **This release** | **14,057** | **63.964** | **219.76** | **220.70** | **Correct** |
| Directed graph with one half-price edge | Swift GGUF + llama.cpp | 15,169 | 123.819 | 122.51 | 122.86 | Correct |
| Directed graph with one half-price edge | Ordinary GSQ + NInfer | 28,692 | 130.426 | 219.99 | 220.50 | Correct |
| Directed graph with one half-price edge | **This release** | **19,742** | **87.604** | **225.36** | **226.00** | **Correct** |
| Competing patterns of biased coin tosses | Swift GGUF + llama.cpp | 25,883 | 186.929 | 138.46 | 138.91 | Correct |
| Competing patterns of biased coin tosses | Ordinary GSQ + NInfer | 45,914 | 189.476 | 242.32 | 242.80 | Correct |
| Competing patterns of biased coin tosses | **This release** | **23,017** | **93.309** | **246.68** | **247.30** | **Correct** |

Equal-weight three-task means:

| Backend | Output tokens/task | Seconds/task | Effective output tok/s | Pure decode tok/s | Correct |
|---|---:|---:|---:|---:|---:|
| Swift GGUF + llama.cpp | 19,162 | 148.324 | 127.80 | 128.17 | 3/3 |
| Ordinary GSQ + NInfer | 29,530 | 128.983 | 223.63 | 224.23 | 3/3 |
| **This release** | **18,939** | **81.626** | **230.60** | **231.33** | **3/3** |

The programming answers passed 2,005 and 2,004 seeded reference/edge tests respectively, plus separate 200,000-element/node cases. The probability answer matched independent exact rational calculations: `P(A first)=50/63`, `E[N]=853/84`, `P(N≤12)=394220/531441` for `P(H)=2/3`, A=`HTHH`, B=`THHT`.

Across these three tasks, this release generated 56,816 tokens in 244.877 seconds. Ordinary GSQ + NInfer generated 88,591 tokens in 386.949 seconds. The observed total output count was 35.9% lower and total request time was 36.7% shorter. In the shortest-subarray task, however, this release used 72 *more* tokens than ordinary GSQ, so the saving is not guaranteed per task.

At configured 256K capacity, sampled whole-card GPU-memory peaks in the graph and coin tasks were 21,536 / 21,648 MiB for this release, 21,737 / 21,785 MiB for ordinary GSQ + NInfer, and 25,639 / 25,537 MiB for Swift GGUF + llama.cpp. These include existing desktop/system use and one-second sampling may miss short peaks. A separate 37,269-token input retrieval test succeeded for all three; this release took approximately 9.1 seconds, while Swift GGUF + llama.cpp took approximately 14.0 seconds. Neither the complete 256K input capacity nor continuous 96K output was exercised. These small-sample tests do not prove a universal speed, production stability, or 12 GB total VRAM operation.

The shortest-subarray task was also run two additional times per backend. Across those three same-task runs, average request time was 129.69 seconds for Swift GGUF + llama.cpp, 65.80 seconds for ordinary GSQ + NInfer, and 62.93 seconds for this release. Output token counts and checked answers were identical across those reruns. These repeated runs are excluded from the three-different-task mean above.

The detailed local test report and machine-readable results were retained with the development workspace. This public summary excludes local filesystem paths and private system details.
