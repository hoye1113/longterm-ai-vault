---
title: MOC - AI Agent Development
description: 三元（Sitor AI）吃透 AI Agent 开发课程总索引 — 六大支柱 30+ 篇
created: 2026-06-10
tags:
  - ai_agent
  - moc
source: vault_initiative - moc - sitor-ai - ai_agent
---

# AI Agent Development

本 MOC 汇总 [三元（Sitor AI）](https://sitor.ai/courses/agent-fundamentals)「吃透 AI Agent 开发」课程的全部内容。课程从「底层实现级」角度拆解 Claude Code、Manus、OpenClaw 等真实产品的工程决策，按 PARA 原则归入 `01-Areas/AI Agent Development/` 下。

> 免责声明：本笔记仅供个人学习使用，版权归原作者 [[Sitor AI]] 所有。

## 六大支柱

课程围绕 Agent 开发的六大工程支柱展开，由内到外逐层构建：

| 支柱 | 一句话 | 人体类比 |
|------|--------|---------|
| Agent Loop | 单次会话内的循环执行 | 神经反射弧 |
| Tool System | 工具调用、权限、MCP | 双手 |
| Context Engineering | 上下文管理与压缩 | 工作记忆 |
| Memory | 跨会话的长期记忆 | 长期记忆 |
| Multi-Agent | 拆任务、分上下文 | 团队协作 |
| Harness Engineering | 权限、重试、Hook、生命周期 | 骨架 |

## 课程章节

### 01-Cognitive Calibration — 认知校准（5 篇 ✅）

- [[0-1 前言|前言 — 我为什么要做这门课]]
- [[1-1 搞定 Agent 六大支柱|搞定 Agent 六大支柱]]
- [[1-2 从 ChatBot 到 Agent|从 ChatBot 到 Agent]]
- [[1-3 大模型底层机制|大模型底层机制]]
- [[1-4 Agent 架构演进|Agent 架构演进]]

### 02-Agent Loop — Agent 循环机制（3 篇 ✅）

- [[2-1 流式响应工程真相|流式响应工程真相]]
- [[2-2 模型 API 容错|模型 API 容错]]
- [[2-3 Agent Loop 保险丝|Agent Loop 保险丝]]

### 03-Tool System — 工具系统（6 篇 ✅）

- [[3-1 Function Calling 与 Structured Output|Function Calling 与 Structured Output]]
- [[3-2 一次工具调用背后经历了什么|一次工具调用背后经历了什么]]
- [[3-3 Deferred Loading 和动态工具集|Deferred Loading 和动态工具集]]
- [[3-4 MCP 的工程真相|MCP 的工程真相]]
- [[3-5 Skills - Agent 时代的知识分发系统|Skills - Agent 时代的知识分发系统]]
- [[3-6 生产级权限系统的四层防线|生产级权限系统的四层防线]]

### 04-Context Engineering — 上下文工程（10 篇 ✅）

- [[4-1 Context Engineering 全景|Context Engineering 全景]]
- [[4-2 System Prompt 工程化与 Context Rot|System Prompt 工程化与 Context Rot]]
- [[4-3 上下文压缩|上下文压缩]]
- [[4-4 Cache 全解与成本控制|Cache 全解与成本控制]]
- [[4-5 Just-In-Time Context|Just-In-Time Context]]
- [[4-6 RAG 全流程|RAG 全流程]]
- [[4-7 检索优化|检索优化]]
- [[4-8 LLM 编译知识库|LLM 编译知识库]]
- [[4-9 Agent 的记忆系统|Agent 的记忆系统]]
- [[4-10 记忆的五种失效模式|记忆的五种失效模式]]

### 05-Memory — 记忆系统（待收录 ❌）

> 跨会话的长期记忆，与 Context Engineering（单次会话内）形成互补。

### 06-Multi-Agent — 多 Agent 协作（待收录 ❌）

> 不是分角色，是分上下文。核心价值在于隔离上下文窗口。

### 07-Harness Engineering — 骨架工程（待收录 ❌）

> 模型外面那层壳——权限、重试、Hook、生命周期管理。

## 快速导航

| 章节 | 篇数 | 状态 |
|------|------|------|
| 01-Cognitive Calibration | 5 | ✅ 已完成 |
| 02-Agent Loop | 3 | ✅ 已完成 |
| 03-Tool System | 6 | ✅ 已完成 |
| 04-Context Engineering | 10 | ✅ 已完成 |
| 05-Memory | — | ❌ 待收录 |
| 06-Multi-Agent | — | ❌ 待收录 |
| 07-Harness Engineering | — | ❌ 待收录 |

**已收录**：24 / 30+ 篇

## 关联笔记

- [[MOC - Agent Theory and Design]] — 外部文章索引
- [[MOC - Loock AI 全栈课程|Loock AI 全栈课程]] — LangGraph.js + Coding Agent 实战课程
- [[MOC - Agent Theory and Design]] — 视频转录知识库
