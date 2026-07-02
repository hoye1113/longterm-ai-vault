---
title: "Loop：Agent Loop 到底是什么？"
source: "B站视频 - Startup Ideas Podcast"
source_url: "https://www.bilibili.com/video/BV1cVjN6oEwx/"
speaker: "Ross Mikita (YouTube: Ross Mikita)"
duration: "22:33"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - loop_engineering
  - harness_engineering
  - ai_coding
created: 2026-07-02
description: "Ross Mikita 区分 Human-in-the-Loop 与 Agent Loop，批判 Boris/Peter 式开放式 autoloop 为 token 焚烧与老虎机，给出 Graphite 评分驱动的 code review 闭环作为唯一日常可用范例。"
transcript_source: "Recastory/workspace/knowledge/A7-loop-agent-loop/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Loop：Agent Loop 到底是什么？

## 先搞懂这一期

**这是什么节目？**  
**Startup Ideas Podcast** 一期约 23 分钟的对话。嘉宾 **Ross Mikita**（YouTube 同名）被请来 **讲清楚 agentic loop 是什么**——因为他觉得行业里大多数人 **要么不懂，要么 hype 过头**。语气很冲，但有一个 **可复制的 closed-loop 实例**。

**这期在回答哪三个问题？**

1. **Human-in-the-Loop（HITL）和 Agent Loop 差在哪？** 图表上差「谁在中途审批」。
2. **Boris / Peter 说的「我不写 prompt，我 generate loops」**——普通人该跟吗？  
3. **有没有今天就能用的、合理的 loop？** 有，但在 **code review**，不在「一条 PRD 建整个 App」。

**用一条线串起来（没看视频也能复述）：**

**HITL（你我在用的）：** 你 prompt → agent 出结果 → **你**看、测、再 prompt → 循环。你是 **导演**。

**Agent Loop（ hype 版）：** 你 **只 fire 一次**（PRD.md / slash goal）→ agent 产出 → **产出喂回给自己** → 继续改 → 人不 intermediate。像雇了一个 **从不问你的超级程序员** 闷头干到底。

Ross 的立场：**开放式 App Loop 对普通人 = 烧 token + 错误假设 + 老虎机**——Peter 一个月能烧 **130 万美元 token**，你有吗？Plan 文档 **永远盖不全** product vision（agency 的人都懂「你还漏了这个」）。**Slash goal / slash loop** 各工具名字不同，本质一样。

**唯一他 daily 用的 loop：** Cursor + GitHub + **Graphite** code review——review 给 **1–5 分**，低于 4 不 merge；**grep loop** Skill 读 review → fix → push → 等新区 review，直到 ≥4 或跑满 5 轮。**反馈函数固定**，目标 binary-ish，这才叫 closed loop。

**结论句：Human-in-the-loop is the best loop**——至少现在、至少对要做有品味产品的 startup builder。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| [[Loop Engineering 橙皮书 - 花叔]] 讲 Loop = Harness 上一层 | 这期是 **反 hype 科普 + 边界条件** |
| [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] Boris 不谈 prompt | Ross **解释普通人不能无脑 copy 的原因** |
| [[Alchemy CPO-从代码审查到自动代理]] 审查自动化 | 与 **grep loop** 同一脉络：review 分闭环 |
| Agent 自主跑三天 | **需要 meta-harness（测试、浏览器截图）** 才 maybe  work——你没有 |

---

## 分话题讲

### 1. 两种循环：一张图讲清

```
HITL:
  你 ──prompt──▶ Agent ──result──▶ 你（测试/审批）──▶ 再 prompt ...

Agent Loop:
  你 ──fire once（PRD/spec）──▶ Agent ⇄ result feedback ⇄ Agent ...
                                    （人不在环里）
```

**HITL 日常：** 做 todo app——先 landing page，满意再做 auth，再做 backend；**每一步你 govern**。

**Agent Loop 叙事：** 一份 spec.md 够 agent 自己 loop 直到「done」——**听起来**像未来，**实践中**对 meaningful product 问题很大。

---

### 2. 开放式 Loop 为什么容易翻车

**① Token 预算**  
不是 $200/月 tier 就别想。大佬可以 **unlimited tickets** 做 research；你烧完额度得 **捐钱给即将万亿估值的公司**。

**② Plan 永远不够**  
雇一个聪明 dev **不 consult 你** 闷头做完——会做满 **错误假设**（架构、UI、edge case）。人类 agency 都 extract 不全需求，何况一份 markdown。

**③ 老虎机 / Full Self-Driving 类比**  
Miami → Charleston 按 GO，**不能** halfway 下车吃 Fried chicken、给用户看半成品收反馈。Startup 要靠 **给人看 app 换反馈**——open loop **缺这一环**。

**④ 即使 Boris/Peter**  
Ross 猜他们有 **test suite + browser screenshot + insane meta-harness**——不是 slash goal 三个字。普通人 **没有这套 infra**。

---

### 3. Slash Goal / Slash Loop：名字不同，一回事

Cursor 有 `/loop`，别的工具有 `/goal`——**同一模式**：

- 高层 prompt + 可选 attach markdown  
- 「build entire thing, don't stop, no mistakes」  

**适用边界（Ross 承认）：**
- ✅ **Experimentation**：他做过 Among Us AI benchmark simulator，**1.5 小时**搞定，细节错也无所谓  
- ✅ **Prototype / 不在乎审美**  
- ❌ **有意义的 product + 品味 + 有限 budget**  

教 startup listener「用 loop 做百万美元 App」——**misleading**（除非你就是想 burn tokens 做 research）。

---

### 4. Grep Loop：唯一推荐的 Closed Loop

**栈：** Cursor（harness）+ GitHub + **Graphite**（code review agent；CodeRabbit 等同类）

**流程：**
1. Push feature → Graphite 自动 review AI 生成的 code  
2. 输出问题 + **1–5 分**  
3. 规则：**≥4 才允许上 production**  
4. 触发 **grep loop** Skill：读 GitHub review → fix → push → Graphite 新 review  
5. 循环直到 ≥4/5 或 **最多 5 轮**

**为何这算「真 loop」：**
- **Fixed feedback engine**（评分 + 具体 comment）  
- **Goal 明确**（分数门槛）  
- **范围 closed**（只改 review 指出的）  

**仍会 break：**
- 单次 push **>1000 行** diff → 很难 5/5 → 要拆 PR  
- Loop **不 perfect**——但比 open-ended app loop **现实得多**

这和本期 sponsor CodeRabbit 同类——**binary-ish output**（过/不过）才适合 autoloop。

---

### 5. 什么时候 Loop 合理：Binary vs Creative

| 场景 | Loop 合理？ | 原因 |
|------|------------|------|
| Code review 评分 | ✅ | 固定 rubric，输出可验证 |
| SEO 批量 300 页同模板 | ✅ maybe | 样式一致即可 |
| 做有品味的 SaaS / App | ❌ now | 需要人 mid-flight 反馈 |
| 科学 benchmark toy | ✅ experiment | 细节错可接受 |

**Future：** Ross **不否认** 将来 meta-harness 成熟后 open loop **可能** work——**不是 2026 年 6 月录音时的建议**。

---

### 6. 与 Boris/Peter 叙事的关系（不扣帽子）

Ross **不是说他们恶意**——他们 **必须** experiment self-healing agents；token 对他们 **不重要**。

问题在 **content 教普通人 copy**——「oh this is marshmallow crispy」除非你想 **donate to trillion-dollar cos**。

**Human-in-the-loop is the best loop** = 对 **startup builder 的默认策略**。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Human-in-the-Loop (HITL)** | 人每步 prompt、测试、审批 |
| **Agent Loop** | 人 fire 一次，agent 自反馈循环 |
| **Open loop** | 目标模糊、反馈靠 agent 自己猜（建整个 app） |
| **Closed loop** | 固定 feedback engine + 明确 stop 条件 |
| **Slash goal / loop** | 各工具 CLI 的一键 autoloop 命令 |
| **Grep loop** | Graphite review → fix skill → push 循环 |
| **Meta-harness** | 测试、浏览器、review 等让 loop 可运行的外层 |
| **Slot machine effect** | 烧 token 赌一次「能不能成」 |

---

## 值得记住的原话

> **"Human in the loop is the best loop."**  
> 人在环里，是目前最好的 loop。

> **"It's basically a slot machine."**  
> （开放式 app loop） basically 老虎机。

> **"The only place a loop makes sense is in a very confined process with a very fixed feedback loop — code review."**  
> Loop 只在该窄、反馈固定的地方合理——code review。

> **"You think your plan doc covers everything — it never does."**  
> 你以为 plan 盖全了——永远不会。

> **"Unless you want to donate money to companies about to go public at trillion dollar evaluation — this just doesn't make sense."**  
> 除非你想给万亿市值公司捐 token 钱——现在别这么干。

---

## 小结

**这期最核心的判断：** **Human-in-the-loop 仍是默认最优**；开放式 app autoloop 对普通人像 **老虎机烧 token**——唯一日常合理的是 **固定 scorer 的窄 loop**（如 Graphite code review → fix → push）。

**读完应带走：**
- Agent Loop ≠ 无脑 while-true；没有 fixed feedback，loop 不收敛。
- Plan doc 永远盖不全；open loop 只适合 experiment / throwaway prototype。
- 与 Boris 式 loop 叙事对照：背后常有 **你没有的 harness budget**。

**和 vault 的关系：** 接 loop_engineering 与 [[MOC - Harness Engineering]]——补「哪种 loop 现在别盲目上」的刹车片。

---

## 行动启示

1. **默认 HITL** 做 product；把 open loop 限在 **experiment / throwaway prototype**。  
2. **若要 autoloop**：先找 **fixed scorer**（review 分、测试 pass、lint zero）——没有 scorer 不要 loop。  
3. **抄 grep loop 模式**：review agent + Skill「读 review → fix → push」+ merge 门槛。  
4. **控制 diff 大小**（<1k lines）让 review loop 能收敛。  
5. **读 Boris 叙事时加一层 filter**：他的 loop 背后有 **你没有的 harness budget**。  
6. 与 [[Loop Engineering 橙皮书 - 花叔]] 对照：橙皮书讲 **怎么设计 loop**；本期讲 **哪种 loop 现在别盲目上**。

---

## 相关阅读

- [[Loop Engineering 橙皮书 - 花叔]] — Loop = Harness 上一层；五动作循环  
- [[遇事留痕 - Loop Engineering 的基础 - 魔术师卡颂]] — 失败与 PR 日志是优化 loop 的燃料  
- [[Claude Code负责人 Boris Cherny-Tokenmaxxing与AI智能体前沿]] — Boris 侧 loop / token 叙事  
- [[Alchemy CPO-从代码审查到自动代理]] — 代码审查 → 自动代理链  
- [[MOC - Harness Engineering]] — Harness / Loop 横切索引  

---

## 来源

- **视频**：[BV1cVjN6oEwx](https://www.bilibili.com/video/BV1cVjN6oEwx/)（B 站转载 Startup Ideas Podcast）  
- **嘉宾**：Ross Mikita  
- **转写**：Recastory `A7-loop-agent-loop/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
