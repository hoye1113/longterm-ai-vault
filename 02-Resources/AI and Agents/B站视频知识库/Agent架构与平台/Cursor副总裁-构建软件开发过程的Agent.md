---
title: "Cursor副总裁：构建软件开发过程的Agent"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1MQVf6SEST/"
speaker: "Cursor 副总裁（工程负责人视角）"
duration: "20:39"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - cursor
  - harness_engineering
  - skills
  - multi_agent
created: 2026-06-09
description: "Cursor VP 讲第三纪元 Agent 团队：98% merge 由 AI 写但企业常卡 40% 增效；瓶颈在 STLC 全链；PM/EM/Security/Growth 四类自治 Agent 与 Skills 原子单元。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1MQVf6SEST/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Cursor 副总裁：构建软件开发过程的 Agent

## 先搞懂这一期

**这是什么节目？**  
Cursor 副总裁在大会上的 **~21 分钟 field notes**。不是产品发布，是 **「我们怎么建 Agent 团队」** 的战术分享——进入 **第三纪元：人类 × Agent 协作**。

**这期在回答哪三个问题？**

1. **为什么 AI 写代码暴涨，生产力却只涨 ~40% 就 plateau？**  
2. **STLC 各阶段，人还要做什么？Agent 该产出什么 artifact？**  
3. **Cursor 内部实际跑了哪些「Agent 团队」？** 怎么从 bug 报告一路链到 PM/EM/Security/Growth？

**用一条线串起来（没看视频也能复述）：**

动机：2025 初企业 **0% AI 代码** → 现在 ~15–20%（企业）到 Cursor 自身 **~98% merge commits by AI**——变化史上最大。  
但客户 rollout：**先爽一波，一年后卡在 ~40% 增效**——因为 **只换了 STLC 里写代码那一小段**，瓶颈挪到 plan/ship/retro。  
框架：**intelligence（模型+harness）→ Agent 系统 → 人类**。人类 job = **审 polished artifacts + 高保真 feedback**；中间系统要产出 **决策清单 + 像素级 demo**。  
案例 1 — **Issue Glass**（内测 Glass）：Slack 报 bug → cloud agent 常卡住 → Lauren 建 **how skill + why skill** → **bug reporter agent** 追问细节（有时直接当 support 关闭）→ 上层 **PM agent**（P0/P1/P2 分拣）+ **EM agent**（experimental，路由负责人）。  
案例 2 — **Security bot**：PR 触发，模拟 appsec 工程师挖漏洞，**200+ 自动修**。  
案例 3 — **Agentic risk detection**：PR 创建 → agent 评风险；低风险 **免人工 review 直接 merge**；中高风险 **比 CODEOWNERS 更准的路由**。  
案例 4 — **Growth 四 Agent**：实验 audit、Notion↔Linear↔Statsig 同步、24h 监控指标、胜者 PR 清 feature flag——实验吞吐 **暴涨**。  
文化：**AgentX channel**（agent 抱怨 devx）；Lauren 类 **meta 思维 champion**；团队配比变（2 SWE + DS + designer + PM 的 growth pod 极有效）。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Cursor = IDE 里写代码 | **STLC 全链 Agent 团队** + artifact 审阅 UX |
| Copilot 增效 30–40% | 那是 **Phase 2 天花板**；Phase 3 要 **链系统** |
| Skills = 文档技巧 | **how skill** 是 cloud agent 挖 codebase 的 **关键原子** |
| Code review 靠 CODEOWNERS | **Agent 风险评分** 可更准路由 reviewer |

---

## 分话题讲

### 1. 40% plateau：只换了 STLC 的一角

**说法：**  
直觉：R&D 60–80% 花在「手写代码」→ 模型写好代码应 **3–4x**。现实很多团队 **~40% throughput** 就停——因为还在 **Phase 2：coding assistance**，没 graduate 到 **Agent 系统链 STLC**。

**STLC 五段：** plan → build → ship/validate → retro。AI 写了 build 里大块代码，但 **plan 要人看 rigorous plan**；build 要人看 **架构决策、风险百行、demo**；ship 要 **人名 on production**；retro 要人喂 outcome。

**和你何干：**  
别只测「AI 写了多少行」——测 **端到端 STLC 周期** 哪段还卡人。

---

### 2. 人类工作 = 审 artifact + 高保真 feedback

**说法：**  
把 intelligence 变成 software：**模型+harness** 在下，**人类在上**审 artifacts。  
Agent 系统中间层要输出：  
- **清晰 synthesis**（agent 做了什么）  
- **待人类决策点**  
- **像素/ demo**（PR 带截图、demo link 永远最香）  
- **IO loop**：人类 feedback  agent 能 pick up 继续跑

新 Cursor IDE 迭代：**review polished artifacts + 反馈** 是核心 UX。

**和你何干：**  
你建的每个 agent workflow，问：**最后给人什么 artifact？决策点写清了吗？**

---

### 3. PM Agent + EM Agent：从 Issue Glass 长出来

**说法：**  
Launch Glass 内测 → `#issue-glass` 每天 10–20 条 paper cut → oncall Lauren 发现：**@cursor fix** 的 cloud agent 常 stuck。  
她手动试 pattern：  
1. **how skill** — 教 harness **rigorous inspect codebase**  
2. **why skill** — 更深解释代码在干嘛  
3. **bug reporter agent** — Slack 触发，**反向追问**报 bug 的人（有时 sass，有时当 support 关掉）  
4. **PM agent** — 分拣 P0/P1/P2  
5. **EM agent**（实验）— 「两个 remote SSH bug 来了，@工程师」——**ownership map 还不完美**

架构：**EM agent（自治，日/周跑）**  synthesize 下层 automation；各层用 skills + tools。

**和你何干：**  
Meta 问题（triage、路由）适合 **更高阶 agent synthesize  lower automations**——从 primitive curiosity 几周长成。

---

### 4. Security bot：无限 appsec 的杠杆

**说法：**  
PR publish 触发；跑一系列 prompt 找 **critical/high/medium/low**；**200+ 漏洞自动修**；appsec 团队 **不必按同速扩招**——且 **每 PR 更 thorough**（「got a guy」）。

**和你何干：**  
STLC **ship 前** 插 autonomous security agent，ROI 清晰。

---

### 5. Agentic risk detection：低风险 fast path

**说法：**  
改 policy 后 PR 常撞 **8 个 reviewer**（code owners）——小改也堵。  
Agent 读 PR → **风险评分**；观察一周后：**very low risk → merge 无需人**；medium/high 还审，且 agent 能指 **谁最懂这块 code**（比 CODEOWNERS 准）。

**和你何干：**  
**更多 review 政策** 和 **agent 风险评估** 可以并存——严但不堵低风险。

---

### 6. Growth 四 Agent：实验工厂

**说法：**  
Growth pod：~2 工程师，目标 **月 20–30 实验**；栈 Statsig + Linear + Notion + code。痛点：setup 错 metric、Notion/Linear 复制粘贴、**6 天才发现 metric 挂了**。  
四个 agent：  
- **Audit setup**（metric 对不对）  
- **Sync docs**（Notion ↔ Linear ↔ Statsig）  
- **Monitor run**（24h 看 bonkers）  
- **Suggest winner + PR 清 flag**（人选 variant B → agent 提 PR 删 Statsig 分支代码）

人仍 **最终选 variant**；实验吞吐上去，**dead branch 减少**。

**和你何干：**  
非 build 阶段的 **admin/triage** 是 Agent 团队第一批高 ROI 场景。

---

### 7. 组织与文化：Factory 思维

**说法：**  
- **DevX channel** → 有人建 **AgentX**（cloud agent 抱怨 devx，试验 auto-fix）  
- **Champions**（Lauren）：empower **meta 改造**  
- **Team 配比变**：growth pod **2 SWE + 1 DS + 1 designer + 1 PM** 极有效——agent 干脏活后的 **新黄金比例**

**和你何干：**  
招/组 team 时按 **「agent 干多少 admin/code」** 重算 headcount 结构。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **STLC** | Software Testing/Lifecycle：plan/build/ship/retro |
| **40% plateau** | Phase 2 coding assistance 常见增效天花板 |
| **Polished artifacts** | 给人类审的 synthesis + 决策点 + demo |
| **how skill / why skill** | 教 agent rigorously 读 codebase 的 skill 原子 |
| **Issue Glass** | Cursor 内测 Glass 的 dogfood bug 频道 |
| **Agent manager (EM agent)** | 自治、周期性 synthesize 下层 automation |
| **Agentic risk detection** | PR 风险评分 → 低风险 fast path |
| **Skills 原子单元** | 小 skill 组合成更大 agentic experience |

---

## 值得记住的原话

> **"About 98% of merge commits are being written by AI."**（Cursor）  
> 约 98% 的 merge commits 由 AI 写（Cursor 自身）。

> **"The vibe number... plateau is maybe 40-ish percent."**  
> 平均 plateau 大概 40% 增效。

> **"We've only replaced like a tiny part of the SDLC... we found all of these new bottlenecks."**  
> 我们只换了 SDLC 一小角……新瓶颈全冒出来了。

> **"What are the things we still want humans to do?"**  
> 哪些步骤还要人做？——从这角度设计 agent 系统。

> **"Skills are the atomic unit."**  
> Skills 是原子单元。

> **"I've got a guy on it."**（= booted a cloud agent）  
> 「我派了人」= 起了 cloud agent。

> **"Fixed over 200 vulnerabilities, almost all automatically fixed."**  
> 修 200+ 漏洞，几乎全自动。

> **"Why do humans get this channel and the agents don't?"**（→ AgentX）  
> 为啥人有 DevX 频道，cloud agent 没有？

---

## 小结

**这期最核心的判断：** 第三纪元不是「AI 写更多代码」，而是 **STLC 全链建 Agent 团队 + 人类审 polished artifacts**；卡在 40% 是因为 **只 automate 了 build 一角**——Cursor 用 PM/EM/Security/Growth agent 证明 **plan/ship/growth 的 meta 任务** 同样可链 skills 自治化。

**读完应带走：**
- **how skill** 这类原子 skill，是让 cloud agent 「挖 codebase」从 stuck 到有用的关键。  
- **Artifact 设计**：每段 STLC 给人 **决策清单 + demo**，不是 dump 2 万行 PR。  
- **组织**：factory 文化 + champion + 新 team 配比，和工具同等重要。

**和 vault 的关系：** 接 [[Cursor-128个Agent团队协作]]、[[IBM团队-Harness工程详解]]、[[WorkOS-创建和使用Skills方法论]]、[[MOC - Harness Engineering]]。

---

## 行动启示

1. **画 STLC，标人类必审节点**——再决定 agent 产什么 artifact。  
2. **从 annoyance 出发**（Issue Glass）→ skill → 小 automation → 高层 synthesize agent。  
3. **写 how skill**：教 harness 如何 rigorous inspect codebase。  
4. **PR 加 agent 风险分**：低风险 fast path，高风险 smart route。  
5. **Growth/PM/Security 的 admin 链**：Often 比再加一个 coding agent ROI 高。  
6. **设 AgentX/DevX 对称频道**：agent 失败模式也要可见、可修。

---

## 相关阅读

- [[Cursor-128个Agent团队协作]] — Cursor 大规模 multi-agent 编排  
- [[WorkOS-创建和使用Skills方法论]] — Skills 创建与使用  
- [[IBM团队-Harness工程详解]] — harness、verify、guardrails  
- [[MOC - Harness Engineering]] — Harness 横切索引  
- [[Loop-Agent Loop到底是什么]] — Agent loop 与 STLC 链式系统  

---

## 来源

- **视频**：[BV1MQVf6SEST](https://www.bilibili.com/video/BV1MQVf6SEST/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Cursor 副总裁  
- **时长**：~20:39  
- **转写**：Recastory `bilibili-retranscribe/BV1MQVf6SEST/`（FunASR SenseVoice + cam++，**asr v2** 10 段）  
- **版本**：v2 读者向讲义（2026-07-02）
