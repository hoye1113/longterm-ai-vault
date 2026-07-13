---
title: "Agent 任务路由"
tags: [notes, skills, ai_agent]
created: 2026-07-13
source: vault_initiative - agent_control_plane
description: "把用户意图路由到唯一 canonical Skill，避免平台入口复制业务规则。"
---

# Agent 任务路由

| 意图 | 必读 | 不做 |
|---|---|---|
| 收录外部内容 | `vskill-vault-curate/SKILL.md` + Ingest Contract | 不直接开始写正文 |
| B 站/BV/Recastory/ASR | curate + `ASR内容分轨与收录决策` | 不凭 Speaker 数量或素材等级决定形态 |
| 写观点文 | `vskill-vault-write` blade | 不当作资料收录 |
| 写真实或重构对谈 | write dialogue + Host-Guest SUBDOC | 不把 editorial 问题冒充原话 |
| 找反向链 | `vskill-vault-relate` | 不凑链接 |
| 跨笔记讨论 | `vskill-vault-discuss` | 不修改 vault |
| MOC 设计 | `vskill-vault-moc-builder` | 未确认不新建 MOC |

canonical Skill 根目录：`99-System/Skills/`。平台适配层只负责发现和转发，若与 canonical 内容冲突，以 canonical 为准。

## B 站按需加载

1. 所有 B 站任务先读 ASR 决策入口。
2. `content_form: dialogue` 再读 Host-Guest SUBDOC。
3. `content_form: lecture` 再读 B站视频转写收录 SUBDOC。
4. `content_form: roundtable` 读取 dialogue 证据规则，并保留每位说话人的独立立场。
5. ≥45 分钟再读 Spot Check；不要为短视频加载该文档。

## 相关阅读

- [[MOC - Agent Theory and Design]]

