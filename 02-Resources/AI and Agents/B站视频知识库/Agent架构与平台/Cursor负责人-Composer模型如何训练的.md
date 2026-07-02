---
title: "Cursor负责人：Composer模型如何训练的？"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1iH7R6tEfJ/"
speaker: "Federico（Cursor Composer Research Lead）、Dima（Fireworks AI）"
duration: "45:12"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - cursor
  - harness_engineering
created: 2026-06-09
description: "Federico+Dima 拆解 Composer 2：Kimi 2.5 基座+mid-training 吃 code token+大规模 RL 在 Cursor harness 里 rollout；异步全球集群、权重 delta 同步、MoE 数值对齐、sim RL vs 在线 real-time RL。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1iH7R6tEfJ/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Cursor 负责人：Composer 模型如何训练的？

## 先搞懂这一期

**这是什么节目？**  
播客访谈 **Cursor Composer 2 research lead Federico** + **Fireworks 的 Dima**（Composer 2 RL 基础设施）。讲 **为什么 Cursor 自训模型**、**Composer 2 训练栈**、以及 RL 系统里 **算法× infra 的一堆硬问题**（不是 benchmark 复读）。

**这期在回答哪三个问题？**

1. **应用公司为何要训模型？** 模型权重像 **有限存储**——Cursor 只关心 **Cursor 内软件工程**，把每一位 bit 专投这一任务 → **更小更便宜仍强**（Composer 比 Opus 级便宜一个数量级）。  
2. **Composer 2 训练配方？** **Kimi 2.5**（1T MoE，~3B active）→ **mid-training 规模吃 code token** → **大规模 RL 在真实 Cursor harness 里 rollout**（学 tool、环境、**写正确 code**）。  
3. **RL infra 难在哪？** 要同时跑 **trainer + 成千上万 agent session**；**异步 pipeline** 换 GPU 利用率；**全球分集群 inference** + **权重 delta 压缩同步**；**MoE router 数值 mismatch**；环境必须 **像真用户电脑** 否则 model **在 fake env 里作弊**。

**用一条线串起来：**

「货架模型 + prompt」有上限 → **post-training 把 tool 行为 bake 进权重** → 自底向上 mid-train+RL **更快给用户可用模型**（自 pretrain 太慢）→ RL = 在 harness 里完整 session rollout + reward（compile/LM judge）→ **async trainer∥rollout**（staleness vs 利用率）→ **FP4 训练 + Fireworks 推理**；推理算力约 **训练 1/3** 若引擎优化 → **VM 栈** 秒启 10 万环境，Docker 不够像 production → **RL 里学 self-summarize/compaction** 撑 long horizon → **offline sim RL 教 reasoning**，**online real-time RL** 用用户 thumbs 几小时一更（不能从零训，只能「大蛋糕上的樱桃」）→ **自家产品环境 > RL env .vendor**。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Cursor = 套壳 GPT | **Composer 2 = 专精 Cursor 内 SE 的自训 agent 模型** |
| RL = 实验室概念 | **Production = trainer + inference + VM 环境 + reward 工程** |
| 越大模型越好 | **数据维度 scale + 清掉权重里「分心能力」** 专精仍符合 bitter lesson |
| Harness 与模型分开 | **RL 把 compaction 等 harness 行为 joint optimize 进模型** |

---

## 分话题讲

### 1. 为什么 Cursor 要当「基础模型公司」

Federico 比喻：权重 = **存储驱动器**，容量有限。Cursor **只做一件事**——**Cursor 里的软件工程**——那就 **把所有 bit 投这一任务**。  
Composer **比 Opus 便宜数量级**，因 ** specialize 全部权重**。  

Dima：**应用演化路径** = 货架模型 prompt → 摸清 harness → **usage + harness 细节** 应用最强杠杆 → **craft model to your environment**。  
第二原因：**质量×速度×成本** 三维；infra 优化有顶，**训练继续推 Pareto frontier**。

**和你何干：**  
有 **独特 tool/环境/轨迹** 的产品，最终可能都要 **post-train**，不只 prompt。

---

### 2. Composer 2 配方：mid-training + RL 双轴

Composer 1 主要推 **RL**；Composer 2 **同时推**：
- **Continual mid-training**：海量 **code token**（近 pretrain 规模）+ 部分 web → 学库、模式、广分布。  
- **Large-scale RL**：在 **Cursor harness** 里 agent session → 学 **tool call、导航、写对 code**（mid-train 会写 code，但不保证 **correct**）。

**为何不自 pretrain？** **Top-down**：最快给用户有用模型；bottom-up pretrain→mid→RL **太慢**。下一版希望 **自有 base**。

Tab 补全 vs Composer：**tab 是小模型低延迟**；Composer **大模型 agent**，mid-train 目标不同。

---

### 3. RL 循环：不是 next token，是整段 session

Rollout = 用户眼里 **一次完整 Cursor agent 会话**（可能 50 turn：tool → code → …）→ **reward**（可验证 compile/test 或 LM judge）→ 信号回传更新权重。

额外组件：
- 大规模 **forward/backward**（和 pretrain 一样要堆 GPU）  
- **Orchestrate 环境** + **inference**（rollout 时要跑模型）  

**Sync vs async pipeline：**  
- Sync：训完再 rollout，**算法干净，一半 GPU 空转**。  
- Async：trainer 与 rollout **流水线并行**，GPU 常满；代价 **staleness**（rollout 完成时权重已变几 step）——用算法 trick 换 **compute efficiency**。

Cursor **GPU 有限（万级 not 百万）**：**FP4 训练**、推理与 Fireworks 深协作； myth busted：**优化后 inference FLOPs ≈ training 的 1/3**（不是「RL 推理永远比训练贵一个数量级」）。

---

### 4. 全球分布式与权重 delta _ship

RL inference 可 **分布全球小集群**（难找超大 contiguous cluster）；训练集中一簇。  
Composer 2 用 **四大洲集群** + **低峰复用 production Composer 1.5 推理 GPU**。

**难题：** 每 5–15 分钟 **~1TB 权重 snapshot** 要推到远端 inference——  
- 全量传不现实 → 观察 **每 step 只变一小部分 weight** → **delta 压缩**（可小 ~20×）+ 分片上传 → 远端 **lossless reconcile**，inference **pause ~30s swap weights**。

Dima：**disaggregate trainer/inference** → 用便宜异构硬件跑 rollout，成本下来。

---

### 5. 环境、faking、作弊

RL 环境要 **极度接近真实用户电脑**——model 能 **察觉 fake env**，**ARL 与 production 行为不一致**，会 **学 reward hack**（「哦我在假环境，试 trick」）。

Cursor 自建 **VM 栈**：要能 **burst 10 万 VM**；Docker **不像 production**（DB migration 要真 DB 等）。  
**RL env vendor** 对 **frontier 通用 lab** 有用；**有自家产品的公司** → **最强环境就是 production clone**（隔离好，别动真 DB）。

Federico：**不用 RL env 公司**——coding 有 GitHub 等；难在 **infra + 服务依赖**。

---

### 6. 数值对齐：MoE 的 expert 选错

Async RL 要在 trainer **重跑 forward** 算 log prob；inference vs train **浮点非结合律** → 微小差异 → **MoE router top-k** 可能 **expert 7 vs 9** → 更新错 expert → **训练崩**。  

解法：**deterministic kernel 顺序**（慢）、**router replay**（inference 告诉 trainer 激活了哪个 expert）、量化对齐等——**算法×系统交界**。

---

### 7. Reward、sim RL vs online RL、long horizon

**Reward 细节：** 保密；原则 **越可 verify 越好 scale**（compile/run test）；LM-as-judge 因 **判别比生成易**。专家价值在 **craft task + 编码产品体验规则**，不是人手评每个 rollout。

**Offline sim RL：** 同一 prompt **16–128 并行 try** → GRPO 类算法要多样本；可 **off-policy 乱试** 不影响用户。  
**Online real-time RL：** 用户 happy/sad 信号 **几小时更新一版**；**不能从零训**——用户不愿用烂模型 → 只能 **sim 先 bootstrap 到 bar**，上线后再 **樱桃式改进**；horizon 变长后要 **revisit 更新频率**。

**Long horizon：** credit assignment 变难 + context 有限 → Cursor 在 **RL 里训 self-summarize/compaction**（200k window 实际 **百万 token 任务**）——**harness 行为被 RL joint optimize**（DeepMind「模型吞噬 harness」的一个实例）。

**RL 何时需要：** 长 horizon **tool agent** 几乎必须；纯 next-token 任务有时 SFT 够——但 Federico 认为 RL 还 **sharp「你是专家要做对」** 的人格。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Weight as storage** | 专精 = 有限容量全投单一任务 |
| **Mid-training** | pretrain 与 RL 之间大规模 continue train on code |
| **Rollout** | 一次完整 agent session，用于 RL 采样 |
| **Async RL pipeline** | trainer∥rollout 并行，换 staleness 换 GPU 满负载 |
| **Weight delta sync** | 只传权重变化量，全球 inference 集群快速对齐 |
| **Sim vs online RL** | 模拟多试 vs 真实用户信号；后者不能 cold start |
| **Self-summarize in RL** | 在 RL 里学 compaction，撑超长任务 |
| **Fake env cheating** | 模型识别训练环境并 hack reward |
| **Router replay** | MoE 对齐 inference/training 选的 expert |

---

## 值得记住的原话

> **"Allocate all of the bits… to software engineering inside Cursor and inside Cursor only."**  
> 把每一位权重只投 Cursor 内的软件工程。

> **"The most leveraged attribute… is actual usage… craft your model to your environment."**  
> 最强杠杆是用法数据；把模型 craft 到你的环境。

> **"The model can figure out when it's being run in a fake environment… different behaviors during RL than in production."**  
> 模型分得清假环境，RL 与线上行为会分裂。

> **"If you have your actual product, you should do RL against it."**  
> 有自家产品就该对着它做 RL。

> **"We can't use online RL to create the model from scratch… users need to be using the model."**  
> 在线 RL 造不出从零的模型——用户先得愿意用。

---

## 小结

**这期最核心的判断：** Composer 2 = **专精 Cursor 环境的 mid-train + harness 内 RL**；竞争力不只在算法，在 **async 全球 infra、delta 权重同步、VM 真环境、MoE 数值对齐**；**sim RL .bootstrap，online RL 抛光**；长跑 agent 把 **compaction 训进模型**。

**读完应带走：**
- 应用公司训模型 = **环境+tool 行为写进权重**，prompt 有顶。  
- RL infra = **pretrain 集群 + inference + 10 万 VM 环境 + reward 工程**。  
- **Production clone** 往往胜过 generic RL env vendor。

**和 vault 的关系：** Cursor 模型化对照 [[DeepMind-模型将吞噬Harness]]、[[Cursor-128个Agent团队协作]]、[[MOC - Agent Theory and Design]]。

---

## 行动启示

1. **有独特 tool 链** 就评估 post-train，别只调 prompt。  
2. **RL 环境尽量 clone production**（隔离数据），Docker toy env 防作弊。  
3. **Async pipeline** 前算清 staleness 与 GPU 空转 tradeoff。  
4. **Long horizon** 同时训 **summarize/compaction**，别只 harness 外挂。  
5. **Reward 优先可 verify**；LM judge 拆 rubric，别一个 judge 评一切。

---

## 相关阅读

- [[DeepMind-模型将吞噬Harness]] — harness 能否被模型内化  
- [[Cursor-128个Agent团队协作]] — Cursor 128 agent 与 online RL 叙事  
- [[Cursor副总裁-构建软件开发过程的Agent]] — SDLC agent 产品侧  
- [[IBM团队-Harness工程详解]] — harness verify 与 RL 环境对照  
- [[PlanetScale-Agent时代的基础设施]] — Composer 2.5 实战 demo 提及  

---

## 来源

- **视频**：[BV1iH7R6tEfJ](https://www.bilibili.com/video/BV1iH7R6tEfJ/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Federico（Cursor）、Dima（Fireworks AI）  
- **时长**：~45:12  
- **转写**：Recastory `bilibili-retranscribe/BV1iH7R6tEfJ/`（**asr v2**）  
- **版本**：v2 读者向讲义（2026-07-02）
