# Metrics By Group | DM Group Chat

Reference entry for These entries are confirmed, reusable formal metrics for the DM Group Chat.

## Metric: Create GC pv/au

```yaml
group_name: DM Group Chat
metric_name: Create GC pv/au
metric_aliases:
  - Create GC

meaning_zh: 创建群聊PV/活跃用户。
meaning_en: Average number of group-chat creation events per active user.

caliber_meaning: group-chat creation intensity
calculation_method: Average create-GC PV per active user in the analysis window.
numerator: total create-GC PV
denominator: active users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the UV variant and from enter/send metrics.
interpretation_notes: Group-chat creation signal.
```

## Metric: Create GC uv/au

```yaml
group_name: DM Group Chat
metric_name: Create GC uv/au
metric_aliases:
  - Create GC UV

meaning_zh: 创建群聊UV/活跃用户。
meaning_en: Average number of users creating group chats per active user.

caliber_meaning: group-chat creation coverage
calculation_method: Average create-GC UV per active user in the analysis window.
numerator: total create-GC UV
denominator: active users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the PV variant.
interpretation_notes: Group-chat creation coverage signal.
```

## Metric: GC Enter Chat pv/au

```yaml
group_name: DM Group Chat
metric_name: GC Enter Chat pv/au
metric_aliases:
  - GC Enter Chat

meaning_zh: 进入群聊PV/活跃用户。
meaning_en: Average number of group-chat enter events per active user.

caliber_meaning: group-chat entry intensity
calculation_method: Average enter-chat PV per active user in the analysis window.
numerator: total enter-chat PV
denominator: active users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from create and send metrics.
interpretation_notes: Group-chat entry signal.
```

## Metric: GC Send Message pv/au

```yaml
group_name: DM Group Chat
metric_name: GC Send Message pv/au
metric_aliases:
  - GC Send Message

meaning_zh: 发送群聊消息PV/活跃用户。
meaning_en: Average number of group-chat send-message events per active user.

caliber_meaning: group-chat send intensity
calculation_method: Average send-message PV per active user in the analysis window.
numerator: total group-chat send-message PV
denominator: active users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the enter-chat and send-or-like variants.
interpretation_notes: Group-chat sending signal.
```

## Metric: GC Send or Like pv/au

```yaml
group_name: DM Group Chat
metric_name: GC Send or Like pv/au
metric_aliases:
  - GC Send or Like

meaning_zh: 群聊发送或点赞PV/活跃用户。
meaning_en: Average number of group-chat send-or-like events per active user.

caliber_meaning: group-chat interaction intensity
calculation_method: Average send-or-like PV per active user in the analysis window.
numerator: total group-chat send-or-like PV
denominator: active users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the pure send-message metric.
interpretation_notes: Group-chat interaction signal.
```
