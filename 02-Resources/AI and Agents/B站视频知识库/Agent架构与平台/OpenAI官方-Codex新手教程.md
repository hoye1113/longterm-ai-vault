---
title: "OpenAI官方：Codex新手教程"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV19MzXBNESV/"
speakers:
  - "Derek（OpenAI Customer Onboarding）"
  - "Charlie（OpenAI Engineer）"
duration: "52:54"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - codex
  - openai
  - mcp
  - harness_engineering
created: 2026-06-09
description: "OpenAI Derek 与 Charlie 官方 onboarding：Codex CLI/IDE 安装、AGENTS.md、config.toml 沙箱与审批、prompt 技巧、MCP/Context7、Codex Exec 结构化输出与 Agents SDK 多 Agent 编排。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV19MzXBNESV/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# OpenAI 官方：Codex 新手教程

## 先搞懂这一期

**这是什么节目？**  
OpenAI 客户 onboarding 团队的 **~53 分钟 Getting Started with Codex** 官方课（Derek + Charlie）。不是营销片，是 **CLI + VS Code 扩展** 手把手：clone agents.md 开源站、改 Hero、接 MCP、跑 review。

**这期在回答哪三个问题？**

1. **Codex 有哪些面、怎么装、怎么登录？** CLI / IDE / Cloud / SDK 各干什么？  
2. **AGENTS.md + config.toml 怎么让 Agent 每次进门就懂项目？**  
3. **从 prompt 到 MCP 到 headless `codex exec`，怎么嵌进 SDLC？**

**用一条线串起来（没看视频也能复述）：**

Codex = OpenAI **coding agent**（GPT-5.1 Codex Max 等在 Codex harness 里训）；面：**CLI**（轻量终端 + headless SDK）、**IDE 扩展**（任意 VS Code 系）、**Cloud**（关笔记本并行 async，如 PR review）。  
客户用法：**PR 开 Codex Cloud review**、**Slack @Codex 读整 thread 出 PR**、**SDK 自有容器结构化输出**。  
安装：`brew`/`npm` 装 CLI（更新频，顶栏提示新版本）；VS Code 搜官方 OpenAI Codex 扩展，**开 auto-update**。  
登录：`codex login` / IDE splash → SSO；`/status` 看 model、sandbox、approval、剩余 context。  
**AGENTS.md**：每次 session 零记忆 → 根目录 / 子目录 / `~/.codex` 全局 **AGENTS.md** 自动加载；`/init` 生成；**<100 行**、解锁 **test/lint 反馈环**、踩坑写回 agents.md；大任务指到 `plans.md` / `frontend.md` 做 **progressive discovery**。  
**config.toml**：默认 model、reasoning effort、sandbox、approval policy、profiles（如 `codex -p fast`）、MCP、终端完成 **notification**。  
Prompt：**@ 文件锚定**、小任务起步、verification steps、debug 贴 **full stack trace**、open-ended「下一步建什么」。  
IDE 技巧：TODO → Implement with Codex、**截图改 UI**、`codex resume` 续 session、生成 **mermaid 序列图**。  
MCP：`codex mcp add`；demo **cupcake MCP** + **Context7** 拉最新 OpenAI Responses API 做 agents.md 生成器。  
进阶：**codex exec** + JSON schema 结构化 code quality 报告；Agents SDK 里 Codex 当 MCP tool 多 Agent handoff；自托管 PR review / autofix CI / issue auto-label。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| Codex = ChatGPT 写代码 | **多 surface + Cloud 并行** + **headless exec** |
| README 给 AI 看就行 | **AGENTS.md** 专给 agent loop；plans.md 做大任务 living doc |
| MCP 可选装饰 | Context7 / 自建 doc MCP = **克服 knowledge cutoff** |
| Code review 另一工具 | Codex review **只报 P0/P1**，噪声低才有人用 |

---

## 分话题讲

### 1. Codex 产品面与模型

**说法：**  
- **CLI**：日常交互 + **`codex exec` headless** 进 CI/CD。  
- **IDE 扩展**：Rich GUI，local / **cloud** 任务，chat vs agent vs full access。  
- **Cloud**：笔记本合上也能跑 code review、mobile 触发。  
- 模型在 **Linux/macOS/Windows + bash/PowerShell** 环境训，遵守 sandbox；擅长 **auto-compact** 长跑 refactor。

**和你何干：**  
同一 harness 贯穿 **7 阶段 SDLC**（OpenAI《AI engineering team》指南）——今天入门，明天可挂 review/autofix。

---

### 2. 安装、登录、跟练仓库

**说法：**  
优先 **npm/brew** 装 CLI；开源可下 GitHub binary。IDE 认准 **OpenAI 官方**扩展。  
Work + ChatGPT Enterprise SSO 登录后 CLI/IDE **共享会话**。  
跟练：clone **agents.md** 微站 → `npm install && npm run dev` → 全程在同一 repo 上改 Hero、加按钮。

**和你何干：**  
官方刻意用 **agents.md 站** 教 AGENTS.md——meta 但好用。

---

### 3. AGENTS.md：每次 session 的 TL;DR

**说法：**  
Coding agent **不跨 session 记忆** → AGENTS.md 自动注入「项目怎么回事」。  
层级：**~/.codex/AGENTS.md 全局**、repo 根、**子目录**（进目录加载服务上下文）。  
推荐段落：overview、structure、build/test、常用 CLI、MCP 列表、**feature 端到端 workflow**、指向 task-specific md。  
最佳实践：**短而聚焦**（OpenAI 内部 <100 行）；给 **lint/test 反馈**；Codex 卡壳的命令 **写进 AGENTS.md**；大 refactor 用 **plans.md 模板** checklist Living document（工程师 **10+ 小时 refactor** 案例）。

**和你何干：**  
AGENTS.md = harness 的 **静态 context 层**，和 [[2026 年 Agent 最重要的工程概念 Harness Engineering]] 里 docs-as-truth 同族。

---

### 4. config.toml：默认行为与安全

**说法：**  
Rust 写的 CLI 用 **config.toml** 设：model、reasoning effort、**sandbox mode**、**approval policy**、web search 默认、MCP、profiles。  
默认：**approval on-request**（要到 escalated 权限才问你）；**workspace-write sandbox**（只写当前目录）。  
可改更严或更松；Charlie 爱 **terminal notification**——后台跑完响铃。

**和你何干：**  
团队统一 **toml + AGENTS.md** = 新人 `codex` 进来行为一致。

---

### 5. Prompt 最佳实践

**说法：**  
1. **`@file` 锚定**——防 agent 逛错目录。  
2. **小任务起步**，熟了再变大；可让 Codex **纯 research 拆 task**。  
3. **Verification steps**（tests/lint）写 prompt 或 AGENTS.md。  
4. Debug：**整段 stack trace** 粘贴。  
5. Open-ended：「这 feature 做完下一步建什么？」CLI 会给 **suggested next steps**。

**Starter tasks：** explain codebase、写 README、fix bug、扩测试、跨文件 refactor、**写文档**。

**和你何干：**  
Prompt 是 **ultimate context**，但 recurring 验证应 **沉到 AGENTS.md**。

---

### 6. CLI / IDE 技巧

**说法：**  
- CLI/IDE **`@` 文件**；IDE **Cmd+Shift+C** 绑「选中行加 context」。  
- 代码里 **TODO → Implement with Codex**。  
- **截图 prompt** 改 UI（inline chip 改橙色）——比「左边第三个按钮」可靠。  
- **`codex resume`** / session ID 续聊；IDE 搜历史 task。  
- 生成 **mermaid sequence diagram** 理解 repo 流程。  
- Custom prompts：`~/.codex/prompts/add-test.md` → CLI 里 `@add-test` 拉单元测试模板。

**和你何干：**  
Session = **迷你项目容器**（front-end feature 一条 session、test 一条 session）。

---

### 7. MCP：Cupcake → Context7

**说法：**  
Codex 支持 stdio + HTTP MCP。常见：Figma、Jira/Linear、**Context7**（最新框架 doc）、Datadog。  
Live：`codex mcp add` 注册 **cupcake MCP** → 改 agents.md 页脚显示 Rachel 订了 7 个 marble cupcake。  
进阶：Context7 + **Responses API** 在 agents.md 站加 **「输入 prompt 生成 AGENTS.md」** 输入框；全局 AGENTS.md 可写「新 API **总是先搜 Context7**」。

**和你何干：**  
MCP = harness **动态 context**；doc MCP 解决 **训练 cutoff**。

---

### 8. Code Review 与进阶编排

**说法：**  
- CLI：`codex review`（对 base branch / uncommitted / 指定 commit + 自定义指令）。  
- IDE：slash **code review**；只表面 **P0/P1**（太吵会被 ignore）。  
- **`codex exec --output-schema`**：JSON schema 约束 code quality 报告 → CI/DB/API。  
- **Agents SDK**：frontend agent / PM agent handoff，Codex 作 MCP tool；trace 可见每次 handoff。  
- 自托管：**on-prem PR review**、**autofix CI**（测试失败自动 PR fix）、**issue auto-label**（Codex 开源 repo 在用）。

**和你何干：**  
从 **交互式 codex** 到 **pipeline 里 silent exec** 是团队规模化分界线。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Codex CLI / IDE / Cloud** | 本地终端、VS Code 侧栏、云端并行容器 |
| **AGENTS.md** | 每 session 自动加载的项目 Agent 说明书 |
| **plans.md** | 大任务 checklist living doc，可 progressive discovery |
| **config.toml** | CLI 默认 model、sandbox、approval、MCP |
| **Approval policy / Sandbox** | 何时问权限、能写哪些路径 |
| **codex exec** | Headless 模式 + 结构化 JSON 输出 |
| **Context7 MCP** | 拉最新第三方库文档 |
| **codex resume** | 恢复带完整 context 的旧 session |
| **Progressive discovery** | AGENTS.md 指向子文档，按需读取 |

---

## 值得记住的原话

> **"Coding agents don't retain any context between sessions… AGENTS.md ensures instructions are always loaded automatically."**  
> Agent 不记上次 session——AGENTS.md 保证说明每次自动加载。

> **"Keep it brief… Most of OpenAI's AGENTS.md files are less than 100 lines."**  
> 保持简短——OpenAI 内部 AGENTS.md 大多不到 100 行。

> **"Give the agent feedback from tools like lint, tests… it accelerates how much the agent can do."**  
> 给 lint/test 反馈环，Agent 能独跑更远。

> **"Anchor it with @ mention… a lot of times it goes off the rails because it starts in the wrong part of the codebase."**  
> 用 @ 文件锚定——跑偏常因从错误目录开始。

> **"Code review can't be too noisy… trained to focus on P0/P1."**  
> Review 不能吵——模型被训成只抓 P0/P1。

> **"Codex exec… structured output… build into CI/CD pipeline."**  
> Headless exec + 结构化输出，可塞进流水线。

---

## 小结

**这期最核心的判断：** Codex 入门 = **AGENTS.md（项目记忆）+ config.toml（安全默认）+ 验证环**；熟练后接 **MCP 动态 doc** 与 **`codex exec` 结构化流水线**，Cloud/Slack 把同 harness 扩到 async 协作。

**读完应带走：**
- `/init` 生成 AGENTS.md，踩坑写回，大任务用 plans.md。  
- Prompt 要 @ 锚定 + verification；UI 用截图。  
- Review 要 quiet；exec + schema 才适合 CI。

**和 vault 的关系：** Codex 官方入门锚点，接 [[Codex负责人-现场演示Codex]]、[[Codex实战-构建全能AI营销团队]]、[[MOC - Harness Engineering]]。

---

## 行动启示

1. **Repo 根放 AGENTS.md**（<100 行）+ build/test 命令 + 指向 frontend.md/plans.md。  
2. **团队 config.toml** 统一 sandbox；个人 global AGENTS.md 放 Context7 规则。  
3. **新功能先 research 拆 task**，再 agent mode 实现，结尾跑 review uncommitted。  
4. **~/.codex/prompts/** 沉淀 add-test 等重复 prompt。  
5. **试点 codex exec + JSON schema** 做安全 triage 或 changelog 自动化。

---

## 相关阅读

- [[Codex负责人-现场演示Codex]] — 负责人级 knowledge work 与并行 demo  
- [[Codex实战-构建全能AI营销团队]] — 创作者侧 Skills 栈  
- [[2026 年 Agent 最重要的工程概念 Harness Engineering]] — OpenAI harness 实验叙事  
- [[IBM团队-Harness工程详解]] — verify/guardrails 第一性原理  
- [[MOC - Agent Theory and Design]] — Agent 理论横切索引  

---

## 来源

- **视频**：[BV19MzXBNESV](https://www.bilibili.com/video/BV19MzXBNESV/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Derek、Charlie（OpenAI Customer Onboarding / Engineer）  
- **时长**：~52:54  
- **转写**：Recastory `bilibili-retranscribe/BV19MzXBNESV/`（FunASR SenseVoice + cam++，**asr v2 后处理** 52 段）  
- **跟练仓库**：[agents.md](https://agents.md/) 开源微站  
- **文档**：developers.openai.com/codex、OpenAI Cookbook  
- **版本**：v2 读者向讲义（2026-07-02）
