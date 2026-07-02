---
title: "LCA：60 分钟变成 AI-Native"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1MFjN6iEFU/"
uploader: "Easonlee的AI笔记"
speaker: "Theo Tabah (LCA 联创)"
saved: 2026-07-02
tags:
  - ai_agent
  - ai_career
  - video_transcript
  - bilibili
  - skills
  - context_engineering
created: 2026-07-02
description: "LCA 联创 Theo 的 AI-Native masterclass：People+Agents+Context 三层架构、Skill Chain、Brain 上下文闭环，把提案与原型从数天/数周压到分钟级。"
transcript_source: "Recastory/workspace/knowledge/B5-lca-ai-native/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# LCA：60 分钟变成 AI-Native

## 先搞懂这一期

**这是什么节目？**  
Greg Isenberg 请 LCA 联创 **Theo Tabah** 做 **<60 分钟 AI-Native masterclass**。Theo 帮 Fortune 2000 做 AI 产品与 AI-Native org 转型——这期是他把内部「操作系统」摊开讲。

**这期在回答哪三个问题？**

1. **AI-Native 到底是什么？** 和「ChatGPT 重度用户」差在哪？
2. **三层架构怎么跑？** People、Agents、Context（Brain）各自干什么、怎么连起来？
3. **速度从哪来？** Skill Chain + Brain 闭环，怎么把 proposal / prototype 从数天压到分钟？

**用一条线串起来（没看视频也能复述）：**

**AI-Native org 三 bullet**：人管 agent；agent 读写公司；公司越跑越聪明。只用 ChatGPT ≠ AI-Native——像有网站就自称 tech company 一样 gap 巨大。

**People 层**：AI **吃中间 execution**；人守两端——定方向、deploy judgment/taste、终审。**每个人都是 manager**——不是新工具（Salesforce），是 **unlimited employees**，要把 agent 设到能成功。

**Agents 层**：自治分 L1（纯 chat）→ L4（数天/周少 oversight）。自治要四要素：**Goal、Skills、Tools、Context**——缺一则 first-day-on-job 必败。**Eval** = 看见 agent 做了什么、产出几/10。

**Context / Brain 层**：capture（cron hourly: Slack/meetings/email）→ curate（librarian + trigger 如 RFP）→ store → execute → signal 回写。**Human gate**：未审 agent 产出不回流 brain，防污染。

**Live demo**：Spotify 假案例——**Proposal Skill Chain**（microsite → copy → QA，~3 分钟，从 months-old meeting 抽「record store clerk, trust me」写进提案）→ 语音描述 **Daily Blitz** retention feature → ~10 分钟 **functional prototype**（非 Figma）→ usability test → synthesize → plan v2 **同 session**。

Demis Hassabis 警告：**朝错方向 100 mph 比站着不动更糟**——speed 必须 of your customer。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 会用 ChatGPT / Claude | AI-Native = **People + Agents + Context** 操作系统，不是聊天频率 |
| 听过 Skills / MCP | **Skill Chain**——单 skill 停在中等质量；macro skill 串 playbook |
| 听过 context engineering | **Brain** capture→curate→execute→signal 闭环 + human gate |
| 听过 a16z「native AI 应用」 | **组织级实操**：proposal 3 天→分钟，prototype 1–2 周→10 分钟 |
| 做多 Agent 并行 | LCA 偏 **orchestrator + skill chain + context**；与 RTS 式 token maxxing（YC 论文 5）可对照 |

---

## 分话题讲

### 1. AI-Native 定义：不是 ChatGPT power user

> **"Just using ChatGPT does not make you an AI native company or an AI native person."**

**AI-Native org 三 bullet**：

1. **People manage agents**
2. **Agents read and write to the company**
3. **The company gets smarter over time**

解锁 **speed** + **market signal** → moat。有网站 ≠ tech company；ChatGPT ≠ AI-Native。

Theo 开场用 Demis Hassabis 传记故事定调：DeepMind 联创、AlphaFold、被 Google 收购——AI 能力集中在一处 Elon 觉得太危险，才催生 OpenAI 叙事。Demis 在 Google 说过：**朝错方向 100 mph 比站着不动更糟**——speed 必须 **of your customer**，不能为快而快。

---

### 2. People：AI 吃中间，人守两端

| 时代 | 时间分配 |
|------|----------|
| Pre-AI | 中间 **execution** 占大头；strategy / review 被挤 |
| AI-Native | AI 做中间 execution；人专注 **定方向、deploy judgment/taste、终审** |

> **"Everyone is a manager now."**

Reframe：不是新工具（Salesforce/Excel），是 **unlimited employees**——把 agent 设到能成功，像 Andy Grove 说的 manager 成功 = team output。

Book ends（strategy + review）才是「真正重要的工作」——AI 解放你回到这两端。

---

### 3. Agents：四级自治 + 四要素

| 级别 | 状态 |
|------|------|
| L1 | 纯 chat（ChatGPT/Claude） |
| L2 | Agent 跑，人点 approve |
| L3 | 半自治 |
| L4 | 数天/周少 oversight，「nailing it」 |

**自治四要素**（Boris Cherny, Anthropic：agents = models using tools in a loop）：

- **Goal** — success 长什么样、何时完成、如何衡量
- **Skills** — SOP、quality bar 封装成 markdown skill
- **Tools** — MCP、API、环境
- **Context** — 公司 **readable to agents**

缺一则 first-day-on-job 必败：walk in 第一天就要做 board deck，没 goal/skills/tools/context 全 fail。

**Eval** = 看见 agent 做了什么、怎么到的、产出几/10 vs desired output——来自 skills + goal + context 组合。

---

### 4. Skill Chain：单 skill 不够，要串 playbook

单 skill 停在中等质量；**Skill Chain** = skill1 → 调 skill2 → skill3（macro skill）。

**Proposal flow**（~3–4 分钟，normally 由 trigger 自动 fire）：

1. **Microsite skill** — elevated proposal，非 email 纯文本
2. **Copy skill** — 像 Theo 说话，不像 AI
3. **QA skill** — 不 overpromise、不 hallucinate、只从 transcript/data 拉

Brain 检测 RFP（meeting transcript / inbox）→ 自动 fire → Slack ping Theo 审阅。

Demo 亮点：从 months-old discovery call 抽 **「record store clerk who knows you, trust me」** 写进 Spotify 假提案——**perfect context** 做 human 没时间做的 personalization。

> **"This has been the result of millions of dollars of revenue."**

Sales 关键：**strike while iron is hot**——传统 proposal 要 days（翻 notes、对齐 team）；AI-Native **minutes**。10:37 收到 Slack ping，proposal 已 ready。

---

### 5. Context / Brain：capture → curate → execute → signal

**Problem**：Greg 连 LCA SOP、两周前 hire、StumbleUpon 2014 strategy 都答不出——大 org **blind**。

> **"Make your company readable to agents."**  
> **"You essentially give agents twenty-twenty vision of the right company."**

**Brain** = agent-readable context layer（folder tree + markdown + README 引导 agent 检索）：

```
Capture（cron hourly: Slack/meetings/email/boards）
  → Curate（librarian：什么进 brain、什么 ignore、trigger 检测如 RFP）
  → Store（brain folders）
  → Execute（agents + skills + goals）
  → Signal（客户反馈 → 回流 brain）
```

**Human gate**：未审 agent 产出不回流 capture——避免污染 context。人管 agent 时说的 corrections、lessons 会写回 skills/memory。

**Traces/exhaust**：proposal/prototype 过程中的 decision、cutting-room-floor 文档回流 brain，别进 file graveyard。

Theo 对比 Notion AI 等：**search + context + agent** 一体但略 black box；LCA 选择自建 brain 可控。可加 permissions，让对的人看对的信息。

---

### 6. Demo：Daily Blitz prototype + usability test chain

语音描述 Spotify retention feature（daily mini playlist「Daily Blitz」，三首 hand-picked 歌 + 解释 + 分享）→ **~10 分钟** functional prototype（非 Figma mock）+ **Labs page** 托管。

Skill chain：**Hypothesis → Build prototype → Usability test → Feedback synthesize → Plan v2**

Usability test：类 researcher 引导用户走 workflow、打分——link 发 community，多人填完 → one-click synthesize → plan v2 execute **同 session**。

| 任务 | Before | After |
|------|--------|-------|
| Proposal | 3 days | minutes |
| Clickable prototype | 1–2 weeks | ~5 min + feedback |
| Usability + v2 | weeks | same session |

无 LCA 六年 context？**Mobbin MCP** + design system skill + 自建 md context——「world is large and lovely」。

> **"AI loves to fake it till they make it. Your job is to make sure they don't fake it."**

---

### 7. 创业：TVD × Industry × Function × Size

Services 最热市场：**30-day AI acceleration sprint**（TVD）。

三维 niche：

- **Industry** — restaurants（fragmented, hot）、commercial real estate…
- **Function** — 谁 team
- **Company size** — 太小无 budget

策略：**high-frequency niche workflows first** → 再 general、再 low-frequency high-ROI。Greg newsletter 框架：**niche → general** × **low freq → high freq**。

LCA 做 Fortune 2000，但 Theo 认为 **大量其他 market** 没人做——Industry × Function × Size 切 niche 是 layup。

Closing：**用「管 agent + agent 成功所需」的 lens 思考，你就领先世界上大多数公司。** 别被「必须 technical genius」吓住——scrape your knee and get stuff done。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **AI-Native org** | 人管 agent；agent 读写公司；系统持续 learning |
| **Skill Chain** | 顺序 fire 多 skill 的 macro playbook |
| **Brain** | Agent-readable 公司 context（folder + md + README 导航） |
| **Capture / Curate** | Hourly ingest + librarian 过滤 + trigger 检测 |
| **Eval** | 看见 agent 路径与产出质量 |
| **Human gate** | 未审产出不污染 brain |
| **Traces / exhaust** | 决策过程、cutting-room-floor 回流系统 |
| **TVD** | 30-day AI acceleration team sprint |

---

## 值得记住的原话

> **"Just using ChatGPT does not make you an AI native company."**  
> 只用 ChatGPT 不会让你成为 AI-Native 公司。

> **"Running a hundred miles an hour in the wrong direction is worse than standing still."** — Demis Hassabis  
> 朝错方向 100 mph 比站着不动更糟。（Demis Hassabis）

> **"Everyone is a manager now."**  
> 现在每个人都是 manager。

> **"Agents for models using tools in a loop."** — Boris Cherny  
> Agent = 模型 + 工具 + 循环。（Boris Cherny, Anthropic）

> **"Make your company readable to agents."**  
> 让公司对 agent readable。

> **"AI loves to fake it till they make it. Your job is to make sure they don't fake it."**  
> AI 爱 fake it till make it。你的 job 是 minimize 这个。

> **"This has been the result of millions of dollars of revenue."**  
> 这带来了数百万美元 revenue。

> **"Strike while the iron is hot."**  
> 趁热打铁。

> **"You essentially give agents twenty-twenty vision of the right company."**  
> 你给 agent 对公司 perfect vision。

> **"Think through the lens of managing agents and what those agents need to succeed."**  
> 用管 agent 的 lens 思考，你就领先大多数公司。

---

## 小结

**这期最核心的判断：** AI-Native ≠ ChatGPT 重度用户——是 **People + Agents + Context（Brain）** 与 **Skill Chain**；组织要 **让公司对 agent readable**，并防 agent fake it till make it。

**读完应带走：**
- 人人是 manager；Agent = 模型 + 工具 + loop，缺 Goal/Skills/Tools/Context 任一都会假忙。
- Proposal 3 天→分钟、prototype 1–2 周→~10 分钟是 **Brain + skill chain** 的 compound 结果，非单点模型 magic。
- Traces 与 decision log 要回流 Brain，别进 file graveyard；**strike while iron is hot** 是窗口期判断。

**和 vault 的关系：** 接 skills、harness 与 [[WorkOS-创建和使用Skills方法论]]——把 a16z 宏观叙事落到 org 操作系统。

---

## 行动启示

1. **Audit**：ChatGPT user vs AI-Native org——差在 context + skill chain，不是模型版本。
2. **给 agent 四要素 checklist**：Goal / Skills / Tools / Context 缺什么补什么。
3. **建一条 Skill Chain**：从最高频 workflow（proposal / PRD / QA）开始，别停在单 skill。
4. **Brain capture routine**：hourly cron + curate rules + human gate。
5. **Eval 可见**：agent 路径 + 质量 bar 写进 skill，不盲信输出。
6. **Traces 回流**：decision log 别丢进 file graveyard。
7. **无 mega context 可用 Mobbin MCP + UI skills** 补 design 参考。
8. **Services 创业**：Industry × Function × Size × high-frequency niche workflow。

---

## 相关阅读

- [[Claude Code负责人-AI原生团队如何使用AI]] — Anthropic 团队 AI-native 实践
- [[WorkOS-创建和使用Skills方法论]] — Skills 组织级方法论
- [[Manus创始人-深度干货-上下文工程的最佳实践]] — 上下文工程
- [[Cursor-128个Agent团队协作]] — 多 Agent 并行视角
- [[a16z-AI并非泡沫]] — native AI 应用 vs skeuomorphic 提效（投资侧 prior）
- [[MOC - AI 时代个人发展与组织]] — 组织转型横切索引

---

## 来源

- **视频**：[BV1MFjN6iEFU](https://www.bilibili.com/video/BV1MFjN6iEFU/)（B 站转载 Greg Isenberg × Theo Tabah）
- **嘉宾**：Theo Tabah，LCA 联创
- **转写**：Recastory `B5-lca-ai-native/article.md`（英文 ASR，收录时已人工整理叙事）
- **版本**：v2 读者向讲义（2026-07-02）
