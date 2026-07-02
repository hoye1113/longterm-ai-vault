---
title: "WorkOS：创建和使用 Skills 方法论"
source: "B站视频 - WorkOS Skills at Scale Workshop"
source_url: "https://www.bilibili.com/video/BV18bjG6fEi7/"
speaker: "Nick & Zack (WorkOS Applied AI / DX Engineers)"
duration: "1:21:03"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - skills
  - harness_engineering
  - context_engineering
created: 2026-07-02
description: "WorkOS 工程师 Nick 与 Zack 在 Skills at Scale 工作坊讲解 Skills 作为 agentic 时代 DRY 单元：按需路由、constraints、脚本注入确定性、progressive disclosure、eval 与团队治理。"
transcript_source: "Recastory/workspace/knowledge/A6-workos-skills/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# WorkOS：创建和使用 Skills 方法论

## 先搞懂这一期

**这是什么节目？**  
WorkOS Applied AI 团队在 **「Skills at Scale」** 上的 **互动工作坊**（约 81 分钟）。主讲 **Nick** 和 **Zack** 都是 Developer Experience 工程师——两人自称 **6–8 个月没手写代码**，日常工作就是跟 agent 协作。现场带着观众一起写一个叫 **repo-roast** 的 Skill。

**这期在回答哪三个问题？**

1. **为什么 CLAUDE.md / agents.md 不够，还要 Skills？** 每开新对话都从 zero 开始，全量 memory 又 bloating context。
2. **一个好 Skill 长什么样？** 怎么写 description 让模型 **自动路由**，怎么用 constraints 和脚本 **注入确定性**？
3. **团队规模化时怎么管？** 60 个工程师各写各的 Skill，Slack 里「我这有个超好用的」——共享、版本、eval 谁来做？

**用一条线串起来（没看视频也能复述）：**

每次跟 Claude 说话，它 **不记得** 上次聊过什么——你得 **重新加载**「这项目用 pnpm」「测试要这样跑」。CLAUDE.md 能缓解，但 **每次 kickoff 全塞进 context**，且模型仍可能 **跳过中间步骤**（「你说了要做，我就是不想做」）。

**Skill = agentic 时代的 DRY 单元**：一小包 **可组合、可移植** 的工作 intelligence——**只有相关时才加载**（靠 description 路由），里面可以写 **constraints**（别做什么）而不是长篇菜谱，还可以用 **`!` 脚本** 把 git log 等 **确定性结果** 插进对话，省 token、少幻觉。

工作坊用 **repo-roast** 演示：30 行 markdown + 几条 constraints + bang 脚本 → 从 generic 建议变成 **贴合你 repo 的 roast**。进阶还有 **progressive disclosure**（需要时才读 `testing.md`）、**confidence gating**（不够自信就先问你）、**eval**（有 Skill 不能比没有更差——Next.js installer 曾 **over-prescriptive 导致 -30%**）。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| [[3-5 Skills - Agent 时代的知识分发系统]] 理论 | **工程方法论 + 工作坊实操**（description、bang、eval） |
| CLAUDE.md / AGENTS.md 项目记忆 | **按需加载 vs 全量加载** 的 context 经济学 |
| Prompt 写步骤 | **Constraints > prescriptive novel**；失败模式是 markdown 写成小说 |
| Skills 只在 Claude Code | 跨 **Claude / Codex / Cursor / Dust / OpenClaw / CI**；非技术岗（recruiting）也在用 |

---

## 分话题讲

### 1. 痛点：每对话从零开始

Agent 对话 **无跨 session 持久记忆**（Claude 不会记得「我们上周说过」）——每个 tab、每个 repo 都要 **重新交代**：
- 这项目 care 什么  
- 工具链（pnpm vs npm）  
- 测试/发布惯例  

**CLAUDE.md / agents.md / memory files** 能部分解决，但：
- **Repo 绑定**：队友要记得 pull 更新  
- **Global 污染**：放 home 目录则 **所有项目** 都加载  
- **仍可能 skip 步骤**——不像确定性脚本可靠  
- **无法优雅 interleave 确定性结果**（「去跑 git log 猜十遍」vs「这就是 log」）

**Skill 的定位：** 把 **不可 miss、不想重复说** 的流程 **encode 成离散单元**——solo 12 agents 或传统 12 人团队都适用。

---

### 2. Skill 是什么：最小可以只有 30 行 Markdown

**无 Skill：** 让 AI review repo → generic 建议，顶多扫到 low-hanging fruit。

**有 Skill（~30 行）：** 写明 routing 惯例、semantic commit、README drift 不可接受 → **hyperspecific** 反馈。

Skill 教 LM **按你期望的方式做 repeatable 的事**——否则同一 prompt 每次输出格式、深度都不一致。

**结构（通常是文件夹，不是单文件）：**

```
skill-name/
  SKILL.md          # frontmatter: name + description
  scripts/          # 可选
  references/       # 可选，progressive disclosure 用
```

**Frontmatter 里最重要的是 `description`**——**不是给人看的**，是给 **LM 做 runtime routing**：「用户现在要 roast repo 吗？该 load 这个 Skill 吗？」

---

### 3. Constraints 胜过长篇 Prescriptive

**反直觉：** 写 **几条 hard constraints** 往往比逐步菜谱更有效。

好例子：
- Never be vague  
- 引用代码必须带 **行号 + git commit ref**  
- 每条 finding 必须有 **script 或 git 数据 backing**

**失败模式：** SKILL.md 写成 **小说**——模型在中间迷失，性能反而差。

**原则：** **Tell it what it shouldn't do**；creative 部分留给模型。Next.js installer 的教训：Claude **本身就会 Next**，Skill **过度规定** 反而 **eval 掉 30%**。

---

### 4. Bang 脚本：确定性注入，别让它猜

Claude Code 里 **`!` + 反引号** 可 **执行 shell 并 interpolate 结果**（类似 JS 模板字符串）：

- 不说「去查 stale todos」→ 写 `!git ...` **直接替换**成 todo 列表  
-  morning report、git status、最新 10 commits——**一次 formalize，反复用**

**价值：**
- **Non-deterministic → deterministic base** 再让 LM 推理  
- **省 token**——不用三轮 tab 里 spin 读 docs  
- Review 时知道 **数据从哪来**

Workshop repo-roast 示例 constraints：  
**Never present a finding without script or git data backing** —— 所以 roast 会跑 git/filesystem 脚本再说话。

---

### 5. Skills vs CLAUDE.md / Rules：mental model

**Number one rule：** CLAUDE.md / agents.md **每次 kickoff 都加载**——塞满 **与当前任务无关** 的东西就是浪费 context。

**Nick 的 CLAUDE.md 极小：**
- 要 terse、别 glob  
- ideation plugin 配置（artifacts 进 Obsidian vault）  
- Repo 特有 **一行**（如 we use pnpm）

**更具体的东西（测试流程、roast 格式、migration 步骤）→ Skills**，**只有需要时才 load**。

**怎么决定拆 Skill？** 工作一周后问 Claude：**analyze my week — what skills should I split out?**

| 放 CLAUDE.md | 放 Skill |
|--------------|----------|
| 每次会话都需要的极简偏好 | 特定任务流程（测试、roast、deploy） |
| 一行工具链事实 | 需 scripts / references 的复杂流程 |
| 全局 terse 风格 | 可组合、可分享、可 eval 的单元 |

---

### 6. Skills 放哪、怎么装

**最常见路径：**
- Repo：`.claude/skills/<skill-name>/SKILL.md`  
- Global：`~/.claude/skills/...` —— 所有 Claude 会话可用  
- **`npx skills`**（Vercel 等）：一键装进各工具目录  

**生态：** Claude、Codex、Cursor、Dust（非技术岗）都 increasingly 支持 Skills 形态。WorkOS 有 **public skills repo**（`npx skills add`）、internal specialist skills、个人 marketplace、monorepo 里 repo-specific skills。

**开发循环：** 写 Skill → invoke → 看输出 → 迭代。Claude 自带 **skill-creator / skill-builder**——critique 结构、甚至跑 eval。

**Description 调试技巧：** 直接问 Claude——**「我什么情况下会 load 这个 Skill？description 够好吗？」**

---

### 7. 团队规模化：Global Skills 治理地狱

现场真实 pain（某司 ~60 工程师）：
- 每人写 Skill，Slack 晒「超好用」  
- EM 说「要共享」→ MR 审查 Skill 变更  
- 有人 fork 成「我的 UX roast 2.0」，description 相似 → **路由冲突**，模型不知道 load 哪个  
- 有人 **直接 block 共享**——「三个月新模型出来 Skill 又过时，谁 maintain？」

**WorkOS 做法（partial）：**
- Public repo + internal buckets + **个人 marketplace**  
- Fork skill **keep locally** 做 slight variant  
- **Plugin versioning**（npm-like）——装特定版本，减少「 ten UX roast skills in monorepo」  
- 按 role **flag**（frontend-only marketplace）—— packaging 问题，方向如此  

**Eval ownership：** public shipped skills 有 **evals framework**；internal  informal 些。新模型出来用 skill-builder **review truncation / 是否 over-prescriptive**。

---

### 8. Progressive Disclosure：别一次塞满 context

主 SKILL.md 只做 **路由 + 核心 constraints**；细节放引用文件，**只有需要时才读**：

- 「要做 testing → load `testing.md`」  
- 「要做 scoring → load `scoring-rubric.md`」  
- Migration skill：**reference map** → 只有 Next.js 才 load `workos-off-next.md`  

WorkOS **skill-writer** 本身就是 reference map 范例。

**Audience-aware roast（workshop 创意）：**  
Skill 里写——查 commit 数：10k commits → roast 狠；新人 4 commits → gentle，别吓跑。

---

### 9. Confidence Scoring：不够自信就先问

Zack 开源 **ideation plugin** 模式：
- 多维度 rubric（problem clarity、scope、criteria…）  
- 总分低于阈值 → **强制 ask user questions**（常给 multiple choice）  
- 到 ~95/100 → 输出 **contract**（scope、success criteria、out of scope）→ 再分 phase 执行  

**Repo-roast 可加：** 对 conventional commits 惯例有多 confident？低则 progressive load rubric 或追问。

**要点：** 问「你有多 confident」模型常瞎报；要 **show your work** + rubric 才靠谱。

---

### 10. Eval：Skill 不能帮倒忙

Public skills 用 **evals framework**：
- 同一任务：**without skill** vs **with skill** 多轮跑  
- Grade：with skill 应 **≥80–90%** 且 **优于** without  
- 有时 without 已经 98%，skill 只 +2%——仍 worth tracking  

**Next.js installer 教训：** eval 发现 over-prescriptive **使表现降 ~30%**——Claude 原生就强，Skill 画蛇添足。

**Apple Watch 类比：** eval 数字不 perfect accurate，但给 **improving vs worsening 的向量**。

**Skill 被 ignore / 冲突：**
- Skills 太多 → description 冲突  
- 解法：public skills 保持 **generic triggers**；显式 **`/skill-name`** 或「use superpowers brainstorm skill」  
- Bang script **强制** 走 deterministic 步骤  

---

### 11. Subagent vs Skill

**Skill：** 指令单元，通常 **在主 context** 里执行 repeatable procedure。

**Subagent：** **独立 context** 做一大块工作（如 ideation 里的 review loop）→ 只 **report back 问题列表**，不污染主对话 context。

**Agent teams** 又是另一层——workshop 不展开，但别和 subagent 混为一谈。

可问 Claude「skill calling skill？」——它会 load analyzer skill 查文档，答案通常是 **能但不建议**。

---

### 12. Beyond Editor：Skills 是跨 surface 的工作流包

**非代码例：**
- Recruiting（Dust）：candidate 信息 → Slack/Notion/ATS **拉齐** → 统一格式 report  
- Blog writing：Tone/format 过去靠 Notion doc 逼人读；现在 **Skill 交互到 80% artifact**  
- Animated image Skill：~30 行 md + 2 Python scripts → 用户 prompt → 静图 → Veo animate（32 分钟片子 interstitials 就这么做的）  
- Remotion Skill：本地 :3000 预览，实时改 logo  

**WorkOS CI：** `workos install` 的 brains 全在 **skills directory**——Agent SDK 跑 programmatic Claude；**建 Skill = 证明 Skill 好 = CI 用同一 Skill**。

**分享：** Skill 文件夹 zip → 改 `.skill` 后缀 → 非技术同事 **拖进 Claude Desktop**（版本管理仍 pain，别塞 credentials）。

**RAG _pipeline  anecdote：** 从 flat chunking 改 **agentic tool calls + sideload WorkOS skills**，查询性能 **jump**。

---

### 13. Memory、Meta-Skills、从失败里挖矿

- Claude **built-in memory** + pruning；**auto dream** 类 consolidated memory 在实验  
- Zack 的 **Kase** agent（PI）：framework-specific memory md + retrospective **prune**  
- Obsidian connector：按日期 daily note → 「回顾上周」直接读 vault  
- **Meta：** 「用 skill-builder 回顾我一周 transcript，哪里最低效？帮我做 Skill」  
- **失败 conversation = gold**——pre-agent 时代周六 wipe keyboard；现在 **Jacques/L 日志** 全是 skill-creator 矿  

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Skill** | 按需加载的可组合工作单元（通常 SKILL.md + 可选脚本/引用） |
| **Description routing** | frontmatter description 给 LM 判断「何时自动 invoke」 |
| **Constraints > prescriptive** | 写禁止项/边界，少写逐步小说 |
| **Bang interpolation** | `!cmd` 执行脚本并把输出插入 prompt |
| **Progressive disclosure** | 主 Skill 路由，细节文件用时再读 |
| **Confidence gating** | 置信度不够先追问，够再出 contract/执行 |
| **Skill eval** | 对比有/无 Skill，确保不帮倒忙 |
| **DRY in agentic era** | 不重复交代同一流程 = Skill 化 |
| **Subagent** | 独立 context 干重活，摘要回主 thread |

---

## 值得记住的原话

> **"Skills are like carrying the DRY pattern into the agentic era."**  
> Skills 把 DRY 带进 agent 时代。

> **"Description is not for humans — it's for the LM to do routing."**  
> Description 不是给人看的，是给模型路由。

> **"You told me to do it. I didn't feel like it."**  
> （模型 skip 步骤时）——你知道这是真工程师了。

> **"Never be vague — never present a finding without script or git data backing."**  
> 别含糊——每条发现要有脚本或 git 数据支撑。

> **"All of that context is gold... rich context for a skill creator to mine."**  
> 失败和摩擦的 context 是 Skill 金矿。

> **"If you're not on the two hundred dollar month plan, this shouldn't even be a thought."**  
> （另一期 loop 语境，但同样适用）——别在错误预算下烧 token；Skill 是为了 **省重复劳动**，不是替代思考。

---

## 小结

**这期最核心的判断：** **Skill = agentic 时代的 DRY**——把重复流程、约束和脚本封装成可路由模块；**description 给模型做 routing**，constraints 优于长篇 prescriptive 步骤。

**读完应带走：**
- Progressive disclosure + bang 脚本：主 Skill 薄，细节用时再读；确定性靠脚本，不靠模型「感觉」。
- 失败与摩擦的 context 是 **Skill 金矿**；ship 前要有 **skill eval**，防 over-prescriptive 帮倒忙。
- 团队级 Skills 要 version / fork 治理，别在 monorepo 堆重复 roast Skill。

**和 vault 的关系：** 接 skills tag 与 [[LCA-60分钟变成AI-Native]] 的 Skill Chain——从个人 CLAUDE.md 到组织级能力封装。

---

## 行动启示

1. **Audit CLAUDE.md**：是否每次塞了只偶尔用的东西？能拆成 Skill 的 **立刻拆**。  
2. **写 Skill 先写 description + 3 条 constraints**，别先写 500 行步骤。  
3. **重复第二遍的 shell 查询 → bang 脚本化**。  
4. **大 reference → progressive disclosure**，主文件保持可路由的薄层。  
5. **Ship 前跑 eval**：新模型上线后 re-run；over-prescriptive 要敢删。  
6. **团队共享**：versioned plugin / fork locally，别在 monorepo 堆 10 个同名 roast Skill。  
7. **一周结束问 agent**：「该 solidify 成哪些 Skills？」——用 transcript 当输入。

---

## 相关阅读

- [[3-5 Skills - Agent 时代的知识分发系统]] — Skills 原理与 MCP 对比  
- [[Codex负责人-现场演示Codex]] — Codex 侧 Skills 与 multi-agent 工作流  
- [[Cursor-128个Agent团队协作]] — 大规模 agent 协作的另一路径  
- [[IBM团队-Harness工程详解]] — harness 可靠性；Skills 是 harness 内的知识单元  
- [[MOC - Prompt 工程]] — Prompt / Skills 横切索引  

---

## 来源

- **视频**：[BV18bjG6fEi7](https://www.bilibili.com/video/BV18bjG6fEi7/)（B 站转载 WorkOS Skills at Scale Workshop）  
- **嘉宾**：Nick & Zack，WorkOS Applied AI / DX Engineers  
- **材料**：Workshop repo（repo-roast skill、`dot/share.sh` 共享脚本）  
- **转写**：Recastory `A6-workos-skills/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02）
