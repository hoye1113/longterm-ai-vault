---
title: "a16z：AI 并非泡沫"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV1UajG6oEvj/"
uploader: "Easonlee的AI笔记"
saved: 2026-07-02
tags:
  - ai_agent
  - ai_career
  - video_transcript
  - bilibili
created: 2026-07-02
description: "a16z 合伙人在 LP 对话中论证 AI 非泡沫：模型公司 revenue 增速超 hyperscaler、经济渗透仍低、供给全面短缺；value capture 关键在 token path 与 frontier 竞争结构。"
transcript_source: "Recastory/workspace/knowledge/B3-a16z-ai-bubble/article.md"
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# a16z：AI 并非泡沫

## 先搞懂这一期

**这是什么节目？**  
a16z 合伙人在 LP / 行业对话里，更新 **2024 年 11 月后** 对 AI 市场的 prior。整段是对话，不是单人演讲——核心论点是：**当前不是典型 AI 泡沫**。

**这期在回答哪三个问题？**

1. **AI 到底是不是泡沫？** 模型公司 revenue 已经很大，和「泡沫」叙事怎么对得上？
2. **钱会往哪流？** 企业愿意为 AI 付多少？谁能在 value chain 里 capture 价值？
3. **对创业者和投资人意味着什么？** 退出规模、估值、loss ratio、public market 怎么变？

**用一条线串起来（没看视频也能复述）：**

2024 年 11 月之后，a16z 改了两个大 prior：**scale** 和 **value capture**。

**Scale 这边**：OpenAI + Anthropic **每月新增 revenue 已超过 Meta 或 Microsoft 单家**——不是「将来可能」，是已经在 hyperscaler 量级上跑。但除 coding 和 tech-forward 公司外，AI 在全经济的渗透率仍 **<5%**。一边是 revenue 已经很大，一边是真实经济还没铺开——a16z 认为 outcomes 会 **extraordinary**。Fortune / S&P 500 合计约 **2 万亿美元/年利润**，是 enterprise AI 支出的 realistic 上界；两家 model 公司 run rate 年底或到 **2000 亿美元**，约等于 Fortune 500 利润的 **10%**。

**泡沫这边**：典型泡沫是 **过剩供给摧毁 economics**。现状相反——算力、HBM、数据中心、电力、数据科学家 **全面短缺**；大规模 capacity 或要到 **2028 末–2029 初**；美国 datacenter buildout 还 **落后 schedule 约一年**。所以是 **supply constrained，not demand constrained**。唯一可能 flip 到 oversupply 的，是算法 breakthrough 让模型小几个数量级——短期 unlikely。

**Value capture 这边**：prior 在 model vs application 之间 **cycle 过好几轮**；当前共识是 **必须在 token path**。买方 cost pressure 已来——预算不会按旧 SaaS 曲线涨，价值要么来自 **涨价**，要么来自 **劳动力重构**。**Model market structure**（frontier 几家竞争）是 nobel 变量：oligopoly → token 价高 → 重构压力更大；多 frontier 竞争 → 对整体经济更友好。中国模型约 **落后美国 6 个月、便宜 10 倍**——份额仍 unknown。

**投资节奏**：Top 1% exit 门槛从 2024 的 **100 亿** 飙到 2026.03 的 **320 亿**；AI 50 列表年换血 ~**40%**——first mover 不等于 winner。~**80% 公司 overvalued** + 少数 **massively undervalued**；早期 VC 不应追求低 loss ratio。Public market 缺 fast-growing names——hypergrowth AI IPO 是利好。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| 听过「AI 泡沫」争论 | **供给短缺 vs 需求虚高**——本轮瓶颈在算力/电力，不是没人买 |
| 知道 OpenAI / Anthropic 很赚钱 | **revenue 大 + 渗透 <5%** 的剪刀差——上行空间锚在 Fortune 500 利润池 |
| 在做 AI 产品 / Agent | **token path**——不在 inference 消费链上，要想清楚怎么 capture value |
| 关心 AI 时代职业 | **skeuomorphic 提效 → native proactive AI**；劳动力重构是 spend 来源之一 |
| 看 VC / 创业 | Top 1% exit 加速、AI 50 高换血、platform moat 因 AI 公司极早撞 big-company problems |

---

## 分话题讲

### 1. Revenue 与渗透率：已经很大，经济还没铺开

2024 年 11 月后 prior 巨变：Anthropic + OpenAI **月增 revenue 超过 Meta 或 Microsoft 单家**，已处 hyperscaler 量级。

但除 coding 与 tech-forward 公司外，**全经济 AI 利用率 <5%**。Legal 等白领职能刚开始有 coding 式渗透，还远。

配对结论：revenue 已大、渗透还浅 → outcomes **extraordinary**。Fortune / S&P 500 合计 ~**2T/年利润**——AI 企业支出上界 realistic anchor；OpenAI + Anthropic run rate 年底 ~$200B ≈ **10% of Fortune 500 profit**。

Open source 曾被认为是 cost 解法——a16z 更新 prior：**cost pressure 来得比预期快**，open source 反而 **更重要、更早**。

---

### 2. 不是典型泡沫：供给约束，非需求过剩

泡沫特征：**过剩供给摧毁 economics**。

现状相反：
- 算力、memory、数据中心、电力、数据科学家 **全面短缺**
- 大规模 capacity 或到 **2028 末–2029 初**
- 美国 datacenter buildout **落后 schedule ~1 年**
- TSMC 等 showing restraint；社区对 datacenter 阻力「绝对 crazy」——运营商进小区说建 preserve、捐学校、创就业，仍被「耗水」拦

唯一可能 flip 到 oversupply：**算法 breakthrough** 使模型小几个数量级（human brain 效率类比）——short term unlikely。

$5T capex vs $1–2T revenue return——若仅两家 model 公司 run rate $200B，equation **comfortable**。

---

### 3. 应用 wave：skeuomorphic → native proactive

两阶段：

| 阶段 | 特征 |
|------|------|
| **Skeuomorphic** | 用 AI **更高效地做现有工作**（多数公司 today） |
| **Native AI** | Agentic、**reactive → proactive**；公司 run differently |

Cutting edge 公司投 **新产品** 而非自动化现有流程——最好的人在做 product，不是 internal automation。mature 公司更适合 automation，但是 **slow adopters**；incumbent dollars 暂不在 efficiency gains。

现场已见 founder **whisper 给 agent**，跑 agent swarms——「future, just really early」。文档化一切、尽量 capture context，是 very early 的 internal 方向。

---

### 4. 退出规模加速：Top 1% exit 门槛在飞

| 时间 | Top 1% exit 门槛 |
|------|------------------|
| 2024 | $10B |
| 2026.02 | $20B |
| 2026.03（仅 closed） | $32B |

OpenAI + Anthropic 若 2026.09 IPO，combined 或 **>$100B**——**大于整个 Russell 2000**。Value creation **pace 快于 prior cycles**；AI 50 列表年换血 ~**40%**——first mover defensibility 更难 predict。

Largest companies 继续 **order of magnitude bigger**，且在 **accelerating**——top 1% exit 每五年翻倍。

---

### 5. Value capture：必须在 token path

Prior 在 model vs application 间 **cycle 多次**（application 全灭 → model 只是 API → model 又 leg into application 求 stickiness）。

当前共识：
- 公司必须在 **token path**
- 买方 **cost pressure** 已来：预算不会按旧 SaaS 曲线涨；AI cost 增长甚至难被 cover
- 价值来源：**涨价** 或 **劳动力重构**
- **Model market structure** 是 nobel 变量：frontier **oligopoly** → token 价高 → 重构压力更大；**5 家竞争** → 价低 → 对整体经济更友好
- 当前 frontier intelligence **ineelastic**；per-token cost 降 10×+，但 frontier dollar appetite **massively increasing**

中国：leading models ~**6 个月落后** US，但 **10× cheaper**（DeepSeek 等）——份额 unknown；distillation ~2% pretrain cost 若持续 → 利好 open source。

---

### 6. 投资哲学：不追求低 loss ratio

早期 VC：**不应 target 低 loss ratio**——「never lost money on a deal」是 **horrible**（没冒够险）。

Philosophy：talented founders + tail winds + tech POV → back leader；space 不成 + 有 leader = no harm；space 成 + 没 leader = 坏 outcome。

当前 AI 轮 loss ratio ~**single digits**——不可 sustained，但 power law justify。~**80% 公司 overvalued** + 少数 **massively undervalued**——LP 难 pick individual names；a16z 强调 **early stage + slugging percentage**。

AI 公司 **极早撞 big company problems**（$B revenue、complex cloud deals、international）→ VC **platform**（sales/pricing/channel 专家）成 moat，firm 随 entrepreneur preference scale。

---

### 7. Public markets：mega-IPO 是利好

OpenAI/Anthropic 等进 public market while **hypergrowth**——对 investor community **really good**。Index inclusion 讨论中；exclude datacenter supply chain 后，public market **few fast-growing names**（Mag7 sub-30% growth）。

Ten years from now：最大的公司会比今天想象的大得多——类似 Mag7 从「想不到 4–5 万亿」到 reality。

---

### 8. VC 行业 5 年后：model market structure 是最大 driver

Unknowns 太多无法 pontificate，但 **#1 driver** = labs market structure、open source role、token 竞争、cost trajectory。

Bill Gates platform quote：built on top 的价值须 exceed platform——乐观 case：**labs extraordinarily valuable + massive ecosystem on intelligence**。

Consumer 侧 excited：过去十年 time spent 被 big tech 捕获；新技术 breakthrough 或 shift **consumer attention** → extraordinary outcomes。B2B 讨论多，consumer shift **early**。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **Token path** | 价值捕获须在模型 inference 消费链上 |
| **Supply constraint** | 算力/电力/人才短缺，非需求泡沫 |
| **Diffusion <5%** | 除 coding 外，AI 在全经济渗透率仍极低 |
| **Skeuomorphic vs Native** | 用 AI 提效旧工作 vs AI-native 新产品/组织 |
| **Top 1% exit** | 顶级 VC 退出门槛（2026.03: $32B） |
| **Model market structure** | frontier 竞争数决定 token 价与重构压力 |
| **Power law** | 少数 winner 承担高 loss ratio |
| **Slugger percentage** | growth 阶段 portfolio 集中度策略 |

---

## 值得记住的原话

> **"OpenAI and Anthropic adding more revenue per month than Meta or Microsoft."**  
> OpenAI 和 Anthropic 月增 revenue 已超过 Meta 或 Microsoft。

> **"Less than five percent diffusion into the economy."**  
> 经济渗透率不到 5%。

> **"I feel pretty confident that we're not in a bubble right now."**  
> 我有信心当前不是泡沫。

> **"We're supply constrained, not demand constrained."**  
> 我们是供给约束，不是需求约束。

> **"You have to be in the token path. That is number one thing."**  
> 必须在 token path 上。这是第一要务。

> **"Everything that is reactive today... going to be a shift to proactive."**  
> 今天 reactive 的东西……会转向 proactive。

> **"The pace of value creation is... happening much faster."**  
> 价值创造节奏……快得多。

> **"Never lost money on a deal... that's horrible, that's not what you want."**  
> 从没在 deal 上亏过钱……那很糟，不是你要的。

> **"Eighty percent said too high... small subset massively undervalued."**  
> 80% 说估值太高……少数 subset 被严重低估。

---

## 小结

**这期最核心的判断：** a16z 认为 AI **不是泡沫**——OpenAI/Anthropic 月增 revenue 已超单家 Meta/Microsoft，但经济渗透率仍 **<5%**；当前是 **supply constrained**，价值创造节奏快于渗透。

**读完应带走：**
- **Token path** 是第一要务；reactive → proactive agent 是产品形态主迁移。
- Skeuomorphic 提效短期 OK，长期要 **AI-native**；first mover ≠ winner，defensibility 动态看。
- VC 哲学：从不亏 deal 可能意味着没押够；80% 说贵 vs 少数 subset 被低估并存。

**和 vault 的关系：** 接 ai_career / 组织横切，与 [[LCA-60分钟变成AI-Native]]、[[MOC - AI 时代个人发展与组织]] 对照宏观与实操。

---

## 行动启示

1. **区分 supply vs demand story**——shortage ≠ bubble；别用 2021 叙事套 2026。
2. **Build on token path**，或 explicit 说明为何不在 path 上仍能 capture value。
3. **Watch model market structure**——竞争数影响 token 价与你的 margin / 客户重构压力。
4. **Native > skeuomorphic long-term**——proactive agent > 聊天提效。
5. **First mover ≠ winner**——AI 50 年换血 40%，defensibility 动态评估。
6. **Enterprise 预算 realism**——Fortune 500 profit pool 是 spend ceiling anchor。
7. **China cost curve**——6mo lag + 10× cheap 是 second frontier 变量。

---

## 相关阅读

- [[MOC - AI 时代个人发展与组织]] — AI 时代职业与组织转型横切索引
- [[LCA-60分钟变成AI-Native]] — native org 实操，与 a16z「公司 run differently」呼应
- [[万人大厂宣布裁员 40% 利润在涨人却多余了]] — 劳动力重构侧影

---

## 来源

- **视频**：[BV1UajG6oEvj](https://www.bilibili.com/video/BV1UajG6oEvj/)（B 站转载 a16z LP 对话）
- **UP主**：Easonlee的AI笔记
- **转写**：Recastory `B3-a16z-ai-bubble/article.md`（英文 ASR，收录时已人工整理叙事）
- **版本**：v2 读者向讲义（2026-07-02）
