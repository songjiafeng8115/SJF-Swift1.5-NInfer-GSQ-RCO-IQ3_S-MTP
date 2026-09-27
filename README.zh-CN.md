# SJF Swift1.5 NInfer GSQ-RCO IQ3_S MTP

这是把 [UkisAI 的 Swift 1.5 GSQ-RCO IQ3_S MTP GGUF](https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF) 转换成 WaveCut NInfer v3 格式后的**非官方发行版**。SJF 是本次转换和测试发行标识，不代表重新训练，也不代表 UkisAI、WaveCut 或阿里巴巴官方发布。

## 下载与还原

从 GitHub Release 下载全部 7 个 `.partNN` 文件，放在同一目录；将本仓库的 `assemble_model.py` 和 `SHA256SUMS.json` 放在同一目录，然后执行：

```powershell
python .\assemble_model.py --parts-dir . --output .\SJF-Swift1.5-NInfer-GSQ-RCO-IQ3_S-MTP.ninfer
```

脚本逐卷校验 SHA-256，按顺序拼接，并校验完整模型。转换模型共 **12,494,820,096 字节**，SHA-256 为 `152307059a0d9a7e31b9f9db63fd568d29160863c128bd92869d33d372ab0908`。原始 GGUF 的 SHA-256 为 `9aecf1cd41b2cb2f32a74e0d889e33855ebef43b26f43b43feb5720239e677e5`，与上游校验文件一致。

## 本机实测

在 Windows / RTX 5090 上使用 WaveCut `ninfer-all` 提交 `8ed38f69670e7dfe2b5db18b1081a3b3085c4305` 和本仓库的 Windows 编译补丁。三道不同、已独立验对的 xhigh 题全部答对；MTP 3、温度 0、单并发条件下，平均每题输出 **18,939 Token**，耗时 **81.6 秒**，整请求平均输出速度 **230.6 Token/s**。逐题对照见 [BENCHMARK.md](BENCHMARK.md)。

256K 是已配置的上下文容量，尚未用真实 256K 输入填满；96K 是单次输出上限，尚未连续生成 96K。约 12.5 GB 是模型文件大小，不是整卡显存需求。两次任务采样的整卡显存峰值约 21.5 GiB；不能据此宣称 12 GB 显存可跑满 256K、稳定 400 Token/s 或生产级稳定。

## 来源与许可

基础权重来自 [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)，Swift 1.5 和源 GGUF 来自 UkisAI；GSQ 相关工作按上游说明署名 ISTA-DASLab；NInfer 运行框架来自 [WaveCut](https://github.com/iamwavecut/ninfer-all)。本发行仅负责格式转换、Windows 兼容补丁与本机验证。

**权重受 [Swift Open License v1.0](LICENSE) 约束，包含商业使用条件。**Qwen 基础模型许可证见 [LICENSE-APACHE-2.0](LICENSE-APACHE-2.0)，原始署名及转换说明见 [NOTICE](NOTICE)。NInfer 源码及相应补丁按 Apache 2.0 处理。请在使用、再分发前阅读许可原文。转换过程见 [CONVERSION.md](CONVERSION.md)。

## 商业使用与授权

**再分发。** 依据 [Swift Open License v1.0](LICENSE) 第 4 条，本转换版允许复制与再分发；每一份副本均须随附该许可证、[NOTICE](NOTICE) 中的署名声明，以及 Qwen 基础模型许可证（[Apache 2.0](LICENSE-APACHE-2.0)）。

**商业使用限制。** 依据该许可证第 5 条：任何实体，连同其控制、被控制或共同受控的实体，在最近一个完整财政年度的总收入**达到或超过 1,000,000 美元（US$1,000,000）**者，**不获**本许可证对其使用上述权重的商业授权。

**企业许可。** 超过该门槛的实体，须向许可方 **UkisAI** 申请单独的书面**企业许可（Swift Enterprise License）**。申请入口：<https://ukisai.com/contact> 。该许可**仅得由 UkisAI 授予**。本发行版及其维护者不是 UkisAI 的代理人：无权授予、再许可或豁免上游权重的任何商业权利，亦无权受理或批准该类申请。

**门槛以下。** 未达门槛的实体，其商业使用依 Swift Open License v1.0 获得授权；非营利与科研用途不受该门槛限制。

**本发行版自身内容。** 格式转换工具、`assemble_model.py`、Windows 兼容补丁与本文档依 [Apache License 2.0](LICENSE-APACHE-2.0) 授权。

**来源声明。** 本发行版是 UkisAI 的 Swift 1.5 权重的非官方格式转换，与 UkisAI、WaveCut、Alibaba Cloud 无隶属、赞助或背书关系。
