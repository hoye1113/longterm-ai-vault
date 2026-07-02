---
title: "Alchemy CPO：从代码审查到自动代理"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1i9E366EAr/"
speaker: "Matthias（Alchemy CPO，前 Facebook 开发者平台）"
duration: "29:45"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - codex
  - skills
created: 2026-06-09
description: "Alchemy CPO Matthias 分享 Codex 进公司的三个转折点：Slack 改文档、事故回溯 code review、PR 里与 Codex 来回改；以及 Linear+Skills 让 Codex 离线干活的个人 side project 体系。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1i9E366EAr/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Alchemy CPO：从代码审查到自动代理

## 先搞懂这一期

**这是什么节目？**  
OpenAI Codex 团队访谈 **Alchemy CPO Matthias**（非工程师出身，做过 consumer product、Facebook 早期开发者平台，现管 crypto 基础设施产品）。前半讲 **公司内 Codex 落地**，后半 **屏幕共享** 他的 personal project 流水线。

**这期在回答哪三个问题？**

1. **企业什么时候真信 AI coding？** 不是 demo 漂亮，是 **code review 能抓到真实 bug**，且工程师愿意在 PR 里跟 Codex 来回改。  
2. **基础设施公司怎么改产品思维？** 开发者客户已经在用 AI 写代码，平台要同时服务 **人类开发者 + 自主 agent 开发者**。  
3. **个人 builder 怎么「人不在电脑旁，Codex 还在干」？** Skills + Linear + agent.md + feature flag 实验。

**用一条线串起来：**

Slack 里 @Codex 改文档 → 大迁移事故后 **retro 跑 Codex review，它抓到了 race condition** → 工程师 PR 里 `@codex review` 循环改 → 公司内 **共享 Skills repo**（PM 写 PRD、分析用户反馈）→ 副业：**Linear 当 backlog，159 个 issue 全是 Codex 建的** → 睡前 dispatch research+build，醒来 toggle feature flag → 写作 Mac/iOS app 用 **Codex App Server** 走 ChatGPT 订阅 → OpenClaw「Lou」+ Apple Watch 语音触发 Codex job → **Snapcat** 十年 hackathon 项目当 personal eval，GPT-5.5 一夜 one-shot。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Codex = 写代码 | **Code review 是企业 adoption 第一拐点**（Datadog 也曾说 1/5 incident 本可拦住） |
| Skills = Claude 专属 | **跨职能共享 repo**，非 PM 也能跑 PM skills |
| Side project = 周末手搓 | **agent.md + plan skill + build**，人走开几小时 |
| 模型越强越好 | 输出 surprise 多半是 **假设没对齐**， upfront clarify 比改 prompt 重要 |

---

## 分话题讲

### 1. 公司内 Codex 三个转折点

**第一刻 — Slack 改文档**  
Docs 频道 @Codex，不用本地跑站。小改动，但 **workflow 从「开 IDE」变成「聊天改文档」**。

**第二刻 — 事故回溯 review**  
大 migration 数月后出 race condition；fix 后有人提议：**用 Codex retro review 旧 PR，看能不能抓到**。抓到了。团队反复 replay 类似场景，**模型能力 + 大型 code base + 生产级代码** 三条线对齐。

**第三刻 — PR 里把 Codex 当队友**  
工程师提 PR → `@codex review` → 按 comment 改 → 再 review，**Slack 里点进去能看到人机来回**。跨过「LLM 不够专业」的心理门槛。

**和你何干：**  
想推 AI coding，先找 **可 replay 的历史 incident + code review**，比泛泛 demo 有说服力。

---

### 2. 今天 Alchemy 怎么用 Codex

**PM 线：** 写 PRD、分析 customer feedback；**公司内部 Skills repo**，多职能复用。  
**平台线：** 假设 **100% 开发者在 AI 辅助下写软件**；还要想 **autonomous agent** 来链上集成——注册、调 API、跑任务，**人类开发者与 agent 开发者需求仍不同，长期可能收敛**。

**和你何干：**  
做 developer platform 要问：**你的 API 文档、鉴权、沙箱，agent 能自助走完吗？**

---

### 3. 创业时间线对比：七年前 vs 现在

Matthias 当年：copy-paste 原型 → 融钱 → **3–4 工程师几个月 MVP**。  
Alchemy 级产品：**~15 工程师一年半** 到 V1。  
他的判断：同样 Apple Watch 级 idea，**今天一个人不到一周** 能出第一版。

**和你何干：**  
有 idea 就先 **试 build**，别等「凑齐团队」。

---

### 4. Side project 体系：焦虑 → dispatch → 醒来验收

他曾焦虑「AI 这么好，不在电脑前就是浪费」。解法：**Skills + 流程**，让 Codex **plan → implement → test → 通知完成**，或 **research 竞品功能 → feature flag 实验批量上线**。

**Linear 用法：**  
12 个项目并行，单个项目 **159 个 done issue，零人工创建**——他只 **口述需求 + agent.md（工作偏好）+ create plan skill → build the plan**。

**核心：** LLM 输出让你不爽，通常是 **它做了你没说的假设**。他的流程 ** upfront 澄清**，再放手 build。

---

### 5. Demo：写作助手 + Codex App Server

Mac 全局快捷键（Cmd+Shift+Space）→ 语音输入 → **professional mode** 重写 Slack 文案。  
背后 **Codex App Server**，走 **ChatGPT 订阅**，不是单独 API key。  
同一套逻辑做了 **iOS keyboard extension**。

**和你何干：**  
Codex 订阅不只写代码；**App Server = 任意 app 的后端 inference**。

---

### 6. OpenClaw Lou、Watch、Computer Use

- **Lou（OpenClaw）**：Discord 频道绑 repo，手机走路也能 dispatch 家里跑的 Codex。  
- **Apple Watch**：短语音 → skills repo 里 test.md → iPhone 转写 → 路由 GitHub → Codex App Server 执行。  
- **Computer Use**：SSH 进树莓派，浏览器里 tedious 复制粘贴 admin panel URL，**全程看 agent 干活**（像看 Cursor 动画）。

**Snapcat eval：** 给猫玩的自拍 app（红点 + 前置摄像头）。十年前 hackathon **5 人一天**；昨晚 **one-shot + skills + 5.5**；UI 用 **生成参考图 → 让 Codex 按图实现 → 再统一 redesign 各页**。

---

### 7. 给 builder 的三条假设

1. **Assume it's possible** — 有 idea 多半能做。  
2. **Assume you can do it** —  blocker 常是「我觉得我不行」。  
3. **Assume it's your fault** — LLM 没做好，先想 **沟通/上下文**，再试；**多试几次** 才走远。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Code review 拐点** | 用历史 bug 证明 AI review 能抓 production 级问题 |
| **PR 内 @codex review** | 把 review-fix 循环放在 PR comment，像结对队友 |
| **共享 Skills repo** | 公司级任务模板（PRD、反馈分析）跨职能复用 |
| **agent.md** | 个人工作偏好/风格，新项目 initialize 时注入 |
| **Codex App Server** | 用 ChatGPT 订阅跑 inference，可嵌进自研 app |
| **Feature flag 实验** | 睡前 batch build 功能，醒来 toggle 决定去留 |
| **Snapcat eval** | 固定 side project 测新模型 one-shot 与 UI 质量 |

---

## 值得记住的原话

> **"We retroactively run code review with Codex to see if Codex would have caught the bug. And it did."**  
> 我们回溯用 Codex 做 code review，看能不能抓到 bug——抓到了。

> **"He was essentially using codex review in pull request comments as his teammate."**  
> 他在 PR comment 里把 Codex review 当队友来回改。

> **"I did not create or write a single one of these [Linear issues]. Codex did."**  
> 这些 Linear issue 我一个没写，全是 Codex 建的。

> **"If the LLM produces something surprising in a negative way… it had to make assumptions and didn't make them the way you would."**  
> 输出让你意外，通常是假设和你不一致。

> **"Assume you haven't found a way to communicate what you want yet. And try again."**  
> 先假设是你还没说清楚，再试。

---

## 小结

**这期最核心的判断：** 企业信 AI coding 的开关是 **code review 可验证 + PR 内人机协作**；个人 builder 的开关是 **Skills/agent.md 把偏好写死 + Linear 当 agent 的项目界面**，让人离开电脑也能并行很多实验。

**读完应带走：**
- Alchemy 同时改 **内部工作方式** 和 **对外 developer/agent 平台**。  
- Side project 不是「更努力坐在电脑前」，是 **dispatch Research+Build+Feature flags**。  
- 模型 eval 可以很简单：**十年老项目一夜 rebuild，看细节与设计**。

**和 vault 的关系：** Codex 企业落地链，接 [[Codex负责人-现场演示Codex]]、[[WorkOS-创建和使用Skills方法论]]、[[MOC - Agent Theory and Design]]。

---

## 行动启示

1. **选 1 个历史 incident**，用 Codex review 旧 diff，有结果再对内宣传。  
2. **建公司级 skills repo**，先从 PM 最高频任务（PRD、反馈摘要）开始。  
3. **个人项目写 agent.md**，新项目复制 initialize，减少「它猜错」surprise。  
4. **Linear/Jira 当 agent backlog**，你只提 intent，issue 生命周期交给 Codex。  
5. **固定一个 eval 小项目**（如 Snapcat），新模型出来只问「比上次好多少」。

---

## 相关阅读

- [[Codex负责人-现场演示Codex]] — Codex 官方 multi-agent、Skills 演示  
- [[WorkOS-创建和使用Skills方法论]] — Skills 跨 Claude/Codex/Cursor 方法论  
- [[OpenClaw创始人-我是如何使用OpenClaw的]] — OpenClaw + Codex 移动端 dispatch  
- [[Loop-Agent Loop到底是什么]] — code review 闭环 vs 开放式 loop  
- [[MOC - Agent Theory and Design]] — Agent 主题横切索引  

---

## 来源

- **视频**：[BV1i9E366EAr](https://www.bilibili.com/video/BV1i9E366EAr/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Matthias，Alchemy CPO  
- **时长**：~29:45  
- **转写**：Recastory `bilibili-retranscribe/BV1i9E366EAr/`（FunASR SenseVoice + cam++，**asr v2**）  
- **版本**：v2 读者向讲义（2026-07-02）
