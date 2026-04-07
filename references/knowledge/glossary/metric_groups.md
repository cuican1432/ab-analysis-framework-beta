# Metric Groups | 指标组正式条目

```yaml
group_name: DM Core
group_aliases:
  - 私信核心指标组
description_zh: 私信核心使用行为指标组，覆盖私聊和群聊场景，通常用于观察进入会话、停留、发送等主链路行为。
description_en: A core DM usage metric group covering both private-chat and group-chat scenarios, usually used to observe entering chat, staying, and sending behaviors.
usage_scope: social / DM / core
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 1
typical_usage: 
priority_hint: P0
common_dimensions:
  -
notes: Use dimensions only when they are explicitly present in the raw data or source table. Surface note: both private-chat and group-chat by default.
```

```yaml
group_name: DM Voice Message
group_aliases:
  - 私信语音指标组
description_zh: 私信语音消息相关指标组，通常用于观察语音录制、取消、发送等行为。
description_en: A DM voice-message metric group that usually covers recording, canceling, and sending voice messages.
usage_scope: social / DM / voice message
business_domain: DM Voice Message
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: 
priority_hint: P2
common_dimensions:
  - By Msg Type
notes: Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Camera
group_aliases:
  - DM Camera
  - Camera Message / DM Camera
description_zh: 私信相机消息相关指标组，用于观察 DM Camera 的发送、上传、拍摄页进入等链路表现。
description_en: A DM camera-message metric group used to observe sending, upload, and shoot-page entry behaviors for DM Camera.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: 
priority_hint: P2
common_dimensions:
  -
notes: Confirmed in the shared formal glossary as a reusable DM camera group. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Camera by Entrance
group_aliases:
  - DM Camera by Entrance
  - Camera by Entrance
description_zh: 私信相机按入口切分的指标组，用于观察不同入口来源下的相机链路表现。
description_en: A DM camera metric group split by entrance source, used to observe camera-path behaviors by entrance source.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: 
priority_hint: P2
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Camera Private Chat
group_aliases:
  - DM Camera Private Chat
  - Camera Private Chat
description_zh: 私信相机私聊指标组，用于观察私聊场景下的相机链路表现。
description_en: A DM camera metric group for private-chat scenarios, used to observe camera-path behaviors in private chat.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: 
priority_hint: P2
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only.
```

```yaml
group_name: [DM] DM Camera Private Chat by Entrance
group_aliases:
  - DM Camera Private Chat by Entrance
  - Camera Private Chat by Entrance
description_zh: 私信相机私聊按入口切分的指标组，用于观察私聊场景下不同入口的相机链路表现。
description_en: A DM camera metric group for private-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture entrance-level variation in private-chat camera behavior
priority_hint: P2
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only.
```

```yaml
group_name: [DM] DM Camera Group Chat
group_aliases:
  - DM Camera Group Chat
  - Camera Group Chat
description_zh: 私信相机群聊指标组，用于观察群聊场景下的相机链路表现。
description_en: A DM camera metric group for group-chat scenarios, used to observe camera-path behaviors in group chat.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture camera behavior in group-chat scenarios
priority_hint: P2
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Camera Group Chat by Entrance
group_aliases:
  - DM Camera Group Chat by Entrance
  - Camera Group Chat by Entrance
description_zh: 私信相机群聊按入口切分的指标组，用于观察群聊场景下不同入口的相机链路表现。
description_en: A DM camera metric group for group-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
usage_scope: social / DM / camera
business_domain: DM Camera
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture entrance-level variation in group-chat camera behavior
priority_hint: P2
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
```

```yaml
group_name: DM Group Chat
group_aliases:
  - 私信群聊指标组
description_zh: 私信群聊相关指标组，通常用于观察群聊进入、发送、互动与创建行为。
description_en: A DM group-chat metric group that usually covers entering, sending, interacting, and creating group chats.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 0
is_sub_business_core: 1
typical_usage: used to capture group-chat effects directly within DM experiments
priority_hint: P2
common_dimensions:
  - By Entrance
  - By Motivation
  - By Msg Type
notes: Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Receive
group_aliases:
  - DM Receive
  - Receive
description_zh: 私信接收侧指标组，用于观察接收消息、被动互动、接收链路相关表现。
description_en: A DM receive-side metric group used to observe received-message and receive-side interaction behaviors.
usage_scope: social / DM / receive
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture receive-side message and interaction behavior across DM surfaces
priority_hint: P3
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
```

```yaml
group_name: [DM] DM Permission
group_aliases:
  - DM Permission
  - Permission
description_zh: 私信权限与陌生人消息机制指标组，用于理解谁可发起请求、消息请求权限等安全机制。
description_en: A DM permission and stranger-message metric group used to understand request permissions and safety mechanisms.
usage_scope: social / DM / safety
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as a DM safety and privacy rule layer
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the shared formal glossary and live Libra group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Send & Load Fail
group_aliases:
  - DM Send Load Fail
  - Send Load Fail
description_zh: 私信发送与加载失败指标组，用于观察发送失败、加载失败及相关体验风险。
description_en: A DM send-and-load-failure metric group used to observe send failures, load failures, and related experience risks.
usage_scope: social / DM / experience
business_domain: DM Performance
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as a DM failure and experience-risk layer
priority_hint: P1
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Leave Chat
group_aliases:
  - DM Leave
  - Leave Chat
description_zh: 私信离开会话相关指标组，用于观察用户退出聊天链路的行为表现。
description_en: A DM leave-chat metric group used to observe chat-exit behaviors.
usage_scope: social / DM / experience
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture chat-exit and disengagement behavior
priority_hint: P3
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Core Performance - Latency
group_aliases:
  - DM Core Performance Latency
  - Core Performance Latency
description_zh: 私信核心性能延迟相关指标组，用于记录更泛化的延迟口径正式指标。
description_en: A DM core-performance latency metric group used to store formal latency metrics under the DM core-performance umbrella.
usage_scope: social / DM / experience
business_domain: DM Performance
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as a DM latency and experience-performance layer
priority_hint: P4
common_dimensions:
  - By Msg Type
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Inner Push
group_aliases:
  - DM Inner Push
  - Inner Push
description_zh: 私信站内推送相关指标组，用于观察站内触达、提醒与召回链路表现。
description_en: A DM in-app push metric group used to observe in-app reach, reminder, and recall behaviors.
usage_scope: social / DM / push
business_domain: DM PUSH
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as in-app DM push recall and notification context
priority_hint: P1
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM push-side context across DM surfaces; not limited to one chat surface by default.
```

```yaml
group_name: [DM] DM Outer Push
group_aliases:
  - DM Outer Push
  - Outer Push
description_zh: 私信站外推送相关指标组，用于观察站外触达、召回与回流链路表现。
description_en: A DM out-of-app push metric group used to observe off-app reach, recall, and re-entry behaviors.
usage_scope: social / DM / push
business_domain: DM PUSH
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as off-app DM push recall and re-entry context
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM push-side context across DM surfaces; not limited to one chat surface by default.
```

```yaml
group_name: [DM] DM Sticker
group_aliases:
  - DM Sticker
  - Sticker
description_zh: 私信贴纸消息相关指标组，用于观察贴纸的发送、消费与使用表现。
description_en: A DM sticker metric group used to observe sticker sending, consumption, and usage behaviors.
usage_scope: social / DM / sticker
business_domain: DM Sticker
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture sticker creation, sending, and consumption behavior in DM
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Streak
group_aliases:
  - DM Streak
  - Streak
description_zh: 私信火花玩法相关指标组，用于观察 streak / 火花在私聊和群聊中的建立、维持与互动表现。
description_en: A DM streak (fire-badge) metric group used to observe streak creation, maintenance, and interaction behaviors across both private chats and group chats.
usage_scope: social / DM / streaks
business_domain: DM Streak
is_company_core: 0
is_business_core: 0
is_sub_business_core: 1
typical_usage: used for DM streak / flame-play effects across both private-chat and group-chat scenarios
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat.
```

```yaml
group_name: [DM] DM Conversion Funnel
group_aliases:
  - DM Conversion
  - Conversion Funnel
description_zh: 私信转化漏斗相关指标组，用于观察从曝光到进入、发送、互动等转化链路表现。
description_en: A DM conversion-funnel metric group used to observe conversion from exposure to entry, sending, and interaction.
usage_scope: social / DM / funnel
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 1
typical_usage: used to capture exposure-to-entry-to-send conversion flow
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Message Pairs
group_aliases:
  - DM Pairs
  - Message Pairs
description_zh: 私信消息对相关指标组，用于观察私聊场景下的消息对、双向互动或 pair 结构表现。
description_en: A DM message-pairs metric group used to observe message-pair and bidirectional interaction behaviors in private-chat scenarios.
usage_scope: social / DM / pairs
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture private-chat relationship strength and pair structure
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: [DM] DM by Link
group_aliases:
  - DM Link
  - by Link
description_zh: 私信链接相关指标组，用于观察链接发送、点击和转化等链路表现。
description_en: A DM by-link metric group used to observe link sending, clicking, and conversion behaviors.
usage_scope: social / DM / link
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture link-sharing and link-conversion behavior in DM
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: Internal Share All
group_aliases:
  - Internal Share
  - internal share funnel metrics
  - internal share search funnel metrics
description_zh: 站内分享全链路指标组，用于观察站内分享的发送、覆盖与转化表现，覆盖 share video、share comment、share profile page 等全题材分享。
description_en: An internal-share metric group used to observe send, coverage, and conversion behaviors across broad in-app share types such as share video, share comment, and share profile page.
usage_scope: social / DM adjacent mechanics / share
business_domain: Share&Repost
is_company_core: 0
is_business_core: 0
is_sub_business_core: 1
typical_usage: used as a broad in-app sharing context layer across social surfaces
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the shared formal glossary and live Libra watched-group list. Surface note: DM-adjacent sharing context; broader than a single DM surface.
```

```yaml
group_name: DM Quick Share
group_aliases:
  - Quick Share
description_zh: 私信快捷分享相关指标组，用于观察快速分享链路的使用表现。
description_en: A DM quick-share metric group used to observe quick-share usage behaviors.
usage_scope: social / DM adjacent mechanics / share
business_domain: Share&Repost
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used to capture quick-share entry and usage behavior near DM
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
```

```yaml
group_name: Key Project-DM
group_aliases:
  - DM core interaction
  - DM business core
description_zh: 私信核心业务交互指标组，通常覆盖发送、点赞、接收、分享等更宽口径的互动信号。
description_en: A DM core interaction metric group that usually covers sending, liking, receiving, and sharing signals.
usage_scope: social / DM / core
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a business-core DM interaction layer
priority_hint: P0
common_dimensions:
  -
notes: Confirmed in the shared formal glossary as a reusable DM interaction group. Surface note: mixed DM core layer; current metrics include broad DM signals plus MUF/pair and some group-chat-specific variants.
```

```yaml
group_name: [DM] DM Negative Feedback
group_aliases:
  - DM Negative Feedback
  - Negative Feedback
description_zh: 私信负反馈与举报类指标组，通常用于观察拉黑、静音、取消静音、举报点击与举报用户等风险信号。
description_en: A DM negative-feedback metric group that usually covers block, mute, unmute, and report-related risk signals.
usage_scope: social / DM / safety
business_domain: DM
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as a risk and safety guardrail layer
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the current experiment report and live Libra group list as a reusable risk group. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Core Performance - Android
group_aliases:
  - DM Core Performance Android
  - Android Performance
description_zh: 私信 Android 端核心性能指标组，通常用于观察聊天列表、聊天房间、发送链路的加载时延与卡顿风险。
description_en: A DM Android performance metric group that usually covers chat-list, chat-room, and send-path latency and frame-drop risks.
usage_scope: social / DM / experience
business_domain: DM Performance
is_company_core: 0
is_business_core: 0
is_sub_business_core: 0
typical_usage: used as an Android performance guardrail layer for DM experience
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the current experiment report as an Android performance guardrail group. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Core Performance - iOS
group_aliases:
  - DM Core Performance iOS
  - iOS Performance
description_zh: 私信 iOS 端核心性能指标组，通常用于观察聊天房间等关键链路的加载时延风险。
description_en: A DM iOS performance metric group that usually covers latency risk in key DM paths such as the chat room.
usage_scope: social / DM / experience
business_domain: DM Performance
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as an iOS performance guardrail layer for DM experience
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the current experiment report as an iOS performance guardrail group. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: Core-Active Days
group_aliases:
  - Tiktok core metrics: the average active days of users
  - Active Days
description_zh: TikTok 核心活跃天数指标组，用来描述用户在给定回看窗口内的活跃覆盖情况。
description_en: A TikTok core metric group that describes user activity coverage over a lookback window.
usage_scope: social / core health
business_domain: company-wise core
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a cross-social health and activity-coverage layer
priority_hint: P0
common_dimensions:
  -
notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
```

```yaml
group_name: Active Hours (HLT)
group_aliases:
  - Tiktok core metrics: the average active hours of users
  - HLT
description_zh: TikTok 核心活跃时长指标组，用来描述用户在给定回看窗口内的人均使用深度。
description_en: A TikTok core metric group that describes user depth of usage over a lookback window.
usage_scope: social / core health
business_domain: company-wise core
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a cross-social depth-of-usage layer
priority_hint: context_dependent
common_dimensions:
  -
notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
```

```yaml
group_name: Core-Publish Days
group_aliases:
  - Publish Days
description_zh: TikTok 创作发布相关指标组，用于描述用户在给定回看窗口内的发布覆盖情况。
description_en: A TikTok creation-related metric group that describes user publish coverage over a lookback window.
usage_scope: social / core health
business_domain: company-wise core
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a cross-social creation and supply-health layer
priority_hint: P0
common_dimensions:
  -
Reference entry for notes: Confirmed in the shared formal glossary as a mandatory-recall core-health.
```

```yaml
group_name: Core-Key Metrics
group_aliases:
  - Core metrics
description_zh: TikTok 核心通用指标组，通常承载停留、发布、播放、完播、会话、登录与响应等基础健康信号。
description_en: A TikTok core general metric group that usually covers stay, publish, play, finish, session, login, and response signals.
usage_scope: social / core health
business_domain: company-wise core
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a cross-social core-health baseline layer
priority_hint: P1
common_dimensions:
  -
Reference entry for notes: Confirmed in the shared formal glossary as a reusable core-health.
```

```yaml
group_name: Activity Status Metrics
group_aliases:
  - Active Status Metrics
description_zh: 私信活跃状态相关指标组，用于观察活跃状态和行为状态的总体变化。
description_en: A DM activity-status metric group used to observe changes in active-status and behavior-status signals.
usage_scope: social / DM / activity
business_domain: Active Status
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture overall activity-status and engagement-state change
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: Activity Status User Metrics
group_aliases:
  - Active Status User Metrics
description_zh: 私信活跃状态用户级指标组，用于观察用户粒度的活跃状态变化。
description_en: A DM activity-status user metric group used to observe user-level active-status changes.
usage_scope: social / DM / activity
business_domain: Active Status
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture user-level activity-status change
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: TnS DM Private Sender Metrics - Conv Level
group_aliases:
  - TnS Private Sender Conv Level
description_zh: 私信私聊发送端会话层指标组，用于观察发送端会话层面的申诉与审核表现。
description_en: A DM private-sender conversation-level metric group used to observe appeal and review behaviors on the sending side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety sender-side review layer for private chat
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: private-chat only.
```

```yaml
group_name: TnS DM Private Sender Metrics - Msg Level
group_aliases:
  - TnS Private Sender Msg Level
description_zh: 私信私聊发送端消息层指标组，用于观察发送端消息层面的申诉与审核表现。
description_en: A DM private-sender message-level metric group used to observe appeal and review behaviors on the sending side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety sender-side review layer at message level
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary. Surface note: private-chat only.
```

```yaml
group_name: TnS DM Private Receiver Metrics - Msg Level
group_aliases:
  - TnS Private Receiver Msg Level
description_zh: 私信私聊接收端消息层指标组，用于观察接收端消息层面的申诉与审核表现。
description_en: A DM private-receiver message-level metric group used to observe appeal and review behaviors on the receiving side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety receiver-side review layer at message level
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: private-chat only.
```

```yaml
group_name: TnS DM Group Chat Sender Metrics - Conv Level
group_aliases:
  - TnS Group Chat Sender Conv Level
description_zh: 私信群聊发送端会话层指标组，用于观察群聊发送端会话层面的通知与申诉表现。
description_en: A DM group-chat sender conversation-level metric group used to observe notification and appeal behaviors on the sending side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety sender-side review layer for group chat
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; concrete metrics are already formalized in the glossary. Surface note: group-chat only.
```

```yaml
group_name: TnS DM Group Chat Sender Metrics - Msg Level
group_aliases:
  - TnS Group Chat Sender Msg Level
description_zh: 私信群聊发送端消息层指标组，用于观察群聊发送端消息层面的申诉表现。
description_en: A DM group-chat sender message-level metric group used to observe appeal behavior on the sending side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety sender-side review layer at message level for group chat
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary. Surface note: group-chat only.
```

```yaml
group_name: TnS DM Group Chat Receiver Metrics - Msg Level
group_aliases:
  - TnS Group Chat Receiver Msg Level
description_zh: 私信群聊接收端消息层指标组，用于观察群聊接收端消息层面的申诉表现。
description_en: A DM group-chat receiver message-level metric group used to observe appeal behavior on the receiving side.
usage_scope: social / DM / TnS
business_domain: DM Safety
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a trust-and-safety receiver-side review layer at message level for group chat
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: group-chat only.
```

```yaml
group_name: DM Growth Pairs-Key Metrics
group_aliases:
  - Growth Pairs Key Metrics
description_zh: 私信增长对相关核心指标组，用于观察增长对场景下的关键健康表现。
description_en: A growth-pairs key-metrics group used to observe core health signals in growth-pairs scenarios.
usage_scope: social / DM / growth pairs
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture core health in growth-pairs scenarios
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: DM Growth Pairs-Active Days
group_aliases:
  - Growth Pairs Active Days
description_zh: 私信增长对活跃天数相关指标组，用于观察增长对用户活跃天数的影响。
description_en: A growth-pairs active-days metric group used to observe effects on active-day coverage.
usage_scope: social / DM / growth pairs
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture activity coverage in growth-pairs scenarios
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: DM Growth Pairs- Retention
group_aliases:
  - Growth Pairs Retention
description_zh: 私信增长对留存相关指标组，用于观察增长对用户留存表现的影响。
description_en: A growth-pairs retention metric group used to observe effects on retention behavior.
usage_scope: social / DM / growth pairs
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture retention in growth-pairs scenarios
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: Muf Growth DM Pairs By time
group_aliases:
  - MUF Growth DM Pairs By Time
description_zh: 按时间切分的 MUF 增长对指标组，用于观察增长对私信对关系在时间维度上的变化。
description_en: A time-sliced MUF growth-pairs metric group used to observe temporal changes in DM pair behavior.
usage_scope: social / DM / growth pairs
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture time-sliced change in MUF-linked growth-pair behavior
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is MUF/pair-based.
```

```yaml
group_name: Inbox Element Metrics
group_aliases:
  - Inbox Elements
description_zh: Inbox 元素相关指标组，用于观察 Inbox 页面元素的曝光、点击与使用表现。
description_en: An inbox-element metric group used to observe exposure, click, and usage behaviors of inbox elements.
usage_scope: social / DM adjacent mechanics / inbox
business_domain: Inbox
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture inbox-surface element exposure and interaction behavior
priority_hint: P3
common_dimensions:
  -
Reference entry for notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface.
```

```yaml
group_name: Inbox element metrics uid
group_aliases:
  - Inbox Element Metrics UID
description_zh: Inbox 元素用户级指标组，用于观察用户维度的 Inbox 元素使用表现。
description_en: An inbox-element user-level metric group used to observe user-level usage of inbox elements.
usage_scope: social / DM adjacent mechanics / inbox
business_domain: Inbox
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture user-level interaction with inbox-surface elements
priority_hint: P3
common_dimensions:
  -
Reference entry for notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface.
```

```yaml
group_name: Inbox message metrics uid
group_aliases:
  - Inbox Message Metrics UID
description_zh: Inbox 消息用户级指标组，用于观察用户维度的 Inbox 消息表现。
description_en: An inbox-message user-level metric group used to observe user-level inbox-message behaviors.
usage_scope: social / DM adjacent mechanics / inbox
business_domain: Inbox
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture user-level inbox message exposure and interaction behavior
priority_hint: P3
common_dimensions:
  -
Reference entry for notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface.
```

```yaml
group_name: [B2C] Business Message Key Metrics
group_aliases:
  - Business Message Key Metrics
description_zh: B2C 业务消息核心指标组，用于观察业务消息的关键健康表现。
description_en: A B2C business-message key-metrics group used to observe core health behaviors for business messages.
usage_scope: social / DM / B2C messaging
business_domain: DM B2C
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a core health layer for business-messaging scenarios
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: B2C messaging surface; do not force it into private-chat or group-chat by default.
```

```yaml
group_name: [DM] Active Status
group_aliases:
  - Active Status
description_zh: 私信活跃状态指标组，用于观察活跃状态相关表现。
description_en: A DM active-status metric group used to observe active-status related behaviors.
usage_scope: social / DM / activity
business_domain: Active Status
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture DM-side activity-status and engagement-state signals
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM by Entrance
group_aliases:
  - DM by Entrance
  - By Entrance
description_zh: 私信按入口切分的指标组，用于观察不同入口来源下的发送、进入与互动表现。
description_en: A DM by-entrance metric group used to observe sending, entry, and interaction behaviors by entrance source.
usage_scope: social / DM / by entrance
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture entrance-sliced variation across DM surfaces
priority_hint: P0
common_dimensions:
  - By Entrance
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
```

```yaml
group_name: [DM] DM by Msg Type
group_aliases:
  - DM by Message Type
  - By Msg Type
description_zh: 私信按消息类型切分的指标组，用于观察不同消息类型下的发送、互动与转化表现。
description_en: A DM by-message-type metric group used to observe sending, interaction, and conversion behaviors by message type.
usage_scope: social / DM / by message type
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture message-type-sliced variation across DM surfaces
priority_hint: P0
common_dimensions:
  - By Msg Type
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
```

```yaml
group_name: [DM] DM Quality & Reply Rates
group_aliases:
  - DM Quality
  - Reply Rates
description_zh: 私信质量与回复率相关指标组，用于观察回复质量、回复率和会话互动体验。
description_en: A DM quality-and-reply-rates metric group used to observe reply quality, reply rates, and chat interaction experience.
usage_scope: social / DM / experience
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture reply quality and conversational responsiveness
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Quality & Reply Rates New
group_aliases:
  - DM Quality New
  - Reply Rates New
description_zh: 私信质量与回复率的新口径指标组，用于观察更新后的质量与回复表现。
description_en: A DM quality-and-reply-rates-new metric group used to observe updated quality and reply behaviors.
usage_scope: social / DM / experience
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture updated reply quality and conversational responsiveness
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
```

```yaml
group_name: [DM] DM Receive New
group_aliases:
  - DM Receive New
  - Receive New
description_zh: 私信接收侧新口径指标组，用于观察接收链路的新版本指标表现。
description_en: A DM receive-new metric group used to observe the updated receive-side metric set.
usage_scope: social / DM / receive
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture updated receive-side behavior across DM surfaces
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
```

```yaml
group_name: [DM] DM Group Chat by Msg Type
group_aliases:
  - DM Group Chat by Msg Type
  - Group Chat by Msg Type
description_zh: 私信群聊按消息类型切分的指标组，用于观察群聊场景下不同消息类型的互动表现。
description_en: A DM group-chat metric group split by message type, used to observe interaction behaviors by message type in group chats.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture message-type-sliced variation in group-chat behavior
priority_hint: P2
common_dimensions:
  - By Msg Type
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 3d Retention
group_aliases:
  - DM Group Chat 3d Retention
description_zh: 私信群聊 3 日留存。
description_en: DM group-chat 3-day retention metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 7d Retention
group_aliases:
  - DM Group Chat 7d Retention
description_zh: 私信群聊 7 日留存。
description_en: DM group-chat 7-day retention metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 14d Retention
group_aliases:
  - DM Group Chat 14d Retention
description_zh: 私信群聊 14 日留存。
description_en: DM group-chat 14-day retention metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 28d Retention
group_aliases:
  - DM Group Chat 28d Retention
description_zh: 私信群聊 28 日留存。
description_en: DM group-chat 28-day retention metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 3d Retention New gt3-users
group_aliases:
  - DM Group Chat 3d Retention New gt3-users
description_zh: 私信群聊新口径 3 日留存（gt3-users）。
description_en: DM group-chat 3-day retention (gt3-users) metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: updated group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 7d Retention New gt3-users
group_aliases:
  - DM Group Chat 7d Retention New gt3-users
description_zh: 私信群聊新口径 7 日留存（gt3-users）。
description_en: DM group-chat 7-day retention (gt3-users) metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: updated group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 14d Retention New gt3-users
group_aliases:
  - DM Group Chat 14d Retention New gt3-users
description_zh: 私信群聊新口径 14 日留存（gt3-users）。
description_en: DM group-chat 14-day retention (gt3-users) metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: updated group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] DM Group Chat 28d Retention New gt3-users
group_aliases:
  - DM Group Chat 28d Retention New gt3-users
description_zh: 私信群聊新口径 28 日留存（gt3-users）。
description_en: DM group-chat 28-day retention (gt3-users) metrics.
usage_scope: social / DM / group chat
business_domain: DM Group Chat
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: updated group-chat retention bucket
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
```

```yaml
group_name: [DM] MuF DM Lifecycle
group_aliases:
  - MuF DM Lifecycle
  - DM Lifecycle
description_zh: 私信 MUF 生命周期指标组，用于记录生命周期相关正式指标。
description_en: A DM MUF lifecycle metric group used to store formal lifecycle-related metrics.
usage_scope: social / DM / lifecycle
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture lifecycle-stage change in MUF-linked DM behavior
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is MUF-based.
```

```yaml
group_name: internal share funnel metrics
group_aliases:
  - Internal Share Funnel Metrics
  - internal share funnel
description_zh: 站内分享漏斗相关指标组，用于记录站内分享漏斗正式指标。
description_en: An internal-share funnel metric group used to store formal metrics for the in-app sharing funnel.
usage_scope: social / DM adjacent mechanics / share
business_domain: Share&Repost
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture broad in-app sharing funnel behavior
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
```

```yaml
group_name: internal share search funnel metrics
group_aliases:
  - Internal Share Search Funnel Metrics
  - internal share search funnel
description_zh: 站内分享搜索漏斗相关指标组，用于记录站内分享搜索漏斗正式指标。
description_en: An internal-share search-funnel metric group used to store formal metrics for the in-app sharing search funnel.
usage_scope: social / DM adjacent mechanics / share
business_domain: Share&Repost
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture in-app sharing search-funnel behavior
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
```

```yaml
group_name: Core Interaction Growth Pairs-Active Days
group_aliases:
  - Core Interaction Growth Pairs Active Days
description_zh: 核心互动增长对活跃天数指标组，用于记录核心互动增长对的活跃天数正式指标。
description_en: A core-interaction growth-pairs active-days metric group used to store formal active-days metrics for core interaction growth pairs.
usage_scope: social / core interaction
business_domain: Core Interaction
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture active-day coverage in core-interaction growth pairs
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: Core Interaction Growth Pairs- Retention
group_aliases:
  - Core Interaction Growth Pairs Retention
description_zh: 核心互动增长对留存指标组，用于记录核心互动增长对的留存正式指标。
description_en: A core-interaction growth-pairs retention metric group used to store formal retention metrics for core interaction growth pairs.
usage_scope: social / core interaction
business_domain: Core Interaction
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture retention in core-interaction growth pairs
priority_hint: P3
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
```

```yaml
group_name: Internal Share To Chat
group_aliases:
  - Internal Share to Chat
  - Share To Chat
description_zh: 站内分享到聊天相关指标组，用于记录从分享流转到聊天的正式指标。
description_en: An internal-share-to-chat metric group used to store formal metrics for share-to-chat behavior.
usage_scope: social / DM adjacent mechanics / share
business_domain: Share&Repost
is_company_core: 1
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture share-to-chat transition behavior
priority_hint: P4
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
```

```yaml
group_name: [DM] DM 2-Way
group_aliases:
  - DM 2-Way
  - 2-Way
description_zh: 私信双向互动指标组，用于观察双向发送或点赞链路的覆盖、强度与会话表现。
description_en: A DM two-way interaction metric group used to observe coverage, intensity, and session-level behavior for bidirectional send-or-like activity.
usage_scope: social / DM / two-way
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture bidirectional interaction strength across DM surfaces
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: mixed; current metrics include group-chat, MUF, and broad DM two-way variants.
```

```yaml
group_name: [DM] MuF DM by Motivation
group_aliases:
  - MuF DM by Motivation
  - Muf DM by Motivation
description_zh: 按 MUF 动机拆分的私信指标组，用于观察主动聊天、分享和作品互动这几类动机下的行为表现。
description_en: A DM metric group split by MUF motivation, used to observe behaviors under motivation buckets such as active chat, share, and post interaction.
usage_scope: social / DM / muf
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture motivation-sliced behavior across active-chat, share, and post-interaction buckets in MUF-linked DM scenarios
priority_hint: P0
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, MUF-only, and session-level motivation is attributed from the first message in the session.
```

```yaml
group_name: [DM] Muf DM Enter From as Dim
group_aliases:
  - Muf DM Enter From as Dim
  - DM Enter From
description_zh: 按进入来源拆分的 MUF 私信指标组，用于观察不同入口来源下的发送或点赞表现。
description_en: A DM MUF metric group split by entry source, used to observe send-or-like behaviors under different entry sources.
usage_scope: social / DM / muf
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture entry-source variation in MUF-linked DM behavior
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, because this group is MUF/pair-based.
```

```yaml
group_name: [DM] Muf DM Msg Type as Dim
group_aliases:
  - Muf DM Msg Type as Dim
  - DM Msg Type
description_zh: 按消息类型拆分的 MUF 私信指标组，用于观察不同消息类型下的发送或点赞表现。
description_en: A DM MUF metric group split by message type, used to observe send-or-like behaviors under different message types.
usage_scope: social / DM / muf
business_domain: DM
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used to capture message-type variation in MUF-linked DM behavior
priority_hint: P1
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, because this group is MUF/pair-based.
```

```yaml
group_name: [B2C] Creator Message Key Metrics
group_aliases:
  - Creator Message Key Metrics
description_zh: 创作者消息核心指标组，用于观察创作者消息的关键健康表现。
description_en: A creator-message key-metrics group used to observe core health behaviors for creator messaging.
usage_scope: social / DM / B2C messaging
business_domain: DM B2C
is_company_core: 0
is_business_core: 1
is_sub_business_core: 1
typical_usage: used as a creator-messaging core health layer
priority_hint: P2
common_dimensions:
  -
notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: B2C messaging surface; do not force it into private-chat or group-chat by default.
```
