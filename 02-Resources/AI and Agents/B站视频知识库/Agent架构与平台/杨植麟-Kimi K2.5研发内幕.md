---
title: "杨植麟GTC演讲：Kimi K2.5的研发内幕"
source:
  - "https://www.bilibili.com/video/BV1AwXCBxEBk/"
  - "https://www.bilibili.com/read/cv47368362"
source_url: "https://www.bilibili.com/video/BV1AwXCBxEBk/"
column_url: "https://www.bilibili.com/read/cv47368362"
column_source: "Recastory/workspace/bilibili-retranscribe/BV1AwXCBxEBk/ingest/column_article.md"
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV1AwXCBxEBk/ingest"
duration: "~30 min"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "杨植麟（Moonshot AI 创始人）GTC 2026 演讲：Muon 优化器将 Token 效率提升两倍、Kimi-Linear 架构兼顾长上下文与推理效率、Agent Swarms 范式解决复杂任务、原生视觉文本早期融合、注意力残差预示下一代架构。"
material_tier: S
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: "Host-Guest canonical"
host_name: "GTC主持人"
guest_name: "杨植麟"
guest_title: "月之暗面（Moonshot AI）创始人"
speaker_inference: "column_article S-tier + GTC keynote structure (host intro, 杨植麟 keynote)"
speaker_confidence: high
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - moonshot_ai
  - kimi
  - scaling_laws
  - open_source
author:
  - "[[杨植麟]]"
concepts:
  - id: muon_optimizer
    zh: Muon 优化器
    en: Muon optimizer
    one_line: 二阶优化器，正交化梯度更新，将Token效率提升两倍
  - id: kimi_linear
    zh: Kimi-Linear 架构
    en: Kimi-Linear architecture
    one_line: 线性注意力变体，细粒度衰减因子，1:3混合全注意力层
  - id: agent_swarms
    zh: Agent Swarms（代理群）
    en: Agent Swarms
    one_line: 协调器与子代理并行协作，通过分工完成复杂任务
  - id: early_fusion
    zh: 原生视觉文本早期融合
    en: native vision-text early fusion
    one_line: 从预训练第一天起融合视觉和文本模态，优于后期融合
  - id: attention_residual
    zh: 注意力残差
    en: attention residual
    one_line: 将残差连接升级为注意力机制，跨层聚合隐藏状态，Token效率提升24%
---

# 杨植麟 GTC 演讲：Kimi K2.5 的研发内幕

**Host：** GTC 主持人  
**Guest：** 杨植麟（月之暗面 Moonshot AI 创始人）  
**形态：** Host-Guest canonical v3.2（**专栏主源** · GTC 2026 Keynote）  
**B 站：** [BV1AwXCBxEBk](https://www.bilibili.com/video/BV1AwXCBxEBk/) · **专栏** [cv47368362](https://www.bilibili.com/read/cv47368362) · **时长** ~30 min

---

## 开场

杨植麟在 GTC 2026 上演讲，核心探讨 Kimi K2.5 如何在 Token 效率、长上下文和智能体集群三个维度实现突破。他指出通过优化底层架构与算法，开源模型正在迅速抹平与专有前沿模型的差距。

五章：**Muon 优化器与 Token 效率** → **Kimi-Linear 架构与长上下文** → **Agent Swarms 范式** → **原生视觉文本早期融合** → **注意力残差：下一代架构**。

**术语速查**

| 中文 | 英文 | 白话 |
|------|------|------|
| Muon 优化器 | Muon optimizer | 二阶优化器，正交化梯度更新 |
| Token 效率 | token efficiency | 相同训练token下实现更低损失 |
| Kimi-Linear | Kimi-Linear | 线性注意力变体，细粒度衰减因子 |
| Agent Swarms | agent swarms | 协调器+子代理并行协作 |
| 早期融合 | early fusion | 从预训练起融合多模态 |
| 注意力残差 | attention residual | 深度维度的注意力机制 |
| QK clip | QK clip | 裁剪查询和键最大值防止训练爆炸 |

---

## 01 开放模型与智能民主化

**杨植麟（Guest）：** 我们的一项主要追求是构建更好的开放模型，我们相信智能的民主化。有了开放模型，你可以在任何地方部署，可以访问模型中的每一个权重，而不仅仅是使用一个黑箱。正如 Jensen 今年早些时候在 CES 上展示的，开放模型正在迅速缩小与专有模型的差距，正在达到前沿水平。

我们相信随着开放模型做得越来越好，我们将使世界各地的人们都能更容易地获得智能。但开放模型不能仅仅是开放的，它们也必须是优秀的。

---

## 02 Token 效率与 Muon 优化器

**杨植麟（Guest）：** 扩展是许多进展的主要驱动力。我们不仅要扩展训练 token 的数量，还要提高 token 效率——将曲线向左移动，在相同训练 token 下实现更低损失。

Token 效率不仅关乎效率，更关乎提高智能的上限。假设你有 50 万亿个高质量 token，应用 Muon 优化器后 token 效率提高两倍，这几乎像魔法一样，你获得了相当于 100 万亿 token 的效果。高质量数据数量有限，通过提高 token 效率，我们将从中获得更好的智能。

Muon 优化器是二阶优化器，每个梯度更新以一种方式转换，使得每个条目都相互正交。正确实现可获得**两倍的 token 效率提升**。我们是第一个证明 Muon 优化器可用于 LLM 训练的工作。

**杨植麟（Guest）：** 但当我们试图扩展到万亿参数模型时，遇到了训练不稳定性——最大 logits 迅速爆炸超过 1000。解决方法是引入 QK clip 技术：对每个注意力头计算最大 logits，然后计算除法因子应用于每个键和查询投影，裁剪最大值防止爆炸。这是**机器学习史上大规模 Muon 训练的第一个例子**。

> **金句 · 杨植麟**
> **中文：** Token 效率不仅关乎效率，更关乎提高智能的上限。通过提高 token 效率，50 万亿 token 可以发挥 100 万亿 token 的效果。
> **原文：** Token efficiency is not just about efficiency — it's about raising the ceiling of intelligence. With Muon, 50T tokens can deliver the effect of 100T tokens.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| Muon 优化器 | Muon optimizer | 二阶优化器，正交化梯度更新，2x token效率 |
| QK clip | QK clip | 裁剪查询和键最大值防止训练爆炸 |

**本章小结**
- Muon 优化器将 token 效率提升两倍，相当于数据量翻倍
- QK clip 技术解决了万亿参数训练不稳定性
- 这是机器学习史上大规模 Muon 训练的第一个例子

---

## 03 Kimi-Linear 架构与长上下文

**杨植麟（Guest）：** Transformer 在超长序列下计算开销巨大，而 LSTM 存在记忆饱和。Kimi-Linear 引入具有细粒度衰减因子的线性注意力变体，配合 1:3 的全注意力层混合比例。

传统线性注意力中，内存是全局的，只有一个全局衰减因子——要么忘记一切，要么保留几乎所有信息。我们引入细粒度衰减因子（对角矩阵），控制每个通道的衰减率：某些通道缓慢衰减保留长上下文信息，其他通道快速忘记过去刷新新信息。

**这是第一个在所有方面都优于全注意力架构的架构**，包括短上下文任务、长输入任务和长输出任务。

> **金句 · 杨植麟**
> **中文：** Kimi-Linear 是第一个在所有方面都优于全注意力架构的架构——短上下文、长输入、长输出全面领先。
> **原文：** Kimi-Linear is the first architecture that outperforms full attention on all fronts — short context, long input, and long output.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| Kimi-Linear | Kimi-Linear | 细粒度衰减因子的线性注意力变体 |
| 细粒度衰减 | fine-grained decay | 对角矩阵控制每个通道的衰减率 |

**本章小结**
- Kimi-Linear 通过细粒度衰减因子解决线性注意力的表达能力问题
- 1:3 混合比例平衡长上下文能力和高效实现
- 在短上下文、长输入、长输出全面优于全注意力架构

---

## 04 Agent Swarms 范式

**杨植麟（Guest）：** 单智能体难以应对极高复杂度的任务。我们引入协调器与子代理并行协作模式——类似人类社会，CEO 分解任务分配给不同角色，整个组织朝同一目标前进。

三种奖励函数指导学习：
1. **实例化奖励**：激励子代理进行实例化，防止"串行崩溃"，训练早期鼓励并行执行
2. **完成奖励**：鼓励每个子任务达到较高完成率，防止系统通过生成伪任务"破解"奖励
3. **结果奖励**：衡量整个任务是否最终完成

使用代理群将大大减少执行时间。可以扩展到 100 甚至 1000 个子代理，在可容忍时间内完成复杂任务，产生真正的经济价值。

> **金句 · 杨植麟**
> **中文：** Agent Swarms 类似人类社会——CEO 分解任务分配给不同角色，通过分工协作在可控时间内完成复杂工程。
> **原文：** Agent Swarms are like human society — a CEO decomposes tasks and assigns them to different roles, completing complex engineering through division of labor.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| Agent Swarms | agent swarms | 协调器+子代理并行协作 |
| 实例化奖励 | instantiation reward | 鼓励并行执行，防止串行崩溃 |
| 完成奖励 | completion reward | 防止生成伪任务 |

**本章小结**
- Agent Swarms 通过协调器+子代理并行协作解决复杂任务
- 三种奖励函数分别防止串行崩溃、伪任务、确保最终完成
- 可扩展到100-1000个子代理，产生真正经济价值

---

## 05 原生视觉文本融合与注意力残差

**杨植麟（Guest）：** K2.5 是第一个具有原生视觉文本联合能力的开放模型。以前的开放模型视觉能力通常在文本基础上后期添加，但 K2.5 从第一天起就融合了视觉和文本训练。

关键发现：视觉和文本可以互补。视觉强化学习甚至提高了处理繁重文本任务的性能；强大的文本基础使视觉任务无需专门的视觉 SFT 数据就能达到接近最先进的性能。

关于下一代架构——**注意力残差**：将残差连接升级为注意力机制，考虑之前所有隐藏状态并用注意力操作聚合。在 Scaling Laws 上可将 **token 效率提高 24%**。

> **金句 · 杨植麟**
> **中文：** 如果我们将所有增益结合起来——Adam 是 2014 年发明的，现在 Muon Clip 替代它；注意力是八年前的，现在 Kimi-Linear 替代它；残差连接也受到挑战，注意力残差取而代之。
> **原文：** If we combine all gains — Adam (2014) replaced by Muon Clip; attention (8 years ago) replaced by Kimi-Linear; residual connections challenged by attention residual.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| 早期融合 | early fusion | 从预训练起融合多模态 |
| 注意力残差 | attention residual | 深度维度的注意力机制，+24% token效率 |

**本章小结**
- K2.5 是第一个原生视觉文本联合的开放模型
- 视觉和文本模态可以互补，而非相互损害
- 注意力残差将 token 效率再提升 24%
- 这些"古老"技术在开源社区取得新进展

---

## 附录

### 章节时间戳（专栏 · 重点速览）

| 章 | 主题 | 时间 |
|----|------|------|
| 01 | 开放模型与智能民主化 | [00:00] |
| 02 | Token 效率与 Muon 优化器 | [03:45] |
| 03 | Kimi-Linear 架构与长上下文 | [08:12] |
| 04 | Agent Swarms 范式 | [13:50] |
| 05 | 原生视觉文本融合与注意力残差 | [20:15] |

### 素材与收录

- **专栏（S 主源）：** [cv47368362](https://www.bilibili.com/read/cv47368362)
- **视频：** [BV1AwXCBxEBk](https://www.bilibili.com/video/BV1AwXCBxEBk/)
- **ingest：** `Recastory/workspace/bilibili-retranscribe/BV1AwXCBxEBk/ingest/column_article.md`
- **形态：** 1 BV = 1 篇 canonical；`material_tier: S` · `dialogue_version: v3.2`

### 相关阅读

- [[MOC - Agent Theory and Design]] — Agent 理论与设计主题索引
- [[MOC - Harness Engineering]] — Harness 工程主题索引
