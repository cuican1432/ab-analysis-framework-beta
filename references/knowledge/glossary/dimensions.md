# Dimension Index | 维度索引

## Entry

```yaml
dimension_name: By Entrance
dimension_aliases:
  - 入口拆分

meaning_zh: 按入口来源拆分行为表现的维度。
meaning_en: A dimension that splits behavior by product entry source.

applies_to_groups:
  - DM Core
  - DM Group Chat

applies_to_metrics:

value_examples:
  - share
  - group_chat_entry
  - conversation_detail

warnings: Use this dimension to explain path differences, but do not let one entrance slice override the global result by itself.
```

## Entry

```yaml
dimension_name: By Msg Type
dimension_aliases:
  - 消息类型拆分

meaning_zh: 按消息类型拆分行为表现的维度，如 text、emoji、voice、sticker、camera。
meaning_en: A dimension that splits behavior by message type such as text, emoji, voice, sticker, or camera.

applies_to_groups:
  - DM Core
  - DM Voice Message

applies_to_metrics:

value_examples:
  - text
  - emoji
  - voice
  - sticker
  - camera

warnings: Useful for heterogeneity and expression-style analysis, but should remain supporting evidence unless the source strongly proves otherwise.
```

## Entry

```yaml
dimension_name: By Motivation
dimension_aliases:
  - 动机拆分

meaning_zh: 按互动或发送动机拆分表现的维度。
meaning_en: A dimension that splits performance by interaction or sending motivation.

applies_to_groups:
  - DM Core
  - DM Group Chat

applies_to_metrics:

value_examples:
  - social
  - share
  - creator_message

warnings: Motivation-based slices are useful for interpretation, but should be treated carefully when the source does not fully explain the classification logic.
```

## Entry

```yaml
dimension_name: Lookback Window
dimension_aliases:
  - time window
  - 回看窗口
  - 统计窗口

meaning_zh: 指标统计所采用的回看时间窗口，例如 1天、3天、7天、14天、30天。
meaning_en: The lookback window used by a metric, such as 1 day, 3 days, 7 days, 14 days, or 30 days.

applies_to_groups:
  - Core-Active Days
  - Active Hours (HLT)

applies_to_metrics:
  - Active Days
  - Last 1-day Active Days
  - Last 3-day Active Days
  - Last 7-day Active Days
  - Last 14-day Active Days
  - Last 30-day Active Days
  - HLT - active hours
  - HLT1-last 1-day active hours/U
  - HLT3-last 3-day active hours/U
  - HLT7-last 7-day active hours/U
  - HLT14-last 14-day active hours/U
  - HLT30-last 30-day active hours/U
  - valid_session_cnt/User
  - VS3-last 3-day ValidSession/U
  - VS7-last 7-day ValidSession/U
  - VS14-last 14-day ValidSession/U
  - VS30-last 30-day ValidSession/U

value_examples:
  - 1d
  - 3d
  - 7d
  - 14d
  - 30d

warnings: This is a caliber qualifier, not a business mechanism by itself.
```
