---
title: "DeepMind团队：当数百万 Agent 相遇"
source: "B站视频 - Google DeepMind: The Podcast"
source_url: "https://www.bilibili.com/video/BV1ixKX6oEzK/"
speaker: "Nana Jaques (Google DeepMind 高级研究员) / Hannah Fry (主持)"
duration: "42:38"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - multi_agent
  - ai_safety
  - harness_engineering
created: 2026-07-02
description: "DeepMind 研究员 Nana Jaques 用婚礼订场地、写代码、Agent 互相砍价等例子，解释 Agent 与聊天机器人的区别，以及数百万 Agent 形成「Agent 社会」时的安全与对齐难题。"
transcript_source: "Recastory/workspace/knowledge/A1-deepmind-million-agents/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# DeepMind团队：当数百万 Agent 相遇

## 先搞懂这一期

**这是什么节目？**  
Google DeepMind 官方播客。主持人 **Hannah Fry**（数学家、科普播客）采访 DeepMind 高级研究员 **Nana Jaques**。整期约 43 分钟，是一段**对话**，不是单人演讲。

**这期在回答哪三个问题？**

1. **Agent 和 ChatGPT 这类「聊天 AI」到底差在哪？** 用起来有什么不同？
2. **如果将来有成百上千万个 Agent 不只替人干活，还在彼此之间订票、砍价、派活，会怎样？** 会不会出现一种新的「Agent 经济」？安全吗？
3. **通向更强 AI 的路，是做一个「什么都会的万能助手」，还是很多「专才 Agent」组成的社会？** 这对「对齐 / 安全」意味着什么？

**用一条线串起来（没看视频也能复述）：**

以前你问 AI 一个问题，它答一句话——**只动嘴，不动手**。  
现在 **Agent** 是：大模型外面套一层 **harness（执行框架）**，能看当前状态、调用工具、连续做多步（发邮件、订餐厅、写代码）。**你还是老板**：界面像聊天，但角色从「提问者」变成 **审批者**——Agent 拟好邮件，你点头，它再发。

今天 Agent **最靠谱的是写代码**；订婚礼、管科学实验还远。原因是：会犯错、会幻觉，人要全程盯着，不能因连续做对几次就放松验证。

再往前想一步：Agent 不只听人的，还会 **互相委托**（A 把买酒交给 B，B 把订场地交给 C）。若规模到百万级，就像一片 **Agent 社会**——有通才、有专才、有专门负责拆任务的「调度者」。Nana 认为：**最终形态可能不是「一个超人 Agent」，而是「很多专才 + 一个协调层」**，更像人类社会分工，而不是复制某一个全能个体。

这时安全变了：不仅要管**单个** Agent 别乱来，还要管 **成千上万个 Agent 一起行动** 时的系统性风险（网页陷阱、集体犯同一种错、拍卖串通等）。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 会用 ChatGPT / Claude 聊天 | Agent = 聊天 AI + **能动手**（工具、多步、代你执行） |
| 听过 Multi-Agent、OpenClaw | 不只「多个 Agent 并行写代码」，而是 **Agent 之间交易、委托、形成经济** |
| 听过 AI 安全、对齐 | 从「对齐一个模型」变成 **「对齐一整片 Agent 社会」** |

---

## 分话题讲

### 1. Agent 和 LLM：一个动嘴，一个还能动手

**说法：**  
- **LLM（大语言模型）**：你问一句，它续写一句——**文本进、文本出**，不改变世界。  
- **Agent**：先**观察**环境状态，再**行动**（调 API、发邮件、跑代码），外面有 **harness** 把模型的「打算」变成真实操作；还能 **自动串多步**（先查档期，再起草邮件，再等你批准发送）。

**例子（婚礼）：**  
- 只问 LLM：给你 caterer 名单、场地建议，**邮件你自己发**。  
- 用 Agent：可接 Gmail，**代你起草并发送**——但必须 **人工核对邮件内容**，发错没有 undo。

**和你何干：**  
如果你在用 Cursor / Claude Code，你已经在用 Agent 形态：**模型 + 工具 + 多轮执行**；区别是这类产品把 harness 做好了，你不用自己拼。

---

### 2. 用起来什么感觉：还是聊天，但你变成「审批经理」

界面仍像和 AI 说话。变化在于：

- 以前：你一步步 prompt，像 **微操**。  
- 现在：Agent 自己规划多步，你主要在 **关键点 approve / reject**。  
- 它去订餐厅、发消息时，你可以去干别的——**前提是你会回来检查**，不能默认「肯定没错」。

Nana 强调：**不是 Agent 能不能做，而是做不到 100% 准确**；步骤越复杂，出错概率越高（和人一样）。  
还有一个老问题叫 **自动化偏见**：Agent 连续成功几次，人就不再细看，漏掉隐蔽错误。所以 harness 的设计目标之一是：**人要在环里，且要保持清醒**——一松懈，「全靠运气」。

---

### 3. 今天 Agent 真正擅长什么：写代码一马当先

全行业都在 **堆 Agent 能力**。现实里 **最好形式化的是软件 / 代码**：

- 内外部 coding Agent 已大量用于加速开发；  
- 人更多放在 **想法和设计**，样板代码、冷门 API 知识交给模型。

但 **全程仍要人监督**——coding Agent 不是无人值守的生产线。

**科学**是 Nana 更远的愿景：不只当「论文 co-author 帮想点子」，而是 Agent 能 **预约实验、跑 wet lab、读结果再决定下一步**。难点在于：

- 写软件：写单元测试就能验证；  
- 做实验：要碰真实世界（电池过热烧设备、生物安全等），必须 **safeguard + 可靠协议** 才能闭环。

**短期结论：** 现有模型擅长 **把人类已有技能组合、补小缺口**（她称为 compositional closure），**还没看到**「做出人类从未想过的科学发现」。所以 **人仍然重要**。

---

### 4. 为什么 Agent 概念很老，你现在才摸得到：缺的是「编排」，不是缺模型

Agent 在强化学习游戏里就有（在模拟环境里捡东西、做任务）。企业里也有「窄 Agent」（数据中心自动化、交易算法），但 **没有语言界面**，普通人碰不到。

**大模型时代的关键变化：** Agent 能 **跟你说话**，你能 ** steer（ steering）** 它——所以大众才开始用。

那为什么还不能「一个助手包办一切」？Nana 说：过去几年精力在 **把模型做强**；模型够用了之后，瓶颈变成 **怎么协调、编排、管理很多 Agent**。  
你要把自己当成 **管一支 Agent 团队的经理**：

- 和人管团队有共通处（分工、跟进）；  
- 不同处：Agent 会犯 **非人类式错误**，又 **不够了解你**，不能指望它「猜到你所有心思」，所以 **编排（ orchestration）** 能力变得关键。

另外：人仍难完全信任 Agent 代劳 **敏感动作**（幻觉可能导致严重后果）。信任 **可以建立，也要赚回来**——例如 **声誉追踪**：某个 Agent  repeatedly 不靠谱，系统应降低对它的信任；即使 mostly reliable，也 **不能盲信**，该验还得验。

---

### 5. 委托：复杂任务要「派活」，但今天的 Multi-Agent 多半在「并行瞎分」

**简单任务：**「明天在这家餐厅订位」——一个 Agent + 工具就够。

**复杂任务：** 大计划拆成多块，可能 **没有单个 Agent 能全做**，就要 **Agent 之间 hand off**（通过 agent-to-agent 协议）。  
委托方（人或 Agent）还要 **处理失败、尽量预防**：派活前要知道 **对方靠不靠谱**、能力是否可认证；还要防 **恶意交互**。

**婚礼统筹类比：** 场地黄了、货没到——人当总策划要兜底；**派给一群 Agent 的总 Agent** 也要能处理这些失败。

**她批评的现状：** 很多所谓 multi-agent 系统其实是 **并行（parallelization）**——把任务 **随机切成块** 分给多个 Agent 同时干，求速度；**不是**  intelligent delegation（按依赖关系 intelligently 拆分）。  
后果：一个 Agent 买酒、另一个买杯子，**可能互不沟通**，杯子数量对不上。

**软件 vs 真实世界：**  
- 写软件：单元测试能验；  
- 买酒：「好不好喝」带主观性，还可能出现 **reward hacking**（字面满足要求、 spirit 不对——例如订了最便宜但很难喝的酒）。

**任务分两类：**  
- **可逆**：搞砸了重来、换 Agent 再派；  
- **不可逆**：花了钱、发了邮件——要 **格外谨慎**。

**反直觉：** Agent **也可以把人当工具**——Nana 在医疗影像里的经验：窄模型在某种扫描上超人类，但会错；**不确定时把 case 转给人类 radiologist 复核**，这种 AI→人的委托在特定场景里很有效。通用 Agent 里类似：**敏感操作仍应 delegate 给人批准**。

---

### 6. 安全：Agentic traps——网页可以给 Agent 下套

Agent 在 **开放网络** 上行动时，会有人 **设陷阱（agentic traps）**：

| 手段 | 什么意思 |
|------|----------|
| **Prompt injection** | 网页里藏人类看不见的文字，Agent 读页面源码时被改目标（例如买酒 Agent 逛到恶意商家网站） |
| **Dynamic cloaking** | 同一 URL，**给人看正常页，给 Agent 看恶意内容**（根据访问行为判断是不是 Agent） |

早期在内网、受控环境试验时问题少；**一旦 Agent 大规模上网**，攻击面变大。Nana 提到一个趋势：**Agent 生成和消费 web 内容的比例，可能首次超过人类**——等于出现 **「给人看的 web」和「给 Agent 看的 web」** 两套逻辑，广告、SEO 都会变。

**怎么防？** 不是 Agent 内部加一道护栏就够。她强调 **纵深防御（defence in depth）**——多层叠加，指望「没有单层万能」：

- 认证 / 检测网页内容是否可信；  
- Agent 侧、模型侧 mitigation；  
- ** meaningful human control**，出事能介入；  
- **最小权限**：就算被 jailbreak，损失也有限。

类比：邮件病毒、点错链接——**老问题在新载体上重演**；对抗样本（改几个像素骗模型）也早就存在。

---

### 7. Agent 经济：个人助理互相砍价，以及「集体犯同一种错」

**日常层面：** 每人有一个 **长期记忆你偏好的个人助理**；你给它预算，它可能 **替你去砍价、订服务**——形成 **localized agent economy**。

Hannah 举 **Taylor Swift 演唱会抢票**：若全是 Agent 在抢，怎么算公平？Nana 说：**规则是人设计的**——例如每人/agent 同等预算，Agent 根据你的偏好、行程、意愿分配出价，总体希望 **人口尺度上更公平**（类似抽签、积分等人类机制可以迁移）。

**金融层面：** 高频交易曾出过 flash crash。金融市场 **已有** 一套缓解经验，不必从零发明；但 Agent 时代多一个新问题：

**认知单一文化（cognitive monoculture）：**  
市面大量 Agent 底层是 **少数几个大模型**（Claude、GPT、Gemini 等），**决策方式相似**。当成千上万「 artificial decision makers」一起行动时，**失败点会相关**——一起买错、一起踩坑。  
对策思路：**让决策多样化**（高级用户可用复杂 system prompt 给 Agent 「性格」）；还要防 **串通（collusion）**——Agent 可能通过环境 **间接协调**，不直接通信。

因此 Google **谨慎、渐进发布** 不奇怪——像自动驾驶：demo 很早，真正上路又花了很多年，**最后一公里** 最难。Agent 要融入 **人类现有结构**，不能假设短期就有完全自治的 Agent 经济。

---

### 8. 终极图景：也许该复制「人类社会」，而不是「一个超人」

Hannah 总结 Nana 最让她记住的一点：

> **只盯「单个 Agent 多强」会 miss 大图。**  
> 每个客户端 Agent 可能只是 **更大 Agent 社会** 里的一分子——有通才、专才、专门 delegate 的、专门抠细节的。

**国际象棋类比：** 通用大模型现在也能下棋了，但 **专业象棋引擎** 更快、更准、更便宜——因为 **只做一件事**。

**人类类比：** 我们常说追求「人类水平智能（human-level）」，但 **没有任何一个人** 会所有技能。真实世界是 **humanity-level**：社会分工、专才协作。

Nana 的猜测（个人观点，非 DeepMind 官方结论）：

- 经济上 **没有动力** 养一个又贵又慢的全能模型干所有活；  
- 更可能：**一层薄的「协调 / 连接层」** + **大量认证过的专才 Agent**（便宜、可靠）。

**对安全 / 对齐的含义：**  
现在对齐主要是 **盯一个模型** 的行为是否符合人类偏好。若变成 **一万个 Agent  intricate 交互**——今天 A 和 B 协作，明天 A 和 C，中间还问人——**整个系统边界都难定义**，对齐对象从「一个实体」变成「分布式系统」。  
经济激励（别让 Agent 为利润最大化伤害人）可能是 **起点之一**，但 **单个 Agent 安全只是必要不充分**——还要研究 **群体安全**。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Agent** | 能观察环境并行动的多步 AI 系统，通常 LLM + harness + 工具 |
| **Harness** | 套在模型外的执行框架：接工具、管权限、串步骤 |
| **Human-in-the-loop** | 关键步骤人要审批，不能全自动到底 |
| **Delegation** | 把子任务派给另一个 Agent（或人） |
| **Parallelization vs intelligent delegation** | 并行切块提速 vs 按任务逻辑/smart 拆分并协调 |
| **Agentic trap** | 恶意网页 / 环境诱导 Agent 做坏事 |
| **Prompt injection** | 隐藏指令篡改 Agent 目标 |
| **Dynamic cloaking** | 对人/Agent 显示不同网页内容 |
| **Defence in depth** | 多层防护叠加，不指望单点万能 |
| **Agentic economy** | Agent 之间交易、委托、竞价形成的市场 |
| **Cognitive monoculture** | 太多 Agent 用同一类模型，集体犯同样错 |
| **Human-level vs humanity-level** | 复制「一个全能人」vs 复制「分工社会」 |

---

## 值得记住的原话

> **"An agent observes state of the world and performs an action... whereas the language model just gives you continuation reply to prompt."**  
> Agent 会看环境并行动；语言模型只会续写你的问题。

> **"You are more in the position of a decision maker to review and approve."**  
> 你更像决策者：审完、批准，它再去执行。

> **"As soon as you switch off [verification], you're all in the dice."**  
> 人一旦不再认真检查，就全靠运气。

> **"We need to see ourselves as managers of teams... develop personal management skills to handle these workflows."**  
> 我们要把自己当成 Agent 团队的经理，学会编排。

> **"Many multi-agent systems act more as parallelization than delegation."**  
> 很多 multi-agent 只是在并行，不是在 intelligent 派活。

> **"Trust is given, but it's also earned."**  
> 信任可以给人，也要靠表现赚回来。

> **"Defence in depth... mitigations upon mitigations."**  
> 纵深防御：一层层 mitigation 叠上去。

> **"Cognitive monoculture... failure points become correlated."**  
> 模型太同质，Agent 集体翻车会同步发生。

> **"Maybe replicating human-level intelligence isn't the ultimate goal... humanity-level intelligence instead."**  
> 也许目标不是复制一个超人，而是复制人类社会的分工协作。

---

## 小结

**这期最核心的判断：** Agent 的终局可能不是「一个超人助手」，而是百万级 **Agent 社会**（专才 + 协调层）；安全与对齐要从「单个模型」扩展到「分布式系统 + 经济激励」。

**读完应带走：**
- Agent = LLM + harness，角色从提问者变成 **审批经理**；写代码领先，但 automation bias 和幻觉让 human-in-the-loop 不可省。
- 今天的 multi-agent 多是 **并行切块**，不是 intelligent delegation；Agent 上网会遇 **agentic traps**，要靠纵深防御和最小权限。
- **Cognitive monoculture** 会让集体失败相关；**humanity-level 分工** 可能比 human-level 全能更符合经济与技术现实。

**和 vault 的关系：** 接 [[MOC - Harness Engineering]] 与 multi_agent 主题——从单 Agent harness 延伸到 Agent 社会、委托与经济。

---

## 行动启示

1. **用 Agent 时默认你是经理，不是甩手掌柜**——尤其不可逆操作（发邮件、付钱）。  
2. **Multi-Agent 架构先问**：是 intelligent 派活，还是并行切块？有没有跨 Agent 的沟通 / 契约？  
3. **上网行动的 Agent 要最小权限 + 人可介入**，假设网页可能被投毒。  
4. **别假设一个万能 Agent 覆盖所有场景**——专才 + 协调层可能是经济和技术上的终局。  
5. **安全思维要从「模型对齐」扩展到「系统 / 群体对齐」**——若你做 agent 平台或编排层，这是下一层问题。

---

## 相关阅读

- [[Agent实战-打造一个AI Agent的完整教程]] — Agent 入门与 Observe-Think-Act 循环  
- [[DeepMind-模型将吞噬Harness]] — Google 侧 harness 与「模型吞噬脚手架」的另一视角  
- [[IBM团队-Harness工程详解]] — harness 可靠性第一性原理  
- [[MOC - Harness Engineering]] — Harness 主题索引  

---

## 来源

- **视频**：[BV1ixKX6oEzK](https://www.bilibili.com/video/BV1ixKX6oEzK/)（B 站转载 *Google DeepMind: The Podcast*）  
- **嘉宾**：Nana Jaques，Google DeepMind Senior Staff Research Scientist  
- **主持**：Hannah Fry  
- **转写**：Recastory `A1-deepmind-million-agents/article.md`（英文 ASR，收录时已人工整理叙事）  
- **版本**：v2 读者向讲义（2026-07-02，含 §小结）
