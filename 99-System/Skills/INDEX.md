---
title: vskill Index
description: vault 自带 agent 能力索引——任何 agent 进入 vault 应先查本文件，按需加载 vskill-*
created: 2026-06-27
updated: 2026-07-13
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
> 3. **B 站 / ASR 收录** → [ASR 双轴决策 SUBDOC](./vskill-vault-curate/SUBDOC%20-%20ASR内容分轨与收录决策.md)（再按正文形态加载子文档）
> 4. 其他任务 → 按需加载 `vskill-*/SKILL.md`
>
> **命名规范**：`vskill-{能力域}-{具体能力}`（如 `vskill-vault-discuss`、`vskill-vault-write`）

---

## 可用 vskill

| 名称 | 状态 | 一句话描述 | 借鉴 | SKILL.md |
|---|---|---|---|---|
| `vskill-vault-discuss` | ✅ v0.2 可用（3 模式）| 基于 vault 笔记进行结构化讨论：summary / roundtable / companion 三模式 | `kb-retriever` + `ljg-roundtable` + `ljg-read` | [SKILL.md](./vskill-vault-discuss/SKILL.md) |
| `vskill-vault-write` | ✅ v0.5 可用 | blade 观点文，或带来源忠实度标记的 Host-Guest 对谈 | `ljg-writes` | [SKILL.md](./vskill-vault-write/SKILL.md) · [对谈稿 SUBDOC](./vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md) |
| `vskill-vault-curate` | ✅ v0.6 可用 | `vault_ingest_v2`；B站按“素材质量 × 正文形态”双轴收录 | `wiki-ingest` + filesystem | [SKILL.md](./vskill-vault-curate/SKILL.md) · **[ASR 双轴入口](./vskill-vault-curate/SUBDOC%20-%20ASR内容分轨与收录决策.md)** · [v4 工作流](./vskill-vault-curate/SUBDOC%20-%20B站视频%20v3%20工作流.md) |
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
vault-audit.py        ← 季度结构质量审计（已实现脚本）
    ↓
vskill-vault-moc-builder  ← MOC 重构 / 升级
    ↓
loop
```

**B 站 / ASR 收录（先读 [ASR 双轴决策 SUBDOC](./vskill-vault-curate/SUBDOC%20-%20ASR内容分轨与收录决策.md)）**：

```
动态发现素材 → material_tier: S|A|B
              → content_form: dialogue|lecture|roundtable
              → Pass 1 保留清单 → 按形态成稿
              → note validator + gap check → relate → MOC
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
