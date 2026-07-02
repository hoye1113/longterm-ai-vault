---
title: "Snorkel：小模型 RL 超越大模型"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1JvjP6XE1k/"
speaker: "Koby Crawford (Snorkel AI)"
saved: 2026-07-02
tags:
  - ai_agent
  - ai_evaluation
  - video_transcript
  - bilibili
created: 2026-07-02
description: "Snorkel 用专家在环数据 + GRPO，4B 模型在金融 FinQA tool-use 上 pass@1 约 2× 超越 235B；核心失败是 tool discipline 而非 reasoning，单次训练 ~$500。"
transcript_source: "Recastory/workspace/knowledge/B2-snorkel-rl/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Snorkel：小模型 RL 超越大模型

## 先搞懂这一期

**这是什么节目？**  
Conference 末场 talk。**Koby Crawford**（Snorkel AI）分享 Snorkel research 与 Artificial Analysis **RL agentic project** 合作结果。偏 research + enterprise 落地，不是产品 demo。

**这期在回答哪三个问题？**

1. **企业性能不够时，换大模型是唯一解吗？**  
2. **235B reasoning model 和 4B 小模型，在金融 tool-use 上差在哪？**  
3. **怎么用 ~$500、~24h 的 GRPO，让 4B beat 235B？**

**用一条线串起来（没看视频也能复述）：**

企业默认路径：FinQA / 金融分析 performance 不够 → **drop in larger model** → 推理成本、延迟、on-prem 部署压力暴涨。

Snorkel 挑战：**有时用对数据训对行为，比 Terrance Tao 式通才 reasoning 更管用**——金融分析师只需 sequential SQL + 基本算术，不需要解 Virtually 算法。

**235B 典型失败**：问 YouTube revenue YoY → 不 inspect 环境 → 查 **不存在 table** → 空结果两次 → **hallucinate loose answer**。工具有 `get_table_names`，没用。

**4B + expert data + GRPO** 后：`get_table_names` → schema inspect → query → **error self-correction** → 正确答案。**Pass@1 ~2× 235B**，单次训练 **~$500、~24h**。

核心反直觉：**问题不在 reasoning，在 tool discipline**；**single-table-only 训练 uplift 最大**；**Rubrics** 帮从 pass/fail 定位到具体 behavior gap。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 听过「换更大模型」 | **换大模型常常是错锤子**——窄任务要 **behavior fix** |
| 听过 RLHF / GRPO | **GRPO on-prem ~$500/run** 可 tractable，不必等 vendor 更大模型 |
| 读过 [[OpenAI评估团队-不再低估模型]] | **Rubrics 定位 specific behavior**——与 OpenAI「找 gap、别低估小模型」一致 |
| 做 enterprise agent 部署 | **Expert-in-the-loop 数据 + verification** ROI 常高于 scale 参数 |

---

## 分话题讲

### 1. 企业默认「换大模型」常常是错锤子

金融/医疗等 on-prem 场景：性能不够 → 上大模型 → 推理成本与延迟暴涨。Snorkel 挑战的是：**有时用对数据训对小行为，比通才 reasoning 更管用**。

**Terrance Tao tower effect**（RL 团队用语）：通才数学家什么都能碰，但分析师任务需要的是 **窄而可靠的 tool workflow**——sequential query + 加减法，不需要 deep math。

> Stop making models bigger... sometimes we find great wins with the right data applied to the right problem statement.

**和你何干：** 性能瓶颈先问：**是 reasoning 不够，还是 tool discipline 缺口？**

---

### 2. 235B 典型失败链：有 tool 不用

问 YouTube revenue YoY growth（FinQA 环境）：

1. 235B reasoning model **未 inspect 环境**  
2. 直接 query **不存在的 table**  
3. 两次空结果  
4. **Hallucinate** loose answer  

`get_table_names` 等 tool **存在但未被调用**——greater reasoning 没帮上忙。

> It didn't inspect the environment... queried a non-existing table... falls back to just loose hallucinating an answer.

**和你何干：** Tool-use eval 要看 **是否先 discover schema**，非只看 final answer。

---

### 3. 4B RL 后的正确行为：discover → inspect → query → correct

Finetune 后的 4B：

1. **`get_table_names`** — 先发现有哪些表  
2. **`get_table_info`** — 读 schema  
3. **Run SQL query**  
4. Column 报错 → **读 error、自修正**到正确 column  
5. 正确答案  

学到的是 **tool discipline + error correction**，不是更深数学。

> It wasn't the reasoning that was the issue. It was the tool use.

**和你何干：** 训练/RL 投资方向：**fix core tool failure mode**，非盲目 scale 参数。

---

### 4. Expert-in-the-loop 数据 + 验证

Snorkel 平台 solicit **金融 HD 级专家**；每条 task 经 verification——query 可执行、答案可验证。数据质量是 Snorkel 核心卖点（「very, very, very motivated about high quality」）。

FinQA **RL 环境**自包含、无外部依赖；已发布在 HuggingFace Spaces / OpenEnv，可 fork 适配自家 needs。

Pipeline 概要：

- Expert 生成 high quality dataset  
- Verification step：task fit ask、verifiable answer  
- **GRPO** on 4B private base model  
- **~24h job，under $500 per run**

> RL does not have to be a very expensive thing... under five hundred dollars per run.

**和你何干：** On-prem 团队若已考虑自托管小模型，这是 **actionable** 路径。

---

### 5. 反直觉 ablation：single-table-only 训练 uplift 最大

Dataset 含 single-table 与 multi-table Q&A。Ablation：

| 训练 regime | 结果 |
|-------------|------|
| Full mixed | 有 uplift |
| Curriculum single→multi | 一般 |
| **Single-table only** | **最大 uplift** |

Fix **core tool failure mode** 后，harder multi-table benchmark（infrequent reasoning）仍 **13.9% → 26.6%**（~2×）——泛化来自行为修复，非花哨 curriculum。

> Single-table-only training was actually the one that yielded the greatest uplift.

**和你何干：** **Simple subset 训练** 可能优于复杂 curriculum——fix core failure first。

---

### 6. Rubrics：从 pass/fail 定位到 behavior

Snorkel research 方向：eval **rubrics** 把响应拆成多条子问题（是否先 list tables？schema 对吗？error 处理了吗？）→ 定位 **哪条 behavior 错** → 决定生成哪类 training data。

RL 仍吃 scalar reward（GRPO），但 rubric 指导 **data 投资方向**——与 [[OpenAI评估团队-不再低估模型]]「never underestimate + 找 specific gap」eval 哲学一致。

> Find the specific behavior that's really the problem.

> Use the rubric to help you do an analysis of what are the behaviors you want to generate datasets to help you with.

**和你何干：** **Rubric 先定位 behavior gap**，再决定上大模型还是 RL。

---

### 7. 4B vs 235B 结果与 on-prem 可行性

Pass@1 **约 double**（百分比意义上 solve rate 显著提升）——**right dataset + right RL** 让小模型在 **narrow production task** 上超越 frontier reasoning giant。

Cost/speed/security：4B 更适合 on-prem、financial data 不出域、低 inference cost。

**和你何干：** Narrow production task 上，**~$500 GRPO run** 值得试点，不必等 vendor 更大模型。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **GRPO** | Group Relative Policy Optimization，本次 RL 算法 |
| **FinQA environment** | 金融 tool-use RL 评测环境（开源） |
| **Expert-in-the-loop** | 专家参与数据生成与 verification |
| **Tool discipline** | 先 discover schema 再 query，而非瞎猜表名 |
| **Terrance Tao effect** | 通才大模型 vs 窄任务所需 behavior |
| **Rubrics** | 把 eval 拆成多条 behavior 子问题 |
| **Single-table-only training** | 只训简单子集反而 uplift 最大的 ablation |
| **Pass@1** | 单次采样正确率 |
| **Reward hacking** | 字面满足要求、spirit 不对（eval 设计要防） |

---

## 值得记住的原话

> **"Stop making models bigger... sometimes we find great wins with the right data applied to the right problem statement."**  
> 别一味做大模型——用对数据打对问题，有时收益巨大。

> **"We'll just drop in a larger model... sometimes maybe that isn't quite the answer."**  
> 性能不够就换大模型——有时那不是答案。

> **"The Terrance Tao effect... brilliance might not necessarily be what a financial analyst actually has to have."**  
> Terrance Tao 效应：通才 brilliance 不一定是分析师需要的。

> **"It didn't inspect the environment... falls back to just loose hallucinating an answer."**  
> 没 inspect 环境——最后 hallucinate loose 答案。

> **"It wasn't the reasoning that was the issue. It was the tool use."**  
> 问题不在推理，在 tool use。

> **"RL does not have to be a very expensive thing... under five hundred dollars per run."**  
> RL 不必很贵——单次 run 五百美元以内。

> **"Single-table-only training was actually the one that yielded the greatest uplift."**  
> 只训 single-table 反而 uplift 最大。

> **"Find the specific behavior that's really the problem."**  
> 找到真正出问题的那条具体行为。

> **"Four billion parameter model performs better than the two hundred and thirty five billion parameter model."**  
> 40 亿参数模型表现优于 2350 亿参数模型。

---

## 小结

**这期最核心的判断：** 金融 tool-use 上 **4B + expert data + GRPO** 可 **pass@1 约 2× 超越 235B**——瓶颈常在 **tool discipline（inspect 环境）**，不在 reasoning 深度或参数规模。

**读完应带走：**
- 「性能不够换大模型」常常是错锤子；**Terrance Tao effect**——通才 brilliance 不等于岗位所需行为。
- **Rubrics** 定位 specific behavior gap；single-table-only 训练 ablation 反而 uplift 最大。
- RL run ~$500/24h 级，narrow production task 值得试点 expert data + verification。

**和 vault 的关系：** 接 ai_evaluation，与 OpenAI eval 线互补——**小模型 + 数据 + RL** 的落地 counter-narrative。

---

## 行动启示

1. **Rubric 先定位 behavior gap**，再 scale 参数或换大模型。  
2. **Tool-use 任务**：检查模型是否 discover schema，而非只看 final answer。  
3. **Expert data + verification** 比盲目 scale 参数更 ROI。  
4. **GRPO on-prem ~$500** 值得 narrow production task 试点。  
5. **Simple subset 训练** 可能优于复杂 curriculum——fix core failure first。  
6. **FinQA/OpenEnv** 可 fork 做自家 financial agent eval。  
7. 合读 [[OpenAI评估团队-不再低估模型]]：别低估小模型 + 找 specific gap。

---

## 相关阅读

- [[OpenAI评估团队-不再低估模型]] — eval 方法论：找 specific gap、dogfood  
- [[Databricks-企业级Agent生产实践]] — 企业三层 eval 与 behavioral 层  
- [[YC论文俱乐部-5篇论文揭示AI研究趋势]] — 研究趋势与 eval 交叉  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1JvjP6XE1k](https://www.bilibili.com/video/BV1JvjP6XE1k/)（B 站转载 Easonlee的AI笔记 × Snorkel AI Koby Crawford）  
- **嘉宾**：Koby Crawford，Snorkel AI  
- **转写**：Recastory `B2-snorkel-rl/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
