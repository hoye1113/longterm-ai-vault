---
title: "OpenClaw实战：从本地到K8S部署"
source: "B站视频 - Easonlee的AI笔记"
source_url: "https://www.bilibili.com/video/BV18LV66aEG9/"
speaker: "Sally（Red Hat，10 年容器/Linux/K8s 安全）"
duration: "21:46"
saved: 2026-07-02
tags:
  - ai_agent
  - video_transcript
  - bilibili
  - harness_engineering
  - skills
  - mcp
created: 2026-06-09
description: "Red Hat 工程师 Sally 用容器跑 OpenClaw：反驳「安全噩梦」、四好处（可重现/隔离密钥/便携/备份）、Podman Secrets、团队 baseline 镜像愿景。"
transcript_source: "Recastory/workspace/bilibili-retranscribe/BV18LV66aEG9/article.md"
asr_version: v2
curate_method: "vskill-vault-curate（读者向讲义 v2）"
---

# OpenClaw 实战：从本地到 K8S 部署

## 先搞懂这一期

**这是什么节目？**  
Red Hat 工程师 **Sally** 在 meetup 上的 **~22 分钟分享 + 现场 demo**。主题：用 **Podman/Docker/K8s/OpenShift** 跑 OpenClaw，以及为什么容器党认为「AI Agent 安全噩梦」反而是机会。

**这期在回答哪三个问题？**

1. **OpenClaw 装工作笔记本真的「安全噩梦」吗？** 容器/Linux 安全老兵怎么看？  
2. **为什么 Agent 应该跑在容器里？** 比「本机 npm install」强在哪？  
3. **从本地一个命令到 K8s 集群，路径长吗？** 现场 spin up 要几秒？

**用一条线串起来（没看视频也能复述）：**

Sally 背景：Red Hat 10 年，前 7 年 **容器 + Linux 安全 + OpenShift**，后转 emerging tech / AI。  
休假试 OpenClaw → 回公司 Slack 被喊 **security nightmare** → 反驳：**我们 10 年干的就是把任意应用安全跑起来**。  
她的 **ForeverClaw Shira** + 两个 sub-agent（Joy 占星、Bruno Bruins 季后赛简报）——问 Shira「为啥跑容器」，得到四词：**reproducible、isolate secrets、portable、backup**。  
容器还能 **mount 整个 agent 目录**（tools/skills/MCP）一次启动；**Podman Secrets → OpenClaw secret ref 双层指针**，日志里不见明文 key。  
愿景：AI workload 会像普通 app 一样 **local dev → lift to K8s**；NVDIA 10 个工程师各跑 K8s OpenClaw 做 model eval，**≈6 人工作量**。  
职场 OpenClaw：**公司 baseline 镜像**（批准 MCP、auth、团队 skills）fan-out 给新人，再个性化。  
Demo：自研 installer，`npm run dev` 式 **一条命令** spin Podman 实例（Joe），配 OpenRouter/Gemma、Anthropic fallback、可选 OTel；同一套 **Kind/OpenShift** 上跑 Carl。

---

## 背景：这期在 AI Agent 大图里的位置

| 你可能已有的认识 | 这期补上的那一块 |
|----------------|-----------------|
| OpenClaw = Mac mini 个人助理 | **生产级容器/K8s 部署**与团队 baseline |
| Agent 安全 = 别装 | **隔离密钥 + sandbox + 显式 host 权限** 的工程路径 |
| K8s 跑传统微服务 | **ForeverClaw + PVC +  nightly backup** 同样适用 |
| 写代码还是工程师主业 | Sally：**几个月没手写 code**，AI 写得更好了 |

---

## 分话题讲

### 1. 「安全噩梦」vs 金色机会

**说法：**  
同事：别装工作本。Sally：Red Hat 10 年 **REL**——**任何应用都能安全跑**；OpenClaw 是向全公司证明的 **golden opportunity**。

**和你何干：**  
会容器/K8s 的人，Agent 时代 **技能更值钱**——不是回避，是 **硬化部署**。

---

### 2. 容器四好处（ForeverClaw 版）

**说法：**

| 好处 | 含义 |
|------|------|
| **Reproducible** | 镜像一致，环境不漂 |
| **Isolate secrets** | API key 不进主机明文 |
| **Portable** | laptop / x86 / Mac / K8s 同一故事 |
| **Backup/Recovery** | Volume + 每晚 systemd 备份 |

**说法补：**  
容器 = **天然 sandbox**；给 host 什么权限要 **显式声明**。Sally：**本机原生跑东西很 messy**，她一切都 containerize。

**和你何干：**  
个人 ForeverClaw 也应用 **volume + 定时备份**——Agent 状态是资产。

---

### 3. Secrets：Podman + OpenClaw 双层 ref

**说法：**  
- **Podman Secrets**：key 存系统 secret，容器里只是 **ref**  
- **OpenClaw secret ref**：容器内再一层指针  
- 不完美，但 **日志里不刷明文 API key**

K8s 侧同理：**Secret ref → env**，不是裸 env 字符串。

**和你何干：**  
部署 OpenClaw 时 **两层 secret  indirection** 值得抄。

---

### 4. Mount agent 目录：skills/MCP 一次就绪

**说法：**  
把整个 **agent 目录**（tools、skills、MCP servers）mount 进容器，启动即就绪——不用每次手工装插件。

**和你何干：**  
团队 baseline 镜像 = **curated 目录 + mount**，新人 clone 即用。

---

### 5. AI 改变工程师分工（不是全员失业）

**说法：**  
NVDIA 朋友：10 工程师各跑 K8s OpenClaw 盯 model eval，**像 6 个人的活**。  
Sally：**几个月没写 code**；org meeting 宣布「不用 AI 写代码是 missing out」——顶级工程师 **挑眉**，但她坚持 AI **1000x  better at writing code**。  
结果：团队做 **outside the box、creative** 的事， tedious code 交给 AI。

**和你何干：**  
Leverage 在 **设计/运维 Agent 工厂**，不在手写 CRUD。

---

### 6. 职场愿景：baseline + 个性化

**说法：**  
新员工入职 → 拿到 **公司批准版 OpenClaw**：  
- 批准 MCP 列表  
- 公司 auth  
- 团队 skills（Google Drive 等）  
→ **fan-out 全团队**，个人再定制。  
对比：坐同事旁边 copy repo 自己拼。

**和你何干：**  
企业 Agent 落地先定 **golden image**，再谈个人 sub-agent（Joy/Bruno 模式）。

---

### 7. Demo：一条命令 spin 实例

**说法：**  
自研 installer（GitHub 开源，Sally 自用）：  
- 给 pod 取名、 bump port（8899）  
- **Podman secret mappings** 自动转 OpenClaw secret ref  
- 选 provider：OpenRouter（Gemma）、Anthropic fallback、本地 endpoint  
- 可选 **OpenTelemetry + Jaeger**  
- **SSH sandbox**：OpenClaw 在远程 workspace 跑命令  
- 现场 **2 秒** 起 Joe；K8s 上 Carl、OpenShift 可切换

**Mac 坑：** 容器里 spawn 容器在 Mac 上难（VM 套 VM）；Linux 可以。

**和你何干：**  
「OpenClaw 难装」——** opinionated installer** 可压到秒级；Docker 友称在测。

---

## 关键概念（读完应能解释）

| 词 | 白话 |
|----|------|
| **ForeverClaw** | 长期运行的个人 OpenClaw 实例（Sally 的叫 Shira） |
| **Sub-agent** | 专责子任务（Joy 占星、Bruno 体育） |
| **Podman Secrets** | 密钥与容器解耦的存储/挂载 |
| **OpenClaw secret ref** | 配置里指向外部 secret 的指针 |
| **PVC / Volume** | Agent 运行时状态持久化 |
| **Baseline 镜像** | 公司批准 MCP/skills/auth 的标准 OpenClaw |
| **SSH sandbox** | Agent 在指定远程 workspace 执行命令 |

---

## 值得记住的原话

> **"It's a security nightmare, do not use OpenClaw." / "What have I been doing the past 10 years?"**  
> 「安全噩梦别装」/「我过去 10 年干的就是这个？」

> **"If we can't take an application and run it securely, come on. This is our golden opportunity."**  
> 不能让应用安全跑起来，还叫什么。这是金色机会。

> **"Reproducible... isolate your secrets... portable... backup and recovery."**  
> 可重现、隔离密钥、便携、备份恢复。

> **"I run everything in containers... natively is messy."**  
> 我什么都跑容器；本机原生很乱。

> **"Doing the job of six engineers"**（NVDIA model eval 团队）  
> 像六个工程师的活（10 人各跑 OpenClaw）。

> **"If you're not using AI for everything, you're missing out."**  
> 不用 AI 搞定一切，你在错过。

> **"Spin up OpenClaw... took two seconds."**  
> 起 OpenClaw 两秒（边讲边 demo）。

---

## 小结

**这期最核心的判断：** OpenClaw 的「安全噩梦」叙事，对 **会容器化的人** 是机会——**reproducible + secret 隔离 + volume 备份 + K8s 规模化**，和跑任何 enterprise app 同一套；个人 ForeverClaw 与职场 baseline 镜像 **同一技术栈**。

**读完应带走：**
- 四词：**可重现、密钥隔离、便携、可备份**——Agent 更该容器化，不是更该裸奔本机。  
- **Podman/K8s Secret + OpenClaw secret ref** 双层，减日志泄密。  
- **公司 baseline OpenClaw → fan-out → 个性化**，是可落地的 onboarding 模型。

**和 vault 的关系：** OpenClaw 部署线，接 [[30分钟精通OpenClaw]]、[[PlanetScale-Agent时代的基础设施]]、[[IBM团队-Harness工程详解]]。

---

## 行动启示

1. **Personal OpenClaw 上 Podman/Docker + volume**，每晚备份 state。  
2. **API key 走 secret ref**，别写进 config 明文。  
3. **skills/MCP 目录 mount 进容器**，重建环境零手工。  
4. **local Podman → Kind/OpenShift** 同一 installer 故事，先 dev 后 prod。  
5. **团队定 golden image**：批准 MCP、auth、共享 skills，再允许 sub-agent 个性化。  
6. **Mac 用户**：接受「容器套容器」限制，或 dedicated Linux/Mac mini 宿主机。

---

## 相关阅读

- [[30分钟精通OpenClaw]] — 个人助理安全设置与用例  
- [[OpenClaw创始人-我是如何使用OpenClaw的？]] — 创始人用法  
- [[Taven创始人-将OpenClaw嵌入产品的实战经验]] — Pi/OpenClaw 企业嵌入  
- [[PlanetScale-Agent时代的基础设施]] — Agent 时代基础设施观  
- [[IBM团队-Harness工程详解]] — harness 与可靠性  

---

## 来源

- **视频**：[BV18LV66aEG9](https://www.bilibili.com/video/BV18LV66aEG9/)（B 站 *Easonlee的AI笔记*）  
- **讲者**：Sally，Red Hat（容器/Linux/K8s 安全）  
- **时长**：~21:46  
- **转写**：Recastory `bilibili-retranscribe/BV18LV66aEG9/`（FunASR SenseVoice + cam++，**asr v2** 14 段）  
- **版本**：v2 读者向讲义（2026-07-02）
