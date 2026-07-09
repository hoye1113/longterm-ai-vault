---
title: "Eric Jang：从零构建 AlphaGo"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV19qLA6BEHx/"
column_url: "https://www.bilibili.com/read/cv49271767/"
host_name: "Dwarkesh Patel"
guest_name: "Eric Jang"
guest_title: "1x Technologies VP · 前 Google DeepMind 高级研究科学家 · AlphaGo 团队"
material_tier: S
ingest_dir: "Recastory/workspace/bilibili-retranscribe/BV19qLA6BEHx/ingest"
speaker: "Dwarkesh / Eric"
duration: "~90:00"
saved: 2026-07-08
created: 2026-07-08
updated: 2026-07-08
description: "Eric Jang 深度拆解如何从零构建 AlphaGo：神经网络将深不可测的游戏树模拟摊销进 10 层网络前向传播，MCTS 作为策略改进器，价值函数截断搜索深度，自我对弈的本质是搜索结果蒸馏，以及为什么 LLM 难以直接复现 AlphaGo 的成功。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV19qLA6BEHx/ingest/column_article.md"
column_source: "Recastory/workspace/bilibili-retranscribe/BV19qLA6BEHx/ingest/column_article.md"
curate_method: "vskill-vault-write canonical-dialogue v3.2"
dialogue_version: v3.2
genre: Host-Guest canonical
speaker_inference: "column Dwarkesh Patel's Podcast"
speaker_confidence: high
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - ai_evaluation
  - ai_coding
concepts:
  - id: amortized_search
    zh: 摊销搜索
    en: amortized search
    one_line: 神经网络前向传播近似极深游戏树模拟
  - id: mcts_improvement
    zh: MCTS 策略改进
    en: MCTS policy improvement
    one_line: 蒙特卡洛树搜索产出比原始网络更精准的动作分布
  - id: value_network
    zh: 价值网络
    en: value network
    one_line: 预测当前棋盘胜率以截断搜索深度
  - id: distillation_loop
    zh: 搜索蒸馏循环
    en: distillation loop
    one_line: MCTS 搜索结果重新作为标签训练策略网络
  - id: bitter_lesson
    zh: 苦涩的教训
    en: bitter lesson
    one_line: 计算能力是决定因素，算法细节终将不重要
  - id: test_time_scaling
    zh: 测试时间缩放
    en: test-time scaling
    one_line: 权衡测试时间计算与训练计算
  - id: nash_equilibrium
    zh: 纳什均衡
    en: Nash equilibrium
    one_line: 完美信息博弈中存在超人类最优策略
author:
  - "[[Eric Jang]]"
---

# Eric Jang：从零构建 AlphaGo

**Host：** Dwarkesh Patel  
**Guest：** Eric Jang（1x Technologies VP · 前 Google DeepMind 高级研究科学家 · AlphaGo 团队）  
**形态：** Host-Guest canonical v3.2（**专栏主源**）  
**B 站：** [BV19qLA6BEHx](https://www.bilibili.com/video/BV19qLA6BEHx/) · **时长** ~90 min

---

## 开场

Eric Jang 在休假期间重建了 AlphaGo。他指出 AlphaGo 的核心价值在于展示了神经网络如何通过少量计算步骤，**摊销并近似极其复杂的搜索问题**——一个 10 层网络通过约 10 步推理，就能捕获一个看似 NP 类问题的宏观结构。这种"模拟压缩"也是 AlphaFold 成功的底层逻辑。

**术语速查**

| 中文 | 英文 | 白话 |
|------|------|------|
| 摊销搜索 | amortized search | 网络前向传播替代穷举树搜索 |
| 蒙特卡洛树搜索 | MCTS | 选择→扩展→评估→回溯四步迭代 |
| 策略网络 | policy network | 预测好走法的概率分布 |
| 价值网络 | value network | 预测当前棋盘胜率（截断搜索深度） |
| PUCT | predicted upper confidence bound for trees | AlphaGo 的动作选择准则 |
| 纳什均衡 | Nash equilibrium | 不被任何策略打败的最优策略 |
| 蒸馏 | distillation | 搜索结果重新作为训练标签 |
| DAgger | dataset aggregation | 模仿学习中的迭代纠正算法 |
| KataGo | KataGo | David Wu 发起的开源围棋 AI（计算量减 40 倍） |

---

## 01 AlphaGo 的运作原理与围棋基础

**Eric：** 围棋规则极简：黑白棋子争夺地盘，包围对手棋子的四个邻居即可提子。Trump Taylor 规则使围棋完全明确，所有 AI 训练都基于此。游戏复杂度约为 361 的 300 次方——远超宇宙原子数。

**Dwarkesh：** 所以计算机科学家多年来认为围棋不可解？

**Eric：** 对。穷尽搜索所需计算量太大。但 AlphaGo 的核心突破是**用神经网络使搜索问题变得可行**。两个问题：树的广度（361 种走法）和深度（300 步）。AlphaGo 同时解决两者。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 组合爆炸 | combinatorial explosion | 361^300 种可能棋局 |
| 分支因子 | branching factor | 每步可选走法数 |
| 子节点合并 | transposition | 不同路径到达同一棋盘状态 |

**小结：** 围棋复杂度使穷举不可行，但存在可压缩的宏观结构。

---

## 02 MCTS：四步迭代搜索

**Eric：** MCTS 每步执行四个步骤：**选择**（用 PUCT 准则找最佳子节点）、**扩展**（添加新叶子）、**评估**（用价值网络猜胜负）、**回溯**（更新祖先节点的 Q 值）。

选择准则 PUCT = Q(S,A) + C·P(A)·√N/(1+N_A)。最初所有访问计数为零，选择偏向策略概率最高的节点；随模拟增加，由 Q 值（利用项）主导。

**Dwarkesh：** MCTS 的每一步都会重新实例化树？

**Eric：** 基本是。每步从新根开始搜索，但会保留一些信息供后续使用。模拟次数通常 200~2048；AlphaGo Lee 每步用数万次，因为想最大化模型强度。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 选择 | selection | 沿 PUCT 最高路径向下 |
| 扩展 | expansion | 添加新叶子节点 |
| 评估 | evaluation | 价值网络快速猜胜负 |
| 回溯 | backup | 更新祖先节点 Q 值 |

**小结：** MCTS 是稀疏搜索——只探索被扩展的路径，远小于穷举树。

---

## 03 价值函数：截断搜索深度的关键

**Eric：** 人类棋手一眼判断胜负，是因为脑中存在隐式价值函数——扫描棋盘后隐式地摊销大量可能对局，取平均值决定是否继续。AlphaGo 的价值网络做同样的事：**输入棋盘状态，输出胜率，替代玩到终局的模拟**。

**Dwarkesh：** 价值函数为什么既可训练又必要？

**Eric：** 开局时胜率收敛到 0.5，随步数增加逐渐分化。残局时价值估计极准，因为不确定性随树深度增加而降低。关键洞察：我们真正关心的是宏观结构（谁赢），而非微观路径（具体怎么下）。这与混沌系统类似——围棋棋盘对初始条件极其敏感，但宏观胜率可预测。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 价值函数 | value function | 棋盘→胜率的映射 |
| 截断深度 | depth truncation | 不必下到终局即可评估 |
| 混沌系统 | chaotic system | 微小扰动改变微观路径但不改变宏观结构 |

**小结：** 价值网络将 300 步的深度搜索压缩为一步前向传播。

---

## 04 策略网络与架构选择

**Eric：** 策略网络产生好走法的概率分布，与价值网络共享表示层。两者都是分类问题，用交叉熵损失训练。架构上 ResNet 在低预算下比 Transformer 性价比更高——Conv 提供局部归纳偏置，Transformer 需要更多数据学习全局注意力。

KataGo 的关键发现：**全局特征聚合**对棋盘两侧价值连接非常重要。卷积的感受野擅长局部特征，但难以连接远距离特征。

**Dwarkesh：** 完美信息博弈只需要当前状态来决策？

**Eric：** 围棋是完美信息博弈，存在纳什均衡策略——完全由当前状态决定，不输任何其他策略。不完美信息博弈（如 2v2 围棋）则需要历史上下文。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 归纳偏置 | inductive bias | ResNet 局部性 vs Transformer 全局注意力 |
| 全局特征聚合 | global feature pooling | 跨棋盘连接信息 |
| 完美信息博弈 | perfect information game | 所有状态对双方可见 |

**小结：** ResNet 仍是低预算围棋的最优选择；架构不是决定因素。

---

## 05 自我对弈：搜索结果的蒸馏

**Eric：** AlphaGo 的强化学习本质是**蒸馏**：MCTS 耗费大量计算得出搜索结果，重新作为标签训练策略网络。训练后的网络前向传播直接给出接近搜索后的判断，实现**测试时间计算量向训练时间计算量的转化**。

**Dwarkesh：** 这与 LLM 的策略梯度有什么区别？

**Eric：** LLM 的策略梯度是"通过吸管吸取监督"——展开整个轨迹才能获得学习信号，方差极高。MCTS 对每个动作都有监督目标，信号方差极低。AlphaGo 永远不必从 0% 成功率开始——MCTS 总能提供比当前策略更好的标签，这就是爬坡的监督学习信号。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 蒸馏 | distillation | 搜索分布→策略标签 |
| 软标签 | soft labels | MCTS 分布比 one-hot 信息量更大 |
| 在策略 vs 离策略 | on-policy vs off-policy | AlphaGo 大部分在策略训练 |
| DAgger | dataset aggregation | 即使偏离最优轨迹也有纠正标签 |

**小结：** 蒸馏循环是 AlphaGo 训练的核心——每步都把搜索结果压缩进网络。

---

## 06 为什么 LLM 难以复现 AlphaGo 的成功

**Eric：** 围棋有明确规则、有限离散动作空间、可判定终局——MCTS 能提供极低方差的监督信号。语言空间广度太大，缺乏局部可验证的价值函数，LLM 很难像围棋 AI 那样通过局部搜索实现每步自我迭代。

**Dwarkesh：** LLM 不是天生就会做 MCTS 吗？会回溯、换方法？

**Eric：** 表面类似，但 LLM 没法在不实际解决问题的情况下局部评估和改进下一步行动。LLM 的 token 空间太大，PUCT 的探索启发式可能不是指导搜索的正确方法。不过，前向搜索和模拟的思想可能会卷土重来。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 动作空间 | action space | 围棋 361 vs LLM 10 万+ |
| 局部可验证 | locally verifiable | 围棋每步可评估，LLM 不能 |
| 信用分配 | credit assignment | 长轨迹中哪步该负责 |

**小结：** 围棋的结构特性使 MCTS 蒸馏高效；LLM 缺少等价的局部验证机制。

---

## 07 测试时间缩放与苦涩的教训

**Eric：** Andy Jones 的论文表明可以权衡测试时间计算和训练计算——更多 MCTS 模拟 = 更少训练计算。这正是后来 LLM 推理时间缩放的原型。

**Dwarkesh：** AlphaGo Zero 曾是计算量最大的 AI 模型（约 3E23 FLOPs）。

**Eric：** 我花了约 1 万美元（Prime Intellect 捐赠 + 自费）就重建了接近水平。LLM 编码使 DeepMind 整个团队数百万美元的研究现在只需几千美元。苦涩的教训意味着**架构选择不重要，计算能力是决定因素**——GPU 变快后，Katago 的许多技巧变得不那么必要。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 苦涩的教训 | bitter lesson | 计算量终将压倒算法技巧 |
| 计算最优 | compute-optimal | 给定预算下最大化性能 |
| 跨棋盘迁移 | cross-board transfer | 9×9 预训练迁移到 19×19 |

**小结：** 现代硬件使重建 AlphaGo 变得平价；苦涩的教训持续应验。

---

## 08 自动化科学研究的瓶颈

**Eric：** LLM 自动化 AI 研究在超参数优化和实验执行上卓越，但**退后一步审视方向是否错误**时乏力。当前模型在给定轨道上选下一个实验不擅长，缺乏横向思维——无法回到第一性原理判断轨道是否有意义。

围棋可作为自动化科学家的训练环境：外层循环（胜率验证）极快，内层循环（研究工程）可并行。掌握后可迁移到生物科学、机器人等领域。

**Dwarkesh：** 你怎么看并行代理？

**Eric：** 局部改进的可堆叠性有限——两个好想法可能互相干扰。苦涩的教训要求你知道计算能带来多少，以及何时要求过多。许多计算乘数的益处短暂，GPU 变强后它们的价值递减。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 横向思维 | lateral thinking | 跳出当前轨道审视方向 |
| 外层循环 | outer loop | 胜率 / 可验证结果 |
| 内层循环 | inner loop | 实验执行与调参 |

**小结：** 自动化研究的瓶颈是横向思维；围棋是理想的快速验证沙箱。

---

## 09 深度学习与混沌的哲学

**Eric：** 一个 10 层网络通过约 10 步推理，能摊销几乎难以处理的搜索问题——这是深刻成就。AlphaFold 也是同理：相对较小的网络 10 步就能捕捉 NP 类问题的宏观结构。这让我怀疑我们对 P=NP 的理解是否完整。

**Dwarkesh：** 天气预测也有类似的混沌结构——微观路径不可预测，但宏观结构（飓风在哪里）可预测。

**Eric：** 围棋也是。一颗棋子可能扰乱整个预测（混沌），但我们真正关心的是宏观胜率（可预测）。密码学的哈希函数依赖初始条件但没有宏观结构——所以无法快速近似。混沌边缘的系统有可预测的宏观模式。

**本章概念**

| 中文 | 英文 | 白话 |
|------|------|------|
| 混沌边缘 | edge of chaos | 有序与混乱之间的可预测区域 |
| 宏观结构 | macro structure | 胜率 vs 具体棋局 |
| NP 难 | NP-hard | 最坏情况难，但实际可近似 |

**小结：** AlphaGo 暗示：混沌系统中宏观量可被神经网络压缩学习。

---

## 总结

| 维度 | 要点 |
|------|------|
| 核心洞察 | 10 层网络摊销 300 步搜索 |
| MCTS | 四步迭代搜索 + PUCT 选择 |
| 价值网络 | 截断深度的关键 |
| 自我对弈 | 搜索结果蒸馏为策略标签 |
| LLM 差异 | 缺局部可验证价值函数 |
| 自动化研究 | 横向思维是瓶颈 |
| 苦涩的教训 | 计算力终将压倒算法技巧 |
| 混沌哲学 | 宏观结构可压缩学习 |

---

## 附录

### 章节时间戳（视频简介）

| 时间 | 主题 |
|------|------|
| 05:12 | 围棋决策的本质是深度搜索的摊销 |
| 18:45 | MCTS 是神经网络直觉的改进算子 |
| 25:30 | 价值函数是截断搜索深度的关键 |
| 45:12 | 自我对弈的本质是搜索结果的蒸馏 |
| 65:20 | 为什么 LLM 难以直接复现 AlphaGo 的成功 |
| 82:15 | 自动化科学研究的瓶颈在于横向思维 |

### Ingest

- BV：`BV19qLA6BEHx`
- ingest：`Recastory/workspace/bilibili-retranscribe/BV19qLA6BEHx/ingest`
- 专栏：`.../ingest/column_article.md`

### 相关阅读

- [[杨立昆-世界模型才是未来]] — 混沌系统与世界模型对照
- [[DeepMind研究员-递归循环中AI构建AI]] — RSI 与自我改进
- [[OpenAI首席科学家-超越代码的强化学习]] — RL 理论对照
- [[Karpathy-从Vibe Code到Agentic Code]] — LLM 自动化研究
- [[MOC - Harness Engineering]] — 搜索与推理 harness
- [[MOC - Agent Theory and Design]] — 入口
