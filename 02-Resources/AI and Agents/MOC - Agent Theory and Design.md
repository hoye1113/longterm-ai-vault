---
title: MOC - Agent Theory and Design
description: Agent 时代理论与实践的横切索引——覆盖 Harness、Claude Code、Codex、Cursor、OpenClaw、AI
  评估与研究、团队组织 等子主题，58 篇笔记
created: 2026-06-11
updated: 2026-07-03
tags:
  - ai_agent
  - ai_philosophy
  - moc
  - article
source: vault_initiative - moc - ai_agent - harness_engineering - claude_code -
  codex - cursor
---

# MOC - Agent Theory and Design

> 主题 MOC（合并自原 `MOC - AI Agent 参考资料` + `MOC - B站视频知识库`），覆盖 `02-Resources/AI and Agents/` 下所有"Agent 理论 + 实践"类笔记。共 **58 篇**笔记，按 11 个子主题分组。
>
> **本 MOC 是 v1（圆桌共识落地）**，建立 3 个横切 MOC 后，这里只承担"主题 MOC"角色——跨子目录的横切链接见：
> - [[MOC - Harness Engineering]]（横切，跨课程/公众号/B站）
> - [[MOC - AI 时代个人发展与组织]]（横切，FDE/职业/哲学）
> - [[MOC - Prompt 工程]]（横切，Prompts + Skills）

---

## A. Harness Engineering（18 篇）

> 围绕"harness = 围绕 Agent 的工程系统"这一概念展开。**Anthropic（Claude Code）** 与 **OpenAI（Codex）** 两大权威来源 + IBM 团队的登山绳比喻 + DeepMind「模型吞噬 harness」+ Loop 正反辩 + 花叔/卡颂 Loop Engineering + Anthropic 官方汇编本。

| 文章 | 核心主题 |
|------|---------|
| [[祝贺Claude Code成功越狱，获得永生]] | 花叔逆向 Claude Code 泄露的 1902 源文件，harness 内部由 system prompt / 四层权限 / 记忆 / 9 段式压缩 / swarm / grep 构成 |
| [[2026 年 Agent 最重要的工程概念 Harness Engineering]] | OpenAI 5 个月 0 人工代码 100 万行实验；harness = docs/ 当 source of truth + linter 强制不变量 + 黄金原则 |
| [[IBM团队-Harness工程详解]] | 现场 demo：guardrails→verify→login handler；不改 prompt 让 GPT-3.5 级模型完成任务 |
| [[DeepMind-模型将吞噬Harness]] | Logan Kilpatrick：Antigravity 主线、模型从权重到 system、harness alpha 6 个月内 upstream |
| [[Loop-Agent Loop到底是什么]] | Ross Mikita：HITL vs Agent Loop；开放式 loop 是 token 焚烧；code review 评分闭环才合理 |
| [[别再搭 Harness 了，先把你的痛点解决，用最笨的方式]] | 马斯克五步法在 Agent 工作流上的应用；先痛点后系统 |
| [[Loop Engineering 橙皮书 - 花叔]] | 五动作循环 + 六零件 + 四笔代价；Loop = Harness 上一层 |
| [[Harness 实践 - 将任何文字编辑成精美的文章 - ConardLi]] | 用同一套骨架（8 Phase + 3 Checkpoint + Reacticle）将任意文字编辑成精美网页文章，验证 Harness 可迁移 |
| [[遇事留痕 - Loop Engineering 的基础 - 魔术师卡颂]] | Session Log + GitHub issue/PR 是项目自我优化的燃料，自动优化循环的基础 |
| [[驾驭 AI - 把不确定问题转化为可控实验 - 魔术师卡颂]] | Vibe Coding 报点式协作；不确定问题 → 客观标准 + 反馈闭环，用 token 换精力 |
| [[想锻炼 AI 能力 - AI Native CLI - 魔术师卡颂]] | 传统 CLI → AI Native：结构化 stdout、可恢复错误、分级权限、内置 Skill |
| [[AI Coding 时间管理 - 50% 工作法 - 魔术师卡颂]] | 50% 业务 / 50% Harness；减并行、拉长 Agent 自治、防摸鱼退化 |
| [[如何为项目定制 Harness 环境 - 魔术师卡颂]] | 减框架增基建；superpowers/gstack 入门 → 重基建轻编排 |
| [[AI框架与 Harness 的关系 - 魔术师卡颂]] | Harness 三层（约束/路由/编排）；superpowers、gstack 在顶层 |
| [[AI 主导的项目和人主导的区别 - 魔术师卡颂]] | monorepo + 统一 CLI；各端差异收敛到工具层 |
| [[如何让 Skill 自动优化 - 魔术师卡颂]] | PR 反馈 → 规则集自优化；warp common-skills 三条件 |
| [[未来的 AI 编程就是 Loop 套 Loop - 魔术师卡颂]] | 三层 Loop 嵌套；信息压缩：代码→门禁→规则质量 |
| [[Anthropic Agent 工程实战指南 - 从入门到生产落地]] | 1758 行 Anthropic 官方 15 篇博客汇编，按"入门-进阶-核心-高级-生产"5 模块系统化梳理 |

---

## B. Claude Code 实战（7 篇）

> Anthropic Claude Code 团队的内部实践 + 用户实战案例。

| 文章 | 核心主题 |
|------|---------|
| [[Claude Code负责人-AI原生团队如何使用AI]] | Boris 20% side project→千人流传；Todo/Plan 从痛点长出；Eval 分 E2E 与 triggering |
| [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] | 指数增长、Tokenmaxxing、Auto 模式路由、rate limit 与 switching cost 变薄 |
| [[Claude Code之父-编程已被解决接下来发展]] | Lauren × Boris：编码 100% 代理化、闪电循环/例程、7 Powers、印刷术类比、组织流程 moat |
| [[Cowork负责人-揭秘Cowork与Mythos]] | Felix：Mythos 阶跃、Cowork 十天+VM、技能/记忆 Markdown、本地信任、执行免费与品味 |
| [[Claude设计主管-Cowork揭秘40分钟教程]] | Jenny Wen：松散设计流程、可工作原型、内部 dogfooding、Cowork 洞察自动化、3–6 月愿景原型 |
| [[Claude Code实战-结合Obsidian打造第二大脑]] | Obsidian+Git+Tailscale；thinking 模式、Interviewer 子 agent；AI 读强于写 |
| [[Claude Code实战-构建一个AI数据分析师]] | Brex：监控-调查-故事-决策四循环 + Snowflake MCP + token 护栏 |
| [[Claude Code实战-Gstack把AI变成团队]] | Garry Tan：GStack 轻薄脚手架；Office Hours 六问、对抗性审查、设计散弹枪、Playwright QA、并行 PR |

---

## C. Codex & OpenClaw 实战（9 篇）

> OpenAI Codex 团队 + OpenClaw（开源 AI Agent）生态的实战。

| 文章 | 核心主题 |
|------|---------|
| [[Codex 自我改进 Prompt]] | OpenAI agent improvement loop，从 traces 到 Skill/Automation 的固化 |
| [[OpenAI官方-Codex新手教程]] | AGENTS.md、config.toml 沙箱、MCP、Codex Exec + Agents SDK 编排 |
| [[Codex负责人-现场演示Codex]] | Codex 负责人 live demo（**canonical v3.2** ✓） |
| [[Codex产品负责人-Codex团队如何用Codex]] | Alex × Romain：Spark demo、十要点规范、八周规划、PM 补位与能动性招聘（**canonical v3.2** ✓） |
| [[Codex 负责人-所有人都是 builder 是个很糟糕的主意 - Founder Park]] | Lenny 对谈 Ambrosino：taste 最贵、PM 不消失、晚发 3 月会死、会删代码 |
| [[Codex实战-构建全能AI营销团队]] | Riley：7 Skills 营销全流程 + YouTube/Readwise 接地 + Gen Media |
| [[OpenClaw创始人-我是如何使用OpenClaw的]] | WhatsApp→Claude Code；CLI Army；Just talk to it，别沉迷 24h loop |
| [[30分钟精通OpenClaw]] | 安全五步、五用例 demo、SOUL/USER/MEMORY 本地 MD 人格 |
| [[Taven创始人-将OpenClaw嵌入产品的实战经验]] | Pi 内核企业嵌入：Excel Skill 小 CLI、一客户一 Agent + AGENTS.md |
| [[OpenClaw实战-从本地到K8S部署]] | Podman/K8s 四好处、Secret ref 双层、baseline 镜像愿景 |

---

## D. Agent 架构与原理（10 篇）

> Agent 本身的架构、记忆、上下文工程、multi-agent 与企业生产实践。

| 文章 | 核心主题 |
|------|---------|
| [[Agent实战-打造一个AI Agent的完整教程]] | ~59min 入门：Observe-Think-Act、harness、agents.md、MCP、Skills 现场搭 EA |
| [[DeepMind团队-当数百万Agent相遇]] | DeepMind 科学家：Agent vs LLM、delegation、multi-agent 经济与安全 |
| [[Databricks-企业级Agent生产实践]] | 五支柱 playbook：eval→observability→data→orchestration→governance |
| [[PlanetScale-Agent时代的基础设施]] | Agent 优化 DB、schema rewind、small sharp tools、分片策略 |
| [[Geoff-Ralph Loops的基础设施]] | Geoffrey Huntley Loom 直播：agent-first 栈、Thread/Weaver、NixOS 十秒部署、Ralph SUT 验系统 |
| [[OpenAI员工-上下文工程和Agent记忆]] | 三大记忆模式 + IT demo：burst/trim/compact/summarize |
| [[Manus创始人-深度干货-上下文工程的最佳实践]] | compaction vs summarize、三层 action space、avoid over-engineering |
| [[Karpathy爆火项目-AutoResearch解读与启发]] | 自主实验 loop + 9 类商业用例 + Agent Hub 展望 |
| [[AI Agent 和 Skill 测评方案及落地实践 - martinskxu]] | Agent/Skill 测评四场景法、评分规则设计、基线管理、稳定性评估、TPerf 实战案例 |

---

## E. Cursor 与工具链（5 篇）

> Cursor 团队的内部故事 + 多 Agent 协作 + AI 工具产品视角。

| 文章 | 核心主题 |
|------|---------|
| [[Cursor副总裁-构建软件开发过程的Agent]] | STLC 全链 Agent 团队：98% AI merge 但 40% plateau；Skills 原子单元 |
| [[Cursor-128个Agent团队协作]] | 208 Agent 并行、脚本互通信、Judge 校验、Claude 写/GPT 审 |
| [[Cursor负责人-Composer模型如何训练的]] | Kimi 2.5→mid-training→Cursor harness RL；async 全球集群 + sim/online RL |
| [[Alchemy CPO-从代码审查到自动代理]] | 三转折点：Slack 文档→事故 retro review→PR 协作；Linear+Skills 离线干活 |
| [[smart-draw 手绘风可编辑 AI 图表 - 极客公园]] | 自然语言→Excalidraw 手绘风可编辑图；补 AI 生图不可改与 Mermaid 工业味缺口 |

---

## F. AI Native 团队与工作流（6 篇）

> 团队组织形态的转型——从"人写代码"到"AI 协作"。

| 文章 | 核心主题 |
|------|---------|
| [[Claude Code负责人-AI原生团队如何使用AI]] | Dogfooding 实践、AI 优先的工作流 |
| [[LCA-60分钟变成AI-Native]] | People + Agents + Context 三层、Skill Chain、Brain 闭环 |
| [[WorkOS-创建和使用Skills方法论]] | Skills at scale：DRY 进 agentic era、MCP 安全、可移植工作单元 |
| [[5次创业者-AI智能体独自经营初创公司]] | R2/ClawChief 幕僚长 + Devin playbook；先建 SDLC 再放量 |
| [[硅谷今年最火的岗位 FDE，我们闷头干了三年]] | FDE = 蜂群最小节点的中国实践，按结果收费 |
| [[AI 主导的项目和人主导的区别 - 魔术师卡颂]] | monorepo + 统一 CLI 流程；各端差异收敛到工具层 |

---

## G. AI 时代职业、方法论与组织（8 篇）

> 蜂群组织 / 个人 / 工程师面试 / 产品观 / 行业判断。

| 文章 | 核心主题 |
|------|---------|
| [[Codex 负责人-所有人都是 builder 是个很糟糕的主意 - Founder Park]] | 实现廉价后 taste/策展最贵；反对取消 PM；zone defense 协作 |
| [[a16z-AI并非泡沫]] | 供给约束非泡沫、token path、native vs skeuomorphic 产品 |
| [[微软CEO-AI竞争终局与企业私有评估]] | 纳德拉：私有评估=企业 IP、线束、Work IQ、元工作、社会许可 |
| [[所谓的agent开发到底是个啥岗位]] | 生产力→生产关系→蜂群组织→蜂群最小节点要"业务+技术+AI 协作" |
| [[Agent 越用越翻车，怎么破局答案藏在经典管理学里]] | TRM、锚定效应、苏格拉底提问、过度设计、瓶颈思维 5 大心法 |
| [[AI 时代如何面试工程师]] | 从 Coder 到 Engineer，6 项核心能力 + 1 项元能力（好奇心）|
| [[80% 的 App 未来会消失吗我不这么认为]] | 产品价值在品味、复杂度封装、协同服务；竞争维度从"做出来"变"做得好" |
| [[万人大厂宣布裁员 40% 利润在涨人却多余了]] | 智能通缩、AI 替代螺旋、2025-2028 危机时间轴、UBI |

---

## J. AI 评估与研究（6 篇）

> 前沿 eval、benchmark 饱和、LLM-as-judge 校准、RL 小模型、论文俱乐部。

| 文章 | 核心主题 |
|------|---------|
| [[OpenAI评估团队-不再低估模型]] | Frontier eval、benchmark 饱和、bench gaming、SWE-bench Verified→真实工作 task |
| [[微软CEO-AI竞争终局与企业私有评估]] | 私有评估集=护城河；模型切换试金石；公开榜饱和后的企业 eval |
| [[Agenta CEO-构建真正有效的AI评估]] | LLM-as-judge 校准、GEPA 提示词优化、业务 error analysis、二元评判、TauBench |
| [[DeepMind团队-AI评估规划化与民主化]] | Kaggle 评估民主化、SAE 智能体考试、Game Arena PvP、工具/模型混淆 |
| [[Snorkel-小模型RL超越大模型]] | 4B + GRPO beat 235B；tool discipline > reasoning；rubrics 定位 behavior gap |
| [[YC论文俱乐部-5篇论文揭示AI研究趋势]] | Bio scaling、Self-play RL、Stream RAG、Lean 验证、RTS 式 agentic coding |

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
- **公众号**：**28** 篇（`02-Resources/AI and Agents/Agent Design & Patterns/`）
- **B 站视频**：47 篇 · S **30** + A **12** dialogue-asr + A **5** lecture
  - **收录入口**（2026-07-06）：`99-System/Skills/vskill-vault-curate/SUBDOC - ASR内容分轨与收录决策.md` · 细节 `SUBDOC - B站视频 v3 工作流.md`
  - 单篇 canonical **47/47**（P0 +15，2026-07-06）；`- 对谈稿.md` **0**
  - A 级划章明细 `99-System/audit/bilibili-a-tier-v3-rewrite-2026-07-03.md` · rollout `bilibili-v3-rollout-2026-07-03.md`
- **数据流水线**：Recastory（`ingest/` 简介+专栏 + ASR → vault）；kimi `.desc-info-text` → `video_description.md`

---

## 维护

- **总笔记数**：**57**（B 站 32 + 公众号等；2026-07-03 新增魔术师卡颂 8 篇 + Founder Park/极客公园 2 篇）
- **Inbox**：已清空（wechat 快照 → `99-System/Attachments/wechat-snapshots/`）
- **最后更新**：2026-07-06（ASR 无专栏 SOP 文档闭环）
- **更新机制**：每收录 1 篇新笔记，**必须**更新本 MOC（按 §8 SOP 步骤 7）
- **孤立判定**：MOC 内的笔记被 `[[MOC - Agent Theory and Design]]` 链入 = 破孤（按 §7 "MOC 入口破孤"）
