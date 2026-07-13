---
name: vskill-vault-curate
description: 收录 URL、PDF、截图、粘贴或用户提供的B站图文专栏到当前 Obsidian Markdown vault。
---

# Vault Curate Adapter

必须完整读取 canonical `99-System/Skills/vskill-vault-curate/SKILL.md` 和 `99-System/Agent/INGEST-CONTRACT.md` 后执行。

B 站 opus/cv 图文专栏任务必须先读 `99-System/Skills/vskill-vault-curate/SUBDOC - B站图文专栏精华收录.md`。图片与 Recastory/ASR 默认跳过；历史核验才读取 Legacy 索引。

输入：外部来源及可选主题提示。输出：canonical Markdown 笔记；B站专栏使用 `bilibili_opus_ingest_v1` 报告。完成前运行适用校验；失败时报告 incomplete，不宣称完成。
