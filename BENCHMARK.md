# Windows RTX 5090 validation, 2026-09-27

Three different xhigh tasks compared the original Swift GGUF under llama.cpp, ordinary GSQ under NInfer, and this converted Swift GSQ under NInfer. Each backend was cold-started in turn and ran alone on the GPU. All runs used one concurrent request, greedy decoding (temperature 0), MTP 3, a configured 262,144-token context capacity, and a 98,304-token maximum response. Request time starts when the request was sent and ends when the complete response arrived; model loading time is excluded. Output tokens divided by request time gives the listed effective speed.

| Task | Backend | Output tokens | Seconds | Effective output tok/s | Result |
|---|---|---:|---:|---:|---|
| Shortest subarray | Swift GGUF + llama.cpp | 16,434 | 134.225 | 122.44 | Correct |
| Shortest subarray | Ordinary GSQ + NInfer | 13,985 | 67.047 | 208.59 | Correct |
| Shortest subarray | **This release** | **14,057** | **63.964** | **219.76** | **Correct** |
| Directed graph with one half-price edge | Swift GGUF + llama.cpp | 15,169 | 123.819 | 122.51 | Correct |
| Directed graph with one half-price edge | Ordinary GSQ + NInfer | 28,692 | 130.426 | 219.99 | Correct |
| Directed graph with one half-price edge | **This release** | **19,742** | **87.604** | **225.36** | **Correct** |
| Competing patterns of biased coin tosses | Swift GGUF + llama.cpp | 25,883 | 186.929 | 138.46 | Correct |
| Competing patterns of biased coin tosses | Ordinary GSQ + NInfer | 45,914 | 189.476 | 242.32 | Correct |
| Competing patterns of biased coin tosses | **This release** | **23,017** | **93.309** | **246.68** | **Correct** |

Equal-weight three-task means:

| Backend | Output tokens/task | Seconds/task | Effective output tok/s | Correct |
|---|---:|---:|---:|---:|
| Swift GGUF + llama.cpp | 19,162 | 148.324 | 127.80 | 3/3 |
| Ordinary GSQ + NInfer | 29,530 | 128.983 | 223.63 | 3/3 |
| **This release** | **18,939** | **81.626** | **230.60** | **3/3** |

The programming answers passed 2,005 and 2,004 seeded reference/edge tests respectively, plus separate 200,000-element/node cases. The probability answer matched independent exact rational calculations: `P(A first)=50/63`, `E[N]=853/84`, `P(N≤12)=394220/531441` for `P(H)=2/3`, A=`HTHH`, B=`THHT`.

Across these three tasks, this release generated 56,816 tokens in 244.877 seconds. Ordinary GSQ + NInfer generated 88,591 tokens in 386.949 seconds. The observed total output count was 35.9% lower and total request time was 36.7% shorter. In the shortest-subarray task, however, this release used 72 *more* tokens than ordinary GSQ, so the saving is not guaranteed per task.

At configured 256K capacity, sampled whole-card GPU-memory peaks were 21,536 and 21,648 MiB for this release on two tasks. These include existing desktop/system use and one-second sampling may miss short peaks. A separate 37,269-token input retrieval test succeeded. Neither the complete 256K input capacity nor continuous 96K output was exercised. These small-sample tests do not prove a universal speed, production stability, or 12 GB total VRAM operation.

The detailed local test report and machine-readable results were retained with the development workspace. This public summary excludes local filesystem paths and private system details.
