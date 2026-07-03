---
title: "B站 ingest 对账审计"
created: 2026-07-03
tags: [audit, bilibili]
---

# B站 ingest × vault 对账（Phase 0）

> Recastory workspace · manifest 32 条 · 生成 2026-07-03

## 汇总

- **素材等级**：S=15 · S-=0 · A=17 · B=0
- **enrich**：ok=11 · partial=17 · skipped=4
- **column_article**：15/32
- **vault 文件存在**：32/32

## 分级说明

| 等级 | 条件 | Phase 3 策略 |
|------|------|--------------|
| **S** | column ≥3k 字 + 含主持人/嘉宾 | **canonical 单篇** Host-Guest v3.2（`{主题}.md` + 附录） |
| **S-** | column ≥1k 字 | 优先读 column |
| **A** | 仅有 video_description | 轻量 v3 |
| **B** | 仅 ASR | 补来源 |

## 全量清单

| BV | 等级 | enrich | column | 字 | 对话体 | column_url | Host×Guest | vault | 备注 |
|----|------|--------|--------|-----|--------|------------|------------|-------|------|
| BV12x1xB8E7b | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV14nrMBKENb | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV174GU6AEZY | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV18bjG6fEi7 | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV19MzXBNESV | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1EwK96AEyU | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1Mpf9B5Egk | A | partial | — | — | — | — | — | ✓ | 未找到 UP 主评论 |
| BV1NpAHzZEcc | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1PnQfBvEs3 | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1UajG6oEvj | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1WnctziEac | A | partial | — | — | — | — | — | ✓ | opus 页面未解析出专栏链接: https://www.bilibili.com/opus/45649506 |
| BV1ZWTL64Erg | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1cVjN6oEwx | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1eyBgB2EbX | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1ixKX6oEzK | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1kWctzeEYK | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV1o4TL6sExw | A | partial | — | — | — | — | — | ✓ | UP 主评论中未解析出 http 链接 |
| BV12qTu6WETP | S | skipped | ✓ | 13023 | ✓ | ✓ | 嘉宾）：一场剧变即将到来。每个人都将在电脑上拥有属于自己的专属个人助理，它能让你 × Quill Delta → Markdown）

---

## 摘要

导读： | ✓ | — |
| BV14AjN6eEcg | S | ok | ✓ | 21501 | ✓ | ✓ | 每分钟工具调用数）来提升产出。

1. 知识库是 Agent 廉价且高效的真相来 × rank）和较小的样本量下表现出色，但它有一个性能弧线。随着样本数量增加，它们很 | ✓ | — |
| BV18LV66aEG9 | S | ok | ✓ | 6928 | ✓ | ✓ | — | ✓ | — |
| BV18hjG6bE6t | S | ok | ✓ | 18122 | ✓ | ✓ | 如园艺管理、特定金融需求）即时编写并运行软件，操作系统的原生功能将被 AI 彻底 × 主持人）：我们可以编辑一下这个场景，让它看起来像我们预想的那样。是的。

Log | ✓ | — |
| BV1BLGH6REyX | S | ok | ✓ | 15756 | ✓ | ✓ | — | ✓ | — |
| BV1JvjP6XE1k | S | ok | ✓ | 7186 | ✓ | ✓ | — | ✓ | — |
| BV1LFjV6BEpe | S | ok | ✓ | 15872 | ✓ | ✓ | Skills）”，如“热核审查”能让代理进入极端严苛的审计模式。这种将工作流代码 × 主持人）：你现在有正在运行的代理吗？我知道你已经设置好了。你的代理今天在忙什么？ | ✓ | — |
| BV1MFjN6iEFU | S | ok | ✓ | 18629 | ✓ | ✓ | 如商业地产、餐饮）。通过针对高频、利基的工作流程提供AI加速服务，初创公司可以快 × 主持人）：如何成为一家AI原生公司？在本期节目中，我们将用不到60分钟的时间，为 | ✓ | — |
| BV1MQVf6SEST | S | skipped | ✓ | 8469 | ✓ | ✓ | — | ✓ | — |
| BV1NuGU6yE1b | S | ok | ✓ | 22957 | ✓ | ✓ | 嘉宾）：我从未见过如此陡峭的增长，而且它还在不断地呈指数级增长。Claude C × 如社交连接）上，因为 AI 可以写出任何代码，但无法瞬间复制用户关系网。

1. | ✓ | — |
| BV1dZLS66E3m | S | ok | ✓ | 7293 | ✓ | ✓ | — | ✓ | — |
| BV1eWGH6JE6m | S | skipped | ✓ | 9345 | ✓ | ✓ | — | ✓ | — |
| BV1i9E366EAr | S | skipped | ✓ | 13633 | ✓ | ✓ | Quill Delta → Markdown）

---

## 摘要

导读： × 主持人）：马蒂亚斯，感谢您的加入。

Matias Castello | ✓ | — |
| BV1iH7R6tEfJ | S | ok | ✓ | 18084 | ✓ | ✓ | RL）阶段的表现和在生产环境中的行为就会有所不同。

Sonya Huang × 基于用户反馈）作为持续优化的手段。Federico 指出，在线 RL 存在悖论： | ✓ | — |
| BV1s2Gd6aEF7 | S | ok | ✓ | 20702 | ✓ | ✓ | 如判断 AI 幻觉、内化知识）将超越基础技能；他主张通过“代码即论文”等方式，鼓 × 主持人）： 诺亚·布莱尔的 Claude Code 设置可能是我见过最酷的。他在 | ✓ | — |

## Phase 1 待补 column（partial 且无 column）

- BV1NpAHzZEcc → `Agent架构与平台/Karpathy爆火项目-AutoResearch解读与启发.md`
- BV1kWctzeEYK → `Agent架构与平台/30分钟精通OpenClaw.md`
- BV1WnctziEac → `Agent架构与平台/OpenClaw创始人-我是如何使用OpenClaw的.md`
- BV174GU6AEZY → `Agent架构与平台/5次创业者-AI智能体独自经营初创公司.md`
- BV1eyBgB2EbX → `Agent架构与平台/Claude Code负责人-AI原生团队如何使用AI.md`
- BV1Mpf9B5Egk → `Agent架构与平台/Claude Code实战-构建一个AI数据分析师.md`
- BV19MzXBNESV → `Agent架构与平台/OpenAI官方-Codex新手教程.md`
- BV14nrMBKENb → `Agent架构与平台/OpenAI员工-上下文工程和Agent记忆.md`
- BV1PnQfBvEs3 → `Agent架构与平台/Agent实战-打造一个AI Agent的完整教程.md`
- BV12x1xB8E7b → `Agent架构与平台/Manus创始人-深度干货-上下文工程的最佳实践.md`
- BV1ixKX6oEzK → `Agent架构与平台/DeepMind团队-当数百万Agent相遇.md`
- BV1o4TL6sExw → `Agent架构与平台/Databricks-企业级Agent生产实践.md`
- BV1ZWTL64Erg → `Agent架构与平台/PlanetScale-Agent时代的基础设施.md`
- BV18bjG6fEi7 → `Agent架构与平台/WorkOS-创建和使用Skills方法论.md`
- BV1cVjN6oEwx → `Agent架构与平台/Loop-Agent Loop到底是什么.md`
- BV1EwK96AEyU → `AI评估与研究/OpenAI评估团队-不再低估模型.md`
- BV1UajG6oEvj → `行业观点与组织/a16z-AI并非泡沫.md`

## 已知 vault 与 ingest 冲突

- **A8 BV12qTu6WETP**：vault「Deep Dive Podcast」→ column **Marina Mogilko × Thibault Sottiaux**
