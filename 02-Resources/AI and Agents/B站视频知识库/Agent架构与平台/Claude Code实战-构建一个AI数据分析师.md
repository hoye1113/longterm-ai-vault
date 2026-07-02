---
title: "Claude Code实战：构建一个AI数据分析师"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1Mpf9B5Egk/"
speaker: "Brex 数据团队工程师（与主持人对谈）"
duration: "51:46"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - claude_code
  - claude
  - mcp
  - context_engineering
created: 2026-06-09
description: "Brex 工程师演示用 Claude Code + Snowflake MCP 复刻数据分析师四步循环（监控-调查-故事-影响），强调查询结果 token 爆炸、窄语义层与 data analysis Skills 护栏。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1Mpf9B5Egk/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Claude Code 实战：构建一个 AI 数据分析师

## 先搞懂这一期

**这是什么节目？**  
**Brex** 数据团队工程师与播客主持人的 **~52 分钟对谈 + 现场 demo**。不是 SQL 教程，是用 **Claude Code 搭「像数据科学家一样想问题」的 Agent**——含 Snowflake MCP 从零生成、公开融资数据集问答、以及 Brex 真实支出数据洞察。

**这期在回答哪三个问题？**

1. **AI 能帮数据分析师干什么，不能干什么？** 监控、调查、讲故事、推动实验，哪几步已可用？  
2. **为什么数据分析 Agent 要单独做 MCP，还要管 context？** 和「写代码的 Claude」有何不同？  
3. **PM 自助查数会不会干掉数据岗？** Brex 内部实际发生了什么？

**用一条线串起来（没看视频也能复述）：**

开场：八个月前 AI 只会 debug SQL，现在能写 **boilerplate + 进阶分析**；客户已用数据选出 **Cursor 是 coding tool 首选**。  
**分析师四循环**：① **监控**已有 dashboard/query；② **调查**异常（可下钻客户/交易）；③ **故事化**给业务（需人指导「好故事」）；④ **影响**——改按钮、跑实验、再循环（端到端尚未完全自动）。  
**比邮件图表强在哪**：可 **按角色定制** 周报；Claude **总会读、总会追问**，不像 dashboard 被 ignore。  
**跨工具上下文**：Slack 事故 thread 能解释 metric 异常——**不只 warehouse**。  
**Demo 主线**：公开 **startup funding** 数据集 → 3 条「真实在跑的」SQL 作种子 → planning mode 生成 **Startup Funding MCP**（query tool + analyze tool + eval + token 护栏）→ 问「谁最可能 Series B」「哪个 AI coding tool momentum 最高」→ Cursor 排第一。  
**坑**：一条 query 可 **200 万行炸 context**；8 种客户分段全给会 **每次选不同字段**；应用 **data analysis Skill**（limit 50、timeout、join 披露）。  
**起步三板斧**：挑 core queries、写 domain context、再接到 Claude Code 或 Hex 等 BI。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Claude Code = 写应用代码 | **数据域 MCP + Skills** = 分析师 harness |
| RAG / BI 自带 AI | 仍要 **人定 queries 与语义层**；AI 不会凭空懂表结构 |
| 上下文工程 = prompt 技巧 | 数据分析特有：**结果集 token 爆炸**、窄 segmentation |
| MCP 连数据库即可 | 要 **从 Snowflake 历史 query / dashboard 反推** 种子 SQL |

---

## 分话题讲

### 1. 数据分析师四步循环：AI 能接哪几棒

**说法：**

| 阶段 | Agent 能力 | 人的角色 |
|------|-----------|----------|
| **监控** | 代跑 query、读 trend、摘要 dashboard | 定监控什么 |
| **调查** | 下钻 + Slack/Linear 等 **外部上下文** | 定 investigation 方向 |
| **故事化** | 侧向深挖、补 Google Doc 评论里的洞 | **教什么是好故事** |
| **影响** | 查 codebase 历史实验、估 impact | 批准改产品/跑实验 |

**例子：**  
PM 把现有 dashboard 的 query **扔进 Claude Code 每天/每周跑**——数据人 cut out，但 PM **问题更好**，数据人做更深分析。

**和你何干：**  
别指望一个 prompt 端到端；**先自动化最烦的监控与 boilerplate SQL**。

---

### 2. 周报 vs Dashboard：为什么「有人读」 matters

**说法：**  
传统周一邮件/charts：有人扫一眼，有人 ignore。Claude 版可 **按职能定制**（只看某产品线用户），且 **「Claude 总会读、总会提 follow-up 问题」**——甚至尝试 **自己答** 那些问题。

**例子：**  
Brex 内部 weekly review：metric 变了，Agent 去 Slack 发现 **data incident**，解释「不是客户流失，是 pipeline 坏了」——省周一早上 panic。

**和你何干：**  
Agent 监控的价值 = **interpretation + 跨源关联**，不是多一张静态图。

---

### 3. 为什么用 MCP：Rails 给所有人同一起点

**说法：**  
没有 MCP：每人扔 ad-hoc SQL，**没有数据团队文档化的 join 模式**。  
MCP = **结构化、可重复** 地连 Snowflake，让 PM/工程师 **从同一套 rails 起跑**，再偏离。  
起步：**一个 domain 3 条 query**（含 join、典型分析，如 funding velocity）；从 **Snowflake query history / 现有 dashboard**  scrape，别让 Claude 瞎编没人用的 SQL。

**Demo prompt 要素：**  
建 startup funding MCP → weekly reporting + deep dive + trend monitor → **3 条 eval 问题** → planning mode 澄清（本地 vs prod、alerting 等）。

**和你何干：**  
数据 MCP 的第一性原理：**capabilities（能问什么）**，不是自然语言问题列表。

---

### 4. 数据分析 Agent 特有问题：Context 管理

**说法：**

| 问题 | 原因 | 对策 |
|------|------|------|
| **Token 爆炸** | 一条 query 1 万～200 万行进 context | 指令里写 **LIMIT**、分步分析；提醒「上条有 limit ≠ 全表」 |
| **分段混淆** | 8 种 customer segmentation 全给 | **Tight semantic context**：一次只暴露一种 |
| **字段歧义** | 列名/doc 不清；同义不同名 | 显式命名、synonym、**表文档给 Agent 看** |
| **只有数没有事** | 缺 Slack/Jira 等 | 接 **Glean MCP**；**每个连接建 subagent** |

**和你何干：**  
写 doc / navigate codebase 的 Claude 套路 **不能直接 copy** 到 analytics——第一步就可能炸窗。

---

### 5. Live Demo：Series B 预测与 Cursor momentum

**说法：**  
MCP 建好后：  
- 「最近 Series A 谁最可能 Series B？」→ 结合 **金额、行业（AI vs healthcare 61% vs 73%）、velocity query**。  
- 「哪个 AI coding tool momentum 最高？」→ **Cursor #1**（大 Series A、A16Z 等）；数据集局限：公司改名、被收购会 **丢 thread**（如 Windsurf/Cognition 混淆）。

**Brex 支出侧：**  
Cursor **startup + enterprise 双杀**；OpenAI enterprise 强（ChatGPT Pro 渗透）；Anthropic **startup 产品内嵌 agent 选 Claude** 多；ElevenLabs 是 **voice 附加首选**。

**和你何干：**  
**三条种子 query** 决定 MCP 上限——质量 > 数量；eval 问题要 **domain 相关**。

---

### 6. 护栏：Skills 防 PM 拖垮库

**说法：**  
PM 自助 fear：**random query 打挂库** + **token 成本失控**。  
**data analysis Skill**：强制 limit 50、join 超时 2–3 分钟 kill 重写、**computational story mapping**（SQL 当叙事链）、导出 CSV skill。  
PM 用 Skill → 数据人 review **join  leaps** 再 productionize。

**和你何干：**  
Self-serve analytics = **MCP + Skills 护栏 + 数据人可见的 join 披露**，不是裸 Claude。

---

### 7. 入门三步（TL;DR）

**说法：**  
1. 定 domain，挑 **2–3 条真实在用的 core queries**（含 join + 一条稍复杂分析）。  
2. 写 **context**：表含义、为何 business care、common joins。  
3. 进 Claude Code MCP，或 **同一套 context 灌进 Hex 等 BI**——AI BI 工具也不会替你做这步。

**和你何干：**  
数据团队新 scope：**semantic layer for agents**，和给人看的 dashboard 同等重要。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Monitoring agent** | 代跑已有 query、解读 trend |
| **Startup Funding MCP** | Demo 中 Snowflake 融资域工具包 |
| **Tight semantic context** | 一次只给 Agent 一种客户分段/语义层 |
| **Seed queries** | 从生产 query history 挑出的 MCP 模板 SQL |
| **Data analysis Skill** | limit/timeout/join 披露的护栏技能包 |
| **Glean MCP** | 企业内 Slack/Drive 统一检索接 Claude |
| **Computational story mapping** | 把 SQL 步骤当叙事链，非孤立查询 |
| **Self-serve analytics** | PM 用 MCP+Skill 查数，数据人审 productionize |

---

## 值得记住的原话

> **"Recreating the way a data scientist actually thinks… not just the data, all the things outside of that."**  
> 复刻数据科学家怎么想——不只有数，还有数外面的东西。

> **"Claude will always read it. Claude will always start to ask questions."**  
> Claude 总会读周报，总会往下追问。

> **"One query might return 2 million rows… blowing up your entire context window."**  
> 一条查询两百万行，整个 context 窗会炸。

> **"If you start to give it all eight segmentations, Claude gets confused."**  
> 八种分段全塞进去，Claude 会乱选。

> **"Those three or four queries… really important… reuse them each time."**  
> 那三四条 query 才是核心——每次都在复用这些模式。

> **"Customers on our platform have already picked it — definitely Cursor."**  
> 我们客户真实支出已经选了——就是 Cursor。

---

## 小结

**这期最核心的判断：** Claude Code 做数据分析，.harness 核心是 **MCP rails + 窄语义 context + 结果集 token 管理**；Agent 价值在 **监控解读 + Slack 等外源**，不是替代数据科学家讲故事与定实验。

**读完应带走：**
- 四循环里 **监控/调查** 最先自动化；故事与实验仍要人。  
- MCP 从 **真实 query history** 长出来，带 eval 与 limit 指令。  
- **Skills** 给 PM self-serve 上锁，别裸跑大 join。

**和 vault 的关系：** Claude Code 实战 + 上下文工程交叉，接 [[OpenAI员工-上下文工程和Agent记忆]]、[[Databricks-企业级Agent生产实践]]。

---

## 行动启示

1. **Scrape 3 条生产 query** 作 MCP 种子，别让 Agent 发明没人用的 join。  
2. **System prompt 写清**：大结果集先 LIMIT、注明「带 limit 的结果≠全表」。  
3. **一次一种 segmentation** 暴露给 Agent，文档写 synonym 防歧义。  
4. **接 Slack/Jira MCP**，调查阶段才像真人分析师。  
5. **Publish data analysis Skill** 给 PM：limit、timeout、join 说明模板。

---

## 相关阅读

- [[OpenAI员工-上下文工程和Agent记忆]] — trim/compact/summarize 与长期记忆模式  
- [[Manus创始人-深度干货-上下文工程的最佳实践]] — Context Engineering 另一视角  
- [[Claude Code负责人-AI原生团队如何使用AI]] — Anthropic 内部 Agent 工作流  
- [[Databricks-企业级Agent生产实践]] — 企业级 Agent 生产  
- [[MOC - Agent Theory and Design]] — Agent 理论横切索引  

---

## 来源

- **视频**：[BV1Mpf9B5Egk](https://www.bilibili.com/video/BV1Mpf9B5Egk/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Brex 数据团队工程师（访谈）  
- **时长**：~51:46  
- **转写**：Recastory `bilibili-retranscribe/BV1Mpf9B5Egk/`（FunASR SenseVoice + cam++，**asr v2 后处理** 57 段）  
- **公开数据**：Brex Blog 月度 AI 支出 benchmark（视频中提及）  
- **版本**：v2 读者向讲义（2026-07-02）
