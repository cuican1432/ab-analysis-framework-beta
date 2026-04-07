# Metric Groups Review

## DM Core
- [x] Review
- Chinese description: 私信核心使用行为指标组，覆盖私聊和群聊场景，通常用于观察进入会话、停留、发送等主链路行为。
- English description: A core DM usage metric group covering both private-chat and group-chat scenarios, usually used to observe entering chat, staying, and sending behaviors.
- Scope: social / DM / core
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 1
- Typical usage: 
- Priority: P0
- Common dimensions: 
- Aliases: 私信核心指标组
- Notes: Use dimensions only when they are explicitly present in the raw data or source table. Surface note: both private-chat and group-chat by default.
- Review note: 

## DM Voice Message
- [x] Review
- Chinese description: 私信语音消息相关指标组，通常用于观察语音录制、取消、发送等行为。
- English description: A DM voice-message metric group that usually covers recording, canceling, and sending voice messages.
- Scope: social / DM / voice message
- Business domain: DM Voice Message
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: 
- Priority: P2
- Common dimensions: By Msg Type
- Aliases: 私信语音指标组
- Notes: Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Camera
- [x] Review
- Chinese description: 私信相机消息相关指标组，用于观察 DM Camera 的发送、上传、拍摄页进入等链路表现。
- English description: A DM camera-message metric group used to observe sending, upload, and shoot-page entry behaviors for DM Camera.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: 
- Priority: P2
- Common dimensions: 
- Aliases: DM Camera; Camera Message / DM Camera
- Notes: Confirmed in the shared formal glossary as a reusable DM camera group. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Camera by Entrance
- [x] Review
- Chinese description: 私信相机按入口切分的指标组，用于观察不同入口来源下的相机链路表现。
- English description: A DM camera metric group split by entrance source, used to observe camera-path behaviors by entrance source.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: 
- Priority: P2
- Common dimensions: By Entrance
- Aliases: DM Camera by Entrance; Camera by Entrance
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Camera Private Chat
- [x] Review
- Chinese description: 私信相机私聊指标组，用于观察私聊场景下的相机链路表现。
- English description: A DM camera metric group for private-chat scenarios, used to observe camera-path behaviors in private chat.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: 
- Priority: P2
- Common dimensions: By Entrance
- Aliases: DM Camera Private Chat; Camera Private Chat
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only.
- Review note: 

## [DM] DM Camera Private Chat by Entrance
- [x] Review
- Chinese description: 私信相机私聊按入口切分的指标组，用于观察私聊场景下不同入口的相机链路表现。
- English description: A DM camera metric group for private-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture entrance-level variation in private-chat camera behavior
- Priority: P2
- Common dimensions: By Entrance
- Aliases: DM Camera Private Chat by Entrance; Camera Private Chat by Entrance
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only.
- Review note: 

## [DM] DM Camera Group Chat
- [x] Review
- Chinese description: 私信相机群聊指标组，用于观察群聊场景下的相机链路表现。
- English description: A DM camera metric group for group-chat scenarios, used to observe camera-path behaviors in group chat.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture camera behavior in group-chat scenarios
- Priority: P2
- Common dimensions: By Entrance
- Aliases: DM Camera Group Chat; Camera Group Chat
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
- Review note: 

## [DM] DM Camera Group Chat by Entrance
- [x] Review
- Chinese description: 私信相机群聊按入口切分的指标组，用于观察群聊场景下不同入口的相机链路表现。
- English description: A DM camera metric group for group-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
- Scope: social / DM / camera
- Business domain: DM Camera
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture entrance-level variation in group-chat camera behavior
- Priority: P2
- Common dimensions: By Entrance
- Aliases: DM Camera Group Chat by Entrance; Camera Group Chat by Entrance
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
- Review note: 

## DM Group Chat
- [x] Review
- Chinese description: 私信群聊相关指标组，通常用于观察群聊进入、发送、互动与创建行为。
- English description: A DM group-chat metric group that usually covers entering, sending, interacting, and creating group chats.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 0
- Sub-business core: 1
- Typical usage: used to capture group-chat effects directly within DM experiments
- Priority: P2
- Common dimensions: By Entrance; By Motivation; By Msg Type
- Aliases: 私信群聊指标组
- Notes: Surface note: group-chat only.
- Review note: 

## [DM] DM Receive
- [x] Review
- Chinese description: 私信接收侧指标组，用于观察接收消息、被动互动、接收链路相关表现。
- English description: A DM receive-side metric group used to observe received-message and receive-side interaction behaviors.
- Scope: social / DM / receive
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture receive-side message and interaction behavior across DM surfaces
- Priority: P3
- Common dimensions: By Entrance
- Aliases: DM Receive; Receive
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
- Review note: 

## [DM] DM Permission
- [x] Review
- Chinese description: 私信权限与陌生人消息机制指标组，用于理解谁可发起请求、消息请求权限等安全机制。
- English description: A DM permission and stranger-message metric group used to understand request permissions and safety mechanisms.
- Scope: social / DM / safety
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as a DM safety and privacy rule layer
- Priority: P3
- Common dimensions: 
- Aliases: DM Permission; Permission
- Notes: Confirmed from the shared formal glossary and live Libra group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Send & Load Fail
- [x] Review
- Chinese description: 私信发送与加载失败指标组，用于观察发送失败、加载失败及相关体验风险。
- English description: A DM send-and-load-failure metric group used to observe send failures, load failures, and related experience risks.
- Scope: social / DM / experience
- Business domain: DM Performance
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as a DM failure and experience-risk layer
- Priority: P1
- Common dimensions: By Entrance
- Aliases: DM Send Load Fail; Send Load Fail
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Leave Chat
- [x] Review
- Chinese description: 私信离开会话相关指标组，用于观察用户退出聊天链路的行为表现。
- English description: A DM leave-chat metric group used to observe chat-exit behaviors.
- Scope: social / DM / experience
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture chat-exit and disengagement behavior
- Priority: P3
- Common dimensions: By Entrance
- Aliases: DM Leave; Leave Chat
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Core Performance - Latency
- [x] Review
- Chinese description: 私信核心性能延迟相关指标组，用于记录更泛化的延迟口径正式指标。
- English description: A DM core-performance latency metric group used to store formal latency metrics under the DM core-performance umbrella.
- Scope: social / DM / experience
- Business domain: DM Performance
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as a DM latency and experience-performance layer
- Priority: P4
- Common dimensions: By Msg Type
- Aliases: DM Core Performance Latency; Core Performance Latency
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Inner Push
- [x] Review
- Chinese description: 私信站内推送相关指标组，用于观察站内触达、提醒与召回链路表现。
- English description: A DM in-app push metric group used to observe in-app reach, reminder, and recall behaviors.
- Scope: social / DM / push
- Business domain: DM PUSH
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as in-app DM push recall and notification context
- Priority: P1
- Common dimensions: By Entrance
- Aliases: DM Inner Push; Inner Push
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM push-side context across DM surfaces; not limited to one chat surface by default.
- Review note: 

## [DM] DM Outer Push
- [x] Review
- Chinese description: 私信站外推送相关指标组，用于观察站外触达、召回与回流链路表现。
- English description: A DM out-of-app push metric group used to observe off-app reach, recall, and re-entry behaviors.
- Scope: social / DM / push
- Business domain: DM PUSH
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as off-app DM push recall and re-entry context
- Priority: P1
- Common dimensions: 
- Aliases: DM Outer Push; Outer Push
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM push-side context across DM surfaces; not limited to one chat surface by default.
- Review note: 

## [DM] DM Sticker
- [x] Review
- Chinese description: 私信贴纸消息相关指标组，用于观察贴纸的发送、消费与使用表现。
- English description: A DM sticker metric group used to observe sticker sending, consumption, and usage behaviors.
- Scope: social / DM / sticker
- Business domain: DM Sticker
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture sticker creation, sending, and consumption behavior in DM
- Priority: P2
- Common dimensions: 
- Aliases: DM Sticker; Sticker
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Streak
- [x] Review
- Chinese description: 私信火花玩法相关指标组，用于观察 streak / 火花在私聊和群聊中的建立、维持与互动表现。
- English description: A DM streak (fire-badge) metric group used to observe streak creation, maintenance, and interaction behaviors across both private chats and group chats.
- Scope: social / DM / streaks
- Business domain: DM Streak
- Company core: 0
- Business core: 0
- Sub-business core: 1
- Typical usage: used for DM streak / flame-play effects across both private-chat and group-chat scenarios
- Priority: P2
- Common dimensions: 
- Aliases: DM Streak; Streak
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat.
- Review note: 

## [DM] DM Conversion Funnel
- [x] Review
- Chinese description: 私信转化漏斗相关指标组，用于观察从曝光到进入、发送、互动等转化链路表现。
- English description: A DM conversion-funnel metric group used to observe conversion from exposure to entry, sending, and interaction.
- Scope: social / DM / funnel
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 1
- Typical usage: used to capture exposure-to-entry-to-send conversion flow
- Priority: P3
- Common dimensions: 
- Aliases: DM Conversion; Conversion Funnel
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Message Pairs
- [x] Review
- Chinese description: 私信消息对相关指标组，用于观察私聊场景下的消息对、双向互动或 pair 结构表现。
- English description: A DM message-pairs metric group used to observe message-pair and bidirectional interaction behaviors in private-chat scenarios.
- Scope: social / DM / pairs
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture private-chat relationship strength and pair structure
- Priority: P3
- Common dimensions: 
- Aliases: DM Pairs; Message Pairs
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## [DM] DM by Link
- [x] Review
- Chinese description: 私信链接相关指标组，用于观察链接发送、点击和转化等链路表现。
- English description: A DM by-link metric group used to observe link sending, clicking, and conversion behaviors.
- Scope: social / DM / link
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture link-sharing and link-conversion behavior in DM
- Priority: P3
- Common dimensions: 
- Aliases: DM Link; by Link
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## Internal Share All
- [x] Review
- Chinese description: 站内分享全链路指标组，用于观察站内分享的发送、覆盖与转化表现，覆盖 share video、share comment、share profile page 等全题材分享。
- English description: An internal-share metric group used to observe send, coverage, and conversion behaviors across broad in-app share types such as share video, share comment, and share profile page.
- Scope: social / DM adjacent mechanics / share
- Business domain: Share&Repost
- Company core: 0
- Business core: 0
- Sub-business core: 1
- Typical usage: used as a broad in-app sharing context layer across social surfaces
- Priority: P3
- Common dimensions: 
- Aliases: Internal Share; internal share funnel metrics; internal share search funnel metrics
- Notes: Confirmed from the shared formal glossary and live Libra watched-group list. Surface note: DM-adjacent sharing context; broader than a single DM surface.
- Review note: 

## DM Quick Share
- [x] Review
- Chinese description: 私信快捷分享相关指标组，用于观察快速分享链路的使用表现。
- English description: A DM quick-share metric group used to observe quick-share usage behaviors.
- Scope: social / DM adjacent mechanics / share
- Business domain: Share&Repost
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used to capture quick-share entry and usage behavior near DM
- Priority: P3
- Common dimensions: 
- Aliases: Quick Share
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
- Review note: 

## Key Project-DM
- [x] Review
- Chinese description: 私信核心业务交互指标组，通常覆盖发送、点赞、接收、分享等更宽口径的互动信号。
- English description: A DM core interaction metric group that usually covers sending, liking, receiving, and sharing signals.
- Scope: social / DM / core
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a business-core DM interaction layer
- Priority: P0
- Common dimensions: 
- Aliases: DM core interaction; DM business core
- Notes: Confirmed in the shared formal glossary as a reusable DM interaction group. Surface note: mixed DM core layer; current metrics include broad DM signals plus MUF/pair and some group-chat-specific variants.
- Review note: 

## [DM] DM Negative Feedback
- [x] Review
- Chinese description: 私信负反馈与举报类指标组，通常用于观察拉黑、静音、取消静音、举报点击与举报用户等风险信号。
- English description: A DM negative-feedback metric group that usually covers block, mute, unmute, and report-related risk signals.
- Scope: social / DM / safety
- Business domain: DM
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as a risk and safety guardrail layer
- Priority: P1
- Common dimensions: 
- Aliases: DM Negative Feedback; Negative Feedback
- Notes: Confirmed from the current experiment report and live Libra group list as a reusable risk group. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Core Performance - Android
- [x] Review
- Chinese description: 私信 Android 端核心性能指标组，通常用于观察聊天列表、聊天房间、发送链路的加载时延与卡顿风险。
- English description: A DM Android performance metric group that usually covers chat-list, chat-room, and send-path latency and frame-drop risks.
- Scope: social / DM / experience
- Business domain: DM Performance
- Company core: 0
- Business core: 0
- Sub-business core: 0
- Typical usage: used as an Android performance guardrail layer for DM experience
- Priority: P1
- Common dimensions: 
- Aliases: DM Core Performance Android; Android Performance
- Notes: Confirmed from the current experiment report as an Android performance guardrail group. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Core Performance - iOS
- [x] Review
- Chinese description: 私信 iOS 端核心性能指标组，通常用于观察聊天房间等关键链路的加载时延风险。
- English description: A DM iOS performance metric group that usually covers latency risk in key DM paths such as the chat room.
- Scope: social / DM / experience
- Business domain: DM Performance
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as an iOS performance guardrail layer for DM experience
- Priority: P1
- Common dimensions: 
- Aliases: DM Core Performance iOS; iOS Performance
- Notes: Confirmed from the current experiment report as an iOS performance guardrail group. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## Core-Active Days
- [x] Review
- Chinese description: TikTok 核心活跃天数指标组，用来描述用户在给定回看窗口内的活跃覆盖情况。
- English description: A TikTok core metric group that describes user activity coverage over a lookback window.
- Scope: social / core health
- Business domain: company-wise core
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a cross-social health and activity-coverage layer
- Priority: P0
- Common dimensions: 
- Aliases: Tiktok core metrics: the average active days of users; Active Days
- Notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
- Review note: 

## Active Hours (HLT)
- [x] Review
- Chinese description: TikTok 核心活跃时长指标组，用来描述用户在给定回看窗口内的人均使用深度。
- English description: A TikTok core metric group that describes user depth of usage over a lookback window.
- Scope: social / core health
- Business domain: company-wise core
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a cross-social depth-of-usage layer
- Priority: context_dependent
- Common dimensions: 
- Aliases: Tiktok core metrics: the average active hours of users; HLT
- Notes: Confirmed from the live Libra metric-group list and the shared formal glossary.
- Review note: 

## Core-Publish Days
- [x] Review
- Chinese description: TikTok 创作发布相关指标组，用于描述用户在给定回看窗口内的发布覆盖情况。
- English description: A TikTok creation-related metric group that describes user publish coverage over a lookback window.
- Scope: social / core health
- Business domain: company-wise core
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a cross-social creation and supply-health layer
- Priority: P0
- Common dimensions: 
- Aliases: Publish Days
- Notes: Confirmed in the shared formal glossary as a mandatory-recall core-health group.
- Review note: 

## Core-Key Metrics
- [x] Review
- Chinese description: TikTok 核心通用指标组，通常承载停留、发布、播放、完播、会话、登录与响应等基础健康信号。
- English description: A TikTok core general metric group that usually covers stay, publish, play, finish, session, login, and response signals.
- Scope: social / core health
- Business domain: company-wise core
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a cross-social core-health baseline layer
- Priority: P1
- Common dimensions: 
- Aliases: Core metrics
- Notes: Confirmed in the shared formal glossary as a reusable core-health group.
- Review note: 

## Activity Status Metrics
- [x] Review
- Chinese description: 私信活跃状态相关指标组，用于观察活跃状态和行为状态的总体变化。
- English description: A DM activity-status metric group used to observe changes in active-status and behavior-status signals.
- Scope: social / DM / activity
- Business domain: Active Status
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture overall activity-status and engagement-state change
- Priority: P3
- Common dimensions: 
- Aliases: Active Status Metrics
- Notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## Activity Status User Metrics
- [x] Review
- Chinese description: 私信活跃状态用户级指标组，用于观察用户粒度的活跃状态变化。
- English description: A DM activity-status user metric group used to observe user-level active-status changes.
- Scope: social / DM / activity
- Business domain: Active Status
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture user-level activity-status change
- Priority: P3
- Common dimensions: 
- Aliases: Active Status User Metrics
- Notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## TnS DM Private Sender Metrics - Conv Level
- [x] Review
- Chinese description: 私信私聊发送端会话层指标组，用于观察发送端会话层面的申诉与审核表现。
- English description: A DM private-sender conversation-level metric group used to observe appeal and review behaviors on the sending side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety sender-side review layer for private chat
- Priority: P3
- Common dimensions: 
- Aliases: TnS Private Sender Conv Level
- Notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: private-chat only.
- Review note: 

## TnS DM Private Sender Metrics - Msg Level
- [x] Review
- Chinese description: 私信私聊发送端消息层指标组，用于观察发送端消息层面的申诉与审核表现。
- English description: A DM private-sender message-level metric group used to observe appeal and review behaviors on the sending side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety sender-side review layer at message level
- Priority: P3
- Common dimensions: 
- Aliases: TnS Private Sender Msg Level
- Notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary. Surface note: private-chat only.
- Review note: 

## TnS DM Private Receiver Metrics - Msg Level
- [x] Review
- Chinese description: 私信私聊接收端消息层指标组，用于观察接收端消息层面的申诉与审核表现。
- English description: A DM private-receiver message-level metric group used to observe appeal and review behaviors on the receiving side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety receiver-side review layer at message level
- Priority: P3
- Common dimensions: 
- Aliases: TnS Private Receiver Msg Level
- Notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: private-chat only.
- Review note: 

## TnS DM Group Chat Sender Metrics - Conv Level
- [x] Review
- Chinese description: 私信群聊发送端会话层指标组，用于观察群聊发送端会话层面的通知与申诉表现。
- English description: A DM group-chat sender conversation-level metric group used to observe notification and appeal behaviors on the sending side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety sender-side review layer for group chat
- Priority: P3
- Common dimensions: 
- Aliases: TnS Group Chat Sender Conv Level
- Notes: Confirmed from the live Libra watched-group list; concrete metrics are already formalized in the glossary. Surface note: group-chat only.
- Review note: 

## TnS DM Group Chat Sender Metrics - Msg Level
- [x] Review
- Chinese description: 私信群聊发送端消息层指标组，用于观察群聊发送端消息层面的申诉表现。
- English description: A DM group-chat sender message-level metric group used to observe appeal behavior on the sending side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety sender-side review layer at message level for group chat
- Priority: P3
- Common dimensions: 
- Aliases: TnS Group Chat Sender Msg Level
- Notes: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary. Surface note: group-chat only.
- Review note: 

## TnS DM Group Chat Receiver Metrics - Msg Level
- [x] Review
- Chinese description: 私信群聊接收端消息层指标组，用于观察群聊接收端消息层面的申诉表现。
- English description: A DM group-chat receiver message-level metric group used to observe appeal behavior on the receiving side.
- Scope: social / DM / TnS
- Business domain: DM Safety
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a trust-and-safety receiver-side review layer at message level for group chat
- Priority: P3
- Common dimensions: 
- Aliases: TnS Group Chat Receiver Msg Level
- Notes: Confirmed from the live Libra watched-group list; formal metric entries are still pending. Surface note: group-chat only.
- Review note: 

## DM Growth Pairs-Key Metrics
- [x] Review
- Chinese description: 私信增长对相关核心指标组，用于观察增长对场景下的关键健康表现。
- English description: A growth-pairs key-metrics group used to observe core health signals in growth-pairs scenarios.
- Scope: social / DM / growth pairs
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture core health in growth-pairs scenarios
- Priority: P3
- Common dimensions: 
- Aliases: Growth Pairs Key Metrics
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## DM Growth Pairs-Active Days
- [x] Review
- Chinese description: 私信增长对活跃天数相关指标组，用于观察增长对用户活跃天数的影响。
- English description: A growth-pairs active-days metric group used to observe effects on active-day coverage.
- Scope: social / DM / growth pairs
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture activity coverage in growth-pairs scenarios
- Priority: P3
- Common dimensions: 
- Aliases: Growth Pairs Active Days
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## DM Growth Pairs- Retention
- [x] Review
- Chinese description: 私信增长对留存相关指标组，用于观察增长对用户留存表现的影响。
- English description: A growth-pairs retention metric group used to observe effects on retention behavior.
- Scope: social / DM / growth pairs
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture retention in growth-pairs scenarios
- Priority: P3
- Common dimensions: 
- Aliases: Growth Pairs Retention
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## Muf Growth DM Pairs By time
- [x] Review
- Chinese description: 按时间切分的 MUF 增长对指标组，用于观察增长对私信对关系在时间维度上的变化。
- English description: A time-sliced MUF growth-pairs metric group used to observe temporal changes in DM pair behavior.
- Scope: social / DM / growth pairs
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture time-sliced change in MUF-linked growth-pair behavior
- Priority: P3
- Common dimensions: 
- Aliases: MUF Growth DM Pairs By Time
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is MUF/pair-based.
- Review note: 

## Inbox Element Metrics
- [x] Review
- Chinese description: Inbox 元素相关指标组，用于观察 Inbox 页面元素的曝光、点击与使用表现。
- English description: An inbox-element metric group used to observe exposure, click, and usage behaviors of inbox elements.
- Scope: social / DM adjacent mechanics / inbox
- Business domain: Inbox
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture inbox-surface element exposure and interaction behavior
- Priority: P3
- Common dimensions: 
- Aliases: Inbox Elements
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface group.
- Review note: 

## Inbox element metrics uid
- [x] Review
- Chinese description: Inbox 元素用户级指标组，用于观察用户维度的 Inbox 元素使用表现。
- English description: An inbox-element user-level metric group used to observe user-level usage of inbox elements.
- Scope: social / DM adjacent mechanics / inbox
- Business domain: Inbox
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture user-level interaction with inbox-surface elements
- Priority: P3
- Common dimensions: 
- Aliases: Inbox Element Metrics UID
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface group.
- Review note: 

## Inbox message metrics uid
- [x] Review
- Chinese description: Inbox 消息用户级指标组，用于观察用户维度的 Inbox 消息表现。
- English description: An inbox-message user-level metric group used to observe user-level inbox-message behaviors.
- Scope: social / DM adjacent mechanics / inbox
- Business domain: Inbox
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture user-level inbox message exposure and interaction behavior
- Priority: P3
- Common dimensions: 
- Aliases: Inbox Message Metrics UID
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent inbox context; not a single chat-surface group.
- Review note: 

## [B2C] Business Message Key Metrics
- [x] Review
- Chinese description: B2C 业务消息核心指标组，用于观察业务消息的关键健康表现。
- English description: A B2C business-message key-metrics group used to observe core health behaviors for business messages.
- Scope: social / DM / B2C messaging
- Business domain: DM B2C
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a core health layer for business-messaging scenarios
- Priority: P2
- Common dimensions: 
- Aliases: Business Message Key Metrics
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: B2C messaging surface; do not force it into private-chat or group-chat by default.
- Review note: 

## [DM] Active Status
- [x] Review
- Chinese description: 私信活跃状态指标组，用于观察活跃状态相关表现。
- English description: A DM active-status metric group used to observe active-status related behaviors.
- Scope: social / DM / activity
- Business domain: Active Status
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture DM-side activity-status and engagement-state signals
- Priority: P3
- Common dimensions: 
- Aliases: Active Status
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM by Entrance
- [x] Review
- Chinese description: 私信按入口切分的指标组，用于观察不同入口来源下的发送、进入与互动表现。
- English description: A DM by-entrance metric group used to observe sending, entry, and interaction behaviors by entrance source.
- Scope: social / DM / by entrance
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture entrance-sliced variation across DM surfaces
- Priority: P0
- Common dimensions: By Entrance
- Aliases: DM by Entrance; By Entrance
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
- Review note: 

## [DM] DM by Msg Type
- [x] Review
- Chinese description: 私信按消息类型切分的指标组，用于观察不同消息类型下的发送、互动与转化表现。
- English description: A DM by-message-type metric group used to observe sending, interaction, and conversion behaviors by message type.
- Scope: social / DM / by message type
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture message-type-sliced variation across DM surfaces
- Priority: P0
- Common dimensions: By Msg Type
- Aliases: DM by Message Type; By Msg Type
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
- Review note: 

## [DM] DM Quality & Reply Rates
- [x] Review
- Chinese description: 私信质量与回复率相关指标组，用于观察回复质量、回复率和会话互动体验。
- English description: A DM quality-and-reply-rates metric group used to observe reply quality, reply rates, and chat interaction experience.
- Scope: social / DM / experience
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture reply quality and conversational responsiveness
- Priority: P1
- Common dimensions: 
- Aliases: DM Quality; Reply Rates
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Quality & Reply Rates New
- [x] Review
- Chinese description: 私信质量与回复率的新口径指标组，用于观察更新后的质量与回复表现。
- English description: A DM quality-and-reply-rates-new metric group used to observe updated quality and reply behaviors.
- Scope: social / DM / experience
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture updated reply quality and conversational responsiveness
- Priority: P1
- Common dimensions: 
- Aliases: DM Quality New; Reply Rates New
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat unless the source table narrows it.
- Review note: 

## [DM] DM Receive New
- [x] Review
- Chinese description: 私信接收侧新口径指标组，用于观察接收链路的新版本指标表现。
- English description: A DM receive-new metric group used to observe the updated receive-side metric set.
- Scope: social / DM / receive
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture updated receive-side behavior across DM surfaces
- Priority: P3
- Common dimensions: 
- Aliases: DM Receive New; Receive New
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: both private-chat and group-chat by default.
- Review note: 

## [DM] DM Group Chat by Msg Type
- [x] Review
- Chinese description: 私信群聊按消息类型切分的指标组，用于观察群聊场景下不同消息类型的互动表现。
- English description: A DM group-chat metric group split by message type, used to observe interaction behaviors by message type in group chats.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture message-type-sliced variation in group-chat behavior
- Priority: P2
- Common dimensions: By Msg Type
- Aliases: DM Group Chat by Msg Type; Group Chat by Msg Type
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 3d Retention
- [x] Review
- Chinese description: 私信群聊 3 日留存正式存储位置。
- English description: Formal storage location for DM group-chat 3-day retention metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 3d Retention
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 7d Retention
- [x] Review
- Chinese description: 私信群聊 7 日留存正式存储位置。
- English description: Formal storage location for DM group-chat 7-day retention metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 7d Retention
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 14d Retention
- [x] Review
- Chinese description: 私信群聊 14 日留存正式存储位置。
- English description: Formal storage location for DM group-chat 14-day retention metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 14d Retention
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 28d Retention
- [x] Review
- Chinese description: 私信群聊 28 日留存正式存储位置。
- English description: Formal storage location for DM group-chat 28-day retention metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 28d Retention
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 3d Retention New gt3-users
- [x] Review
- Chinese description: 私信群聊新口径 3 日留存（gt3-users）正式存储位置。
- English description: Formal storage location for DM group-chat 3-day retention (gt3-users) metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: updated group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 3d Retention New gt3-users
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 7d Retention New gt3-users
- [x] Review
- Chinese description: 私信群聊新口径 7 日留存（gt3-users）正式存储位置。
- English description: Formal storage location for DM group-chat 7-day retention (gt3-users) metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: updated group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 7d Retention New gt3-users
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 14d Retention New gt3-users
- [x] Review
- Chinese description: 私信群聊新口径 14 日留存（gt3-users）正式存储位置。
- English description: Formal storage location for DM group-chat 14-day retention (gt3-users) metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: updated group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 14d Retention New gt3-users
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] DM Group Chat 28d Retention New gt3-users
- [x] Review
- Chinese description: 私信群聊新口径 28 日留存（gt3-users）正式存储位置。
- English description: Formal storage location for DM group-chat 28-day retention (gt3-users) metrics.
- Scope: social / DM / group chat
- Business domain: DM Group Chat
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: updated group-chat retention bucket
- Priority: P2
- Common dimensions: 
- Aliases: DM Group Chat 28d Retention New gt3-users
- Notes: Confirmed from the live Libra watched-group list. Surface note: group-chat only.
- Review note: 

## [DM] MuF DM Lifecycle
- [x] Review
- Chinese description: 私信 MUF 生命周期指标组，用于记录生命周期相关正式指标。
- English description: A DM MUF lifecycle metric group used to store formal lifecycle-related metrics.
- Scope: social / DM / lifecycle
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture lifecycle-stage change in MUF-linked DM behavior
- Priority: P1
- Common dimensions: 
- Aliases: MuF DM Lifecycle; DM Lifecycle
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is MUF-based.
- Review note: 

## internal share funnel metrics
- [x] Review
- Chinese description: 站内分享漏斗相关指标组，用于记录站内分享漏斗正式指标。
- English description: An internal-share funnel metric group used to store formal metrics for the in-app sharing funnel.
- Scope: social / DM adjacent mechanics / share
- Business domain: Share&Repost
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture broad in-app sharing funnel behavior
- Priority: P3
- Common dimensions: 
- Aliases: Internal Share Funnel Metrics; internal share funnel
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
- Review note: 

## internal share search funnel metrics
- [x] Review
- Chinese description: 站内分享搜索漏斗相关指标组，用于记录站内分享搜索漏斗正式指标。
- English description: An internal-share search-funnel metric group used to store formal metrics for the in-app sharing search funnel.
- Scope: social / DM adjacent mechanics / share
- Business domain: Share&Repost
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture in-app sharing search-funnel behavior
- Priority: P3
- Common dimensions: 
- Aliases: Internal Share Search Funnel Metrics; internal share search funnel
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
- Review note: 

## Core Interaction Growth Pairs-Active Days
- [x] Review
- Chinese description: 核心互动增长对活跃天数指标组，用于记录核心互动增长对的活跃天数正式指标。
- English description: A core-interaction growth-pairs active-days metric group used to store formal active-days metrics for core interaction growth pairs.
- Scope: social / core interaction
- Business domain: Core Interaction
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture active-day coverage in core-interaction growth pairs
- Priority: P3
- Common dimensions: 
- Aliases: Core Interaction Growth Pairs Active Days
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## Core Interaction Growth Pairs- Retention
- [x] Review
- Chinese description: 核心互动增长对留存指标组，用于记录核心互动增长对的留存正式指标。
- English description: A core-interaction growth-pairs retention metric group used to store formal retention metrics for core interaction growth pairs.
- Scope: social / core interaction
- Business domain: Core Interaction
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture retention in core-interaction growth pairs
- Priority: P3
- Common dimensions: 
- Aliases: Core Interaction Growth Pairs Retention
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: private-chat only, because this group is pair-based.
- Review note: 

## Internal Share To Chat
- [x] Review
- Chinese description: 站内分享到聊天相关指标组，用于记录从分享流转到聊天的正式指标。
- English description: An internal-share-to-chat metric group used to store formal metrics for share-to-chat behavior.
- Scope: social / DM adjacent mechanics / share
- Business domain: Share&Repost
- Company core: 1
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture share-to-chat transition behavior
- Priority: P4
- Common dimensions: 
- Aliases: Internal Share to Chat; Share To Chat
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: DM-adjacent sharing context; broader than a single DM surface.
- Review note: 

## [DM] DM 2-Way
- [x] Review
- Chinese description: 私信双向互动指标组，用于观察双向发送或点赞链路的覆盖、强度与会话表现。
- English description: A DM two-way interaction metric group used to observe coverage, intensity, and session-level behavior for bidirectional send-or-like activity.
- Scope: social / DM / two-way
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture bidirectional interaction strength across DM surfaces
- Priority: P1
- Common dimensions: 
- Aliases: DM 2-Way; 2-Way
- Notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: mixed; current metrics include group-chat, MUF, and broad DM two-way variants.
- Review note: 

## [DM] MuF DM by Motivation
- [x] Review
- Chinese description: 按 MUF 动机拆分的私信指标组，用于观察动机维度下的活跃、分享与互动表现。
- English description: A DM metric group split by MUF motivation, used to observe active, share, and interaction behaviors under motivation dimensions.
- Scope: social / DM / muf
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture motivation-sliced behavior in MUF-linked DM scenarios
- Priority: P0
- Common dimensions: 
- Aliases: MuF DM by Motivation; Muf DM by Motivation
- Notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, because this group is MUF-based.
- Review note: 

## [DM] Muf DM Enter From as Dim
- [x] Review
- Chinese description: 按进入来源拆分的 MUF 私信指标组，用于观察不同入口来源下的发送或点赞表现。
- English description: A DM MUF metric group split by entry source, used to observe send-or-like behaviors under different entry sources.
- Scope: social / DM / muf
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture entry-source variation in MUF-linked DM behavior
- Priority: P1
- Common dimensions: 
- Aliases: Muf DM Enter From as Dim; DM Enter From
- Notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, because this group is MUF/pair-based.
- Review note: 

## [DM] Muf DM Msg Type as Dim
- [x] Review
- Chinese description: 按消息类型拆分的 MUF 私信指标组，用于观察不同消息类型下的发送或点赞表现。
- English description: A DM MUF metric group split by message type, used to observe send-or-like behaviors under different message types.
- Scope: social / DM / muf
- Business domain: DM
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used to capture message-type variation in MUF-linked DM behavior
- Priority: P1
- Common dimensions: 
- Aliases: Muf DM Msg Type as Dim; DM Msg Type
- Notes: Confirmed from the live Libra watched-group list and extracted report rows. Surface note: private-chat only, because this group is MUF/pair-based.
- Review note: 

## [B2C] Creator Message Key Metrics
- [x] Review
- Chinese description: 创作者消息核心指标组，用于观察创作者消息的关键健康表现。
- English description: A creator-message key-metrics group used to observe core health behaviors for creator messaging.
- Scope: social / DM / B2C messaging
- Business domain: DM B2C
- Company core: 0
- Business core: 1
- Sub-business core: 1
- Typical usage: used as a creator-messaging core health layer
- Priority: P2
- Common dimensions: 
- Aliases: Creator Message Key Metrics
- Notes: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later. Surface note: B2C messaging surface; do not force it into private-chat or group-chat by default.
- Review note:
