---
title: "Databricks：企业级 Agent 生产实践"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1o4TL6sExw/"
speaker: "Sandy (Databricks 数据 AI 技术负责人，前 AWS 首席数据 AI 架构师)"
duration: "37:06"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - harness_engineering
  - ai_evaluation
  - multi_agent
created: 2026-07-02
description: "Sandy 用两年客户现场经验提出五支柱 playbook：先 eval 再 trace 再数据，第七周才选模型；零售银行 chatbot 案例说明 demo 漂亮、上线翻车的典型死法。"
transcript_source: "Recastory/A2-databricks-agent/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Databricks：企业级 Agent 生产实践

## 先搞懂这一期

**这是什么节目？**  
Databricks 数据 AI 技术负责人 **Sandy** 在 AI Engineer 类会议上的主题演讲，约 37 分钟。她前 AWS 干了五年首席数据 AI 架构师，过去两年专门帮 B2B 和受监管行业（金融等）客户把 AI 从 demo 拉到生产。

**这期在回答哪三个问题？**

1. **为什么 demo 很漂亮，一上生产就翻车？** 客户问「AI 到底在干什么」，ROI 落空，问题出在哪？
2. **企业 Agent 上生产，最少要想清楚哪几件事？** 有没有可复用的框架，而不是每个项目从零摸索？
3. **选 GPT 还是 Claude，应该什么时候开始争？** 和大多数人直觉相反，答案可能很晚。

**用一条线串起来（没看视频也能复述）：**

Sandy 见过的客户对话几乎一个模子：领导催做 AI → 团队先争该用哪个模型 → 用干净数据做 demo → 领导签字上生产 → 几周后用户投诉、没人说得清 AI 为什么答错、凌晨三点不知道找谁。**根因不是模型不够聪明，是三个洞没填：看不见 AI 在干什么（可观测性）、没定义什么叫成功（评估）、出事没人负责（治理）。**

她据此提出 **五支柱**：评估 → 可观测性 → 数据基础 → 多 Agent 编排 → 治理。**写代码、选模型之前，先把评估想清楚。** 零售银行 chatbot 案例：先前 POC 花 8.5 万美元、6 个月失败；新路径 8 周 POC 里，**第七周才选模型**——前两周收 200 条真实客服问答建测试集，上线后靠 trace 发现 vector 库里政策文档过期，才修掉 CSAT 下跌。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Agent = 模型 + prompt + 工具 | **上生产** 还要 eval 体系、全链路 trace、数据策略、编排模式、治理流程 |
| 评估 = 看 accuracy 高不高 | 评估是 **系统规格书**：deflection rate、85% 阈值等 **业务数字**；数据集是 **活系统**，incident 后持续入库 |
| 可观测性 = 看 latency、错误率 | **Trace 每一步决策**——intent 分类、调 DB、查 RAG、guardrail——客诉和监管都要 |
| Multi-Agent = 多个 Agent 并行 | 三种编排模式（中央调度 / 事件总线 / 人工介入）；5 个以上 Agent 复杂度指数涨 |
| 先选模型再开发 | **第七周才选模型**——有 eval 数据集后，一周可比完 |

---

## 分话题讲

### 1. Demo 翻车的典型死法：三大缺口

**说法：**  
Sandy 两年里客户对话高度重复：组织内部争论 GPT vs Claude → 可控环境用干净数据做 demo → 领导满意 → 上生产 → 几周后「AI 在干什么？」ROI 落空、无法 scale。

三个缺口叠在一起：

| 缺口 | 白话 |
|------|------|
| **可观测性** | 看不见 Agent 每一步决策，就不该上生产 |
| **评估** | 嘴上说 accuracy、latency、groundedness，但没定义 **对业务什么叫 success**，没有持续 measurement 系统 |
| **治理** | AI 失败谁负责？凌晨 3 点找谁？喂给 AI 的数据谁拥有？对客户胡说八道怎么办？ |

**和你何干：**  
如果你在做 chatbot / 客服 Agent / 内部问答，demo 阶段就要问：**上线后用户投诉，你能回放 AI 的每一步吗？**

---

### 2. 五支柱：eval 必须早于写代码

**说法：**  
五个支柱 ideally 按序建；现实可并行，但 **评估必须最先想清楚**——在讨论任何模型、任何功能、写任何代码之前：

1. **Evaluation（评估）** — success 长什么样？用什么系统持续量？
2. **Observability（可观测性）** — 如何 trace 每个 decision？（欧洲监管：无 tracing 不准 onboard AI）
3. **Data Foundation（数据基础）** — 问答数据 + tracing 数据；典型项目 ~60% 时间
4. **Orchestration（编排）** — 单 Agent 简单；5+ Agent 复杂度指数涨
5. **Governance（治理）** — 失败问责、PII、prompt/model 变更、incident playbook

Databricks 把这些封装进 **Agent Bricks** 产品。

**例子（零售银行 deflection）：**  
chatbot 主目标是 **deflect** 简单查询（余额、overdraft 政策），让人工客服只处理复杂 case。Success 必须写数字：100 条 query 里 60 条简单 query 由 Agent 处理，accuracy ≥ 85%，再加 latency 等运营指标。

**和你何干：**  
别从「选模型」开会；从「上线后怎么知道它成功了」开会。

---

### 3. 三层 eval：behavioral 层最易漏

**说法：**  
评估分三层，是架构决策：

| 层 | 内容 | 例子 |
|----|------|------|
| **Deterministic（确定性）** | 格式、regex、NER、PII、intent | 老派 ML 已做多年，先扫掉 |
| **Semantic（语义）** | groundedness、relevance、safety | **LLM-as-judge**：用第二个模型评第一个模型的输出 |
| **Behavioral（行为）** | tool call 对不对、duplicate API、loop | demo 里 3 次 DB 调用无感；生产 thousands queries × duplicate = 烧钱 |

**例子（account balance）：**  
用户问余额，Agent 答对了。但 trace 显示它对同一 DB **调了 3 次**（retry/duplicate）。Demo 无所谓；生产 + 监管投诉，这是 cost 与 explainability 双重事故。

Golden dataset 来源：**跟 domain expert 聊真实 ground 上发生了什么**——客服实际怎么答、用户问 confusing question 时怎么办。Automated pipeline：问题 → AI 答 → 与 test set 比 → 打分 → 低分进人工 → fix → **新 case 入库**。

**和你何干：**  
很多团队只评「答案对不对」，漏评「调了几次 API、有没有 loop」。CI 里加 behavioral 检查。

---

### 4. Observability：trace 是客诉与合规前提

**说法：**  
Overdraft fee waived 场景（简化版 trace）：

```
用户：我被收了 overdraft fee，能 waive 吗？
  → intent classification（confidence score）
  → 调 customer DB API 取账户
  → RAG 查 overdraft 政策 vector DB
  → reasoning：claim 是否 legitimate
  → guardrail check
  → 回复用户
```

无 trace → 客户 dispute 时只能说「给个 discount 息事宁人」。有 trace → 可定位 duplicate call、outdated policy doc、错误 reasoning。

**在线 monitoring** 可在 duplicate 发生时 fallback、限 retry（最多 3 次）、超阈值转人工。

企业往往多框架、多云——需要 **centralized tracing data layer** 服务运维 dashboard、一线 support、eval pipeline。Databricks 用 Delta Lake + Unity Catalog 管 tracing 数据，MLflow 可对 trace 自动跑 LLM judge。

**和你何干：**  
Trace 不是优化项，是 **准入条件**——监管行业和非监管都一样。

---

### 5. Data Foundation：Agent 对脏数据零容忍

**说法：**  
人类看报表发现错数会找人改；Agent ** confidently 给错答案**，你还不知道。Sandy 典型项目 **60% 时间** 花在数据上。

两类数据：

- **Question data** — RAG、工具 hook、预训练/后训练所需
- **Tracking data** — trace/observability，供 auditor、在线监控、LLM judge

Databricks 栈：云存储 → Delta Lake（表格式）→ Unity Catalog（权限、PII tag、column description 供 AI 取 context）→ 应用层。

**和你何干：**  
vector DB 里的文档过期了，Agent 会 confidently 用旧政策答——案例里银行改利率政策后 CSAT 跌，trace 才定位到 embedding 没更新。

---

### 6. 多 Agent 编排三种模式

**说法：**

| 模式 | 特点 | 适用 |
|------|------|------|
| **Orchestrator-Worker（中央调度）** | 一个 orchestrator 分发；出问题查它的 log | 需要 central control |
| **Choreography（事件编排）** | 各 Agent 自治，订阅 message bus；可并行，latency 更低 | Agent 彼此独立（如 mortgage：一 Agent 查客户、一 Agent 查审批） |
| **Human-in-the-Loop** | confidence 低于阈值 → 人工介入 | 高风险决策 |

Sandy 另有 YouTube 视频详谈 state management、fault tolerance、scale。

**和你何干：**  
5 个以上 Agent 之前，先定编排模式，别默认「多开几个 Agent 并行」。

---

### 7. Governance：prompt 是变更管理，不是 git commit

**说法：**

- **Audit trail** — 每个 action、connection、request
- **PII pre-validation** — NER/regex；某客户测试阶段检出 **47 次** PII breach
- **Prompt versioning** — 企业级必须走变更流程：哪次 failure 导致哪次 prompt 改、下一版修什么——不能只有「fix typo」式 commit message
- **Model change management** — 厂商升级模型后，用 **自家 eval dataset** 测，不能只看公开 benchmark

**和你何干：**  
Prompt 变更和代码变更一样：记录 failure → fix 链路，否则三个月后没人知道为什么改。

---

### 8. 案例：零售银行 — 第七周才选模型

**说法：**  
背景：月 2 万通客服电话，~60% 简单 query；先前 POC 花 **$85k / 6 月失败**——上生产后无人知为何 fail、无法 measure、无 accountability。

8 周新路径：

- **Week 1–2**：收 200 条真实客服 Q&A；定义 success（60% deflection、85% accuracy 等）；建 automated eval pipeline（低分→人工→fix→入库）
- **中间**：data foundation、API 连接、trace；测出 duplicate API、满意度下降根因
- **Week 7–8**：**才**用 eval dataset 跑不同模型比 accuracy，选型
- **上线 6 周后**：银行改 interest rate 政策，邮件通知了客户，但 **vector DB 未更新** → thumbs down → trace 定位 outdated embedding → 修复

**和你何干：**  
有 eval set 后一周可比完模型，别先开 months 的 GPT vs Claude 宗教战争。

---

### 9. Production Incident Playbook

**说法：**  
Detect（dashboard）→ Diagnose（tracing）→ Contain（prompt 回滚 / 转人工 / circuit breaker）→ Fix（judge + eval report）→ **新 test case 入库**。需接 ITSM，凌晨 3 点 alert 对的人。

**Cost 治理**：behavioral eval 随 dataset 变大很贵；CI 里 prompt 变更只跑 eval **subset**，merge main 再全量。

**和你何干：**  
incident playbook 和 eval dataset 一样，是 living system——每次故障修复后必入库。

---

## 关键概念表

| 词 | 白话 |
|----|------|
| **Five Pillars** | Eval / Observability / Data / Orchestration / Governance |
| **Living eval dataset** | 从 ~200 条起步，生产 incident 与人工 fix 持续入库 |
| **Behavioral eval** | 评 tool call、duplicate、loop，非只看最终答案 |
| **Golden dataset** | 来自 domain expert 的真实 ground truth Q&A |
| **LLM-as-judge** | 第二个模型评第一个模型的输出（safety/groundedness/relevance） |
| **Deflection rate** | 简单 query 由 Agent 处理、不转人工的比例 |
| **Trace** | 每步 decision 的可回放记录 |
| **Week 7 model selection** | 先 eval 再选型，逆转「先争模型」习惯 |
| **Agent Bricks** | Databricks 把五支柱封装的产品化能力 |

---

## 值得记住的原话

> **"Everyone wanted to do something with AI... every conversation started with, let's choose the model."**  
> 人人都想做 AI……每次对话都从「选哪个模型」开始。

> **"If we can't trace every decision that it's making, it's no using production."**  
> trace 不了 Agent 的每一步决策，就不该上生产。

> **"Evaluation before touching any code, before discussing about any models, any features."**  
> 写代码、讨论模型和功能之前，先想清楚 evaluation。

> **"A lot of teams miss the behavioral layer when talking about evaluation."**  
> 谈评估时很多团队漏掉 behavioral 层。

> **"Three API calls in demo environment is fine, but in production... that's an expensive operation."**  
> Demo 里调三次 API 没事；生产里这是烧钱操作。

> **"Humans are always forgiving... agents don't forgive gaps. They'll give you the wrong answer confidently."**  
> 人对脏数据会原谅；Agent 不会。它会 confidently 给错答案。

> **"We selected the model in week seven, like in the eight weeks POC."**  
> 8 周 POC 里，我们在第七周才选模型。

> **"Your evaluation dataset is a living system."**  
> 评估数据集是活系统。

> **"Prompt versioning... cannot be just a change to a prompt and commit to git."**  
> Prompt 版本管理不能只是改 prompt 然后 git commit；得像代码一样走正式变更流程。

> **"Start with defining success, not from the technical sense, from the business sense."**  
> 从定义 success 开始——不是技术意义，是业务意义。

---

## 小结

**这期最核心的判断：** 企业 Agent 上生产失败，根因通常不是模型不够强，而是 **没先定义业务 success、看不见决策链、数据与治理没跟上**——五支柱里 **evaluation 是规格书**，应早于选模型。

**读完应带走：**
- Demo 翻车三板斧：不可观测、无业务数字 eval、无 accountability；regulated 行业 **trace 是准入门槛**。
- Eval 分三层：deterministic、LLM-as-judge、**behavioral**（tool call / duplicate / loop）——第三层最易漏。
- **第七周才选模型**：先 living golden dataset，再比模型；数据 foundation 常占项目大部分时间。

**和 vault 的关系：** 接 harness_engineering 与 ai_evaluation——把「能跑 demo」和「能 scale 生产」之间的工程 gap 说透。

---

## 行动启示

1. **明天就能做**：用 10–20 条「好答案」样例建 mini golden set + Python 自动比对 pipeline。  
2. **Success 写数字**：deflection rate、accuracy 阈值、latency——别停在「要准确」。  
3. **Eval 三层齐建**：尤其 behavioral（tool/duplicate/loop）。  
4. **Trace 当准入条件**：客诉时你会感谢自己。  
5. **Living dataset 指定 owner**：分类（security/logging 等），incident 后必入库。  
6. **模型选型延后**：有 eval set 后一周可比完。  
7. **Prompt/model 变更 = change management**：记录 failure → fix 链路。  
8. **CI eval 成本控制**：prompt PR 跑 subset，main merge 跑全量。

---

## 相关阅读

- [[OpenAI评估团队-不再低估模型]] — eval 方法论与「别低估模型」的互补视角  
- [[IBM团队-Harness工程详解]] — Harness 可靠性与 eval 系统视角  
- [[Loop-Agent Loop到底是什么]] — 开放式 loop 的 token 成本与评分闭环  
- [[MOC - Agent Theory and Design]] — Agent 理论总索引  

---

## 来源

- **视频**：[BV1o4TL6sExw](https://www.bilibili.com/video/BV1o4TL6sExw/)（B 站 *Easonlee的AI笔记* 转载）  
- **讲者**：Sandy，Databricks 数据 AI 技术负责人（前 AWS 首席数据 AI 架构师）  
- **时长**：37:06  
- **转写**：Recastory `A2-databricks-agent/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
