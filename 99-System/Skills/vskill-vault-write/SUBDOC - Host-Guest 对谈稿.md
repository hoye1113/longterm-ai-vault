---
title: SUBDOC - Host-Guest 对谈稿
description: 从播客/访谈/公众号对谈素材生成 Host 问 + Guest 答 + 章末小结 + 大总结；保留数字与原话金句（中文语境化）
created: 2026-07-03
tags:
  - skills
  - vskill
  - content_creation
source: vault_initiative - vskill-vault-write - dialogue_format
---

# SUBDOC - Host-Guest 对谈稿

> **无专栏 ASR**：先读 [ASR 内容分轨与收录决策](../vskill-vault-curate/SUBDOC%20-%20ASR内容分轨与收录决策.md) §无专栏 ASR 收录 SOP，再读本 SUBDOC。  
> **适用**：Lenny's Podcast 译稿、Founder Park 式公众号、B 站/YouTube 双人访谈、任何 **Host 提问 + Guest 回答** 的可识别素材。
>
> **IRON LAW**：**禁止改成第三人称摘要体。** 读者应感到在听一场被剪辑过的对谈，不是在读新闻稿。
>
> **参照成品**（vault 内）：[[Codex 负责人-所有人都是 builder 是个很糟糕的主意 - Founder Park]]（Founder Park 原文形态；vault 讲义版可另存或作附录）

---

## 何时走本 SUBDOC

| 走本 SUBDOC | 不走（用 SKILL 主流程「5 步切刀」） |
|-------------|--------------------------------------|
| 素材有明确 **Host / Guest** 或 Q&A 结构 | 用户要基于 vault 笔记写 **原创观点文** |
| 用户说「对谈稿」「对话体」「Founder Park 那种」 | 无访谈原文，只有主题 |
| `vskill-vault-curate` 收录的是 **访谈译稿/播客转写** 且用户要 **发布形态** | 只要 vault 检索用讲义（见下方「双轨输出」） |
| **B 站 ASR 无说话人标签** 但可推断 Q&A | 单人演讲 / 无交替问答 |

**触发词**：对谈、访谈、Lenny、Host/Guest、对话体、Founder Park、播客转写、一章一问。

---

## ASR 说话人识别（无 metadata 时必做）

B 站转载 ASR **通常无 Speaker 1/2**；Guest 名常被听错（`tabo`→Thibault）。**禁止**凭 vault 旧笔记抄 Host 名——须从 ASR + 外源核对。

### Step 1：ASR 信号扫描（5 分钟）

| 信号 | 倾向 Host | 倾向 Guest |
|------|-----------|------------|
| 问句密度 | 「what do you think」「can you show me」 | 长段第一人称答 |
| 产品/团队 | 「my audience」「my app」「I built」 | 「we released」「our team」「I use Codex to」 |
| 赞助 / 口播 | Soundcore、newsletter、subscribe | 无 |
| 现场 demo | 「fix my app」「rate it like mine」 | 操作 narrating、「let's see what it does」 |
| 身份句 | — | 「he runs ChatGPT and Codex」类（可能是 Host 介绍 Guest 的旁白被 ASR 连成一段） |

### Step 2：金句外源核对

拿 ASR 里 **≥2 句 distinctive 英文**（含数字）搜 YouTube / Spotify / 原播客页。命中则锁定 **Host 真名 + Guest 真名 + 节目名**。

例（A8 / BV12qTu6WETP）：

- ASR：`Google says seventy five percent` + `back to our conversation with tabo`
- 外源：**Silicon Valley Girl** × **Thibault Sottiaux**（OpenAI ChatGPT & Codex 负责人）
- Host 真名：**Marina Mogilko**（非 B 站 UP「Easonlee」——UP 是转载/笔记层，不是 Host）

### Step 3：写进 frontmatter

```yaml
host_name: "Marina Mogilko"
guest_name: "Thibault Sottiaux"
guest_title: "OpenAI ChatGPT & Codex 负责人"
source_original: "https://www.youtube.com/watch?v=DPe_srf0GlI"
source_bilibili: "https://www.bilibili.com/video/BV12qTu6WETP/"
speaker_inference: "asr_heuristic + youtube_quote_match"
speaker_confidence: high   # high | medium | 待核实
```

`speaker_confidence: medium` 时正文 Host/Guest 可用 **Host：** / **Guest：**，文末注「待核实原名」。

### Step 4：划章

优先用 **原视频 chapter**（YouTube/B 站时间戳）；无则用 ASR **话题转折点**（Guest 长段、赞助结束、demo 开始）。

### 主题演讲 → 合成 Moderator（无 column 边缘案例）

ASR 为 Guest 单人长讲、现场几乎无 Host 问句时，仍走 **A-dialogue**（非九段）：

- Host 命名为 `Moderator（{场合}）`（如「AI Engineer 现场」）
- 在 Guest 长段之间插入 **过渡问**（从 ASR 话题转折提炼，不编造事实）
- frontmatter：`speaker_inference: "…（主题演讲，Host 为过渡提问）"`
- 样板：[[Databricks-企业级Agent生产实践]]

---

## 落盘：单篇 canonical（2026-07-03 起）

| 场景 | 路径 | 说明 |
|------|------|------|
| **新收录 S 级** | `B站视频知识库/{子目录}/{主题}.md` | 正文 = 本 SUBDOC 四章对谈；`dialogue_version: v3.2` |
| **A-dialogue（无专栏）** | 同上 | ASR 主源；`curate_method: canonical-dialogue v3.2-asr` |
| **附录** | 同文件 `## 附录` | 章节时间戳、ingest 路径、相关阅读（从旧讲义抽取） |
| **存量迁移** | `bilibili-canonical-merge.py` | 合并后 **删除** `- 对谈稿.md`，批量改指向 canonical 的 wikilink |

**禁止**再产 `{主题}.md` + `{主题} - 对谈稿.md` 双文件。

**样板**：[[Codex负责人-现场演示Codex]]

---

## 双轨输出（legacy · 2026-07-03 前）

> 以下仅适用于迁移前已存在的双文件；新收录勿用。

| 轨道 | 文件名 | 形态 |
|------|--------|------|
| A 对谈稿 | `{主题} - 对谈稿.md` | Host/Guest（已合并进 canonical） |
| B 讲义 | `{主题}.md` | 九段索引（S 级正文已替换为对谈） |

默认（legacy）：用户未说明时产 A；现改为 **只产 canonical 单篇**。

---

## 输入契约

```yaml
host_name: "Lenny"           # 提问者
guest_name: "Andrew Ambrosino"
guest_title: "OpenAI Codex 团队负责人"   # 一句话身份
source_url: "https://..."
source_type: podcast | wechat | video_transcript | paste
raw_transcript: "..."        # 全文或分段时间戳稿
chapter_count: 4             # 默认 4，可 3–6
language: zh                 # 成稿语言；原话英→中需语境化翻译
publish_channel: wechat | blog | vault  # 影响开头尾注
anchor_notes: []             # 可选：vault 已有笔记，用于「相关阅读」
```

---

## 成稿结构（强制）

```
# {标题：Guest 一句狠话或核心矛盾}

> 对谈：{Host} × {Guest}（{身份}）| 来源：{节目/公众号} | {日期}

---

## 开场：为什么现在聊这个
（第三人称，2–4 短段：背景 + 核心问题 + 四章预告）

---

## 01 {章节标题 = 本章结论，不是「第一部分」}

**{Host}：** {1 个主问题，带场景}

**{Guest}：** {第一人称回答，2–6 段；全中文；B 档术语不写括注英文}

> **金句 · {Guest}**
> **中文：** …
> **原文：** …

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| … | … | … |

**本章小结**
- {全中文判断，无裸英文}

（02 / 03 / 04 同结构）

---

## 总结：{一句总判断}

| 维度 | 要点 |
|------|------|
| … | … |

### {块 1：如「对个人的启示」}
### {块 2：如「对团队/产品的启示」}
### 仍待验证（可选）

> **金句 · {Guest}（封底）**
> **中文：** …
> **原文：** …

---

## 相关阅读（进 vault 时必填 ≥1 wikilink）
```

---

## 章节划分 SOP

1. **通读素材**，标 **4–6 个话题转折点**（Guest 长段、Host 换题、章节广告）。
2. **每章只绑 1 个 Host 问题**——从转折点反推「Host 此时最该问什么」。问题要 **具体**（含「你们团队里是不是也…」），禁止「你怎么看 AI 的未来」。
3. **Guest 答**：从原文 **抽连续段落**，删口头赘词（嗯、那个），**不删**数字、专名、转折（「我不同意…」）。
4. **原话金句**：Guest 标志性句子 → `> **` 引用块 **``；英译中须 **像中文口语**，不是机翻。
5. **本章小结**：只写 **本章新增** 的判断；禁止复述 Guest 刚说过的话。
6. **大总结**：跨章拼 **mental model**（例：实现廉价 → taste → 策展 → 删代码）；禁止四章小结复制粘贴。

---

## Host / Guest 写法规则

### Host

- 每章 **1 主问 + 最多 1 追问**（追问写在同一段，用「那…」「所以你的意思是…」）。
- Host 不发表长篇观点；不替 Guest 总结（总结留给「本章小结」）。

### Guest

- **第一人称**（「我们团队」「我发现」）。
- **保留数字**（90 个原型、500 万 WAU、晚 3 月会死）——无出处则标 `[待核实]`，不编。
- **保留冲突句**（「这是个很糟糕的主意」「我完全不同意」）比平铺叙述更有力。
- 一段超过 **120 字** → 按语义拆成两段，中间不必再标 Guest。

### 翻译与语境化（英→中）— v3.1 中文读者优先

**默认**：正文 **全中文叙述**；英文仅出现在 **专名 / 金句原文 / 概念表**。

#### 术语三档与「译解层」分工

| 档 | 对话正文 | 术语速查 / 本章概念 |
|----|----------|---------------------|
| **A 专名** | 保留英文（Codex、GPT-5） | 英文列照写；白话写产品/专名含义 |
| **B 技术词** | **只用中文**（智能体、定时任务、无感智能） | **必须写英文原文** + 白话解读 |
| **C 金句** | 中文口语句 | 双语块另列 **原文** |

**原则**：英文是源词汇；**术语速查**（开场）与 **本章概念**（每章）是对话正文的 **译解层**——读者在这里查「中文说法 ↔ 英文原文 ↔ 什么意思」。正文不再括注 `(agent)`，避免重复。

**禁止**：句内中英混排（❌「Agent 长 horizon 已可 today 部署」→ ✅ 正文「智能体跑长程任务很稳」；英文见概念表 `long-horizon task`）。

#### 金句双语块（每章 ≥1，大总结 ≥1）

```markdown
> **金句 · Thibault**
> **中文：** 变的是技术成熟度，不是人要先换一套工作方式。
> **原文：** It is more that the technology has matured than that people need to change.
```

#### 术语速查 + 本章概念（三列表，强制）

开场与每章概念表 **统一三列**：`| 中文 | 英文 | 白话 |`

```markdown
**术语速查（后文对话用中文；英文原文在此统一对照解读）**

| 中文 | 英文 | 白话 |
|------|------|------|
| 智能体 | agent | 能多步执行、调工具的助手 |
| 无感智能 | ambient intelligence | 日常对话中恰当时机获助，不靠提示词技巧 |

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 长程任务 | long-horizon task | 步骤多、跑得久仍稳定的任务 |
```

- **中文**：成稿对话里用的说法（与正文一致）
- **英文**：素材原词 / 行业通用叫法；同义可 `/`（如 `elder review / dual-agent review`）
- **白话**：一句人话解读，可稍长；本章新出现的 B 档词 **必须进表**
- 开场术语速查：全文级 **6–10 行**；每章概念：**3–6 行**（含本章新词，可与开场重复以方便跳读）

#### 每章固定四层（v3.2）

1. **Host 问 → Guest 答**（Guest 段 ≥800 字/章，30min 访谈基准；B 档词只用中文）
2. **金句双语块**（≥1）
3. **本章概念**（三列表 3–6 行，**英文列必填**）
4. **本章小结**（全中文 bullet）

#### 篇幅门（S 级 + column 主源）

- 全文 **4500–6000 汉字**（31min 访谈）；45min+ 可 6000–8000
- 每章 Guest 答 **≥800 字**；保留数字、demo 步骤、专栏对话细节
- **素材优先级**：`column_article` 对话 **扩写**，ASR 仅 spot-check 数字

#### Agent 友好（可选 frontmatter）

```yaml
concepts:
  - id: elder_review
    zh: 长老审查
    en: elder review
    one_line: 执行智能体 + 审查智能体，降低自主运行风险
```

或在文末 `## 概念索引（agent）` 汇总全文概念表。

#### 口语化与反翻译腔（v3.2）

**目标**：读起来像中文播客转写，不像英译摘要。信息密度、概念表、金句双语块 **保留**；改的是 **Guest/Host 对话句**。

**流程**（column 主源 → 对谈稿时必做）：

1. **朗读关**：每段 Guest 答默念出声；卡壳处 **整段重写**，不抠词（AGENTS.md §10 朗读关）
2. **连词瘦身**：删掉能删的因果/转折包装，直接说事

| 翻译连接词 / AI 腔（删或换） | 口语换法 |
|---|---|
| 此外 / 另外 / 与此同时 | 删掉，下句直接接 |
| 因此 / 所以 / 由此可见 | Often 删；要强调时用「这就…」「于是…」 |
| 然而 / 但是 / 不过 | 留一个即可，别段段转折 |
| 归根结底 / 本质上 / 关键在于 | 删，或换「要紧的是」「说白了」 |
| 有意思的是 / 值得注意的是 | 删，或换「你看」「我愣了一下」 |
| 进行（讨论/研究/探索） | 聊 / 做 / 试 |
| 拥有…的能力 | 能… |
| 提供支持 / 提供工具 | 撑你 / 给你用 |
| 不仅…而且… | 拆成两句，或只留狠的那半句 |
| 在这个意义上 | 这么说 |
| 被动堆叠（「被…所…」） | 改主动：「你担着」「它干」 |

3. **句长**：Guest 口语 **15–35 字/句** 为主；超过 45 字必拆。少用分号串英文式并列，改句号或「——」只留一处。
4. **标签体禁止**（像写文档不像说话）：

❌ `常见陷阱：` `复杂工作流例：` `个人路径补充：`

✅ 直接开口：`很多人都栽在这：` → 更好：`很多人都栽在这——`

5. **中英混排**：正文零裸英文词（ready / dump / agent 混句）；**A 专名、概念表英文列、金句原文** 除外。
6. **Host 问**：短、带场景（「能现场秀一个吗？」），少用公文问法（「应如何…」「有哪些必备…」可改为「该怎么收拾？」）。

**发布前 grep**（正文对话段，概念表/金句原文除外）：

```
此外|另外|因此|然而|归根结底|本质上|关键在于|值得注意的是|有意思的是|进行.*讨论|拥有.*能力|不仅.*而且
```

命中 → 该段重写。

---

## 质量门（发布前必过）

### 结构

- [ ] **3–6 章**（Pass 1 章地图定数，全文一致；禁止机械固定 4 章）
- [ ] 每章：**Host 问 → Guest 答 → 本章小结** 三段齐全
- [ ] 有 **开场** + **大总结**（`维度 | 要点` 表 + 封底金句双语块）
- [ ] 全文 **无**「本文将介绍」「综上所述」式摘要体段落（除「本章小结」「总结」标题下）

### 对话体

- [ ] 正文章节 Guest 回答 **≥ 60% 为第一人称叙述**（非「他表示」）
- [ ] 每章至少 **1 个** 数字 / 专名 / 反直觉句
- [ ] 每章 **金句双语块 ≥1**；大总结 **封底金句双语块 ≥1**
- [ ] 开场 **术语速查** + 每章 **本章概念** 均为 **中文 | 英文 | 白话** 三列；B 档技术词 **英文列非空**
- [ ] 对话正文 B 档词 **只写中文**（英文进表，不在句内括注）
- [ ] 对话段过 **v3.2 连词 grep**；朗读关无卡壳
- [ ] 正文 **无句内裸英文词**（专名 A 档、金句 C 档除外）
- [ ] S 级 column 源：全文 **4500–6000 字**，每章 Guest **≥800 字**

### vault 协议（进库时）

- [ ] frontmatter §3 五字段
- [ ] tags 来自 §4；访谈加 `article` + 来源 tag（`wechat` / `podcast_rss` / `youtube` 等）
- [ ] 反向链 ≥ 1（§7）
- [ ] 相关 MOC 更新（§8 SOP 步骤 7）

### 反 AI 痕迹（§10）

- [ ] 无「标志着」「值得注意的是」「某种程度上」
- [ ] 朗读关：默念每段 Guest 答，卡壳处整段重写

---

## 工作流（与 curate / write 衔接）

```
[素材]
  URL / 转写 / 粘贴
       ↓
vskill-vault-curate  Step 2 抓内容（kimi-webbridge 优先）
       ↓
判定：是否有 Host/Guest 或 Q&A？
  否 → 普通收录（讲义 v2 或 article 体）
  是 → 读本 SUBDOC
       ↓
vskill-vault-write  mode=dialogue
  输入：raw_transcript + host/guest 元数据
       ↓
产出 A：对谈稿正文
       ↓
（可选）vskill-vault-relate → 反向链 top 5 → 人工选 1–3
       ↓
（可选）讲义索引 追加文末
       ↓
落盘 02-Resources/... + 更新 MOC
       ↓
report：路径 / 四章标题 / 金句列表 / 待核实数字
```

**Agent 执行口令（可复制）**：

```text
按 SUBDOC Host-Guest 对谈稿执行：
- Host={host} Guest={guest}
- 3–6 章（Pass 1 定），每章 Host 1 问 + Guest 答 + 本章小结
- 保留数字与原话金句（中文语境化），禁止第三人称摘要
- 文末大总结（维度 | 要点 表）+ 封底金句
- 素材：{paste or file path}
```

---

## 章节标题命名

用 **结论做标题**，不用过程词：

| ❌ | ✅ |
|----|-----|
| 关于产品流程的变化 | 实现廉价，taste 变贵 |
| 第二部分 | 角色融合，但 PM 不会消失 |
| 规划讨论 | Codex 晚发三个月会死 |

---

## 示例片段（格式参考）

```markdown
## 02 角色融合，但 PM 不会消失

**Lenny：** 很多公司在喊「角色消亡」——PM、设计师、工程师的边界是不是彻底没了？

**Andrew：** 一些公司很喜欢赶潮流，走极端。消灭角色概念的危险在于，它可能同时消灭掉「这些领域是有可以学习的最佳实践的专业」这一认知。

我听到很多公司说「我们要取消产品角色」，我觉得这是个**很糟糕的主意**，然后说「每个人都是 builder」。结果是产品管理这个已经积累了真正最佳实践、真正踩过坑的学科，被直接抛弃了。

**本章小结**
- 「人人 builder」≠ 可以取消 PM 学科；危险在丢掉 accumulated practice
- 边界可以模糊，但策展、引导、对齐变成最稀缺能力
- Codex 招人硬标准：品味——无限 tokens 世界里不能生产垃圾
```

---

## 关联

- 主 skill：[SKILL.md](./SKILL.md)（`mode: dialogue` 时读本 SUBDOC）
- 收录：[vskill-vault-curate SUBDOC 索引](../vskill-vault-curate/SKILL.md#子文档按内容形态)
- 协议：[AGENTS.md](../../../AGENTS.md) §10 反模式
- 范例：[[Codex负责人-现场演示Codex]]（canonical v3.2 · 专栏主源 + 附录）
