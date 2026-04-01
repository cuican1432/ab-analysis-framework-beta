# Metric Group Index | 指标组索引

## Entry

```yaml
group_name: DM Core
group_aliases:
  - 私信核心指标组

description_zh: 私信核心使用行为指标组，通常用于观察进入会话、停留、发送等主链路行为。
description_en: A core DM usage metric group that usually covers entering chat, staying, and sending behaviors.

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used as a business-core metric group in DM experiments
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

usage_scope: DM / direct message experiments
is_company_core:
is_business_core: true
is_sub_business_core: true

typical_usage: often used when a DM experiment may affect voice-message creation or usage
priority_hint: P1

common_dimensions:
  - By Msg Type

notes:
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

notes:
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
  - Lookback Window

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
  - Lookback Window

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
  - Lookback Window

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
  - Lookback Window

notes: Confirmed in the shared formal glossary as a reusable core-health group.
```
