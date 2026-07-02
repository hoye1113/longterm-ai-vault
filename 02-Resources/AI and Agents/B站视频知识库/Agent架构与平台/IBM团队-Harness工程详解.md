---
title: "IBM团队：Harness工程详解"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1eWGH6JE6m/"
speaker: "Tade / Ta (IBM AI Developer Advocate，姓发音类似 contagious)"
duration: "20:27"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - harness_engineering
created: 2026-06-09
description: "IBM 工程师 Tade 用 18 分钟演讲 + 现场 Hacker News 点赞 demo 说明：harness 的核心是可靠性；不改 prompt，靠 guardrails、verify、login handler 让 GPT-3.5 级模型完成任务。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1eWGH6JE6m/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# IBM 团队：Harness 工程详解

## 先搞懂这一期

**这是什么节目？**  
IBM AI Developer Advocate **Tade（Ta）** 在 AI 工程师大会上的 **~20 分钟主题演讲 + 现场 coding demo**。不是访谈，是一个人讲清楚概念，再 **incrementally 搭一个「baby harness」**。

**这期在回答哪三个问题？**

1. **为什么需要 Harness？** 我们大多数人是在「租」模型，黑盒 + 变量太多，怎么保证 Agent **可靠**？  
2. **Agent Harness 到底是什么？** 和 ML 里的 test harness、和「agent loop」有什么区别？  
3. **Harness 能强到什么程度？** 能不能 **不改 prompt**，只靠工程外壳，让 **故意选的很差的老模型** 完成真实浏览器任务？

**用一条线串起来（没看视频也能复述）：**

开场先问：有多少人真懂 harness？——今天目标让你离场能 **「oh I get it enough」**。  
**Why**：多数人不是 token billionaire，每月 $20 租 Claude Pro，context 有限、模型是 **黑盒**（甚至可能偷换版本）→ harness 的名字叫 **reliability**。  
**What**：登山绳 / 狗绳比喻 → 锚定在稳定环境，防止漂移。ML harness = 测试套件；今天讲的是 **AI agent harness** = **模型外一切让你 grounded in reality 的东西**（工具注册表、模型、context 压缩、guardrails、agent loop、**verify**）。  
**Demo 主线**（全程 **不改 user prompt / system prompt**）：用 **GPT-3.5-turbo** 做 browser agent，任务 = Hacker News **upvote 第一条**。  
- v0：点 upvote 遇 login → agent **撒谎说成功了**（没 verify）  
- +guardrails：max iterations、naive context 压缩  
-  refactor → `run_harness`  
- +**verify step**：查 trace 里是否真的 click 成功、是否 failed login → **不再撒谎**  
- +**login handler**：harness **确定性**填表登录（不是让 LLM 猜密码）→ **真的 upvote 成功**  
收尾：**OpenRAG** 企业 harness；**2025 agents → 2026 harnesses → 2027 dynamic on-the-fly harness**（agent 先给自己生成 harness 再干活，像 plan mode on steroids）。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Harness = 套在模型外的框架 | **第一性原理 + 现场 incremental build**；强调 **verify / 确定性步骤** 不是 prompt 技巧 |
| Claude Code / Cursor = coding agent | 它们 **也是 harness**（coding agent = harness 的一种） |
| 模型越强 agent 越强 | **同一 prompt**，换 harness 结果 **radically different**；差模型 + 好 harness 也能干活 |
| OpenAI Harness Engineering 文档 | IBM 侧 **reliability 叙事 + OpenRAG 企业 RAG harness** |

---

## 分话题讲

### 1. 为什么需要 Harness：租来的黑盒模型

**说法：**  
大多数人 **pay rent**——$20/月 Claude Pro，context 有限，模型是 **black box**（Opus 不可用时不一定知道被换成 Sonnet）。变量太多 **不可控** → harness 的游戏叫 **reliability**：不管租什么模型，**agent 该做的事要做对**。

**例子：**  
Anthropic/Google 员工可能是 **token billionaire**；IBM 用 Watson 也算沾边；**绝大多数开发者是租客**。

**和你何干：**  
你自己搭 agent 时，默认模型会变、会幻觉——**harness 是普通人的解法**，不是只有 frontier lab 才需要。

---

### 2. Harness 是什么：登山绳、狗绳、两种 harness

**说法：**  
- **登山 harness**：系在稳定的山上，不能 off the rails  
- **狗 harness**：狗不会跑出去 **bankrupt you with tokens**  
- **ML harness**：test suite + test runner，给输入看输出质量  
- **AI agent harness（本期重点）**：**everything around the model that gives it grounding in reality**——系在 **稳定环境** 上的那层

**和你何干：**  
术语在 ML / AI 圈 **含义不同**；谈 agent 时默认是后者。

---

### 3. Agent Harness 的六个 moving parts

**说法：**（以 Claude Code / Cursor / Codex 为例）

| 部件 | 作用 |
|------|------|
| **Tool registry** | 读文件、写文件、跑 bash 等 |
| **Model** | 有的可选模型，有的固定 |
| **Context 管理** | 几乎都会 **compact** 自己的 context——这是 harness 的活 |
| **Guardrails** | 如 max steps：超过 5 次 tool call **kill the run** |
| **Agent loop** | 有人以为 harness = loop；**错**——harness 是 **loop 外面的东西**，甚至可以是 **loop around your loop** |
| **Verify step** | 干完后跑 lint/test，或查 trace 验证是否真的成功 |

**和你何干：**  
设计 agent 平台时，问「verify 在哪一层」——不能只有 loop。

---

### 4. Demo 设定：故意用最差模型 + 永不改 prompt

**说法：**  
- Browser/computer use agent，Playwright（**不是** Playwright MCP，是普通工程代码）  
- 任务 prompt 极简：`upvote story`（Hacker News 第一条）  
- 模型：**GPT-3.5-turbo**（~2023，故意很差）  
- **铁律**：demo 全程 **不修改 prompt**，只加 harness 层

**第一跑结果：**  
打开 HN → 点 upvote → 撞 **login** → agent panic；更糟的是它 **声称成功**（实际没 verify）。

**和你何干：**  
「prompt 再狠一点」不是唯一出路——**没有 verify 的 agent 会 lying**。

---

### 5. Incremental harness 四步（demo 精华）

**Step 1 — Guardrails**  
- `max_iterations`（如 >6 step 就杀）  
- `max_messages` → 触发 **naive context 压缩**（只留 system + user + 最近 2 条 message）  
- 逻辑收进 `run_harness`，index 缩到 ~19 行

**Step 2 — Verify step + max attempts**  
- `run_harness` 最多试 3 次；核心逻辑在 `run_harness_attempt`  
- **`verify_successful_upvote`**（**确定性代码**，不是 LLM）：  
  - 查 trace：有没有 browser click upvote？  
  - 是否 **failed login**（tool 名 / message）？  
  - 是否在 login URL 且 autologin 没跑？  
- **结果**：仍可能失败，但 **不再撒谎**——「admit you have a problem」是 TDD 味的第一步

**Step 3 — Login handler**  
- 每个 agent loop 推 trace **之前**，查当前 URL  
- 若是 login 页 → harness **程序化填 credential + submit**（可走 env secret）  
- 给 agent queue 一条消息：「harness 已登录，你可以继续」  
- **结果**：登录 + upvote **真实成功**（现场可 unvote 验证）

**核心教训：**  
**整段 demo 没动 prompt**；改的是 **guardrails + verify + 确定性 login**——outcome **radically changed**。

---

### 6. 实践与展望：OpenRAG、年份预言

**OpenRAG（IBM 开源）：**  
大企业私有数据、敏感域做 RAG（teams / calls / PDFs / invoices）——**hell of a harness**，企业级安全。

**Cheap model + great harness：**  
Quinn、GPT-OSS 等 **免费/便宜模型** + 好 harness 也能走很远。

**时间线（演讲者观点，非 IBM 官方）：**  
- **2025**：year of agents  
- **2026**：year of **harnesses**（本场所在）  
- **2027**：**dynamic on-the-fly harnesses**——你说「帮我买票」，agent **先给自己生成 harness**（自知可能 hallucinate），再执行任务，类似 **plan mode on steroids**

**和你何干：**  
Harness 不是静态配置文件；未来可能是 **任务前动态生成** 的约束层。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Harness（AI agent）** | 模型外一切让 agent 锚定在可控环境上的工程（工具、guardrails、verify…） |
| **Reliability** | 不管黑盒模型怎么变，行为可预期 |
| **Token rent / Token billionaire** | 租 API vs 自有 frontier 算力 |
| **Black box model** | 不知底层是否换版、不可控 |
| **ML harness** | 模型输入输出测试套件 |
| **Verify step** | 用 trace/测试/规则验证「真的成功了吗」 |
| **Login handler** | harness 侧确定性登录，不让 LLM 瞎填密码 |
| **Guardrails** | max steps、context 压缩等硬限制 |
| **OpenRAG** | IBM 企业 RAG + harness 安全 |
| **Dynamic harness** | 任务前 agent 自生成约束层（演讲者 2027 展望） |

---

## 值得记住的原话

> **"The name of the game with harness is reliability."**  
> Harness 这门游戏的名字叫可靠性。

> **"We pay rent... $20 a month for Cloud Pro... The model you rent is a black box."**  
> 我们在付租金……模型是黑盒。

> **"The agent harness is everything around the model that gives it grounding in reality."**  
> Agent harness 是模型外一切让它锚定现实的东西。

> **"Isn't a harness just the agent loop? No, it's the stuff around the agent loop."**  
> Harness 不只是 agent loop，是 loop 外面的东西。

> **"We will not change the prompt at all... we're just going to build a harness and the outcome will change."**  
> 我们完全不改 prompt……只搭 harness，结果就会变。

> **"It lies... it doesn't verify — this is the job of a harness."**  
> 它在撒谎……因为没有 verify——这才是 harness 该干的。

> **"Step one to solving a problem is admitting you have one."**  
> 解决问题的第一步是承认有问题（verify 失败后不再假成功）。

> **"Fill in credentials programmatically from the harness, not from the agent."**  
> 由 harness 程序化填登录信息，不是 agent。

> **"I did not touch the prompt once... Built a harness. And the outcome radically changed."**  
> 我一次都没动 prompt……只建了 harness，结果彻底变了。

> **"2025 was the year of agents... 2026 is the year of harnesses."**  
> 2025 是 agent 之年……2026 是 harness 之年。

---

## 小结

**这期最核心的判断：** Harness 的第一性是 **reliability**——在「租来的黑盒模型」上，用 **工具 + guardrails + verify + 确定性 handler** 把 agent 系在稳定环境上；**改 harness 可以比改 prompt 更 radically 地改变结果**。

**读完应带走：**
- Agent harness ≠ agent loop；verify 和 login 这类步骤 **应该由确定性代码做**，不是全交给 LLM。  
- Demo 证明：**GPT-3.5 + 同一 prompt**，靠 incremental harness 也能完成 browser 任务——关键是 **不撒谎、能登录、能验证**。  
- 企业侧看 **OpenRAG**；时间线上从 agents → harnesses → **动态自生成 harness**。

**和 vault 的关系：** Harness 主题入口，接 [[MOC - Harness Engineering]]、[[DeepMind-模型将吞噬Harness]]、[[2026 年 Agent 最重要的工程概念 Harness Engineering]]。

---

## 行动启示

1. **先加 verify 再谈 prompt**：任何 browser/tool agent 查 trace，失败要 **显式 fail**，不要信模型自述成功。  
2. **敏感动作 harness 化**：登录、付款、发邮件——**确定性 handler + secret**，别写进 system prompt。  
3. **Guardrails 当默认**：max iterations、context 压缩是 harness 基础款，不是高级功能。  
4. **差模型 + 好 harness** 值得试——别默认只有换 Opus 才能做任务。  
5. **读 diff 而非 live code**：演讲也强调现在工程是 **inspect diffs**；你的 agent 平台也要让人类审 diff/trace。

---

## 相关阅读

- [[MOC - Harness Engineering]] — Harness 横切索引  
- [[DeepMind-模型将吞噬Harness]] — Google 侧 harness 会被模型 upstream 吗  
- [[2026 年 Agent 最重要的工程概念 Harness Engineering]] — OpenAI 侧 harness 实验  
- [[DeepMind团队-当数百万Agent相遇]] — harness 与 agent 社会、human-in-the-loop  
- [[Cursor副总裁-构建软件开发过程的Agent]] — Cursor 把 harness 扩到 SDLC 各阶段  

---

## 来源

- **视频**：[BV1eWGH6JE6m](https://www.bilibili.com/video/BV1eWGH6JE6m/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Tade（Ta），IBM AI Developer Advocate  
- **时长**：~20:27  
- **转写**：Recastory `bilibili-retranscribe/BV1eWGH6JE6m/`（FunASR SenseVoice + cam++，**asr v2 后处理** 19 段）  
- **Demo 代码**：演讲提及 slides on GitHub（现场 poor man's harness 仓库）  
- **版本**：v2 读者向讲义（2026-07-02，IBM 试点闭环）
