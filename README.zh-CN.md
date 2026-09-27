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

## 商用授权边界（重要）

再分发本次转换是许可允许的（Swift Open License v1.0 第 4 条），但必须随副本附带许可证、署名声明和 Qwen 基础模型许可证。

商业使用受同一许可第 5 条限制：

- 如果企业本身及其控制、被控制或共同受控的关联实体，**最近一个完整财年的总营收达到 100 万美元（US$1,000,000）及以上**，则**不在本许可的商用授权范围内**。
- 超过该门槛的企业，可向许可方 **UkisAI** 申请单独的书面商用许可（Swift Enterprise License，联系：<https://ukisai.com/contact>）。**这项授权只有 UkisAI 能给。** 本发行版是由 "SJF" 发布的非官方转换版，**无权代授、转授或豁免**上游权重的商用许可；联系 SJF 不能替代这一步。
- 未达门槛的企业，可按本许可进行商业使用；非营利与研究用途不受影响。

与权重许可分开说明：SJF 可提供**有偿的转换适配、部署、技术支持、托管服务**，也可对自行编写的新增部分（转换工具、`assemble_model.py`、Windows 兼容补丁、本文档）另行授权，这些新增内容按 Apache 2.0 授权。上述服务只覆盖 SJF 自己的工作，**不包含也不能包含**上游 Swift 权重或 Qwen 基础模型的商用许可。

需要部署或技术支持服务，请在本仓库提 Issue 联系。
