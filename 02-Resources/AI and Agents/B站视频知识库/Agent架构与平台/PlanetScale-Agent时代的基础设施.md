---
title: "PlanetScale：Agent 时代的基础设施"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1ZWTL64Erg/"
speaker: "Sam Shank (PlanetScale CEO)"
duration: "25:40"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - cursor
  - harness_engineering
created: 2026-07-02
description: "PlanetScale CEO Sam 用 Cursor Agent 现场演示：慢查询优化、危险 schema 拦截、秒级 Rewind、在线分片；核心论题是 infra 必须 safe by default，把 DBA 经验封装成 narrow tools。"
transcript_source: "Recastory/A3-planetscale-agent/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# PlanetScale：Agent 时代的基础设施

## 先搞懂这一期

**这是什么节目？**  
PlanetScale CEO **Sam Shank** 在 AI Engineer 类会议上的主题演讲，约 26 分钟。PlanetScale 是云数据库公司（Vitess 分片、Postgres 等），Cursor 也是它的客户。Sam 整场 **几乎完全靠 Cursor Agent 做 live demo**——每次彩排路径不同，但都能到目标。

**这期在回答哪三个问题？**

1. **Agent 要改线上数据库，基础设施得长什么样？** 不能指望 Agent 永远做对——平台怎么兜底？
2. **Day one 建应用很容易，真正的难点在哪？** 和「快速 spin up sandbox」的行业 obsession 有什么关系？
3. **Cursor 这类 coding Agent 和 infra 平台怎么配合？** 谁负责 refactor query、谁负责 safe deploy？

**用一条线串起来（没看视频也能复述）：**

Sam 开了一家慢得要命的 demo 电商（Sam's Sofa），数据库在 PlanetScale 上，query 平均 4 秒。他在 Cursor 里让 Agent 读 PlanetScale 的优化建议、加 index、开 Deploy Request——站点变快了。一个「坏 Agent」试图 drop column，**平台扫描 in-flight queries 后 reject**；另一个被故意放行 push 坏变更，生产挂了，Sam 点 **Schema Rewind**，秒级恢复、中间写入不丢。流量涨后垂直扩展到头，再 demo **3 节点→16 shard 在线分片**，Cursor 帮改 query 避开慢 scatter-gather join。

Sam 的论题：**Agent 非确定性，infra 必须 safe by default**——把 DBA 几十年经验封装成 **small sharp tools**（branch、Deploy Request、rewind、traffic control、backpressure），别把整个 log 流丢给模型。Day one 容易，**长期维护 living production** 才是 infra 主战场。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Agent 能写代码、调 API | **Infra 平台** 要为 Agent 设计：branch、diff、reject、rewind、audit |
| 数据库变更 = DBA 手工操作 | Agent 改 schema 要有 **Deploy Request**（类 PR）+ 自动 break-query 检测 |
| 搞砸了 restore snapshot | **Schema Rewind**：flip 回上一版本，**不丢中间写入**，与表大小无关 |
| Cursor = 写应用代码 | Cursor 也能扛 **query refactor**（分片后加 shard key routing） |
| 模型越强 Agent 越安全 | **Narrow composable tools** 降歧义；组合扩展智能，风险不必线性涨 |

---

## 分话题讲

### 1. Agent 非确定性，平台必须 safe by default

**说法：**  
Sam 全程用 Agent 做 demo，每次彩排路径不同——「agents are non-deterministic」。PlanetScale 是高可用服务，**可能直接 block Agent 操作**。行业 horror story 是 Agent 搞坏数据库；本场展示 **拦截坏变更** 与 **快速 undo** 两面。

Demo 里还故意加了 prompt 让 Agent 做坏事——有的被拦，有的被放行以演示 rewind。

**和你何干：**  
如果你让 Agent 碰生产 infra（DB、K8s、云资源），assume 它会犯错，平台要有 veto 和 undo。

---

### 2. 现场 demo 第一段：Cursor Agent 优化慢 DB

**说法：**  
Sam's Sofa 电商站（Cloudflare 托管）：order rate OK，但 **query 平均 ~4s、max ~5s**——checkout  abandonment 风险。PlanetScale 3 节点 cluster + Grafana + **Agents View** 监控多个 Agent 并行操作。

在 Cursor 里 prompt：读 housing recommendations → act on recommendations → optimize database。Sub-agents 并行：list schema changes、读 PlanetScale Insights API、farm work out。**Composer 2.5** 极快，支撑 live demo。

PlanetScale Insights 原本为人设计，现 **对 Agent 极友好**：解释哪些 query 慢、建议 index/schema 变更；自有模型测试 index 推荐后再生成 suggestion。

**和你何干：**  
好 infra 不是丢 raw log，而是 **surface 结构化 recommendation** 供 Agent act。

---

### 3. Deploy Request + Branch = Agent 友好的 DBA 工作流

**说法：**  
Database **branch** = 类 production 环境做 schema 变更 → 就绪后开 **Deploy Request**（类 PR）→ 审查 diff → deploy。图表 **竖线** 标记变更时刻——Agent 改 infra 时你必须知道「什么时候、改了什么」。

加 index 后，最慢的 query 在 Grafana 上立刻变快；每条 graph 都 correlate 变更、异常、错误。

**和你何干：**  
Agent 改 infra 和 human 改 infra 应走同一套 review 流程——可见 diff、可 reject。

---

### 4. 安全拦截：reject drop column

**说法：**  
一 Agent（「bad guy」）试图 **drop column** → PlanetScale 扫描 in-flight queries → 变更会 break active queries → **reject**（除非 force）。

**和你何干：**  
平台自动检测「这个 schema 变更会不会打断正在跑的 query」——Agent 不需要自己推理这一点。

---

### 5. Schema Rewind：允许犯错 + 秒级 undo

**说法：**  
另一 Agent 被 prompt 做坏事 → smoke test 后 **允许 push** → 生产丢列、站点挂 → **Schema Rewind**：flip 回上一 schema 版本，**中间写入不丢**。非 restore snapshot——PlanetScale 保 long-running window，**与表大小无关**（客户有 600–700 TB 表同样秒级 rewind）。

**和你何干：**  
Living system 需要 **undo** 而非 snapshot 考古——Agent 操作 infra 的前提。

---

### 6. Sharding：infra primitive + Cursor 承担 query refactor

**说法：**  
优化后 query 更快 → 流量涨 → 垂直扩展到头 → **Vitess 在线分片** 3 节点→16 shards。

流程：queue → copy data（单库→16 shard，**持续 replicate 新数据**）→ verify 每行 → 切 read replicas → 切 primary（**可 fail back**）。全程应用照常跑。

**VSchema** 声明式：hash sharding key、哪些表 co-locate。**Scatter-gather join** 在 critical path 极慢——旧 app 要 years 级 refactor；demo 里 **Cursor 大规模给 query 加 shard key routing**，直达单 shard。Sam 称这是 demo 里 Cursor 最重活。

Sam 曾在 GitHub 早期写 issue：**尽量别分片，因为真的极难。** 但流量到了不得不做。

**和你何干：**  
分片 = infra 能力 + 应用 refactor；coding Agent 可扛后者，但 **sharding key 设计** 仍需人懂产品。

---

### 7. Small sharp tools：智能可组合，风险不线性涨

**说法：**  
PlanetScale 先为 **人类**（最 flaky 的 agent）建 safe-by-default，再为 **更快 Agent** 优化。

| Tool | 作用 |
|------|------|
| Branch / Deploy Request | 隔离变更、可审查 |
| Rewind | 秒级 undo schema |
| Traffic Control | query/credential/tag 级资源隔离，越界 kill |
| Backpressure | schema change 期间 query 变慢则平台主动减速 |
| Recommendations | 把专家经验 surface 给 Agent |

**反模式**：把 streams of logs、tons of data 丢给 Agent——容易做错。

**和你何干：**  
设计 Agent 工具接口时：**窄、可组合、低歧义**，别给一个「manage_database」万能工具。

---

### 8. Living OS：变更 → monitoring → 下一轮 instruction

**说法：**  
五阶段闭环：

1. **Instruction** — 平台 primitive 收窄任务  
2. **Development** — branch / deploy / rollback（Agent 自治管理）  
3. **Deployment** — 受控并行（reshard 时可能 block schema change）  
4. **Long-state + backpressure** — Agent 不必自己 watch Grafana  
5. **Monitoring** — 每次变更连到 impact、**哪个 Agent** 所为；production behavior → 下一轮 instruction

Sam 判断：**every infrastructure platform** 未来都需要这些 primitive；database 是最严肃场景——「if we can do it with databases, we can do it with anything」。

行业 obsession 在 **point of creation**（快速 spin up sandbox）；Sam 说未来在 **long-term evolution**——应用有时活二十年，Agent 要在 living OS 里持续维护。

**和你何干：**  
Agent 平台设计别只优化 Day one；优化 **Day 1000 的 prune、rollback、audit**。

---

## 关键概念表

| 词 | 白话 |
|----|------|
| **Deploy Request** | 类 PR 的数据库 schema 变更审查与 deploy |
| **Schema Rewind** | 秒级 flip 回上一 schema 版本，不丢中间写入 |
| **VSchema** | Vitess 声明式分片配置，Agent 可生成 |
| **Scatter-gather query** | 跨 shard 聚合，critical path 慢 |
| **Small sharp tools** | 窄接口、可组合、降歧义 |
| **Backpressure** | 平台在变更期间主动限速保护生产 |
| **Traffic Control** | query/credential 级资源隔离与 kill |
| **Agents View** | 监控多个 Agent 并行 DB 操作 |
| **Living OS** | 生产环境像操作系统，需持续维护而非一次性 deploy |

---

## 值得记住的原话

> **"Agents are non-deterministic. Every time I've practiced this demo, it's done something different."**  
> Agent 非确定性。每次彩排 demo 路径都不同。

> **"We have successfully stopped an agent from breaking production."**  
> 我们成功阻止 Agent 破坏生产。

> **"We have just undone a nasty outage that could have lasted hours, very, very quickly."**  
> 本可持续数小时的严重故障，我们极快 undo 了。

> **"There is nothing worse than getting woken up at two in the morning, production's broken, you have absolutely no idea what changed."**  
> 凌晨两点 production 挂了、不知道改了什么——没有比这更糟的。

> **"If you narrow tools down, you reduce ambiguity, and you increase reliability."**  
> 工具越窄，歧义越少、可靠性越高。

> **"Composition scales intelligence without increasing risk."**  
> 组合扩展智能，风险不必线性涨。

> **"We build PlanetScale for the flakiest agents of all, which is humans."**  
> PlanetScale 先为最 flaky 的 agent——人类——而建。

> **"Day one is extremely easy... continual pruning, evolution and maintenance... a living operating system."**  
> Day one 容易……难的是 living OS 的持续维护。

> **"Good infrastructure turns expertise into primitives."**  
> 好基础设施把专家经验变成 primitive。

> **"If we can do it with databases, we can do it with anything."**  
> 数据库这么严肃的场景都能做，别的也能。

---

## 小结

**这期最核心的判断：** Agent 时代的基础设施要把 **living production** 变成 Agent 可安全操作的 surface——**窄工具 + 平台 veto + rewind**，比给 Agent  raw log 和万能 SQL 更可靠。

**读完应带走：**
- Insights / Schema Rewind / Agents View 等是把 **专家经验 primitive 化**，让 Agent 在真实库上改而不炸。
- **Composition scales intelligence without increasing risk**——组合小工具，风险不必线性涨。
- Day one 容易，难的是 **living OS** 的持续 pruning 与 audit；人类仍是最 flaky 的 agent，infra 先为人建再为 AI 建。

**和 vault 的关系：** 接 [[IBM团队-Harness工程详解]] 与 [[Cursor-128个Agent团队协作]]——harness 在数据库层的落地样例。

---

## 行动启示

1. **Infra 为 Agent 设计**：branch、diff、reject、rewind、audit 不是 DBA 奢侈品，是 Agent 操作前提。  
2. **别丢 raw log 给 Agent**：surface 结构化 recommendation 与 narrow tools。  
3. **允许 Agent 并行 + 平台 veto**：Agents View + 自动 break-query 检测。  
4. **Rewind 比 restore 快一个数量级**：living system 需要 undo 而非 snapshot 考古。  
5. **分片 = infra + 应用 refactor**：Cursor 类 agent 可扛 query 改造，但 VSchema 设计仍需人懂产品。  
6. **Backpressure 解放 Agent**：不必让 Agent 自己 watch Grafana。  
7. **变更必须可关联**：谁（哪个 Agent）在何时改了什么 → 下一轮 instruction。

---

## 相关阅读

- [[Cursor-128个Agent团队协作]] — Cursor 多 Agent 编排与 Sam 本场 demo 工具  
- [[IBM团队-Harness工程详解]] — Harness 约束与可靠性第一性原理  
- [[DeepMind-模型将吞噬Harness]] — 模型 vs harness 边界讨论  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1ZWTL64Erg](https://www.bilibili.com/video/BV1ZWTL64Erg/)（B 站 *Easonlee的AI笔记* 转载）  
- **讲者**：Sam Shank，PlanetScale CEO  
- **时长**：25:40  
- **转写**：Recastory `A3-planetscale-agent/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
