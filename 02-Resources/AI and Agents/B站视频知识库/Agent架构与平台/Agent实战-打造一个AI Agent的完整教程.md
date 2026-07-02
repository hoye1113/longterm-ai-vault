---
title: "Agent实战：打造一个AI Agent的完整教程"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1PnQfBvEs3/"
speaker: "Remi Gasiglia（AI Agent 教育者）/ Greg Eisenberg（主持人）"
duration: "58:54"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - skills
  - mcp
  - harness_engineering
  - context_engineering
  - claude_code
  - codex
created: 2026-06-09
description: "Remi 用 ~59 分钟从零讲清 chat vs agent、Observe-Think-Act 循环、harness、agents.md、memory.md、MCP 与 Skills，现场搭 Executive Assistant 并演示跨 Claude Code/Codex/Antigravity 同一套本地 markdown 栈。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1PnQfBvEs3/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Agent 实战：打造一个 AI Agent 的完整教程

## 先搞懂这一期

**这是什么节目？**  
Greg Eisenberg 播客上的 **~59 分钟 Agent 入门 crash course**。嘉宾 **Remi Gasiglia** 面向完全新手，用「公司部门 + 本地文件夹 + .md 文件」把 agent 概念拆到能动手搭。

**这期在回答哪三个问题？**

1. **Agent 和 Chat 到底差在哪？** 为什么 founders 用 agent 号称日常 **10–20×** 产出？  
2. **Agent 里面在转什么？** Loop、harness、LLM、工具、上下文各是什么关系？  
3. **初学者今天能搭什么？** 如何用 **agents.md + memory.md + MCP + Skills** 做出一个 Executive Assistant，并扩到整家公司？

**用一条线串起来（没看视频也能复述）：**

AI 进入 **stage two：从 chat 到 agent**。Chat = **question → answer**（乒乓球）；Agent = **goal → result**（你给任务，它 plan → execute → 交付）。  
内核是 **Observe → Think → Act** 循环，跑在 **agent harness**（Claude Code / Codex / Cowork / Manus 都是不同「车」）。  
搭 agent = ** onboard 员工**：先 **agents.md**（角色 + 业务上下文），再 **memory.md**（跨 session 偏好），**MCP** 接 Gmail/Calendar/Notion/Stripe，**Skills** 把重复 SOP 封成 `.skill`。  
Remi 的工作区 = 每家公司一个文件夹，下面 **Executive Assistant / Head of Marketing** 等子目录，各自 **CLAUDE.md + skills + MCP + context**；未来是人人一套 **AIOS**，人不再进 SaaS，只坐在 harness 里指挥。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Agent = 会调工具的 LLM | **Chat vs Agent 范式** + **Observe-Think-Act** 可观察循环 |
| Harness = 外壳框架 | **学车比喻**：会开一辆就能换 Claude Code / Codex / Antigravity |
| Prompt 工程 | **Context 工程**：prompt 可以极短（「写 cold email」），靠 agents.md 撑质量 |
| MCP 是连接器 | **翻译器比喻**（Ross Mikita）：LLM 说英语，Notion/Gmail 各说各语，MCP 居中翻译 |
| Skills 是 Claude 功能 | **SOP for AI**：讲一次流程，永不重复解释；与 memory.md 分工不同 |

---

## 分话题讲

### 1. Chat vs Agent：从乒乓球到 goal → result

**说法：**  
Chat model = **question → answer**，你问它答，活还是你干。Agent = **goal → result**：你给任务（「给 Greg 建极简 portfolio 站并 preview」），它自己规划、执行、交付。

**例子：**  
Remi 称很多 founder/员工用 agent 后 **10–20×** 日常产出；堆到周、月、年，和仍只用 chat 的人差距会拉开。

**和你何干：**  
别被「AI agent」营销词糊住——判断标准就一个：**你给的是问题还是可验收的目标？**

---

### 2. Agent Loop：Observe → Think → Act

**说法：**  
Prompt 进去后 agent 反复：**观察**（读 workspace 文件、工具结果）→ **想**（下一步做什么）→ **行动**（写代码、搜 web、调 MCP）→ 再观察，直到任务完成。完成条件由你在 prompt 里定（如「编译 10 个来源 + 输出 PPT」）。

**例子：**  
建 Greg 的 portfolio：空白 agent 先想「Greg 是谁？」→ 调 Perplexity 研究 → 写 plan → 写 HTML → 起 local server → **截图自检**是否完成。Claude Code 把 loop 展示得最清楚；Codex、Antigravity 同一逻辑。

**和你何干：**  
设计 agent 任务时，**写清「什么叫 done」**；否则 loop 不知道何时停。

---

### 3. Agent 四组件 + Harness =  facilitating loop 的平台

**说法：**  
Agent = **LLM（脑）** + **Loop（不停直到完成）** + **Tools** + **Context**。  
**Agent harness** = 让上述 loop 跑起来的应用（Claude Code、Codex、Cowork、Manus、OpenClaw 等）。Remi 比喻：**先学会开车**（概念），再开 Toyota / Range Rover（不同 harness）；功能差在「座椅加热、巡航」，核心踏板一样。

**例子：**  
三平台同一 prompt、不同 demo 文件夹，同时建 portfolio；Anti-Gravity 最快出 localhost preview，Claude Code loop 步骤最可见。

**和你何干：**  
**投资学概念，不是押宝单一产品**；本地 markdown 栈可跨 harness 迁移。

---

### 4. 安全与权限：给 agent 什么钥匙

**说法：**  
Claude Code / Codex / Antigravity 默认由大厂背书，相对安全；OpenClaw Remi 称 **Wild West**。风险任务（如 Meta 广告预算）靠 **tool 权限 scoped**：只读、限额、不把 write 全开。

**和你何干：**  
agent 越能「替你点按钮」，越要 **最小权限 + 最坏情况可接受**。

---

### 5. agents.md：像 onboard 新员工的 system prompt

**说法：**  
Chat 有 **自动 cloud memory**（ChatGPT/Claude 会偷偷记你）；**Agent 没有**——你必须显式给上下文。  
**agents.md**（Claude 叫 `CLAUDE.md`，Codex 叫 `AGENTS.md`，Gemini 叫 `GEMINI.md`）= 始终加载的「岗位说明书」：角色、你是谁、业务、工具偏好、语气。  
大上下文可放 `context/` 子文件夹，在 agents.md 里写：**每次任务前先读 context/**。

**例子：**  
空文件夹问「写 cold email」→ agent 反问卖什么、给谁；拖入预填 agents.md 后，同一句 prompt 直接产出带 Notion/Stripe 语境的邮件。

**和你何干：**  
用 chat 访谈式生成 agents.md（「问我问题，帮我写文件」）；**context 工程 > prompt 工程**。

---

### 6. memory.md：跨 session 的自改进循环

**说法：**  
Session 内说「favorite color is lavender」，agent 口头「记住了」，**新 session 全忘**——不是坏了，是设计如此。  
Remi 在 agents.md 底部加规则：**读 memory.md；被纠正或学到新偏好时更新 memory.md**（in-place 替换，别堆矛盾条目）。  
OpenClaw / Manus 等有内置 memory，底层仍是同一思路。

**例子：**  
「别用 Cheers 落款，用 Warm regards」→ 写入 memory → 下次 session 自动遵守。Meta ads 结构偏好、项目「禁用 dark mode」同理。  
Remi 建议 agents.md **≤200 行**；memory 可要求 **只存 substantial 修正**。

**和你何干：**  
**memory = 偏好与纠正**；**agents.md = 稳定身份与业务事实**。别混。

---

### 7. MCP：工具层的标准翻译器

**说法：**  
Harness 默认只有 web search；要 Gmail、Calendar、Notion、Granola、Stripe 等，走 **MCP（Model Context Protocol）**。Anthropic 推出；Cowork **Browse connectors** 一键 OAuth；Codex/Manus/Perplexity Computer 同类。  
比喻：以前每个工具要 custom integration；MCP 让 agent **仍说「英语」**，工具说各自语言，MCP 翻译。

**例子：**  
Remi 预连 Gmail、Calendar、Granola、Notion、Stripe。在 Claude Code 里一句：**summarize inbox → 读 Granola 会议 → 起草 proposal 邮件 + Stripe 链接 → Notion 建项目**，全程不切 app。

**和你何干：**  
Executive Assistant 的价值在 **MCP 串联**，不是「总结邮件」本身。

---

### 8. Skills：AI 的 SOP，讲一次永不重复

**说法：**  
Skill = **Standard Operating Procedure for AI**。无 skill 时写 proposal 要来回改格式 15–30 分钟，且 **memory 不该塞流程细节**。  
Skill 打包成 **`.skill`（本质是 markdown 流程 + 可选 references）**，存在 harness 的隐藏目录（如 `.claude/skills/`）。

**创建两法：**  
1. 有素材（课程 transcript）→ 用内置 **skill creator skill** 一键生成（如 viral hooks skill + hook formulas 参考）。  
2. 手动跑通流程一次 → 「把刚才做的封成 skill」（如 Sebastian refer skill、ads analyst skill）。

**例子：**  
Ads analyst：粘贴 Meta Ad Library URL → 爬 220 条广告 + landing 截图 → 视觉/文案/落地页 master report（Remi 称 agency 时代要 3–4 小时）。  
Skills 可 **链式**：morning brief skill 里写「有 podcast 则用 podcast research skill」；Cowork/Claude Code 可 **定时 9:00 跑 daily brief**。  
OpenClaw Meta ads bot：agents.md + ~15 skills + cron + MCP，同一套概念。

**Global vs Project：**  
Truncate（删冗余句）→ global；Sebastian refer → 仅 Executive Assistant project，避免污染 marketing 上下文。MCP 也分 global/project。

**和你何干：**  
**每周自动化 3–5 个小流程**，compound 成「整 life/work 自动化」；OpenClaw 建议 **先在 Claude Code 跑稳再迁**（Cowork 最易上手）。

---

### 9. 文件夹 AIOS 与未来工作方式

**说法：**  
Remi 工作区：`workspaces/` → 每公司 → 各部门文件夹 → 各自 CLAUDE.md + skills + MCP + context；顶层 orchestrator 管全局。  
**Markdown on disk = 未来 proof 栈**；LLM 吃 md 比 PDF/Docs 顺。  
愿景：人人 **AIOS** + 部门 agent；Cody Schneider 观点——未来员工入职自带 AIOS + skills，成为 **100× employee**。  
Remi 用 Claude Code + VS Code 作中枢，**不再打开 Gmail/Notion 界面**。

**和你何干：**  
从 **一个角色文件夹（Executive Assistant）** 开始；用 interview 生成 agents.md → 连 MCP → 日常中 **skill 化重复流程**。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Chat vs Agent** | 问答 vs 目标到结果 |
| **Observe-Think-Act** | Agent 单圈：观察→思考→行动 |
| **Agent harness** | 跑 agent loop 的平台（Claude Code 等） |
| **agents.md / CLAUDE.md** | 始终加载的岗位与业务上下文 |
| **Context engineering** | 把业务装进 agent，prompt 可极简 |
| **memory.md** | 跨 session 偏好与纠正，需规则驱动更新 |
| **MCP** | 工具与 LLM 之间的标准协议 |
| **Skill** | 可复用流程包（SOP），非 memory |
| **Global vs Project** | skill/MCP/CLAUDE.md 作用域 |
| **AIOS** | 个人/公司 markdown + agent 操作系统 |

---

## 值得记住的原话

> **"A chat model is question to answer. But then an agent is goal to result."**  
> Chat 是问答；Agent 是目标到结果。

> **"Chat is ping pong back and forth. An agent is you give it a goal."**  
> Chat 像乒乓球；Agent 是你给一个目标。

> **"The agent harness is just applications where this loop is facilitated."**  
> Harness 就是让 loop 跑起来的应用。

> **"Learn to drive… jump in any car."**  
> 学会开车，换什么 harness 都能开。

> **"Now it's all about context engineering… your prompts can be stupidly simple."**  
> 现在是上下文工程，prompt 可以傻简单。

> **"Skills are SOPs for AI — explain something once, never explain again."**  
> Skill 是 AI 的 SOP，讲一次就够。

> **"MCP sits as a translator… Claude speaks English, Notion Spanish, Gmail French."**  
> MCP 是翻译器，工具各说各语。

> **"Build skills for tiny manual processes each week… automate your entire life."**  
> 每周 skill 化小流程，compound 成全自动。

---

## 小结

**这期最核心的判断：** Agent 时代的关键不是更长的 prompt，而是 **harness + 本地 markdown 栈（agents.md / memory.md / skills / MCP）**；同一套文件夹可在 Claude Code、Codex、Cowork 间切换，像换车不换驾照。

**读完应带走：**
- **Loop + 四组件 + harness** 是 universal 语法；产品名会变，结构不变。  
- **memory 不会自动持久**——必须写进文件规则；与 **skills（流程）** 分工。  
- 从 **Executive Assistant + 1–2 个 MCP + 每周几个 skill** 起步，再扩部门文件夹；OpenClaw 等自治 harness 放第二步。

**和 vault 的关系：** Agent 入门主入口，接 [[IBM团队-Harness工程详解]]、[[WorkOS-创建和使用Skills方法论]]、[[Manus创始人-深度干货-上下文工程的最佳实践]]。

---

## 行动启示

1. **写 agents.md**：用 chat 访谈生成角色、业务、工具偏好；大 context 放 `context/` 并在 md 里指向。  
2. **加 memory 规则**：纠正语气、落款、工具习惯 → 更新 memory.md，别指望 session 记忆。  
3. **连 2–3 个 MCP**：从 inbox + calendar 或 Notion 开始，练一句多工具任务。  
4. **每周封 1 个 skill**：手动跑通的流程（proposal、referral、daily brief）→ skill creator。  
5. **权限最小化**：广告、支付、发信类 agent 先只读或 draft，再逐步放权。

---

## 相关阅读

- [[IBM团队-Harness工程详解]] — harness 可靠性、verify、guardrails  
- [[WorkOS-创建和使用Skills方法论]] — Skills 工程化与 eval  
- [[3-5 Skills - Agent 时代的知识分发系统]] — Skills 原理与 MCP 对比  
- [[Manus创始人-深度干货-上下文工程的最佳实践]] — context 爆炸与 offload/reduce  
- [[Claude Code实战-结合Obsidian打造第二大脑]] — 同一 markdown 栈 + Obsidian 深度用法  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1PnQfBvEs3](https://www.bilibili.com/video/BV1PnQfBvEs3/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Remi Gasiglia；主持人 Greg Eisenberg  
- **时长**：~58:54  
- **转写**：Recastory `bilibili-retranscribe/BV1PnQfBvEs3/`（FunASR SenseVoice + cam++，**asr v2** 57 段）  
- **版本**：v2 读者向讲义（2026-07-02）
