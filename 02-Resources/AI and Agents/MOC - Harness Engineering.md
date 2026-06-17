---
title: MOC - Harness Engineering
description: Harness Engineering 主题横切 MOC——跨课程、公众号、B站视频的 Harness 相关笔记，5 篇核心 + 跨 MOC 链接
created: 2026-06-11
updated: 2026-06-11
tags:
  - ai_agent
  - harness_engineering
  - moc
source: vault_initiative - moc - ai_agent - harness_engineering
---

# MOC - Harness Engineering

> **横切 MOC**：跨 `02-Resources/AI and Agents/` 子目录、`01-Areas/AI Agent Development/` 子目录的 Harness 主题笔记汇总。
>
> **核心定义**（来自 [[2026 年 Agent 最重要的工程概念 Harness Engineering]]）：harness = 围绕 Agent 的工程系统（工具、约束、反馈、安全、记忆），让 AI 从"能力强但不可预测"变成"稳定可靠能交付"。
>
> 5 篇核心笔记 + 跨 MOC 链接 = 完整的 Harness 主题地图。

---

## 核心笔记（按权威
| # | 笔记 | 来源 | 视角 | 一句话 |
|---|------|------|------|--------|
| 1 | [[2026 年 Agent 最重要的工程概念 Harness Engineering]] | 公众号（特工宇宙翻译 OpenAI 官方）| **OpenAI 5 个月实验** | harness = docs/ 当 source of truth + linter 强制不变量 + 黄金原则 |
| 2 | [[祝贺Claude Code成功越狱，获得永生]] | 公众号（花叔）| **Anthropic 源码逆向** | harness 内部 6 大模块：system prompt / 四层权限 / 记忆 / 9 段式压缩 / swarm / grep |
| 3 | [[Anthropic Agent 工程实战指南 - 从入门到生产落地]] | 公众号（Anthropic 官方汇编）| **Anthropic 完整方法论** | 15 篇博客按"入门-进阶-核心-高级-生产"5 模块系统化 |
| 4 | [[IBM团队-Harness工程详解]] | B站视频 | **工程可靠性视角** | Harness = 登山绳 + 黑盒模型对抗；可靠性比聪明重要 |
| 5 | [[别再搭 Harness 了，先把你的痛点解决，用最笨的方式]] | 公众号（三元同学）| **反规范视角** | 马斯克五步法：先痛点后系统，不先搭系统 |
| 6 | [[Loop Engineering 橙皮书 - 花叔]] | GitHub 橙皮书系列（花叔）| **Loop = Harness 上一层** | 别再自己一句句指挥 agent；五动作循环 + 六零件 + 四笔代价 |
点后系统，不先搭系统 |

---

## Harness 的 6 大核心模块

> 把 5 篇笔记的"harness 是什么"汇总成 6 大模块，每个模块对应至少 2 篇笔记的具体实现：

| 模块 | 花叔（Claude Code）| OpenAI 实验 | Anthropic 官方 |
|------|-------------------|------------|----------------|
| **System Prompt 工程** | 静态/动态分界 + 缓存 | "地图而非说明书" 100 行 AGENTS.md | 第 15 章 system prompt 设计 |
| **权限 / 安全** | 四层流水线 + 熔断 | 用户类型 `ant` 内部版 | 第 13 章 沙箱隔离 |
| **记忆系统** | auto memory + autoDream（只记偏好不记代码）| 上下文评分 + 渐进披露 | 第 7 章 + 第 9 章 5 种失效模式 |
| **上下文压缩** | 9 段式结构化提取 | 任务树评分 + 关键信息 | 第 4 章 缓存 + 成本 |
| **多 Agent 协作** | utils/swarm + 邮箱文件 + 权限冒泡 | 团队级 swarm 编排 | 第 10 章 Anthropic 实战 |
| **可观测性 / 反馈** | 内部 git worktree + DevTools + PromQL/LogQL | doc-gardening + 黄金原则 + 熵治理 | 第 12 章 评测体系 |

> **对比建议**：先读 [[祝贺Claude Code成功越狱]]（最具体可看源码）→ 再读 [[2026 年 Agent 最重要的工程概念 Harness Engineering]]（最系统的搭建方法论）→ 最后用 [[Anthropic Agent 工程实战指南 - 从入门到生产落地]] 查具体模块的实现。

---

## 跨 MOC 链接

| 横切主题 | MOC |
|----------|-----|
| Claude Code 实践 | [[MOC - Agent Theory and Design#B. Claude Code 实战（3 篇）]] |
| Coding Agent 体系 | [[MOC - Loock AI 全栈课程]] — 包含 LangGraph.js Coding Agent 实现 |

### 关联 Areas
- [[AI Agent Development]] — sanyuan 的系统课程（Context Engineering / Memory 等模块有 Harness 理论对应）
- [[Workflow and 
- **总笔记数**：6 核心 + 3 跨 MOC 链接
- **最后更新**：2026-06-15（新增 Loop Engineering）
- **入选标准**：笔记主题必须直接讨论"围绕 Agent 的工程系统"（不是单纯的"Agent 本身"或"Agent 怎么用"）
