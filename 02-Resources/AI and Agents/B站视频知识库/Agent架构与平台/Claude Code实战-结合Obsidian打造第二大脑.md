---
title: "Claude Code实战：结合Obsidian打造第二大脑"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1s2Gd6aEF7/"
speaker: "Noah Breyer（Aethic / Alephic 创始人，前 Percolate 联创）"
duration: "70:01"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - claude_code
  - context_engineering
  - memory
  - multi_agent
created: 2026-06-09
description: "Noah 展示 Obsidian vault + Git + 地下室 mini PC（Tailscale）+ 手机 Termius 跑 Claude Code；thinking 模式、Interviewer 子 agent、跨 vault 检索与 tacit 跨 repo 抄作业，主张 AI 的读强于写。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1s2Gd6aEF7/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Claude Code 实战：结合 Obsidian 打造第二大脑

## 先搞懂这一期

**这是什么节目？**  
AI & I 播客 **~70 分钟深度访谈**。嘉宾 **Noah Breyer**（Aethic/Alephic AI 战略咨询、BRXND 大会、前 Percolate 联创）展示他如何把 **Claude Code 当第二大脑**——主要 **不是写代码**，而是 **思考、研究、组织笔记**，并在 **手机上** 完成同等深度工作。

**这期在回答哪三个问题？**

1. **Claude Code + Obsidian 怎么组成「第二大脑」？** 文件夹、PARA、子 agent 各扮演什么角色？  
2. **为什么要在 vault 根目录起 Claude，而不是单项目子文件夹？**  
3. **手机 + 家庭服务器 + 语音（Grok）** 如何让人在「非 deep work 设备」上做研究？

**用一条线串起来（没看视频也能复述）：**

Obsidian = 本地 **markdown + 文件夹**；Git 同步；**Claude Code 跑在 vault 根**（可访问全库 PARA，sandbox 允许读子目录）。  
新 talk/项目 → 建文件夹 → frontmatter 声明 **thinking mode 禁止代写** → 让 Claude **扫全 vault 1500+ 笔记** 拉相关 research →  spawn **Interviewer 子 agent** 提问、记 running log → **daily progress** 按日汇总；ChatGPT/Claude/Grok 对话用 web clip 进 `chats/`。  
地下室 **mini PC + Tailscale VPN + Git pull** → 手机 **Termius** SSH 进 Claude Code → 公交站旁改 conference 站、pond 边 push PR。  
核心哲学：**generative 被过度强调——AI 的 read 能力日常更有用**；别让它 jump to artifact，要 **facilitate thinking**。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Claude Code = coding agent | **#1 用法是与笔记交互**；code 多是「已知问题的小修」 |
| Obsidian = 笔记 app | **Git-backed markdown OS**；可加 package.json 自定义命令 |
| 第二大脑 = 收集 | **Thinking mode + Interviewer**；显式禁止写稿 |
| Subagent = 写代码 | **Thinking partner** 子 agent：提问、记 log，不产出终稿 |
| [[Agent实战-打造一个AI Agent的完整教程]] 的 agents.md | Noah 用 **项目 frontmatter + 子 agent 定义** 达到类似边界 |

---

## 分话题讲

### 1. 栈：Obsidian + Git + Claude Code

**说法：**  
Noah 从 Evernote 迁到 Obsidian——因 **纯 md 文件** 可 Git sync、可被 agent 直接读。Claude Code 装在 **vault 根目录**（非单项目子文件夹）：sandbox 限制「不能随意跑根外命令」，但 **可读任意子目录**——适合「从全库找相关笔记」。  
Vault 用 **PARA** 组织；可加 **package.json** 注册自定义 slash/command，扩展 Obsidian 能力。

**例子：**  
BRXND 营销+AI 大会 talk 项目夹：`research/`（文章 PDF）、`chats/`（外站对话 clip）、`daily progress/`、`conclusions.md` 等。

**和你何干：**  
第二大脑要 agent 友好 → **markdown 优先**；起 Claude 的位置决定 **检索半径**。

---

### 2. Thinking Mode vs Writing Mode：禁止 jump to artifact

**说法：**  
模型默认 **helpful assistant = 急着帮你写完**。Noah 在 frontmatter 写死：**thinking mode，不要 outline/draft/任何 talk 正文，只 gather & organize**。仍常需反复 **「我说 no 就是 no」**。  
Ghostwriter 产品（如 Spiral）同理：好 ghostwriter **先 interview 再共写**，不是「给题目就交稿」。

**例子：**  
conclusions 文件是 **思考结论片段**，不是成稿；整 talk 仍在 piecing together 阶段。

**和你何干：**  
研究/策划类任务 **单独声明模式**；比通用「你是助手」有效得多。

---

### 3. Interviewer 子 Agent：Thinking Partner

**说法：**  
Claude Code **subagent** 定义成 **collaborative thinking partner**：facilitate thinking、**sharp questions**、**不代写**；对话中 **记 running log**（问了什么、 uncover 了什么）。  
可与 `chats/` 里 ChatGPT、Claude、Grok 的 **完整 transcript** 交叉——Interviewer 被要求 review 这些外部线程。

**例子：**  
「Transformers eating the world」线索：从 time series 论文、Tesla 删 30 万行 C++ 等碎片，跨月 thread 积累 → 与 OSS/Wild Bill Donovan/简单破坏手册 **conclusion 线** 慢慢织合。

**和你何干：**  
**子 agent = 角色契约**；thinking partner 是 Claude Code 里很值的一种。

---

### 4. 项目工作流：从空文件夹到 daily catch-up

**说法：**  
**Day 0**：声明 thinking mode → 给过往 talk 样例定风格 → 给大主题（如送《Simple Sabotage Field Manual》、transformers 叙事）→ **「扫全 vault ~1500 条，把相关的 pull 进 research/」**（多是 keyword/find 级 relevance，非概念跳跃）。  
**Day N**：外读 Wild Bill 传记、ChatGPT deep research → 新开笔记或 clip chat → Interviewer 串线。  
**中断后回归**：**「catch me up on the last three days」**——Claude 按日期读项目内新文件（Noah 称这是 **easy capability**，要会押在模型 strengths 上）。  
**Daily progress**：每天让 AI **写当日学到什么、推进了什么**。

**和你何干：**  
长周期思考项目 **必备 daily progress + catch-up prompt**；比依赖 chat memory 可靠。

---

### 5. 跨 Vault 检索：何时 relevant

**说法：**  
Noah 承认泛化「找 relevant 笔记」常 **牵强**；本 talk 的检索较简单——**主题已在 vault 里积累过**（破坏手册、OSS、 bureaucracy 等），agent 做 **find/grep 式收集** 即可。  
Relevance 在这里 = **已有思考线索的汇编**，不是 cold discovery。

**和你何干：**  
**先有人类策展的主题**，再让 agent 扫库；别期待 agent 替你做概念 leap。

---

### 6. 手机 + 家庭服务器：Termius + Tailscale

**说法：**  
地下室 **mini PC** 跑 Linux；**Tailscale** 私人 VPN（仅授权设备可连）；Obsidian vault **GitHub private repo** sync 到服务器；手机 **Termius** SSH → 直接 **Claude Code CLI** 在 vault 里思考、改 md、跑 subagent。  
周二送娃后早餐 **2 小时在手机上写 talk**；conference 站 broken link → 路边 pull repo、Claude 改、push PR。  
Noah 给朋友 **partition mini PC**，共享同款 phone workflow。

**和你何干：**  
**Git + 远程 Claude** = 轻量「第二大脑云」；不必等 SaaS 第二大脑产品。

---

### 7. Grok Voice Mode 与移动研究

**说法：**  
Noah 称 **Grok voice**（2/3/4 等版本）在 **tool calling + 研究深度** 上优于 ChatGPT voice / Gemini voice；Tesla 内置 Grok 按钮，长途开车 **多轮对话研究**（《伊利亚特》、self-attention、Walter Benjamin 等）。  
ChatGPT voice 问题：模型变强但 voice 层滞后、personality 怪、**tool calling 弱**。  
Voice = **「为你定制的播客」**——适合 curiosity-driven 探索，再沉淀进 Obsidian/Chats。

**和你何干：**  
**capture 管道**：voice 探索 → clip/摘要进 vault → Claude Code 深度整合。

---

### 8. Tacit 跨 Repo 代码共享：AI 当翻译层

**说法：**  
Every 内多产品 **各用各栈**（Rails/TS…）；历史上要抽象共享库很重。现在：**把开发者加进另一 repo**，「让 Claude Code 去看 Sparkle 怎么做的 file search，在 Para 里做一版」——**tacit code sharing**，不必模块化。  
Alephic 对客户项目用 **GitHub MCP**：「去看 intelligence repo 里 CRM 那套怎么实现的，搬过来」。  
Noah 的 **aha moment**：ChatGPT Plugin spec——**manifest.json 描述怎么收发数据**，平台处理 rest；与一辈子 **确定性 API 集成直觉 180°**——probabilistic computer 需要 **新 fingerspitzengefühl（指尖感）**。

**和你何干：**  
Monorepo 不是唯一复用法；**agent 读他库实现** 是低成本对齐手段。

---

### 9. 小工具、Linux 助手与孩子/媒介素养

**说法：**  
**Attachments 清理**：Obsidian 附件名混乱 → Claude Code 小工具用 **Gemini Flash** 批量 rename、建 metadata 表、回写链接（类似 Sparkle 思路）。  
**Claude Code helpers**：Omarchy Linux、Mac Homebrew、新机器 **一键偏好**（pip→uv 等）——「不熟悉命令行时 Claude 当 sysadmin」。  
**Ten 岁女儿 v0 vibe code** 抽 Secret Santa app（75 iter，自己悟到 groups 数据建模）——Noah 认为 **10 岁能 ship app 不可能是 bubble**。  
教育观：别藏 AI；English teacher  job 是 **让人想学会写**，不是防 cheat；**《The Truth Detective》** 儿童媒介素养；hallucination = 互联网 misinformation 的 cousin。

**和你何干：**  
Vault 维护 **可脚本化**；family/education 讨论是 **AI literacy** 延伸，非本栈必需但体现 Noah 整体观。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Thinking mode** | 只收集组织思考，禁止代写终稿 |
| **Interviewer subagent** | 提问式 thinking partner + running log |
| **Daily progress** | 按日汇总项目学到什么 |
| **Catch me up** | 中断后按时间读文件恢复上下文 |
| **Vault 根起 Claude** | 全库 PARA 检索 vs 单项目隔离 |
| **Tailscale + Termius** | 手机 SSH 进家服 Claude Code |
| **Read > Write** | AI 日常读/整合比生成 artifact 更值 |
| **Tacit code sharing** | 跨 repo 让 Claude 读实现再移植 |
| **Thomas's English Muffin theory** | AI 渗入组织缝隙，不必统一工具栈 |

---

## 值得记住的原话

> **"Probably my number one Claude Code use is using it as a tool to interact with my notes."**  
> Claude Code 第一用法是跟笔记交互。

> **"There's entirely too much focus on its ability to write and not enough on its ability to read."**  
> 太关注写，不够关注读。

> **"Thinking mode — do not create outline drafts or any versions of talks writing."**  
> 思考模式：不要写大纲或任何讲稿版本。

> **"Can you catch me up on the last three days of research?"**  
> 帮我追上过去三天的研究——回归深工作利器。

> **"The phone is not the best place for deep work… I feel like it's really changed."**  
> 手机曾不适合深工；这套栈改变了这一点。

> **"Just ask Claude Code to figure out how it works and do your own version."**  
> 让 Claude Code 看懂他库实现，再做你的版本。

> **"Fingerpitzengefühl — building fingertip feeling."**  
>  probabilistic 工具要靠用出来直觉，不能单靠旧软件集成经验。

---

## 小结

**这期最核心的判断：** **Obsidian（Git markdown）+ Claude Code（读全库、子 agent、模式约束）+ 可选家服远程** = 可落地的第二大脑；价值在 **thinking / research / 跨笔记整合**，不是替写讲稿。

**读完应带走：**
- **Frontmatter + Interviewer** 对抗「急着写稿」；**daily progress + catch-up** 对抗中断。  
- **根目录起 Claude** 换全 vault 检索；项目文件夹管 scope。  
- **Tailscale + Termius** 把手机变成深工终端；voice（Grok）作上游 capture。  
- **跨 repo**：AI 读代码 == 低成本 best practice 迁移。

**和 vault 的关系：** Claude Code 非编码工作流样板，接 [[Agent实战-打造一个AI Agent的完整教程]]、[[IBM团队-Harness工程详解]]、[[Loop Engineering 橙皮书 - 花叔]]。

---

## 行动启示

1. **Obsidian vault 接 Git**；Claude Code 在 **vault 根** 启动。  
2. **新项目 frontmatter**：thinking vs writing mode 写死。  
3. **建 Interviewer 子 agent**（或 CLAUDE.md 等价规则）：只问只记不写。  
4. **daily progress 笔记** + 回归时用 **catch me up N days**。  
5. 若要手机用：旧机器 + **Tailscale** + **Termius** + private Git sync。  
6. 附件/重复 chore → **一次性 Claude 小脚本**（rename、metadata）。

---

## 相关阅读

- [[Agent实战-打造一个AI Agent的完整教程]] — agents.md、memory、MCP、Skills 入门  
- [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] — Claude Code 团队视角  
- [[IBM团队-Harness工程详解]] — harness、verify、context 管理  
- [[Manus创始人-深度干货-上下文工程的最佳实践]] — 长任务 context offload/compact  
- [[Loop Engineering 橙皮书 - 花叔]] — Loop / 留痕与迭代  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1s2Gd6aEF7](https://www.bilibili.com/video/BV1s2Gd6aEF7/)（B 站 *Easonlee的AI笔记*）  
- **嘉宾**：Noah Breyer（Alephic.com / BRXND.ai）  
- **时长**：~70:01  
- **转写**：Recastory `bilibili-retranscribe/BV1s2Gd6aEF7/`（FunASR SenseVoice + cam++，**asr v2** 67 段）  
- **版本**：v2 读者向讲义（2026-07-02）
