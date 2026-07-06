# CLAUDE.md

> 本仓库是 AI 知识库 vault。协议见 [AGENTS.md](./AGENTS.md)；能力见 [99-System/Skills/INDEX.md](./99-System/Skills/INDEX.md)。

## Agent 进入顺序

1. 读 **AGENTS.md**（目录 / frontmatter / tag / 反向链 / 收录 SOP）
2. 读 **Skills INDEX** → 按任务加载 `vskill-*`
3. **形态专项**：B 站 BV / Recastory ASR → 先读下方「B 站 ASR 收录」再动手

## 任务路由

| 用户意图 | 加载 |
|----------|------|
| 收录 URL / 公众号 / 粘贴 | `vskill-vault-curate` |
| **B 站视频 / ASR 转写 / 新 BV** | **↓ B 站 ASR 收录（必读）** |
| 写观点文 / 对谈稿 | `vskill-vault-write` |
| 找反向链 | `vskill-vault-relate` |
| 跨笔记讨论 | `vskill-vault-discuss` |
| 建 / 改 MOC | `vskill-vault-moc-builder` |

## B 站 ASR 收录（agent 必读）

**入口文档**（决策树 + 经验 + 反模式 + 脚本口令）：

`99-System/Skills/vskill-vault-curate/SUBDOC - ASR内容分轨与收录决策.md`

**铁律**：**1 BV = 1 篇** `02-Resources/AI and Agents/B站视频知识库/{子目录}/{主题}.md`；禁止 `{主题} - 对谈稿.md` 双文件。

**三轨**（形态 > 等级；对谈 **禁止** 压成九段摘要）：

```
reconcile 定 S/A（bilibili-ingest-reconcile.py）
  ├─ S：UP 专栏 ≥3k + 主持人/嘉宾 → Host-Guest 对谈 · 专栏主源
  ├─ A-dialogue：无专栏 + 访谈/webinar → Host-Guest 对谈 · ASR 主源
  └─ A-lecture：无专栏 + 单人教程/解读 → 九段讲义 v3
→ gap-check 全绿（bilibili-v3-gap-check.py）→ 反向链 → MOC
```

**子文档**（按轨加载）：`SUBDOC - B站视频 v3 工作流` · `Host-Guest 对谈稿` · `B站视频转写收录`（仅 A-lecture）

**skill**：`vskill-vault-curate` + `vskill-vault-write mode=dialogue`（S / A-dialogue 轨）
