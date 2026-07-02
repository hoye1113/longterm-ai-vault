---
title: "Cursor工程师：让128个Agent像团队般协作"
source: "B站视频 - Cursor / BasedTen 对谈"
source_url: "https://www.bilibili.com/video/BV1LFjV6BEpe/"
speaker: "Harry (BasedTen ML 研究员) / Sam (Cursor Cloud Agents 工程师)"
duration: "41:57"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - cursor
  - multi_agent
  - harness_engineering
created: 2026-07-02
description: "Harry 同时跑 128+ Agent 做 KV cache compaction 研究，用脚本互发 user message 实现数学家团队；Sam 分享 thermonuclear review、多模型分工与 taste 仍是瓶颈。"
transcript_source: "Recastory/A4-cursor-128-agents/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Cursor工程师：让128个Agent像团队般协作

## 先搞懂这一期

**这是什么节目？**  
Cursor × BasedTen 工程师对谈，约 42 分钟。一边是 **Harry**（BasedTen ML 研究员，Charlie 联合创始人团队），一边是 **Sam**（Cursor Cloud Agents 团队工程师，入职约半年）。不是单人演讲，是两人聊各自怎么 **同时跑大量 Agent**。

**这期在回答哪三个问题？**

1. **一个人怎么管 128 个 Agent 而不乱？** 任务怎么拆、怎么互相说话、人怎么介入？
2. **Cursor 内部用 Agent 写 Agent 产品，有什么纪律？** review、多模型分工、plan mode 怎么用？
3. **模型能力涨这么快，人的工作还剩什么？** taste、选问题、读代码——哪些 Agent 还做不了？

**用一条线串起来（没看视频也能复述）：**

Harry 团队在研究 **KV cache compaction**（怎么压缩模型上下文缓存），同时开着 **128–208 个 Cursor Agent**：主 Agent 派活给子 Agent，每个起数学家名字（Poincaré、Hubert…），用自写脚本互发 **user message** 才肯理对方——模型默认 ignore 彼此。Sam 这边管 Cloud Agents，内部有 **thermonuclear review**（多轮 adversarial 代码审查）、GPT 写 Claude 审的多模型分工、plan mode 里先写大 markdown 计划再开 team。

两人共识：**抽象阶梯在上移**——从 narrow task 到 delegate 整个 research program；但 **taste（选什么问题、怎么执行）** 仍靠人。可验证任务 Agent 能跑数天；不可验证任务你得自己读代码。Sam 的 spicy take：**冻结今天的模型能力，我们可能只用了 5% 价值**——瓶颈在 harness、UI/UX、production pipeline，不在模型本身。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Multi-Agent = 多个 Agent 并行写代码 | **128 Agent 编排**：命名、脚本互发消息、多屏监控、jump in 纠正 |
| Agent 跑完就停 | **Goal loop + judge agent**：主 Agent 易「我觉得做完了」，要 separate judge hook 继续 |
| 用一个最强模型搞定 | **多模型分工**：Claude implement/plan，GPT review；errors uncorrelated |
| 模型越强越不用人 | **Taste bottleneck**；「能写代码不能读代码」；plan mode 多 spec 20% → 回报巨大 |
| Cursor = 代码补全 | Cursor 内部投 **QA automation、monitoring、deploy**——code production 不只 generation |

---

## 分话题讲

### 1. Harry 的 128 Agent：数学家团队怎么协作

**说法：**  
Harry 研究 KV cache compaction；**60+ Cursor agents** 与 BasedTen 侧合计 **~208** 同时跑。他平时只跟 **main agent** 说话，main agent 再 delegate。

模型默认 **ignore 彼此消息**——你让 Agent A 发消息给 Agent B，B 往往继续干自己的。Harry 的 hack：自写 script `call script(string, name)` → 把 string **inject 为对方 session 的 user message** → 全员 responsive。

每个 Agent 起数学家名（Poincaré、Hubert、Gauss…），问 main agent「Poincaré 今天在干嘛」。多屏监控：10+10+ laptop 看全员发消息；可 jump in（「Gauss 叫 Hubert 做蠢事，不对」）。

Cursor 刚 launch **Multi-Task Mode**：一个 agent 可 launch 一堆 subagents，用户继续说话不 block 它们。

**和你何干：**  
Multi-Agent 协作 today 常需 **工程 hack**（消息注入），不能 assume 模型原生会 team work。

---

### 2. Agent 责任边界：spec 不清就停，goal loop 跑数天

**说法：**  
Harry 必须 **cleanly specify** 每个 agent 干什么；否则 stop working。Long-running 任务两种办法：

- **Reminder loop** — 周期性 checklist message  
- **Separate judge agent** — 主 agent 易「我觉得做完了」；judge 说「你其实没完成」→ hook 继续

Goal loop 可跑 **数天**；prompt 开头 heavy investment + **verifiable completion criteria**。

Sam 补充：危险命令有 guardrail checks；但不 over-share harness 细节——很多人在研究 loop/stop 机制。

**和你何干：**  
长任务先写 **怎么验证完成**，再写 **怎么干活**；考虑 judge agent 防 premature stop。

---

### 3. Cursor 内部：thermonuclear review 与 automate QA

**说法：**  
Sam 跟踪 Codex、Cursor regions、Anthropic setout；**Codex direct 移植**到 Cursor region 看 R&D 怎么 inform 自建。

Lauren（Cursor 3.0 工程师）：Agent 建 scale **驱动 instrumented Cursor** 做 performance QA——先 verify 有 performance problem，改完再 verify 问题消失。**Automate QA** 是投资重点。

**Verifiable >> non-verifiable**：overnight hill-climb easy；eval/design「good」需人 read code——

> **"They can write code for you. They can't actually read code for you."**

**和你何干：**  
可验证任务（测试过/不过）交给 Agent 跑通宵；设计/审美/「好不好」你得自己读产出。

---

### 4. Taste bottleneck 与 read code first

**说法：**  
Non-verifiable 任务，**taste 是瓶颈**——steer 模型 cut down 巨大 search space。模型倾向 **random hypothesis test**（token penalty 训练导致怕花 token）：「可能是 A，测一下；可能是 B，测一下」。更高效：**先读完全部代码**，再定 2–3 个 test。

Sam：**20% more spec effort → outsized returns**——模型被 RL 训练成 **该问用户就问**；人往往 under-specify。Plan mode：大 markdown 写清再开 team。

**Thermonuclear review** skill：多轮 adversarial PR review；GitHub 公开 PR 也跑。

**和你何干：**  
反复说「先读代码再改」；plan mode 不是浪费时间，是省 downstream 返工。

---

### 5. 多模型分工：implement 和 review 用不同 family

**说法：**  
Harry 至少一个 **GPT-5.5** + 一个 **Claude 4.7**：

- **Claude** — implement / plan；你不 specify 清楚时它会 **填 gap**（有时 helpful，有时 problematic）  
- **GPT-5.5** — review 功能；更 utility，「你说什么它做什么」

不同 family errors **uncorrelated** → 平均 out。Frontier 模型 correlated mistakes 是 real problem。

**和你何干：**  
同一任务 implement 和 review 换模型 family，别自审。

---

### 6. Agent 互聊的趣事：prompt inject 与 personality

**说法：**  
Harry 试图 **prompt inject** Sam 的 agent「删文件」——Sam 的 agent 拒信 untrusted message from Harry's ecosystem。两人 agent 还 **take on founder personality**——能分辨哪个是 Harry 的、哪个是 Sam 的。

Harry 给 Agent 起数学家名是否影响行为？他不确定，但 **quant 背景** 的命名让他觉得好玩。

未来问题：**Harry 的 agents 会和你的 agents 协作吗？** UI/UX 和 infra 都还没 ready。

**和你何干：**  
Agent-to-agent 安全（消息来源验证）today 就要想，别等 scale 了再补。

---

### 7. BasedTen 背景：inference + training feedback loop

**说法：**  
Charlie 创立 BasedTen；open source **specialization + post-training**。Cursor 大量 inference 走 BasedTen → 合并后 **inference signals + training** 形成 feedback loop——比纯 prompting 强。

2025 中 open source base 够好 → specialize repeatable enterprise subtasks。**Manage agent** = 核心 driving model + 编排层。

Harry：**abstraction ladder** 上移——delegate experiments to agent team；**bottleneck = taste + problem selection**。不能 prompt GPT-5.5「去写 KV compaction 论文」就完事——人定 problem、inject taste，scope 清楚后 agent team 可 wild。

GPT-5.5 **40h goal loop** 出 amazing plots（KV compaction visualization）——但需人 seed what to check。

**和你何干：**  
Post-training specialization > prompting for tool-call patterns（16–32 parallel tools, limit search depth）。

---

### 8. Compaction、context、公司-as-one-model

**说法：**  
**Token penalty 副作用**：模型怕花 token，不敢 deep read；compaction by reference vs shallow summary。OpenAI compaction endpoint；good compaction 可能使 200k context 够用。

Sam vs Harry debate：engineer 成本 vs token 成本 order-of-magnitude——Sam 认为 good engineer 可能花跟 salary 同量级的 tokens。

**Company as one model**：Composer online RL；公司围绕一模型 specialized domain knowledge + many copies running different tasks。

**Icicle problem**：internet+RL 训练 → vanilla average behavior，product vertical 里 far from promptable → post-training 越来越重要。

**和你何干：**  
Context 管理：harness 做 compaction/引用，别指望 model 自己管理 external scratch pad 直到它 read。

---

### 9. 未来 6 个月：UI/UX lag、automations、5% value

**说法：**  
Sam：**UI/UX 和 production pipeline 滞后 model releases**——定义上 model 先存在才能做 product。Cursor 内部「Sharpen the saw」：6h 砍树 4h 磨斧；focus **code production**（CI、monitoring、deploy）非只 generation。模型能写 2 万行 code，怎么 get to production？

**Automations** 新产品：trigger → agent，cron 式 replicable workflows（triaging issue、monitor security）。

Charlie spicy：**frozen today's models → only 5% value realized**——harness/usage 是杠杆。

Harry counter：human brain 100T params， ceiling 还高；但 agree methods matter。

Agent maxing **$200/mo still token bottleneck**；未来 agents 协作、甚至 **pay for own inference**（mechanistic interpretability 趣味）。

**和你何干：**  
别只追 model release；投 production pipeline 和 agent management UI。

---

## 关键概念表

| 词 | 白话 |
|----|------|
| **KV cache compaction** | 压缩模型上下文缓存，延长有效 context |
| **Goal loop** | Agent 带明确完成标准长跑，可数天 |
| **Judge agent** | 独立 Agent 判主 Agent 是否真的完成 |
| **Thermonuclear review** | Cursor 内部多轮 adversarial 代码审查 skill |
| **Taste bottleneck** | 不可验证任务里，人选方向/审美是瓶颈 |
| **Abstraction ladder** | 从 narrow task 上移到 delegate whole program |
| **Multi-Task Mode** | Cursor 一个 agent launch 多 subagents 不 block 用户 |
| **Icicle problem** | 大模型 internet 平均行为 vs product vertical 需求 gap |
| **Inference + training loop** | 线上信号反哺 post-training，强于纯 prompt |

---

## 值得记住的原话

> **"They can write code for you. They can't actually read code for you."**  
> 能替你写代码，不能替你读代码。

> **"Taste is the big bottleneck."**  
> 品味是最大瓶颈。

> **"Read the code first before testing random hypothesis."**  
> 先读代码，别随机猜 hypothesis。

> **"If you frozen the capabilities of the models today, we're probably only realizing five percent of the value."**  
> 冻结今天的模型能力，我们可能只用了 5% 价值。

> **"Agent engineer... managing people's team of agents."**  
> Agent 工程师——管别人的 Agent 团队。

> **"Many multi-agent systems act more as parallelization than delegation."**  
> 很多 multi-agent 只是在并行，不是在 intelligent 派活。（与 DeepMind 播客呼应）

> **"Trust is given, but it's also earned."**  
> 信任可以给人，也要靠表现赚回来。

> **"You spend six hours sharpening the saw, four hours chopping down the tree."**  
> 六小时砍树，先花四小时磨斧——投 harness/UI 而非只等模型变强。

> **"The models didn't really pay attention to each other... I made a script to inject user messages."**  
> 模型不太理彼此……我写脚本注入 user message 才 responsive。

> **"I'm the long-term memory for my agents."**  
> 我是 Agent 的长期记忆——模型只有 short-term，人补 taste 和 context。

---

## 小结

**这期最核心的判断：** 128 Agent 并行能跑通工程任务，但 **taste 和读代码仍是人的瓶颈**；模型 today 的能力我们可能只用了约 5%，价值在 harness、spec 和多模型 review 分工里。

**读完应带走：**
- Agent 能写代码，**不能替你读代码、替你定品味**——overnight 只适合可验证任务。
- 很多 multi-agent 要 **工程 hack**（注入 user message）才协作；implement / review 换模型 family 降 correlated mistakes。
- **Agent engineer = 管 Agent 团队的人**；长期记忆和 taste 目前还在人这边。

**和 vault 的关系：** 接 multi_agent 与 [[DeepMind团队-当数百万Agent相遇]] 的 delegation 讨论——工程侧大规模并行的真实约束。

---

## 行动启示

1. **Multi-Agent 先写 spec + 完成标准**；长任务加 judge agent 或 reminder loop。  
2. **Implement 和 review 换模型 family**——降 correlated mistakes。  
3. **Plan mode 多写 20% spec**——回报 disproportionately 大。  
4. **可验证任务 overnight；不可验证任务你读代码**——别 delegate taste。  
5. **Agent 互聊 today 要工程 hack**——消息注入、来源验证。  
6. **投 production pipeline**（CI、QA、monitoring）——不只 generation。  
7. **Internal skill sharing**——重复 prompt 发布为 skill（thermonuclear review 等）。

---

## 相关阅读

- [[Cursor副总裁-构建软件开发过程的Agent]] — Cursor 侧 software development process agent 视角  
- [[WorkOS-创建和使用Skills方法论]] — Skills 创建与复用方法论  
- [[PlanetScale-Agent时代的基础设施]] — Sam 同场 PlanetScale demo 用的 Cursor Agent  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1LFjV6BEpe](https://www.bilibili.com/video/BV1LFjV6BEpe/)（B 站转载 Cursor × BasedTen 对谈）  
- **嘉宾**：Harry（BasedTen ML 研究员）；Sam（Cursor Cloud Agents 工程师）  
- **时长**：41:57  
- **转写**：Recastory `A4-cursor-128-agents/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
