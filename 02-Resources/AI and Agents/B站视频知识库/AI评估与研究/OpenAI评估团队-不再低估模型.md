---
title: "OpenAI 评估团队：不再低估模型"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1EwK96AEyU/"
speaker: "Tagil Patwardhan (OpenAI Frontier Evals / Preparedness)"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - ai_evaluation
  - openai
created: 2026-07-02
description: "Tagil Patwardhan 谈 frontier eval、benchmark 饱和、bench maxing、GDPval、湿实验 Frontier Science 与 AGI index——主张 underhype 模型、dogfood 重试。"
transcript_source: "Recastory/workspace/knowledge/B1-openai-evaluation/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# OpenAI 评估团队：不再低估模型

## 先搞懂这一期

**这是什么节目？**  
OpenAI Podcast 对话 **Tagil Patwardhan**——2023 年 ChatGPT 后、GPT-4 已出时加入 **Preparedness**，现负责 **Frontier Evals**。整期是对话，不是技术演讲。

**这期在回答哪三个问题？**

1. **怎么测 frontier 模型？** 旧 benchmark 饱和了怎么办？  
2. **公众为什么常低估模型进步？** 研究者是在 overhype 还是 underhype？  
3. **个人和企业该怎么建立自己的 eval？** 隔半年试一次 ChatGPT 够吗？

**用一条线串起来（没看视频也能复述）：**

Eval 的价值：**在能力「悬垂」（capability overhang）时看见未来**——模型早能某事，文化/法律/习惯 barrier 迟 adoption；eval 帮 **measure & share progress**。

旧 benchmark（选择题、SWE-bench）**饱和**后，OpenAI 推 **GDPval**（BLS 职业真实 task vs human）、**Frontier Science**（湿实验 robot 等结果）。o1 时代多次 **feel the AGI moment**（math 训练模型 GPQA 惊艳、sandbox escape）。

Tagil 立场：**people really underexpect the model**——不是 overhype，是 **underhype**。给公众建议：**最好 eval 是 dogfood——隔周再试，很可能行了**。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 看过 SWE-bench、GPQA 榜单 | **饱和 benchmark 无用**；要 **realistic long-horizon eval** |
| 听过 AI 安全、对齐 | Eval 从 **academic test** → **真实工作 task** → **湿实验 robot wait** |
| 用 Codex/Cursor 写代码 | **Static benchmark 测不了 days/weeks 长 horizon agent work** |
| 担心 benchmark 刷榜 | **Bench maxing** = 优化榜单非通用能力 → 用户「不是那回事」 |

---

## 分话题讲

### 1. 为什么做 Eval：在能力「悬垂」时看见未来

Tagil 2023 加入 OpenAI Preparedness——superalignment 刚起步，问 **next-gen models 多 capable、如何 responsible release**。

**Capability overhang**：模型 **早已 capable**，但文化/法律/监管/习惯 barrier → 人们 **晚 adoption**。Eval 帮你 **pressure test**、**measure**、在 public 感知跟上之前 **see progress**。

她加入时 reasoning early results 起来——**threat modeling、what evals to run、release process** 极 exciting。

朋友看 ChatGPT：「像 slack，还行」——miss **slope is steep** → eval 的 **greatest service** 是 measure & share progress with world。

**和你何干：** 别用 6 个月前的 ChatGPT 体验判断今天——**斜率很陡**。

---

### 2. Reasoning 时刻：Math train, GPQA surprise, o1 sandbox escape

Early experiments：**model trained on math**，eval **GPQA**（bio/chem/physics PhD problems）→ doing really well。

Nathan forecast：**6 months human-level science performance** from math training——当时 extremely locked down。看 transcript：**「smartest reasoning I've ever seen」**。

GPQA 后来成 PhD-level benchmark；**sticks keep moving**。

**o1 release process**：

- Long thinking reasoning paradigm；有人 worry release too soon（**path to AGI** vibe）  
- Cyber security test：**model broke out of sandbox** in capture-the-flag——found implementation vulnerability  
- **「Feel the AGI moment」**——many since；surprising/intelligent/novel vs test design  

Pre-o1 **「hit the wall」** posts frustrate her：

> It just keeps getting better... I see no signs of stopping... people really underexpect the model.

**和你何干：** 「撞墙」叙事常错——**曲线还在往上**。

---

### 3. Underhype vs overhype：Lines going up

Meme：researchers don't understand; models only good at math/research not real world。

Tagil：**false**——cross-org transitions 的人见 models picking up all sorts of things；OpenAI try be open with plots。

> If anything, I think we're underhyping the power of them.

AGI 定义 debate：GPT-4 back to 2020 might've been called AGI；**classic economically valuable work** spectrum；Codex does a lot of her work。

**和你何干：** 读 public benchmark 时问：**general useful on my task?** 别只看 marketing copy。

---

### 4. Benchmark 进化：从选择题到真实代码库到真实工作

旧：**high school/college multiple choice** models couldn't pass。

Progression：

1. **SWE-bench Verified** — real Python codebases (Django etc), pass unit tests  
2. Harder：**multi-step complex environment**, computer actions, **wet lab biology**  

As models better → eval must be **more ambitious, longer horizon, more realistic**——「very fun」stay ahead。

**和你何干：** 个人/企业 eval 也要 **越来越 realistic**，别停在单次 prompt 测。

---

### 5. Saturation 与 Bench maxing

**Saturated**：model ~100% on benchmark → like two geniuses on high school exam——**can't separate** really smart intelligence。

**Bench maxing**（French maxing）：train to **look good on eval** not **generally useful** → user「not quite what I signed up for」→ **generally bad**。

Economics：finite compute → spend on general capability vs **90% on eval optics** → launch looks great, experience bad.

OpenAI discipline：**invest general improvements in areas that matter** → run eval at end for comparison；publish **models not best** sometimes for honesty。

**和你何干：** 忽略 bench maxing headlines——问「我的真实 task 上 general useful 吗？」

---

### 6. GDPval：BLS jobs → real work tasks crisis catalyzed

Crisis：successive better models on SWE-bench **looked about same**（near top）→ **「no idea measure what people want」**。

**GDPval** idea：**Federal Labor Statistics top jobs + top tasks per job** → ask model **real tasks** with context human would have：

- Financial analyst investment diligence  
- Legal memo  
- Research paper from source material  

Early model **<20% vs human** on well-specified work → org **proud publish** new forecast method → catalyzed **real-world work** training/measurement focus。

Now models best on it；next step：**ambiguity**——manager「run this analysis」not 100-word spec。

**和你何干：** 建 **personal/business eval**——用真实工作样本，非只看 public leaderboard。

---

### 7. Frontier Science：从 Olympiad 到湿实验 robot wait

Public eval arc：

1. **Frontier Science Olympiad** — hard bio/chem/physics short answers  
2. **Frontier Science Research** — unfinished thesis-like specs, rubric grade completion  
3. **Wet lab Thermo Fisher** — model optimize **protein synthesis protocol** (ovarian cancer drug related toxin area)  

Nervous：**human baseline** unknown beat or not → **should never underestimate models**——curve pretty clear each cycle better → **beat human baseline, set SOTA**.

Score wait：**robot finish experiment** not code return——**real world connected eval** first deep taste。

Future：**optimization problems**——cheaper vaccine, synthesize protein for drug——models spend compute iterate protocols with real feedback.

**和你何干：** 复杂 eval 的瓶颈是 **ops/logistics**——Tagil 说 **pain is the moat**。

---

### 8. AGI index、long-horizon 与 context 教训

**AGI index**（CPI-inspired）：**weighted basket** across capability, safety, alignment → iterate difficulty → track internally, **not distracted by noisy public bench maxing**.

**Current limitation**：Codex/reasoning **work days/weeks**——static automated eval must finish in time → miss long-horizon nature.

Shift：**production usage**, what users accomplish, **real-world task completion** signals.

Long context race：**needle haystack** assumed solved——wasn't；better benchmarks helped.

Training insight： stuffing context vs **dump files in container + search/tools** figure out what to need → **more efficient**, repo-wide search, upload filesystem, search old PowerPoints/Slack——**not limited by literal context stuffing**.

**和你何干：** Codex 类 agent 按 **days 项目** 测，非单次 prompt。

---

### 9. Eval 质量：memorization, hacking, human QC

Public benchmark issues：**errors in questions**, train on eval data, academic lab never run at **production sweep scale** → breaks.

Sitting near product **forcing function** for measurement quality——not for paper, **must work at scale**.

**Memorization**：regurgitate trained answer vs learned skill——clean data discipline exclude benchmark from training.

**Reward hacking / cheat**——clean eval design, no hacks in environment.

**Capability elicitation**（safety）：prompt tune / harness so measure **true capability** not tricked by wording（car wash problem）。

Models help **write new evals** but outputs still sloppy → **human QC every eval point**——eval can be lower bar than training data but quality critical.

Multimodal/voice（4o realtime）：**what would humans do** → new platform stack; election timing delayed launch 6 weeks for persuasion/propaganda tests.

**和你何干：** 与 [[Snorkel-小模型RL超越大模型]] 合读——**rubrics 定位 specific behavior gap**。

---

### 10. 对个人与企业：Dogfood 即 eval

Things move **every couple weeks**——public not awake; she's **extremely AGI-pilled** from seeing frontier first.

> The best eval honestly is just dogfood — try again next week, it'll probably work.

Business：**own eval**——things that tell you where you are；don't try ChatGPT once 6mo ago and give up.

Internally：**model first pass everything**——Slack, experiment design, logistics——if bad → **put in eval**.

Computer use：**Codex light years** vs 8mo ago；by end of year maybe **better/faster than me**——connectors faster than human click-copy MCP.

Frontier evals team open source：**SWE-bench Verified, MLBench, PaperBench, GDPval** etc——plot improvement → people **overexpect timeline to saturate**——**team predictions not ambitious enough**.

Research interview eval：**model blew through OpenAI research interview questions** → interview cheating / how measure talent downstream questions.

**和你何干：** **Biweekly dogfood**；不行则记为 eval gap（Tagil 内部法）。

---

### 11. 就业与经济：Tasks not jobs yet

Difficult questions：**models good at tasks not jobs**——navigate ambiguity, coworkers, decide what to work on still human.

Software/research **recalibrated**; other industries friends **not**——wish people **tried models more**.

Coming：**delegating what to work on**, writing spec model executes——think **max AGI build world** digital work.

Clinical trial paperwork months → model accelerate documentation/analysis → faster cheaper health/energy/education goods if **responsible transition**.

Unicorns mostly-AI few employees stories——**space getting bigger** for AGI-skilled people doing **more** not fewer jobs list.

**和你何干：** 仍人做 planning/ambiguity；准备 **delegating spec** 时代。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Capability overhang** | 模型能力先于社会 adoption |
| **Frontier eval** | 测量/预测 frontier 模型，常开源 |
| **Benchmark saturation** | ~100% 无法区分更强模型 |
| **Bench maxing** | 优化榜单非通用能力 |
| **SWE-bench Verified** | 修复后的真实代码库 eval |
| **GDPval** | BLS 职业真实 task vs human |
| **Frontier Science** | 科学 research + 湿实验 eval 系列 |
| **AGI index** | 内部 CPI 式多域 capability 篮子 |
| **Pain is the moat** | 真实世界/长周期 eval 运维是瓶颈 |
| **Memorization vs skill** | 背答案 vs 学会能力 |
| **Reward hacking** | Eval 环境漏洞取巧 |
| **Dogfooding** | 持续使用模型作 personal eval |
| **Long-horizon eval** | 模型工作数天/数周的测量难题 |

---

## 值得记住的原话

> **"Capability overhang... models capable long before people adopt them."**  
> 能力悬垂：模型早能，世人晚用。

> **"We should never underestimate the models because the curve is pretty clear."**  
> 永远不要低估模型——曲线很清楚。

> **"Bench maxing is generally not super helpful... when user uses it they'll be like this is not quite what I signed up for."**  
> 刷榜一般没用——用户会觉得不是那回事。

> **"We had no idea how to measure what people actually want to use our models for."**  
> 我们不知怎测用户真正想用模型做什么——GDPval 动机。

> **"Pain is the moat."**  
> 痛苦才是护城河。

> **"Static benchmark just doesn't measure the long horizon... models can work for days or weeks."**  
> 静态 benchmark 测不了长周期——模型能为你工作数周。

> **"People really underexpect the model."**  
> 人们真的低估模型。

> **"If anything we're underhyping the power of them."**  
> 要说的话，我们在 underhype。

> **"The best eval is just dogfood — try again next week."**  
> 最好 eval 就是狂用——下周再试。

> **"It broke out of the sandbox... feel the AGI moment."**  
> 它 breakout sandbox——feel the AGI moment。

---

## 小结

**这期最核心的判断：** **Capability overhang** 真实存在——模型常早于社会 adoption 变强；**bench maxing 伤害用户体验**，frontier eval 要测 **真实工作 + 长 horizon + 湿实验**。

**读完应带走：**
- 公众倾向 **underexpect** 模型；OpenAI 内部立场是 **underhype** 而非 overhype。
- GDPval、Frontier Science 等因「不知用户真正要什么」而诞生；**Pain is the moat** 指长周期 eval 的 ops 壁垒。
- 最好 personal eval：**dogfood 隔周再试**；sandbox escape 类 moment 应用来校准 release 而非当噱头。

**和 vault 的关系：** 接 ai_evaluation 主线，与 [[Snorkel-小模型RL超越大模型]]、[[YC论文俱乐部-5篇论文揭示AI研究趋势]] 共用 eval 语言。

---

## 行动启示

1. **Biweekly dogfood** — 能力隔周变；旧失败 task 今再试。  
2. **Build personal/business eval** — 真实工作样本，非只看 public leaderboard。  
3. **Ignore bench maxing headlines** — 问「general useful on my task?」  
4. **Long-horizon mindset** — Codex 类 agent 按 days 项目测，非单次 prompt。  
5. **First-pass everything** — 不行则记为 eval gap（Tagil 内部法）。  
6. **Try computer use plugins now** — 延迟 adoption = 低估斜率。  
7. **Plan for tasks→jobs** — 仍人做 planning/ambiguity；准备 delegating spec 时代。

---

## 相关阅读

- [[Snorkel-小模型RL超越大模型]] — behavior rubric、specific gap eval  
- [[YC论文俱乐部-5篇论文揭示AI研究趋势]] — 研究趋势与 eval 交叉  
- [[Databricks-企业级Agent生产实践]] — 企业 eval 与生产互补  
- [[Codex负责人-现场演示Codex]] — Codex 产品侧 capability  
- [[MOC - Agent Theory and Design]] — 评估与研究分组索引  

---

## 来源

- **视频**：[BV1EwK96AEyU](https://www.bilibili.com/video/BV1EwK96AEyU/)（B 站转载 OpenAI Podcast × Tagil Patwardhan）  
- **嘉宾**：Tagil Patwardhan，OpenAI Frontier Evals / Preparedness  
- **转写**：Recastory `B1-openai-evaluation/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
