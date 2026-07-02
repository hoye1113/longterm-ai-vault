---
title: vskill Index
description: vault 自带 agent 能力索引——任何 agent 进入 vault 应先查本文件，按需加载 vskill-*
created: 2026-06-27
updated: 2026-07-02
tags:
  - moc
  - skills
source: vault_initiative - skills_index
---

# vskill Index

> **vskill-** = vault 内部约定的 agent 能力（区别于平台原生 skill，如 Claude Code 的 `.claude/skills/`）。
> **任何 agent 接触本 vault 时的发现顺序**：
> 1. 读 `AGENTS.md`（vault 协议）
> 2. 读本 `INDEX.md`（vskill 列表）
> 3. 按需加载 `vskill-*/SKILL.md`
>
> **命名规范**：`vskill-{能力域}-{具体能力}`（如 `vskill-vault-discuss`、`vskill-vault-write`）

---

## 可用 vskill

| 名称 | 状态 | 一句话描述 | 借鉴 | SKILL.md |
|---|---|---|---|---|
| `vskill-vault-discuss` | ✅ v0.2 可用（3 模式）| 基于 vault 笔记进行结构化讨论：summary / roundtable / companion 三模式 | `kb-retriever` + `ljg-roundtable` + `ljg-read` | [SKILL.md](./vskill-vault-discuss/SKILL.md) |
| `vskill-vault-write` | ✅ v0.1 可用 | 5 步切刀写一篇 1000-1500 字观点笔记（基于 vault anchor_notes）| `ljg-writes` | [SKILL.md](./vskill-vault-write/SKILL.md) |
| `vskill-vault-curate` | ✅ v0.2 可用 | 从外部（URL/PDF/视频/文本）收录到 vault——§8 SOP 7 步；B 站见 SUBDOC（含 ≥45min Spot check） | `wiki-ingest` + `kimi-webbridge` | [SKILL.md](./vskill-vault-curate/SKILL.md) · [B站](./vskill-vault-curate/SUBDOC%20-%20B站视频转写收录.md) · [Spot check](./vskill-vault-curate/SUBDOC%20-%20Spot%20check（长视频%20factual）.md) |
| `vskill-vault-relate` | ✅ v0.1 可用 | 给定笔记，扫描 vault 输出 top-N 反向链候选（4 维评分 + warnings）| `kb-retriever` + `vskill-vault-discuss` | [SKILL.md](./vskill-vault-relate/SKILL.md) |
| `vskill-vault-moc-builder` | ✅ v0.1 可用 | 降秩 + 9 种取景框——合并 / 拆分 / 新建 / 审计 vault MOC | `ljg-rank` + `wiki-ingest` | [SKILL.md](./vskill-vault-moc-builder/SKILL.md) |

## 计划中 vskill（未实现）

| 名称 | 计划能力 | 优先级 | 借鉴来源 |
|---|---|---|---|
| `vskill-vault-audit` | 季度审计：孤岛 / 死链 / tag 一致性 / frontmatter 完整性 | P2 | `neat-freak` + `reality-check` |
| `vskill-vault-concept-anatomy` | 8 刀解剖一个 AI 时代术语（含"元反思"第八刀）| P3 | `ljg-learn` |
| `vskill-vault-lineage` | 递归 5 层找 vault 内主题溯源链 + 问题为轴叙事 | P3 | `ljg-paper-river` |

---

## vskill 工作流（4 步闭环）

```
[用户需求]
    ↓
vskill-vault-discuss  ← 检索 + 跨笔记对比
    ↓
vskill-vault-write    ← 5 步切刀写笔记
    ↓
vskill-vault-curate   ← 自动收录 + 加 MOC（计划中）
    ↓
vskill-vault-audit    ← 季度质量审计（计划中）
    ↓
vskill-vault-moc-builder  ← MOC 重构 / 升级
    ↓
    loop (笔记变多后，重新做 discuss / write / curate / audit)
```

---

## 与平台 skill 的关系

- **不冲突**：vskill- 是 vault 私有约定，平台 skill 是平台能力。两者可以并存。
- **不替代**：vskill-vault-discuss 等不替代 Claude Code 的 Read / Grep 工具，而是规范"何时用 + 怎么用"。
- **不绑定**：vskill-* 是 markdown 文件，理论上任何能读文件的 agent 都能加载。

## 添加新 vskill 的流程

1. 在 `99-System/Skills/` 下创建 `vskill-{name}/` 目录
2. 写 `SKILL.md`（含 frontmatter + 触发条件 + 工作流 + 输入输出契约 + 例子）
3. 在本 `INDEX.md` 添加条目
4. 提交并推送（vault 是 Git 仓库）
