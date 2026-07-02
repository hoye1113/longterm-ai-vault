---
title: "Claude Code负责人 Boris Cherny：Tokenmaxxing与AI智能体前沿"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1NuGU6yE1b/"
speakers:
  - "Alex Kantrowitz（Big Technology Podcast 主持人）"
  - "Boris Cherny（Claude Code 负责人，Anthropic）"
duration: "57:08"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - claude_code
  - claude
  - anthropic
  - ai_career
created: 2026-06-09
description: "Boris Cherny 谈 Claude Code 指数增长、Tokenmaxxing 争议、Cowork 订八程航班、Auto 模式安全路由、rate limit 与 Codex 竞争，以及 Seven Powers 下 switching cost 变薄。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1NuGU6yE1b/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Claude Code 负责人 Boris Cherny：Tokenmaxxing 与 AI 智能体前沿

## 先搞懂这一期

**这是什么节目？**  
**Big Technology Podcast** 对 **Claude Code 负责人 Boris Cherny** 的 **~57 分钟深度访谈**。不是产品发布，是 growth、Token 政治、rate limit、与 Codex 竞争、以及「知识工作还会不会需要人」的压力测试。

**这期在回答哪三个问题？**

1. **Claude Code 增长有多夸张？** 和 API、Chat 比算什么量级？  
2. **Tokenmaxxing 是真实需求还是刷量？** Boris 怎么看组织变革？  
3. **Agent 下一步往哪走？** Cowork、并行 Claude、Auto 模式、moat 还剩什么？

**用一条线串起来（没看视频也能复述）：**

Anthropic 需求 **YoY ~80x**，ARR 叙事从 ~$4B 到 ~$45B；**Claude Code 对很多人是 Anthropic 第一入口**。内部未外发前已爆；Opus 4 → 4.5 → 4.6 → 4.7 **反复 inflect**——团队见过 hypergrowth，没见过这种。  
**Claude Code 定义**：不是 chatbot——**能用工具的 Agent**（改文件、浏览器、Cowork 控电脑）；Gen1 是 autocomplete，现在是 **你 prompt，它出去干活**。  
Boris **不写代码**， increasingly **「一个 Claude prompt 其他 Claude」**。Cowork 帮订 **8 航班 + 5 酒店**（读邮件日历找漏站）。  
**Tokenmaxxing 质询**：Amazon 员工自动化无用任务刷 KPI——Boris **不认为占用量大**；类比 90 年代 HBR「电脑在那，为何没生产力」→ **得重构业务流程**；建议 **给 token 实验空间 + 心理安全**，创新常来自 **想不到的人**（会计、市场、新 grad）。  
**效率 vs 智能**：先 **intelligence**，再 efficiency；Opus 4.7 可 **effort 档位**（extra high vs medium 省 token）。  
**Rate limit**：触顶的是 **少数 power user**（Boris 同时跑 5 个 Claude，夜里 **数百～数千**）；已 **双倍 rate limit**、提 weekly cap、Colossus 容量；低效 **plugin** 会展示 token 占比；企业可走 **API 无限量**。  
**路线图三主题**：模型更聪明 → **更长任务（Auto 模式）** → **更多并行 Claude**（Cowork 亦如此）。  
**Auto 模式**：不再对每个 tool 点 yes——**第二个 Claude 判 tool 是否安全**（千条 eval，实验室+野外更安全）。  
**Chatbot 未来**：更 **proactive**——聊印度行程直接提议代订。  
**Moat（Seven Powers）**：**网络效应**更重要；**switching cost** 变弱（让 Claude 帮你从 A 迁 B）。Claude Code **100% Claude Code 写**（自 2025-11 Opus 4.5）；YC 演讲 **~半数公司 100% AI 写码**。  
**Jack Clark 2028 自改进**：Boris 认同趋势，但仍是 **人 prompt**；模型开始 **提 Claude Code 功能 idea** 但质量参差。  
**World model 辩论**：Boris 偏产品侧——Anthropic 研究显示 **next-token 模型会 planning**；订八程航班 = 你愿赌它懂后果。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Claude Code = 终端写代码 | **Cowork / iOS / Slack** 多入口；非工程师 jump hoops 也用 |
| Token 多 = 浪费 | Boris：**先智能后效率**；组织层面是 **流程再造** 不是刷榜 |
| Rate limit = 产品失败 | **边缘 power user** 问题；主体用户 rarely hit |
| API vs Product 二选一 | Anthropic **双轨投资**；产品增速与 API 都很快 |

---

## 分话题讲

### 1. 增长：从未见过的曲线

**说法：**  
Claude Code 内部预览即爆；外发随 Opus 4 起 **指数再指数**。Dario 口径需求 **80x YoY**；产品（Code、Chat、Cowork、Design、API）都在加速，**Code 是许多人第一触点**。

**和你何干：**  
Demand 超预期 → **harness 与 infra 比功能 PR 更先瓶颈**（rate limit、Colossus）。

---

### 2. Claude Code vs Chatbot：差在 tools

**说法：**  
Chatbot = 来回聊。Agent = **读写信、Organize 桌面、浏览器、Cowork 接管 OS**——「tiny difference, magical」。  
非工程师用 Cowork **修语言输入法**、book flights；**新手比老用户更敢试** weird use case，Boris 常被打脸学到新招。

**和你何干：**  
评估 Agent 产品：**能否接你真实 toolchain**，不是 benchmark 分数。

---

### 3. Tokenmaxxing：刷量 vs 组织学习

**说法：**  
Silicon Valley 有 **mandate + leaderboard 刷 AI 用量**；Amazon FT 报 **无意义自动化冲 KPI**。  
Boris：**不是 Claude Code 用量主因**；客户极分散。  
类比 PC 普及期：**电脑在角落 + 纸柜 = 无生产力**；AI 要在 **流程中心** 才见效。  
建议：① **给人 token 做实验**（不必每笔审批）；② **心理安全**（试 workflow 允许失败）；③ **scaling 后再 optimize**；④ token 竞赛 **看文化**，有的公司适合。  
Anthropic 内部：**工程师 code 产出 +250%**，质量/reviewability **未回归**。

**和你何干：**  
Leader 问「怎么让大家用 AI」→ **先安全实验**，别先 KPI 排行榜。

---

### 4. 模型效率：spiral、effort、自举

**说法：**  
Cowork 导出 PPT 偶 **tool spiral**——Boris 承认 early days；**优先 intelligence**，再压 efficiency。  
控制杆：**选模型**（Opus/Sonnet/Haiku）、**effort**（extra high vs low）。  
**自举**：Claude Code **100% 自写**；Cowork 亦同；YC **~50% 举手全 AI 写码**；一年前 **不可想象**。

**和你何干：**  
Prod 任务：**extra high + 验证**；cron 小活：**low effort**。

---

### 5. Rate limit、Codex 与 infra

**说法：**  
触顶用户 **占比很小**（Pro 略高，Max 也不高）；曾短暂 **降 peak limit** 已 **rollback 并 double**；announce **weekly limit 上调** + **Colossus** 新容量。  
**Plugin token 效率**：界面展示 **各插件吃 token 比例**。  
Power user：并行 5 Claude、夜间 **100～1000** 后台 agent → 可转 **API 计费**。  
**Codex 竞争**：Boris 说 growth **仍在加速**；竞品 **flattering**，专注 **每天和用户聊、每天好一点**。

**和你何干：**  
Team 采购：**Max + API overflow** 给 power user；audit **heavy plugin**。

---

### 6. 路线图：Auto、并行、Cowork 商业化

**说法：**  
三主题：**更聪明模型**、**更长任务**、**更多并行**。  
**Auto 模式**：用 **第二个 Claude** 路由 tool 安全性（替代 permission fatigue 全点 allow）；**比人连点 yes 更安全**。  
Cowork：**QuickBooks、小商家 bookkeeping** 等新域；chatbot 变 **proactive action**。  
Hackathon：**医生、电工、木匠** 无码背景用 Claude Code 做出 **可卖产品**。

**和你何干：**  
Auto 模式 = harness **双层 agent**（执行 + 安全审计），见 [[IBM团队-Harness工程详解]] verify 叙事。

---

### 7. Moat、FDE 与「还要不要人」

**说法：**  
**Seven Powers**：**网络效应**升；**switching cost** 降（迁移 vendor 可让 Claude 做）。制造 **scale economies**（台积电类）仍硬 moat。  
Ethan Mollick 梗：AI lab 真信 ASI 会 **解散 FDE**——Boris：**仍缺好人**；leverage 涨但 **demand 更 insane**；终归要 **人问对问题**。  
Salesforce 全自动配置？**终局仍有人 pilot**——也许只问一句，但 **问对问题 leverage 极大**。  
Taxes：**有人用 Claude 对账 account**，Boris 不推荐但 **接近**。

**和你何干：**  
SaaS 护城河：**网络 + 数据飞轮** > 纯 UI switching cost。

---

### 8. 自改进与世界模型（短答）

**说法：**  
Jack Clark **~2028 模型自改进**：Boris **方向对**，Anthropic 为 **safety** 存在；今天仍是 **人主导 idea**。  
Yann LeCun **world model** vs Brockman **LLM 直达 AGI**：Boris 无研究立场，但 **订八程航班 = 信任其 consequence 理解**； poetry 研究见 **写第一句时已规划第二句**。

**和你何干：**  
产品人：**用真实高风险 task 测 agent**，别只读论文站队。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Tokenmaxxing** | 公司为冲 KPI 让员工刷 AI 用量 |
| **Token billionaire vs rent** | 自有算力 vs 租 Pro/API |
| **Auto mode** | 第二 Claude 判 tool 安全，减 permission 疲劳 |
| **Effort 档位** | 同一模型上的 reasoning 深度/ token 权衡 |
| **Power user 并行** | 同时开多 Claude/Cowork 任务 |
| **Seven Powers** | 规模、网络、切换成本等七种护城河框架 |
| **Organizational change** | AI 生产力 = 流程重构，非只买 license |
| **Claude prompts Claude** | Boris 工作流：meta-agent 调度子 agent |

---

## 值得记住的原话

> **"Claude Code is 100% written by Claude Code. Cowork is 100% written by Claude Code."**  
> Claude Code 全是 Claude Code 写的；Cowork 也是。

> **"I don't write code. I prompt Claude… mostly I have a Claude that prompts other Claudes."**  
> 我不写代码，我 prompt Claude……多半是 Claude 在 prompt 别的 Claude。

> **"I don't think token maxing is a large percent."**  
> 我不认为 Tokenmaxxing 占用量的大头。

> **"Computers are here, why is no one seeing the productivity impact?"**  
> 电脑都有了，为啥看不见生产力？（90 年代 HBR——业务流程要围绕 IT 重组）

> **"Give everyone tokens, let people experiment… psychological safety."**  
> 给大家 token 做实验……给心理安全。

> **"We optimize for intelligence first… then efficiency."**  
> 先优化智能，再优化效率。

> **"Every month there's a step change… you need a beginner mindset."**  
> 每月能力台阶式变——要保留新手心态重试旧任务。

---

## 小结

**这期最核心的判断：** Claude Code 增长是 **真需求 + 产品形态（tools）** 共振，不是单一公司刷 token；瓶颈在 **infra 与 rate limit**，解法在 **Colossus + 透明 plugin 成本 + API**；长期看 **人仍在 loop**，但角色变成 **提问、编排、验结果**。

**读完应带走：**
- Tokenmaxxing 是 **组织学习噪声**，不是 Anthropic 叙事主因。  
- **Auto 模式** = 安全 subagent，不是无脑全开权限。  
- Moat：**网络效应 up，切换成本 down**；Agent 时代仍要雇 **好人**。

**和 vault 的关系：** Anthropic 官方视角锚点，接 [[Claude Code负责人-AI原生团队如何使用AI]]、[[DeepMind-模型将吞噬Harness]]。

---

## 行动启示

1. **团队给 token sandbox + 允许失败**，别先 leaderboard。  
2. **Power user 走 API**；审计 **plugin token 占比**。  
3. **每月用新模型重试** 一年前失败的 Cowork/Code 任务。  
4. **Auto 模式上线前** 跑自己的 tool 风险 eval，别假设比人点 yes 更松。  
5. **SaaS 战略**：投资 **网络/数据 moat**，别赌 UI 锁定。

---

## 相关阅读

- [[Claude Code负责人-AI原生团队如何使用AI]] — Anthropic 内部 Dogfooding 工作流  
- [[Codex负责人-现场演示Codex]] — OpenAI 侧竞品与 knowledge work  
- [[DeepMind-模型将吞噬Harness]] — harness 会被模型吞吗  
- [[a16z-AI并非泡沫]] — 需求与 infra 宏观叙事  
- [[MOC - Agent Theory and Design]] — Agent 理论横切索引  

---

## 来源

- **视频**：[BV1NuGU6yE1b](https://www.bilibili.com/video/BV1NuGU6yE1b/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Boris Cherny、Alex Kantrowitz（Big Technology Podcast）  
- **时长**：~57:08  
- **转写**：Recastory `bilibili-retranscribe/BV1NuGU6yE1b/`（FunASR SenseVoice + cam++，**asr v2 后处理** 58 段）  
- **版本**：v2 读者向讲义（2026-07-02）
