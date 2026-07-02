---
title: "5次创业者：AI智能体独自经营初创公司"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV174GU6AEZY/"
speaker: "Ryan Carson（5 次创业者，Untangled 创始人）"
duration: "39:26"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - codex
  - skills
  - ai_career
created: 2026-06-09
description: "Ryan Carson 用 OpenClaw R2+ClawChief（cron+markdown）当幕僚长/BD，Devin 云开发+playbook 自动化，solo 创始人日 merge 10+ PR；创业哲学从「别写文档」翻转为「先建系统再放量」。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV174GU6AEZY/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# 5次创业者：AI 智能体独自经营初创公司

## 先搞懂这一期

**这是什么节目？**  
访谈 **Ryan Carson**（5 次创业、融了 $2M seed、**故意不雇人** 的 Untangled 创始人）。前半 **OpenClaw 幕僚长 R2 + ClawChief 开源配置**；后半 **Devin 云工程 + Codex + 营销自动化机器**。

**这期在回答哪三个问题？**

1. **Agent 当 Executive Assistant 要哪些零件？** → **Cron jobs + Markdown skills**（他自己说：agent 就是这两样）。  
2. **OpenClaw 不稳定怎么办？** → 专用 Mac 在 closet，**Tailscale SSH + Codex 当「修 OpenClaw 的 agent」**；clone OpenClaw 源码让 Codex **读 harness 自升级**。  
3. **Solo 创始人怎么日 ship 10+ PR？** → Devin 云 VM、playbook、浏览器测试录屏、**land PR skill**；Google Ads CLI、nightly 社媒 pipeline。

**用一条线串起来：**

R2（OpenClaw）= 真人 EA 待遇（独立邮箱/GitHub）→ **每 15 分钟 cron** 跑 executive assistant skill（Gmail/Calendar/Todoist/priority map）→ **nightly prospecting** Firecrawl 找律师/调解员 cold email → Slack **#ryan-r2 线程** 沟通 → **ClawChief repo** 开源 → 工程全在 **Devin 云环境**（本地几乎不碰）→ weekly **signup→结案** 全链路 playwright → WhisperFlow 口述 PRD → build → **land PR 无人工 merge** → 营销：**design.md + 参考图 + GPT Image** 续品牌；**纸笔 weekly 3 任务** 对抗「agent 管季度、人看不清本周」。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| OpenClaw = 个人玩具 | **Chief of staff + BD**：cron 确定性 heartbeat，不靠不可靠 heartbeat |
| MVP = 别写流程 | **反转**：现在要先 **SDLC 文档 + playbook + skill**，再一人十人产出 |
| Devin = 早期不好用 | **2026：云 VM + 浏览器测试** 成 solo 默认栈 |
| Agent onboarding | 比雇人快：**训练写进 markdown，不随人走** |

---

## 分话题讲

### 1. ClawChief：R2 的组织架构

开源 **ClawChief**：markdown + cron。  
- **priority map**：季度业务优先级 + 人生里重要的人（家人、关键联系人）。  
- **auto resolver**：R2 能自己搞定的就自己搞，规则写进 md。  
- **agents.md**：加载 priority map 进 context。

**Cron 铁律：** OpenClaw 自带 heartbeat **不定时**；Ryan 用 **cron 每 15 分钟** deterministic 跑 `executive assistant` skill。Cron 消息要 **DRY**——只写「use this skill」，细节全在 skill 文件。

**和你何干：**  
生产级 recurring agent 任务，**cron > heartbeat**；大段指令放 skill，cron 一行触发。

---

### 2. R2 日常：EA + BD

- **Slack app**（自建 manifest，fiddly 但专业 **thread**）。  
- 读 Ryan 邮件/日历；**以 R2 身份** 发 invite（copy R2 约 this podcast）。  
- **Todoist API** 管任务（不用 md 任务表）。  
- **Prospecting cron（每日）**：Firecrawl 搜 Connecticut 家庭法律师/调解员 → Google Sheet CRM → **代发 cold email**（ryan@ 老域名 deliverability）。  
- 防重复：**spreadsheet 查是否已联系**——对人不用说，对 agent 要写死。

**坑：** skill 里写「CC 另一邮箱」→ R2 线程回复却 **另发新邮件**；agent **字面执行** md，要 pedantic 一次写对。

---

### 3. 运维：Codex 修 OpenClaw

MacBook Pro 在 closet，人在日本 → **VS Code SSH Tailscale**。  
Workspace = **OpenClaw 源码 clone** → 「Codex，check OpenClaw healthy」→ OpenClaw 崩了 **上层 agent 修下层 agent**。  
Pro tip：「pull OpenClaw latest，读源码，告诉我怎么 upgrade 做 X」。

---

### 4. Devin：零本地开发 + Schedules

Devin = **永远同样的云 VM**；`npm run dev` 配一次反复用。  
**Schedules + Playbooks：**
- 每周 **full case**：signup → 完成离婚案件全流程（Playwright）。  
-  nightly smoke：录屏 signup 某功能，坏了报告。  

Playbook = skill：告诉 agent **怎么做一整条 UX**。

**和你何干：**  
Serious solo/small team：**自动化 = cron/schedule + playbook**，与 OpenClaw 同构。

---

### 5. Feature 从想法到 merge：code factory

1. Devin 里 **WhisperFlow brain dump** → skill 引导 **PRD 问答** → PRD.md  
2. **build it**；单线程，harness **auto compaction**  
3. Devin **浏览器测 + 录屏**，常自发现并修 PR  
4. **land PR playbook**：review、resolve、merge **无需 Ryan 看 code**  
5. **10–20 PR/天**；Ryan 读 **agent 写的 markdown 摘要** 多于 diff  

并行：**1–2 个 feature**，脑子在 **GTM/Ads**。

**Google Ads：** 让 Devin 建 **Google Ads API CLI**，Ryan 只 chat「campaign 怎样、怎么 optimize」——不用 Ads UI。

**Content machine：** Descript 剪专家访谈 60s → Drive mp4 → nightly playbook：Gemini 看视频写文案 → **GPT Image** 封面 → Publer API 发社媒。  
品牌：**Design Joy 首单 $6k** 拿 design.md + 参考图，之后 AI 无限延展（仍认首刀设计品味重要）。

---

### 6. 哲学反转与纸笔 weekly

旧创业：**MVP 别写系统文档**。  
现在：**先建 SDLC、reference images、chron+skill**，再 unlock「一人十人」。setup  brutal，但 Ryan ** freed 去见人、销售**。  
**Memory：** 坚持用 OpenClaw 开箱 memory，不折腾 QMD/自研 harness——**别为了工具放弃 real work**。  
**Weekly 任务改纸笔/白板最多 3 条**——agent 强在 today/quarter，**本周分辨率** 人要用物理列表（学自妻子）。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **R2** | Ryan 的 OpenClaw bot，EA/CoS 人格 |
| **ClawChief** | 开源 cron+md 配置，把 OpenClaw 变成幕僚长 |
| **priority map** | 季度优先级 + 重要人物，供 agent 决策 |
| **Cron vs heartbeat** | 定时确定性 vs OpenClaw 「想起来才跑」 |
| **Agent-on-agent** | Codex SSH 修 OpenClaw / 读源码自升级 |
| **Playbook** | Devin 版 skill，描述长流程自动化 |
| **land PR** | agent 自 review+merge 的 playbook |
| **code factory** | agent 写+审+ship 接近 100% 的 SDLC |

---

## 值得记住的原话

> **"Agents are cron jobs and markdown files."**  
> Agent 就是 cron job 加 markdown 文件。

> **"It's almost easier to onboard and train agents than to train your [human team]."**  
>  onboard agent 有时比培训人还容易。

> **"Do not spend time on systems… that's literally reverse now."**  
> 以前 MVP 别写系统——现在完全反过来。

> **"You want to allow Codex or your OpenClaw to inspect its own code."**  
> 让 Codex/OpenClaw 能读自己的源码。

> **"I'm probably shipping at least 10 PRs a day."**  
> 我每天至少 merge 10 个 PR。

---

## 小结

**这期最核心的判断：** Solo AI-native 公司 = **先投入系统（cron、skill、playbook、云 Dev 环境）**，再把执行交给 agent；OpenClaw 管 **办公/BD**，Devin 管 **工程/测试/Ads/内容**；人保留 **品味、关系、本周焦点**。

**读完应带走：**
- **ClawChief** 是可 fork 的 EA 模板；cron 要短、skill 要 pedantic。  
- **上层 agent 修下层** 是远程运维 OpenClaw 的实用招。  
- 创业纪律变了：**文档化流程 = 杠杆**，不是浪费时间。

**和 vault 的关系：** OpenClaw 企业化个人实践，接 [[OpenClaw创始人-我是如何使用OpenClaw的]]、[[Codex负责人-现场演示Codex]]、[[MOC - Agent Theory and Design]]。

---

## 行动启示

1. **fork ClawChief**，先写 priority map + 一条 15 分钟 inbox sweep cron。  
2. **OpenClaw 跑专用机器 + Tailscale**，Codex 当 SRE agent。  
3. **Devin/ Codex playbook** 做 weekly 全链路 smoke + 录屏。  
4. **land PR skill** 标准化 merge，人只看 agent 摘要。  
5. **weekly 3 任务纸笔**，别只信 agent 的 quarter/today 视图。

---

## 相关阅读

- [[OpenClaw创始人-我是如何使用OpenClaw的]] — Peter 侧 IM+CLI 哲学  
- [[30分钟精通OpenClaw]] — 安全与 memory 入门  
- [[Codex负责人-现场演示Codex]] — Codex 官方 automation  
- [[WorkOS-创建和使用Skills方法论]] — Skills 设计  
- [[Cursor副总裁-构建软件开发过程的Agent]] — SDLC agent 化  

---

## 来源

- **视频**：[BV174GU6AEZY](https://www.bilibili.com/video/BV174GU6AEZY/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Ryan Carson（[@Ryan Carson](https://twitter.com/ryancarson)）  
- **开源**：[ClawChief](https://github.com/)（访谈提及，可搜 Ryan Carson ClawChief）  
- **时长**：~39:26  
- **转写**：Recastory `bilibili-retranscribe/BV174GU6AEZY/`（**asr v2**）  
- **版本**：v2 读者向讲义（2026-07-02）
