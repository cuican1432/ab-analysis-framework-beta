# Metrics By Group | [DM] DM Quality & Reply Rates New

These entries are confirmed, reusable formal metrics for the [DM] DM Quality & Reply Rates New group.

## Metric: 1h Response Rate（会话粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 1h Response Rate（会话粒度）
metric_aliases:
  - 1h Response Rate (Conversation Level)

meaning_zh: 会话粒度下 1 小时回复率。
meaning_en: 1-hour response rate at the conversation level.

caliber_meaning: 1h reply rate at conversation granularity
calculation_method: Conversations with a reply within 1 hour divided by eligible conversations.
numerator: conversations replied to within 1 hour
denominator: eligible conversations

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - response_level
  - message_type

neighbor_metric_diff: Keep distinct from the turn-level variant.
interpretation_notes: Core response-quality signal.
```

## Metric: 1h Response Rate（轮次粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 1h Response Rate（轮次粒度）
metric_aliases:
  - 1h Response Rate (Turn Level)

meaning_zh: 轮次粒度下 1 小时回复率。
meaning_en: 1-hour response rate at the turn level.

caliber_meaning: 1h reply rate at turn granularity
calculation_method: Turns with a reply within 1 hour divided by eligible turns.
numerator: turns replied to within 1 hour
denominator: eligible turns

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the conversation-level variant.
interpretation_notes: Core response-quality signal.
```

## Metric: 24h Camera Msg Response Rate（轮次粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 24h Camera Msg Response Rate（轮次粒度）
metric_aliases:
  - 24h Camera Response Rate (Turn Level)

meaning_zh: 轮次粒度下相机消息 24 小时回复率。
meaning_en: 24-hour response rate for camera messages at the turn level.

caliber_meaning: camera-message 24h reply rate at turn granularity
calculation_method: Turns with a reply within 24 hours divided by eligible camera-message turns.
numerator: camera-message turns replied to within 24 hours
denominator: eligible camera-message turns

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the text-message variant and the general response-rate metrics.
interpretation_notes: Camera-message response-quality signal.
```

## Metric: 24h Response Rate（轮次粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 24h Response Rate（轮次粒度）
metric_aliases:
  - 24h Response Rate (Turn Level)

meaning_zh: 轮次粒度下 24 小时回复率。
meaning_en: 24-hour response rate at the turn level.

caliber_meaning: 24h reply rate at turn granularity
calculation_method: Turns with a reply within 24 hours divided by eligible turns.
numerator: turns replied to within 24 hours
denominator: eligible turns

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the conversation-level variant and from media-specific variants.
interpretation_notes: Core response-quality signal.
```

## Metric: 24h text Msg Response Rate（轮次粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 24h text Msg Response Rate（轮次粒度）
metric_aliases:
  - 24h Text Response Rate (Turn Level)

meaning_zh: 轮次粒度下文本消息 24 小时回复率。
meaning_en: 24-hour response rate for text messages at the turn level.

caliber_meaning: text-message 24h reply rate at turn granularity
calculation_method: Turns with a reply within 24 hours divided by eligible text-message turns.
numerator: text-message turns replied to within 24 hours
denominator: eligible text-message turns

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the camera-message variant and the general response-rate metrics.
interpretation_notes: Text-message response-quality signal.
```

## Metric: 7h Response Rate（轮次粒度）

```yaml
group_name: [DM] DM Quality & Reply Rates New
metric_name: 7h Response Rate（轮次粒度）
metric_aliases:
  - 7h Response Rate (Turn Level)

meaning_zh: 轮次粒度下 7 小时回复率。
meaning_en: 7-hour response rate at the turn level.

caliber_meaning: 7h reply rate at turn granularity
calculation_method: Turns with a reply within 7 hours divided by eligible turns.
numerator: turns replied to within 7 hours
denominator: eligible turns

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the 1h and 24h variants.
interpretation_notes: Short-horizon response-quality signal.
```
