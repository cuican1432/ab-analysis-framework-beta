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
  - `[DM] DM Group Chat`
  - `[DM] DM Group Chat by Msg Type`
  - `[DM] DM Group Chat 3d Retention`
  - `[DM] DM Group Chat 7d Retention`
  - `[DM] DM Group Chat 14d Retention`
  - `[DM] DM Group Chat 28d Retention`

### Private Chat

- 含义：一对一私信里的发送、接收、回复、深度和对数相关概念。
- Notes: private-chat concept; keep concrete private-chat metrics in glossary.
- 对应指标组：
  - `DM Core`
  - `DM 2-Way`
  - `DM Message Pairs`
  - `DM by Entrance`
  - `DM by Msg Type`
  - `DM Quality & Reply Rates`
  - `DM Quality & Reply Rates New`
  - `DM Receive`
  - `DM Receive New`
  - `DM Send & Load Fail`
  - `DM Leave Chat`
  - `DM Permission`
  - `DM Negative Feedback`
  - `[DM] DM Core Performance - Android`
  - `[DM] DM Core Performance - iOS`
  - `[DM] DM Core Performance - Latency`

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

- 含义：私信里的分享动作、分享入口、分享类型和分享路径概念。
- Notes: share-action concept; keep share metrics in glossary.
- 对应指标组：
  - `DM Quick Share`
  - `DM_Share_Type | direct message share type`
  - `Quick Share Recall`
  - `Internal Share All`
  - `Internal Share To Chat`
  - `Internal Share Funnel Metrics`
  - `Internal Share Search Funnel Metrics`
  - `DM by Link`

### Repost

- 含义：内容二次传播、转发或 repost 相关的行为概念。
- Notes: redistribution concept; keep concrete repost/share metrics in glossary.
- 对应指标组：
  - `Internal Share All`
  - `Internal Share To Chat`
  - `Internal Share Funnel Metrics`
  - `Internal Share Search Funnel Metrics`

### DM Safety

- 含义：私信里的安全、权限、负反馈、发送失败和负向体验概念。
- Notes: safety / guardrail concept; keep concrete safety metrics in glossary.
- 定位：跨 DM 场景的安全与护栏层，不等同于 B2C Messaging。
- 对应指标组：
  - `DM Permission`
  - `DM Negative Feedback`
  - `TnS DM Private Sender Metrics - Conv Level`
  - `TnS DM Private Sender Metrics - Msg Level`
  - `TnS DM Private Receiver Metrics - Msg Level`
  - `TnS DM Group Chat Sender Metrics - Conv Level`
  - `TnS DM Group Chat Sender Metrics - Msg Level`
  - `TnS DM Group Chat Receiver Metrics - Msg Level`

### DM Experience

- 含义：私信体验层概念，包括回复率、时延、加载体验、转化漏斗和感知质量。
- Notes: experience concept; keep concrete experience metrics in glossary.
- 对应指标组：
  - `DM Quality & Reply Rates`
  - `DM Quality & Reply Rates New`
  - `DM Core`
  - `DM 2-Way`
  - `DM Message Pairs`
  - `DM Conversion Funnel`
  - `DM Send & Load Fail`
  - `DM Leave Chat`
  - `[DM] DM Core Performance - Android`
  - `[DM] DM Core Performance - iOS`
  - `[DM] DM Core Performance - Latency`

---

## Reusable DM Concepts | 可复用 DM 概念

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
