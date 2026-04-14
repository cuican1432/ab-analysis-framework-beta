# Metrics By Group | [DM] DM Core Performance - Android

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM Core Performance - Android.

## Metric: chat_list_load_latency_compliance_rate_threshold_ig

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: chat_list_load_latency_compliance_rate_threshold_ig
metric_aliases:
  - chat list load latency compliance ig

meaning_zh: 聊天列表加载时延合规率（IG口径）。
meaning_en: Chat-list load latency compliance rate under the IG caliber.

caliber_meaning: chat-list latency compliance
calculation_method: Source-defined latency compliance rate for chat-list load behavior.
numerator: compliant loads
denominator: total loads

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the p90 variant and from chat-room latency metrics.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: chat_list_load_latency_compliance_rate_threshold_p90

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: chat_list_load_latency_compliance_rate_threshold_p90
metric_aliases:
  - chat list load latency compliance p90

meaning_zh: 聊天列表加载时延合规率（P90口径）。
meaning_en: Chat-list load latency compliance rate under the p90 caliber.

caliber_meaning: chat-list latency compliance
calculation_method: Source-defined latency compliance rate for chat-list load behavior at p90 threshold.
numerator: compliant loads
denominator: total loads

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the IG variant and from chat-room latency metrics.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: chat_room_load_latency_compliance_rate_threshold_ig

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: chat_room_load_latency_compliance_rate_threshold_ig
metric_aliases:
  - chat room load latency compliance ig

meaning_zh: 聊天房间加载时延合规率（IG口径）。
meaning_en: Chat-room load latency compliance rate under the IG caliber.

caliber_meaning: chat-room latency compliance
calculation_method: Source-defined latency compliance rate for chat-room load behavior.
numerator: compliant loads
denominator: total loads

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the p90 variant and from chat-list latency metrics.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: chat_room_load_latency_compliance_rate_threshold_p90

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: chat_room_load_latency_compliance_rate_threshold_p90
metric_aliases:
  - chat room load latency compliance p90

meaning_zh: 聊天房间加载时延合规率（P90口径）。
meaning_en: Chat-room load latency compliance rate under the p90 caliber.

caliber_meaning: chat-room latency compliance
calculation_method: Source-defined latency compliance rate for chat-room load behavior at p90 threshold.
numerator: compliant loads
denominator: total loads

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the IG variant and from chat-list latency metrics.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: send_message_latency_compliance_rate_threshold_p90

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: send_message_latency_compliance_rate_threshold_p90
metric_aliases:
  - send message latency compliance p90

meaning_zh: 发送消息链路时延合规率（P90口径）。
meaning_en: Send-message latency compliance rate under the p90 caliber.

caliber_meaning: send-path latency compliance
calculation_method: Source-defined latency compliance rate for send-message behavior at p90 threshold.
numerator: compliant sends
denominator: total sends

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the p50 variant.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: send_message_latency_compliance_rate_threshold_p50

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: send_message_latency_compliance_rate_threshold_p50
metric_aliases:
  - send message latency compliance p50

meaning_zh: 发送消息链路时延合规率（P50口径）。
meaning_en: Send-message latency compliance rate under the p50 caliber.

caliber_meaning: send-path latency compliance
calculation_method: Source-defined latency compliance rate for send-message behavior at p50 threshold.
numerator: compliant sends
denominator: total sends

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from the p90 variant.
interpretation_notes: Core Android performance guardrail signal.
```

## Metric: chat_list_frame_drop_level_4

```yaml
group_name: [DM] DM Core Performance - Android
metric_name: chat_list_frame_drop_level_4
metric_aliases:
  - chat list frame drop level 4

meaning_zh: 聊天列表 4 级掉帧相关指标。
meaning_en: Chat-list frame-drop level-4 metric.

caliber_meaning: chat-list rendering smoothness
calculation_method: Source-defined frame-drop rate for the chat list at level 4.
numerator: frame-drop events
denominator: render opportunities

polarity: lower_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from latency-compliance metrics; this one captures rendering smoothness rather than load time.
interpretation_notes: Core Android performance guardrail signal.
```

