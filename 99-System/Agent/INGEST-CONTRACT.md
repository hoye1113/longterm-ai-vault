---
title: "Vault 收录执行契约 v2"
tags: [notes, skills, ai_agent]
created: 2026-07-13
source: vault_initiative - agent_control_plane
description: "定义通用收录契约与 B 站图文专栏精华收录状态机、报告接口和完成条件。"
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

## B 站图文专栏状态机

用户提供单篇 opus/cv 时使用 `bilibili_opus_ingest_v1`：

```text
PREFLIGHT -> DISCOVER -> MATCH -> ADMISSION -> EXTRACT
          -> CLASSIFY -> TRANSFORM -> RELATE -> VALIDATE/REPORT
```

- `DISCOVER`：读取文字正文和页面元数据，提取 opus、cv、BV、标题、发布日期、作者和时长；图片全部跳过。
- `MATCH`：按 BV、opus、cv、source URL 查重，同一来源只保留一篇 canonical。
- `ADMISSION`：拒收纯新闻、重复观点、低价值教程和越界主题。
- `EXTRACT`：生成核心问题、主张、机制、数字、案例、限制、有效问答、实体和疑点清单。
- `CLASSIFY`：判断 C1/C2、S/A/B 与 lecture/dialogue/roundtable。
- `TRANSFORM`：删除重复摘要、宣传、寒暄和平台噪声，只保留知识增量。
- `RELATE`：选择 1–3 个真实相关链接或标 orphan；已有 MOC 可更新。
- `VALIDATE/REPORT`：运行 `bilibili-opus-validate.py`；不要求 Recastory、ASR、transcript 或 Spot Check。

Agent 不扫描 UP 主空间、不维护增量游标，只处理用户提供的单篇专栏。

## 双轴接口

```yaml
material_tier: S | A | B
content_form: dialogue | lecture | roundtable
dialogue_fidelity: source | reconstructed | none
question_source: transcript | editorial | none
factual_status: verified | partial | unverified
```

B 站专栏另写：

```yaml
source_type: bilibili_opus
source_tier: C1 | C2
primary_source: column
opus_id:
column_id:
bv:
```

- C1：正文、章节、BV、人物和时间锚点完整。
- C2：正文可用，但人物、问答、数字或 BV 映射存在缺口。

- S：素材完整、来源明确、正文充分且可核验。
- A：足以成稿，但人物、来源或结构有缺口。
- B：只能有限收录；无法保真则拒收。
- dialogue：追问、冲突或经历依赖问答推进。
- lecture：知识依赖、解释或操作步骤推进，即使存在两个 Speaker。
- roundtable：多人的独立立场及相互回应构成价值。

专栏 lecture 使用 `none/none`；末尾现场 Q&A 不改变 lecture。真实 dialogue/roundtable 使用 `source/transcript`。新专栏流程不生成 `reconstructed/editorial`，也不虚构 Moderator。

新收录必须写 `factual_status`：

- `verified`：专栏、BV 映射、身份、关键数字和限制已经核验，且没有关键未决项。
- `partial`：足以用于理解，但仍有明确的身份、数字、引语或来源缺口，写入 `unresolved_facts`。
- `unverified`：缺原始正文或无法保真，只能作为发现线索，不能作为可直接引用的事实源。

实际核验后写 `factual_reviewed` 与 `verification_basis`。没有该字段的旧笔记按 unverified 使用，但不批量写回。

## B 站专栏来源职责

- column：唯一默认正文主源，提供论述、章节、数字、案例、限制与问答。
- 内嵌视频元数据：BV、标题、时长和时间锚点。
- 官方原始页：只有关键身份或高风险数字需要复核时按需读取。
- 图片：始终跳过，不下载、不识别、不写入附件。
- Recastory/ASR：Legacy，仅用于历史笔记核验。

`verification_basis` 只列实际读取来源；未读视频页或官方页时只能写 `column`。

## Pass 1

```yaml
core_question:
core_claims: []
mechanisms: []
numbers: []
examples: []
constraints_and_counterexamples: []
valuable_questions: []
entities: []
uncertain_facts: []
```

## B 站专栏报告接口

```yaml
workflow: bilibili_opus_ingest_v1
source_id: {opus: "", column: "", bv: ""}
route: {source_tier: C1, material_tier: S, content_form: lecture}
target_path:
sources_read: [column]
sources_skipped: [images, transcript]
related_notes: []
moc_updates: []
checks:
  duplicate:
  source_completeness:
  identity:
  numeric_context:
  fidelity:
  retention:
  frontmatter:
  wikilinks:
unresolved: []
status: complete | incomplete | rejected
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

旧审计继续服务存量笔记。缺 transcript 只有在笔记明确声明 `ASR primary` 时构成 P0；完整专栏主源不因缺 transcript 报错。旧笔记不批量迁移，今后触达时渐进补齐专栏字段。

## 受控变更

新建 MOC、新 tag、覆盖已有 canonical 笔记必须先确认。更新已有 MOC 属于普通收录动作，但必须在报告中披露。

## 相关阅读

- [[MOC - Agent Theory and Design]]
