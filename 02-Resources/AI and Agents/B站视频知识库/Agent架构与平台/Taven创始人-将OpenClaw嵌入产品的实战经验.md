---
title: "Taven创始人：将OpenClaw嵌入产品的实战经验"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1dZLS66E3m/"
speaker: "Tablen AI 创始人（欧洲小型 Agent 公司）"
duration: "20:31"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - skills
  - harness_engineering
  - context_engineering
created: 2026-06-09
description: "Tablen AI 创始人讲 Pi/OpenClaw 企业嵌入：Agent=Goals+Context+Tools 循环；Excel Skill 用小 CLI 组合；一客户一 Agent+AGENTS.md 处理 RFP 邮件。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1dZLS66E3m/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Taven 创始人：将 OpenClaw 嵌入产品的实战经验

## 先搞懂这一期

**这是什么节目？**  
Tablen AI 创始人在 Pi/OpenClaw 社区 meetup 上的 **~20 分钟实战演讲**。不是产品发布，是「我们怎么用 Pi 内核做企业 Agent」的 field notes。

**这期在回答哪三个问题？**

1. **Coding Agent 时代，产品该怎么设计？** 单一职责、小工具组合，还是大而全？  
2. **Agent 和 Coding Agent 差在哪？** 核心 loop 一样，多出来的是 runtime + shell + extension。  
3. **OpenClaw/Pi 怎么嵌进真实业务流程？** 以 B2B 销售 RFP 邮件处理为例，一客户一 Agent + harness 文档。

**用一条线串起来（没看视频也能复述）：**

开场承认：**coding agent 还在 fuck around and find out 阶段**，几周后再讲可能全变——鼓励大家自己 tinkering。  
Ken Thompson「**do one thing well**」→ Co-Work（Claude Desktop）的 Excel Skill 案例：不直接「对话 Excel」，而是 **pandas/openpyxl/LibreOffice CLI 打包成 Skill**。  
Agent 本质极简：**Goals + Context（agents.md）+ Tools，循环**；Coding Agent 在此基础上加 **bash runtime + extension API**（session events、UI interaction）。  
Demo 链：CRM lead qualifier（3 文件 TypeScript）→ 同一逻辑做成 Pi extension（`/pipeline` + UI select）→ Pi 问它自己搭 web UI，同一 extension 机制。  
OpenClaw = Pi 多通道版：`runEmbeddedPiAgent`、sessions、Pi AI 统一 LM 抽象；OpenClaw 自研 plugin（multichannel、subagent gateway）。  
**企业案例**：监控销售 inbox → gateway 路由 → **一客户一 Agent**（AGENTS.md + customer.md）→ CLI 暴露 CRM/ERP → 输出 **draft email**，人留在邮箱里改。  
收尾：coding agent 是软件系统的 **core building block**；Pi 最小可拆，请去 tinkering；sandbox 看 **NVidia open-shell policy**。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| OpenClaw = 个人 WhatsApp 助理 | **Pi 内核 + 企业多 Agent 路由** 的产品化路径 |
| Skill = prompt 技巧 | **小 CLI 工具集打包**（Excel 案例） |
| Agent = 复杂框架 | **三要素 loop**，其余是 use case 魔法 |
| Coding Agent 只写代码 | Extension API 可 **驱动 UI、slash command、web** |

---

## 分话题讲

### 1. 「边做边学」阶段：别等权威教材

**说法：**  
没有 pattern 书可写；coding agent 领域 **每几周就变**。Mario 的 minimal Pi 就是给你 **fool around** 的。

**例子：**  
演讲者几周后会再讲一遍，内容大概率不同。

**和你何干：**  
别等「最佳实践定稿」才动手；用 Pi/OpenClaw **小步试**，比读十篇综述有用。

---

### 2. Do one thing well：Excel Skill 的启示

**说法：**  
Co-Work 面向金融等场景，用户总要碰 Excel。Agent **不能直接「和 Excel 对话」**——用 **pandas、openpyxl、LibreOffice CLI** 等小工具，**打包成 Skill**。

**和你何干：**  
「老大难集成」（Excel、SAP、老 CRM）→ **拆成 Agent 擅长的 CLI**，别逼模型直接操作二进制格式。

---

### 3. Agent 三要素 + Coding Agent 增量

**说法：**  
- **Core Agent**：LM + tools in a loop；Goals、Context（agents.md）、tool calls、结果，循环。  
- **Coding Agent**：同上 + **runtime + shell（bash）** + extension。  
- OpenClaw 语音消息案例：当时没有 voice 插件，Agent **自己调 ffmpeg**——外面像「学会了」，里面是 **又一个 tool call**。

**和你何干：**  
设计系统时先画 **core loop**，再决定要不要 shell、extension、多通道。

---

### 4. 架构模式：让 Coding Agent 易访问

**说法：**  
别堆复杂抽象。问：**coding agent 擅长什么？** 系统怎么 **accessible**？  
CRM lead qualifier：TypeScript **3 文件**，终端命令 `show leads` / `score them`；hook 在 tool call 前做 **RBAC/校验**。

**和你何干：**  
企业 Agent 优先 **CLI + 小 repo**，比 REST 巨 API 更适合当前 coding agent。

---

### 5. Extension：从终端到 Web 同一机制

**说法：**  
Pi extension 关注 **session events + UI interaction**。`/pipeline` slash command 可 **load context、UI select、dropdown**。  
Pi 被要求搭 web UI 时，**同一 extension 机制** 复用到浏览器端（框架还在整理，方向清楚）。

**和你何干：**  
一次写 extension，多端（TUI/Web）复用——比为每个界面重写 agent 逻辑省。

---

### 6. OpenClaw 与 Pi 的包关系

**说法：**  
OpenClaw 用 Pi 的 **core packages**：`runEmbeddedPiAgent`、sessions、agent-core、coding agent、**Pi AI**（统一 LM）、terminal UI。  
OpenClaw 自研 **plugin**：multichannel routing、provider orchestration、subagent gateway——**use case 不同，要求不同**。

**和你何干：**  
嵌 OpenClaw/Pi 时：**内核复用，外围 plugin 自研**。

---

### 7. 企业 RFP 案例：一客户一 Agent

**说法：**  
监控销售 inbox → gateway **按客户路由** → 每个客户一个 Agent：  
- **AGENTS.md**：角色、系统用法、输入输出规范  
- **customer.md**：该客户 workflow、折扣、权限  
- **按 case 复用 session**，保留上下文  
- 工具：**CLI 暴露 CRM/ERP**（agent 擅长跑 CLI），数据进 sandbox  
- 输出：**draft email**；用户 **留在邮箱** 编辑，dashboard 只是 admin

**和你何干：**  
B2B 自动化模板：**文档 harness（AGENTS.md/customer.md）+ CLI 工具 + session  per case + 人审 draft**。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Pi** | Mario 做的 minimal open-source agent/coding agent 内核 |
| **OpenClaw** | 基于 Pi 的多通道个人/团队 Agent 平台 |
| **Co-Work** | Claude Desktop，bundling coding agent 到非 IDE 场景 |
| **Excel Skill** | 小 CLI 工具集打包，非直接读写 xlsx |
| **Agent 三要素** | Goals + Context + Tools（循环） |
| **Extension API** | session events、UI interaction、slash commands |
| **AGENTS.md / customer.md** | 企业 harness：角色 vs 客户专属上下文 |
| **CLI-first 集成** | 用命令行暴露 CRM/ERP，供 agent 调用 |

---

## 值得记住的原话

> **"We are in the fuck around and find out phase for coding agents."**  
> Coding agent 还在边做边学阶段。

> **"Write programs that do one thing and one thing well."**  
> 写只做一件事、把它做好的程序。（Ken Thompson）

> **"It doesn't talk to Excel. Instead, it uses a set of small tools... packaged into their own skill."**  
> 它不跟 Excel 对话，而是用一堆小工具打包成 Skill。

> **"An agent is actually just an LM agent that runs tools in a loop... That's it. There's not much more."**  
> Agent 就是 LM 在循环里跑工具。就这些。

> **"Make it easy for coding agents... think about what is it good at?"**  
> 让 coding agent 用起来简单——想想它擅长什么。

> **"From the outside it looks like learning, but inside it's actually just another tool call."**  
> 外面像学会了，里面是又一个 tool call（OpenClaw + ffmpeg）。

> **"One agent per customer... AGENTS.md... customer.md... let users stay in email."**  
> 一客户一 Agent；harness 文档分层；用户留在邮箱里改 draft。

> **"Coding agents are and will be a core building block for your software systems."**  
> Coding agent 会是软件系统的核心积木。

---

## 小结

**这期最核心的判断：** 企业嵌 Agent 不必等大框架成熟——**Pi/OpenClaw 内核 + 小 CLI Skill + AGENTS.md 类 harness + 一客户一 session**，就能把 inbox→draft 这类流程跑通；Excel 案例说明 **「do one thing well」比直接 API 对话可靠**。

**读完应带走：**
- Agent 本体很薄（Goals/Context/Tools loop）；magic 在 **use case 包装和 harness 文档**。  
- Coding Agent = core agent + shell/runtime + extension；OpenClaw 在此基础上加 **多通道 plugin**。  
- 企业落地：**CLI 暴露后端、draft 输出、人留在熟悉工具（邮箱）里审**。

**和 vault 的关系：** 接 [[WorkOS-创建和使用Skills方法论]]、[[IBM团队-Harness工程详解]]、[[30分钟精通OpenClaw]] 的 OpenClaw 实战线。

---

## 行动启示

1. **Pick 一个「Excel 级」痛点**：拆成小 CLI，打包成 Skill，别逼 LLM 直接操作复杂格式。  
2. **写 AGENTS.md + 客户/场景 md**：角色与实例上下文分开，方便一客户一 Agent。  
3. **CRM/ERP 用 CLI 暴露**：当前 coding agent 对 terminal 最熟。  
4. **输出 draft，人审后发**：自动化止于草稿，人在邮箱/Slack 里拍板。  
5. **Clone Pi，改 extension**：3 文件 demo（lead qualifier）比读架构图上手快。  
6. **关注 NVidia open-shell policy**：sandbox 方向之一。

---

## 相关阅读

- [[WorkOS-创建和使用Skills方法论]] — Skills 原子单元与 harness 设计  
- [[IBM团队-Harness工程详解]] — verify、guardrails 等企业 harness  
- [[30分钟精通OpenClaw]] — OpenClaw 个人助理设置与安全  
- [[OpenClaw创始人-我是如何使用OpenClaw的？]] — 创始人视角  
- [[Loop-Agent Loop到底是什么]] — Agent loop 与 harness 分层  

---

## 来源

- **视频**：[BV1dZLS66E3m](https://www.bilibili.com/video/BV1dZLS66E3m/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Tablen AI 创始人（欧洲小型 Agent 公司）  
- **时长**：~20:31  
- **转写**：Recastory `bilibili-retranscribe/BV1dZLS66E3m/`（FunASR SenseVoice + cam++，**asr v2** 14 段）  
- **版本**：v2 读者向讲义（2026-07-02）
