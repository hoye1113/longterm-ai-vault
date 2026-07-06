---
title: "Scripts - 运行入口"
tags: [notes, skills]
created: 2026-07-06
source: vault_initiative - scripts_readme
description: "99-System/scripts 下脚本的统一入口，包含用途、常用命令和环境准备。"
---

# Scripts - 运行入口

这个目录放的是 vault 的本地自动化脚本。它们分成两类：

- `vault-audit.py`
  - 全库审计：frontmatter、tag、wikilink、孤岛、文件名规则
- `bilibili-*.py`
  - B 站视频 v3 工作流：对账、补字段、批处理、合并 canonical、spot check

## 运行前准备

### 1. Python

- 建议版本：`Python 3.11+`
- 根目录已声明：[pyproject.toml](file:///d:/workSpace/obsidian_repository/pyproject.toml)

### 2. PowerShell 环境变量

如果你要让 Claude Code 通过 `.mcp.json` 连接 Obsidian MCP，先在当前 PowerShell 会话注入：

```powershell
$env:OBSIDIAN_MCP_TOKEN = "your-local-rest-api-token"
```

如果你想让每次打开 PowerShell 都自动生效，把同一行写进你的 profile：

```powershell
code $PROFILE
```

当前机器的 PowerShell profile 路径是：

```text
C:\Users\38788\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

说明：

- 不要把真实 token 写回仓库文档
- `.mcp.json` 现在只保留环境变量占位

## 常用命令

### 1. 全库审计

```powershell
python 99-System/scripts/vault-audit.py
```

输出：

- 审计报告写入 `99-System/audit-report.md`

### 2. B 站 ingest 对账

```powershell
python 99-System/scripts/bilibili-ingest-reconcile.py
```

用途：

- 对齐 ingest 和 vault
- 判定 `material_tier`

参考：

- [SUBDOC - ASR内容分轨与收录决策.md](file:///d:/workSpace/obsidian_repository/99-System/Skills/vskill-vault-curate/SUBDOC%20-%20ASR%E5%86%85%E5%AE%B9%E5%88%86%E8%BD%A8%E4%B8%8E%E6%94%B6%E5%BD%95%E5%86%B3%E7%AD%96.md)
- [SUBDOC - B站视频 v3 工作流.md](file:///d:/workSpace/obsidian_repository/99-System/Skills/vskill-vault-curate/SUBDOC%20-%20B%E7%AB%99%E8%A7%86%E9%A2%91%20v3%20%E5%B7%A5%E4%BD%9C%E6%B5%81.md)

### 3. B 站 canonical 合并

单篇：

```powershell
python 99-System/scripts/bilibili-canonical-merge.py --stem "{主题}" --apply
```

批量：

```powershell
python 99-System/scripts/bilibili-canonical-merge.py --all-s --apply
python 99-System/scripts/bilibili-canonical-merge.py --fix-wikilinks --apply
```

### 4. B 站遗漏检查

```powershell
python 99-System/scripts/bilibili-v3-gap-check.py
```

用途：

- 检查 v3 rollout 是否还有漏项
- 仅校验 manifest 中带 `vault_path` 的条目；`B站视频知识库/README.md` 不计入 32 篇计数

### 5. 长视频 factual spot check

先看 backlog：

```powershell
python 99-System/scripts/bilibili-spot-check.py --list-long
```

生成单篇检查表：

```powershell
python 99-System/scripts/bilibili-spot-check.py "<笔记路径>" -o 99-System/audit/spot-check-<BV>.md
```

## 推荐执行顺序

如果你在跑 B 站 v3 工作流，建议顺序是：

```text
ingest reconcile
-> 读 ASR 分轨决策 SUBDOC（定 S / A-dialogue / A-lecture）
-> enrich / 写正文（dialogue 或九段）
-> canonical merge（仅存量双文件）
-> gap check
-> long-video spot check
```

对应命令见上面四组入口。

## 脚本索引

| 脚本 | 用途 |
|---|---|
| `vault-audit.py` | 全库审计 |
| `bilibili-ingest-reconcile.py` | ingest × vault 对账 |
| `bilibili-concept-cn-fill.py` | 补中文概念字段 |
| `bilibili-vault-v3-light.py` | 轻量生成/整理 v3 内容 |
| `bilibili-vault-v3-batch.py` | 批量处理 v3 内容 |
| `bilibili-vault-s-tier-fm.py` | 处理 S 级 frontmatter |
| `bilibili-canonical-merge.py` | 合并 canonical |
| `bilibili-v3-gap-check.py` | 漏项审计 |
| `bilibili-spot-check.py` | 长视频 factual spot check |
| `bilibili-partial-enrich-run.py` | 局部 enrich 执行入口 |
| `bilibili-lecture-colloquial-pass.py` | 讲义口语化修订 |

## 相关文档

- [README.md](file:///d:/workSpace/obsidian_repository/README.md)
- [AGENTS.md](file:///d:/workSpace/obsidian_repository/AGENTS.md)
- [vskill Index](file:///d:/workSpace/obsidian_repository/99-System/Skills/INDEX.md)
- **[SUBDOC - ASR内容分轨与收录决策.md](file:///d:/workSpace/obsidian_repository/99-System/Skills/vskill-vault-curate/SUBDOC%20-%20ASR%E5%86%85%E5%AE%B9%E5%88%86%E8%BD%A8%E4%B8%8E%E6%94%B6%E5%BD%95%E5%86%B3%E7%AD%96.md)**（B 站 / ASR 收录入口）
- [SUBDOC - B站视频 v3 工作流.md](file:///d:/workSpace/obsidian_repository/99-System/Skills/vskill-vault-curate/SUBDOC%20-%20B%E7%AB%99%E8%A7%86%E9%A2%91%20v3%20%E5%B7%A5%E4%BD%9C%E6%B5%81.md)
- [SUBDOC - Spot check（长视频 factual）.md](file:///d:/workSpace/obsidian_repository/99-System/Skills/vskill-vault-curate/SUBDOC%20-%20Spot%20check%EF%BC%88%E9%95%BF%E8%A7%86%E9%A2%91%20factual%EF%BC%89.md)
