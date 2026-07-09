# AGENTS.md - Obsidian Vault 长期主义规范

> **本文档是 vault 的"宪法"**。约束新笔记收录、跨会话维护、AI agent 协作。
> **限长原则**：≤ 3 页；超出部分拆 sub-doc。
> **适用对象**：vault 主人 + 协作 AI agents
> **最后更新**：2026-07-06 | **版本**：v1.3（附录 B/C 滚动维护）

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
- **B 站 v3 视频**（见 §8 ASR 三轨）：`material_tier` / `curate_method` / `dialogue_version` / `ingest_dir` / `transcript_source` / `host_name` / `guest_name` / `speaker_inference`
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
  - name: loop_engineering
    proposed_by: ai_agent
    proposed_at: 2026-06-25
    reason: "Loop Engineering 子主题——2 篇笔记（Loop Engineering 橙皮书 - 花叔；遇事留痕 - Loop Engineering 的基础 - 魔术师卡颂），Loop = Harness 上一层"
  - name: author
    proposed_by: ai_agent
    proposed_at: 2026-07-01
    reason: "作者 / 人物 / persona 标签——用于 Authors/ 目录下的作者笔记（如 [[三元同学]]），便于跨笔记找同一作者的所有作品"

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

### B 站 / Recastory ASR 收录（形态优先）

> **Agent 必读**：[SUBDOC - ASR内容分轨与收录决策.md](./99-System/Skills/vskill-vault-curate/SUBDOC%20-%20ASR内容分轨与收录决策.md)  
> **落盘目录**：`02-Resources/AI and Agents/B站视频知识库/` · **skill**：`vskill-vault-curate` + `vskill-vault-write mode=dialogue`

**铁律**：1 BV = 1 篇 `{主题}.md`；禁止讲义 + 对谈稿双文件。

**三轨决策**（先 `bilibili-ingest-reconcile.py` 定级，再按形态分轨）：

| 轨 | 判定 | 正文形态 | 主源 |
|----|------|----------|------|
| **S** | UP 专栏 ≥3k + 含主持人/嘉宾 | Host-Guest 对谈 + 附录 | `column_article.md` |
| **A-dialogue** | 无专栏 + 访谈/webinar（≥2 说话人） | 同上 | ASR `article.md` + 简介时间戳 |
| **A-lecture** | 无专栏 + 单人教程/解读 | 九段讲义 v3 | ASR → Pass1 大纲 |

**收录完成前**：`python 99-System/scripts/bilibili-v3-gap-check.py` 须全绿；≥45 min 另跑 Spot check。

**禁止**：对谈 ASR 压成九段摘要；凭 UP 名当 Host 名；ASR 时间顺序逐段复述。

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
- ❌ 自标深度（"再深入一层""最深的一层是""更深地说"——下一句内容让读者自己感到深度）
- ❌ 翻译腔（详见下方"反翻译腔自查表"）
- ❌ AI 痕迹词（"标志着""见证了""充满活力""值得注意的是""某种程度上"）
- ❌ 机械连词堆砌（"此外""另外""不仅...而且..."——能省就省）
- ❌ 抽象集合名词通胀（"领域""阶段""过程""方式"——换具体）
- ❌ 一段里同一论点出现两次（改第一次，删第二次）
- ❌ 助手腔（"任何助手都写得出的句子"——改或删）
- ❌ B 站对谈 ASR 压成九段摘要（→ §8 A-dialogue 轨，Host-Guest 对谈 canonical）
- ❌ 1 BV 产 `{主题}.md` + `{主题} - 对谈稿.md` 双文件

### 反翻译腔自查表（每段写完扫一遍，借鉴 ljg-book）

英文母语模型用中文最容易犯的毛病。信号词出现 → 整句重写。

| 翻译腔 | 真实中文 |
|---|---|
| 进行（研究/讨论/对话） | 直接用具体动词 |
| 做出选择 / 做出决定 | 选；决定 |
| 拥有...的能力 | 能... |
| 通过 X 抓到 Y | X 动词直接带宾 |
| 一是...二是...三是... | 散文式排开，不编号 |
| 在这个意义上 | 这么说 |
| 这是必要的 | 必须这样；非这样不可 |
| 让我们一起... | 我们...（省"让"） |
| 提供支持 | 撑你 |
| 在情感上 X | 情感上 X（省"在"） |
| 这片领域 | 这门学问；这套东西 |
| 「是...的」句 | 直接说 |
| 被动句滥用（"被这事困扰"） | "这事缠着" |
| 长定语拆两句 | 拆开 |
| 三层定语「X 的 Y 的 Z」 | 拆开（一个「的」没事，两个起停下来） |
| 动名词化（"做出决定"） | 直接动词 |
| 抽象集合名词 | 换具体 |
| 形容词副词堆砌 | 选一个 |
| 「因为...所以...」 | 直接说后半句 |
| 「温柔的支持」 | 「温柔地撑」 |

### 反风格自查表（写完自检，借鉴 ljg-writes）

| 信号 | 修正 |
|---|---|
| 在解释？ | 换一个看得见的场景 |
| 在罗列？ | 砍到只留最狠的一个 |
| 在全面覆盖？ | 一篇只说一个点 |
| 同一论点出现两次？ | 改第一次，删第二次 |
| 在宣告深度？ | 删掉宣告，让下一句内容自己显出深度 |
| 任何助手都写得出的句子？ | 改或删 |
| 写完没发现自己之前没想到的？ | 回去切，切得不够狠 |

### 朗读关（Frame 级翻译腔兜底）

信号词 grep 抓不到的翻译腔，靠默念出声捕。每段默念一遍。卡的地方 **整段重写**（不是抠字）——汪曾祺、王小波、阿城、李娟那一路的中文白话。

---

## 附录 A：当前 vault 主题清单（快照 · 现行计数见各 MOC）

| 主题 | 笔记数 | 位置 |
|---|---|---|
| AI Agent 核心理论（Sitor AI 课程）| ~30 | `01-Areas/AI Agent Development/` |
| AI Coding 实战（Loock AI 课程）| 148 | `02-Resources/AI and Agents/Loock AI 全栈应用开发/` |
| B 站 AI 视频（v3 canonical） | **122** | `02-Resources/AI and Agents/B站视频知识库/` |
| AI 公众号文章 | **28** | `02-Resources/AI and Agents/Agent Design & Patterns/`（见 [[MOC - Agent Theory and Design]]） |
| AI 播客转录 | 1 | `02-Resources/AI and Agents/播客转录/` |
| AI 时代职业 / FDE / 哲学 | 13+ | 跨目录 |
| Prompt 库 | 16 | `02-Resources/Prompts/` |

## 附录 B：当前 MOC 清单（快照 · 2026-07-06）

| MOC | 状态 |
|-----|------|
| [[MOC - Agent Theory and Design]] | ✅ 已合并原 B 站 + 公众号索引（B 站 122） |
| [[MOC - Harness Engineering]] | ✅ 横切 27 篇 |
| [[MOC - AI 时代个人发展与组织]] | ✅ 横切 |
| [[MOC - Prompt 工程]] | ✅ 横切 |
| [[MOC - Loock AI 全栈课程]] | ✅ 148 篇 |
| [[MOC - AI Agent Development]] | ✅ Areas 课程 |

## 附录 C：已知未解决问题（滚动维护）

- [ ] `99-System/Attachments/` 空子目录清理
- [ ] Anthropic 1772 行汇编本拆分或保留 + MOC 索引
- [ ] 存量笔记 frontmatter / tag 风格统一（季度审计）
- [ ] Recastory 17 条 partial 手补 `column_url` → 可升 S（见 ASR 分轨 SUBDOC）

---

**v1 变更记录**：
- 2026-07-06 v1.3：附录 B/C 对齐现状；章数/版本号与子 SUBDOC 同步（见 Skills INDEX）
- 2026-07-06 v1.2：§3 B 站扩展字段；附录 A 计数对齐 MOC（B 站 32 / 公众号 28）
- 2026-07-06 v1.1：§8 增 B 站 ASR 三轨收录（S / A-dialogue / A-lecture）；链 ASR 分轨 SUBDOC
- 2026-06-11 v1：基于圆桌研讨会（Tiago Forte / Nick Milo / Sönke Ahrens / Stewart Butterfield / AI Agent 5 视角共识）首次落地
