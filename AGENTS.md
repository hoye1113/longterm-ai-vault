# AGENTS.md - Obsidian Vault 长期主义规范

> **本文档是 vault 的"宪法"**。约束新笔记收录、跨会话维护、AI agent 协作。
> **限长原则**：≤ 3 页；超出部分拆 sub-doc。
> **适用对象**：vault 主人 + 协作 AI agents
> **最后更新**：2026-06-11 | **版本**：v1（圆桌共识落地）

---

## §1. 主题定位（收纳什么）

| 主题 | 占比 | 例 |
|---|---|---|
| **AI Agent 时代** | ≥ 80% | 理论 / 工具 / 职业 / Harness / FDE |
| 编程与工程实践 | ≤ 10% | 项目踩坑（如 ACP 集成） |
| 哲学与自我认知 | ≤ 10% | 与 AI 时代相关的自我认知 |
| **不收录** | — | 教程截图、纯新闻、临时任务、纯代码片段 |

---

## §2. PARA 目录（5 个一级目录）

```
vault/
├── 00-Inbox/              收件箱；新内容先放这里（≤ 10 个文件）
├── 01-Areas/              长期主题（仅 AI Agent Development）
├── 02-Resources/          主题参考资料（按主题分，不按来源）
│   ├── Agent Theory and Design/  公众号+视频+播客+哲学
│   ├── AI Coding Practice/       编程实战（Loock AI 课程等）
│   ├── Prompts/                  Prompt 库
│   └── Philosophy/               自我认知
├── 03-Archive/            归档（主题不再关注 / > 1 年未更新）
└── 99-System/             模板/附件/脚本
```

**判定流程**：新笔记只问 1 个问题 → "它是长期关注（→ Areas）还是参考资料（→ Resources）？"

---

## §3. frontmatter 必填模板（5 字段）

```yaml
---
title: "笔记标题"           # 必填
tags: [tag1, tag2]          # 必填，从 §4 字典选（YAML 列表）
created: 2026-06-11         # 必填，ISO 日期
source: https://...         # 必填（URL 或文件路径；多源用 YAML 列表）
description: "一句话摘要"   # 推荐
author:
  - "[[作者名]]"            # 推荐（多作者用 YAML 列表）
---
```

**特殊字段**（按笔记类型选填）：
- 视频：`genre` / `date` / `duration` / `saved` / `uploader` / `source_url`
- 播客：`speakers` / `date`
- MOC：`moc` 必含

---

## §4. tag 字典（统一风格）

**命名规则**：**全小写英文 + 下划线**（如 `harness_engineering`）

**主题 tag（一级）**：
- `ai_agent` — Agent 时代最大主题
- `ai_coding` — 编程实战
- `ai_evaluation` / `ai_safety` / `ai_career` / `ai_philosophy`

**形态 tag（二级）**：
- `article` / `video_transcript` / `podcast` / `course` / `moc` / `notes`

**来源 tag（三级）**：
- `zhihu` / `wechat` / `bilibili` / `youtube` / `podcast_rss`

**工具 tag**：
- `claude_code` / `codex` / `cursor` / `devin` / `chatgpt` / `claude` / `openai` / `anthropic`

**主题细分 tag**：
- `harness_engineering` / `memory` / `multi_agent` / `context_engineering` / `skills` / `hooks` / `mcp` / `prompting` / `fde`

**Pending tags 区域**（新增 tag 必须登记）：

```yaml
# 已登记 tag（2026-06-11 P1.1 补 15 个 Prompts 时引入）
tags_approved:
  - name: web_clipping
    proposed_by: ai_agent
    proposed_at: 2026-06-11
    reason: "Web Clipping 子主题——2 个 YouTube/网页抓取 Prompt（Clip YouTube Transcript, Clip Web Page）"
  - name: content_creation
    proposed_by: ai_agent
    proposed_at: 2026-06-11
    reason: "Content Creation 子主题——5 个内容创作 Prompt（Rewrite as tweet/thread, Generate TOC/glossary, Emojify）"
  - name: text_refinement
    proposed_by: ai_agent
    proposed_at: 2026-06-11
    reason: "Text Refinement 子主题——8 个文本润色 Prompt（Translate, Summarize, Simplify, Make shorter/longer, Remove URLs, Fix grammar, Explain like I am 5）"

# 提议新 tag 时，先在此登记；3 个月未审核自动失效
# tags_pending:
#   - name: new_tag
#     proposed_by: ai_agent
#     proposed_at: 2026-06-11
#     reason: "..."
```

**反向 tag 清单（不允许用）**：
- ❌ 中文 tag（`蜂群组织` / `自我认知` / `禅宗` / `心理学` / `哲学`）
- ❌ 连字符英文（`harness-engineering` / `human-in-the-loop` / `AI-era`）
- ❌ 旧名（`agents_knowledge` / `AI-Agent` / `openaicodex` / `AIAgent工作流方法论Skill`）
- ❌ 拼写不一致（`humanintheloop` / `human-in-the-loop`）

---

## §5. MOC 规范

**何时建 MOC**：
- 同主题 ≥ 3 篇笔记时
- 跨子目录但同一主题时（建横切 MOC）

**MOC 文件结构**：
- 命名：`MOC - {主题名}.md`（中英混排 OK）
- 位置：主题根目录
- frontmatter tags 必含 `moc`

**MOC 正文三段式**：
1. **主题简介**（2-3 句，含该主题的边界）
2. **核心笔记列表**（每条带 1 行说明，主题分组）
3. **关联笔记 / 横切 MOC 链接**

**两种 MOC 区分**：
- **主题 MOC**：一个子目录下所有笔记（如 `MOC - AI Agent Development`）
- **横切 MOC**：跨子目录但同主题（如 `MOC - Harness Engineering` 链 3 篇：OpenAI / Claude Code / IBM）

---

## §6. 文件命名规则

- ✅ 用 `-` 或空格分隔（如 `1-8 人机交互.md` / `AI 时代如何面试工程师.md`）
- ✅ 中英混排 OK
- ❌ 不用全角冒号 `：`（用半角 `:` 或空格或 `-`）
- ❌ 不用 `/` `_` 替代斜杠的写法（如 `allow _ ask _ deny` 应改为 `allow-ask-deny`）
- ❌ 不超 50 字符（除非课程编号前缀）
- ❌ 不用 `? * < > | "` 等特殊字符
- ❌ 不用纯数字前缀（`0-1 前言` 改为 `0-1-课程前言`）

---

## §7. 反向链硬规则 v1（5 视角共识）

**必填**：每篇笔记写完时，**显式声明 ≥ 1 个反向链**（文末"相关阅读"或正文 `[[wikilink]]`）
- 这个反向链必须语义相关，**不许凑数**
- 找不到 → frontmatter 加 `status: orphan` + 说明原因
- 不可：留空 / 写"暂无" / 用不相关的笔记占位

**推荐**：AI agent 自动建议 top 5 候选反向链
- 人工从 top 5 选 1-3 个（≥1 必填，>3 警告链接膨胀）
- 同主题 ≥ 3 篇时建 MOC，**被 MOC 链入的笔记破孤**

**质量门槛**（年度 review）：
- 每年 review 所有反向链是否仍语义相关
- 失效的反向链删除或更新
- **"MOC 入口"也算连接**（被 MOC 链入 = 破孤）

**判定孤岛标准**：
- 笔记无任何 `[[wikilink]]` 被链入，**且**不在任何 MOC 中 → 孤岛
- 孤岛 > 30 天未修复 → Archive 候选

---

## §8. 收录流程 SOP（7 步）

```
1. 收素材（URL / 截图 / 复制粘贴）
   ↓
2. 抓内容（webfetch / WebBridge / 复制）
   ↓ 清理 UI 噪声，保留核心结构
3. 选位置：Inbox / Areas / Resources 哪一处？
   ↓
4. 写 frontmatter：按 §3 必填模板
   ↓
5. 打 tag：从 §4 字典选（agent 自动建议 + 人工确认）
   ↓
6. 找反向链：agent 自动 top 5 候选 → 人工选 1-3 个
   ↓
7. 更新 MOC：如有相关 MOC，把新笔记加入索引
```

**注意**：
- 单文件 vs 多文件：短文（< 2000 字）单文件；长文（> 5000 字）考虑拆分
- 课程按章节自然拆分（如 `1-8` / `1-9` / `2-19` 等编号）

---

## §9. 维护原则

**Inbox 处理**：
- 每周清空 Inbox 一次
- 超过 10 个文件触发"集中归档日"
- 永远不允许 Inbox 累计超过 10 个

**Archive 触发**：
- 主题不再关注
- 内容 > 1 年未更新且无新反向链
- 孤岛 > 30 天未修复

**季度审计**（每季度跑一次）：
- tag 一致性扫描
- 死链扫描
- 孤岛扫描

**AGENTS.md 更新原则**：
- 本文档 ≤ 3 页
- 超出部分拆 sub-doc（如 `AGENTS - Tag 字典.md`）
- 重大变更需 vault 主人拍板

---

## §10. 反模式清单（绝对禁止）

- ❌ 同一内容放 3 个位置（如 HITL 三处重复）
- ❌ 不加 frontmatter（除 README、测试文件）
- ❌ 死链 wikilink（`[[X]]` 但 X 不存在）
- ❌ 空目录（> 30 天）
- ❌ 凑数反向链（质量低的相关性）
- ❌ 文件名带全角冒号 / 特殊字符
- ❌ 风格不统一的 tag
- ❌ "暂无相关"作为反向链占位
- ❌ 注释"以后补"作为内容占位

---

## 附录 A：当前 vault 主题清单（v1 快照）

| 主题 | 笔记数 | 位置 |
|---|---|---|
| AI Agent 核心理论（Sitor AI 课程）| ~30 | `01-Areas/AI Agent Development/` |
| AI Coding 实战（Loock AI 课程）| 148 | `02-Resources/AI and Agents/Loock AI 全栈应用开发/` |
| B 站 AI 视频转录 | 19 | `02-Resources/AI and Agents/B站视频知识库/` |
| AI 公众号文章 | 12 | `02-Resources/AI and Agents/Agent Design & Patterns/` |
| AI 播客转录 | 1 | `02-Resources/AI and Agents/播客转录/` |
| AI 时代职业 / FDE / 哲学 | 13+ | 跨目录 |
| Prompt 库 | 16 | `02-Resources/Prompts/` |

## 附录 B：当前 MOC 清单（v1 快照）

11 个 MOC（详见审计报告）。**建议合并**：
- `MOC - AI Agent 参考资料` + `MOC - B站视频知识库` → `MOC - Agent Theory and Design`（合并 34 篇）
- `MOC - 从 0 实现 Coding Agent` 重建按 12 章节分组

**建议新增**：
- `MOC - Harness Engineering`（横切，3 篇）
- `MOC - AI 时代个人发展与组织`（横切，8 篇）
- `MOC - Prompt 工程`（横切，13 prompts + Skills）

## 附录 C：已知未解决问题（v1 快照）

- [ ] `99-System/Attachments/` 5 个空子目录清理
- [ ] `Human-in-the-Loop/LangGraph Human-in-the-Loop.md` 删除（与 Loock AI 1-8 重复）
- [ ] 死链 `[[Harness Engineering]]` 修复（IBM 笔记里）
- [ ] Anthropic 1772 行汇编本拆分或保留 + MOC 索引
- [ ] README 与实际目录树对齐
- [ ] `0-1 前言.md` 等 12 个怪异文件名清理
- [ ] 现有 226 篇笔记的 frontmatter 字段缺失补全
- [ ] 现有 4 种 tag 风格统一（按 §4 回填）

---

**v1 变更记录**：
- 2026-06-11 v1：基于圆桌研讨会（Tiago Forte / Nick Milo / Sönke Ahrens / Stewart Butterfield / AI Agent 5 视角共识）首次落地
