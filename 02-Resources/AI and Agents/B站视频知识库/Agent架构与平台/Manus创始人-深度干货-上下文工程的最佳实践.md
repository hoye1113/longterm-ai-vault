---
title: "Manus创始人：深度干货！上下文工程的最佳实践"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV12x1xB8E7b/"
speaker: "Peek / Pe（Manus 联合创始人 & 首席科学家）/ Lance（LangChain）"
duration: "60:48"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - context_engineering
  - multi_agent
  - mcp
  - memory
created: 2026-06-09
description: "LangChain Lance 铺垫 context engineering 五主题；Manus Pe 讲生产 battle-tested 的非共识：compaction vs summarization、share-memory vs communicate、三层 action space、工具 offload，并警告 avoid context over-engineering。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV12x1xB8E7b/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Manus 创始人：上下文工程的最佳实践

## 先搞懂这一期

**这是什么节目？**  
LangChain 与 Manus 联办的 **~61 分钟 webinar + Q&A**。Lance 先梳理 industry 共识（offload / reduce / retrieve / isolate / cache），**Pe（Peek）** 再讲 Manus  July 博客之后的新干货——重点在 Lance 幻灯片 **「discourage / 非共识」** 列。

**这期在回答哪三个问题？**

1. **为什么 Agent 时代要 Context Engineering，而不是继续 Prompt Engineering 或早 fine-tune？**  
2. **上下文爆炸怎么治？** Compaction 和 summarization 有何本质区别？  
3. **Manus 在 production 里怎么做 isolation、工具 offload、eval——以及什么时候该删脚手架？**

**用一条线串起来（没看视频也能复述）：**

Agent 自主 tool call → message 列表 **无界膨胀** → **context rot**（性能随 context 变长下降）。Karpathy 式定义：** delicate art of filling the window with just what's needed for the next step**。  
Industry 五招：**offload**（重 payload 进文件系统）、**reduce**（prune/summarize）、**retrieve**（glob/grep vs 向量）、**isolate**（subagent 分窗）、**cache**（KV cache）。  
Manus 加深：**compaction 可逆**（只留 path/query，内容在外部状态）、**summarization 不可逆**（用 schema 表单式摘要，保留最近几条 full tool result）；**communicate vs share-memory** 两种 subagent 模式；**三层 action space**（atomic function call → sandbox CLI → Python/API）把 MCP 膨胀推出 function 层；最大跃迁往往来自 **简化架构**，不是加层。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Context engineering = 塞满 context window | **精确填下一步所需**；与 prompt engineering 时间线对照（ChatGPT 后 prompt ↑，2025 agent 年 context ↑） |
| Subagent = 多角色 org chart | Manus **不按 designer/coder 分角色**——人类 org 是 context 限制产物 |
| 向量库检索上下文 | Manus session 级 sandbox **不用 index DB**，偏 Claude Code 式 **glob/grep** |
| Fine-tune 做垂直 agent | Pe：**尽量久靠 general model + context engineering**；MCP 让 fixed action space RL 极难 |
| Open deep research 三阶段 | Lance 用同一框架对照 offload/isolate/reduce 如何组合 |

---

## 分话题讲

### 1. 为什么需要 Context Engineering

**说法：**  
Prompt engineering 随 ChatGPT（2022.12）兴起；**context engineering** 与 **year of agents** 同步爆发。根因：agent **LLM + tools + loop**，每次 tool call 把 **observation** 追加进 messages——Manus 典型 **~50 次** tool call，Anthropic 生产 agent **数百 turn**；context 涨，**quality 跌**（**context rot**）。

**Pe 的边界论：**  
创业早期 **别过早 specialized model**——迭代速度被训练周期锁死；产品成熟后 fine-tune 也危险：**MCP 一夜改 action space**，on-policy RL 假设崩塌。  
**Application vs model 的分界线：context engineering**。

**和你何干：**  
默认栈：**frontier model + 上下文策略**；fine-tune/自训是第二阶段，不是 day one。

---

### 2. Context Offloading：重 payload 不进 history

**说法：**  
不必让所有 context 活在 message list。Tool 输出（如 web search）token 极重 → **写入文件系统 / 外部 state**，回给 agent 的只是一行 **path / 摘要指针**；需要时再 retrieve。  
Claude Code、Manus、Open deep research、Deep agents、cognition 等均采用。

**和你何干：**  
设计 tool 返回格式时问：**默认回传全文还是 handle？**

---

### 3. Context Reduction：Prune 与 Summarize

**说法：**  
- **Pruning**：删掉旧 tool call + output（Claude 4.5 SDK 已内置）。  
- **Summarization / compaction trigger**：Claude Code 达 context 比例自动 compact；cognition 在 agent handoff 时 summarize。  
Open deep research：research 阶段对 **token-heavy search** 做 summarize observation。

**和你何干：**  
Reduction 是 **默认能力**，不是高级优化；要配 **threshold**（见 §4）。

---

### 4. Retrieve 与 Isolate：怎么找、怎么分窗

**Retrieve 辩论：**  
Cursor（Lee Robinson）：**语义索引 + grep** 混合；Claude Code：**仅文件系统 + glob/grep**（不用向量）。Manus per-session 新 sandbox **没时间建 index**，同 Claude Code 路线；长期 memory / 企业 KB 仍可能需要 **外部向量库**——取决于 **信息规模**。

**Isolate：**  
Subagent **各自 context window**，分工 concerns。Manus wide research、Claude subagents、Open deep research multi-agent 均用。

**和你何干：**  
代码库 / sandbox 规模 → **glob/grep 优先**；全库企业知识 → 再考虑 index。

---

### 5. Context Caching：KV cache 与成本

**说法：**  
Manus 强调 **KV cache**（Anthropic input caching 等）。Agent **input 远大于 output** 时，cache 命中决定成本；open source 自托管 **distributed KV 难**，frontier API 有时 **更便宜**。  
**Share-memory subagent** 因 system prompt / action space 不同 **无法复用 KV**，prefill 全价——隔离有 **cache 税**。

**和你何干：**  
架构要在 **isolate 收益 vs cache 成本** 间权衡。

---

### 6. Compaction vs Summarization：可逆 vs 不可逆

**说法（Manus 核心区分）：**  
- **Compaction**：每个 tool call/result 有 **full** 与 **compact** 两格式；compact 去掉可从文件系统 **重建** 的字段（如 write_file 只留 path）。**可逆 reduction**——10 步后某旧 action 可能突然重要。  
- **Summarization**：信息 **真正丢失**；必须在 summarize **前** 把关键块 offload 到文件 / log，以便 grep 找回。

**触发策略：**  
- 模型标称 1M context，**实际 rot 常从 ~128k–200k 开始**——用 eval 定 **rot threshold**，接近则 reduction。  
- **先 compaction**（如最旧 50% tool calls compact，新的保持 full 作 few-shot），不够再 summarization。  
- Summarize 时用 **full 版** 数据，且 **保留最近若干条完整 tool result**，避免 summarize 后 tone/风格漂移、不知道停在哪。

**Summarize prompt：**  
别 free-form；用 **schema 表单**（改了哪些文件、用户目标、停在哪）填字段 → **high recall 结构化**。

**和你何干：**  
Search tool：简单 query 可 full → 靠 compaction；复杂 multi-query → **subagent / agent-as-tool** 固定 output schema。

---

### 7. Context Isolation：Communicate vs Share-Memory

**说法（借 Go 谚语「不要通过共享内存通信」的变体）：**  
- **Communicate（经典 subagent）**：主 agent 写 prompt → 子 agent **仅见该指令**，只回 **最终输出**。适合短、清晰任务（ codebase 搜 snippet）。Claude Code **Task tool** 典型。  
- **Share-memory / share-context**：子 agent **见完整 tool history**，但 **独立 system prompt + action space**。适合 deep research——中间搜索/笔记都影响终稿；全塞文件再让子 agent 重读 **浪费 latency + token**。

**Wide Research / MapReduce：**  
主 agent spawn 多 subagent；信息共享靠 **同一 sandbox 文件系统**（传 path 而非复制全文）。  
Subagent 回传：**Submit Result** tool + **constrained decoding** 到主 agent 定义的 **output schema**（像 spreadsheet）。

**Manus 角色观：**  
**不按 designer/programmer/manager  anthropomorphize**——那是人类公司 context 限制；Manus 只有 **general executor + planner + knowledge manager** 等少数 agent，其余 **agent-as-tool**。

**和你何干：**  
短任务 → communicate；长链依赖中间态 → share sandbox + schema 契约。

---

### 8. 三层 Action Space：Function / Sandbox / Packages

**说法：**  
MCP 工具定义本身占 context → **context confusion**（错 tool、假 tool）。动态 RAG 加载 tool 描述会 **KV reset**，且模型 **仍记得已移除的 tool**。

**Manus 分层：**  
1. **Function calling**：~10–20 **atomic** 函数（读写在文件、shell、搜网、浏览器等）——schema 清晰、可 KV-friendly。  
2. **Sandbox utilities**：预装 CLI（格式转换、ASR、Manus 版 MCP 全在 shell 里调，**不注入 function 列表**）；大输出写文件，用 cat/less 处理。  
3. **Packages & APIs**：Python 脚本调预授权 API（3D、金融等）；**重计算在 runtime，只把 summary 回 context**（CodeAct 思想，但 code 难 constrained decode，要选对场景）。

三层对模型仍表现为 **标准 function call**（shell、file 等），接口简单。

**Tool 数量经验：**  
General agent **native function ≤~30**；Manus **~10–20 atomic** + shell **图灵完备**扩展。  
**纯 CodeAct** 试过——难用 constrained decoding，**hybrid** 更稳。

**和你何干：**  
工具爆炸时 **下沉到 shell/script 层**，别全塞进 JSON schema。

---

### 9. 避免 Over-Engineering 与 Production 纪律

**说法：**  
五维（offload / reduce / retrieve / isolate / cache）**互相牵制**——更多 isolate/reduce 伤 cache；engineering 是 **多目标平衡**，很难。  
Pe 最重要警告：**avoid context over-engineering**。Manus 上线后最大跃迁常来自 **删层、简化**，不是 clever retrieval。目标：**让模型 job 更简单，不是更难**。  
Manus 已 **重构 5 次**（3 月→10 月）；模型 **行为变**，不能停。Eval 法：**固定架构换弱/强模型**——若换强模型增益大，架构 **不够 future-proof**（弱模型明天≈今天强模型）。  
Eval 三板斧：**用户 1–5 星** > 可验证 internal tests + execution benchmark > 实习生人工（网站、可视化等「品味」任务）。  
Guardrail：sandbox 出网检查、敏感操作 **人工确认**；browser login 持久化与 prompt injection 仍难，渐进式 **user takeover**。  
RL on harness：MCP 下 **fixed action space 不成立**，别重复造 foundation layer；个性化走 **parameter-free online learning**（如 CJK 字体等集体纠正）。  
Planning：早期 **todo.md 更新占 1/3 action** 已弃；现 **planner subagent（agent-as-tool）**，可用不同模型（如 Grok）做外审。

**和你何干：**  
每季度问：**哪层 scaffolding 可以因为模型变强而删掉？**

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Context engineering** | 为下一步决策精确填充 context window |
| **Context rot** | context 过长后重复、变慢、质量降（常早于标称上限） |
| **Offload** | 重信息存文件/外部 state，history 只留指针 |
| **Compaction** | 可逆压缩 tool 消息（去可重建字段） |
| **Summarization** | 不可逆摘要；用 schema 保 recall |
| **Communicate pattern** | Subagent 只看任务 prompt，只回结果 |
| **Share-memory pattern** | Subagent 见全 tool history + 独立 system |
| **Agent-as-tool** | 对外像 function，对内是 workflow/subagent |
| **Layered action space** | Function → sandbox CLI → code/API |
| **Context confusion** | 工具太多导致错 call / 幻觉 tool |

---

## 值得记住的原话

> **"Context engineering is the delicate art and science of filling the context window with just the right information needed for the next step."**  
> 上下文工程是为下一步精确填充窗口的艺术与科学。

> **"Context engineering is the clearest boundary between application and model."**  
> 上下文工程是应用与模型之间最清晰的分界线。

> **"Compaction is reversible… summarization behaves very differently."**  
> Compaction 可逆；summarization 完全不同。

> **"Do not communicate by sharing memory… [for agents:] by communicating or by sharing memory."**  
> 两种 subagent 协作模式：传话 vs 共享上下文。

> **"Please avoid context over-engineering… the biggest leaps came from simplifying."**  
> 别过度工程上下文；最大进步来自简化。

> **"The goal of context engineering is to make the model's job simple, not harder."**  
> 目标是让模型更好干，不是更难干。

> **"We do not divide by role… that's how human companies work due to human context limits."**  
> 别按人类岗位拆 agent——那是人脑限制，不是 AI 必需。

---

## 小结

**这期最核心的判断：** Context engineering 是 agent 应用的 **主战场**——在 general model 上用 **offload + 可逆 compaction + 谨慎 summarization + 选对 isolation 模式 + 工具分层** 对抗 context rot；与 fine-tune/RL 比，**边界更清晰、迭代更快**。

**读完应带走：**
- **先 compaction 后 summarize**；summarize 用 **schema**，保留最近 full tool traces。  
- Subagent：**短任务 communicate，长链 research share sandbox + output schema**。  
- **≤20 atomic tools + shell/API 层** 控制 tool context；MCP 能力进 sandbox 而非全进 schema。  
- 模型变强 → **删脚手架**；用 weak/strong 模型切换测 architecture 寿命。

**和 vault 的关系：** Context engineering 主笔记，接 [[Agent实战-打造一个AI Agent的完整教程]]、[[IBM团队-Harness工程详解]]、[[DeepMind-模型将吞噬Harness]]。

---

## 行动启示

1. **测 rot threshold**：在你任务上找到 quality 开始掉的 context 长度（别信标称 1M）。  
2. **Tool 返回默认 compact**：path/query/一行摘要，全文落盘。  
3. **Summarize 前 dump full log** 到文件；摘要字段固定 schema。  
4. **Subagent 选型**：搜 snippet → Task/communicate；research 报告 → 共享 sandbox。  
5. **工具>30 时**：下沉 CLI/script，别堆 function definitions。  
6. **每 1–2 月**：换弱模型跑 eval，决定删哪层 context 管理。

---

## 相关阅读

- [[Agent实战-打造一个AI Agent的完整教程]] — agents.md、MCP、Skills 入门栈  
- [[IBM团队-Harness工程详解]] — harness verify/guardrails 与 context 管理并列  
- [[DeepMind-模型将吞噬Harness]] — 模型 upstream 后 scaffolding 会否被吞  
- [[WorkOS-创建和使用Skills方法论]] — Skills 与 context 分工  
- [[Loop-Agent Loop到底是什么]] — 长 loop 与 token/context 代价  
- [[MOC - Harness Engineering]] — Harness / context 横切索引  

---

## 来源

- **视频**：[BV12x1xB8E7b](https://www.bilibili.com/video/BV12x1xB8E7b/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Pe（Peek），Manus 联合创始人 & 首席科学家；Lance，LangChain  
- **时长**：~60:48  
- **转写**：Recastory `bilibili-retranscribe/BV12x1xB8E7b/`（FunASR SenseVoice + cam++，**asr v2** 49 段）  
- **参考**：Manus context engineering 博客（2025-07）；Lance 幻灯片（webinar 共享）  
- **版本**：v2 读者向讲义（2026-07-02）
