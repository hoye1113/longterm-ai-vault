---
title: "OpenClaw 创始人：我是如何使用 OpenClaw 的？"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1WnctziEac/"
speaker: "Peter Steinberger（OpenClaw 创始人，前 iOS/Mac 20 年）"
duration: "37:43"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - claude_code
  - skills
created: 2026-06-09
description: "Peter Steinberger 演示 OpenClaw：WhatsApp 接 Claude Code、CLI 军队、摩洛哥用截图修 Twitter bug、语音消息自解 ffmpeg+Whisper；并泼冷水——别沉迷 orchestrator 与 24h Ralph loop，Just talk to it。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1WnctziEac/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# OpenClaw 创始人：我是如何使用 OpenClaw 的？

## 先搞懂这一期

**这是什么节目？**  
访谈 **OpenClaw（clawd.bot）创始人 Peter Steinberger**——**屏幕共享安装/onboard** + **AI coding 硬观点**「Just talk to it」。OpenClaw = 把 **Claude Code 级 agent** 接到 WhatsApp/Telegram/Discord 等，**住在你电脑上**，有文件/浏览器/CLI 就能干你能在电脑上干的事。

**这期在回答哪三个问题？**

1. **OpenClaw 从哪来、为什么叫龙虾？** 退休回来想 **手机遥控电脑上的 vibe coding agent**；大厂没做，11 月自己 hook WhatsApp → Claude Code binary，现在 **~30 万行**，全平台 IM。  
2. **有多「资源化」？** 摩洛哥 **截图 Twitter bug → WhatsApp → 读推、checkout、fix、commit、回推**；没做语音却 **ffmpeg + curl OpenAI 转写** 自己搞定。  
3. **Peter 怎么看 AI coding  hype？** 反对 **Gas Town 式多 agent 编排、Ralph 24h 空转**；主张 **人在 loop、有 taste、多终端并行、PR 当 prompt request**。

**用一条线串起来：**

「电脑上的怪朋友」→ CLI Army（Google Places、meme、八小时睡眠 API、外卖 ETA…）→ **20 年 ObjC/Swift 的人用 AI 跨到 TS/JS** → 安装/onboard（API key 推荐，订阅有灰色地带）→ 接邮件/日历/Philips Hue/Sonos/摄像头（误报陌生人坐沙发一整夜）→ **英航值机** 当 browser agent 终极测试 → **80% 手机 App 会化**（健身、todo、值机…一个懂上下文的 assistant 就够）→ **Just talk to it**：别堆 orchestrator，5 个 repo checkout 像 RTS 微操。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Claude Code = 写代码 | **Unshackled ChatGPT**——任何能 CLI/浏览器解决的问题 |
| OpenClaw = 聊天壳 | **Harness 可读自己源码**，self-reconfigure；**Skills 持久记忆** |
| Agent = 越自动越好 | **24h 无人 loop 产出 slop**；taste 和 feel 必须人在 loop |
| 要多 agent 编排 | Peter：**MCP/大编排不信**；多开 terminal checkout 更简单 |

---

## 分话题讲

### 1. 起源：WhatsApp → Claude Code，一行进一行出

Peter「退休」回来，agent 跑一小时你吃饭，**两分钟就停下来问你**——很烦。以为大厂会做「手机管电脑 agent」，11 月还没有，就 **WhatsApp 消息调 Claude Code binary**。  
后来 **300k LOC**，几乎全 IM 平台。

**核心句：** 给 AI **电脑级访问**，它就能做 **你能做的一切**（含风险）。

---

### 2. 摩洛哥两个「啊哈」时刻

**Bug 修复：** 推截图发 WhatsApp → agent 读推、clone、fix、commit、**Twitter 回复已修复**。  
**语音：** 他没做 voice support，发语音 → agent 读文件头猜 audio → **ffmpeg 转 wav → curl OpenAI 转写 → 正常回复**。Peter：**比网页 ChatGPT 有意思得多**。

**和你何干：**  
Agent 价值在 **工具链即兴组合**，不是产品里预置的每个功能。

---

### 3. CLI Army 与跨栈 superpower

Agent 擅长 **调 CLI**（训练偏 tool call）。Peter 自建：Google 全家桶、Places、meme/gif、sound 可视化、**外卖 ETA 逆向**、**Eight Sleep 温控**。  
20 年 Apple 栈专家转 JS/TS：**概念都在，语法慢**；AI 抹平语法，**系统思维、品味、依赖选择** 仍值钱。

---

### 4. 安装、onboard、风险

- 站点 **clawd.bot** 一行 install（开源可审）；Mac/Linux/Windows；也可 git clone **hackable install**（agent 读自己 harness 源码自改）。  
- **onboard**：选模型（API key 稳；订阅 Claude 有 ToS 风险）、Telegram/Discord、Skills/Hooks。  
- **权力=风险**：删 home、锁门（智能锁）、给信用卡—— enthusiast 玩法，新手要边界。

**人格：** Claude「灵魂文档」梗 + roast；接 **everything** 后真的会根据你的数字生活怼你。

---

### 5. 用户创意与 80% App 融化

社区：群聊 family member、Twitter bookmark → todo、睡眠提醒、**代购物**、值机。  
Peter 判断：**~80% 手机 App** 可被 **无限资源化 assistant** 替代——Fitness 知道你在 KFC 还会 roast；Eight Sleep 直接调 API；todo/值机/购物 **对话 + 上下文** 即可。

**Skills + 记忆：** 第一次手把手，之后 **写 skill 记住**，第二次两分钟。

---

### 6. 「Just talk to it」——反 orchestrator

Peter 批 **Gas Town**（市长、water、多 agent 互聊）、**Ralph loop**（小步做完丢 context 重来 = **token 焚烧机 + slop**）。  
**问题：** agent **spiky smart 但无 taste**；vision 要在 **build-play-feel** 里长出来，不能全 upfront 规划。  
**24h loop** 是 vanity metric；玩可以，别当生产力。  
** skeptics 误区：** 忽略 AI 一年，花一天写短 prompt 做 iPhone app（在 Linux 上）→ 不 compile →  dismiss **一整年**——要 **持续 play** 才懂「怪物」怎么推理。

**他的工作流：**  
- 新功能：**Discord 截图/复制对话 → terminal「let's discuss」**；help 区 scrape 找 pain point。  
- **不用 MCP、不信大编排**；**5 个 repo checkout**（clawdpot 1–5），像 **RTS 编队**，limiting factor 是 **自己的思考** 不是 Codex 慢。  
- **PR = prompt request**：非技术合伙人也能发 PR，他 **抽 intent 自己重写**。  
- Plan mode？Anthropic 因 model **太 eager 写代码** 才加；他更喜欢 **Codex 慢但稳**，自然语言讨论 option 再动手。  
- Context compact：**老问题**；Codex context 体感长 2–3 倍；多数 feature **单窗口** 够。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **OpenClaw / clawd.bot** | IM 前端 + 本地 Claude Code（等）agent，开源 |
| **Unshackled ChatGPT** | 有电脑权限的 web ChatGPT，能自建工具链 |
| **CLI Army** | 给 agent 一堆 CLI，扩能力不靠 GUI App |
| **Hackable install** | git clone 跑，agent 可读源码改 harness |
| **Skill** | 教 agent 一次，持久复用（值机、购物…） |
| **Just talk to it** | 别过度工程 orchestrator，直接对话迭代 |
| **PR as prompt request** | 非完美 PR 只传意图，维护者按 intent 重做 |
| **80% apps melt** | 单上下文 assistant 替代大量垂直 App |

---

## 值得记住的原话

> **"You're just like having a new weird friend that is also really smart and resourceful that lives on your computer."**  
> 像多了个住你电脑里、怪但聪明又足智多谋的朋友。

> **"It read the tweet… fixed it… replied on Twitter that it's fixed now."**  
> 读推、修 bug、commit、回推说修好了。

> **"It's like unshackled ChatGPT."**  
> 像解开枷锁的 ChatGPT。

> **"Those agents don't really do yet is have taste."**  
> Agent 还不会有品味。

> **"Just talk to it."**  
> 就跟它说（别堆复杂编排）。

> **"I treat pull requests more as prompt requests."**  
> PR 我当 prompt request 看。

---

## 小结

**这期最核心的判断：** OpenClaw 卖的是 **IM × 电脑权限 × 资源化 problem-solving**；真正难的是 **安全边界与 taste**，不是再套一层 Gas Town。Peter 的实践是 **多 terminal、截图进讨论、Skills 记琐事、人在 loop**。

**读完应带走：**
- Agent 会 **即兴组合 ffmpeg/curl/API**，比预置功能狠。  
- **80% App** 论：API + 上下文 + 对话，替代很多 silo app。  
- 反 hype：**24h Ralph、多 agent 管弦乐** 常产 slop；持续玩比一日评判重要。

**和 vault 的关系：** OpenClaw 生态入口，接 [[30分钟精通OpenClaw]]、[[5次创业者-AI智能体独自经营初创公司]]、[[MOC - Agent Theory and Design]]。

---

## 行动启示

1. **新手安全路径：** 只读日历/灯/提醒，别一上来给邮件写权限+信用卡。  
2. **教一次就 skill 化**——值机、重复 workflow 写进 skill markdown。  
3. **别追 24h 无人 loop**；用 **Discord/截图 → discuss** 开功能。  
4. **跨栈别怕**：系统设计与品味比语法重要，交给 agent 写 boilerplate。  
5. **贡献 OpenClaw：PR 写清 intent** 即可，维护者可能按 prompt 重做。

---

## 相关阅读

- [[30分钟精通OpenClaw]] — 安全设置、memory、5 用例  
- [[5次创业者-AI智能体独自经营初创公司]] — Ryan Carson R2 / cron+skill 幕僚长  
- [[OpenClaw实战-从本地到K8S部署]] — 容器化与企业安全叙事  
- [[Claude Code负责人-AI原生团队如何使用AI]] — Claude Code 团队侧对比  
- [[Loop-Agent Loop到底是什么]] — 何时要闭环、何时开放式 loop 是浪费  

---

## 来源

- **视频**：[BV1WnctziEac](https://www.bilibili.com/video/BV1WnctziEac/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Peter Steinberger，OpenClaw 创始人  
- **时长**：~37:43  
- **转写**：Recastory `bilibili-retranscribe/BV1WnctziEac/`（FunASR SenseVoice + cam++，**asr v2**）  
- **项目**：[clawd.bot](https://clawd.bot) / GitHub 开源  
- **版本**：v2 读者向讲义（2026-07-02）
