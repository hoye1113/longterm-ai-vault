---
title: "Nebius联创：AI基建无泡沫 全栈交付是关键"
source:
  - "B站视频 - Easonlee的AI笔记"
  - https://www.bilibili.com/video/BV1F8Ju6VEbp/
source_url: "https://www.bilibili.com/video/BV1F8Ju6VEbp/"
column_url: "https://www.bilibili.com/read/cv50566051/"
source_original: "The Twenty Minute VC · Harry Stebbings × Roman Chernin"
source_original_date: 2026-06-05
host_name: "Harry Stebbings"
guest_name: "Roman Chernin"
guest_title: "Nebius Co-founder"
material_tier: S
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV1F8Ju6VEbp/ingest"
speaker: "Harry Stebbings / Roman Chernin"
duration: "~45:00"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "Harry Stebbings × Nebius联创Roman Chernin：AI基建非泡沫、开源vs闭源模型、四层产品堆栈、托管推理平台、资本支出护城河、世界过度整合威胁。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1F8Ju6VEbp/article.md"
column_source: "Recastory/workspace/bilibili-retranscribe/BV1F8Ju6VEbp/ingest/column_article.md"
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: Host-Guest canonical
speaker_inference: "column_article（S 级专栏图稿，Host/Guest 已标注）"
speaker_confidence: high
uploader: Easonlee的AI笔记
tags:
  - ai_agent
  - ai_coding
  - ai_career
  - bilibili
  - video_transcript
concepts:
  - id: ai_infra_no_bubble
    zh: AI基建非泡沫
    en: AI infrastructure is not a bubble
    one_line: 第一个大规模成功用例刚出现几个月，需求远未饱和
  - id: open_vs_closed_models
    zh: 开源vs闭源模型
    en: open-source vs closed-source models
    one_line: 客户达到规模后为经济效益和微调能力转向开源
  - id: four_layer_stack
    zh: 四层产品堆栈
    en: four-layer product stack
    one_line: 容量→托管云→托管推理→代理工作流，堆栈越高客户越广
  - id: managed_inference_platform
    zh: 托管推理平台
    en: managed inference platform
    one_line: 开发者关注业务逻辑而非底层GPU型号
  - id: capex_moat
    zh: 资本支出护城河
    en: capex as moat
    one_line: 做好你的工作是唯一护城河，工程层面的互相尊重
  - id: world_overconsolidation_threat
    zh: 世界过度整合威胁
    en: world overconsolidation threat
    one_line: 被少数超级帝国控制会扼杀多样性
---

# Nebius联创：AI基建无泡沫 全栈交付是关键

**Host：** Harry Stebbings（The Twenty Minute VC 播客主持人）  
**Guest：** Roman Chernin（Nebius Co-founder）  
**形态：** Host-Guest 对谈稿 v3.2（S 级 · 专栏主源 · 中文口语化）  
**主源：** Recastory `BV1F8Ju6VEbp/ingest/column_article.md`  
**B 站：** [BV1F8Ju6VEbp](https://www.bilibili.com/video/BV1F8Ju6VEbp/) · **专栏：** [cv50566051](https://www.bilibili.com/read/cv50566051/) · **时长** ~45:00

---

## 开场

AI 基础设施竞赛已经开始，资本支出从未如此之高。Nebius 市值已达 660 亿美元，正与超大规模厂商正面竞争。联合创始人 Roman Chernin 在 Harry Stebbings 的播客中直言：AI 基建不是泡沫，编程用例几个月前才真正奏效，全球绝大多数企业的 AI 应用占比极低。Nebius 从容量到代理工作流构建四层堆栈，通过全栈集成策略——向下深入物理世界构建数据中心，向上紧贴客户需求做产品——在 24 个月时间跨度内寻找差异化。而 Roman 最担心的不是竞争，是世界过度整合。

**术语速查（后文对话用中文；英文原文在此统一对照解读）**

| 中文 | 英文 | 白话 |
|------|------|------|
| 杰文斯悖论 | Jevons paradox | 效率提高→成本降低→需求反而增加 |
| 四层产品堆栈 | four-layer product stack | 容量→托管云→托管推理→代理工作流 |
| 托管推理 | managed inference | 平台帮开发者跑模型，按 token 收费 |
| Token Factory | Token Factory | Nebius 的托管推理产品 |
| 全栈集成 | full-stack integration | 向下控制硬件，向上做产品服务 |
| 资本支出 | capital expenditure (capex) | 建数据中心、买 GPU 的投入 |
| 推测解码 | speculative decoding | 用小模型加速大模型推理的技术 |
| 蒸馏 | distillation | 把大模型的能力压缩进小模型 |
| TCO | total cost of ownership | 总拥有成本，含运维和优化 |
| 冷启动 | cold start | 企业从零搭建 AI 基础设施的初始阶段 |

---

## 01 AI基础设施并非泡沫

**Harry Stebbings：** 我们在 AI 基础设施的切入点上处于什么位置？很多人看到资本不断涌入，就认为这是一个泡沫。

**Roman Chernin：** 不，我不认为这是一个泡沫。我认为我们正处于这个激动人心时刻的开端，黄仁勋称之为「有用的 AI」，我们才刚刚开始真正的应用。在众多用例中，我们可能只有一个用例是真正成功的。而这个成功的用例——编程——可能也只是几个月前才开始真正见效的。

**Harry Stebbings：** 但如果我只是完全同意你的观点，那讨论就太无聊了。

**Roman Chernin：** 如果你审视当今世界上绝大多数公司，你会发现他们在 AI 的应用上，无论是应用数量还是用例深度，都只占了很小一部分。即便是一些技术相当先进的大公司，你会发现他们也才刚刚起步。由此我得出结论，我们才刚刚开始。

> **金句 · Roman Chernin**
> **中文：** 距离第一个大规模成功的用例出现并开始广泛应用，才仅仅过了几个月。我认为未来我们将看到更多用例，也将看到更广泛的应用。
> **原文：** It's been only months since the first large-scale successful use case emerged and started being widely adopted. I think we'll see more use cases and broader adoption going forward.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 有用的AI | useful AI | AI从实验进入实际生产 |
| 杰文斯悖论 | Jevons paradox | 更便宜→用更多→总需求反增 |
| 第一个成功用例 | first successful use case | 编程——几个月前才真正奏效 |

**本章小结**

- AI 基建不是泡沫，编程等用例几个月前才真正见效
- 全球绝大多数企业的 AI 应用占比极低，需求远未饱和
- 单位智能成本降低会因杰文斯悖论推动需求指数增长

---

## 02 开源模型与前沿模型的博弈

**Harry Stebbings：** 既然你看到编程在过去六到十二个月中开始奏效，那么是否会有一种趋势，即我们将转向本地托管的开源模型？

**Roman Chernin：** 是的，首先我认为这并非未来，它已经存在于当下。我们看到很多例子，当我们的客户或产品开发者达到一定规模时，他们会开始寻找提高经济效益或加速增长的方法。最好的构建方式显然是基于 OpenAI、Anthropic、Google 等优秀提供商的前沿模型。但是，当你理清了用例，开始看到实际应用并拥有了客户数据循环时，你也许可以找到更便宜，甚至不只是更便宜，而是更高质量的方式来服务相同的用例。

**Harry Stebbings：** 你是否认为这些公司在很多情况下定价已经过高了？

**Roman Chernin：** 实际上，大多数人更关心另一方面，即我们是否会有足够强大的开源环境和足够专业的模型生态来构建基础？我认为我们还处于采用的早期阶段。在 15 个月前的 DeepSeek 时刻，Nebius 的股价在一周内下跌了 40%。但就在同一周，我们创造了公司历史上最好的销售周。

> **金句 · Roman Chernin**
> **中文：** 每次单位智能变得更便宜时，情况就会发生变化。我们并没有减少消耗，反而增加了消耗。因为我们可以用相同的预算解决更复杂的任务。
> **原文：** Every time unit intelligence becomes cheaper, things change. We don't consume less, we consume more. Because we can solve more complex tasks with the same budget.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 可微调 | fine-tunable | 开源模型可以针对特定场景优化 |
| 前沿模型 | frontier models | 最强的闭源模型 |
| DeepSeek时刻 | DeepSeek moment | 更便宜的模型反而带来更多需求 |
| 经济效益 | unit economics | 每个 token 的成本和价值 |

**本章小结**

- 开源不是未来，是当下——客户达到规模后自然转向可微调模型
- 闭源前沿模型仍有广阔市场，总有更复杂的任务需要攻克
- DeepSeek 时刻证明：更便宜的模型带来的是更多需求，不是泡沫

---

## 03 四层产品堆栈

**Harry Stebbings：** 你在哪些方面觉得行动不够快？

**Roman Chernin：** 我们从四个维度来讨论。第一是容量——我们部署了多少兆瓦和 GPU。第二是产品。第三是客户——我们是现场业务。第四是资本。

**Harry Stebbings：** 既然容量翻十倍，你能一夜之间卖掉吗？

**Roman Chernin：** 不是一夜之间，但我们肯定有需求。关键问题不是是否有需求，而是我们如何构建需求组合。在裸机层面，你可能只有十几家客户可以合作；在托管基础设施方面，有数百家；在推理方面，有数千家；在 Agentic 方面，将有成千上万的新开发者。

> **金句 · Roman Chernin**
> **中文：** 我们相信，堆栈越高，为客户创造的潜在价值就越大。实际上，堆栈越高，我们能服务的客户群体就越广。
> **原文：** We believe the higher in the stack, the more potential value we create for customers. In fact, the higher in the stack, the broader the customer base we can serve.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 裸机 | bare metal | 纯物理服务器，客户自己部署一切 |
| 托管云 | managed cloud | IaaS，带虚拟化和API |
| 托管推理 | managed inference | 按 token 收费的模型运行服务 |
| 代理工作流 | agentic workflows | 端到端任务自动执行 |
| 售后业务 | after-sales business | 云业务本质——销售是承诺，交付才是开始 |

**本章小结**

- 四层堆栈从兆瓦→GPU小时→token→端到端任务，客户群指数扩大
- 堆栈越高，价值越大，但需要不同的工程能力
- 容量是基础，但真正的护城河在产品和客户关系

---

## 04 托管推理与Token Factory

**Harry Stebbings：** 你提到了四层堆栈中的第三层是托管推理。对于不理解的人来说，你如何看待这一层？

**Roman Chernin：** 你用代码构建了你的产品，用 OpenAI 构建了优秀的业务。唯一的问题可能是你没有足够的利润，或者你想更积极地应用数据并调整模型的行为。于是你从 Hugging Face 获取权重，使用 vLLM 来运行它，然后它就不工作了，因为你还没能真正提取出你期望的价值。

**Harry Stebbings：** 通过 Token Factory，你可以在 60 个开源模型上运行。你之前说过，通过优化可以将推理成本降低多达 70%。你到底是如何让一个 token 变得更便宜的？

**Roman Chernin：** 你可以做模型蒸馏，制作一个质量相同但更小的模型；你可以做推测解码，可以优化缓存。模型每周、每月都在变化。每次发布新模型时，它可能在某些基准测试中表现更好。你希望拥有灵活性，希望有人支持你进行实验。

> **金句 · Roman Chernin**
> **中文：** 开发者不应关注底层 GPU 型号或 VLLM 优化，而应关注业务逻辑。Nebius 的 Token Factory 通过蒸馏、推测解码等技术优化，能将推理成本降低 70%。
> **原文：** Developers shouldn't focus on the underlying GPU型号 or VLLM optimization, but on business logic. Nebius's Token Factory optimizes through distillation, speculative decoding and other techniques, reducing inference costs by 70%.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| Token Factory | Token Factory | Nebius 的托管推理产品 |
| 蒸馏 | distillation | 大模型能力压缩进小模型 |
| 推测解码 | speculative decoding | 小模型草稿+大模型验证加速推理 |
| 模型飞轮 | model flywheel | 推理→生成数据→改进模型→更好推理 |

**本章小结**

- 托管推理让开发者关注业务逻辑而非基础设施
- 蒸馏+推测解码+缓存优化可降低 70% 推理成本
- 模型迭代极快，平台抽象帮助客户始终用最新最优模型

---

## 05 资本支出与护城河

**Harry Stebbings：** 当人们将你们与其他新晋云服务商比较时，通常会提到 CoreWeave。区别在哪里？

**Roman Chernin：** 我们构建的原则是「全栈」。向下全栈意味着我们深入物理世界，构建数据中心、机架和服务器。当你控制这些底层环节时，你可以行动得更快，进一步压缩成本。上游的垂直整合就是产品——我们要紧跟客户需求和细分市场。

**Harry Stebbings：** 与英伟达关系中的权力动态如何？

**Roman Chernin：** 我们以非常简单的方式看待这个问题。我认为英伟达最令人着迷的地方在于，它在很大程度上仍然是一家工程师驱动的公司。要赢得英伟达的尊重，最好的方式就是如果英伟达的工程师尊重你的工程师，你就会拥有正确的关系基础。

> **金句 · Roman Chernin**
> **中文：** 做好你的工作是唯一护城河。我们正处于资本密集型的游戏中，正在与世界上资本最雄厚的公司竞争。
> **原文：** Doing your job well is the only moat. We're in a capital-intensive game, competing against the deepest pockets in the world.

> **金句 · Roman Chernin**
> **中文：** 整合是我们主要的威胁。世界越民主化、越多样化，我们作为企业就越被需要。
> **原文：** Consolidation is our main threat. The more democratic and diverse the world is, the more needed we are as a company.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 全栈集成 | full-stack integration | 向下控制硬件，向上做产品 |
| 工程师驱动 | engineer-driven | 公司决策由技术能力而非销售驱动 |
| 过度整合 | overconsolidation | 少数巨头控制一切，扼杀多样性 |

**本章小结**

- 全栈集成：向下控制数据中心和硬件，向上做产品
- 与英伟达的关系基础是工程师之间的互相尊重
- 24 个月时间跨度内资本可以解锁容量，但执行力才是关键
- Roman 最担心的不是竞争，是世界过度整合

---

## 附录

### 时间戳索引

| 章节 | 主题 | 时间 |
|------|------|------|
| 01 | AI基建非泡沫 | [03:15] |
| 02 | 开源vs闭源模型 | [06:42] |
| 03 | 四层产品堆栈 | [11:50] |
| 04 | 托管推理平台 | [24:15] |
| 05 | 资本支出护城河 | [35:40] |
| 06 | 世界过度整合威胁 | [41:10] |

### 素材信息

| 字段 | 值 |
|------|-----|
| BV 号 | BV1F8Ju6VEbp |
| 专栏链接 | https://www.bilibili.com/read/cv50566051/ |
| 来源作者 | Easonlee的AI笔记 |
| 形态 | 专栏完整图稿（Quill Delta → Markdown） |
| 时长 | ~45:00 |
| Host | Harry Stebbings（The Twenty Minute VC 播客） |
| Guest | Roman Chernin（Nebius Co-founder） |

### 相关阅读

- [[MOC - Agent Theory and Design]]
- [[MOC - Harness Engineering]]
