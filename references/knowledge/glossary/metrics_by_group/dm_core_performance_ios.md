# Metrics By Group | [DM] DM Core Performance - iOS

These entries are confirmed, reusable formal metrics for the [DM] DM Core Performance - iOS group.

## Metric: chat_room_load_latency_compliance_rate_threshold_p90

```yaml
group_name: [DM] DM Core Performance - iOS
metric_name: chat_room_load_latency_compliance_rate_threshold_p90
metric_aliases:
  - chat room load latency compliance p90

meaning_zh: iOS 聊天房间加载时延合规率（P90口径）。
meaning_en: iOS chat-room load latency compliance rate under the p90 caliber.

caliber_meaning: iOS chat-room latency compliance
calculation_method: Source-defined latency compliance rate for iOS chat-room load behavior at p90 threshold.
numerator: compliant loads
denominator: total loads

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from Android performance metrics and from the IG variant.
interpretation_notes: Core iOS performance guardrail signal.
```

