---
title: "Lex Fridman播客：2026年AI现状与展望"
source:
  - "https://www.bilibili.com/video/BV1ArFCz5EjX/"
  - "https://www.bilibili.com/read/cv45480286/"
source_url: "https://www.bilibili.com/video/BV1ArFCz5EjX/"
column_url: "https://www.bilibili.com/read/cv45480286/"
column_source: "Recastory/workspace/bilibili-retranscribe/BV1ArFCz5EjX/ingest/column_article.md"
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV1ArFCz5EjX/ingest"
duration: "~120 min"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "Lex Fridman × Sebastian Raschke × Nathan Lambert：DeepSeek 时刻后的国际AI竞争格局、文本扩散模型、工具使用、持续学习、AGI时间线、开源生态与广告货币化。"
material_tier: S
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: "Host-Guest canonical"
host_name: "Lex Fridman"
guest_name:
  - "Sebastian Raschke"
  - "Nathan Lambert"
guest_title:
  - "机器学习研究员，《从零开始构建LLM》作者"
  - "艾伦人工智能研究所训练后负责人"
speaker_inference: "column_article S-tier + podcast structure (Lex host, Sebastian & Nathan co-guests)"
speaker_confidence: high
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - openai
  - anthropic
  - deepseek
  - scaling_laws
author:
  - "[[Sebastian Raschke]]"
  - "[[Nathan Lambert]]"
concepts:
  - id: deepseek_moment
    zh: DeepSeek 时刻
    en: DeepSeek moment
    one_line: 2025年1月DeepSeek R1以更低成本达到领先性能，标志中国开源AI崛起
  - id: text_diffusion
    zh: 文本扩散模型
    en: text diffusion model
    one_line: 迭代填补缺失token的并行生成范式，可能用于快速廉价大规模任务
  - id: recursive_lm
    zh: 递归语言模型
    en: recursive language model
    one_line: 将长上下文任务分解为子任务，递归调用LLM解决，比一次性处理更高效
  - id: continual_learning
    zh: 持续学习
    en: continual learning
    one_line: 不断改变权重使模型根据新信息适应调整，vs 上下文学习
  - id: bitter_lesson
    zh: 苦涩的教训
    en: bitter lesson
    one_line: 计算资源将变得更加丰富，能从中获得100倍收益的模型会胜出
---

# Lex Fridman 播客：2026 年 AI 现状与展望

**Host：** Lex Fridman（播客主持人）  
**Guest：** Sebastian Raschke（ML研究员，《从零开始构建LLM》作者） × Nathan Lambert（艾伦AI研究所训练后负责人）  
**形态：** Host-Guest canonical v3.2（**专栏主源** · Lex Fridman Podcast #476）  
**B 站：** [BV1ArFCz5EjX](https://www.bilibili.com/video/BV1ArFCz5EjX/) · **专栏** [cv45480286](https://www.bilibili.com/read/cv45480286/) · **时长** ~120 min

---

## 开场

Lex Fridman 邀请两位 ML 研究员——Sebastian Raschke（《从零开始构建 LLM》《从零开始构建推理模型》作者）和 Nathan Lambert（艾伦AI研究所训练后负责人、RLHF 权威书籍作者）——回顾 2026 年 AI 领域的技术突破与产业格局。

五章：**DeepSeek 时刻与国际竞争** → **文本扩散模型与架构演进** → **工具使用与持续学习** → **AGI 时间线与编程自动化** → **产业格局与开源生态**。

**术语速查**

| 中文 | 英文 | 白话 |
|------|------|------|
| DeepSeek 时刻 | DeepSeek moment | 中国开源模型以更低成本达到领先性能 |
| 文本扩散模型 | text diffusion model | 并行填补缺失token的生成范式 |
| 递归语言模型 | recursive language model | 分解子任务递归调用LLM |
| 持续学习 | continual learning | 权重不断更新适应新信息 |
| 上下文学习 | in-context learning | 通过长上下文窗口加载额外信息 |
| Muon 优化器 | Muon optimizer | 二阶优化器，正交化梯度更新 |
| RLVR | RL with verifiable rewards | 可验证奖励的强化学习 |
| 苦涩的教训 | bitter lesson | 计算资源越丰富，能从中获益越多的模型越赢 |

---

## 01 DeepSeek 时刻与国际竞争格局

**Lex（Host）：** 我想从一个有用视角开始——"DeepSeek 时刻"。大约一年前，DeepSeek R1 发布，以据称更少的计算资源、更低的成本达到接近领先的性能。从那时到今天，AI 竞争在研究和产品层面都变得异常激烈。在国际层面，谁是赢家？中国公司还是美国公司？Sebastian，你认为谁会赢？

**Sebastian Raschke（Guest）：** "赢"是一个非常宽泛的词。我确信在 2020 年代，不会有任何一家公司拥有独家技术，因为研究人员经常跳槽、更换实验室，他们是流动的。所以我不认为在技术获取方面会有明确的赢家。区分因素将是**预算和硬件限制**，而不是想法。我目前看不到赢家通吃的局面。

**Nathan Lambert（Guest）：** 各个实验室投入的精力不同。Anthropic 的 Claude Opus 4.5 引发的热潮令人难以置信。文化上，Anthropic 以大力押注代码闻名，代码策略目前对他们很奏效。但中国有很多令人瞩目的技术，DeepSeek 正在失去其作为中国最杰出开源模型制造商的桂冠。智谱 AI 的 GLM、Minimax、Kimi Moonshot 表现更加出色。2025 年 DeepSeek 的出现为更多中国公司开启了一种新型运营模式。

**Lex：** 你认为中国公司会继续发布开源模型多久？

**Nathan：** 会持续几年。许多中国公司意识到美国科技公司不会为中国 API 订阅付费，所以将开源模型视为参与美国庞大 AI 支出市场的能力。政府也看到这在技术采纳方面正在建立国际影响力。但构建这些模型非常昂贵，到某个时候会出现整合。

> **金句 · Sebastian Raschke**
> **中文：** 我看不到赢家通吃的局面。想法不会是专有的，实现这些想法所需的方法或资源才是。
> **原文：** I don't think ideas will be proprietary, but the methods or resources needed to implement them will be.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| DeepSeek 时刻 | DeepSeek moment | 中国开源模型以更低成本达到领先性能 |

**本章小结**
- 研究人员流动性强，不会有独家技术赢家
- 区分因素是预算和硬件限制，不是想法
- 中国开源模型生态快速演进，DeepSeek 不再独占鳌头
- 未来几年会出现整合，但2026年不会减少

---

## 02 文本扩散模型与架构演进

**Lex：** 你认为2026年哪个模型会赢？有什么新架构方向？

**Sebastian：** 文本扩散模型是有趣的方向。人们从图像生成中了解扩散模型——迭代去噪产生高质量图像。现在想把这个用于文本，但文本是离散的，不像像素是连续的。文本扩散模型从一些随机文本开始，迭代填补缺失部分，可以同时处理多个 token，更高效。但权衡是：有些任务不是并行的，比如推理任务或工具使用。

**Nathan：** 我听说代码初创公司在使用——你有一个代码库，有人在"氛围编码"，模型需要生成非常长的代码差异。用自回归模型会花数分钟，导致用户流失。扩散模型可以非常快地生成。但它不适合工具使用——Claude Code 和 ChatGPT 的自回归链会被外部工具打断，我不知道如何在扩散设置中做到这一点。

**Lex：** 你认为工具使用的前景如何？

**Sebastian：** 这是一个巨大突破，可以真正将某些任务从记忆外包给实际操作。与其让 LLM 记住 23 加 5 是多少，不如直接用计算器。它能减少幻觉，但不能完全解决——模型仍需知道何时调用工具，互联网也不总是正确的。

**Nathan：** 开放模型和封闭模型使用工具的方式非常不同。开放模型需要对多种工具、多种用例都有用，这很难。封闭模型将特定工具深度整合到体验中——比如引用公共和私人信息的混合，发送到安全云环境执行再返回。这些可能帮助定义开放和封闭的利基市场。

> **金句 · Nathan Lambert**
> **中文：** 开放模型在工具使用上处于劣势，但这将需要一个更灵活、更有趣的模型，成为协调器和工具使用模型。
> **原文：** Open models are at a disadvantage for tool use, but this will require a more flexible, interesting model that becomes a coordinator and tool-use model.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| 文本扩散模型 | text diffusion model | 并行填补缺失token，可能用于快速廉价任务 |
| 递归语言模型 | recursive language model | 分解子任务递归调用，比一次性处理更高效 |

**本章小结**
- 文本扩散模型可能用于快速、廉价的大规模任务，但不适合工具使用
- 递归语言模型将长上下文任务分解为子任务，更高效
- 开放模型在工具使用上处于劣势，封闭模型深度整合特定工具
- 工具使用不能完全解决幻觉，但能减少

---

## 03 持续学习、记忆与长上下文

**Lex：** 持续学习——不断改变权重使模型根据新信息适应——的重要性？

**Nathan：** 这与AGI定义密切相关。语言模型不会像员工那样从反馈中学习。如果我们真的要达到通用适应性智能，需要能够从反馈和在职学习中快速学习。但这也是一种权衡——我们是否需要通过持续学习更新权重？或者我们只需要向模型提供更多上下文和信息？

**Sebastian：** 持续学习我们已经有不同形式了——从GPT-5到5.1和5.2就是精心策划的更新。更细粒度的例子是RLHF。问题是不能为每个人都这样做，因为更新每个人权重太昂贵。除非有设备上的东西，成本由消费者承担，像苹果试图用Apple基础模型做的那样。

**Lex：** 记忆呢？添加记忆的机制有哪些不同的想法？

**Sebastian：** 这很昂贵，因为你必须花费token。你只能做这么多——更像是一种偏好或风格。人们仍然使用LoRA适配器，不是更新整个权重矩阵，而是两个较小的权重矩阵。但这是经济学问题。LoRA学得少但忘得也少，你需要找到那个**金发姑娘区**。

**Nathan：** 普遍接受的观点是，这是计算和数据问题，有时涉及小的架构改进。混合注意力模型——如果你的Transformer中有状态空间模型，它们更适合，因为只需要更少计算来建模最远的token。但我预计上下文长度今年会增加到200万或500万，不会达到1亿。那将是一个真正的突破。

> **金句 · Sebastian Raschke**
> **中文：** 没有免费的午餐。一个极端是RNN，把所有东西塞进一个状态，上下文越长忘记越多；另一个是Transformer，记住每个token，非常昂贵。Nemotron 3找到了很好的比例。
> **原文：** No free lunch. One extreme is RNN with a single state, the other is Transformer remembering every token. Nemotron 3 found a good ratio.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| 持续学习 | continual learning | 权重不断更新适应新信息 |
| 上下文学习 | in-context learning | 通过长上下文窗口加载信息 |
| 金发姑娘区 | Goldilocks zone | 在成本和能力之间找到平衡点 |

**本章小结**
- 持续学习已有不同形式（模型版本更新、RLHF），但为每个人更新权重太昂贵
- 记忆主要通过上下文或LoRA适配器实现，需要找到成本与能力的平衡
- 上下文长度会继续增长，但百万级token仍是挑战
- 递归语言模型和稀疏注意力是处理长上下文的新方向

---

## 04 AGI 时间线与编程自动化

**Lex：** 我们来谈AGI时间线。没有人真正同意AGI和ASI的定义，这是否公平？

**Nathan：** 很多分歧，但很多人说同样的事情——一个可以复制大多数数字经济工作的东西。远程工作者是合理的例子。今天的语言模型功能强大但还不是远程工作者的替代品。

**Lex：** Anthropic的AI27报告关注代码和研究品味——超人程序员→超人AI研究员→超智能AI研究员→完全ASI。他们预测2031年。

**Nathan：** 我觉得AI是"参差不齐"的——在某些方面非常出色，另一些方面非常糟糕。我认为超人程序员几乎是无法实现的，因为能力上总会有差距。这是一种**人机协作**，人类弥补模型无法做到的事情。

**Sebastian：** 我认为编程可能像计算器——你不需要人工计算那个数字。但问题是：你还会让人类要求AI做事情吗？还是会有AI直接建网站？我认为用"搭建网站"讨论太简单了，我宁愿考虑安全关键系统。

**Lex：** 我越来越看好你所阐述的观点。这是一个**人类技能问题**——Anthropic或其他公司正在引领潮流，了解如何最好地利用模型进行编程。有很多程序员还在边缘地带，没有真正好的使用指南。

**Nathan：** Cursor的Composer模型是中国大型专家混合模型之一的微调。他们每90分钟根据用户在现实世界中的反馈更新模型权重——这是模型上最接近真实世界强化学习的实践。

> **金句 · Nathan Lambert**
> **中文：** 我认为软件工程将更多地转向系统设计和结果目标。很难接受软件开发将发生多大变化，以及有多少人可以在不接触代码的情况下完成任务的严重性。
> **原文：** Software engineering will shift toward system design and outcome goals. It's hard to grasp how much software development will change.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| 参差不齐 | jagged | AI在某些方面出色，另一些方面糟糕 |
| 人机协作 | human-AI collaboration | 人类弥补模型弱点，最优秀研究员激活超能力 |
| 规范驱动设计 | spec-driven design | 用自然语言精确指定想要什么 |

**本章小结**
- AGI定义分歧大，但远程工作者替代是合理基准
- AI能力"参差不齐"，超人程序员不太可能完全实现
- 编程自动化是人类技能问题，不是模型能力问题
- Cursor每90分钟更新权重，是最接近真实世界RL的实践

---

## 05 产业格局、开源生态与广告货币化

**Lex：** 你认为今年商业上会有疯狂的大动作吗？比如谷歌或苹果收购Anthropic？

**Nathan：** Dario永远不会出售。但我们开始看到整合——Grok 200亿美元、Scale AI近300亿美元。许可协议并非每个人都能受益，而不是通过完全收购让普通员工的股票归属受益。这种整合趋势将继续。

**Lex：** Anthropic、OpenAI、XAI——它们能如此轻易筹集大量资金，只要融资容易就不觉得有必要上市。

**Nathan：** 他们不会IPO，因为公开市场存在供应压力。我希望更多美国大型AI初创公司上市，因为这样就能看到它们如何花钱，让人们有机会投资。它们是塑造未来的公司。

**Lex：** 你认为OpenAI和Anthropic主要是LLM服务提供商。如果AI变得更加商品化，那些只提供LLM的公司很可能会消亡。

**Sebastian：** 我认为他们会。他们的优势在于拥有大量用户，会转型。Anthropic最初不计划从事代码工作，但碰巧发现这是个好利基市场。

**Lex：** 你提到了Llama的消亡。Meta有获胜的途径吗？

**Nathan：** 我认为没人知道。Llama有点不同——它是该组织最集中的体现。我觉得Meta领导层对Llama感到兴奋，但问题在于试图将开放变现，强行推动它。感觉很勉强，太注重基准测试方面。

**Sebastian：** 我认为我们作为开源社区可能过于严苛了。作为一家公司，他们希望得到积极头条新闻，结果却不是。这导致了一种报复性反应——"我们试图给你一些很酷的东西，但现在你却对我们持负面态度"。

**Lex：** 关于广告——OpenAI试图在2025年推出广告。但问题是他们做不到，因为有不带广告的替代品。

**Nathan：** 广告的提议是通过大量用户赚取巨额资金，投入更好研发。这就是为什么YouTube在任何领域都主导市场。但现在启动这个飞轮令人恐惧，因为它是一项长期投资。

> **金句 · Sebastian Raschke**
> **中文：** 如果每个人都使用相同的LLM，每个人都在同步前进。公司都希望拥有竞争优势，那时就无法避免使用私有数据进行实验和专业化。
> **原文：** If everyone uses the same LLM, everyone is同步前进. Companies want competitive advantage, so specialization with private data becomes inevitable.

**本章概念**
| 中文 | 英文 | 白话 |
|------|------|------|
| 苦涩的教训 | bitter lesson | 计算资源越丰富，能从中获益越多的模型越赢 |
| 人机协作 | human-AI collaboration | 人类与AI各取所长 |

**本章小结**
- AI行业整合趋势开始，许可协议伤害创业生态系统
- 前沿LLM公司不太可能IPO，因为公开市场供应压力
- Llama问题在于强行将开放变现，太注重基准测试
- 广告模式可能成为LLM货币化方向，但启动飞轮令人恐惧
- 中国开放权重模型正在积累力量，美国需要投资开源模型

---

## 附录

### 章节时间戳（专栏 · 重点速览）

| 章 | 主题 | 时间 |
|----|------|------|
| 01 | DeepSeek 时刻与国际竞争格局 | ~00:00 |
| 02 | 文本扩散模型与架构演进 | ~30:00 |
| 03 | 持续学习、记忆与长上下文 | ~55:00 |
| 04 | AGI 时间线与编程自动化 | ~80:00 |
| 05 | 产业格局、开源生态与广告货币化 | ~100:00 |

### 素材与收录

- **专栏（S 主源）：** [cv45480286](https://www.bilibili.com/read/cv45480286/)
- **视频：** [BV1ArFCz5EjX](https://www.bilibili.com/video/BV1ArFCz5EjX/)
- **ingest：** `Recastory/workspace/bilibili-retranscribe/BV1ArFCz5EjX/ingest/column_article.md`
- **形态：** 1 BV = 1 篇 canonical；`material_tier: S` · `dialogue_version: v3.2`

### 相关阅读

- [[MOC - Agent Theory and Design]] — Agent 理论与设计主题索引
- [[MOC - Harness Engineering]] — Harness 工程主题索引
