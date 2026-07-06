---
title: "SUBDOC - ASR 内容分轨与收录决策"
parent: vskill-vault-curate
created: 2026-07-06
updated: 2026-07-06
status: active
version: 1.2
description: "B 站 / 视频 ASR 收录的唯一入口决策树——agent 读到本项目时先读本文件，再按轨加载子 SUBDOC"
---

# ASR 内容分轨与收录决策

> **Agent 入口**：vault 内任何 **B 站 BV / Recastory ASR / 视频转写** 收录任务，**先读本 SUBDOC**，再按决策树加载子文档执行。  
> **铁律**：**1 BV = 1 篇 `{主题}.md`**；禁止 `{主题} - 对谈稿.md` 双文件。

---

## 本次 rollout 核心经验（2026-07-03）

### 1. 形态决定格式，不是等级

| 误区 | 正确做法 |
|------|----------|
| A 级一律压成九段讲义 | **A-dialogue**（访谈/webinar）→ Host-Guest 对谈 canonical，ASR 主源 |
| 有 ASR 就逐段摘要 | 对谈体 **禁止** 按 ASR 时间顺序摘要；按 **论点划章** 写对话 |
| S 级才值得高密度 | A-dialogue 密度目标 **对齐 S 级**（Founder Park / 极客公园专栏体感） |
| 九段讲义 = 通用模板 | 九段 **仅** 用于 A-lecture（单人解读 / 教程 walkthrough） |

**一句话**：没有专栏 ≠ 低密度；没有专栏 + 是对谈 → **ASR → Host-Guest**，不是九段压缩。

### 2. 主源优先级（写正文时）

```
S 级：  column_article.md  > video_description（时间戳→附录）> ASR（仅核数字）
A-dialogue： article.md（ASR）+ video_description（划章/Guest 线索）> 外源金句搜索
A-lecture： article.md + video_description > Pass1 大纲 → 九段讲义
```

### 3. 划章规则（不固定章数）

**目标 3–6 章**，按优先级取锚点：

1. `video_description` / 专栏里的 `[MM:SS]` 导读条目
2. 原视频 YouTube chapter（若有 `source_original`）
3. ASR **话题转折**（Guest 长段开始、赞助结束、demo 开始、Host 换题）

**禁止**：按 ASR 每 10 分钟机械切章；禁止固定「必须 4 章」。

### 4. ASR 说话人识别（无 Speaker 标签时必做）

B 站转载 ASR 通常无 Host/Guest 标签，Guest 名常被听错。

| 步骤 | 动作 | 产出 |
|------|------|------|
| Step 1 | ASR 信号扫描（问句密度 / demo / 赞助 / 身份句） | Host vs Guest 倾向 |
| Step 2 | 拿 ≥2 句 distinctive 英文金句搜 YouTube/播客原页 | 锁定真名 + 节目名 |
| Step 3 | 写入 frontmatter + `speaker_confidence` | high / medium / 待核实 |
| Step 4 | 用 description 时间戳 + 话题转折划章 | 3–6 章地图 |

详见 [Host-Guest 对谈稿 SUBDOC](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md) §ASR 说话人识别。

### 5. 单篇 canonical 结构

**S 级 & A-dialogue** 共用骨架：

```text
frontmatter（material_tier / curate_method / dialogue_version / ingest_dir）
开场（Host/Guest/形态/时长）
术语速查表（| 中文 | 英文 | 白话 |）
01–0N 章 ×（对话 + 金句 + 本章概念 + 小结）
总结（| 维度 | 要点 |）
## 附录（时间戳 / ingest 路径 / ASR 路径 / 相关阅读）
```

**A-lecture** 用九段讲义（见 [B站视频转写收录 SUBDOC](./SUBDOC%20-%20B站视频转写收录.md)）。

### 6. 质量门与脚本（收录完成前必跑）

```bash
python 99-System/scripts/bilibili-v3-gap-check.py   # 须全绿
```

| 检查项 | S | A-dialogue | A-lecture |
|--------|---|------------|-----------|
| `dialogue_version: v3.2` | ✓ | ✓ | — |
| `curate_method` 含 canonical-dialogue | ✓（无 -asr） | ✓（v3.2-asr） | 讲义 v3 |
| 概念表三列中文非空 | ✓ | ✓ | ✓ |
| ≥45 min → spot_check | ✓ | ✓ | 视 factual 密度 |
| 反向链 ≥1 | ✓ | ✓ | ✓ |
| 无 `- 对谈稿.md` 孤儿 | ✓ | ✓ | ✓ |

### 7. 反模式清单（绝对禁止）

- ❌ 对谈内容压成九段摘要（丢失 Q&A 密度）
- ❌ 产双文件 `{主题}.md` + `{主题} - 对谈稿.md`
- ❌ 凭 UP 名当 Host 名（UP 常是转载层）
- ❌ ASR 顺序逐段复述
- ❌ 概念表英文列空着（B 档技术词必填）
- ❌ gap-check 未绿就 commit
- ❌ 小结写「带走」、行动启示写论断（分工反了）

---

## 无专栏 ASR 收录 SOP

> **适用**：`column_article.md` 不存在 / <3k / 无「主持人/嘉宾」标记——即 reconcile 定 **A 级** 的全部情况。  
> **口诀**：读者应感到在「对话/被引导」→ **A-dialogue**；在「跟操作/跟讲解」→ **A-lecture**。

### Step 0：ingest 最小集

Recastory `{ingest_dir}/` 收录前须具备：

| 文件 | 必填 | 用途 |
|------|------|------|
| `metadata.json` | ✓ | BV / duration / enrichment |
| `video_description.md` | ✓ | **划章主锚**（`[MM:SS]` 导读）、Guest 线索 |
| `article.md` | ✓ | ASR v2 后处理全文（正文主源或讲义主源） |
| `uploader_comment.md` | 可选 | cv 链；有则后续可 enrich 升 S |
| `column_article.md` | **无** | 本 SOP 前提 |

**简介抓取**：按 [B站视频转写收录](./SUBDOC%20-%20B站视频转写收录.md) Step 0（kimi-webbridge 读 `.desc-info-text`，降级 B 站 API `data.desc`）。

**无 description 时间戳时**：Pass 1 全靠 ASR 话题转折划章（见下）。

### Step 1：形态判定

| 信号 | 倾向轨 | 处理方式 |
|------|--------|----------|
| ASR 问句 ↔ 长答交替、播客形态 | **A-dialogue** | 真 Host-Guest |
| ASR 有 **Speaker1/2** 且角色稳定 | **A-dialogue** | 映射 `host_name` / `guest_name`（见 Speaker 双路径 A） |
| Build Hour / webinar 双讲者 | **A-dialogue** | description + Speaker 或 heuristic |
| **单人主题演讲、现场少互动** | **A-dialogue**（边缘） | **合成 Moderator 过渡问**（样板 [[Databricks-企业级Agent生产实践]]） |
| 单人深度分享、隐含问答结构（播客主持 + 嘉宾长段） | **A-dialogue** | ASR 演讲结构划章；Host 可为原节目主持（例 [[Manus创始人-深度干货-上下文工程的最佳实践]]） |
| 屏幕录制 + 逐步操作、无 Q&A | **A-lecture** | 九段讲义 |
| 单人解读 / 官方教程 walkthrough | **A-lecture** | Pass1 大纲 → 九段 |

**不确定时**：先读 ASR 前 10 分钟——问句密度高 → dialogue；连续 monologue + demo narrating → 仍可能是 dialogue（主题演讲）或 lecture（教程），看有无逐步「跟着做」。

**禁止**：因无 column 就默认九段摘要。

### Step 2：Pass 1（不进 vault）

对 **A-dialogue** 与 **A-lecture** 均建议先写 Pass 1（distill/ 或 agent 内联草稿）：

```markdown
## Pass 1 — {BV} / {主题}

### 三问
1. …
2. …
3. …

### 故事线（5–8 步，非 ASR 时间顺序）
1. …

### Host / Guest（A-dialogue 必填；A-lecture 填讲者即可）
- Host: …（推断依据：…）
- Guest: …（推断依据：…）
- speaker_confidence: high | medium | 待核实

### 章地图（3–6 章）
| 章 | 标题 | 锚点（MM:SS 或 ASR 话题） | 必留数字 / demo |
|----|------|---------------------------|-----------------|

### 待核 factual
- …
```

**A-lecture** 额外产出：Pass1 读者大纲（3 问 + 论点地图）→ 转 [九段讲义模板](./SUBDOC%20-%20B站视频转写收录.md)。

### Step 3：Speaker 双路径（A-dialogue）

| 路径 | 条件 | 动作 |
|------|------|------|
| **A · 有标签** | ASR 含 `Speaker 1` / `Speaker2` 或 FunASR 分段 | 读前 5–10 段定谁常问、谁常答 → 写 frontmatter；例 [[OpenAI员工-上下文工程和Agent记忆]] |
| **B · 无标签** | 典型 B 站转载 ASR | [Host-Guest §ASR 说话人识别](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md)：heuristic 表 → 外源金句搜索 → `speaker_confidence` |

**禁止**凭 UP 名（如 Easonlee）当 Host——UP 是转载层。

### Step 4：Pass 2 — A-dialogue 落盘

`vskill-vault-write mode=dialogue` + [Host-Guest SUBDOC](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md)

**ASR → 对谈体三条规则**：

1. **不按时间轴**：按 Pass 1 章地图重组；禁止 `### [mm:ss]` 逐段摘要。
2. **长 monologue 拆 Q&A**：每 2–4 段 Guest 内容前插 Host 追问——从 ASR 隐含问题提炼，**不杜撰事实**。
3. **主题演讲（边缘）**：Host 用 `Moderator（现场）` + 过渡问（「你刚才提到 X，能展开吗？」）；frontmatter 写 `speaker_inference: "asr_heuristic + video_description（主题演讲，Host 为过渡提问）"`。

**IRON LAW**：Guest 正文禁止「他表示 / 她认为」；数字与原话金句保留。

**写法示例（ASR monologue → 对谈）**：

ASR 原文（逐段摘要体 · **禁止**）：
> Sandy 介绍了五支柱框架，第一根是 evaluation，因为客户常在 demo 漂亮、上线翻车时才发现没有 eval……

Pass 2 转化（Host 过渡问 · **要这样写**）：
> **Moderator：** 五支柱里为什么 eval 必须打头？  
> **Sandy：** 因为我们现场见过太多次——demo 很漂亮，一上生产就翻车。没有 living golden dataset，后面 observability、data 都无从谈起……

完整边缘案例：[[Databricks-企业级Agent生产实践]]。

**12 篇 A-dialogue 划章参考**（BV / 章数 / 依据）：[`bilibili-a-tier-v3-rewrite-2026-07-03.md`](../../../audit/bilibili-a-tier-v3-rewrite-2026-07-03.md) §A-dialogue。

**frontmatter 最小集（A-dialogue）**：

```yaml
material_tier: A
curate_method: "vskill-vault-write canonical-dialogue v3.2-asr"
dialogue_version: v3.2
genre: "Host-Guest canonical (ASR primary)"
ingest_dir: "Recastory/workspace/bilibili-retranscribe/{BV}/ingest"
transcript_source: "Recastory/.../article.md"
host_name: "…"
guest_name: "…"
speaker_inference: "asr_v2 Speaker1=… / asr_heuristic + video_description"
speaker_confidence: high
```

**落盘**：`B站视频知识库/{子目录}/{主题}.md` — 3–6 章对谈 + 术语表 + 总结 + `## 附录`（时间戳 / ingest / ASR 路径 / 相关阅读）。

### Step 5：Pass 2 — A-lecture 落盘

按 [九段讲义](./SUBDOC%20-%20B站视频转写收录.md) 写 `{主题}.md`；`curate_method: vskill-vault-curate v3-ingest（讲义 v3）`。

可选：`bilibili-vault-v3-batch.py --a-tier-only` 机械门（**跳过** A-dialogue / S）。

### Step 6：质量门

```bash
python 99-System/scripts/bilibili-v3-gap-check.py   # 须全绿
```

≥45 min 且 factual 密度高 → [Spot check](./SUBDOC%20-%20Spot%20check（长视频%20factual）.md) + frontmatter `spot_check: YYYY-MM-DD`。

### 无 column 不阻塞；cv 回补可升 S

17 条 partial 无 UP cv 链 → 手补 `column_url` → enrich → 可升 S 覆盖 ASR 版（非 vault 阻塞）：

```bash
python 99-System/scripts/bilibili-partial-enrich-run.py --list
```

---

## 决策树（agent 逐步执行）

```
[输入] Recastory ingest 完成 或 用户给 BV + ASR 路径
                    │
                    ▼
        ┌───────────────────────┐
        │ Phase 0: 对账定级      │
        │ bilibili-ingest-       │
        │ reconcile.py           │
        └───────────┬───────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   column ≥3k              无 column
   + 主持人/嘉宾                  │
        │                       ▼
        │              ┌────────────────┐
        │              │ 形态判定        │
        │              │ ≥2 说话人/Q&A？ │
        │              └───┬────────┬───┘
        │                  │        │
        │                 是       否
        │                  │        │
        ▼                  ▼        ▼
    ┌───────┐        ┌─────────┐ ┌─────────┐
    │ S 级   │        │A-dialogue│ │A-lecture│
    │专栏主源│        │ ASR 主源 │ │九段讲义 │
    └───┬───┘        └────┬────┘ └────┬────┘
        │                 │           │
        └────────┬────────┘           │
                 ▼                    │
    vskill-vault-write                │
    mode=dialogue                     │
    Host-Guest v3.2                   │
    curate_method:                    │
      canonical-dialogue v3.2         │
      或 v3.2-asr                     │
                 │                    │
                 │                    ▼
                 │         SUBDOC 九段 + v3-batch
                 │         curate_method: 讲义 v3
                 ▼                    ▼
            {主题}.md（单篇 canonical）
                 │
                 ▼
        gap-check 全绿 → MOC → 反向链
```

---

## 三轨对照（frontmatter 速查）

| 字段 | S | A-dialogue | A-lecture |
|------|---|------------|-----------|
| `material_tier` | S | A | A |
| `curate_method` | `canonical-dialogue v3.2` | `canonical-dialogue v3.2-asr` | `v3-ingest（讲义 v3）` |
| `dialogue_version` | v3.2 | v3.2 | — |
| `genre` | Host-Guest canonical | Host-Guest canonical (ASR primary) | — |
| `column_url` | 有 | 通常无 | 无 |
| `speaker_inference` | column 为主 | asr_heuristic + description | 可选 |
| 正文形态 | 对谈 3–6 章 + 附录 | 同左 | 九段 |

**样板笔记**：

- S：[[Codex负责人-现场演示Codex]]
- A-dialogue：[[OpenAI员工-上下文工程和Agent记忆]]、[[Loop-Agent Loop到底是什么]]
- A-lecture：[[Karpathy爆火项目-AutoResearch解读与启发]]

---

## 新增 BV 标准口令（Phase 5）

```bash
# 1. Recastory ingest（Recastory 仓）
python -m tools.ingest.bilibili_backfill --bv BVxxxx --force

# 2. 对账定级
python 99-System/scripts/bilibili-ingest-reconcile.py

# 3. 按决策树分轨落盘（人工/agent 写正文）
#    S → write mode=dialogue · column 主源
#    A-dialogue → write mode=dialogue · ASR 主源
#    A-lecture → 九段讲义 v3

# 4. 质量门
python 99-System/scripts/bilibili-v3-gap-check.py

# 5. MOC + 反向链
#    更新 MOC - Agent Theory and Design
```

**partial 回补（非阻塞 P2）**：17 条 A 级无 cv 链 → 手补 `column_url` → enrich → 可升 S 覆盖 ASR 版。

```bash
python 99-System/scripts/bilibili-partial-enrich-run.py --list
```

---

## 子文档加载顺序

| 步骤 | 读什么 |
|------|--------|
| 0 | **本 SUBDOC**（决策树 + 经验） |
| 1 | [B站视频 v3 工作流](./SUBDOC%20-%20B站视频%20v3%20工作流.md)（Phase 0–5 细节） |
| 2a 对谈轨 | [Host-Guest 对谈稿](../vskill-vault-write/SUBDOC%20-%20Host-Guest%20对谈稿.md) |
| 2b 讲义轨 | [B站视频转写收录](./SUBDOC%20-%20B站视频转写收录.md) |
| 3 | [ASR 后处理与 manifest](./SUBDOC%20-%20ASR后处理与manifest.md)（Recastory 侧） |
| 4 | [Spot check](./SUBDOC%20-%20Spot%20check（长视频%20factual）.md)（≥45 min） |

---

## 脚本索引

| 脚本 | 何时跑 |
|------|--------|
| `bilibili-ingest-reconcile.py` | 定 S/A、ingest 对账 |
| `bilibili-canonical-merge.py` | 存量双文件合并（新收录勿用） |
| `bilibili-v3-gap-check.py` | **收录完成前必跑** |
| `bilibili-vault-v3-batch.py` | A-lecture 机械门（跳过 S / A-dialogue） |
| `bilibili-concept-cn-fill.py` | 概念表中文列补全 |
| `bilibili-partial-enrich-run.py` | partial 专栏回补队列 |
| `bilibili-spot-check.py` | ≥45 min factual 对读 |

---

## 审计与进度

- Rollout 汇总：`99-System/audit/bilibili-v3-rollout-2026-07-03.md`
- A 级分轨明细：`99-System/audit/bilibili-a-tier-v3-rewrite-2026-07-03.md`
- Recastory manifest：`Recastory/workspace/bilibili/manifest.json`
