# Metric Group Review Draft | 指标组人工评审稿

- Source: `references/knowledge/glossary/metric_groups.md`
- Total groups: **75**
- Review usage: 每个条目先看中文解释、适用范围、核心级别和常见维度；如有问题直接在条目下补意见。
- Review mark: `- [ ] Review` = 待确认；你 review 后可以手动改成 `- [x] Review`。

## Summary | 汇总视图

- review_status `group_name` | 优先级 `priority_hint` | 范围 `usage_scope`
- [x] `DM Core` | 优先级 `P0` | 范围 `social / DM / direct message`
- [x] `DM Voice Message` | 优先级 `P1` | 范围 `social/ DM / voice message`
- [x] `[DM] DM Camera` | 优先级 `P1` | 范围 `social/DM / camera`
- [x] `[DM] DM Camera by Entrance` | 优先级 `P2` | 范围 `social/DM / camera`
- [x] `[DM] DM Camera Private Chat` | 优先级 `P2` | 范围 `social/DM / camera`
- [x] `[DM] DM Camera Private Chat by Entrance` | 优先级 `P2` | 范围 `social/DM / camera`
- [x] `[DM] DM Camera Group Chat` | 优先级 `P2` | 范围 `social/DM / camera`
- [x] `[DM] DM Camera Group Chat by Entrance` | 优先级 `P2` | 范围 `social/DM / camera`
- [x] `DM Group Chat` | 优先级 `P0` | 范围 `social / DM / group chat`
- [x] `[DM] DM Receive` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Permission` | 优先级 `P1` | 范围 `social / DM / safety`
- [x] `[DM] DM Send & Load Fail` | 优先级 `P1` | 范围 `social / DM / experience`
- [x] `[DM] DM Leave Chat` | 优先级 `P2` | 范围 `social / DM / experience`
- [x] `[DM] DM Core Performance - Latency` | 优先级 `P1` | 范围 `social / DM / experience`
- [x] `[DM] DM Inner Push` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Outer Push` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Sticker` | 优先级 `P1` | 范围 `social / DM / sticker`
- [x] `[DM] DM Streak` | 优先级 `P1` | 范围 `social / DM / streaks`
- [x] `[DM] DM Conversion Funnel` | 优先级 `P1` | 范围 `social / DM / funnel`
- [x] `[DM] DM Message Pairs` | 优先级 `P1` | 范围 `social / DM / pairs`
- [x] `[DM] DM by Link` | 优先级 `P2` | 范围 `social / DM / link`
- [x] `Internal Share All` | 优先级 `P0` | 范围 `social / share`
- [x] `DM Quick Share` | 优先级 `P2` | 范围 `social / DM / share`
- [x] `DM_Share_Type | direct message share type` | 优先级 `P2` | 范围 `social / DM / share`
- [x] `Key Project-DM` | 优先级 `P0` | 范围 `social/ DM / direct message`
- [x] `[DM] DM Negative Feedback` | 优先级 `P1` | 范围 `social / DM / safety`
- [x] `[DM] DM Core Performance - Android` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Core Performance - iOS` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `Core-Active Days` | 优先级 `P0` | 范围 `social / core health`
- [x] `Active Hours (HLT)` | 优先级 `context_dependent` | 范围 `social / core health`
- [x] `Core-Publish Days` | 优先级 `P0` | 范围 `social / core health`
- [x] `Core-Key Metrics` | 优先级 `P1` | 范围 `social / core health`
- [x] `Activity Status Metrics` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `Activity Status User Metrics` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `TnS DM Private Sender Metrics - Conv Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `TnS DM Private Sender Metrics - Msg Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `TnS DM Private Receiver Metrics - Msg Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `TnS DM Group Chat Sender Metrics - Conv Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `TnS DM Group Chat Sender Metrics - Msg Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `TnS DM Group Chat Receiver Metrics - Msg Level` | 优先级 `P1` | 范围 `social / DM / TnS`
- [x] `DM Growth Pairs-Key Metrics` | 优先级 `P1` | 范围 `social / DM / growth pairs`
- [x] `DM Growth Pairs-Active Days` | 优先级 `P1` | 范围 `social / DM / growth pairs`
- [x] `DM Growth Pairs- Retention` | 优先级 `P1` | 范围 `social / DM / growth pairs`
- [x] `Muf Growth DM Pairs By time` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `Inbox Element Metrics` | 优先级 `P1` | 范围 `social / inbox`
- [x] `Inbox element metrics uid` | 优先级 `P1` | 范围 `social / inbox`
- [x] `Inbox message metrics uid` | 优先级 `P1` | 范围 `social / inbox`
- [x] `[B2C] Business Message Key Metrics` | 优先级 `P1` | 范围 `social / DM / B2C messaging`
- [x] `[DM] Active Status` | 优先级 `P1` | 范围 `social / DM / activity`
- [x] `[DM] DM by Entrance` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM by Msg Type` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Quality & Reply Rates` | 优先级 `P1` | 范围 `social / DM / experience`
- [x] `[DM] DM Quality & Reply Rates New` | 优先级 `P1` | 范围 `social / DM / experience`
- [x] `[DM] DM Receive New` | 优先级 `P1` | 范围 `social / DM / direct message`
- [x] `[DM] DM Group Chat by Msg Type` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 3d Retention` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 7d Retention` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 14d Retention` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 28d Retention` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 3d Retention New gt3-users` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 7d Retention New gt3-users` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 14d Retention New gt3-users` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] DM Group Chat 28d Retention New gt3-users` | 优先级 `P1` | 范围 `social/DM / group chat`
- [x] `[DM] MuF DM Lifecycle` | 优先级 `P1` | 范围 `social / DM / lifecycle`
- [x] `Quick Share Recall | Quick Share Recall` | 优先级 `P1` | 范围 `social / share`
- [x] `internal share funnel metrics` | 优先级 `P1` | 范围 `social / share`
- [x] `internal share search funnel metrics` | 优先级 `P1` | 范围 `social / share`
- [x] `Core Interaction Growth Pairs-Active Days` | 优先级 `P1` | 范围 `social / core interaction`
- [x] `Core Interaction Growth Pairs- Retention` | 优先级 `P1` | 范围 `social / core interaction`
- [x] `Internal Share To Chat` | 优先级 `P1` | 范围 `social / share`
- [x] `[DM] DM 2-Way` | 优先级 `P1` | 范围 `social/ DM / direct message`
- [x] `[DM] MuF DM by Motivation` | 优先级 `P1` | 范围 `social / DM / muf`
- [x] `[DM] Muf DM Enter From as Dim` | 优先级 `P1` | 范围 `social / DM / muf`
- [x] `[DM] Muf DM Msg Type as Dim` | 优先级 `P1` | 范围 `social / DM / muf`
- [x] `[B2C] Creator Message Key Metrics` | 优先级 `P1` | 范围 `social / DM / B2C messaging`

## Full Review Entries | 完整评审条目

### DM Core

- [x] Review
- 中文描述: 私信核心使用行为指标组，覆盖私聊和群聊场景，通常用于观察进入会话、停留、发送等主链路行为。
- English summary: A core DM usage metric group covering both private-chat and group-chat scenarios, usually used to observe entering chat, staying, and sending behaviors.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `true`
- 常见用途: （空）
- 优先级: `P0`
- 常见维度: （空）
- 备注: Use dimensions only when they are explicitly present in the raw data or source table.
- Review note: （空）

### DM Voice Message

- [x] Review
- 中文描述: 私信语音消息相关指标组，通常用于观察语音录制、取消、发送等行为。
- English summary: A DM voice-message metric group that usually covers recording, canceling, and sending voice messages.
- 使用范围: `social/ DM / voice message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: （空）
- 优先级: `P1`
- 常见维度: By Msg Type
- 备注: （空）
- Review note: （空）

### [DM] DM Camera

- [x] Review
- 中文描述: 私信相机消息相关指标组，用于观察 DM Camera 的发送、上传、拍摄页进入等链路表现。
- English summary: A DM camera-message metric group used to observe sending, upload, and shoot-page entry behaviors for DM Camera.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: （空）
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed in the shared formal glossary as a reusable DM camera group.
- Review note: （空）

### [DM] DM Camera by Entrance

- [x] Review
- 中文描述: 私信相机按入口切分的指标组，用于观察不同入口来源下的相机链路表现。
- English summary: A DM camera metric group split by entrance source, used to observe camera-path behaviors by entrance source.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: （空）
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Camera Private Chat

- [x] Review
- 中文描述: 私信相机私聊指标组，用于观察私聊场景下的相机链路表现。
- English summary: A DM camera metric group for private-chat scenarios, used to observe camera-path behaviors in private chat.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: （空）
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Camera Private Chat by Entrance

- [x] Review
- 中文描述: 私信相机私聊按入口切分的指标组，用于观察私聊场景下不同入口的相机链路表现。
- English summary: A DM camera metric group for private-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a private-chat camera supporting group in DM experiments
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Camera Group Chat

- [x] Review
- 中文描述: 私信相机群聊指标组，用于观察群聊场景下的相机链路表现。
- English summary: A DM camera metric group for group-chat scenarios, used to observe camera-path behaviors in group chat.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a group-chat camera supporting group in DM experiments
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Camera Group Chat by Entrance

- [x] Review
- 中文描述: 私信相机群聊按入口切分的指标组，用于观察群聊场景下不同入口的相机链路表现。
- English summary: A DM camera metric group for group-chat scenarios split by entrance source, used to observe camera-path behaviors by entrance.
- 使用范围: `social/DM / camera`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a group-chat camera supporting group in DM experiments
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### DM Group Chat

- [x] Review
- 中文描述: 私信群聊相关指标组，通常用于观察群聊进入、发送、互动与创建行为。
- English summary: A DM group-chat metric group that usually covers entering, sending, interacting, and creating group chats.
- 使用范围: `social / DM / group chat`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `true`
- 常见用途: used to capture group-chat effects directly within DM experiments
- 优先级: `P0`
- 常见维度: By Entrance | By Motivation | By Msg Type
- 备注: （空）
- Review note: （空）

### [DM] DM Receive

- [x] Review
- 中文描述: 私信接收侧指标组，用于观察接收消息、被动互动、接收链路相关表现。
- English summary: A DM receive-side metric group used to observe received-message and receive-side interaction behaviors.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a receive-side supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Permission

- [x] Review
- 中文描述: 私信权限与陌生人消息机制指标组，用于理解谁可发起请求、消息请求权限等安全机制。
- English summary: A DM permission and stranger-message metric group used to understand request permissions and safety mechanisms.
- 使用范围: `social / DM / safety`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a safety / privacy supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the shared formal glossary and live Libra group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Send & Load Fail

- [x] Review
- 中文描述: 私信发送与加载失败指标组，用于观察发送失败、加载失败及相关体验风险。
- English summary: A DM send-and-load-failure metric group used to observe send failures, load failures, and related experience risks.
- 使用范围: `social / DM / experience`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a failure / risk supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Leave Chat

- [x] Review
- 中文描述: 私信离开会话相关指标组，用于观察用户退出聊天链路的行为表现。
- English summary: A DM leave-chat metric group used to observe chat-exit behaviors.
- 使用范围: `social / DM / experience`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a supporting risk or engagement group in DM experiments
- 优先级: `P2`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Core Performance - Latency

- [x] Review
- 中文描述: 私信核心性能延迟相关指标组，用于记录更泛化的延迟口径正式指标。
- English summary: A DM core-performance latency metric group used to store formal latency metrics under the DM core-performance umbrella.
- 使用范围: `social / DM / experience`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a performance-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Msg Type
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Inner Push

- [x] Review
- 中文描述: 私信站内推送相关指标组，用于观察站内触达、提醒与召回链路表现。
- English summary: A DM in-app push metric group used to observe in-app reach, reminder, and recall behaviors.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a supporting reach/retention group in DM experiments
- 优先级: `P1`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Outer Push

- [x] Review
- 中文描述: 私信站外推送相关指标组，用于观察站外触达、召回与回流链路表现。
- English summary: A DM out-of-app push metric group used to observe off-app reach, recall, and re-entry behaviors.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a supporting reach/retention group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Sticker

- [x] Review
- 中文描述: 私信贴纸消息相关指标组，用于观察贴纸的发送、消费与使用表现。
- English summary: A DM sticker metric group used to observe sticker sending, consumption, and usage behaviors.
- 使用范围: `social / DM / sticker`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a feature-specific supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Streak

- [x] Review
- 中文描述: 私信火花玩法相关指标组，用于观察 streak / 火花在私聊和群聊中的建立、维持与互动表现。
- English summary: A DM streak (fire-badge) metric group used to observe streak creation, maintenance, and interaction behaviors across both private chats and group chats.
- 使用范围: `social / DM / streaks`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `true`
- 常见用途: used for DM streak / flame-play effects across both private-chat and group-chat scenarios
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Conversion Funnel

- [x] Review
- 中文描述: 私信转化漏斗相关指标组，用于观察从曝光到进入、发送、互动等转化链路表现。
- English summary: A DM conversion-funnel metric group used to observe conversion from exposure to entry, sending, and interaction.
- 使用范围: `social / DM / funnel`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `true`
- 常见用途: often used as a funnel support group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Message Pairs

- [x] Review
- 中文描述: 私信消息对相关指标组，用于观察私聊场景下的消息对、双向互动或 pair 结构表现。
- English summary: A DM message-pairs metric group used to observe message-pair and bidirectional interaction behaviors in private-chat scenarios.
- 使用范围: `social / DM / pairs`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a relationship-strength supporting group in private-chat experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM by Link

- [x] Review
- 中文描述: 私信链接相关指标组，用于观察链接发送、点击和转化等链路表现。
- English summary: A DM by-link metric group used to observe link sending, clicking, and conversion behaviors.
- 使用范围: `social / DM / link`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a feature-specific supporting group in DM experiments
- 优先级: `P2`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Internal Share All

- [x] Review
- 中文描述: 站内分享全链路指标组，用于观察站内分享的发送、覆盖与转化表现，覆盖 share video、share comment、share profile page 等全题材分享。
- English summary: An internal-share metric group used to observe send, coverage, and conversion behaviors across broad in-app share types such as share video, share comment, and share profile page.
- 使用范围: `social / share`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `true`
- 常见用途: often used as a broad internal-share supporting or guardrail group in social experiments
- 优先级: `P0`
- 常见维度: （空）
- 备注: Confirmed from the shared formal glossary and live Libra watched-group list.
- Review note: （空）

### DM Quick Share

- [x] Review
- 中文描述: 私信快捷分享相关指标组，用于观察快速分享链路的使用表现。
- English summary: A DM quick-share metric group used to observe quick-share usage behaviors.
- 使用范围: `social / DM / share`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a feature-specific supporting group in DM experiments
- 优先级: `P2`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### DM_Share_Type | direct message share type

- [x] Review
- 中文描述: 私信分享类型相关指标组，用于观察不同分享类型的分布与转化表现。
- English summary: A DM share-type metric group used to observe the distribution and conversion of share types.
- 使用范围: `social / DM / share`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a sharing-behavior supporting group in DM experiments
- 优先级: `P2`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Key Project-DM

- [x] Review
- 中文描述: 私信核心业务交互指标组，通常覆盖发送、点赞、接收、分享等更宽口径的互动信号。
- English summary: A DM core interaction metric group that usually covers sending, liking, receiving, and sharing signals.
- 使用范围: `social/ DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a business-core supporting group in DM experiments
- 优先级: `P0`
- 常见维度: （空）
- 备注: Confirmed in the shared formal glossary as a reusable DM interaction group.
- Review note: （空）

### [DM] DM Negative Feedback

- [x] Review
- 中文描述: 私信负反馈与举报类指标组，通常用于观察拉黑、静音、取消静音、举报点击与举报用户等风险信号。
- English summary: A DM negative-feedback metric group that usually covers block, mute, unmute, and report-related risk signals.
- 使用范围: `social / DM / safety`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a risk / guardrail group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the current experiment report and live Libra group list as a reusable risk group.
- Review note: （空）

### [DM] DM Core Performance - Android

- [x] Review
- 中文描述: 私信 Android 端核心性能指标组，通常用于观察聊天列表、聊天房间、发送链路的加载时延与卡顿风险。
- English summary: A DM Android performance metric group that usually covers chat-list, chat-room, and send-path latency and frame-drop risks.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `false`
- 子业务核心: `false`
- 常见用途: often used as a platform-performance guardrail group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the current experiment report as an Android performance guardrail group.
- Review note: （空）

### [DM] DM Core Performance - iOS

- [x] Review
- 中文描述: 私信 iOS 端核心性能指标组，通常用于观察聊天房间等关键链路的加载时延风险。
- English summary: A DM iOS performance metric group that usually covers latency risk in key DM paths such as the chat room.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a platform-performance guardrail group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the current experiment report as an iOS performance guardrail group.
- Review note: （空）

### Core-Active Days

- [x] Review
- 中文描述: TikTok 核心活跃天数指标组，用来描述用户在给定回看窗口内的活跃覆盖情况。
- English summary: A TikTok core metric group that describes user activity coverage over a lookback window.
- 使用范围: `social / core health`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a core health or guardrail group in social experiments
- 优先级: `P0`
- 常见维度: （空）
- 备注: Confirmed from the live Libra metric-group list and the shared formal glossary.
- Review note: （空）

### Active Hours (HLT)

- [x] Review
- 中文描述: TikTok 核心活跃时长指标组，用来描述用户在给定回看窗口内的人均使用深度。
- English summary: A TikTok core metric group that describes user depth of usage over a lookback window.
- 使用范围: `social / core health`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a core health or time-spent supporting group in social experiments
- 优先级: `context_dependent`
- 常见维度: （空）
- 备注: Confirmed from the live Libra metric-group list and the shared formal glossary.
- Review note: （空）

### Core-Publish Days

- [x] Review
- 中文描述: TikTok 创作发布相关指标组，用于描述用户在给定回看窗口内的发布覆盖情况。
- English summary: A TikTok creation-related metric group that describes user publish coverage over a lookback window.
- 使用范围: `social / core health`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a creation or supply-side guardrail group in social experiments
- 优先级: `P0`
- 常见维度: （空）
- 备注: Confirmed in the shared formal glossary as a mandatory-recall core-health group.
- Review note: （空）

### Core-Key Metrics

- [x] Review
- 中文描述: TikTok 核心通用指标组，通常承载停留、发布、播放、完播、会话、登录与响应等基础健康信号。
- English summary: A TikTok core general metric group that usually covers stay, publish, play, finish, session, login, and response signals.
- 使用范围: `social / core health`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a core health supporting group across social experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed in the shared formal glossary as a reusable core-health group.
- Review note: （空）

### Activity Status Metrics

- [x] Review
- 中文描述: 私信活跃状态相关指标组，用于观察活跃状态和行为状态的总体变化。
- English summary: A DM activity-status metric group used to observe changes in active-status and behavior-status signals.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a supporting engagement group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
- Review note: （空）

### Activity Status User Metrics

- [x] Review
- 中文描述: 私信活跃状态用户级指标组，用于观察用户粒度的活跃状态变化。
- English summary: A DM activity-status user metric group used to observe user-level active-status changes.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a supporting user-level engagement group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
- Review note: （空）

### TnS DM Private Sender Metrics - Conv Level

- [x] Review
- 中文描述: 私信私聊发送端会话层指标组，用于观察发送端会话层面的申诉与审核表现。
- English summary: A DM private-sender conversation-level metric group used to observe appeal and review behaviors on the sending side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
- Review note: （空）

### TnS DM Private Sender Metrics - Msg Level

- [x] Review
- 中文描述: 私信私聊发送端消息层指标组，用于观察发送端消息层面的申诉与审核表现。
- English summary: A DM private-sender message-level metric group used to observe appeal and review behaviors on the sending side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary.
- Review note: （空）

### TnS DM Private Receiver Metrics - Msg Level

- [x] Review
- 中文描述: 私信私聊接收端消息层指标组，用于观察接收端消息层面的申诉与审核表现。
- English summary: A DM private-receiver message-level metric group used to observe appeal and review behaviors on the receiving side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
- Review note: （空）

### TnS DM Group Chat Sender Metrics - Conv Level

- [x] Review
- 中文描述: 私信群聊发送端会话层指标组，用于观察群聊发送端会话层面的通知与申诉表现。
- English summary: A DM group-chat sender conversation-level metric group used to observe notification and appeal behaviors on the sending side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; concrete metrics are already formalized in the glossary.
- Review note: （空）

### TnS DM Group Chat Sender Metrics - Msg Level

- [x] Review
- 中文描述: 私信群聊发送端消息层指标组，用于观察群聊发送端消息层面的申诉表现。
- English summary: A DM group-chat sender message-level metric group used to observe appeal behavior on the sending side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; one concrete metric is already formalized in the glossary.
- Review note: （空）

### TnS DM Group Chat Receiver Metrics - Msg Level

- [x] Review
- 中文描述: 私信群聊接收端消息层指标组，用于观察群聊接收端消息层面的申诉表现。
- English summary: A DM group-chat receiver message-level metric group used to observe appeal behavior on the receiving side.
- 使用范围: `social / DM / TnS`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a trust-and-safety supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries are still pending.
- Review note: （空）

### DM Growth Pairs-Key Metrics

- [x] Review
- 中文描述: 私信增长对相关核心指标组，用于观察增长对场景下的关键健康表现。
- English summary: A growth-pairs key-metrics group used to observe core health signals in growth-pairs scenarios.
- 使用范围: `social / DM / growth pairs`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a growth-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### DM Growth Pairs-Active Days

- [x] Review
- 中文描述: 私信增长对活跃天数相关指标组，用于观察增长对用户活跃天数的影响。
- English summary: A growth-pairs active-days metric group used to observe effects on active-day coverage.
- 使用范围: `social / DM / growth pairs`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a retention-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### DM Growth Pairs- Retention

- [x] Review
- 中文描述: 私信增长对留存相关指标组，用于观察增长对用户留存表现的影响。
- English summary: A growth-pairs retention metric group used to observe effects on retention behavior.
- 使用范围: `social / DM / growth pairs`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a retention-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Muf Growth DM Pairs By time

- [x] Review
- 中文描述: 按时间切分的 MUF 增长对指标组，用于观察增长对私信对关系在时间维度上的变化。
- English summary: A time-sliced MUF growth-pairs metric group used to observe temporal changes in DM pair behavior.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a time-sliced growth-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Inbox Element Metrics

- [x] Review
- 中文描述: Inbox 元素相关指标组，用于观察 Inbox 页面元素的曝光、点击与使用表现。
- English summary: An inbox-element metric group used to observe exposure, click, and usage behaviors of inbox elements.
- 使用范围: `social / inbox`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an inbox-supporting group in messaging experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Inbox element metrics uid

- [x] Review
- 中文描述: Inbox 元素用户级指标组，用于观察用户维度的 Inbox 元素使用表现。
- English summary: An inbox-element user-level metric group used to observe user-level usage of inbox elements.
- 使用范围: `social / inbox`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an inbox-supporting user-level group in messaging experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Inbox message metrics uid

- [x] Review
- 中文描述: Inbox 消息用户级指标组，用于观察用户维度的 Inbox 消息表现。
- English summary: An inbox-message user-level metric group used to observe user-level inbox-message behaviors.
- 使用范围: `social / inbox`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an inbox-supporting user-level group in messaging experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [B2C] Business Message Key Metrics

- [x] Review
- 中文描述: B2C 业务消息核心指标组，用于观察业务消息的关键健康表现。
- English summary: A B2C business-message key-metrics group used to observe core health behaviors for business messages.
- 使用范围: `social / DM / B2C messaging`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a business-messaging core-supporting group
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] Active Status

- [x] Review
- 中文描述: 私信活跃状态指标组，用于观察活跃状态相关表现。
- English summary: A DM active-status metric group used to observe active-status related behaviors.
- 使用范围: `social / DM / activity`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a supporting engagement group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM by Entrance

- [x] Review
- 中文描述: 私信按入口切分的指标组，用于观察不同入口来源下的发送、进入与互动表现。
- English summary: A DM by-entrance metric group used to observe sending, entry, and interaction behaviors by entrance source.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a slice-oriented supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Entrance
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM by Msg Type

- [x] Review
- 中文描述: 私信按消息类型切分的指标组，用于观察不同消息类型下的发送、互动与转化表现。
- English summary: A DM by-message-type metric group used to observe sending, interaction, and conversion behaviors by message type.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a slice-oriented supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Msg Type
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Quality & Reply Rates

- [x] Review
- 中文描述: 私信质量与回复率相关指标组，用于观察回复质量、回复率和会话互动体验。
- English summary: A DM quality-and-reply-rates metric group used to observe reply quality, reply rates, and chat interaction experience.
- 使用范围: `social / DM / experience`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an engagement-quality supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Quality & Reply Rates New

- [x] Review
- 中文描述: 私信质量与回复率的新口径指标组，用于观察更新后的质量与回复表现。
- English summary: A DM quality-and-reply-rates-new metric group used to observe updated quality and reply behaviors.
- 使用范围: `social / DM / experience`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an updated engagement-quality supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Receive New

- [x] Review
- 中文描述: 私信接收侧新口径指标组，用于观察接收链路的新版本指标表现。
- English summary: A DM receive-new metric group used to observe the updated receive-side metric set.
- 使用范围: `social / DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a receive-side supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Group Chat by Msg Type

- [x] Review
- 中文描述: 私信群聊按消息类型切分的指标组，用于观察群聊场景下不同消息类型的互动表现。
- English summary: A DM group-chat metric group split by message type, used to observe interaction behaviors by message type in group chats.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a slice-oriented supporting group in DM experiments
- 优先级: `P1`
- 常见维度: By Msg Type
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM Group Chat 3d Retention

- [x] Review
- 中文描述: 私信群聊 3 日留存正式存储位置。
- English summary: Formal storage location for DM group-chat 3-day retention metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 7d Retention

- [x] Review
- 中文描述: 私信群聊 7 日留存正式存储位置。
- English summary: Formal storage location for DM group-chat 7-day retention metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 14d Retention

- [x] Review
- 中文描述: 私信群聊 14 日留存正式存储位置。
- English summary: Formal storage location for DM group-chat 14-day retention metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 28d Retention

- [x] Review
- 中文描述: 私信群聊 28 日留存正式存储位置。
- English summary: Formal storage location for DM group-chat 28-day retention metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 3d Retention New gt3-users

- [x] Review
- 中文描述: 私信群聊新口径 3 日留存（gt3-users）正式存储位置。
- English summary: Formal storage location for DM group-chat 3-day retention (gt3-users) metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: updated group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 7d Retention New gt3-users

- [x] Review
- 中文描述: 私信群聊新口径 7 日留存（gt3-users）正式存储位置。
- English summary: Formal storage location for DM group-chat 7-day retention (gt3-users) metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: updated group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 14d Retention New gt3-users

- [x] Review
- 中文描述: 私信群聊新口径 14 日留存（gt3-users）正式存储位置。
- English summary: Formal storage location for DM group-chat 14-day retention (gt3-users) metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: updated group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] DM Group Chat 28d Retention New gt3-users

- [x] Review
- 中文描述: 私信群聊新口径 28 日留存（gt3-users）正式存储位置。
- English summary: Formal storage location for DM group-chat 28-day retention (gt3-users) metrics.
- 使用范围: `social/DM / group chat`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: updated group-chat retention bucket
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list.
- Review note: （空）

### [DM] MuF DM Lifecycle

- [x] Review
- 中文描述: 私信 MUF 生命周期指标组，用于记录生命周期相关正式指标。
- English summary: A DM MUF lifecycle metric group used to store formal lifecycle-related metrics.
- 使用范围: `social / DM / lifecycle`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a lifecycle supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Quick Share Recall | Quick Share Recall

- [x] Review
- 中文描述: 快捷分享召回相关指标组，用于记录召回链路正式指标。
- English summary: A quick-share recall metric group used to store formal metrics for the quick-share recall flow.
- 使用范围: `social / share`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a recall-supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### internal share funnel metrics

- [x] Review
- 中文描述: 站内分享漏斗相关指标组，用于记录站内分享漏斗正式指标。
- English summary: An internal-share funnel metric group used to store formal metrics for the in-app sharing funnel.
- 使用范围: `social / share`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a share-supporting group in social experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### internal share search funnel metrics

- [x] Review
- 中文描述: 站内分享搜索漏斗相关指标组，用于记录站内分享搜索漏斗正式指标。
- English summary: An internal-share search-funnel metric group used to store formal metrics for the in-app sharing search funnel.
- 使用范围: `social / share`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a share-supporting group in social experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Core Interaction Growth Pairs-Active Days

- [x] Review
- 中文描述: 核心互动增长对活跃天数指标组，用于记录核心互动增长对的活跃天数正式指标。
- English summary: A core-interaction growth-pairs active-days metric group used to store formal active-days metrics for core interaction growth pairs.
- 使用范围: `social / core interaction`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a growth-supporting retention group
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Core Interaction Growth Pairs- Retention

- [x] Review
- 中文描述: 核心互动增长对留存指标组，用于记录核心互动增长对的留存正式指标。
- English summary: A core-interaction growth-pairs retention metric group used to store formal retention metrics for core interaction growth pairs.
- 使用范围: `social / core interaction`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a growth-supporting retention group
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### Internal Share To Chat

- [x] Review
- 中文描述: 站内分享到聊天相关指标组，用于记录从分享流转到聊天的正式指标。
- English summary: An internal-share-to-chat metric group used to store formal metrics for share-to-chat behavior.
- 使用范围: `social / share`
- 公司核心: `true`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a share-to-chat supporting group
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）

### [DM] DM 2-Way

- [x] Review
- 中文描述: 私信双向互动指标组，用于观察双向发送或点赞链路的覆盖、强度与会话表现。
- English summary: A DM two-way interaction metric group used to observe coverage, intensity, and session-level behavior for bidirectional send-or-like activity.
- 使用范围: `social/ DM / direct message`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a supporting interaction-strength group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list and extracted report rows.
- Review note: （空）

### [DM] MuF DM by Motivation

- [x] Review
- 中文描述: 按 MUF 动机拆分的私信指标组，用于观察动机维度下的活跃、分享与互动表现。
- English summary: A DM metric group split by MUF motivation, used to observe active, share, and interaction behaviors under motivation dimensions.
- 使用范围: `social / DM / muf`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a motivation-split supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list and extracted report rows.
- Review note: （空）

### [DM] Muf DM Enter From as Dim

- [x] Review
- 中文描述: 按进入来源拆分的 MUF 私信指标组，用于观察不同入口来源下的发送或点赞表现。
- English summary: A DM MUF metric group split by entry source, used to observe send-or-like behaviors under different entry sources.
- 使用范围: `social / DM / muf`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as an entry-source supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list and extracted report rows.
- Review note: （空）

### [DM] Muf DM Msg Type as Dim

- [x] Review
- 中文描述: 按消息类型拆分的 MUF 私信指标组，用于观察不同消息类型下的发送或点赞表现。
- English summary: A DM MUF metric group split by message type, used to observe send-or-like behaviors under different message types.
- 使用范围: `social / DM / muf`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a message-type supporting group in DM experiments
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list and extracted report rows.
- Review note: （空）

### [B2C] Creator Message Key Metrics

- [x] Review
- 中文描述: 创作者消息核心指标组，用于观察创作者消息的关键健康表现。
- English summary: A creator-message key-metrics group used to observe core health behaviors for creator messaging.
- 使用范围: `social / DM / B2C messaging`
- 公司核心: `false`
- 业务核心: `true`
- 子业务核心: `true`
- 常见用途: often used as a creator-messaging core-supporting group
- 优先级: `P1`
- 常见维度: （空）
- 备注: Confirmed from the live Libra watched-group list; formal metric entries can be expanded later.
- Review note: （空）
