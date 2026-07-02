---
title: "Codex实战：构建全能AI营销团队"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1BLGH6REyX/"
speaker: "Riley Brown（创作者 / 营销，Chorus Skills 作者）"
duration: "49:22"
saved: 2026-07-02
spot_check: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - codex
  - openai
  - skills
  - content_creation
created: 2026-06-09
description: "Riley Brown 用 Codex 超级 App + 7 个 Skills/Plugins 跑通营销全流程：YouTube/Readwise 接地、Excalidraw/Paper 可视化、Remotion 动效、FAL Gen Media 迷你 App、Gmail 品牌合作与 Buffer 自动化。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV1BLGH6REyX/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# Codex 实战：构建全能 AI 营销团队

## 先搞懂这一期

**这是什么节目？**  
创作者 **Riley Brown**（约 150 万粉丝）的 **~50 分钟 Codex 实战教程**。不是官方发布会，是一个人讲自己每天用 Codex 做 **95% 内容与营销工作** 的 7 个 Skills + 插件栈，目标年底冲到 1000 万粉丝。

**这期在回答哪三个问题？**

1. **Codex 当「超级 App」到底能干什么？** 和 Claude Desktop 分栏体验有什么不同？  
2. **Skills 和 Plugins 怎么分工？** `/` 和 `@` 各管什么，怎么叠成可复用工作流？  
3. **Grounding（接地）为什么比裸写 prompt 重要？** 怎么把 AI 绑到你的品味、第二大脑和参考素材上？

**用一条线串起来（没看视频也能复述）：**

Riley 开场：电脑里 **95% 营销任务已在 Codex 里完成**。  
**Codex 定位**：OpenAI 把 chat + cowork + code **合成一个超级 App**——对话中间栏 + 右侧动态预览（表格 / 幻灯片 / 浏览器 / App），带 computer use、browser use，越用越能控电脑。  
**操作语法**：`/` 调 **Skill**（指令文件）；`@` 调 **Plugin**（Skills 捆绑包，如 Vercel、Gmail、Calendar）。  
**Skill 1–2（Grounding）**：`YouTube researcher` 拉 transcript 仿 Theo/Andrej Karpathy 风格写 intro；`Readwise CLI` 读 Twitter 书签第二大脑 → 30 条选题，可叠 YouTube researcher，再 **一键变每天 8 点 automation**。  
**Skill 3–4（可视化）**：Excalidraw diagram skill（可 spawn subagent 并行）；Paper MCP 做 Figma 级动画 explainer + steering 实时改布局。  
**Skill 5（动效）**：Remotion / Hyperframes 插件做片头 overlay、手机 demo 动画，截图 + 注释改 timeline。  
**Skill 6（Gen Media）**：自 vibe code 的 FAL API **迷你 App**——人能用 grid 改图，Agent 也能调同一 API 批量出 thumbnail。  
**Skill 7 + Bonus**：Gmail + Calendar **品牌合作 researcher** 筛 inbox → 优先级表；Buffer publisher 把 memory 里选题灌进排期。  
收尾：Skills 在 chorus.com/skills 一键装到 Codex / Claude Code。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Codex = 写代码的 Agent | **Knowledge work 超级 App**：表格、Deck、浏览器、本地文件同一 harness |
| Skills = Claude Code 专属 | **Codex / Claude Code 通用** Skills 文件；Plugin = 技能包 |
| Prompt 写好就能出好内容 | **Grounding**：YouTube transcript、Readwise 书签才是「你的品味」 |
| Agent 只能替你点按钮 | **迷你 App 双入口**：人改最后一成，Agent 批量 cook |

---

## 分话题讲

### 1. Codex 超级 App：一个窗口干完营销

**说法：**  
Codex 像 Claude Desktop，但 **chat + cowork + code 合一**。选模型后 Agent 能 **增删改本地文件**；左侧会话、中间对话、右侧 **任务相关预览**（App / 网页 / 表格 / PPT）。Computer use + browser use 让 Agent 能 **看见并操作浏览器**（鼠标移动可见）。

**和你何干：**  
营销不再切 5 个工具——**预览栏即交付物**，适合内容创作者把「研究 → 视觉 → 排期」锁在一个 harness 里。

---

### 2. Skills vs Plugins：`/` 与 `@`

**说法：**

| 概念 | 含义 | 唤起方式 |
|------|------|----------|
| **Skill** | 给 Agent 的 **指令文件**（workflow recipe） | `/skill-name` |
| **Plugin** | **Skills + 能力捆绑**（如 Vercel 含多个 deploy skill） | `@plugin-name` |

左上角 **Plugins** 面板安装；Vercel 例：`@vercel` 让 Agent 自选子 skill；`/vercel-sandbox` 可点名具体 skill。

**和你何干：**  
先建 **原子 Skill**，测通后再 `@` 插件或 **Automation** 定时跑——Riley 的 Readwise 早报就是这么来的。

---

### 3. Grounding Skill 1：YouTube researcher

**说法：**  
裸 ChatGPT 写脚本 = OpenAI 的 RLHF 品味，不是你的 niche。**Grounding = 把 Agent 指到高质量参考点**。  
`/youtube-researcher`：拉 Theo、t3.gg 等 **最新视频 transcript**，生成 5 个 hook；也可仿 Andrej Karpathy 口吻解释 skills/plugins。需 **Supadata** 等 API 拉 YouTube/Instagram/TikTok/X transcript。

**例子：**  
并行开两个 chat：一个写 Theo 风 intro，一个查 Cleo Abram shorts 选题——Codex **多会话并行**，蓝点表示完成。

**和你何干：**  
内容团队的第一性原理：**先接地再生成**，比堆 adjective 的 prompt 更稳。

---

### 4. Grounding Skill 2：Readwise / 第二大脑

**说法：**  
Readwise 不只 Kindle 高亮——Riley 在 AI Twitter 看到推文 **bookmark → Readwise**（Chrome 扩展可即时同步 + 备注「下条视频用」）。  
`/readwise-cli`：读近一周收藏 → **30 条短视频选题**，找主题聚类；叠 `/youtube-researcher` 再对照自己的 YouTube 历史。  
迭代 Skill：**输出必须带原帖链接**——对话里说一句「以后都要带 URL」，Skill 文件即更新。  
满意后：**「每天早上 8 点在这个 chat 跑同样流程」** → Automations 里出现 `morning-readwise-shortform-ideas`。

**和你何干：**  
**先手工跑通 → 固化 Skill → 再 Automation**，和 [[WorkOS-创建和使用Skills方法论]] 同构。

---

### 5. 可视化：Excalidraw、Paper、Subagent

**说法：**  
- **Excalidraw diagram skill**：解释 plugins/skills，可叠 YouTube + Readwise 取 Riley 口吻；Skill 文件夹含 scripts/assets/**outputs**；默认少字多图，可改 Skill 加正文。  
- **慢？** 说「YouTube / Readwise 用 **subagent**」——主 Agent spawn 多个 subagent 并行，~11 分钟出 share URL。  
- **Paper MCP**：HTML 级 **动画 explainer**（类 AI版 Figma）；开 steering 截图说「别 overlap、改单列」→ 画布 **live 改**；导出 PNG 做 thumb / landing ideation。

**和你何干：**  
复杂营销资产 = **主 Agent 编排 + subagent 取上下文**，别让一个 loop 串行爬完 YouTube 又读 Readwise。

---

### 6. 动效与 Gen Media 迷你 App

**说法：**  
- **@remotion / @hyperframes**：插件做片头「七大能力」弹字、手机 UI demo；timeline 级 prompt（「8 秒 zoom in」「11 秒 zoom out」）；**截图 + 圈注** 改 composition，render 进 Premiere。  
- **Gen Media + FAL**：自写本地 DB 迷你 App，人类 grid 里 drag 改图（「nighttime + pink tiger」）；Agent 也可 **调同一 FAL API** 批量出 Riley 元素 thumbnail，人做 **最后 10%** 精修。

**和你何干：**  
Riley 强调的机会：**Skill 内嵌 mini app**——Agent cook，人类在 App 里收束；比 one-shot 生成更贴创作者工作流。

---

### 7. 商务栈：Gmail、Calendar、Buffer

**说法：**  
- **Brand deal researcher Skill**：搜 inbox 付费合作 → 去重 → 对照 YouTube 研究是否 fit → **优先级表格**（Hyperagent、Cursor、Canva…）；Gmail 插件 + Calendar 插件建议下周空档，人批准后再发邮件。  
- **Automation**：每日早晨把合作表 **email 给自己**。  
- **Bonus `/buffer-publisher`**：读 Codex memory + 近期研究 → **5 条 Buffer 草稿 idea**。

**和你何干：**  
Skill **栈叠**：Gmail Skill 里再调 YouTube researcher——企业营销 harness 也是 **小 Skill 组合**，不是一个大 prompt。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Super App** | Codex 把对话、文档、表格、浏览器、代码预览合成一体 |
| **Grounding** | 把生成任务绑到 YouTube transcript、书签等外部参考 |
| **Skill** | Agent 可复用的指令文件；`/name` 调用 |
| **Plugin** | 多 Skill + 集成能力包；`@name` 调用 |
| **Automation** | 定时/重复跑已验证 Skill 工作流 |
| **Subagent** | 主 Agent 派生子 Agent 并行取上下文 |
| **Steering（Paper）** | 边看画布边注入修改 prompt |
| **Mini App** | Skill 内人类+Agent 共用的本地工具（如 FAL grid） |
| **Supadata** | 拉各平台 video transcript 的 API |

---

## 值得记住的原话

> **"95% of the tasks that I do on my computer for content and marketing is inside Codex."**  
> 我电脑上内容和营销的事，95% 在 Codex 里干完。

> **"Plugins are bundles of skills. Skills are instruction files for an AI agent."**  
> Plugin 是技能包；Skill 是给 Agent 的指令文件。

> **"Grounding is connecting your AI agent to a useful reference point."**  
> Grounding 就是把 Agent 接到有用的参考点上。

> **"Do a useful thing… then say please turn this into a skill… then automate it every day at X time."**  
> 先做出有用输出 → 固化成 Skill → 再定时自动化。

> **"The agent can also use the app… I control the app and the agent controls the app as well."**  
> Agent 也能用这个 App——人和 Agent 共用同一套 API。

> **"I don't like to rely on AI to do everything… I want to take it the final 10%."**  
> 我不让 AI 包到底——最后 10% 价值在人手里。

---

## 小结

**这期最核心的判断：** Codex 对创作者不是「多一个 chat」，而是 **Skills 层叠的超级 App**；**Grounding（YouTube + 第二大脑）** 决定内容像不像你，**可视化 / 动效 / Gen Media** 决定传播形态，**Gmail + Automation** 决定商务与日程能不能 autonomous 一半。

**读完应带走：**
- `/` = Skill，`@` = Plugin；先手工迭代 Skill，再 Automation。  
- 重任务用 **subagent** 并行；Paper / Remotion 用 **截图 steering** 比纯文字改稿快。  
- **迷你 App + Skill** 是 Riley 认为的市场空白——Agent 批量，人类 grid 精修。

**和 vault 的关系：** Codex 实战线，接 [[Codex负责人-现场演示Codex]]、[[OpenAI官方-Codex新手教程]]、[[WorkOS-创建和使用Skills方法论]]。

---

## 行动启示

1. **先选一条 grounding 源**：YouTube 对标频道或 Readwise 书签，再写内容 Skill。  
2. **Skill 输出格式写死**：原帖链接、Excalidraw 少字多图——用对话改 Skill 文件，别每次重 prompt。  
3. **并行 chat + subagent**：研究、视觉、邮件分轨，避免一个 context 挤爆。  
4. **验证后再 Automation**：Readwise 早报是模板——失败工作流不要 cron。  
5. **Gen 资产留 human grid**：FAL /  thumbnail 流程设计成「Agent 填充、人改最后一屏」。

---

## 相关阅读

- [[Codex负责人-现场演示Codex]] — OpenAI 官方 knowledge work + 并行 Agent 演示  
- [[OpenAI官方-Codex新手教程]] — CLI / AGENTS.md / MCP 系统入门  
- [[WorkOS-创建和使用Skills方法论]] — Skills 创建与组织方法论  
- [[Claude Code实战-结合Obsidian打造第二大脑]] — 另一套「第二大脑 + Agent」路径  
- [[MOC - Agent Theory and Design]] — Agent 理论横切索引  

---

## 来源

- **视频**：[BV1BLGH6REyX](https://www.bilibili.com/video/BV1BLGH6REyX/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Riley Brown（创作者；Chorus Skills）  
- **时长**：~49:22  
- **转写**：Recastory `bilibili-retranscribe/BV1BLGH6REyX/`（FunASR SenseVoice + cam++，**asr v2 后处理** 38 段）  
- **Skills 入口**：chorus.com/skills（视频中提及）  
- **版本**：v2 读者向讲义（2026-07-02）
