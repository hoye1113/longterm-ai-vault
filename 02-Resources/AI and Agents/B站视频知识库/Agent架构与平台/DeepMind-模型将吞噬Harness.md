---
title: "DeepMind：模型将吞噬 Harness？"
source: "B站视频 - Google DeepMind 访谈"
source_url: "https://www.bilibili.com/video/BV18hjG6bE6t/"
speaker: "Logan Kilpatrick (Google AI Studio & Gemini API)"
duration: "51:10"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - harness_engineering
  - cursor
  - codex
created: 2026-07-02
description: "Logan Kilpatrick 谈 Antigravity 作 Google agent harness 主线、模型从权重到 expanding system 的演进、harness alpha 六个月内 upstream，以及 coding narrow superintelligence 与创业机会。"
transcript_source: "Recastory/workspace/knowledge/A5-deepmind-harness/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# DeepMind：模型将吞噬 Harness？

## 先搞懂这一期

**这是什么节目？**  
Google I/O 后的一期长访谈。主持人对话 **Logan Kilpatrick**——他同时负责 **Google AI Studio** 和 **Gemini API**，日常给 next-gen builders 做工具。整集约 51 分钟，从 agentic AI 一直聊到 world model、DeepMind 文化。

**这期在回答哪三个问题？**

1. **Google 的 agentic 战略到底是什么？** Antigravity 和 Gemini 是什么关系？
2. **「模型将吞噬 harness / scaffolding」**——外部编排层还有 alpha 吗？创业公司还能活吗？
3. **Coding agent 已经强到什么程度？** 对开发者、对世界模型、对 Google 内部研究节奏意味着什么？

**用一条线串起来（没看视频也能复述）：**

Sundar 在 I/O 宣布进入 **agentic era**。对 Google 来说，这不只是「模型更强」，而是多一条产品 **主线**：以前 Gemini 是 50+ 产品的 throw line；现在 **Antigravity** 正在成为 **agent harness** 的新 throw line——Search、Gemini App、Cloud、AI Studio 都在变成 **agentic native**，替用户 **take action**。

Logan 的核心判断：**两年前说的「模型 = 权重 in/out」已经过时**。今天的 Gemini 3.5 背后是 tool calling、hosted tools、search、code execution、containers、harness 叠出来的 **expanding system**。外部大家拼命建的 harness/scaffolding，很多能力会被 **upstream 进 native model**——按今天对 harness 的理解，**六个月内 alpha 会迁到别处**。

同时 coding 已强到像 **narrow superintelligence**：不是取代人类开发者，而是 **抬高你的 ambition 上限**——你以前觉得够不着的主意，现在敢想更大；但 research 侧的大训练 run 仍要人掌舵，不能把 token 随便烧。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 听过 harness、脚手架 | Google 官方视角：**Antigravity = 跨产品 harness 生态** |
| 担心模型公司吃掉应用层 | **两股力同时成立**：capability overhang 巨大 + vertical focus 仍是 startup 超能力 |
| Claude/Codex 占 coding 心智 | Google 叙事切换极快；**没有长时 agent 产品，很难做出 great coding model** |
| [[DeepMind团队-当数百万Agent相遇]] 谈 Agent 社会 | 这期谈 **Google 怎么把 harness 产品化**，以及 **模型吞噬 harness** 的时间表 |

---

## 分话题讲

### 1. Antigravity：Google 的 agent harness 新主线

**说法：**  
- **Gemini 时代**：语言模型 API 是统一 throw line。  
- **Agentic 时代**：**Antigravity** 是 agent harness throw line——产品不只回答，还要 **替用户做事**。

**Antigravity 不是单一 App，是一套生态：**
- Web 上 agent-first 体验  
- CLI  
- Skills  
- Gemini API 托管 agent（不想自建 infra 的开发者）

**关键句：** 同一 harness 驱动 Search、Gemini App、Cloud、AI Studio 等——不是只有 Antigravity 品牌那一个入口。

> **"It is the agent harness. Coding is a specialized use case of the agent harness, but coding has proved to be the general purpose agent harness."**  
> 这就是 agent harness；coding 是 specialized 用例，但 coding 已被证明是 **general-purpose agent harness**。

各产品对 harness 大约 **80% 共享 + 20% 定制**：AI Studio 偏 coding gold path；Gemini App 偏 consumer 24/7 always-on agent。

**和你何干：** 如果你在 Cursor / Codex / Antigravity 里写代码，你碰到的「模型 + 工具 + 多步」就是 harness；Google 正在把这条线 **横切进所有产品**。

---

### 2. Agentic 成熟度：整体还在 Crawl

Logan 用 crawl / walk / run 分级：

| 层级 | 代表 |
|------|------|
| **Crawl** | 大多数面向 13 亿+ 用户的 Google 产品——要 **stewardship**，不能 overnight 改用户与互联网的关系 |
| **Walk** | Gemini App（Spark）：24/7 always-on agent，可能替你做一堆 action |
| **Run（实验室）** | Antigravity autonomous coding：单次 **billions tokens、数千美元**；GDM 也在 frontier 探索 |

Search 是最典型的「有责任地带用户上车」的例子——不能突然把交互方式全换掉。

**和你何干：** 大众产品 agentic 会 **慢**；Labs / 开发者工具会 **快**。别用 frontier demo 的预期去要求 Gmail 明天全自动。

---

### 3. 业务蚕食？Google 更在意 Outcome，不是 Eyeball

早期担心 AI 问答会 **蚕食 Search**——实际 **搜索量上升**。Agent 做更多事的同时，人也在搜更多。

Logan 的成功定义：**不是最大化 eyeball time，是最大化 customer outcome**——帮用户办完事，他们去生活。

**Agent LB Growth（他的说法）：**  
个人用 coding agent 时，会让 agent **选基础设施**——「用什么数据库你定」。推而广之，shopping agent 也会替人选品。广告、SEO、**GEO（Generative Engine Optimization）** 会和旧逻辑 **叠加演进**，未必是 radical 颠覆。

---

### 4. Coding 格局：Gemini 叙事切换极快

主持人观察：开发者朋友 **Claude / Codex 大约各半**，Gemini 相对少。

Logan 的回应：
- **12 月** 叙事还是 Google 靠 Gemini 3 大幅领先；**假期 agentic coding 浪潮**后叙事又变——**warp speed**。
- **没有真正做 long-running agent 的产品，很难做出 great coding model**——Windsurf 收购、Antigravity 内部 token 消耗曲线就是证据：**engine spending takes time to make model progress**。
- **Gemini 3.5 Flash** 纯 post-training 就在 coding 上超过此前 Pro——团队功劳很大。
- 外部看「落后」可能 **miss 大 pre-training run 的时间线**——DeepMind 在大集群 pre-training 上是强项。

**Dogfooding：** 必须用 Gemini 换 feedback flywheel；但也 **healthy 使用竞品**——10 万+ Google 工程师 = 规模优势。

---

### 5. Soft Takeoff 与 Narrow Superintelligence

**Coding 加速 research 的自强化循环？** Logan 说「显然成立」，但模型侧仍 early——大训练 run 的资源分配还要 **human in the driver seat**，不能 accidental 烧掉一万 TPUs。

**产品侧已见迹象：**
- Antigravity 建 mobile app 比 Google 史上任何团队都快  
- Joshua 团队 Gemini Mac App 交付创纪录  

**Coding 像 narrow superintelligence：** 强到不可思议，但对人类开发者是 **accelerant**——**more agency**，敢 tackle 更 ambitious 的问题；副作用是 **MVP 不够了**，你会被技术抬着往「再做大十步」走。

下一批可能起飞的域：**verifiability 高的**——math、finance、science（有证明/测试/可重复实验）。

---

### 6. Vibe Coding 游戏与世界模型（Veo 3）

Logan 2025 年 10 月 tweet：**年底人人能 vibe code 视频游戏**——接近但未完全（不是 CoD/GTA 级 3A）。

瓶颈常在 **product scaffolding**：sprite 生成、Three.js 粗糙边、编排层——**不是纯 model quality gap**。

AI Studio 数据：曾约 **20% 应用是游戏**；GDM **GameArena** 用游戏作 AGI progress proxy（DeepMind 基因里游戏很深）。

**World model 定义在变：**
- 传统：action-conditioned video model  
- 现在（Veo 3 / Demis  framing）：**对世界有理解的 unified model**——不是 Gemini + 视频模型拼盘，是 **single true unified model**  
- 台上 live demo：实时给视频加狗、嘉宾反应、主持人继续讲——**subtle nuance** 极好  

Logan 个人对 generative media 的态度：内容 **authenticity** 重要——Veo 改的是 **布景**（咖啡桌、灯光），不是替换成 AI 版本人。

**短期游戏路径：** coding agent + game engine scaffolding > 纯 world model 直接做游戏（world model  inherent open-ended，要 scaffolding 才 usable）。

---

### 7. 核心争议：模型将吞噬 Harness

> **"What we have historically thought of as the model is not the model anymore... it's an entire expanding sprawling system."**

两年前 LLM = weights，tokens in/out。现在名字仍叫 Gemini 3.5 / GPT-x，实质是：
- Agentic tool calling  
- Hosted tools（search、code execution 等）  
- Containers 里 spin up model + harness  

**Scaffolding 往往领先模型几步** → 最终被 **upstream 进 native model system**。

**Agent harness 是 quintessential example：**  
人人说「alpha 在 harness」；Logan 认为 **按今天对 harness 的理解，六个月内** 模型会 digest 大量 harness 能力，**alpha 迁移到别处**——不是「不需要 harness」，是 **价值层上移**。

外部 scaffolding 仍有空间：例如 **可选 search provider**、**code execution** 多实现——模型 native 能 search，但你可能还要别的。

**Lock-in 论点：** 初期「绑某厂商 harness」成立；随 model capability 提升会减弱。需要 **HarnessBench** 类 benchmark：模型适配 **不同 harness** 的能力如何。

---

### 8. 创业公司还有没有机会？

两股力 **同时为真**：
1. **Capability overhang**——模型能做的事超前于产品 adoption，alpha 巨大  
2. **Model labs 做 general problems**——压力真实  

Startup superpower 仍是 **vertical domain expertise + focus**——「你能 focus，就能做成任何事」；Google 有义务服务 13 亿用户，**不能 focus 一个 wonder app**。

20 个月前担心 startup 空间收缩——实际 **机会更多**；coding agent 还帮你 **缩小与大公司 established codebase 的差距**。

---

### 9. AI Studio 与 DeepMind 文化（短）

**AI Studio：** 一周约 **35 万应用**被 build——很多是 **personal problem-solving** 软件，以前根本不会有人做；Android 成为 builder platform。

**DeepMind 文化（Logan 观察）：**
- Portfolio 强，偶有某域 under-invest 被拉开——**strike team** 文化仍在（Demis 纪录片）  
- Demis = 科学/Nobel 导向；Sam = business；Anthropic = safety——DNA 不同  
- 使命：solve disease、cancer——别迷失 benchmark 数字竞赛  
- DeepMind = Google **engine room** + 与 Android/Cloud 等 applied 协作  

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Antigravity** | Google 的 agent harness 生态（Web/CLI/Skills/API），驱动多产品 agentic 化 |
| **Throw line** | 横跨多条产品线的统一技术主线（Gemini → Antigravity） |
| **Agent harness** | 把模型「打算」变成多步 action 的编排层；coding harness 是其最强 specialized 形态 |
| **Model eats harness** | 外部 scaffolding 能力被 upstream 进 native model，独立 harness 的 alpha 衰减 |
| **Expanding system** | 今天的「模型」= 权重 + tools + hosted capabilities + containers，不只是 weights |
| **HarnessBench** | Logan 提议的 benchmark：测模型适配不同 harness 的能力 |
| **Narrow superintelligence** | 单域（如 coding）远超人类，但整体非 AGI |
| **Agent LB Growth** | Agent 替用户做选型/决策，改变 aggregator 与广告逻辑 |
| **Capability overhang** | 模型能力领先于产品与用户 adoption |
| **World model（新定义）** | 具世界理解的 unified model，非仅 action-conditioned 视频生成 |
| **Crawl/Walk/Run** | Google 产品 agentic 成熟度分级 |

---

## 值得记住的原话

> **"It is the agent harness... coding has proved to be the general purpose agent harness."**  
> 这就是 agent harness；coding 已被证明是 general-purpose harness。

> **"What we have historically thought of as the model is not the model anymore."**  
> 我们历史上对「模型」的理解已经不对了。

> **"The model eats that scaffolding... perhaps won't be true, at least in the way that we think of the harness today, in six months."**  
> 模型会吃掉 scaffolding；按今天对 harness 的理解，六个月内 alpha 会迁走。

> **"Success probably doesn't look like maximizing eyeball time... maximizing outcome for customers."**  
> 成功不是最大化盯屏时间，是最大化用户 outcome。

> **"It's actually really hard to make a great coding model... if you don't actually have a product that does that."**  
> 没有长时 agent 产品，很难做出 great coding model。

> **"Coding is just so good that it does kind of feel like narrow superintelligence... an accelerant... I have more agency in the world."**  
> Coding 强到像 narrow superintelligence；对我它是加速器，我在世界上有更多 agency。

> **"If you can focus, you can do anything."**  
> 能 focus，startup 什么都能做。

---

## 小结

**这期最核心的判断：** Google 把 **Antigravity 定为跨产品 agent harness 主线**；「模型」不再只是权重——**scaffolding 会被 upstream 进 native model**，但 coding harness 已是 narrow superintelligence 级加速器。

**读完应带走：**
- Coding 被 Logan 视为 **general-purpose agent harness** 的特殊用例；没有长时 agent 产品，很难训出 great coding model。
- 产品成功 metric 从 **eyeball time** 转向 **customer outcome**；搜索与 agent 可共生而非零和。
- 6–12 个月视野内，外部 harness 的 alpha 会迁移——价值留在 vertical workflow、eval、domain data。

**和 vault 的关系：** 与 [[DeepMind团队-当数百万Agent相遇]]、[[IBM团队-Harness工程详解]] 构成 Google / 通用 harness 三角。

---

## 行动启示

1. **别把 alpha 全押在「自建 harness」上**——6–12 个月视野内，能力会上游进模型；问：**上游之后价值在哪一层**（vertical workflow、eval、domain data）？  
2. **做 coding / agent 产品的人**：长时运行、真实 token 消耗 = **训练与迭代的基础设施**，不是副产品。  
3. **选模型时**：除 benchmark 外，看 **在你实际 harness 栈里** 的表现——未来可能需要 HarnessBench 式思维。  
4. **用 coding agent 时**：预期 **ambition 被抬高**——主动设 scope 边界，别被技术推着无限做大。  
5. **读 Google 产品节奏**：大众面 crawl、Labs run——**别用 frontier 标准要求 consumer 产品 overnight agentic**。

---

## 相关阅读

- [[DeepMind团队-当数百万Agent相遇]] — Agent 社会、委托与安全；与本期 harness 产品化互补  
- [[IBM团队-Harness工程详解]] — harness 可靠性第一性原理  
- [[2026 年 Agent 最重要的工程概念 Harness Engineering]] — OpenAI 侧 harness 实验与 docs-as-truth  
- [[Codex负责人-现场演示Codex]] — 竞品侧 coding agent 与 Skills 工作流  
- [[MOC - Harness Engineering]] — Harness 主题索引  

---

## 来源

- **视频**：[BV18hjG6bE6t](https://www.bilibili.com/video/BV18hjG6bE6t/)（B 站转载 Google DeepMind 访谈）  
- **嘉宾**：Logan Kilpatrick，Google AI Studio & Gemini API  
- **转写**：Recastory `A5-deepmind-harness/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
