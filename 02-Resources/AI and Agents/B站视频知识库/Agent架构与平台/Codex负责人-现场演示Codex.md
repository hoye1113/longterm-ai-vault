---
title: "Codex负责人：现场演示 Codex"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV12qTu6WETP/"
speaker: "Thibault (OpenAI ChatGPT Codex & API 负责人)"
duration: "31:08"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - codex
  - openai
  - skills
  - harness_engineering
created: 2026-07-02
description: "OpenAI Codex 负责人 Thibault 谈 knowledge work 转型、elder review、并行 agent 工作流，并现场演示 email/Slides/LinkedIn/voice dictation。"
transcript_source: "Recastory/workspace/knowledge/A8-codex-demo/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Codex负责人：现场演示 Codex

## 先搞懂这一期

**这是什么节目？**  
Deep Dive Podcast 对话 **Thibault**——OpenAI **ChatGPT Codex 与 API** 负责人，团队 powering 大部分你已用的 OpenAI AI。整期约 31 分钟，**对话 + 现场 demo**，不是单人演讲。

**这期在回答哪三个问题？**

1. **Knowledge worker（营销、运营、创作）的工作方式，接下来 6 个月会怎么变？** 和软件工程一样被 AI 改吗？
2. **今天就能部署的 agent 工作流长什么样？** 并行 thread、cron、computer use 具体怎么用？
3. **人还要负什么责？** vibe coding 能走多远？未来还要会 prompt 吗？

**用一条线串起来（没看视频也能复述）：**

Google 说 **75% 代码已是 AI 写的**——Thibault 判断：**同样的事 6 个月内会扩散到所有 knowledge work**，不是因为人变了，是因为 **agent 终于可靠了**：长 horizon、100+ plugins、computer/browser use，非 technical 用户也能用。

过去 agent 不可靠，得 technical 调配置；现在 GPT-5 级 **extremely reliable**。Marketer 可以说「每 12 小时跑市场研究，发 PDF 邮件」——半年前还算 advanced，现在 **trivial**。

**责任在人**：你 ship 的 code/content，坏了是你的错，不是 agent 的。augment，不 replace team。

现场 demo：**并行 agentic threads**（email triage、Codex 产品动态、calendar 行程、Google Slides）；**computer use** 抓 LinkedIn analytics 进 spreadsheet；帮 host 修 content app 的 **voice dictation**（今天要 API key，3 个月 mainstream）。

未来 3–5 年：**dramatic change**——benefits 不再 proportional to prompt skill，像好裁缝一眼懂你；**ambient intelligence** 支撑社会。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 会用 ChatGPT 聊天 | **Codex = 全功能 agent**：browser、computer use、100+ plugins，不是纯对话 |
| 听过 software engineering 被 AI 改 | **同样 pattern 将到 knowledge work**——cron、chief of staff、50%+ 任务已 non-technical |
| 听过 Claude Code / Cursor | OpenAI 侧 **parallel threads + elder review + skill 封装 workflow** 的产品形态 |
| 担心 AI 替人、责任归属 | **Humans remain responsible**——augment 框架，vibe coding joy build OK，scale 需 technical partner |

---

## 分话题讲

### 1. Knowledge work 的 six-month transformation

Thibault 核心判断：**technology matured more than people need to change**。

Marketer 日工作拆解举例：

- 1 小时 market research → **cron 每 12h** 自动研究 → email/PDF  
- 1 小时 summarize emails  
- 2 小时 prospect 筛选  

「Advanced」概念如 **cron schedule**，6 个月前还算高阶，现在 natural language 就能说：「run every twelve hours, do market research, send PDF email」。

Executive 趣味：Slack 新闻 **每天打印到物理打印机**——newspaper 隐喻将 mainstream。

**和你何干：** 不必等「成为 power user」——技术 maturity 到了，**今天就能部署 cron research / inbox triage**。

---

### 2. Morning dashboard 与 Elder review

Craig 播客式愿景：**wake up, coffee, approve what AI did overnight**——Thibault：**not far off, technology exists, packaging problem**。

上周发布 **elder review**：

- **Main agent** 执行 actions  
- **Second agent verify** 所有 actions——过滤 harmful / 低 risk  
- Safety/alignment 团队创新 → 允许 agent **更长 autonomous**，甚至 handling sensitive data  
- 有了这层 safety，用户愿给 agent **更多 life access**

**和你何干：** 敏感任务（email、付款、对外发布）可借鉴 **双 agent verify** 或 human batch approve 心态。

---

### 3. 组织 Agent 数据：examples beat explanation

Starter 问：agent 需要 good data；tone of voice doc 不够，还要 strategy docs。

Thibault 个人：**local tidy folders**，agent 帮 organize；**3 个月 cloud**——travel 时 phone vs laptop **同一 agent entity**，非两个 separate legal entities 要分别 map。

Must-have files：

- **Tone of voice = examples**——past newsletters、recording snippets、professional vs personal messages——**不推荐抽象解释语气**  
- Per-project folders（thousands notes）  
- 也可 **pull from existing apps**（Notion/Slack…）不必全 file  

Multi-machine today：Google Drive 等 workaround；cloud memory coming。

**和你何干：** 给 agent 的「语气文件」= **粘贴历史写作样本**，别写抽象 tone doc。

---

### 4. 责任 dilemm：taxes、team、verification burden

Host：**AI 可做 taxes** + monthly automation 提醒策略——**want to be responsible?** 现有 entrepreneur **不因此 fire team**，而是让人 **use agent**。

Thibault：

> Humans remain responsible... if you produce code, you are responsible... it's your fault, not the agent's.

**Augment your own capabilities**——boring parts automatic；human **remain in control, understand entire system**。

Pitfall：**fall too much into using for everything** before capability curve——pushing boundary good（discover reliable vs 3–6mo），但 brain explode from over-automation portfolio。

**和你何干：** 生产环境 code/content 必须 **人 understand & sign off**；团队不裁，让人 **用 agent 提效**。

---

### 5. Vibe coding：joy vs scale

Host 团队：technical person + non-technical **vibe coders**——300 word English app usable，extend 1000 words **architecture wrong**。

Thibault：

- **Share with couple people / joy build** → agent alone **perfectly fine**  
- **Scale hundreds of thousands users** → **technical person in mix so useful**  
- **6–9 months** significant **long-term maintainability** improvements——may reduce need for constant technical handholding，not eliminate  
- **Explosion of infrastructure/apps**——creative people prototype fast；**demand for technical folk** hard to cap  

Creative + good ideas = **great time to experiment**。

**和你何干：** prototype / joy build 放心 vibe code；要 scale 到大量用户，**请 technical partner 进架构**。

---

### 6. Live demo：Parallel agentic threads

Thibault 现场 **multiple parallel threads**：

1. Podcast email in inbox → triage  
2. Popular sources → **Codex shipped last 2 weeks** breakdown  
3. Calendar → trip plan suggestion  
4. 「Making presentation in Google Slides」→ agent prepares deck  

UI：see which thread still working；可 **stop** sensitive one（「don't want changes to your inbox」）。

Host **content repurposing app**（morning GPT idea #5）：link md files → newsletter；wanted **dictate into app**——built fancy, simplify；**voice broken**。

Thibault fix live：**integrate OpenAI speech-to-text API**——need API key today（dev 可 mock），read docs——**sophisticated problem host wouldn't think of**——**still need someone little technical today; mainstream in ~3 months** auto-connect OpenAI account。

Agent **didn't wait**——built A/B test newsletter drive proactively。

**和你何干：** 一 session **多 agentic 线并行**：email、slides、analytics 同时跑；敏感 thread 随时 stop。

---

### 7. Computer use：LinkedIn analytics

**Fastest computer use**——surprisingly quick click navigate。

Demo：computer tool → LinkedIn → load analytics → **spreadsheet** impressions/proposals。

Can **run again** more specific columns——workflow you like → **create skill run daily**（skill creator）。

Codex vs ChatGPT：**full agent, browser, computer**——not just chat。

**和你何干：** 重复 analytics workflow → 让 Codex **create skill run daily**，复利式 personal BI。

---

### 8. Chief of staff 与 50% non-technical tasks

Sophisticated prompt example：**Gmail chief of staff**——important summary + prepare me；calendar **time audit**——hiring vs building where hours go optimization discussion。

Thibault personal use：

- Curating world thinks about Codex  
- **Strategize narrative order** of product pieces  
- **Organize notes into Codex** all day vs separate notes app → **memories build**  
- End of day prompt dump to doc  
- Stay on top email/Slack  

**>50% Codex tasks non-technical already**（app ~3 months; Codex AI ~1yr）。

Order DoorDash/shopping via computer use——fastest implementation **surprisingly quick**。

**和你何干：** Codex 已 **crossing the chasm** 到 knowledge workers——chief of staff、time audit 今天可试。

---

### 9. 3–5 年：dramatic change, prompt skill decays

> There is going to be dramatic change.

Future：**benefits whether or not you actively engage**——today benefits **proportional to prompt skill**；future like **good tailor** instantly gets you shine——**ambient intelligence supporting society**。

Engage as **authentic self in conversation**——not necessarily「ask right questions」but **natural conversation** → appropriate help at right time。

Depends on **packaging + memory + cloud same agent** more than prompt engineering skill.

**和你何干：** 不必焦虑 prompt 技巧——未来靠 **packaging、memory、authentic conversation**；但 **今天** 仍值得部署 workflow 练手感。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Codex** | OpenAI 全功能 agent：tools、browser、computer use、100+ plugins |
| **Agentic thread** | 并行独立 task stream（email、slides、research 各一条） |
| **Elder review** | 第二 agent 验证第一 agent 所有 actions，降 risk |
| **Cron automation** | 「每 12h 跑 research」等 schedule，natural language 即可 |
| **Tone examples** | 用历史写作样本定义语气，非抽象描述 |
| **Computer use** | Agent 操作 browser/desktop 完成任务 |
| **Human responsibility** | 产出物法律责任在人 |
| **Vibe coding** | 非工程师 agent 建 app；scale 需 architecture |
| **Skill from workflow** | 重复 workflow 封装为 skill daily run |
| **Ambient intelligence** | 不强 prompt 也受益的社会级 AI 支持 |

---

## 值得记住的原话

> **"Everyone is going to get their own little personal assistant on their computer that allows you to do more than whatever was possible three or six months ago."**  
> 人人会有电脑上的小私人助理，能做比三六个月前更多。

> **"In the future that will not be the case — you won't have to actively prompt and be creative."**  
> 未来不必靠主动 prompt 和创意提问。

> **"Humans remain responsible... if it breaks, it's your fault, not the agent's fault."**  
> 人仍负责——坏了是你的错，不是 Agent 的。

> **"I don't recommend trying to explain your tone of voice — I recommend including examples."**  
> 别抽象解释语气——给范例。

> **"Technology already exists — it's about packaging."**  
> 技术已有——差 packaging。

> **"Elder review... second agent verifying all actions of the first agent."**  
> Elder review：第二 agent 验证第一 agent 所有动作。

> **"Over fifty percent of tasks done on Codex are non-technical tasks today."**  
> Codex 上过半任务已是非技术。

> **"Like going to a nice tailor — instantly looks at you and makes you shine."**  
> 像好裁缝——一眼懂你让你发光。

---

## 小结

**这期最核心的判断：** Codex 侧判断 **agent 长 horizon + plugins + computer use 已可 today 部署**——知识工作将在约 6 个月内像软件工程一样被改写；**packaging 和 responsibility 在人**，不在模型缺能力。

**读完应带走：**
- Cron 研究、并行 threads、chief-of-staff 类 workflow 是 **现在就能上的** low-hanging fruit。
- Tone 靠 **范例** 不靠抽象描述；Elder review = 第二 agent 验证第一 agent。
- 过半 Codex 任务已非技术；你 ship 的 code/content **你负责**，vibe prototype 与 scale 要分阶段。

**和 vault 的关系：** 接 ai_coding 与 [[WorkOS-创建和使用Skills方法论]]——OpenAI coding agent 产品化与 skill 封装的对照。

---

## 行动启示

1. **Today deploy cron research/triage** — 12h market research、inbox summary 等 low-hanging automation。  
2. **Tone = paste examples** — newsletters/messages 进 project folder，别写抽象 tone doc。  
3. **Parallel threads** — 一 session 多 agentic 线：email、slides、analytics 同时跑。  
4. **Elder review mindset** — 敏感任务用 verify agent 或 human approve batch。  
5. **You remain responsible** — 生产环境 code/content 必须人 understand & sign off。  
6. **Scale = invite engineer** — vibe prototype OK；growth 架构靠 technical partner。  
7. **Repeat → skill** — LinkedIn brief 等 workflow 让 Codex **create skill run daily**。

---

## 相关阅读

- [[OpenAI官方-Codex新手教程]] — Codex CLI 入门与 AGENTS.md 体系  
- [[OpenAI评估团队-不再低估模型]] — capability 测量与 eval 对照  
- [[Cursor-128个Agent团队协作]] — 工程团队 agent 编排  
- [[WorkOS-创建和使用Skills方法论]] — workflow 封装为 skill  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV12qTu6WETP](https://www.bilibili.com/video/BV12qTu6WETP/)（B 站转载 Deep Dive Podcast × Thibault）  
- **嘉宾**：Thibault，OpenAI ChatGPT Codex & API Lead  
- **转写**：Recastory `A8-codex-demo/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
