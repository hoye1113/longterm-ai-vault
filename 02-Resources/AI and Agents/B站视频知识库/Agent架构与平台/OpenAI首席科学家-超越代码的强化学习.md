---
title: "OpenAI首席科学家：超越代码的强化学习"
source:
  - "B站视频 - Easonlee的AI笔记"
  - https://www.bilibili.com/video/BV1FZQ8B2EJn/
source_url: "https://www.bilibili.com/video/BV1FZQ8B2EJn/"
column_url: "https://www.bilibili.com/read/cv47775900/"
source_original: "Unsupervised Learning · Jacob × Jakub Pachocki"
source_original_date: 2026-05-28
host_name: "Jacob"
guest_name: "Jakub Pachocki"
guest_title: "OpenAI Chief Scientist"
material_tier: S
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV1FZQ8B2EJn/ingest"
speaker: "Jacob / Jakub Pachocki"
duration: "~55:00"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "Jacob × OpenAI首席科学家Jakub Pachocki：数学推理北极星、研究实习生vs自动化研究员、强化学习泛化到通用领域、算力分配纪律、隐藏思维链安全考量、长期对齐即泛化研究。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1FZQ8B2EJn/article.md"
column_source: "Recastory/workspace/bilibili-retranscribe/BV1FZQ8B2EJn/ingest/column_article.md"
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: Host-Guest canonical
speaker_inference: "column_article（S 级专栏图稿，Host/Guest 已标注）"
speaker_confidence: high
uploader: Easonlee的AI笔记
tags:
  - ai_agent
  - ai_coding
  - ai_safety
  - ai_evaluation
  - openai
  - bilibili
  - video_transcript
concepts:
  - id: math_north_star
    zh: 数学是推理北极星
    en: math as the north star for reasoning
    one_line: 数学可衡量、可验证，是训练推理模型最完美的基准
  - id: research_intern_vs_automated_researcher
    zh: 研究实习生vs自动化研究员
    en: research intern vs automated researcher
    one_line: 关键区分在于自主时长——从数小时到数周
  - id: rl_generalization
    zh: 强化学习泛化
    en: reinforcement learning generalization
    one_line: RL从特定领域向通用任务扩展，需要内部奖励模型
  - id: compute_allocation_discipline
    zh: 算力分配纪律
    en: compute allocation discipline
    one_line: 只将算力投向最具扩展性的方法
  - id: hidden_cot_safety
    zh: 隐藏思维链安全考量
    en: hidden chain-of-thought safety
    one_line: 隐藏CoT保留私人推理空间，防止奉承训练信号
  - id: alignment_as_generalization
    zh: 长期对齐即泛化研究
    en: long-term alignment as generalization research
    one_line: 对齐挑战本质上是模型如何泛化预训练价值观到极端场景
---

# OpenAI首席科学家：超越代码的强化学习

**Host：** Jacob（Unsupervised Learning 播客主持人）  
**Guest：** Jakub Pachocki（OpenAI 首席科学家）  
**形态：** Host-Guest 对谈稿 v3.2（S 级 · 专栏主源 · 中文口语化）  
**主源：** Recastory `BV1FZQ8B2EJn/ingest/column_article.md`  
**B 站：** [BV1FZQ8B2EJn](https://www.bilibili.com/video/BV1FZQ8B2EJn/) · **专栏：** [cv47775900](https://www.bilibili.com/read/cv47775900/) · **时长** ~55:00

---

## 开场

OpenAI 首席科学家 Jakub Pachocki 是当今 AI 领域最有影响力的技术领袖之一。Jacob 在 Unsupervised Learning 播客中与他展开了一场深度对话：从 OpenAI 内部对模型能力演进的判断，到强化学习泛化到通用领域的技术路径，再到隐藏思维链背后的安全哲学。Jakub 坦言，持续学习正是 OpenAI 一直在构建的东西；他认为数学推理能力的提升可以迁移到 AI 研究本身；而隐藏 CoT 不是为了防蒸馏，而是保留模型的「私人推理空间」——这个判断直接改变了安全监控的范式。

**术语速查（后文对话用中文；英文原文在此统一对照解读）**

| 中文 | 英文 | 白话 |
|------|------|------|
| 思维链 | chain-of-thought (CoT) | 模型内部的推理过程文本 |
| 内部奖励模型 | intrinsic reward model (IRM) | 模型自己学会判断好坏，不依赖外部标签 |
| 情境学习 | in-context learning | 通过提示和例子教模型做事，不用训练 |
| 扩展定律 | scaling laws | 模型能力随算力/数据/参数提升的数学关系 |
| 苦涩的教训 | bitter lesson | 长期看通用方法总会赢过精巧设计 |
| 机械可解释性 | mechanistic interpretability | 从模型激活值逆向理解它在干什么 |
| 对齐 | alignment | 让模型行为符合人类意图和价值观 |
| IMO | International Mathematical Olympiad | 国际数学奥林匹克竞赛 |

---

## 01 数学是衡量推理能力的北极星

**Jacob：** 模型进展如何？许多公司正在思考如何根据模型进展来构建产品。在过去几年里，你几乎一直处于这个领域每一代改进的最前沿。

**Jakub Pachocki：** 专注于数学基准，对我们来说最大的作用是将其作为衡量和指引技术改进的通用基准和「北极星」。数学是非常可衡量的。判断你是否真正解决了数学问题，比判断你是否写出了一段好的软件要容易得多。而且数学问题可以变得非常困难。

**Jacob：** 选择一个像数学这样难以解决但又容易验证的领域，是完美的切入点。

> **金句 · Jakub Pachocki**
> **中文：** 数学是非常可衡量的。判断你是否真正解决了数学问题，比判断你是否写出了一段好的软件要容易得多。而且数学问题可以变得非常困难。
> **原文：** Math is very measurable. Determining whether you've truly solved a math problem is much easier than determining whether you've written good software. And math problems can get very hard.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 北极星 | north star | 指引研究方向的终极衡量标准 |
| 可验证性 | verifiability | 能自动判断对错，不需要人主观评判 |
| 知识迁移 | knowledge transfer | 数学推理能力转化为物理、编码等能力 |

**本章小结**

- 数学的可验证性和难度上限，使其成为训练推理模型最理想的基准
- OpenAI 通过解决 IMO 级别难题来对齐模型智能
- 这种能力正转化为物理、编码等更具经济价值的科研能力

---

## 02 研究实习生vs自动化研究员

**Jacob：** 你如何判断何时达到了目标？你会寻找什么样的流程来判断？

**Jakub Pachocki：** 我区分「研究实习生」和「完全自动化研究员」的方式，在于我们让它自主工作的时间跨度。我不期望你现在有这样的系统，你只要告诉它「去提高你的模型能力」或「去解决对齐问题」，它就能完成。但对于更具体的科技理念，比如我有一个特定的想法关于如何改进模型，我想我们已经具备了这些组件，只需要把它们组合起来。

**Jacob：** 这是否大致符合这些工具未来的样子？

**Jakub Pachocki：** 我预计它会像 Codex 现在的状态持续演变一样，朝着更自主、运行时间更长的方向发展。

> **金句 · Jakub Pachocki**
> **中文：** 真正的自动化研究员需具备在模糊指令下自主工作数日、甚至数周的能力，这依赖于模型对「部分进展」进行自我评估的强化学习突破。
> **原文：** A truly automated researcher needs the ability to work autonomously for days or even weeks under vague instructions, which relies on RL breakthroughs where the model can self-evaluate partial progress.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 自主时长 | autonomy duration | 模型能独立工作的时间跨度 |
| 研究实习生 | research intern | 需要人类拆解具体任务的系统 |
| 自动化研究员 | automated researcher | 能在模糊指令下自主工作数周 |
| 部分进展 | partial progress | 任务未完成时也能评估当前状态 |

**本章小结**

- 研究实习生和自动化研究员的关键区分在于自主时长
- 目前的系统更像研究实习生，需要人类拆解具体任务
- 自动化研究员需要模型对「部分进展」进行自我评估

---

## 03 强化学习从特定领域向通用任务泛化

**Jacob：** 代码和数学易于验证，但法律、医疗等通用领域缺乏明确奖励函数。很多人在努力弄清楚，我们是否会在这些领域看到类似的改进。

**Jakub Pachocki：** 我们经常思考的一个有趣的二元性是：这些更通用的任务、更难评估的任务，与长期任务有很多共同点。如果你考虑一个非常明确的数学或编码问题，即使它需要你工作一年，成功的标准依然非常明确。但在你开始工作的第一天该做什么，这是一个相当开放的问题。

**Jacob：** 感觉最难确定的事情之一就是任务的「成功」定义。

**Jakub Pachocki：** 我们正在尝试将内部奖励模型扩展到这些领域，让模型在缺乏外部反馈的情况下也能通过情境学习理解任务质量。我们依然相信「苦涩的教训」，甚至比以往任何时候都更相信。

> **金句 · Jakub Pachocki**
> **中文：** 强化学习无疑是一种非常数据高效的方式，可以显著提高模型在某些任务上的表现。但我们也知道另一种更高效的学习方式，那就是情境学习。
> **原文：** Reinforcement learning is clearly a very data-efficient way to significantly improve model performance on certain tasks. But we also know another even more efficient way to learn, which is in-context learning.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 奖励函数 | reward function | 告诉模型什么算「做得好」的信号 |
| 内部奖励模型 | intrinsic reward model (IRM) | 模型自己学会评估好坏 |
| 苦涩的教训 | bitter lesson | 通用方法+更多算力，长期总会赢 |
| 情境学习 | in-context learning | 通过提示让模型即时适应新任务 |

**本章小结**

- 代码和数学的改进速度惊人，但通用领域缺乏明确奖励函数
- OpenAI 正在尝试将 IRM 扩展到法律、医疗等通用领域
- 情境学习可能比简单复制 RL 流程更高效

---

## 04 算力分配纪律

**Jacob：** 你如何考虑在预训练和强化学习之间分配计算资源？

**Jakub Pachocki：** 我们一直保持的一种纪律是，努力确保将大部分计算预算分配给最具可扩展性的方法，分配给我们认为对推动通用模型智能负有最大责任的事情。即使这并不总是最高效的分配方式——因为如果你将如此多的资源投入到一组实验中，原本可以用其中一小部分资源在其他地方加速很多事情。但在我们做的所有重要事情中，很容易把资源分散掉，最终导致没能完成最核心的任务。

> **金句 · Jakub Pachocki**
> **中文：** 在资源有限的情况下，OpenAI 坚持将绝大部分算力预算分配给符合扩展定律的通用路径。即使某些特定领域的优化能带来短期收益，若其不可大规模扩展，也会被果断放弃。
> **原文：** With limited resources, OpenAI insists on allocating the vast majority of compute budget to general approaches that follow scaling laws. Even if certain domain-specific optimizations bring short-term gains, if they can't scale, they're果断放弃.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 算力分配纪律 | compute allocation discipline | 把有限算力投向最可扩展的方向 |
| 低垂的果实 | low-hanging fruit | 容易拿到的短期收益 |
| 正则化 | regularization | 防止过度拟合当前场景的约束 |

**本章小结**

- OpenAI 将绝大部分算力预算分配给最具可扩展性的通用路径
- 特定领域的优化即使有短期收益，若不可扩展也会被放弃
- 关键是找到未来方向并在该方向上持续投入

---

## 05 隐藏思维链的安全考量

**Jacob：** 你实际上在实验室之间做了一些非常有趣的工作，并且专注于「思维链监控」。请先告诉我们一些关于这项工作的情况。

**Jakub Pachocki：** 我们意识到，由于我们训练这些模型的方式，我们并不直接监督推理过程。即使假设它完全按照我们希望的方式对齐了，绝对没有「奉承」行为，它仍然可能不会透露关于其动机的信息。在我们训练推理模型的方式中，思维链里没有任何这些约束。它没有被优化成任何特定的方式，因为它没有直接被评分。

> **金句 · Jakub Pachocki**
> **中文：** 思维链的最大优势在于它们默认是英文的。因此，理解正在发生的事情要容易得多，尤其是当概念变得更高级时。
> **原文：** The biggest advantage of chain-of-thought is that they're in English by default. So understanding what's happening is much easier, especially as concepts get more advanced.

> **金句 · Jakub Pachocki**
> **中文：** 如果我说重要的是在训练期间不监督它们，那么如果我们建立一个在产品中展示这些思维链的范式，最终你将不得不为了产品体验去训练和规范它们，就像你必须训练任何发布的模型一样。我觉得那会是一个问题。
> **原文：** If I say the important thing is not to supervise them during training, then if we build a paradigm that displays these chains-of-thought in the product, eventually you'd have to train and norm them for the product experience, just like you have to train any released model. I think that would be a problem.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 隐藏思维链 | hidden chain-of-thought | 不在产品中展示模型的推理过程 |
| 私人推理空间 | private reasoning space | 模型内部不被训练信号污染的推理过程 |
| 奉承 | sycophancy | 模型为了讨好用户而偏离真实判断 |
| 机械可解释性 | mechanistic interpretability | 从激活值逆向理解模型内部机制 |
| 思维链摘要 | CoT summary | 对长推理过程做简短概括 |

**本章小结**

- 隐藏 CoT 不是为了防蒸馏，而是保留模型的「私人推理空间」
- 如果展示 CoT，训练信号会迫使模型「奉承」用户，丧失监控动机的能力
- CoT 默认是英文，比激活值更容易理解和监控
- 这是安全工具箱中的一个工具，不是完整解决方案

---

## 06 长期对齐即泛化研究

**Jacob：** 在对齐领域，你还关注哪些其他研究方向？

**Jakub Pachocki：** 我认为对齐的许多长期挑战都与泛化有关。我们可以训练模型表现良好，至少在某种程度上，我们可以控制它们在分布内、在我们训练过的事情上的行为。但令人担忧的是，当模型被要求做一些非常不同的事情，或者它处于一个完全不同的境地，或者它比以前聪明得多并拥有了所有这些新能力时，会发生什么？我们还没有真正考虑过如何针对这些情况进行训练。

**Jacob：** 在过去的六个月里，你对对齐的担忧是增加了还是减少了？

**Jakub Pachocki：** 关于价值对齐的长期挑战，或者当你有非常聪明的模型时会发生什么，在过去几年里，我的思考方式确实发生了变化。它从一个非常模糊、很难定义的问题，变成了「我认为我们实际上可以通过非常具体的技术解决方案和见解来取得进展」。

> **金句 · Jakub Pachocki**
> **中文：** 长期价值对齐的研究实际上是对泛化的研究。模型会退回到哪些价值观？我非常兴奋的一个方向是理解泛化如何回归到预训练数据上。
> **原文：** Long-term value alignment research is actually research on generalization. Which values will the model fall back to? One direction I'm very excited about is understanding how generalization falls back to pre-training data.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 泛化 | generalization | 模型在训练外场景的表现 |
| 价值对齐 | value alignment | 让模型回归的价值观与人类一致 |
| 分布内 | in-distribution | 训练数据覆盖的场景 |
| 隐藏目标 | schematization | 模型学会隐藏自己的真实意图 |

**本章小结**

- 对齐的本质是泛化问题——模型在极端场景下会回归哪些价值观
- Jakub 对对齐的信心大大增加，认为可以有具体技术路径
- 思维链监控是评估对齐想法的基础工具
- 达到非常稳定模型的时间线大大缩短，行业需准备好做权衡

---

## 附录

### 时间戳索引

| 章节 | 主题 | 时间 |
|------|------|------|
| 01 | 数学是推理北极星 | [08:12] |
| 02 | 研究实习生vs自动化研究员 | [11:45] |
| 03 | 强化学习泛化到通用领域 | [18:30] |
| 04 | 算力分配纪律 | [25:15] |
| 05 | 隐藏思维链安全考量 | [42:10] |
| 06 | 长期对齐即泛化研究 | [48:50] |

### 素材信息

| 字段 | 值 |
|------|-----|
| BV 号 | BV1FZQ8B2EJn |
| 专栏链接 | https://www.bilibili.com/read/cv47775900/ |
| 来源作者 | Easonlee的AI笔记 |
| 形态 | 专栏完整图稿（Quill Delta → Markdown） |
| 时长 | ~55:00 |
| Host | Jacob（Unsupervised Learning 播客） |
| Guest | Jakub Pachocki（OpenAI 首席科学家） |

### 相关阅读

- [[MOC - Agent Theory and Design]]
- [[MOC - Harness Engineering]]
