---
title: "SUBDOC - B站视频转写收录"
parent: vskill-vault-curate
created: 2026-07-02
updated: 2026-07-02
status: active
version: 1.0
---

# SUBDOC - B站视频转写收录

> **适用**：Recastory `workspace/knowledge/` 英文 ASR 转写 → vault `02-Resources/AI and Agents/B站视频知识库/`  
> **父 skill**：[[vskill-vault-curate/SKILL.md]]  
> **样板笔记**：`DeepMind团队-当数百万Agent相遇.md`（v2 读者向讲义）

---

## 流水线（两 Pass）

```
Recastory article.md（ASR 英文口语）
        ↓ Pass 1（读者向大纲，写入 distill/knowledge.md 或内联草稿）
        ↓ Pass 2（vault 正文，严格本节模板）
vault 笔记 + MOC 更新 + vskill-vault-relate 反向链
```

**Pass 1 产出**（不进 vault 或仅作中间稿）：

- 这期在回答哪 **3 个问题**
- **5–8 步故事线**（白话，非 ASR 顺序）
- 谁是谁（嘉宾 / 主持 / 节目形态）
- 章节地图（按论点，不按转写顺序）

**Pass 2**：按下方 **正文九段** 写 vault 笔记。

---

## 正文九段（顺序固定）

| # | 章节 | 回答的问题 | 与相邻节的区别 |
|---|------|-----------|---------------|
| 1 | `## 先搞懂这一期` | 读**前**：讲啥、怎么串 | 不是小结；含 3 问 + 故事线 |
| 2 | `## 背景` | 在 vault 大图里占哪块 | 表格：已有认识 vs 这期补上 |
| 3 | `## 分话题讲` | 正文：说法 / 例子 / 和你何干 | 按论点分节，非 ASR 顺序 |
| 4 | `## 关键概念` | 术语表（读完应能解释） | 定义，不是论断 |
| 5 | `## 值得记住的原话` | 嘉宾原话 + 中文 | 引用，不是改写 |
| 6 | `## 小结` | 读**后**：信什么、记住什么 | **论断**；见 §小结写法 |
| 7 | `## 行动启示` | 读**后**：**做**什么 | **动作**；不写重复论断 |
| 8 | `## 相关阅读` | vault 内 ≥1 反向链 | 用 `vskill-vault-relate` 候选 |
| 9 | `## 来源` | URL / 转写路径 / 版本 | 溯源 |

**禁止**：IBM v1 式「一句话总结 + 思维导图」堆在开头替代「先搞懂」；ASR 顺序逐段摘要。

---

## §小结写法

**位置**：`## 值得记住的原话` 之后、`## 行动启示` 之前。

**结构**（三段，可略调但三块都要有）：

```markdown
## 小结

**这期最核心的判断：** …（1 句，嘉宾/节目立场，可带限定语）

**读完应带走：**
- …（论断 / 洞察，不是操作步骤）
- …
- …

**和 vault 的关系：** …（1 句：接哪条主题线，如 harness / eval / multi_agent）
```

**约束**：

- 不重复 `frontmatter.description` 原文
- 不重复「先搞懂」故事线整段复述——小结是**压缩论断**，故事线是**叙事地图**
- 不用「综上所述 / 总而言之 / 一句话总结」
- 「行动启示」写步骤；「小结」写**你信什么**

---

## 多论文单文件（B4 类）

整篇仍走九段；`## 分话题讲` 内每篇论文一节，节末加：

```markdown
#### 本篇小结

…（2–3 句：这篇论文/这场的核心论断）
```

整篇 `## 小结` 收束五讲的**共同主题 + 各讲一句**。

---

## frontmatter（§3 + 扩展）

```yaml
---
title: "笔记标题"
source: "B站视频 - {频道或节目名}"
source_url: "https://www.bilibili.com/video/BV.../"
speaker: "{嘉宾} / {主持}"   # 能识别则填
duration: "MM:SS"            # plan.json 有则填
saved: YYYY-MM-DD
tags:
  - ai_agent                  # 主 tag，按内容选
  - video_transcript
  - bilibili
  - {细分 tag}
created: YYYY-MM-DD
description: "≤100 字，检索用；不是正文小结"
transcript_source: "Recastory/workspace/bilibili-retranscribe/<BV>/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
spot_check: YYYY-MM-DD          # 可选；≥45 min 且 Spot check 通过后填
---
```

---

## PARA 与目录

| 批次 | 典型目录 |
|------|----------|
| A 组（平台 / harness / skills） | `B站视频知识库/Agent架构与平台/` |
| B 组 eval / 论文 | `B站视频知识库/AI评估与研究/` |
| 行业 / 组织 | `B站视频知识库/行业观点与组织/` |

---

## 质量门（收录前自检）

- [ ] 没看视频能否用「先搞懂」故事线复述？
- [ ] 「小结」与「行动启示」是否分工（论断 vs 动作）？
- [ ] 反向链 ≥1，且非凑数（§7）
- [ ] tag 全在 AGENTS.md §4 字典
- [ ] 朗读关：无 §10 反翻译腔信号词
- [ ] **≥45 min**：跑 [Spot check SUBDOC](./SUBDOC%20-%20Spot%20check（长视频%20factual）.md)（`99-System/scripts/bilibili-spot-check.py` + 人工 P0 清零）

---

## 关联

- 转写源：Recastory `skills/distill/SKILL.md` Phase D
- 反向链：`vskill-vault-relate`
- MOC：`MOC - Agent Theory and Design` 等（Step 7）
