---
title: "Claude Code负责人：AI原生团队如何使用AI"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1eyBgB2EbX/"
speaker: "Cat（Anthropic Claude Code 产品负责人）"
duration: "40:31"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - claude_code
  - harness_engineering
created: 2026-06-09
description: "Cat 讲 Claude Code 从 Boris 20% 项目到千人流传：终端极简+可扩展、工程师 E2E 原型 dogfood、Todo/Plan 从内部痛点长出来；PM 用 Claude Code 合 Slack/GitHub 反馈，Eval 分 E2E 与 triggering 两类。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1eyBgB2EbX/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Claude Code 负责人：AI 原生团队如何使用 AI

## 先搞懂这一期

**这是什么节目？**  
访谈 **Anthropic Claude Code PM Cat**——产品怎么 **从内部 viral 到对外**、团队怎么 ship、她个人怎么用、以及 **Eval / 路线图**（几个月 horizon，不做三年规划）。

**这期在回答哪三个问题？**

1. **Claude Code 为什么长这样？** 终端 = 开发者已有 CLI 肌肉；**ASCII 屏效迫使你 brutal 砍 UI**；深度靠 hooks/subagents/slash commands。  
2. **团队怎么一周一周发功能？** **强 product engineer E2E**：原型 → 内部 dogfood（~1000 人自愿反馈群，**~10 分钟一条**）→ 爱的 fast track；大项目（IDE 集成）才 formal review。  
3. **个人怎么用好？** 当 **over-eager 新 grad** 给反馈；投 **CLAUDE.md**；prototype 不是 docs；**plan mode 是用户要 explicit 才加的 hack**。

**用一条线串起来：**

Boris API 玩具 → Cat 20% 环境配置 → 决定对外 → 内部跨 research/DS/PM/design viral → **Todo list** 来自 Sid：重构 30 处 agent 只做 5 处 → **强制写任务+做完才停** → 持久 `/todo` → **Plan mode** 抵抗模型太 eager 写代码 → PM 用 Claude Code **Slack  synthesize 反馈、dedupe GitHub、更 docs** → Eval：**SWE-bench 端到端** + **web search/todo triggering** → 贴纸 Easter egg 寄 500 份寄到 **8 小时** → 未来：**CLI 仍最强 + SDK 扩 agent 生态 + 终端外 form factor 给 PM/design/marketing**。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Claude Code = coding CLI | **Dogfood 驱动**；很多功能 **内部试两三版才公开** |
| Plan mode 是核心设计 | 团队 **本想用户自然语言要 plan**；plan mode 是 **向 eager model 妥协** |
| PM 写 PRD 给工程 | Cat/Megan **自己 commit**；designer PR 到 console |
| Eval = 上线门槛 | **两类 eval 都不完美**；**社区负反馈 +  obvious 重复 issue** 同样驱动优先级 |

---

## 分话题讲

### 1. 起源与内部 viral

Boris 原为理解 API 的 side project；Cat 20% 时间 **配环境**，狂发 product feedback。  
对外决定后全职。传播路径：Boris 团队 → 全 org → research → **DS/PM/design**。  
**高 viral**：因为终端里 **任何 CLI 都能接**（GitHub CI、Datadog…）。

---

### 2. 设计哲学：极简 onboarding，任意深度

- 终端只有 ASCII → **不能堆按钮**，feature 必须 **名字+一行说清就能用**。  
- **可组合**：hooks、custom slash、subagents——各公司 DPE 团队自定义。  
- 「像打游戏」：**power user 自己挖**。

**PM 角色（developer product）：** 定 **可定制性边界**、aspirational bar；**定价 packaging** 让工程专注体验。

---

### 3. 怎么 ship：工程师 E2E + dogfood

常态：**工程师原型 → 内部 dogfood → 听反馈**（懂？bug？爱？）。  
爱的 **fast track 公开**；不爱或 confuse **内部死掉**。  
小功能（todo、plan）**常常无 PRD**——难在 **form factor + prompt**，不是集成。  
大功能（VS Code / IntelliJ）**几个月 + product review**——「meet people where they work」。

**反馈源：** ~1000 人 internal Slack（opt-in）；企业 **~10 家** 超高信号 early adopter；Twitter 偶尔。  
优先级：**GitHub issue 百 thumbs up + sales DM 三客户 broken** → 非常明显；**重复 10 次** 的抱怨 Cat 亲耳听到就够排。  
**负反馈文化：** 「我们要听 **什么不行**」，fix SLA **1–2 周**（prioritized 的）。

**Cat 用 Claude Code 干活：** Slack 查「还有谁要 subagent 自定义模型」；GitHub dedupe；**docs 第一稿 agent 写、人清最后 10%**。  
**几乎不用 Google Docs**——why 在 PR 里，**问 Claude Code 搜 GitHub 比读 stale doc 准**。

---

### 4. Todo list 与 Plan mode 的故事

**Todo：** 大 refactor agent **early stop**（30 改 5）→ Sid：**逼模型写下任务，提醒没做完不能停** → 意外有效 → 从 transcript 飞过 → **持久 `/todo`**（用户真用来 **track progress**）。  
**Plan mode：** 用户一直说「先说计划别写码」；团队 **希望自然语言就够**；1–2 月压力后 **加 explicit /plan**——可能未来 model 更听话会 **弱化 plan mode**。  
Even in plan：**模型仍说「我可以现在开始写码」**——Anthropic 模型 **trigger-happy**；Cat 个人更爱 **Codex 慢但稳**。

---

### 5. Eval：两类，都不银弹

**End-to-end（如 SWE-bench）：** 换 harness/模型看 **是否退化**；分数变了 **难归因**，要读 **大量 gnarly transcript** 找主题。  

**Triggering eval：** 工具该不该调用——如 **web search 不能 100% 乱搜**，问 React 最新 release 该搜。黑白边界 **codify 成 eval**；灰区后处理。  
Todo 误触发（**一项任务也写 todo**）本可用 eval 卡。  

**Capability eval（数据科学等）** 更难——要大数据集+金标准。  
**社区也是 eval**：todo triggering 他们花很多时间调。

---

### 6. 团队文化与小故事

- **Swag Easter egg**：聊天提 swag → 贴纸 portal；有人 **反查 source map**，**~500 地址**；12 人估 1 小时，实际 **8 小时** 贴邮票。  
- **Time estimate 梗**：agent 说「两周」，10 分钟做完——**只见过 human hours**。  
- **Designer Megan**：`/init` vs **手写 proud designer CLAUDE.md**；**global personal CLAUDE.md** 跨 repo。  
- **招聘 PM**：爱开发者、最好写过 code / devtools； steward **Claude Code SDK** + **customization hub**（share hooks/slash）。  
- **Vision（几个月）：** CLI 最强 coding agent；**SDK 让 legal/EA/health/finance agent 变多**；**非终端 form factor** 给 PM/design/marketing/sales——terminal 仍难 explain 给从未用过的人。

**AI PM 最难技能：** **模型能力直觉**——feature 是 prompt 20% 能补还是 **3 个月后再看**；失败时分辨 context/model/task capability。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Dogfood** | 上千员工自愿群，高密度 pre-release 反馈 |
| **Product engineer E2E** | 工程师 owning 原型到发布 |
| **Todo forcing** | 写任务清单+禁止早停，解决大 refactor 半途而废 |
| **Triggering eval** | 测「该不该调用某 tool」，非测最后答案 |
| **E2E eval** | SWE-bench 类整任务成败，粗但防退化 |
| **CLAUDE.md** | 每 session 注入的 repo/个人 onboarding 记忆 |
| **Demo is not docs** | 让 Claude Code 原型感受 feature，别只写 spec |
| **Over-eager new grad** | 把 Claude Code 当快但需纠错的 junior |

---

## 值得记住的原话

> **"Do people immediately understand it… or do people just love it?"**  
> 内部 dogfood 就看：立刻懂？爱不爱？

> **"We love negative feedback… we want to hear what doesn't work."**  
> 我们要负反馈，听什么不行。

> **"Plan mode was a hack… the model is so trigger-happy."**  
> Plan mode 是 hack，模型太爱立刻写码。

> **"Demo is not docs."**  
> Demo 不是文档——先原型再决定做不做。

> **"A year or two is a really long time… build for the next generation of models."**  
> 一两年太久；为下一代模型建产品。

---

## 小结

**这期最核心的判断：** Claude Code 的成功 = **终端极简 × 可扩展 harness ×  brutal internal dogfood**；功能多从 **工程师自己的痛点原型** 长出来，PM 合反馈与 packaging，**不迷信完美 eval** 但 **triggering 值得投资**。

**读完应带走：**
- Todo/Plan 都是 **对抗 eager model** 的 UX，不是最初蓝图。  
- **源码+PR=文档** 的小团队优势。  
- AI PM 核心：**模型能力直觉** 胜过堆 artifact。

**和 vault 的关系：** Claude Code 官方团队视角，接 [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]]、[[IBM团队-Harness工程详解]]、[[MOC - Harness Engineering]]。

---

## 行动启示

1. **大任务先让 agent 写 todo**，并明确「全部完成前别停」。  
2. **维护 CLAUDE.md**（架构、测试偏好、gotcha），global+repo 两层。  
3. **新 feature 先 Claude Code 原型**，再写 PRD pitch。  
4. **自建 triggering 检查表**（如：单项任务禁止 todo；乱 web search 告警）。  
5. **负反馈渠道** 刻意要「哪里坏了」，别只要赞。

---

## 相关阅读

- [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] — Boris 增长与 token 叙事  
- [[IBM团队-Harness工程详解]] — harness verify/guardrails 对照  
- [[Loop-Agent Loop到底是什么]] — 何时要闭环 eval  
- [[OpenClaw创始人-我是如何使用OpenClaw的]] — 用户侧反 orchestrator  
- [[MOC - Harness Engineering]] — Harness 横切索引  

---

## 来源

- **视频**：[BV1eyBgB2EbX](https://www.bilibili.com/video/BV1eyBgB2EbX/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Cat（Claude Code PM，Twitter @_caw）  
- **时长**：~40:31  
- **转写**：Recastory `bilibili-retranscribe/BV1eyBgB2EbX/`（**asr v2**）  
- **版本**：v2 读者向讲义（2026-07-02）
