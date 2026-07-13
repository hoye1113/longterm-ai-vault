---
title: "SUBDOC - B站图文专栏精华收录"
parent: vskill-vault-curate
created: 2026-07-13
updated: 2026-07-13
status: active
version: 1.0
description: "用户提供单篇 opus/cv 后，以专栏文字为主源提炼高密度 canonical 笔记。"
---

# B站图文专栏精华收录

## 适用边界

只处理用户明确提供的单篇 B 站 opus/cv。不得扫描 UP 主空间、维护增量游标或自动收录。图片一律跳过：不读取、不识别、不下载、不写附件。

Recastory、ASR、transcript 和长视频 Spot Check 已退出默认流程。历史核验见 [LEGACY - B站 ASR 与 Recastory.md](./LEGACY%20-%20B站%20ASR%20与%20Recastory.md)。

## 状态机

```text
PREFLIGHT -> DISCOVER -> MATCH -> ADMISSION -> EXTRACT
          -> CLASSIFY -> TRANSFORM -> RELATE -> VALIDATE/REPORT
```

1. `PREFLIGHT`：读取 AGENTS、Ingest Contract、Density Profile 和本文件。
2. `DISCOVER`：从文字 DOM 和播放器元数据提取标题、作者、发布日期、opus、cv、BV、时长。禁止读取图片。
3. `MATCH`：按 BV、opus、cv、source URL 查重。已有 canonical 时停止，新建或覆盖须用户确认。
4. `ADMISSION`：纯新闻、重复观点、低价值教程、越界主题标 rejected。
5. `EXTRACT`：建立 Pass 1，不落入正式知识目录。
6. `CLASSIFY`：输出 source_tier、material_tier、content_form 和理由。
7. `TRANSFORM`：按知识增量压缩，保持原论述，不补来源之外的事实。
8. `RELATE`：检索 top 5，选 1–3 个真实相关链接或标 orphan；只更新已有 MOC。
9. `VALIDATE/REPORT`：运行专栏验证器，通过后输出机器可读报告。

## Pass 1

```yaml
core_question:
core_claims: []
mechanisms: []
numbers: []
examples: []
constraints_and_counterexamples: []
valuable_questions: []
entities: []
uncertain_facts: []
```

## 分类

- C1：完整正文、章节、BV、人物和时间锚点齐全。
- C2：正文可用，但人物、问答、数字或 BV 映射有缺口。
- lecture：论述、教程或机制推进；末尾有 Q&A 仍是 lecture，使用 `none/none`。
- dialogue：真实追问改变论述方向，使用 `source/transcript`。
- roundtable：三人以上独立观点和回应构成价值，使用 `source/transcript`。
- 新流程不创建 reconstructed dialogue。`unknown：` 改为“现场提问：”或“观众提问：”。

## 提炼规则

保留核心命题、机制、方法框架、关键案例、带语境数字、限制反例和有效问答。删除重复摘要、重点速览重复项、章节预告、寒暄串场、展位导流、关注提示、平台 UI 和无知识增量的例子。

删除一段后若仍能回答“是什么、为什么、怎么用、何时不成立”，默认删除。不按固定比例压缩，不机械套固定章数，不把转述写成直接引语。

## Frontmatter

```yaml
source_type: bilibili_opus
source_url: "https://www.bilibili.com/opus/..."
opus_id: "..."
column_id: "cv..."
video_url: "https://www.bilibili.com/video/BV.../"
bv: "BV..."
uploader: "Easonlee的AI笔记"
source_tier: C1 | C2
primary_source: column
material_tier: S | A | B
content_form: lecture | dialogue | roundtable
dialogue_fidelity: source | none
question_source: transcript | none
factual_status: verified | partial | unverified
factual_reviewed: YYYY-MM-DD
verification_basis:
  - column
```

只有实际读取视频页或官方页，才能把相应来源加入 `verification_basis`。有关键疑点则写 `unresolved_facts` 并使用 partial/unverified。

## 完成门

```powershell
python 99-System/scripts/bilibili-opus-validate.py <note> --vault-root <vault>
```

同一 BV/opus/cv 无重复、有反向链或 orphan、图片未进入正文或附件、来源字段合法、忠实度与正文形态一致，才可报告 complete。

