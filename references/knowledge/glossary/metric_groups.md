# Metric Group Index | 指标组索引

## Entry

```yaml
group_name: DM Core
group_aliases:
  - 私信核心指标组

description_zh: 私信核心使用行为指标组，通常用于观察进入会话、停留、发送等主链路行为。
description_en: A core DM usage metric group that usually covers entering chat, staying, and sending behaviors.

usage_scope: social / DM / direct message
is_company_core: false
is_business_core: false
is_sub_business_core: true

priority_hint: P0

common_dimensions:
  - By Entrance
  - By Msg Type
  - By Motivation

notes:
```

## Entry

```yaml
group_name: DM Voice Message
group_aliases:
  - 私信语音指标组

description_zh: 私信语音消息相关指标组，通常用于观察语音录制、取消、发送等行为。
description_en: A DM voice-message metric group that usually covers recording, canceling, and sending voice messages.

usage_scope: social / DM / voice message
is_company_core: false
is_business_core: false
is_sub_business_core: false

priority_hint: P1

common_dimensions:
  - By Msg Type

notes:
```

## Entry

```yaml
group_name: [DM] DM Camera
group_aliases:
  - DM Camera
  - Camera Message / DM Camera

description_zh: 私信相机消息相关指标组，用于观察 DM Camera 的发送、上传、拍摄页进入等链路表现。
description_en: A DM camera-message metric group used to observe sending, upload, and shoot-page entry behaviors for DM Camera.

usage_scope: social / DM / camera
is_company_core: false
is_business_core: false
is_sub_business_core: false

priority_hint: P1

common_dimensions:

notes: Confirmed in the shared formal glossary as a reusable DM camera group.
```

## Entry

```yaml
group_name: [DM] DM Camera by Entrance
group_aliases:
  - DM Camera by Entrance
  - Camera by Entrance

description_zh: 私信相机按入口切分的指标组，用于观察不同入口来源下的相机链路表现。
description_en: A DM camera metric group split by entrance source, used to observe camera-path behaviors by entrance source.

usage_scope: social / DM / camera
is_company_core: false
is_business_core: false
is_sub_business_core: false

priority_hint: P2

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Camera Private Chat
group_aliases:
  - DM Camera Private Chat
  - Camera Private Chat

description_zh: 私信相机私聊指标组，用于观察私聊场景下的相机链路表现。
description_en: A DM camera metric group for private-chat scenarios, used to observe camera-path behaviors in private chat.

usage_scope: social / DM / camera
is_company_core: false
is_business_core: false
is_sub_business_core: false

priority_hint: P2

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Camera Private Chat by Entrance
group_aliases:
  - DM Camera Private Chat by Entrance
  - Camera Private Chat by Entrance

description_zh: 私信相机私聊按入口切分的指标组，用于观察私聊场景下不同入口的相机链路表现。
description_en: A DM camera metric group for private-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a private-chat camera supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Camera Group Chat
group_aliases:
  - DM Camera Group Chat
  - Camera Group Chat

description_zh: 私信相机群聊指标组，用于观察群聊场景下的相机链路表现。
description_en: A DM camera metric group for group-chat scenarios, used to observe camera-path behaviors in group chat.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a group-chat camera supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Camera Group Chat by Entrance
group_aliases:
  - DM Camera Group Chat by Entrance
  - Camera Group Chat by Entrance

description_zh: 私信相机群聊按入口切分的指标组，用于观察群聊场景下不同入口的相机链路表现。
description_en: A DM camera metric group for group-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a group-chat camera supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: DM Group Chat
group_aliases:
  - 私信群聊指标组

description_zh: 私信群聊相关指标组，通常用于观察群聊进入、发送、互动与创建行为。
description_en: A DM group-chat metric group that usually covers entering, sending, interacting, and creating group chats.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used when a DM experiment may spill over into group-chat behavior
priority_hint: P1

common_dimensions:
  - By Entrance
  - By Motivation
  - By Msg Type

notes:
```

## Entry

```yaml
group_name: [DM] DM Receive
group_aliases:
  - DM Receive
  - Receive

description_zh: 私信接收侧指标组，用于观察接收消息、被动互动、接收链路相关表现。
description_en: A DM receive-side metric group used to observe received-message and receive-side interaction behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a receive-side supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Permission
group_aliases:
  - DM Permission
  - Permission

description_zh: 私信权限与陌生人消息机制指标组，用于理解谁可发起请求、消息请求权限等安全机制。
description_en: A DM permission and stranger-message metric group used to understand request permissions and safety mechanisms.

usage_scope: DM / safety or privacy experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a safety / privacy supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the shared formal glossary and live Libra group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Send & Load Fail
group_aliases:
  - DM Send Load Fail
  - Send Load Fail

description_zh: 私信发送与加载失败指标组，用于观察发送失败、加载失败及相关体验风险。
description_en: A DM send-and-load-failure metric group used to observe send failures, load failures, and related experience risks.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a failure / risk supporting group in DM experiments
priority_hint: P0

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Leave Chat
group_aliases:
  - DM Leave
  - Leave Chat

description_zh: 私信离开会话相关指标组，用于观察用户退出聊天链路的行为表现。
description_en: A DM leave-chat metric group used to observe chat-exit behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting risk or engagement group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Core Performance - Latency
group_aliases:
  - DM Core Performance Latency
  - Core Performance Latency

description_zh: 私信核心性能延迟相关指标组，用于记录更泛化的延迟口径正式指标。
description_en: A DM core-performance latency metric group used to store formal latency metrics under the DM core-performance umbrella.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a performance-supporting group in DM experiments
priority_hint: P0

common_dimensions:
  - By Msg Type

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Inner Push
group_aliases:
  - DM Inner Push
  - Inner Push

description_zh: 私信站内推送相关指标组，用于观察站内触达、提醒与召回链路表现。
description_en: A DM in-app push metric group used to observe in-app reach, reminder, and recall behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting reach/retention group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Outer Push
group_aliases:
  - DM Outer Push
  - Outer Push

description_zh: 私信站外推送相关指标组，用于观察站外触达、召回与回流链路表现。
description_en: A DM out-of-app push metric group used to observe off-app reach, recall, and re-entry behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting reach/retention group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Sticker
group_aliases:
  - DM Sticker
  - Sticker

description_zh: 私信贴纸消息相关指标组，用于观察贴纸的发送、消费与使用表现。
description_en: A DM sticker metric group used to observe sticker sending, consumption, and usage behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a feature-specific supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Streak
group_aliases:
  - DM Streak
  - Streak

description_zh: 私信连贯互动相关指标组，用于观察连续互动或 streak 行为表现。
description_en: A DM streak metric group used to observe consecutive interaction or streak behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting retention/engagement group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Conversion Funnel
group_aliases:
  - DM Conversion
  - Conversion Funnel

description_zh: 私信转化漏斗相关指标组，用于观察从曝光到进入、发送、互动等转化链路表现。
description_en: A DM conversion-funnel metric group used to observe conversion from exposure to entry, sending, and interaction.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a funnel support group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Message Pairs
group_aliases:
  - DM Pairs
  - Message Pairs

description_zh: 私信消息对相关指标组，用于观察消息对、双向互动或 pair 结构的表现。
description_en: A DM message-pairs metric group used to observe message-pair and bidirectional interaction behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a relationship-strength supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM by Link
group_aliases:
  - DM Link
  - by Link

description_zh: 私信链接相关指标组，用于观察链接发送、点击和转化等链路表现。
description_en: A DM by-link metric group used to observe link sending, clicking, and conversion behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a feature-specific supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Internal Share All
group_aliases:
  - Internal Share
  - internal share funnel metrics
  - internal share search funnel metrics

description_zh: 站内分享全链路指标组，用于观察站内分享的发送、覆盖与转化表现。
description_en: An internal-share funnel metric group used to observe send, coverage, and conversion behaviors for in-app sharing.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a share-supporting or guardrail group in social experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the shared formal glossary and live Libra watched-group list.
```

## Entry

```yaml
group_name: DM Quick Share
group_aliases:
  - Quick Share

description_zh: 私信快捷分享相关指标组，用于观察快速分享链路的使用表现。
description_en: A DM quick-share metric group used to observe quick-share usage behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a feature-specific supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: DM_Share_Type | direct message share type
group_aliases:
  - DM Share Type
  - direct message share type

description_zh: 私信分享类型相关指标组，用于观察不同分享类型的分布与转化表现。
description_en: A DM share-type metric group used to observe the distribution and conversion of share types.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a sharing-behavior supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Key Project-DM
group_aliases:
  - DM core interaction
  - DM business core

description_zh: 私信核心业务交互指标组，通常覆盖发送、点赞、接收、分享等更宽口径的互动信号。
description_en: A DM core interaction metric group that usually covers sending, liking, receiving, and sharing signals.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a business-core supporting group in DM experiments
priority_hint: P0

common_dimensions:

notes: Confirmed in the shared formal glossary as a reusable DM interaction group.
```

## Entry

```yaml
group_name: [DM] DM Negative Feedback
group_aliases:
  - DM Negative Feedback
  - Negative Feedback

description_zh: 私信负反馈与举报类指标组，通常用于观察拉黑、静音、取消静音、举报点击与举报用户等风险信号。
description_en: A DM negative-feedback metric group that usually covers block, mute, unmute, and report-related risk signals.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a risk / guardrail group in DM experiments
priority_hint: P0

common_dimensions:

notes: Confirmed from the current experiment report and live Libra group list as a reusable risk group.
```

## Entry

```yaml
group_name: [DM] DM Core Performance - Android
group_aliases:
  - DM Core Performance Android
  - Android Performance

description_zh: 私信 Android 端核心性能指标组，通常用于观察聊天列表、聊天房间、发送链路的加载时延与卡顿风险。
description_en: A DM Android performance metric group that usually covers chat-list, chat-room, and send-path latency and frame-drop risks.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a platform-performance guardrail group in DM experiments
priority_hint: P0

common_dimensions:

notes: Confirmed from the current experiment report as an Android performance guardrail group.
```

## Entry

```yaml
group_name: [DM] DM Core Performance - iOS
group_aliases:
  - DM Core Performance iOS
  - iOS Performance

description_zh: 私信 iOS 端核心性能指标组，通常用于观察聊天房间等关键链路的加载时延风险。
description_en: A DM iOS performance metric group that usually covers latency risk in key DM paths such as the chat room.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a platform-performance guardrail group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the current experiment report as an iOS performance guardrail group.
```

## Entry

```yaml
group_name: Core-Active Days
group_aliases:
  - Tiktok core metrics: the average active days of users
  - Active Days

description_zh: TikTok 核心活跃天数指标组，用来描述用户在给定回看窗口内的活跃覆盖情况。
description_en: A TikTok core metric group that describes user activity coverage over a lookback window.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a core health or guardrail group in social experiments
priority_hint: P0

common_dimensions:

notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
```

## Entry

```yaml
group_name: Active Hours (HLT)
group_aliases:
  - Tiktok core metrics: the average active hours of users
  - HLT

description_zh: TikTok 核心活跃时长指标组，用来描述用户在给定回看窗口内的人均使用深度。
description_en: A TikTok core metric group that describes user depth of usage over a lookback window.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a core health or time-spent supporting group in social experiments
priority_hint: context_dependent

common_dimensions:

notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
```

## Entry

```yaml
group_name: Core-Publish Days
group_aliases:
  - Publish Days

description_zh: TikTok 创作发布相关指标组，用于描述用户在给定回看窗口内的发布覆盖情况。
description_en: A TikTok creation-related metric group that describes user publish coverage over a lookback window.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a creation or supply-side guardrail group in social experiments
priority_hint: P0

common_dimensions:

notes: Confirmed in the shared formal glossary as a mandatory-recall core-health group.
```

## Entry

```yaml
group_name: Core-Key Metrics
group_aliases:
  - Core metrics

description_zh: TikTok 核心通用指标组，通常承载停留、发布、播放、完播、会话、登录与响应等基础健康信号。
description_en: A TikTok core general metric group that usually covers stay, publish, play, finish, session, login, and response signals.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a core health supporting group across social experiments
priority_hint: P1

common_dimensions:

notes: Confirmed in the shared formal glossary as a reusable core-health group.
```

## Entry

```yaml
group_name: Activity Status Metrics
group_aliases:
  - Active Status Metrics

description_zh: 私信活跃状态相关指标组，用于观察活跃状态和行为状态的总体变化。
description_en: A DM activity-status metric group used to observe changes in active-status and behavior-status signals.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting engagement group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
```

## Entry

```yaml
group_name: Activity Status User Metrics
group_aliases:
  - Active Status User Metrics

description_zh: 私信活跃状态用户级指标组，用于观察用户粒度的活跃状态变化。
description_en: A DM activity-status user metric group used to observe user-level active-status changes.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting user-level engagement group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
```

## Entry

```yaml
group_name: TnS DM Private Sender Metrics - Conv Level
group_aliases:
  - TnS Private Sender Conv Level

description_zh: 私信私聊发送端会话层指标组，用于观察发送端会话层面的申诉与审核表现。
description_en: A DM private-sender conversation-level metric group used to observe appeal and review behaviors on the sending side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
```

## Entry

```yaml
group_name: TnS DM Private Sender Metrics - Msg Level
group_aliases:
  - TnS Private Sender Msg Level

description_zh: 私信私聊发送端消息层指标组，用于观察发送端消息层面的申诉与审核表现。
description_en: A DM private-sender message-level metric group used to observe appeal and review behaviors on the sending side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary.
```

## Entry

```yaml
group_name: TnS DM Private Receiver Metrics - Msg Level
group_aliases:
  - TnS Private Receiver Msg Level

description_zh: 私信私聊接收端消息层指标组，用于观察接收端消息层面的申诉与审核表现。
description_en: A DM private-receiver message-level metric group used to observe appeal and review behaviors on the receiving side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
```

## Entry

```yaml
group_name: TnS DM Group Chat Sender Metrics - Conv Level
group_aliases:
  - TnS Group Chat Sender Conv Level

description_zh: 私信群聊发送端会话层指标组，用于观察群聊发送端会话层面的通知与申诉表现。
description_en: A DM group-chat sender conversation-level metric group used to observe notification and appeal behaviors on the sending side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; concrete metrics are already formalized in the glossary.
```

## Entry

```yaml
group_name: TnS DM Group Chat Sender Metrics - Msg Level
group_aliases:
  - TnS Group Chat Sender Msg Level

description_zh: 私信群聊发送端消息层指标组，用于观察群聊发送端消息层面的申诉表现。
description_en: A DM group-chat sender message-level metric group used to observe appeal behavior on the sending side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary.
```

## Entry

```yaml
group_name: TnS DM Group Chat Receiver Metrics - Msg Level
group_aliases:
  - TnS Group Chat Receiver Msg Level

description_zh: 私信群聊接收端消息层指标组，用于观察群聊接收端消息层面的申诉表现。
description_en: A DM group-chat receiver message-level metric group used to observe appeal behavior on the receiving side.

usage_scope: DM / trust & safety
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a trust-and-safety supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
```

## Entry

```yaml
group_name: DM Growth Pairs-Key Metrics
group_aliases:
  - Growth Pairs Key Metrics

description_zh: 私信增长对相关核心指标组，用于观察增长对场景下的关键健康表现。
description_en: A growth-pairs key-metrics group used to observe core health signals in growth-pairs scenarios.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a growth-supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: DM Growth Pairs-Active Days
group_aliases:
  - Growth Pairs Active Days

description_zh: 私信增长对活跃天数相关指标组，用于观察增长对用户活跃天数的影响。
description_en: A growth-pairs active-days metric group used to observe effects on active-day coverage.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a retention-supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: DM Growth Pairs- Retention
group_aliases:
  - Growth Pairs Retention

description_zh: 私信增长对留存相关指标组，用于观察增长对用户留存表现的影响。
description_en: A growth-pairs retention metric group used to observe effects on retention behavior.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a retention-supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Muf Growth DM Pairs By time
group_aliases:
  - MUF Growth DM Pairs By Time

description_zh: 按时间切分的 MUF 增长对指标组，用于观察增长对私信对关系在时间维度上的变化。
description_en: A time-sliced MUF growth-pairs metric group used to observe temporal changes in DM pair behavior.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a time-sliced growth-supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Inbox Element Metrics
group_aliases:
  - Inbox Elements

description_zh: Inbox 元素相关指标组，用于观察 Inbox 页面元素的曝光、点击与使用表现。
description_en: An inbox-element metric group used to observe exposure, click, and usage behaviors of inbox elements.

usage_scope: Inbox / social messaging experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an inbox-supporting group in messaging experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Inbox element metrics uid
group_aliases:
  - Inbox Element Metrics UID

description_zh: Inbox 元素用户级指标组，用于观察用户维度的 Inbox 元素使用表现。
description_en: An inbox-element user-level metric group used to observe user-level usage of inbox elements.

usage_scope: Inbox / social messaging experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an inbox-supporting user-level group in messaging experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Inbox message metrics uid
group_aliases:
  - Inbox Message Metrics UID

description_zh: Inbox 消息用户级指标组，用于观察用户维度的 Inbox 消息表现。
description_en: An inbox-message user-level metric group used to observe user-level inbox-message behaviors.

usage_scope: Inbox / social messaging experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an inbox-supporting user-level group in messaging experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [B2C] Business Message Key Metrics
group_aliases:
  - Business Message Key Metrics

description_zh: B2C 业务消息核心指标组，用于观察业务消息的关键健康表现。
description_en: A B2C business-message key-metrics group used to observe core health behaviors for business messages.

usage_scope: B2C / business messaging experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a business-messaging core-supporting group
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] Active Status
group_aliases:
  - Active Status

description_zh: 私信活跃状态指标组，用于观察活跃状态相关表现。
description_en: A DM active-status metric group used to observe active-status related behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting engagement group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM by Entrance
group_aliases:
  - DM by Entrance
  - By Entrance

description_zh: 私信按入口切分的指标组，用于观察不同入口来源下的发送、进入与互动表现。
description_en: A DM by-entrance metric group used to observe sending, entry, and interaction behaviors by entrance source.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a slice-oriented supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Entrance

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM by Msg Type
group_aliases:
  - DM by Message Type
  - By Msg Type

description_zh: 私信按消息类型切分的指标组，用于观察不同消息类型下的发送、互动与转化表现。
description_en: A DM by-message-type metric group used to observe sending, interaction, and conversion behaviors by message type.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a slice-oriented supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Msg Type

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Quality & Reply Rates
group_aliases:
  - DM Quality
  - Reply Rates

description_zh: 私信质量与回复率相关指标组，用于观察回复质量、回复率和会话互动体验。
description_en: A DM quality-and-reply-rates metric group used to observe reply quality, reply rates, and chat interaction experience.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an engagement-quality supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Quality & Reply Rates New
group_aliases:
  - DM Quality New
  - Reply Rates New

description_zh: 私信质量与回复率的新口径指标组，用于观察更新后的质量与回复表现。
description_en: A DM quality-and-reply-rates-new metric group used to observe updated quality and reply behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an updated engagement-quality supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Receive New
group_aliases:
  - DM Receive New
  - Receive New

description_zh: 私信接收侧新口径指标组，用于观察接收链路的新版本指标表现。
description_en: A DM receive-new metric group used to observe the updated receive-side metric set.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a receive-side supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Group Chat by Msg Type
group_aliases:
  - DM Group Chat by Msg Type
  - Group Chat by Msg Type

description_zh: 私信群聊按消息类型切分的指标组，用于观察群聊场景下不同消息类型的互动表现。
description_en: A DM group-chat metric group split by message type, used to observe interaction behaviors by message type in group chats.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a slice-oriented supporting group in DM experiments
priority_hint: P1

common_dimensions:
  - By Msg Type

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 3d Retention
group_aliases:
  - DM Group Chat 3d Retention

description_zh: 私信群聊 3 日留存正式存储位置。
description_en: Formal storage location for DM group-chat 3-day retention metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 7d Retention
group_aliases:
  - DM Group Chat 7d Retention

description_zh: 私信群聊 7 日留存正式存储位置。
description_en: Formal storage location for DM group-chat 7-day retention metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 14d Retention
group_aliases:
  - DM Group Chat 14d Retention

description_zh: 私信群聊 14 日留存正式存储位置。
description_en: Formal storage location for DM group-chat 14-day retention metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 28d Retention
group_aliases:
  - DM Group Chat 28d Retention

description_zh: 私信群聊 28 日留存正式存储位置。
description_en: Formal storage location for DM group-chat 28-day retention metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 3d Retention New gt3-users
group_aliases:
  - DM Group Chat 3d Retention New gt3-users

description_zh: 私信群聊新口径 3 日留存（gt3-users）正式存储位置。
description_en: Formal storage location for DM group-chat 3-day retention (gt3-users) metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: updated group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 7d Retention New gt3-users
group_aliases:
  - DM Group Chat 7d Retention New gt3-users

description_zh: 私信群聊新口径 7 日留存（gt3-users）正式存储位置。
description_en: Formal storage location for DM group-chat 7-day retention (gt3-users) metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: updated group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 14d Retention New gt3-users
group_aliases:
  - DM Group Chat 14d Retention New gt3-users

description_zh: 私信群聊新口径 14 日留存（gt3-users）正式存储位置。
description_en: Formal storage location for DM group-chat 14-day retention (gt3-users) metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: updated group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] DM Group Chat 28d Retention New gt3-users
group_aliases:
  - DM Group Chat 28d Retention New gt3-users

description_zh: 私信群聊新口径 28 日留存（gt3-users）正式存储位置。
description_en: Formal storage location for DM group-chat 28-day retention (gt3-users) metrics.

usage_scope: DM / social interaction experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: updated group-chat retention bucket
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list.
```

## Entry

```yaml
group_name: [DM] MuF DM Lifecycle
group_aliases:
  - MuF DM Lifecycle
  - DM Lifecycle

description_zh: 私信 MUF 生命周期指标组，用于记录生命周期相关正式指标。
description_en: A DM MUF lifecycle metric group used to store formal lifecycle-related metrics.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a lifecycle supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Quick Share Recall | Quick Share Recall
group_aliases:
  - Quick Share Recall

description_zh: 快捷分享召回相关指标组，用于记录召回链路正式指标。
description_en: A quick-share recall metric group used to store formal metrics for the quick-share recall flow.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a recall-supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: internal share funnel metrics
group_aliases:
  - Internal Share Funnel Metrics
  - internal share funnel

description_zh: 站内分享漏斗相关指标组，用于记录站内分享漏斗正式指标。
description_en: An internal-share funnel metric group used to store formal metrics for the in-app sharing funnel.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a share-supporting group in social experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: internal share search funnel metrics
group_aliases:
  - Internal Share Search Funnel Metrics
  - internal share search funnel

description_zh: 站内分享搜索漏斗相关指标组，用于记录站内分享搜索漏斗正式指标。
description_en: An internal-share search-funnel metric group used to store formal metrics for the in-app sharing search funnel.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a share-supporting group in social experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Core Interaction Growth Pairs-Active Days
group_aliases:
  - Core Interaction Growth Pairs Active Days

description_zh: 核心互动增长对活跃天数指标组，用于记录核心互动增长对的活跃天数正式指标。
description_en: A core-interaction growth-pairs active-days metric group used to store formal active-days metrics for core interaction growth pairs.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a growth-supporting retention group
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Core Interaction Growth Pairs- Retention
group_aliases:
  - Core Interaction Growth Pairs Retention

description_zh: 核心互动增长对留存指标组，用于记录核心互动增长对的留存正式指标。
description_en: A core-interaction growth-pairs retention metric group used to store formal retention metrics for core interaction growth pairs.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a growth-supporting retention group
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: Internal Share To Chat
group_aliases:
  - Internal Share to Chat
  - Share To Chat

description_zh: 站内分享到聊天相关指标组，用于记录从分享流转到聊天的正式指标。
description_en: An internal-share-to-chat metric group used to store formal metrics for share-to-chat behavior.

usage_scope: TikTok core health / A/B experiments
is_company_core: true
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a share-to-chat supporting group
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```

## Entry

```yaml
group_name: [DM] DM 2-Way
group_aliases:
  - DM 2-Way
  - 2-Way

description_zh: 私信双向互动指标组，用于观察双向发送或点赞链路的覆盖、强度与会话表现。
description_en: A DM two-way interaction metric group used to observe coverage, intensity, and session-level behavior for bidirectional send-or-like activity.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a supporting interaction-strength group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list and extracted report rows.
```

## Entry

```yaml
group_name: [DM] MuF DM by Motivation
group_aliases:
  - MuF DM by Motivation
  - Muf DM by Motivation

description_zh: 按 MUF 动机拆分的私信指标组，用于观察动机维度下的活跃、分享与互动表现。
description_en: A DM metric group split by MUF motivation, used to observe active, share, and interaction behaviors under motivation dimensions.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a motivation-split supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list and extracted report rows.
```

## Entry

```yaml
group_name: [DM] Muf DM Enter From as Dim
group_aliases:
  - Muf DM Enter From as Dim
  - DM Enter From

description_zh: 按进入来源拆分的 MUF 私信指标组，用于观察不同入口来源下的发送或点赞表现。
description_en: A DM MUF metric group split by entry source, used to observe send-or-like behaviors under different entry sources.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as an entry-source supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list and extracted report rows.
```

## Entry

```yaml
group_name: [DM] Muf DM Msg Type as Dim
group_aliases:
  - Muf DM Msg Type as Dim
  - DM Msg Type

description_zh: 按消息类型拆分的 MUF 私信指标组，用于观察不同消息类型下的发送或点赞表现。
description_en: A DM MUF metric group split by message type, used to observe send-or-like behaviors under different message types.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a message-type supporting group in DM experiments
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list and extracted report rows.
```

## Entry

```yaml
group_name: [B2C] Creator Message Key Metrics
group_aliases:
  - Creator Message Key Metrics

description_zh: 创作者消息核心指标组，用于观察创作者消息的关键健康表现。
description_en: A creator-message key-metrics group used to observe core health behaviors for creator messaging.

usage_scope: B2C / creator messaging experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a creator-messaging core-supporting group
priority_hint: P1

common_dimensions:

notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
```
