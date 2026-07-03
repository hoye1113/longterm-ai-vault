---
title: vskill Index
description: vault 自带 agent 能力索引——任何 agent 进入 vault 应先查本文件，按需加载 vskill-*
created: 2026-06-27
updated: 2026-07-03
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
| `vskill-vault-write` | ✅ v0.3 可用 | blade 观点文 **或** Host-Guest 对谈稿 v3.2；B 站 S 级落盘 **单篇 canonical** `{主题}.md` | `ljg-writes` | [SKILL.md](./vskill-vault-write/SKILL.md) · [对谈稿 SUBDOC](./vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md) |
| `vskill-vault-curate` | ✅ v0.4 可用 | 收录 §8 SOP；B 站 **v3 工作流**（S→canonical 单篇 / A→讲义九段） | `wiki-ingest` + `kimi-webbridge` | [SKILL.md](./vskill-vault-curate/SKILL.md) · [B站](./vskill-vault-curate/SUBDOC%20-%20B站视频转写收录.md) · [v3 工作流](./vskill-vault-curate/SUBDOC%20-%20B站视频%20v3%20工作流.md) |
| `vskill-vault-relate` | ✅ v0.1 可用 | 给定笔记，扫描 vault 输出 top-N 反向链候选（4 维评分 + warnings）| `kb-retriever` + `vskill-vault-discuss` | [SKILL.md](./vskill-vault-relate/SKILL.md) |
| `vskill-vault-moc-builder` | ✅ v0.1 可用 | 降秩 + 9 种取景框——合并 / 拆分 / 新建 / 审计 vault MOC | `ljg-rank` + `wiki-ingest` | [SKILL.md](./vskill-vault-moc-builder/SKILL.md) |

## 计划中 vskill（未实现）

| 名称 | 计划能力 | 优先级 | 借鉴来源 |
|---|---|---|---|
| `vskill-vault-audit` | 季度审计：孤岛 / 死链 / tag 一致性 / frontmatter 完整性 | P2 | `neat-freak` + `reality-check` |
| `vskill-vault-concept-anatomy` | 8 刀解剖一个 AI 时代术语（含"元反思"第八刀）| P3 | `ljg-learn` |
| `vskill-vault-lineage` | 递归 5 层找 vault 内主题溯源链 + 问题为轴叙事 | P3 | `ljg-paper-river` |

---

## vskill 工作流（闭环）

```
[用户需求]
    ↓
vskill-vault-discuss  ← 检索 + 跨笔记对比
    ↓
vskill-vault-write    ← blade 观点文 | dialogue 对谈稿（见 SUBDOC）
    ↓
vskill-vault-curate   ← 收录 + 加 MOC（访谈可先 curate 再 write dialogue）
    ↓
vskill-vault-audit    ← 季度质量审计（计划中）
    ↓
vskill-vault-moc-builder  ← MOC 重构 / 升级
    ↓
loop
```

**访谈 / B 站 S 级（column 对话体）**：

```
reconcile 定 S → write mode=dialogue（v3.2）→ 讲义保留索引 → relate → MOC
详见 SUBDOC - B站视频 v3 工作流
```

**B 站 A 级（仅 ASR + description）**：

```
curate 九段讲义 v3 → v3-batch 机械门 → spot check（≥45min）→ MOC
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
