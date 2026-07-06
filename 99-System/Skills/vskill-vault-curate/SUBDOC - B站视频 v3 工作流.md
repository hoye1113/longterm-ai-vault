---
title: "SUBDOC - B站视频 v3 工作流"
parent: vskill-vault-curate
created: 2026-07-03
updated: 2026-07-03
status: active
version: 1.1
---

# B站视频 v3 工作流（Recastory ingest → vault）

> **Agent 入口**：[SUBDOC - ASR内容分轨与收录决策](./SUBDOC%20-%20ASR内容分轨与收录决策.md)（决策树 + 经验 + 反模式）  
> **适用**：Recastory `workspace/` 32 条 BV · vault `02-Resources/AI and Agents/B站视频知识库/`  
> **对账表**：`99-System/audit/bilibili-ingest-reconcile-2026-07-03.md`  
> **rollout 进度**：`99-System/audit/bilibili-v3-rollout-2026-07-03.md`

---

## 总览：单篇 canonical（2026-07-03 起）

**原则**：一条 BV → **一篇** `{主题}.md`；质量 > 数量。

```
Recastory ingest（metadata + video_description + 专栏主源? + ASR）
                    │
        bilibili-ingest-reconcile.py 定 material_tier
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   tier = S                 tier = A
   专栏主源 column_article     无专栏，仅 description + ASR
   ≥3k + 对话体                │
        │                       ▼
        ▼                   讲义 v3 九段（单篇）
vskill-vault-write
mode=dialogue → 直接写入 {主题}.md
SUBDOC Host-Guest v3.2 + 文末附录
        │
        ▼
  {主题}.md（canonical）
  正文 = Host-Guest 四章 + 总结
  附录 = 时间戳 / ingest / 相关阅读
```

| 等级 | 条件 | vault 产出 |
|------|------|------------|
| **S** | `column_article.md` ≥3k 字 + 含主持人/嘉宾 | **1 篇** canonical（对谈形态 + 附录） |
| **A** | 无专栏主源，有 `video_description` + ASR | **分轨**（见 Phase 2A） |

**A 级分轨（2026-07-03 起）**

| 形态 | 判定 | vault 产出 |
|------|------|------------|
| **A-dialogue** | 访谈 / 播客 / webinar Q&A（≥2 说话人） | **canonical Host-Guest**（ASR 主源，同 S 结构） |
| **A-lecture** | 单人解读 / 教程 walkthrough | 九段讲义 v3 |

**术语**：「专栏主源」= Recastory `ingest/column_article.md`（B 站 cv/opus 图稿对话体）。旧称 column。

**共用规范**：

- 正文 **中文口语**；AGENTS.md §10 反翻译腔 + 连词 grep
- 术语 **`| 中文 | 英文 | 白话 |`**
- 小结用 **「要点」/ 维度表**，不用「带走」
- frontmatter：`material_tier` / `ingest_dir` / `dialogue_version: v3.2`（S 级）

**迁移（存量 15 对）**：`bilibili-canonical-merge.py` 将对谈稿并入 `{主题}.md`；**删除** `- 对谈稿.md`（合并后立即改 vault 内死链，不保留 stub）。

**样板**：[[Codex负责人-现场演示Codex]]（已合并）

---

## Phase 0：对账

```bash
python 99-System/scripts/bilibili-ingest-reconcile.py
```

| 等级 | 条件 | 数量（2026-07-03） |
|------|------|-------------------|
| **S** | 专栏主源 ≥3k + 对话体 | 15 |
| **A** | 无专栏主源 | 17 |

---

## Phase 1：ingest 补全（Recastory 仓）

`bilibili_enrich.py` / `bilibili_backfill.py` — 17 条 A 级 partial 待 UP 评论链或手补 cv。

vault **不阻塞**；A 级用 ASR + description。

---

## Phase 2A：A 级（分轨）

### 2A-dialogue：访谈 / webinar → ASR 主源 canonical

**主源**：`article.md`（ASR）+ `video_description.md`（导读时间戳、Guest 线索）  
**规范**：[Host-Guest 对谈稿 SUBDOC](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md) · ASR 说话人识别（Step 1–3）

```text
Pass 1: ASR 故事线 + Host/Guest 推断 + 划章（description 时间戳优先）
Pass 2: vskill-vault-write mode=dialogue
4 章 ×（对话 + 金句 + 本章概念 + 小结）
总结：| 维度 | 要点 |
落盘：{主题}.md（单篇 canonical）
附录：时间戳 / ingest / ASR 路径 / 相关阅读
```

```yaml
material_tier: A
curate_method: "vskill-vault-write canonical-dialogue v3.2-asr"
dialogue_version: v3.2
genre: Host-Guest canonical (ASR primary)
speaker_inference: asr_heuristic + video_description
```

**与 S 级差别**：无 `column_source`；信息密度靠 ASR 全量提炼，工作量 ≈ S 的 3–5×。

**试点**：[[Loop-Agent Loop到底是什么]]、[[Manus创始人-深度干货-上下文工程的最佳实践]]

### 2A-lecture：教程 / solo → 九段讲义

按 [SUBDOC - B站视频转写收录](./SUBDOC%20-%20B站视频转写收录.md) 九段写 `{主题}.md`。

`curate_method: vskill-vault-curate v3-ingest（讲义 v3）`

---

## Phase 2S：S 级 canonical（单篇，不再双文件）

**主源**：`ingest/column_article.md`（专栏主源）  
**辅源**：`video_description.md` 时间戳 → **附录**；ASR 只核对数字

```text
vskill-vault-write mode=dialogue
SUBDOC Host-Guest v3.2
4 章 ×（对话 + 金句 + 本章概念 + 小结）
总结：| 维度 | 要点 | + 封底金句
4500–6000 字
落盘：B站视频知识库/{子目录}/{主题}.md（不是 - 对谈稿.md）
附录：章节时间戳 · ingest · 相关阅读
```

---

## Phase 3：合并存量（S 级 15 篇）

```bash
python 99-System/scripts/bilibili-canonical-merge.py --stem "{主题}" --apply
```

Codex 试点 ✓；其余 14 篇按 P1→P2 队列。

---

## Phase 4：MOC + 反向链

- MOC **只链** `{主题}.md`（不再单独链 `- 对谈稿`）
- 季度：`bilibili-ingest-reconcile` 重跑

---

## 质量门

### S canonical

- [ ] SUBDOC Host-Guest 质量门全过
- [ ] `dialogue_version: v3.2`；`curate_method: canonical-dialogue v3.2`
- [ ] 附录含 ingest / 时间戳 / 相关阅读

### A canonical（ASR 主源）

- [ ] SUBDOC Host-Guest 质量门全过
- [ ] `dialogue_version: v3.2`；`curate_method: canonical-dialogue v3.2-asr`
- [ ] Host/Guest 名经 ASR + description / 外源核对
- [ ] 附录含 ingest / 时间戳 / ASR 路径 / 相关阅读

### A 讲义（lecture 轨）

- [ ] 九段齐全；概念三列；朗读关

---

## 脚本索引

| 脚本 | 用途 |
|------|------|
| `bilibili-ingest-reconcile.py` | ingest × vault 对账、定 S/A |
| `bilibili-canonical-merge.py` | 对谈稿 + 讲义附录 → 单篇 canonical |
| `bilibili-concept-cn-fill.py` | 概念表中文列补全 |
| `bilibili-v3-gap-check.py` | 遗漏审计 |
| `bilibili-vault-v3-batch.py` | A 级讲义机械规则（**跳过** canonical S） |
| `bilibili-partial-enrich-run.py` | 列出 / 批量跑 partial enrich |

---

## Phase 5：新增 BV 收录 SOP

```bash
# 1. Recastory ingest + enrich
python -m tools.ingest.bilibili_backfill --bv BVxxxx --force

# 2. 对账定级
python 99-System/scripts/bilibili-ingest-reconcile.py

# 3. 分轨落盘
#    S（有 column ≥3k + 对话体）→ vskill-vault-write mode=dialogue · 专栏主源
#    A-dialogue（访谈/webinar）→ ASR 主源 canonical-asr
#    A-lecture（教程/solo）→ 九段讲义 v3

# 4. 质量门 + 反向链 + MOC
python 99-System/scripts/bilibili-v3-gap-check.py   # 须全绿

# 5. 更新 MOC - Agent Theory and Design 脚注
```

**禁止**：产 `{主题} - 对谈稿.md` 双文件。

---

## 关联

- [B站视频转写收录 SUBDOC](./SUBDOC%20-%20B站视频转写收录.md)
- [Host-Guest 对谈稿 SUBDOC](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md)
- [vskill-vault-write SKILL](../vskill-vault-write/SKILL.md)
