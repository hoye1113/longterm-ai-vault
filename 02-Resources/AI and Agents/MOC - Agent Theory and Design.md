---
title: MOC - Agent Theory and Design
description: Agent 时代理论与实践的横切索引——覆盖 Harness、Claude Code、Codex、Cursor、OpenClaw、AI
  团队组织、AI 时代职业/方法论 6 大子主题，34 篇笔记
created: 2026-06-11
updated: 2026-06-25
tags:
  - ai_agent
  - ai_philosophy
  - moc
  - article
source: vault_initiative - moc - ai_agent - harness_engineering - claude_code -
  codex - cursor
---

# MOC - Agent Theory and Design

> 主题 MOC（合并自原 `MOC - AI Agent 参考资料` + `MOC - B站视频知识库`），覆盖 `02-Resources/AI and Agents/` 下所有"Agent 理论 + 实践"类笔记。共 **34 篇**笔记，按 9 个子主题分组。
>
> **本 MOC 是 v1（圆桌共识落地）**，建立 3 个横切 MOC 后，这里只承担"主题 MOC"角色——跨子目录的横切链接见：
> - [[MOC - Harness Engineering]]（横切，跨课程/公众号/B站）
> - [[MOC - AI 时代个人发展与组织]]（横切，FDE/职业/哲学）
> - [[MOC - Prompt 工程]]（横切，Prompts + Skills）

---

## A. Harness Engineering（7 篇）

> 围绕"harness = 围绕 Agent 的工程系统"这一概念展开。**Anthropic（Claude Code）** 与 **OpenAI（Codex）** 两大权威来源 + IBM 团队的登山绳比喻 + 三元同学的反向思考 + 花叔的 Loop Engineering 橙皮书 + ConardLi 的 Harness 迁移实战 + 卡颂的「遇事留痕」+ 1752 行 Anthropic 官方汇编本。

| 文章 | 核心主题 |
|------|---------|
| [[祝贺Claude Code成功越狱，获得永生]] | 花叔逆向 Claude Code 泄露的 1902 源文件，harness 内部由 system prompt / 四层权限 / 记忆 / 9 段式压缩 / swarm / grep 构成 |
| [[2026 年 Agent 最重要的工程概念 Harness Engineering]] | OpenAI 5 个月 0 人工代码 100 万行实验；harness = docs/ 当 source of truth + linter 强制不变量 + 黄金原则 |
| [[IBM团队-Harness工程详解]] | Harness = 登山绳 + 黑盒模型对抗；可靠性比聪明重要 |
| [[别再搭 Harness 了，先把你的痛点解决，用最笨的方式]] | 马斯克五步法在 Agent 工作流上的应用；先痛点后系统 |
| [[Loop Engineering 橙皮书 - 花叔]] | 五动作循环 + 六零件 + 四笔代价；Loop = Harness 上一层 |
| [[Harness 实践 - 将任何文字编辑成精美的文章 - ConardLi]] | 用同一套骨架（8 Phase + 3 Checkpoint + Reacticle）将任意文字编辑成精美网页文章，验证 Harness 可迁移 |
| [[遇事留痕 - Loop Engineering 的基础 - 魔术师卡颂]] | Session Log + GitHub issue/PR 是项目自我优化的燃料，自动优化循环的基础 |
| [[Anthropic Agent 工程实战指南 - 从入门到生产落地]] | 1758 行 Anthropic 官方 15 篇博客汇编，按"入门-进阶-核心-高级-生产"5 模块系统化梳理 |

---

## B. Claude Code 实战（3 篇）

> Anthropic Claude Code 团队的内部实践 + 用户实战案例。

| 文章 | 核心主题 |
|------|---------|
| [[Claude Code负责人-AI原生团队如何使用AI]] | Claude Code 团队工作流、Dogfooding、To-Do List 设计 |
| [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] | Anthropic 增长数据、Tokenmaxxing、AI 调 AI |
| [[Claude Code实战-结合Obsidian打造第二大脑]] | Home Server + Obsidian + Git + 手机 SSH |
| [[Claude Code实战-构建一个AI数据分析师]] | Claude Code 做数据分析：监控-调查-故事化-决策完整循环 |

---

## C. Codex & OpenClaw 实战（6 篇）

> OpenAI Codex 团队 + OpenClaw（开源 AI Agent）生态的实战。

| 文章 | 核心主题 |
|------|---------|
| [[Codex 自我改进 Prompt]] | OpenAI agent improvement loop，从 traces 到 Skill/Automation 的固化 |
| [[OpenAI官方-Codex新手教程]] | OpenAI Codex CLI 完整入门、AGENTS.md 体系、7 阶段研发集成 |
| [[Codex实战-构建全能AI营销团队]] | Codex 7 大 Skills、Grounding、YouTube 接地 |
| [[OpenClaw创始人-我是如何使用OpenClaw的]] | OpenClaw 起源、CLI Army、8 Sleep 控制、AI 自助解决语音 |
| [[30分钟精通OpenClaw]] | OpenClaw 安全设置、5 大真实用例、Memory 机制 |
| [[Taven创始人-将OpenClaw嵌入产品的实战经验]] | Ken Thompson 哲学、Excel Skill 案例、Agent 三要素 |
| [[OpenClaw实战-从本地到K8S部署]] | 容器化 4 大好处、ForeverClaw 设计、Sub-Agents |

---

## D. Agent 架构与原理（5 篇）

> Agent 本身的架构、记忆、上下文工程等基础理论。

| 文章 | 核心主题 |
|------|---------|
| [[Agent实战-打造一个AI Agent的完整教程]] | Agent 入门、Agent Loop (Observe-Think-Act)、Skills (.md) |
| [[OpenAI员工-上下文工程和Agent记忆]] | 3 大记忆模式（Reshape & Fit, Isolate & Route, Extract & Retrieve）|
| [[Manus创始人-深度干货-上下文工程的最佳实践]] | Context Engineering 范式、Context Offloading 策略 |
| [[Karpathy爆火项目-AutoResearch解读与启发]] | AutoResearch 4 步循环 + 6 大商业应用 |
| [[AI Agent 和 Skill 测评方案及落地实践 - martinskxu]] | Agent/Skill 测评四场景法、评分规则设计、基线管理、稳定性评估、TPerf 实战案例 |

---

## E. Cursor 与工具链（3 篇）

> Cursor 团队的内部故事 + AI 工具产品视角。

| 文章 | 核心主题 |
|------|---------|
| [[Cursor副总裁-构建软件开发过程的Agent]] | Cursor 团队如何构建 Agent 团队，覆盖完整 STLC |
| [[Cursor负责人-Composer模型如何训练的]] | Cursor 自研模型内幕、存储思维、模型"作弊"问题 |
| [[Alchemy CPO-从代码审查到自动代理]] | 3 大时刻：Slack 文档 → Code Review 回溯 → PR 协作 |

---

## F. AI Native 团队与工作流（3 篇）

> 团队组织形态的转型——从"人写代码"到"AI 协作"。

| 文章 | 核心主题 |
|------|---------|
| [[Claude Code负责人-AI原生团队如何使用AI]] | Dogfooding 实践、AI 优先的工作流 |
| [[5次创业者-AI智能体独自经营初创公司]] | R2 / ClotChef 系统、Agent = cron + md、创业哲学反转 |
| [[硅谷今年最火的岗位 FDE，我们闷头干了三年]] | FDE = 蜂群最小节点的中国实践，按结果收费 |

---

## G. AI 时代职业、方法论与组织（5 篇）

> 蜂群组织 / 个人 / 工程师面试 / 产品观 / 焦虑。

| 文章 | 核心主题 |
|------|---------|
| [[所谓的agent开发到底是个啥岗位]] | 生产力→生产关系→蜂群组织→蜂群最小节点要"业务+技术+AI 协作" |
| [[Agent 越用越翻车，怎么破局答案藏在经典管理学里]] | TRM、锚定效应、苏格拉底提问、过度设计、瓶颈思维 5 大心法 |
| [[AI 时代如何面试工程师]] | 从 Coder 到 Engineer，6 项核心能力 + 1 项元能力（好奇心）|
| [[80% 的 App 未来会消失吗我不这么认为]] | 产品价值在品味、复杂度封装、协同服务；竞争维度从"做出来"变"做得好" |
| [[万人大厂宣布裁员 40% 利润在涨人却多余了]] | 智能通缩、AI 替代螺旋、2025-2028 危机时间轴、UBI |

---

## H. AI 时代个人心得与洞察（2 篇）

> 个人使用 AI 的实战心法。

| 文章 | 核心主题 |
|------|---------|
| [[用AI的这三年，想跟你分享这9条心得]] | 花钱用最好的模型 / 每周自动化 / 实习生思维 / 品味护城河 / 把时间还给现实的人 |

---

## 关联 Areas / MOC

### 关联 Areas
- [[AI Agent Development]] — sanyuan 的系统课程（底层实现视角）
- [[Workflow and Skill Management]] — 个人工作流与 Skill 实践
- [[AI Tools and Products]] — 具体工具产品研究

### 关联 Resources
- [[MOC - Loock AI 全栈课程]] — Loock AI 的 LangGraph.js + Next.js + Coding Agent 全栈课程笔记（148 篇）
- [[MOC - Harness Engineering]] — Harness 主题横切 MOC（跨子主题）
- [[MOC - AI 时代个人发展与组织]] — 蜂群组织 / 职业 / 哲学 横切 MOC
- [[MOC - Prompt 工程]] — Prompt + Skills 横切 MOC

### 数据源
- **公众号**：15 篇（`02-Resources/AI and Agents/Agent Design & Patterns/`）
- **B 站视频**：19 篇（`02-Resources/AI and Agents/B站视频知识库/Agent架构与平台/`）
- **数据流水线**：Recastory 工具链（yt-dlp 替代 + ffmpeg + faster-whisper + LLM distill）

---

## 维护

- **总笔记数**：34（合并前 12 公众号 + 19 B站 + 3 微信公众号新收录）
- **最后更新**：2026-06-25（收录 遇事留痕 - Loop Engineering 的基础）
- **更新机制**：每收录 1 篇新笔记，**必须**更新本 MOC（按 §8 SOP 步骤 7）
- **孤立判定**：MOC 内的笔记被 `[[MOC - Agent Theory and Design]]` 链入 = 破孤（按 §7 "MOC 入口破孤"）
