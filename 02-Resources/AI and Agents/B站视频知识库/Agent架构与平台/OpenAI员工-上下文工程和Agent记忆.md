---
title: "OpenAI员工：上下文工程和Agent记忆"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV14nrMBKENb/"
speakers:
  - "Micah（OpenAI Startup Marketing）"
  - "Emory（OpenAI Solution Architect）"
  - "Brian（OpenAI Solution Architect，远程 Q&A）"
duration: "57:43"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - openai
  - context_engineering
  - memory
  - mcp
created: 2026-06-09
description: "OpenAI Build Hour：Emory 讲上下文工程与 Agent 记忆三大模式（Reshape & Fit / Isolate & Route / Extract & Retrieve），IT 故障 demo 演示 burst、trim、compact、summarize 与 cross-session 注入。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV14nrMBKENb/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# OpenAI 员工：上下文工程和 Agent 记忆

## 先搞懂这一期

**这是什么节目？**  
OpenAI **Build Hour** 系列第 N 期（Micah 主持 + 解决方案架构师 **Emory** 主讲），**~58 分钟** 幻灯片 + **双 Agent 并排 live demo**。主题不是 prompt 技巧，是 **Context Engineering** 与 **Agent Memory Patterns**——Build Hour 前序还有 Responses API、Agent RFT 等。

**这期在回答哪三个问题？**

1. **Context Engineering 到底是什么？** 和 prompt engineering、RAG 什么关系？  
2. **长运行 Agent 为什么会「忘事、爆窗、中毒」？** 四种 failure mode 长什么样？  
3. **Trim / Compact / Summarize / Cross-session 各解决什么？** 怎么选？

**用一条线串起来（没看视频也能复述）：**

Emory 引 **Andrej Karpathy**：context engineering = **艺术（判断每步什么最重要）+ 科学（可重复模式）**；现代 LLM 表现 **不只靠模型，更靠你给的 context**。  
生态：**prompt、structured output、RAG、state/history、memory** 都在 **context engineering** 大球里。  
**North Star**：**最小高信号 context** → 最大化 desired outcome。  
**三大策略**：① **Reshape & Fit**（trim/compact/summarize）；② **Isolate & Route**（subagent 分流工具与 context）；③ **Extract & Retrieve**（memory tool、state object、向量检索）。  
**短 vs 长记忆**：session 内技巧 vs **跨 session** 持久化。  
**Failure modes**：**burst**（一次 tool  dump 3000+ token）、**conflict**（退款 policy 互斥指令）、**poisoning**（幻觉进 summary 传播）、**noise**（工具定义过多重叠）。  
**Demo**：Next.js **IT 故障双 Agent**（Agents SDK）——左无 memory 多轮后忘 WiFi 过热；右有 memory 仍记得。  
展示 **get_orders / get_refund** tool 致 **context burst** → 启用 **trim**（turn 6 丢旧 tool output）、**compact**（去旧 tool 留 placeholder）、**summarize**（turn 5 压成 **memory 组件** 注入）→ **cross-session** 把 summary 写进 system prompt，新 session **「你好，MacBook Sequoia 网还断吗？」**  
Q&A：Agents SDK 实现 session 技巧；memory eval（completeness + long-task golden set）；**global vs session memory scope**；temporal tag / weight decay **prune  stale memory**；多用户 scale = **向量检索 vs 纯文本持久化** 两桶。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Prompt engineering 够用 | **Context engineering** 统管 RAG、memory、tool hygiene |
| 上下文满了就新开 chat | **Trim/compact/summarize** 有参数与 turn 边界规则 |
| Memory = 向量库 | 还有 **state object、summary 注入、memory guardrails** |
| 工具越多越好 | **Tool noise/conflict** 是独立 failure mode |

---

## 分话题讲

### 1. Context Engineering 定义与 North Star

**说法：**  
Karpathy 式定义：**艺术 + 科学**——每步推理/action 什么最重要（判断），又有 **reshape/isolate/extract** 等可测模式（科学）。  
比 prompt engineering 宽：含 **structured output、RAG、session state、memory tools**。  
目标：**smallest high-signal context**。

**和你何干：**  
做 Agent 平台先画 **context budget 分配**，不是先挑最大模型。

---

### 2. 三大策略 + 短/长记忆

**说法：**

| 策略 | 手段 | 典型场景 |
|------|------|----------|
| **Reshape & Fit** | trim、compact、summarize | 长对话、tool-heavy |
| **Isolate & Route** | subagent 分流 context/tools | 降 conflict/poisoning |
| **Extract & Retrieve** | memory tool、state、向量检索 | 跨 session 个性化 |

**短记忆** = session 内撑满 context window；**长记忆** = 多 session 收集再取回。

**和你何干：**  
Real-world harness **组合多种**，非单选。

---

### 3. 四种 Failure Mode（带 IT demo 画面）

**说法：**  
- **Burst**：`get_refund` 一次塞进整份 policy → turn 2→3 **3000+ token spike**。对策：**控制 tool output 字段**，高信号即可。  
- **Conflict**：system「无 warrant 不退款」vs tool「VIP 可退」→ Agent 乱承诺。对策：**prompt/tool 别互打架**。  
- **Poisoning**：幻觉 summary 写入 memory **跨 turn 传播**。对策：summary prompt 写 **contradiction/hallucination control**。  
- **Noise**：太多相似 tool definition → 选错 tool。对策：**小集合、清晰边界**。

**Demo 对照**：左 Agent 多轮后 **重问已答过的 WiFi/过热**；右 Agent **记得 F 更新、background sync**。

**和你何干：**  
上线前用 **context lifecycle 可视化**（system/user/tool/agent output/memory 占比）找 spike。

---

### 4. Reshape 技巧：Trim vs Compact vs Summarize

**说法：**

|  technique | 行为 | 优点 | 代价 |
|-----------|------|------|------|
| **Trim** | 丢最旧 turn，留最近 N turn | 快、无额外 latency | **丢历史** |
| **Compact** | 丢旧 **tool result**，留 message 骨架 + placeholder | 仍保留对话叙事 | tool-heavy 场景佳 |
| **Summarize** | 旧 turn 压成 **structured summary** 作 memory 注入 | **保留信息密度** | 多一次 model call、latency/cost |

**Heuristics**：  
- 分析生产 session snapshot；**别 mid-turn 截断**（turn = user msg 到下一 user msg）。  
- **40%/80% 阈值**  proactive 触发，别等撞 hard limit。  
- 独立任务链 → trim；**跨 turn 依赖** → summarize。

**Demo 参数例**：trim trigger turn 6 keep 3；summarize trigger turn 5 keep recent 3 → 出现橙色 **memory** 条，含设备型号、试过的步骤、时序。

**和你何干：**  
Summary prompt 要 **领域结构化**（IT：product/env/issues/tried steps/timeline/next steps），见 demo 的 MacBook Sequoia 案例。

---

### 5. Cross-session 与 Memory Guardrails

**说法：**  
Turn 5 summary → **reset session** → **cross-session injection** 把 summary 写入 system prompt → 新 hi 得到 **「还在 Sequoia 更新后的网络问题吗？」**  
Memory 指令要点：memory **可能 stale/incomplete**；**勿 over-weight memory**；**不存 secrets**；防 injection。  
**Memory scope**：**global**（用户常住美国、偏好友好语气）vs **session**（这次要 window seat）——多次 session 偏好可 **graduate 到 global**。

**和你何干：**  
长期记忆 = **summary + guardrails**，不是无脑全量 chat log。

---

### 6. Isolate & Route + Extract & Retrieve（Deck 精要）

**说法：**  
- **Isolate & Route**：**tool offloading 到 subagent** → 主 Agent fresh context，减 conflict/poisoning。  
- **Extract**：live term 用 **memory tool** 存 1–2 句 note（JSON/markdown）；或 **state object**（goal 等）周期性 inject。  
- **Retrieve**：类似 RAG——store → search/filter/rank → inject。  
- Memory 形态：**从简单键值 evolve 到段落**；consolidate/prune 用 **temporal tag、weight decay**。

**Scaling 两桶**：  
1. **检索式** long-term memory → 向量库 sharding、embedding 优化。  
2. **纯 persist 文本** → 磁盘/DB 存储管理。  
Pilot：**小流量开 memory** 再看 memory 池演化（travel concierge vs life coach 信息量差几个数量级）。

**和你何干：**  
Build Hour demo 代码在 **GitHub build-hours**；实现首选 **OpenAI Agents SDK** session API。

---

### 7. Eval 与 Q&A 要点

**说法：**  
- Eval：常规 eval **with vs without memory**；memory-specific eval（summary 质量、injection 时机、long-running task golden set ~50 例）。  
- **Hierarchical context**：项目级 + 任务级 **可以**，看 use case（Manus 式 offloading 同类）。  
- Libraries：**Agents SDK** 起步，生态 fast evolving。

**和你何干：**  
Memory 功能 **没 uplift 可能因任务不够长**——先测是否触达 context 阈值。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Context Engineering** | 统筹 prompt、RAG、memory、tool 的上下文优化学科 |
| **Reshape & Fit** | trim/compact/summarize 把对话塞进 budget |
| **Isolate & Route** | subagent 分流工具与 context |
| **Extract & Retrieve** | 抽取记忆存入 store，按需检索注入 |
| **Context burst** | 单 turn tool 输出导致 token 尖峰 |
| **Context poisoning** | 错误信息写入 summary/memory 并传播 |
| **Cross-session injection** | 上 session summary 写入新 session system prompt |
| **Memory scope** | global 用户事实 vs session 临时偏好 |
| **Turn block** | 从 user 消息到下一条 user 消息的不可分割单元 |

---

## 值得记住的原话

> **"Modern LLMs perform based on the context you give them."**  
> 现代 LLM 的表现取决于你给它的 context。

> **"Aiming for the smallest high-signal context."**  
> 目标是最小的高信号 context。

> **"With memory off… it falls back to re-asking information the user already gave."**  
> 没 memory 时会重问用户已经说过的信息。

> **"Context burst… from 300–400 tokens to more than 3000."**  
> 一次 tool dump 让 context 从几百涨到三千多。

> **"Do not trim mid-turn and break turn blocks."**  
> 别在 turn 中间 trim，会打断 turn 块。

> **"Memory is not authoritative — treat as potentially stale."**  
> Memory 非权威——当作可能过时或不完整。

---

## 小结

**这期最核心的判断：** 长运行 Agent 的瓶颈是 **有限 context budget**；应用 **reshape（trim/compact/summarize）+ isolate（subagent）+ extract（memory tool/retrieve）** 组合，并显式防 **burst/conflict/poisoning/noise**；跨 session 靠 **结构化 summary + guardrails**，不是堆全文 log。

**读完应带走：**
- Tool 设计 **控制返回字段**，policy 别一次 dump 全书。  
- **Turn 边界** 神圣；80% 阈值 proactive 压缩。  
- Eval 要 **with/without memory** + long-context golden set。

**和 vault 的关系：** 上下文工程官方 Build Hour，接 [[Manus创始人-深度干货-上下文工程的最佳实践]]、[[Claude Code实战-构建一个AI数据分析师]]。

---

## 行动启示

1. **给 Agent 加 context lifecycle 监控**（system/tool/memory 分项）。  
2. **Tool output 只返回高信号字段**；Refund policy 做分级检索而非全量 inject。  
3. **Summarize prompt 写结构化模板 + 幻觉/矛盾控制**（Emory IT 模板可抄）。  
4. **Cross-session 加 memory guardrails**（stale、secrets、over-weight）。  
5. **Agents SDK 试点 trim vs summarize**，用 40/80% 阈值 + eval uplift 定参。

---

## 相关阅读

- [[Manus创始人-深度干货-上下文工程的最佳实践]] — Context offloading 与 Manus 实践  
- [[Claude Code实战-构建一个AI数据分析师]] — 数据分析场景的 context 爆炸  
- [[IBM团队-Harness工程详解]] — guardrails、verify、context 压缩 harness 视角  
- [[DeepMind团队-当数百万Agent相遇]] — 多 Agent 与 HITL  
- [[MOC - Agent Theory and Design]] — Agent 理论横切索引  

---

## 来源

- **视频**：[BV14nrMBKENb](https://www.bilibili.com/video/BV14nrMBKENb/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Emory、Micah、Brian（OpenAI Solution Architecture / Startup Marketing）  
- **时长**：~57:43  
- **转写**：Recastory `bilibili-retranscribe/BV14nrMBKENb/`（FunASR SenseVoice + cam++，**asr v2 后处理** 39 段）  
- **Demo / 资源**：OpenAI Build Hours GitHub、Context Engineering Cookbook、Agents Python SDK  
- **版本**：v2 读者向讲义（2026-07-02）
