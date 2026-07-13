---
title: "Vault 收录执行契约 v2"
tags: [notes, skills, ai_agent]
created: 2026-07-13
source: vault_initiative - agent_control_plane
description: "定义收录状态机、双轴分类、报告接口、失败行为和完成条件。"
---

# Vault 收录执行契约 v2

## 状态机

1. `PREFLIGHT`：读取 AGENTS、Router、Contract、Density 和适用 Skill。
2. `ADMISSION`：判断主题相关性；查重 source、source_url、BV。
3. `INVENTORY`：发现实际素材路径，记录缺失和路径漂移，不拼固定路径。
4. `CLASSIFY`：独立判断素材质量与正文形态，写明理由。
5. `TRANSFORM`：先产 Pass 1 保留清单，再按形态成稿。
6. `RELATE`：扫描 top 5，选择 1–3 个或标 orphan。
7. `INTEGRATE`：写入 canonical 笔记并更新已有 MOC；受控变更先确认。
8. `VALIDATE/REPORT`：执行结构、来源、密度和专项检查；失败则报告 incomplete。

## 双轴接口

```yaml
material_tier: S | A | B
content_form: dialogue | lecture | roundtable
dialogue_fidelity: source | reconstructed | none
question_source: transcript | editorial | none
factual_status: verified | partial | unverified
```

- S：素材完整、来源明确、正文充分且可核验。
- A：足以成稿，但人物、来源或结构有缺口。
- B：只能有限收录；无法保真则拒收。
- dialogue：追问、冲突或经历依赖问答推进。
- lecture：知识依赖、解释或操作步骤推进，即使存在两个 Speaker。
- roundtable：多人的独立立场及相互回应构成价值。

非对谈必须使用 `dialogue_fidelity: none`、`question_source: none`。真实问答使用 `source/transcript`。编辑重构使用 `reconstructed/editorial`，不得伪装现场主持。

新收录必须写 `factual_status`：

- `verified`：身份、关键数字、引语、限制和来源路径已经核验；长视频已完成 spot check。
- `partial`：足以用于理解，但仍有明确的身份、数字、引语或来源缺口，写入 `unresolved_facts`。
- `unverified`：缺原始正文或无法保真，只能作为发现线索，不能作为可直接引用的事实源。

实际核验后写 `factual_reviewed` 与 `verification_basis`。没有该字段的旧笔记按 unverified 使用，但不批量写回。

## 来源职责

- metadata：身份、BV、日期、时长。
- description：导读、章节锚点、人物线索。
- transcript Markdown：原始论述、问答、数字、限定条件。
- transcript JSON：时间与 Speaker 核验。
- column：中文编辑骨架、重点与术语辅助。
- 原始节目页：人名、职位、节目名核实。

专栏不能替代 ASR/原页的事实核验。

## Pass 1

```yaml
core_questions: []
story_or_dependency_map: []
chapter_map: []
claims: []
mechanisms: []
numbers: []
examples_or_demos: []
constraints_and_counterexamples: []
quotes: []
entities: []
uncertain_facts: []
```

## 报告接口

```yaml
workflow: vault_ingest_v2
source_id:
route:
target_path:
source_inventory:
related_notes: []
moc_updates: []
checks:
  duplicate_source:
  source_completeness:
  frontmatter:
  tags:
  filename:
  wikilinks:
  retention:
  speaker_identity:
  factual_spot_check:
unresolved: []
status: complete | incomplete | rejected
```

`unresolved` 非空默认不能标 complete。允许的人工待核项必须进入笔记且在报告中披露。

## 存量可信度审计

`bilibili-trust-audit.py` 只读关联 vault、source inventory 与 Recastory manifest，按 P0–P3 输出风险队列。修复坚持最小变更：先纠正来源、人物和忠实度字段；只有证据明确时才改正文。

## 受控变更

新建 MOC、新 tag、覆盖已有 canonical 笔记必须先确认。更新已有 MOC 属于普通收录动作，但必须在报告中披露。

## 相关阅读

- [[MOC - Agent Theory and Design]]
