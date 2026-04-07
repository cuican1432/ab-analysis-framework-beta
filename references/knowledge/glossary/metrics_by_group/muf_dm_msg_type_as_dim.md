# Metrics By Group | [DM] Muf DM Msg Type as Dim

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] Muf DM Msg Type as Dim.

## Metric: MUF Send or Like Message Days/User

```yaml
group_name: [DM] Muf DM Msg Type as Dim
metric_name: MUF Send or Like Message Days/User
metric_aliases:
  - MUF Send or Like Message Days per User

meaning_zh: MUF 发送或点赞消息天数/用户。
meaning_en: Average number of MUF send-or-like active days per user under the message-type split.

caliber_meaning: MUF send-or-like coverage per user
calculation_method: Average MUF active days per user in the analysis window.
numerator: days with MUF send-or-like events
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the pair-based and message-based variants.
interpretation_notes: Message-type split MUF coverage signal.
```

## Metric: MUF Send or Like Message Pair/User

```yaml
group_name: [DM] Muf DM Msg Type as Dim
metric_name: MUF Send or Like Message Pair/User
metric_aliases:
  - MUF Send or Like Message Pair per User

meaning_zh: MUF 发送或点赞消息对/用户。
meaning_en: Average number of MUF send-or-like message pairs per user under the message-type split.

caliber_meaning: MUF send-or-like pair intensity per user
calculation_method: Average MUF send-or-like pairs per user in the analysis window.
numerator: total MUF send-or-like pairs
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the days-based and message-based variants.
interpretation_notes: Message-type split MUF pair-intensity signal.
```

## Metric: MUF Send or Like Message/User

```yaml
group_name: [DM] Muf DM Msg Type as Dim
metric_name: MUF Send or Like Message/User
metric_aliases:
  - MUF Send or Like Message per User

meaning_zh: MUF 发送或点赞消息数/用户。
meaning_en: Average number of MUF send-or-like messages per user under the message-type split.

caliber_meaning: MUF send-or-like intensity per user
calculation_method: Average MUF send-or-like PV per user in the analysis window.
numerator: total MUF send-or-like PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the pair-based and days-based variants.
interpretation_notes: Message-type split MUF intensity signal.
```

## Metric: Message/User

```yaml
group_name: [DM] Muf DM Msg Type as Dim
metric_name: Message/User
metric_aliases:
  - Message per User

meaning_zh: 消息数/用户。
meaning_en: Average number of messages per user under the message-type split.

caliber_meaning: generic message intensity per user
calculation_method: Average message PV per user in the analysis window.
numerator: total message PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from MUF-specific metrics.
interpretation_notes: Broad supporting signal under the message-type dimension.
```
