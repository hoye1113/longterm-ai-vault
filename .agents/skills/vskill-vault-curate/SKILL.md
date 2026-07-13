---
name: vskill-vault-curate
description: 收录 URL、PDF、截图、粘贴、B站视频或ASR到当前 Obsidian Markdown vault。
---

# Vault Curate Adapter

必须完整读取 canonical `99-System/Skills/vskill-vault-curate/SKILL.md` 和 `99-System/Agent/INGEST-CONTRACT.md` 后执行。

B 站、BV、Recastory 或视频 ASR 任务还必须先读 `99-System/Skills/vskill-vault-curate/SUBDOC - ASR内容分轨与收录决策.md`，再按 `content_form` 加载 dialogue、lecture 或 roundtable 所需子文档。

输入：外部来源及可选主题提示。输出：canonical Markdown 笔记和 `vault_ingest_v2` 报告。完成前运行适用的结构与 B 站专项校验；失败时报告 incomplete，不宣称完成。

