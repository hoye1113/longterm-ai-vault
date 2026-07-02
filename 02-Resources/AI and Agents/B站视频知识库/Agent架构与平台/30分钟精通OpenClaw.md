---
title: "30分钟精通OpenClaw（5个真实用例+设置+内存）"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1kWctzeEYK/"
speaker: "Peter（OpenClaw 早期用户，Bot 名 Zoe）"
duration: "28:51"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - skills
  - memory
  - hooks
created: 2026-06-09
description: "Peter 用 Zoe 演示 OpenClaw 安全五步法、日历/文档/语音/日报/创作者周报五用例、Google Workspace OAuth 配置，以及 SOUL/USER/MEMORY 等 MD 人格与记忆文件。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1kWctzeEYK/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# 30 分钟精通 OpenClaw（5 个真实用例 + 设置 + 内存）

## 先搞懂这一期

**这是什么节目？**  
Peter（频道主，Bot **Zoe**）的 **~29 分钟实操教程**。在 Mac mini 上现场 demo：**安全 setup → 5 个真实用例 → Google Workspace 接入 → memory/人格 MD 文件**。

**这期在回答哪三个问题？**

1. **OpenClaw 怎么设才相对安全？** Dedicated 机器、独立账号、audit、权限最小化？  
2. **日常到底能干什么？** 五个他真在用的 task 是什么？  
3. **怎么让 Bot 「像懂你的朋友」？** memory 存在哪、怎么编辑？

**用一条线串起来（没看视频也能复述）：**

结论先行：OpenClaw 是他用过 **最好的 personal AI assistant**，但仍 **early software**。  
**安全五步**：① 专用机器（Mac mini/旧 MacBook，24/7）② Bot **独立 Apple/Gmail** ③ `openclaw security audit --fix` ④ **读日历、写选定文件**（非全盘 Drive）⑤ **绝不共享 Bot**（群聊/公开站 = 泄密风险，有 vibe-coded app 泄漏先例）。  
**五用例 demo**：日历（查 Caltrain → 发 invite 到自己主 Gmail）、Google Doc/Sheet 编辑（共享文件给 Zoe）、**Edge TTS 语音** dad joke、**cron daily briefing**（天气/日历/内容排期/Twitter 趋势 + memory 个性化）、**weekly creator email**（yt-dlp YouTube 公数 + Substack 浏览器抓 stats + 竞品选题）。  
**Google Workspace**：GCP 建项目 → 开 Gmail/Calendar/Drive/Docs/Sheets/Slides API → OAuth consent → desktop client 下载 JSON → ** paste 给 Zoe 配**。UI 烂，**让 Bot 一步步带**。  
**Memory/人格**：`~/.clawdbot/`（ASR 作 cloudud）下 **SOUL.md**（价值观/语气）、**USER.md**、**IDENTITY.md**、**MEMORY.md**（长期记忆、open loops/tensions/patterns）、**HEARTBEAT.md**（30 分钟查 ongoing tasks）、**memory/YYYY-MM-DD.md** 日记；可手改或 chat 让 Zoe 改。  
收尾：Peter Steinberger 一人开源、**builder 典范**；安全 setup → tinkering → 接 Workspace → 当朋友用。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| OpenClaw = 聊天 Bot | **cron + 工具链 + Workspace OAuth** 的 personal OS |
| AI 助理 = ChatGPT App | **Telegram  texto + 语音 + 邮件周报**，24/7 在 dedicated 硬件 |
| Memory = 向量库黑盒 | **本地 MD 文件**（SOUL/USER/MEMORY/daily notes）可读可改 |
| 安全 = 别用 | **最小权限 + 独立账号 + audit** 的可操作清单 |

---

## 分话题讲

### 1. 安全五步（必做）

**说法：**

| 步 | 做法 |
|----|------|
| 1 | **Dedicated 电脑**，24/7 在线（Mac mini + 免费 keep-awake app） |
| 2 | Bot **独立凭证**（独立 Gmail/Apple ID） |
| 3 | Terminal 跑 **`openclaw security audit --fix`** |
| 4 | **读**个人日历；**写**仅共享的 Doc/Sheet；不碰整个 Drive |
| 5 | **Bot 只服务你一人**——不加群、不上公开网 |

**例子：** 有人把 Bot 接 vibe-coded app，**机密漏到公网**。

**和你何干：** Personal agent **权限越大，隔离越狠**——独立账号不是矫情，是底线。

---

### 2. 用例一：日历（最小权限版）

**说法：**  
Zoe 有 **自己的 Google Calendar**；Peter **只读共享**个人日历给 Zoe。  
Telegram：「查 Caltrain 10am 班次 → 发 10:14 家庭出行 invite」→ Zoe 浏览查班次 → **以 attendee 发 invite 到主 Gmail**。  
不如直接给主日历 API 强大，但 **安全**；比手开 Google Calendar 快。

**和你何干：** **Share read + Bot 发 invite** 是日历自动化的 pragmatic 折中。

---

### 3. 用例二：文档与表格

**说法：**  
共享 Doc「Peter-Zoe」→ 「写 ferry building 出行计划」→ 2 分钟填好路线、午餐、tips。  
共享 **内容排期 Sheet** → 「加标题 Master OpenClaw in 20 minutes 到 2/4 格」→ 精确改 cell。  
移动场景 ** texto Bot 改 Doc/Sheet** 比 ChatGPT 复制粘贴省太多。

**和你何干：** **按文件共享** 而非全盘 Drive，是 Workspace 集成模板。

---

### 4. 用例三：语音（Edge TTS）

**说法：**  
问 Zoe 有哪些 TTS → 选免费 **Microsoft Edge TTS**（300+ 声音）→ 「发 voice note 讲 dad joke」。  
Setup：**让 Bot 自己配 gateway**——「set up edge TTS」即可。  
可双向：Whisper 输入 + 语音回复；适合问候、口述摘要。

**和你何干：** OpenClaw **「问 Bot 配 Bot」**——first-class 用法，别自己啃 config。

---

### 5. 用例四 & 五：Cron 简报

**Daily briefing（cron）：**  
拉 **天气、日历、内容排期、Twitter 读权限、memory** → 个性化提醒（例：「你整周 infrastructure mode，该 shipping 了」）。  
**Weekly Inside Report（邮件）：**  
- YouTube：**yt-dlp** 拉公数 + 竞品频道  
- Substack：**无 API** → Zoe 作 **admin 用 browser** 抓 stats（核对过准确）  
→ 邮件：选题建议 + 自己的 YT/Substack 数据。

**和你何干：** **Cron + 多数据源** 是 personal agent 的 killer feature；Substack 案说明 **browser tool** 补 API 缺口。

---

### 6. Google Workspace 接入（痛苦但值得）

**说法：**  
GCP Console 建项目 → APIs & Services **逐个 enable**（Gmail/Calendar/Drive/Docs/Sheets/Slides…）→ OAuth consent（external + test user）→ **Desktop OAuth client** → 下载 JSON → Telegram 贴给 Zoe → OAuth 流程 Bot 代跑。  
Google Cloud UI **很难用**；卡住就 **截图问 Zoe**。

**和你何干：** 预算 **30 分钟 + Bot 向导**；写进 runbook 给第二次部署。

---

### 7. Memory 与人格：本地 MD

**说法：**  
关键文件（路径以 OpenClaw 实际为准，演讲示 `clawdbot` 目录）：

| 文件 | 作用 |
|------|------|
| **IDENTITY.md** | 名字、emoji、语气（Zoe：warm, sharp, funny） |
| **SOUL.md** | 价值观、voice rules（禁 AI 腔、active voice、少 emoji…） |
| **USER.md** | 关于你的信息 |
| **MEMORY.md** | 长期 curated 记忆；**open loops / tensions / patterns** |
| **HEARTBEAT.md** | 每 30 分钟看有没有 ongoing tasks |
| **memory/日期.md** | 每日对话 recap |

**MEMORY 高级用法：**  
- **Open loops**：你提过但没闭环的事  
- **Tensions**：公开自我 vs 私聊矛盾  
- **Patterns**：Bot 观察到的行为模式（如「building  energizes you」）

可 **直接编辑 MD** 或 chat 让 Zoe 更新；daily notes 可 feed 进 **更洞察的 briefing**。

**和你何干：** Personal agent 差异化在 **MEMORY/SOUL 策展**，不在模型名。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Zoe** | Peter 的 OpenClaw Bot 实例 |
| **security audit --fix** | OpenClaw 内置安全加固命令 |
| **Dedicated credentials** | Bot 独立 Gmail/Apple，与主账号隔离 |
| **Edge TTS** | 免费 Microsoft 语音合成 |
| **Cron jobs** | OpenClaw 定时任务（日报/周报） |
| **yt-dlp** | 拉 YouTube 公开视频数据 |
| **SOUL / USER / MEMORY** | 人格、用户、长期记忆 MD 文件 |
| **Open loops** | 未闭环承诺/目标，供 Bot 提醒 |

---

## 值得记住的原话

> **"OpenClaw is generally the best personal AI assistant that I've ever used... still really early software."**  
> 是我用过最好的 personal AI；但仍是很早期的软件。

> **"Run it on a dedicated computer... its own credentials... security audit... never share your bot."**  
> 专用机、独立账号、安全审计、绝不共享 Bot。

> **"Someone's vibe coded app started leaking confidential stuff to the public."**  
> 有人把 Bot 接公开 app，机密漏了。

> **"It's not as powerful as full calendar access, but this is the safe way."**  
> 没全权日历强，但这是安全做法。

> **"Just ask Zoe to set up edge TTS — it will do the whole thing for you."**  
> 让 Zoe 配 TTS，它全包。

> **"Substack has no public API... added Zoe as admin... uses the browser."**  
> Substack 无 API；Zoe 当 admin 用浏览器抓数。

> **"Memory and personality is managed through a bunch of local MD files."**  
> 记忆和人格就是一堆本地 MD 文件。

> **"Not just something that gets stuff done — make a friend that guides you."**  
> 不只是干活，要做成会引导你的朋友。

---

## 小结

**这期最核心的判断：** OpenClaw 的个人助理价值 = **安全 isolated setup + Telegram/voice/cron 日常链 + Workspace 最小共享 + MD memory 策展**；早期但 **「问 Bot 配 Bot」** 把 GCP OAuth 等摩擦压到可接受。

**读完应带走：**
- **安全五步** 和 **五用例** 可直接抄作 personal agent checklist。  
- Google 集成：**按文件/日历共享 + OAuth JSON 给 Bot**，别给主账号全权。  
- **SOUL/MEMORY/open loops** 是「像朋友」的关键，不是更大模型。

**和 vault 的关系：** OpenClaw 入门线，接 [[OpenClaw创始人-我是如何使用OpenClaw的？]]、[[OpenClaw实战-从本地到K8S部署]]、[[Taven创始人-将OpenClaw嵌入产品的实战经验]]。

---

## 行动启示

1. **Mac mini/旧机 + 独立 Gmail** 起 OpenClaw，跑 **`security audit --fix`**。  
2. **先日历+单 Doc 共享**，跑通 texto → invite / 写 Doc。  
3. **加 daily cron briefing**，链 calendar + 一个 Sheet + 只读 Twitter。  
4. **GCP OAuth 让 Bot 向导**；JSON paste Telegram，省自己读 doc。  
5. **编辑 SOUL.md**：禁 AI 腔、主动语态、你的偏好写死。  
6. **MEMORY 加 open loops**，让 daily briefing 催你闭环大目标。  
7. **Bot 永不进群、不接公开站**。

---

## 相关阅读

- [[OpenClaw创始人-我是如何使用OpenClaw的？]] — Peter Steinberger 创始人视角  
- [[OpenClaw实战-从本地到K8S部署]] — 容器化与团队部署  
- [[Taven创始人-将OpenClaw嵌入产品的实战经验]] — Pi/OpenClaw 企业嵌入  
- [[WorkOS-创建和使用Skills方法论]] — Skills 与扩展  
- [[IBM团队-Harness工程详解]] — harness、安全与 verify  

---

## 来源

- **视频**：[BV1kWctzeEYK](https://www.bilibili.com/video/BV1kWctzeEYK/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Peter（OpenClaw 早期用户，Bot：Zoe）  
- **时长**：~28:51  
- **转写**：Recastory `bilibili-retranscribe/BV1kWctzeEYK/`（FunASR SenseVoice + cam++，**asr v2** 48 段）  
- **版本**：v2 读者向讲义（2026-07-02）
