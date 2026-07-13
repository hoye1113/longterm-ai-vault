# AGENTS.md - Obsidian Vault Agent 启动契约

> 本仓库是面向 **AI Agent 时代** 的长期 Obsidian Markdown 知识库。Markdown 文件是唯一事实源；Obsidian 只负责人工阅读、编辑与链接呈现，不是 Agent 写入网关。

## 每次进入仓库

1. 先读本文件，确认项目边界和权限。
2. 按任务读取 [ROUTER](99-System/Agent/ROUTER.md)。
3. 收录任务必须再读 [INGEST-CONTRACT](99-System/Agent/INGEST-CONTRACT.md) 和对应 canonical Skill。
4. 写正文前读取 [DENSITY-PROFILE](99-System/Agent/DENSITY-PROFILE.md)。
5. 目录、PARA、frontmatter、tag 与 MOC 细则见 [PROJECT](99-System/Agent/PROJECT.md)。

权威顺序：用户当前指令 > 本文件 > Agent 工作流契约 > canonical Skill > 形态专项 SUBDOC > README > 历史审计报告。

## 任务路由

| 用户意图 | canonical Skill |
|---|---|
| 收录 URL、PDF、截图、粘贴或 B 站图文专栏 | `vskill-vault-curate` |
| 基于素材写观点文或对谈稿 | `vskill-vault-write` |
| 找反向链 | `vskill-vault-relate` |
| 基于已有笔记讨论 | `vskill-vault-discuss` |
| 新建、合并、拆分或审计 MOC | `vskill-vault-moc-builder` |

B 站 opus/cv 图文专栏任务必须先读：

`99-System/Skills/vskill-vault-curate/SUBDOC - B站图文专栏精华收录.md`

Recastory/ASR 已冻结为 Legacy，不参与新收录；仅在核验历史笔记时按 Legacy 索引加载。

## 收录硬规则

所有收录按以下状态机执行：

```text
PREFLIGHT -> ADMISSION -> INVENTORY -> CLASSIFY -> TRANSFORM
          -> RELATE -> INTEGRATE -> VALIDATE/REPORT
```

- 写入前按 BV、opus ID、cv ID、`source_url` 查重。
- B 站新收录只接受用户提供的单篇 opus/cv；不自动扫描空间，不读取图片。
- B 站分类使用双轴：`material_tier: S|A|B` 与 `content_form: dialogue|lecture|roundtable`。
- 1 BV = 1 篇 canonical 笔记；禁止额外生成 `- 对谈稿.md`。
- 每篇笔记必须有语义相关的 `[[wikilink]]`；找不到则标 `status: orphan`，不得凑数。
- 已有 MOC 可随收录更新；新建 MOC、新 tag、覆盖已有 canonical 笔记必须先取得用户确认。
- 校验未通过或 `unresolved` 非空时，不得报告“收录完成”。
- 新 B 站专栏收录必须声明 `source_tier`、`primary_source: column` 与 `factual_status`；不要求 transcript、Recastory 或 Spot Check。
- 基于 vault 回答时，verified 可附来源引用；partial 使用保守措辞；unverified 只作为检索线索。

## 修改边界

- Agent 直接读写 vault 内 Markdown，不依赖 Obsidian MCP、REST API 或 Obsidian 进程。
- Recastory 等外部素材仓默认只读，除非用户明确要求修改。
- 不批量重写存量笔记；协议升级采用新收录强制、旧笔记渐进迁移。
- 不写入、回显或提交 token、cookie、密钥和本地凭据。
- 不创建重复内容，不用不相关链接破孤，不把编辑性提问伪装成现场原话。

## 完成定义

收录完成必须同时满足：目标路径正确、frontmatter 合法、tag 合法、来源可回溯、无重复 source/BV、正文符合密度契约、反向链或 orphan 已声明、已有 MOC 已处理、专项校验通过，并向用户披露路径、路由、变更和未解决项。
