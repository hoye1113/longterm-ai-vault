---
title: "YC 论文俱乐部：5 篇论文揭示 AI 研究趋势"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV14AjN6oEcg/"
uploader: "Easonlee的AI笔记"
saved: 2026-07-02
tags:
  - ai_agent
  - ai_evaluation
  - video_transcript
  - bilibili
  - harness_engineering
  - multi_agent
created: 2026-07-02
description: "YC Paper Club 五讲：ESM3 蛋白质 scaling、LLM self-play RL、Stream RAG 语音 Agent、Lean 形式化验证、Channel AI RTS 式 agentic 编程；Host 论 memory、f−h、intelligence per sample。"
transcript_source: "Recastory/workspace/knowledge/B4-yc-paper-club/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# YC 论文俱乐部：5 篇论文揭示 AI 研究趋势

## 先搞懂这一期

**这是什么节目？**  
YC **Paper Club** 线下分享，主持人 **Friends** 串讲 **5 篇论文 + 1 场工程实践**。偏 applied，不是纯理论沙龙——每条线都能单独跟进。

**这期在回答哪三个问题？**

1. **Scaling 还在哪些模态成立？** 蛋白质、RL task、token、形式证明——Bitter Lesson 是否继续赢？
2. **Scaling 的坑在哪？** junk task、ICL 非单调、语音 latency、human-data ceiling——哪里会 plateau？
3. **做 research / 做 product 的人各该带走什么？** bio-AI 窗口、self-play reward 设计、Stream RAG framing、Lean 验证、RTS 式 agent 编排。

**用一条线串起来（没看视频也能复述）：**

Friends 开场先泼冷水：memory 热了一年半；**f−h**（human demonstration 训练的天花板）他强烈怀疑 Noam Brown 的乐观路线——更押 **Office-Zero** 式无人类偏置；**intelligence per sample** 上 ICL 非单调、撞 context cliff，不像人脑学象棋那样单调变好。

五讲各自占一块：

- **ESM3**：蛋白质 masked LM 的 scaling laws 与 NLP 同型，28 亿 metagenomic 序列破 ESM2 data wall；单序列无 MSA 逼近 AlphaFold3，抗体设计已 win——Bitter Lesson 在 biology **大体成立**。
- **Self-Play RL**：Conjecturer 出题 + Solver 解题；vanilla reward 学成 **junk 题**；self-guidance 用 7B 8× compute 换约 2× 67B pass@，仍 plateau。
- **Stream RAG**：语音 Agent 不能等说完再 retrieve；partial speech **何时够**触发 RAG——latency −0.5~1.5s，accuracy 持平。
- **Lean**：verified intelligence 时代——数学、代码、科学从「能写」到「能证」；与论文 5 的 token maxxing 形成对照。
- **Channel AI**：agentic 编程 = **RTS** 非 chess——worktree 并行、KB 驱动、macro 优先；RPS/engineer 3.5× 后再 +60% MoM。

共同主题：**scale** 与 **verification**（结构 proxy、Lean、retrieval gate、形式证明、PR 人审）如何在不同模态落地。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 听过 Bitter Lesson / scaling laws | **蛋白质**上同样 log-linear；data wall 靠 metagenomics 破 |
| 听过 RLHF / post-training | **Self-play** 自动生成 task——但 junk reward 是真实陷阱 |
| 做过 RAG 聊天 | **Voice** 要等说完才 RAG → 对话不像人；streaming 触发时机是 framing 问题 |
| 用过 Cursor / Claude Code | **RTS 式**并行 orchestration vs 单人 chess 深度线 |
| 关心 eval / 对齐 | **Lean** 验证链 + OpenAI eval 湿实验——「如何证模型真进步」多模态对照 |

---

## 分话题讲

### 开场：Friends 的研究议程

Friends 在论文前定调 club 品味，并征集 future presentation。

**Memory** 仍是 1.5 年 hot topic：Mem0、recursive LM、Carta、AgentNet、dynamic chunking 等并行——欢迎 memory 主题上台；自己刚与 Noam Brown 在 podcast 讨论 human-data ceiling。

**f−h 与 Office-Zero**：Noam 仍信 human 解空间 + test-time compute + recursive self-improve 能推到接近 AGI；Friends **强烈怀疑**——若 full solution 基于 **f-training on human solutions**，无论多少 test-time compute，都会被锁在人类解的典型集合。图上 **左侧 AlphaGo**（有人类棋谱偏置）vs **右侧 Office-Zero**（无人类示范 mandering）——他押后者。

**Intelligence per sample**：人类每获新样本会 continuous learning；业界主流 **ICL** 却 **非单调**——样例增多先升后 bob/weave，最终撞 **context length cliff**。LoRA 低 rank 小样本 impressively well，但也快速 plateau；路径上最优策略应随样本流变化，而我们叙事像单调改进。象棋、围棋、一万小时音乐对人脑单调变好——LLM 曲线形态不同。

**Club 运营**：征集 bio-AI、memory、共建 benchmark challenge、open source hack；下期约两周后已满，7 月第一场仍招人。

---

### 论文 1：Bitter Lesson through Biology（ESM3）

#### 先搞懂这一篇

**这一篇在回答什么问题？**  
Richard Sutton 的 **Bitter Lesson**——general methods + scale compute/data 终胜 hand-crafted domain knowledge——**在蛋白质/生物学上成立吗？**

**用一条线串起来：**  
蛋白质 = 20 种氨基酸字母串，像 NLP 的 token；在进化序列库上做 masked LM，**从不告诉模型结构先验**。ESM3 用 3M→600M→6B 参数，无监督指标 **P@L**（远程结构接触精度）呈 **log-linear scaling**，低算力曲线外推高算力 run 干净吻合。ESM2 在 ~5000 万序列 **plateau**；ESM3 扩到 **28 亿** metagenomic 序列（土壤、海洋、肠道未培养物种）→ 曲线继续爬——进化已「训」40 亿年，人类只采样 <1% 多样性。

vs **AlphaFold 的 MSA**（手工多序列比对）：general protein 单序列距 AlphaFold3 约 3 分；**抗体设计**单序列 **50 vs 47 已 win**——MSA 不是死了，是 **只在 data abundant 时仍有用**。副产品：7B 模型折叠 >10 亿结构 → SAE 空间排成 **protein Google Maps**；inverse design 设计 PDL-1 binder 等蛋白药，湿实验验证。

**讲者**：Yash Big（bio-AI，Stanford / Biohub 圈）

#### 本篇小结

Bitter Lesson 在蛋白质上 **大体成立**：scale data + compute 的 masked LM 可破 ESM2 plateau；MSA 只在 data abundant 时仍有用，抗体设计已可单序列 win。

---

### 论文 2：Scaling Self-Play with Self-Guidance

#### 先搞懂这一篇

**这一篇在回答什么问题？**  
LLM post-training 的 RL task 靠手工收集，log scale 不可持续——**self-play 能否让模型自己生成 frontier tasks 并持续变强？**

**用一条线串起来：**  
当前栈：pretrain → 越来越长的 **RL runs**（coding/math tasks，post-train compute 已逼近 pretrain）。**Asymmetric self-play**：**Conjecturer** 生成完整 task（如 Lean 数学题 + unit tests）；**Solver** 解题；同模型两角色。理论诱惑：演示有天花板；固定环境 RL 会满分或零 reward；self-play 应 **无限生成 frontier tasks**——围棋已超越人类仍继续涨。

**Vanilla 失败**：Conjecturer reward = Solver **做错 1、做对 0** → 最优策略是 **junk complex 题**（Lean 里冗长恶心 statement）。训练曲线：Conjecturer 越来越强，**Solver 与 baseline RL 一样**——task 分布无用。

**Self-Guidance 修复**：从 3000 道 Lean unsolved 题 ground synthetic；reward = trickiness × **guide score**（LLM judge 相关且非过度复杂）。结果：7B + **8×** compute → pass@ 约 **2× 67B**；仍 **plateau**，远非 100%。

**讲者**：Luke（Tatsuoka lab，adversarial robustness → post-training self-play）

#### 本篇小结

Self-play 理论诱人，但 naive reward 学成 **junk task**；Self-Guidance + LLM judge 可让小模型用 compute 换 pass@，但仍会 **plateau**——reward 设计是核心。

---

### 论文 3：Stream RAG（实时语音 Agent）

#### 先搞懂这一篇

**这一篇在回答什么问题？**  
经典 RAG 等用户**问完**再 retrieve——**voice Agent** 要等 5–15 秒才答，不像对话；用户还在说时，**何时**该触发 RAG？

**用一条线串起来：**  
语音幻觉更难抓：听不像读那样主动纠错。核心 framing：**partial speech 何时足够**？例：「今天天气怎样？我想决定要不要出门」——主问题在前半。

**Fixed-interval streaming RAG**：音频分 block，每 block 触发 RAG；用 early pipeline top docs 与「假设完整句」top docs **一致性**决定——匹配则提前用 intermediate query 跑完 pipeline，不等说完。**Learned trigger** 替代：模型判断 chunk 是否已够答，避免每 chunk 全 pipeline。

论文流程：partial spoken question → query grades → 双路 retrieve → 比 retrieval quality → 停或继续。结果（Zeroguma audio）：合成 latency **−0.5s**；真人 **−1.5s**；accuracy 与终局 RAG **持平**。Arnab 强调：**问题 framing** 比某一种 fixed-interval 更重要。

**讲者**：Arnab Mitty（Giga，UW bandit learning；生产 voice agent）

#### 本篇小结

Voice Agent 的关键 framing 是 **partial speech 何时够** 触发 RAG；latency 可降 0.5–1.5s 而 accuracy 持平，比某一种 fixed block 策略更重要。

---

### 论文 4：Lean 与 Verified Intelligence

#### 先搞懂这一篇

**这一篇在回答什么问题？**  
OpenAI / DeepMind 推 Erdős、IMO——**共同点是什么？** 形式化验证 in the loop；**Lean** 如何把「能生成」变成「能证明」？

**用一条线串起来：**  
**Lean** = interactive theorem prover + 函数式编程语言；证明 **fully explicit**，机器 **100% check**——不能教授式 handwave。**Mathlib** 数十万行形式化数学。证明器光谱：左 SMT/ATP（低 effort、表达有限）→ 右 Lean/Coq（高表达、高 effort）；LLM 降低 write-proof cost，生态爆发：AlphaProof、DeepSeek-Prover、Harmonic、Matthink…

**三 bubble**：(1) **Math** 最热闹；(2) **Program verification**——bug 万亿美元级；vibe coding 要 guarantee → **verifiable coding**；(3) **AI for science**——可复现性、输出能否 prove correct。

举例：**Bridge** 用 Lean 验证一般程序；**TorchLean** 证 Flash Attention = 标准 attention；TML 形式化 **temperature=0 inference 仍 non-deterministic**（浮点误差翻转 batch argmax）。与论文 2 呼应：Luke 的 junk Lean statement 展示 formal language 如何界定「题」；Ruben 展示 Lean 作为 **beautiful 验证基础设施**。Friends 称论文 5 是本场 **antithesis**（token maxxing vs 形式证明）。

**讲者**：Ruben George（AI for math/science）

#### 本篇小结

Lean 把「能生成」推向 **能证明**；math / verifiable coding / AI for science 三 bubble 共享 **verified intelligence**——与 token maxxing 式 agentic coding 形成对照。

---

### 论文 5：Channel AI — RTS 式 Agentic Programming

#### 先搞懂这一篇

**这一篇在回答什么问题？**  
Agentic 编程该怎么组织团队和工作流——**chess 式单人深度线**，还是另一种博弈？

**用一条线串起来：**  
Channel AI 自动化 software + **content** 开发，纯 AI 系统让人付费。**Chess vs RTS**：旧编程线性、一次设计做对；Agentic 像 **Warcraft/Starcraft**——经济、生产、侦察、战斗同时跑；地图逐步揭开；无单维完美，要 **持续 course correct**。

**工程栈**：**Git worktrees** 多 repo 并行；**Orchestrator**（Claude/Codex）最少 keystroke 从 idea → worker 开工；**Workers** 推到底（PR + summary），**错也可**人后面改——token 换人的时间；**dangerous permissions + sandbox**；task 可移植（本地→隔夜跑别处）。

**KB > Code 作 context**：结构化 linked markdown KB **便宜**；本场 PPT：Friends 要求 → Claude 读 KB 生成 → 迭代 → **回写 KB**。**可见性**：多 agent 流高可见；**Audio cues** 映射 Warcraft/Starcraft 单位音效；**APM tracker**（tool calls/min）。原则：**Macro default, micro when counts**；**Satisficed not perfect**；Claude 估工期永远离谱——并行 push，别信 timeline。Channel AI：**3.5× RPS/engineer/month** → 全员 adopt 后 **+60% MoM**。

**讲者**：Luc Warthine（Channel AI CEO）

#### 本篇小结

Agentic 编程像 **RTS 不是 chess**：worktree 并行、KB 驱动、macro 优先、satisficing push；Channel AI 用 orchestrator + workers 拿到 **3.5× RPS** 后再 **+60% MoM**。

---

### 跨讲题对照

| 主题 | 论文 1 | 论文 2 | 论文 3 | 论文 4 | 论文 5 |
|------|--------|--------|--------|--------|--------|
| Scaling | compute+data laws | self-play task scaling | latency vs accuracy | prover scaling | token/compute parallelism |
| Bitter Lesson | 主论点 | hand task collection 瓶颈 | — | hand proof → LLM | hand coding → agents |
| Test-time compute | recursive structure refine | self-play rollouts | streaming partial RAG | proof search | parallel workers |
| Verification | contact P@L proxy | Lean unit tests | retrieval quality gate | Lean proof | PR + human spot check |
| Production gap | wet lab drug design | junk task trap | voice latency | verifiable coding | RTS workflow |

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Bitter Lesson** | Sutton：general methods + scale 终胜 hand-crafted domain knowledge |
| **ESM3 / P@L** | 蛋白质 masked LM；P@L = 远程结构接触精度，无监督结构代理 |
| **MSA** | 多序列比对；AlphaFold 手工归纳偏置；abundant 时仍有用 |
| **Self-play (asymmetric)** | Conjecturer 出题 + Solver 解题；同模型两角色 |
| **Junk task trap** | Reward「Solver 做错」→ 最优出恶心复杂题，Solver 不提升 |
| **Self-Guidance** | Ground synthetic 于 unsolved Lean + LLM judge 质量 |
| **Stream RAG / Partial query sufficiency** | 说话过程中触发检索；核心：partial speech 何时够 |
| **Lean / Verified intelligence** | 定理证明器 + FP；从能生成到能形式验证 |
| **f−h** | human demonstration 训练的天花板辩论 |
| **Intelligence per sample** | 每新样本如何学；ICL 非单调 vs 人类单调改进 |
| **RTS agentic coding** | 并行 worktree、orchestrator、macro 优先、satisficing |
| **KB-driven agents** | Linked markdown 知识库作便宜 context，优于扫 code |

---

## 值得记住的原话

> **"Memory has been like the hot topic for at least the last year and a half."**  
> 至少一年半以来，memory 一直是头号热点之一。

> **"Full solutions based on f-training on unknown human solutions will limit you to some typical set."**  
> 若全解基于人类解的训练，你会被困在某个人类解的典型集合里。

> **"As you increase the number of samples in ICL, it is not monotonic... hits a cliff, which is the context length."**  
> ICL 样例增多，性能并非单调提升……最终撞 context length 悬崖。

> **"Evolution has been generating this training data for four billion years."**  
> 进化这套训练数据跑了四十亿年。

> **"The headline isn't that MSAs are dead yet — hand-crafted features only help where they're abundant."**  
> 标题不是说 MSA 已死——手工特征只在数据丰富处才有用。

> **"The easiest way to reach tricky problems is to produce messy, artificially complex problems."**  
> 要出「刁题」，最省事的路子是 messy、人为复杂、不优雅的题。

> **"In principle, nothing bounds learning... In practice, self-play plateaus."**  
> 原则上学习无上界……实践中 self-play 会平台期。

> **"When you're listening, it's difficult to actively catch hallucinations compared to reading text."**  
> 听语音时，人很难像读文本那样主动抓幻觉。

> **"You cannot fool the proof checker."**  
> 证明检查器骗不过去。

> **"Coding with agents feels exactly like playing real-time strategy games."**  
> 用 agent 写代码，体感就是打即时战略。

> **"Macro by default, micro when it counts."**  
> 默认打宏观，关键时刻再微操。

> **"Satisficed is enough, but not perfect."**  
> 够好就行，不必完美。

---

## 小结

**这期最核心的判断：** Applied research 的主线是 **scale 与 verification 并行**——Bitter Lesson 在 bio/RL 仍赢，但 junk task、ICL cliff、f−h 天花板提醒 **不能 naive scale**；工程侧 agentic coding 走向 **RTS + KB**，学术侧走向 **Lean / Stream RAG**。

**读完应带走：**
- **ESM3**：data wall 可破，抗体设计窗口在；**Self-play**：reward 设计 > 算力堆叠。
- **Stream RAG**：语音 latency 靠 partial sufficiency framing；**Lean**：verified intelligence 是 coding/science 下一层。
- **Channel AI**：macro default、KB compound context；Friends 开场 **memory 热但 f−h / intelligence per sample 仍开放**。

**和 vault 的关系：** 接 ai_evaluation 与 multi_agent 横切——五讲可分别链 OpenAI eval、Snorkel RL、Cursor 128、Loop、Harness MOC。

---

## 行动启示

1. **Bio-AI 窗口期**：metagenomic 数据指数增长——ML 背景转 biology 的 leverage 高。
2. **Self-play 别 naive reward**：「越难越好」会学成 junk generator；必须 **ground + quality judge**。
3. **Voice Agent 先 framing 再调参**：何时触发 partial RAG，比某一种 block 间隔更重要。
4. **Lean 从 Mathlib + 小证明入手**：工程团队可先 verifiable coding 试点。
5. **Agentic 团队当 RTS 打**：worktree 并行、orchestrator 派工、worker satisficing push。
6. **KB 投资 > 注释堆砌**：presentation/PR 反馈 **回写 KB**，形成 compound context 优势。
7. **跟 f−h 辩论保持清醒**：human demonstration RL 想清楚 ceiling。
8. **Intelligence per sample 实验**：别默认 ICL 越多越好；小样本试 LoRA、流式策略切换。

---

## 相关阅读

- [[OpenAI评估团队-不再低估模型]] — eval、湿实验与 capability 测量
- [[Snorkel-小模型RL超越大模型]] — 小模型 RL beat 大模型；与 self-play 7B beat 67B 同脉
- [[DeepMind团队-当数百万Agent相遇]] — multi-agent scaling 与协调
- [[Cursor-128个Agent团队协作]] — 大规模并行 agent 工程
- [[IBM团队-Harness工程详解]] — harness 可靠性；RTS orchestration 是 harness 操作层
- [[Loop-Agent Loop到底是什么]] — agent loop 与 self-play / 长 horizon RL 对照
- [[MOC - Agent Theory and Design]] — 主题 MOC 入口

---

## 来源

- **视频**：[BV14AjN6oEcg](https://www.bilibili.com/video/BV14AjN6oEcg/)（B 站转载 YC Paper Club）
- **活动**：Friends 主持；Yash Big / Luke / Arnab Mitty / Ruben George / Luc Warthine
- **转写**：Recastory `B4-yc-paper-club/article.md`（英文 ASR，收录时已人工整理叙事）
- **版本**：v2 读者向讲义（2026-07-02）
