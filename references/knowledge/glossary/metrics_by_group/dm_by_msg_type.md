# Metrics By Group | [DM] DM by Msg Type

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM by Msg Type.

## Metric: Send Camera Days/Days

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Camera Days/Days
metric_aliases:
  - Camera Send Days

meaning_zh: 发送相机消息天数占比。
meaning_en: Share of days with at least one camera-message send.

caliber_meaning: camera-message send coverage over days
calculation_method: Days with at least one camera-message send divided by days in the window.
numerator: days with camera sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Camera Days/User and Send Camera/User.
interpretation_notes: Camera message coverage signal.
```

## Metric: Send Camera Days/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Camera Days/User
metric_aliases:
  - Camera Send Days per User

meaning_zh: 发送相机消息天数/用户。
meaning_en: Average number of camera-message send-active days per user.

caliber_meaning: camera-message send coverage per user
calculation_method: Average camera-message send-active days per user in the analysis window.
numerator: days with camera sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Camera Days/Days.
interpretation_notes: Supporting camera-message coverage signal.
```

## Metric: Send Camera/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Camera/User
metric_aliases:
  - Camera Send per User

meaning_zh: 发送相机消息量/用户。
meaning_en: Average number of camera-message sends per user.

caliber_meaning: camera-message send intensity per user
calculation_method: Average camera-message sends per user in the analysis window.
numerator: total camera-message sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants.
interpretation_notes: Camera message intensity signal.
```

## Metric: Send Emoji Days/Days

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Emoji Days/Days
metric_aliases:
  - Emoji Send Days

meaning_zh: 发送表情消息天数占比。
meaning_en: Share of days with at least one emoji-message send.

caliber_meaning: emoji-message send coverage over days
calculation_method: Days with at least one emoji-message send divided by days in the window.
numerator: days with emoji sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Emoji Days/User.
interpretation_notes: Emoji message coverage signal.
```

## Metric: Send Emoji Days/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Emoji Days/User
metric_aliases:
  - Emoji Send Days per User

meaning_zh: 发送表情消息天数/用户。
meaning_en: Average number of emoji-message send-active days per user.

caliber_meaning: emoji-message send coverage per user
calculation_method: Average emoji-message send-active days per user in the analysis window.
numerator: days with emoji sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Emoji Days/Days.
interpretation_notes: Supporting emoji-message coverage signal.
```

## Metric: Send Text Days/Days

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Text Days/Days
metric_aliases:
  - Text Send Days

meaning_zh: 发送文本消息天数占比。
meaning_en: Share of days with at least one text-message send.

caliber_meaning: text-message send coverage over days
calculation_method: Days with at least one text-message send divided by days in the window.
numerator: days with text sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Text Days/User and Send Text/User.
interpretation_notes: Text message coverage signal.
```

## Metric: Send Text Days/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Text Days/User
metric_aliases:
  - Text Send Days per User

meaning_zh: 发送文本消息天数/用户。
meaning_en: Average number of text-message send-active days per user.

caliber_meaning: text-message send coverage per user
calculation_method: Average text-message send-active days per user in the analysis window.
numerator: days with text sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Text Days/Days.
interpretation_notes: Supporting text-message coverage signal.
```

## Metric: Send Text/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Text/User
metric_aliases:
  - Text Send per User

meaning_zh: 发送文本消息量/用户。
meaning_en: Average number of text-message sends per user.

caliber_meaning: text-message send intensity per user
calculation_method: Average text-message sends per user in the analysis window.
numerator: total text-message sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants.
interpretation_notes: Text message intensity signal.
```

## Metric: Send Voice_message Days/Days

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Voice_message Days/Days
metric_aliases:
  - Voice Message Send Days

meaning_zh: 发送语音消息天数占比。
meaning_en: Share of days with at least one voice-message send.

caliber_meaning: voice-message send coverage over days
calculation_method: Days with at least one voice-message send divided by days in the window.
numerator: days with voice sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Voice_message Days/User and Send Voice_message/User.
interpretation_notes: Voice-message coverage signal.
```

## Metric: Send Voice_message Days/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Voice_message Days/User
metric_aliases:
  - Voice Message Send Days per User

meaning_zh: 发送语音消息天数/用户。
meaning_en: Average number of voice-message send-active days per user.

caliber_meaning: voice-message send coverage per user
calculation_method: Average voice-message send-active days per user in the analysis window.
numerator: days with voice sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Voice_message Days/Days.
interpretation_notes: Supporting voice-message coverage signal.
```

## Metric: Send Voice_message/User

```yaml
group_name: [DM] DM by Msg Type
metric_name: Send Voice_message/User
metric_aliases:
  - Voice Message Send per User

meaning_zh: 发送语音消息量/用户。
meaning_en: Average number of voice-message sends per user.

caliber_meaning: voice-message send intensity per user
calculation_method: Average voice-message sends per user in the analysis window.
numerator: total voice-message sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants.
interpretation_notes: Voice-message intensity signal.
```
