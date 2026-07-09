---
title: "Postgres之父：LLM不会取代关系数据库"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1rh526BEjY/"
column_url: "https://www.bilibili.com/read/cv49010546/"
host_name: "Ryan Peterman"
guest_name: "Mike Stonebraker"
guest_title: "图灵奖得主，Ingres & Postgres 创建者"
material_tier: S
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV1rh526BEjY/ingest"
speaker: "Mike Stonebraker"
duration: "~60:00"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "图灵奖得主 Mike Stonebraker 剖析数据库演进史，辛辣点评 Google MapReduce 与最终一致性的错误，用 Beaver 基准测试证明 LLM 在真实数据仓库任务中准确率为 0%，并提出万物皆 SQL 是解决复杂查询的唯一可行路径。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1rh526BEjY/ingest/column_article.md"
column_source: "Recastory/workspace/bilibili-retranscribe/BV1rh526BEjY/ingest/column_article.md"
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: Host-Guest canonical (interview)
speaker_inference: "column interview"
speaker_confidence: high
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - ai_coding
author:
  - "[[Mike Stonebraker]]"
concepts:
  - id: no_silver_bullet_db
    zh: 数据库无一刀切
    en: no one-size-fits-all DB
    one_line: 专用引擎比通用数据库快一个数量级
  - id: eventual_consistency_wrong
    zh: 最终一致性的错误
    en: eventual consistency mistake
    one_line: 为性能牺牲正确性，大多数企业无法容忍
  - id: llm_zero_percent
    zh: LLM 真实任务准确率 0%
    en: LLM 0% on real tasks
    one_line: 在生产数据仓库基准测试中，LLM Text-to-SQL 几乎为零
  - id: everything_is_sql
    zh: 万物皆 SQL
    en: everything is SQL
    one_line: 将异构数据映射为关系表，用查询优化器连接
  - id: dbos
    zh: DBOS：数据库重构操作系统
    en: DBOS
    one_line: 用数据库技术替换 OS 上半部分，文件系统比 Linux 更快
  - id: beaver_benchmark
    zh: Beaver 基准测试
    en: Beaver benchmark
    one_line: 四个真实生产数据仓库的匿名基准，LLM 得分 0%
---

# Postgres之父：LLM不会取代关系数据库

**Host：** Ryan Peterman  
**Guest：** Mike Stonebraker（图灵奖得主，Ingres & Postgres 创建者）  
**形态：** Host-Guest canonical v3.2（**专栏主源** · 深度访谈）  
**B 站：** [BV1rh526BEjY](https://www.bilibili.com/video/BV1rh526BEjY/) · **时长** ~60 min

---

## 开场

Ryan Peterman 与图灵奖得主 Mike Stonebraker 深度对谈：从 Ingres 和 Postgres 的诞生故事，到 Google MapReduce 与最终一致性的错误判断，再到 DBOS 用数据库重构操作系统的实验。Stonebraker 用 Beaver 基准测试证明，LLM 在真实生产数据仓库的 Text-to-SQL 任务中准确率几乎为 0%——真实模式的混乱、百行 SQL 的复杂度和非公开业务逻辑，与 LLM 训练集中的干净样本完全不同。

**术语速查**

| 中文 | 英文 | 白话 |
|------|------|------|
| 一刀切 | one-size-fits-all | 通用数据库在所有场景都不是最优 |
| 最终一致性 | eventual consistency | 异步同步副本，可能短暂不一致 |
| Text-to-SQL | text-to-SQL | 用自然语言生成 SQL 查询 |
| Beaver 基准 | Beaver benchmark | 四个真实生产数据仓库的匿名基准 |
| DBOS | database OS | 用数据库技术替换操作系统上半部分 |
| 万物皆 SQL | everything is SQL | 将所有异构数据映射为关系表 |

---

## 01 Ingres 的诞生：从学术原型到商业公司

**Ryan Peterman：** 你是如何开始构建数据库系统的？

**Mike Stonebraker：** 1971 年，吉恩·王把我带到他的门下，说"我们一起做点什么吧"。当时竞争对手是 Codicil 提案（低级的意大利面条式网络）和 IBM 的 IMS（分层树状结构）。Ted Codd 的关系模型完全合理，所以我们决定构建 Ingres。

我们投入最初的 90% 让它运行起来，然后又投入接下来的 90% 让它真正工作。加州大学版本的 Ingres 在 100 所大学运行，因为它在 Unix 上免费。但亚利桑那州立大学考虑使用时，发现没有 COBOL——他们是一个 COBOL 商店。不受支持的操作系统，不受支持的数据库系统，没有 COBOL，注定我们无关紧要。唯一的出路就是创办一家公司。

**Ryan Peterman：** Oracle 是怎么竞争的？

**Mike Stonebraker：** 拉里·埃里森是一位出色的销售员，他让现在时和将来时变得难以区分。他基本上对客户撒谎，发布不起作用的东西并让客户帮他调试。Oracle 写了两页手册定义参照完整性，底部写着"尚未实现"——而 Ingres 早就实现了。**对客户撒谎，我认为是不道德的。**

> **金句 · Mike Stonebraker**
> **中文：** 拉里·埃里森让现在时和将来时难以区分；Oracle 写了参照完整性的定义，底部写着"尚未实现"。
> **原文：** Larry Ellison made it hard to distinguish present tense from future tense — Oracle wrote the referential integrity definition with "not yet implemented" at the bottom.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 关系模型 | relational model | Ted Codd 的理论基础 |
| 参照完整性 | referential integrity | 删除员工时部门该何去何从 |
| 商业化困境 | commercialization gap | 没有 COBOL 就无法进入企业市场 |

**本章小结**

- Ingres 从伯克利学术项目起步，因缺少 COBOL 被迫商业化
- Oracle 通过销售策略而非技术优势竞争
- 参照完整性等核心功能 Ingres 领先 Oracle 数年

---

## 02 Postgres 的技术创新：可扩展类型系统

**Ryan Peterman：** Ingres 没有做而 Postgres 会做的是什么？

**Mike Stonebraker：** 最初的理由是支持地理信息系统——需要点、线、多边形等类型，Ingres 做不到。另一个故事：1985 年，一个客户处理债券金融工具，他想按自己的日历定义做日期减法（每月 30 天），但公历实现不允许。他必须把两个日期检索到用户代码中做减法，效率降低了两到三倍。

他问："为什么我不能用我想要的方式重载你的减法定义？"问题在于，你想要债券时间，就像你想要点、线和多边形一样。**Postgres 被设计成具有可扩展的类型系统**，你可以拥有任何你想要的数据类型，而且它们非常高效。

> **金句 · Mike Stonebraker**
> **中文：** Postgres 的主要精髓是可扩展的类型系统——你可以拥有任何你想要的数据类型。
> **原文：** The main essence of Postgres is its extensible type system — you can have any data type you want.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 可扩展类型 | extensible types | 用户自定义数据类型 |
| 抽象数据类型 | abstract data types | GIS/债券时间等专用类型 |
| 继承 | inheritance | Postgres 支持类型继承（后移除） |

**本章小结**

- Postgres 的核心创新是可扩展类型系统
- 从 GIS 到金融工具，专用数据类型的需求推动了架构设计
- 类型系统的灵活性使 Postgres 传播到远超商业数据处理的领域

---

## 03 数据库无一刀切：专用引擎快一个数量级

**Ryan Peterman：** 你认为一刀切的数据库系统并非最优？

**Mike Stonebraker：** 流处理引擎、列式存储数据仓库、向量处理——它们彼此之间没有任何相似之处，在各自场景下都比通用数据库快一个数量级。Postgres 选择不实现列式存储和多节点支持，所以在大型数据仓库方面没有竞争力。

在低端——你有一个数据库问题——答案是选择 Postgres。庞大的编程社区，各种数据类型实现，免费，人才容易找到。在你尝试每秒处理一百万次事务之前，在你尝试支持一个 PB 级数据仓库之前，它都能正常工作。**在低端，它是 Postgres。在高端，那就不对了。**

> **金句 · Mike Stonebraker**
> **中文：** 在低端，它是 Postgres。在高端，那就不对了——专用引擎快一个数量级。
> **原文：** At the low end, it's Postgres. At the high end, that's not right — purpose-built engines are an order of magnitude faster.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 列式存储 | columnar storage | Vertica 等数据仓库引擎 |
| 多节点 | multi-node | PB 级数据仓库的必备能力 |
| 数量级差距 | order of magnitude | 专用 vs 通用的性能鸿沟 |

**本章小结**

- 专用引擎（流处理/列式/向量）比通用数据库快一个数量级
- Postgres 是低端万能选择，但高端需要专用方案
- 数据库不存在一刀切的最优解

---

## 04 批判 Google：MapReduce 与最终一致性的错误

**Ryan Peterman：** 你为什么如此不认同 MapReduce？

**Mike Stonebraker：** 很多不明智的人说"谷歌很聪明，他们一定知道他们在做什么"。但 Hadoop 效率低得离谱——我们 2011 年的论文用分布式数据库系统击败了 Hadoop。但这并不是谷歌唯一愚蠢的地方——他们还认为最终一致性是实现并发控制的正确方法。

假设东海岸和西海岸仓库各有最后一个小部件。如果你允许最终一致性，两个仓库同时卖出最后一个，最终状态将是负一——有人拿不到小部件。大多数企业无法容忍库存为负。**最终一致性根本行不通。**

谷歌的杰夫·迪恩最终明白了这一点，当他们开发 Spanner 时，采用的是传统的事务系统。谷歌完全放弃了最终一致性，也完全放弃了 MapReduce。这是性能与数据完整性的权衡——如果你不在乎你的数据，你才愿意处理糟糕的事情发生。

> **金句 · Mike Stonebraker**
> **中文：** 最终一致性根本行不通——大多数企业无法容忍库存为负。谷歌最终回归了传统事务系统。
> **原文：** Eventual consistency simply doesn't work — most businesses can't tolerate negative inventory. Google eventually returned to traditional transaction systems.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| MapReduce | MapReduce | Google 早期推崇，效率极低 |
| 最终一致性 | eventual consistency | 异步同步可能产生数据错误 |
| Spanner | Spanner | Google 回归传统事务的正确路径 |
| 数据完整性 | data correctness | 性能不能以正确性为代价 |

**本章小结**

- MapReduce 效率极低，被分布式数据库系统轻松击败
- 最终一致性牺牲正确性换取性能，大多数企业无法容忍
- Google 自己最终回归了传统事务系统（Spanner）

---

## 05 DBOS：用数据库技术重构操作系统

**Ryan Peterman：** DBOS 是什么？

**Mike Stonebraker：** Databricks 的创始人 Mate Zaharia 说，他们在任何给定时间协调一百万个 Spark 作业，尝试了所有操作系统人员编写的调度器，都无法扩展。于是他们把所有调度数据放在一个 Postgres 数据库中——它就突然明白了。

核心思想是：**你在操作系统中做的几乎所有事情都是大规模管理数据，你应该使用数据库技术来做这件事。** 在 DBMS 之上编写的文件系统比 Linux 文件系统更快。调度引擎具有竞争力。你可以让所有东西都故障转移，获得高可用性。

我们和风险投资家谈，他们异口同声地说"如果你认为你能取代 Linux，那简直是痴人说梦"。但编程语言扩展真的很棒——TypeScript、Java、Go、Python 版本都有。DBOS 支持事务性工作流：**工作流需要是原子性的，这意味着它要么全部发生，要么看起来从未发生过**。目前约三分之二的客户正在进行代理式 AI 应用。

> **金句 · Mike Stonebraker**
> **中文：** 你在操作系统中做的几乎所有事情都是大规模管理数据——你应该用数据库技术来做。
> **原文：** Almost everything you do in an operating system is large-scale data management — you should use database technology to do it.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| DBOS | database OS | 用数据库替换 OS 上半部分 |
| 事务性工作流 | transactional workflow | 原子性：要么全做要么全不做 |
| 代理式 AI | agentic AI | LLM + 信号增强的读写应用 |
| 故障转移 | failover | 数据库自带高可用 |

**本章小结**

- DBOS 证明数据库技术可以替换 OS 核心功能
- 文件系统比 Linux 更快，调度引擎具有竞争力
- 代理式 AI 从只读走向读写，需要事务性工作流的原子性保证

---

## 06 LLM 在真实数据仓库任务中表现为 0%

**Ryan Peterman：** Text-to-SQL 的现状如何？

**Mike Stonebraker：** 在 Spider 和 Bird 基准上，最好的 LLM 系统准确率约 85%——看起来不错。但在我们的 **Beaver 基准测试**中——四个真实生产数据仓库——LLM 的准确率是 **0%**。用 RAG 增强后达到 10%，如果把 FROM 子句作为提示给它，达到 35%。

区别在哪？第一，数据仓库数据不在"堆栈"上，LLM 没训练过。第二，真实查询 100 行 SQL，Spider/Bird 只有 10-20 行。第三，真实模式一团糟——表名不助记、列名是下划线Z、物化视图导致冗余。**这些东西的定义是还没有准备好投入使用。**

**Ryan Peterman：** 人类程序员能得多少分？

**Mike Stonebraker：** 一旦你消除了文本的歧义，一个了解 SQL 的程序员，如果知道模式，会获得非常高的准确率——至少 90%。

> **金句 · Mike Stonebraker**
> **中文：** LLM 在真实数据仓库任务中得分 0%——模式一团糟，查询 100 行，不在训练集里。
> **原文：** LLMs score 0% on real data warehouse tasks — schemas are a mess, queries are 100 lines, and it's not in the training set.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| Beaver 基准 | Beaver benchmark | 四个真实生产数据仓库 |
| 0% 准确率 | 0% accuracy | LLM 在真实场景完全失败 |
| 模式混乱 | schema mess | 表名不助记、冗余、特殊日期 |
| 业务逻辑 | business logic | 查询依赖非公开的领域知识 |

**本章小结**

- LLM 在干净基准上 85%，在真实数据仓库上 0%
- 原因：训练数据不含仓库数据、查询复杂度差距、模式混乱
- 人类程序员了解模式后准确率可达 90%+

---

## 07 万物皆 SQL：解决复杂查询的唯一路径

**Ryan Peterman：** 面对跨系统的复杂查询怎么办？

**Mike Stonebraker：** 慕尼黑市交通部有六名全职人员处理市民投诉。他们的数据库是：电车时刻表（SQL）、灯光序列（SQL）、交叉路口（CAD）、联邦规定（文本）、本地规定（文本）。你连接了 SQL、SQL、CAD、文本和文本。

**我们的观点是，把所有东西都变成 SQL，都变成表格，然后用查询优化器进行连接。** 使用 LLM 进行结构化数据连接是一个糟糕的主意——你最好把它们保留为表，然后在 SQL 中进行连接。一旦这变成读写操作，它就成了分布式数据库问题，你需要原子性、一致性等等。

> **金句 · Mike Stonebraker**
> **中文：** 把所有东西都变成表格，然后用查询优化器连接——这是处理严谨场景的唯一可行方案。
> **原文：** Turn everything into tables, then join them with a query optimizer — the only viable approach for serious scenarios.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 万物皆 SQL | everything is SQL | 异构数据统一为关系表 |
| 查询优化器 | query optimizer | 连接多源数据的核心引擎 |
| 读写代理 | read-write agents | 从只读走向需要事务保证 |

**本章小结**

- 复杂查询涉及 SQL + CAD + 文本等多种异构数据
- 解决路径：将所有数据映射为关系表，用查询优化器连接
- LLM 不适合做结构化数据连接，保留为表用 SQL 更可靠

---

## 08 职业建议：追随热情，钱自然会来

**Ryan Peterman：** 你会给刚毕业的自己什么建议？

**Mike Stonebraker：** 当初我们在伯克利对数据库一无所知，就说"我们来写一个数据库系统吧"。一开始做那么疯狂的事情，确实是相当疯狂。但你努力，让事情成功，一路学习。**跳出思维定势，想些疯狂的点子，然后尝试去实现它们。**

我不确定我会推荐 18 岁的年轻人主修计算机科学——我认为医疗保健和建筑行业是稳妥的选择。如果你即将获得博士学位，选择一个不随大流的领域。我和我妻子都说"追随你的热情，钱自然会来"——我一分钟都不相信这话。但我真的喜欢我所做的事情，我赚不赚钱都无所谓。

> **金句 · Mike Stonebraker**
> **中文：** 跳出思维定势，想些疯狂的点子，然后尝试去实现它们。
> **原文：** Think outside the box, come up with crazy ideas, and try to implement them.

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 逆流而上 | go against the tide | 选非热门领域突破 |
| 热情驱动 | passion-driven | 做热爱的事，不会饿死 |
| 疯狂点子 | crazy ideas | 伟大项目往往始于疯狂想法 |

**本章小结**

- 伟大项目始于疯狂想法和一无所知时的勇气
- 不随大流选非热门领域，更容易做出突破
- 做热爱的事比追求高薪更可能带来长期满足

---

## 总结

| 维度 | 要点 |
|------|------|
| 起源 | Ingres 从学术到商业化，Oracle 靠销售策略竞争 |
| 创新 | Postgres 可扩展类型系统是核心突破 |
| 架构 | 无一刀切；专用引擎快一个数量级 |
| Google | MapReduce 低效 + 最终一致性错误 |
| DBOS | 数据库重构 OS，文件系统比 Linux 更快 |
| LLM | 真实数据仓库准确率 0%，模式混乱是根本原因 |
| 路径 | 万物皆 SQL，查询优化器连接异构数据 |

---

## 附录

### 章节时间戳（视频简介）

| 时间 | 主题 |
|------|------|
| 18:45 | 数据库无一刀切 |
| 24:12 | 批判 Google MapReduce 与最终一致性 |
| 33:50 | DBOS：用数据库重构操作系统 |
| 44:30 | LLM 在真实数据仓库任务中 0% |
| 49:15 | 万物皆 SQL |
| 54:20 | 计算机科学可能不再是增长型行业 |

### Ingest

- BV：`BV1rh526BEjY`
- ingest：`Recastory/workspace/bilibili-retranscribe/BV1rh526BEjY/ingest`
- 专栏：`.../ingest/column_article.md`

### 相关阅读

- [[MOC - Agent Theory and Design]] — AI Agent 主题入口
- [[MOC - Harness Engineering]] — Harness 工程入口
- [[C++之父-AI代码的局限性]] — AI 代码局限性的系统编程视角
