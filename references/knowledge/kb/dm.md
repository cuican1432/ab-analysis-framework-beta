# Business Knowledge Topic: TikTok - Social - DM | 业务知识主题：TikTok - Social - DM

这个文件是 `kb/` 里的一个正式知识主题页。  
This file is one formal topic page inside `kb/`.

如果你要先看 KB 总览，请先看：
- `references/knowledge/kb/index.md`

TikTok - Social business KB is split into four sub-domain pages:
- Core Interaction
- DM
- Story
- UR

This page is the DM layer for reusable DM-specific knowledge.

If you need support-documented messaging and adjacent distribution rules that complement this DM knowledge page, such as DM permissions, request flow, read status, streaks, safety controls, inbox/push notifications, or share/repost behavior, also read:
- `references/knowledge/kb/messaging_support.md`

## What Belongs Here

- DM subdomain concepts,
- DM interaction patterns,
- DM safety / experience concepts,
- DM-specific user behavior slices,
- DM-specific product mechanisms,
- reusable DM reading hints.

## What Does Not Belong Here

- experiment-local conclusions,
- one-off report claims,
- metric rows that belong in glossary,
- copied final outputs from a single experiment.

---

## DM Subdomains | DM 子方向

### Core DM

- 含义：默认覆盖 DM 主链路、且不应被直接缩写成“只看私聊”的核心层概念。
- Notes: DM-wide core concept; use the source table or raw data to decide whether a specific case is private-chat only, group-chat only, or cross-surface.
- 对应指标组：
  - `DM Core`
  - `Key Project-DM`
  - `[DM] DM Receive`
  - `[DM] DM Receive New`
  - `[DM] DM by Entrance`
  - `[DM] DM by Msg Type`

### Streaks

- 含义：私信里的连续互动、连续使用和 streak 相关概念。
- Notes: continuity / recurrence concept; keep concrete streak metrics in glossary.
- 对应指标组：
  - `[DM] DM Streak`

### Stickers

- 含义：私信里的 sticker 相关概念，包括 sticker panel、sticker sending 和 sticker path usage。
- Notes: sticker-format concept; keep concrete sticker metrics in glossary.
- 对应指标组：
  - `[DM] DM Sticker`

### Group Chat

- 含义：群聊里的创建、进入、发送、接收、留存和消息类型相关概念。
- Notes: group-chat concept; keep group-chat metrics in glossary.
- 对应指标组：
  - `DM Group Chat`
  - `[DM] DM Group Chat by Msg Type`
  - `[DM] DM Group Chat 3d Retention`
  - `[DM] DM Group Chat 7d Retention`
  - `[DM] DM Group Chat 14d Retention`
  - `[DM] DM Group Chat 28d Retention`

### Private Chat

- 含义：一对一私信里更明确依赖 pair、MUF 或关系对结构的概念。
- Notes: private-chat concept; use this bucket only when the group is explicitly private-chat, MUF-based, or pair-based.
- 对应指标组：
  - `[DM] DM Message Pairs`
  - `DM Growth Pairs-Key Metrics`
  - `DM Growth Pairs-Active Days`
  - `DM Growth Pairs- Retention`
  - `Muf Growth DM Pairs By time`
  - `[DM] MuF DM Lifecycle`
  - `[DM] MuF DM by Motivation`
  - `[DM] Muf DM Enter From as Dim`
  - `[DM] Muf DM Msg Type as Dim`

### Two-Way

- 含义：私信里的双向互动、回复质量和对话往返强度相关概念。
- Notes: two-way interaction concept; use this bucket for reciprocal interaction and reply-quality layers across DM surfaces.
- 对应指标组：
  - `[DM] DM 2-Way`
  - `[DM] DM Quality & Reply Rates`
  - `[DM] DM Quality & Reply Rates New`

### B2C Messaging

- 含义：面向创作者或商家的消息体系概念，包括 creator messaging 和 business messaging。
- Notes: B2C messaging concept; keep concrete B2C metrics in glossary.
- 对应子方向：
  - Creators Messaging
  - Business Messaging
- 对应指标组：
  - `[B2C] Business Message Key Metrics`
  - `[B2C] Creator Message Key Metrics`

### Creators Messaging

- 含义：面向创作者的消息体系概念。
- Notes: creator-facing messaging concept; keep concrete creator metrics in glossary.
- 定位：B2C Messaging 的 creator-facing 分支。
- 对应指标组：
  - `[B2C] Creator Message Key Metrics`

### Business Messaging

- 含义：面向商家的消息体系概念。
- Notes: business-facing messaging concept; keep concrete business metrics in glossary.
- 定位：B2C Messaging 的 business-facing 分支。
- 对应指标组：
  - `[B2C] Business Message Key Metrics`

### Share

- 含义：与私信强相关的分享动作、分享入口、分享类型和分享路径概念，既包括私信内分享，也包括与 DM 收件链路直接相邻的 internal share surfaces。
- Notes: share-action concept; keep concrete share metrics in glossary, and use `messaging_support.md` for official platform-level sharing mechanics.
- 对应指标组：
  - `DM Quick Share`
  - `DM_Share_Type | direct message share type`
  - `Quick Share Recall | Quick Share Recall`
  - `Internal Share All`
  - `Internal Share To Chat`
  - `internal share funnel metrics`
  - `internal share search funnel metrics`
  - `[DM] DM by Link`

### Repost

- 含义：与私信分享链路相邻、但不等同于私信本身的二次传播或 repost 行为概念。
- Notes: adjacent redistribution concept; treat it as neighboring context for DM/share analysis rather than a core DM mechanic. At the moment, no dedicated repost metric group is formalized in the glossary.
- 当前状态：
  - use adjacent share groups as context when repost behavior may influence DM/share interpretation
  - do not relabel broad share groups as repost-specific groups unless the source explicitly does so

### DM Safety

- 含义：私信里的安全、权限、负反馈和治理相关概念。
- Notes: safety / guardrail concept; keep concrete safety metrics in glossary.
- 定位：跨 DM 场景的安全与护栏层，不等同于 B2C Messaging。
- 对应指标组：
  - `[DM] DM Permission`
  - `[DM] DM Negative Feedback`
  - `TnS DM Private Sender Metrics - Conv Level`
  - `TnS DM Private Sender Metrics - Msg Level`
  - `TnS DM Private Receiver Metrics - Msg Level`
  - `TnS DM Group Chat Sender Metrics - Conv Level`
  - `TnS DM Group Chat Sender Metrics - Msg Level`
  - `TnS DM Group Chat Receiver Metrics - Msg Level`

### DM Experience

- 含义：私信体验层概念，包括回复率、时延、加载体验和感知质量。
- Notes: experience concept; keep concrete experience metrics in glossary.
- 对应指标组：
  - `[DM] DM Send & Load Fail`
  - `[DM] DM Leave Chat`
  - `[DM] DM Core Performance - Android`
  - `[DM] DM Core Performance - iOS`
  - `[DM] DM Core Performance - Latency`

### Funnel

- 含义：私信链路里的进入、转化、下游动作衔接等漏斗相关概念。
- Notes: funnel concept; keep concrete funnel metrics in glossary.
- 对应指标组：
  - `[DM] DM Conversion Funnel`

---

## Reusable DM Concepts | 可复用 DM 概念

### Support-Documented DM Rules

- For support-documented DM mechanics such as direct-message permissions, request flow, read status, safety controls, and Business / Organization Account inbox differences, use:
  - `references/knowledge/kb/messaging_support.md`
- Keep this `dm.md` page focused on DM subdomains, reusable DM concepts, and how DM-related metric groups should be interpreted.

### Sticker-related Terms To Keep Separate

These terms should stay separate instead of being merged into one generic `Sticker` entry:

- `Big-moji`
- `UGC sticker`
- `Sticker panel`

Their detailed definitions can remain in `drafts/` until fully confirmed.

### Private-message subdirection data assets

- 中文：私信子方向数据资产
- 英文：Private-message subdirection data assets
- 含义：私信子方向的数据资产总览页，通常按业务简介、核心资产、埋点与公共层、子方向核心资产来组织。
- Notes: page-level concept; useful for reading the DM domain map, not for metric recall.

### Reply rate

- 中文：回复率
- 英文：Reply rate
- 含义：衡量消息被回复的比例或效率的通用概念。
- Notes: generic engagement concept; keep specific reply-rate metrics in glossary.

### Depth vs pair count

- 中文：深度 vs 对数
- 英文：Depth vs pair count
- 含义：用于区分“深度”口径和“对数”口径的通用解释；在私信语境里，深度通常更偏 PV / 次数口径，对数通常更偏 pair 口径。
- Notes: interpretation concept; useful for reading sibling metrics and avoiding口径混淆.

### DM by Entrance

- 含义：按私信入口来源切分的行为概念。
- Notes: slice concept; keep concrete metrics in glossary.

### DM by Msg Type

- 含义：按私信消息类型切分的行为概念。
- Notes: slice concept; keep concrete metrics in glossary.

### DM by Motivation

- 含义：按私信动机切分的行为概念。
- Notes: slice concept; keep concrete metrics in glossary.

### DM 2-Way

- 含义：双向互动的私信分析概念。
- Notes: interaction-balance concept; keep concrete metrics in glossary.

### DM Message Pairs

- 含义：围绕 pair 维度组织的私信分析概念。
- Notes: pair-based interaction concept; keep concrete metrics in glossary.

---

## DM Reading Hint | 使用提示

- 先看 DM 子方向，再看具体机制概念。
- 需要具体指标时，去 `references/knowledge/glossary`。
- 不要把 case-specific 结论写进这里。
