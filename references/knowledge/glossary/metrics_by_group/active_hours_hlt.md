# Metrics By Group | Active Hours (HLT)

These entries are confirmed, reusable formal metrics for the Active Hours (HLT) group.

## Metric: HLT - active hours

```yaml
group_name: Active Hours (HLT)
metric_name: HLT - active hours
metric_aliases:
  - HLT

meaning_zh: 用户在指定时间窗内的总活跃时长。
meaning_en: Total active hours in the specified lookback window.

caliber_meaning: total usage depth over a lookback window
calculation_method: Sum active hours within the lookback window.
numerator: active hours within window
denominator:

polarity: higher_is_better
priority_hint: P2
common_dimensions:
  - time_window
  - user_id

neighbor_metric_diff: Do not confuse the total active-hours metric with the per-user active-hours variants below.
interpretation_notes: Core time-spent signal; often used as a supporting guardrail for engagement depth.
```

## Metric: HLT1-last 1-day active hours/U

```yaml
group_name: Active Hours (HLT)
metric_name: HLT1-last 1-day active hours/U
metric_aliases:
  - HLT1

meaning_zh: 最近1天活跃小时数/用户。
meaning_en: Average active hours per user in the last 1 day lookback window.

caliber_meaning: short-window usage depth per user
calculation_method: Average active hours per user within the last 1 day window.
numerator: active hours within last 1 day
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as HLT3/HLT7/HLT14/HLT30, but with the shortest lookback window.
interpretation_notes: Short-cycle supplement for usage depth.
```

## Metric: HLT3-last 3-day active hours/U

```yaml
group_name: Active Hours (HLT)
metric_name: HLT3-last 3-day active hours/U
metric_aliases:
  - HLT3

meaning_zh: 最近3天活跃小时数/用户。
meaning_en: Average active hours per user in the last 3 day lookback window.

caliber_meaning: short-window usage depth per user
calculation_method: Average active hours per user within the last 3 day window.
numerator: active hours within last 3 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as HLT1 and HLT7, with a mid-short lookback window.
interpretation_notes: Short-cycle supplement for usage depth.
```

## Metric: HLT7-last 7-day active hours/U

```yaml
group_name: Active Hours (HLT)
metric_name: HLT7-last 7-day active hours/U
metric_aliases:
  - HLT7

meaning_zh: 近 7 日人均活跃时长。
meaning_en: Average active hours per user in the last 7 day lookback window.

caliber_meaning: core time-spent depth per user over a one-week window
calculation_method: Average active hours per user within the last 7 day window.
numerator: active hours within last 7 days
denominator: users

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Same family as HLT1/HLT3/HLT14/HLT30, but with a one-week lookback window that is often more sensitive to recent engagement changes.
interpretation_notes: Strong core health companion metric; keep it distinct from longer windows.
```

## Metric: HLT14-last 14-day active hours/U

```yaml
group_name: Active Hours (HLT)
metric_name: HLT14-last 14-day active hours/U
metric_aliases:
  - HLT14

meaning_zh: 最近14天活跃小时数/用户。
meaning_en: Average active hours per user in the last 14 day lookback window.

caliber_meaning: mid-window usage depth per user
calculation_method: Average active hours per user within the last 14 day window.
numerator: active hours within last 14 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as HLT7 and HLT30, but with a mid-length lookback window.
interpretation_notes: Mid-cycle supplement for usage depth.
```

## Metric: HLT30-last 30-day active hours/U

```yaml
group_name: Active Hours (HLT)
metric_name: HLT30-last 30-day active hours/U
metric_aliases:
  - HLT30

meaning_zh: 最近30天活跃小时数/用户。
meaning_en: Average active hours per user in the last 30 day lookback window.

caliber_meaning: long-window usage depth per user
calculation_method: Average active hours per user within the last 30 day window.
numerator: active hours within last 30 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as HLT7 and HLT14, but with the longest standard lookback window.
interpretation_notes: Long-cycle supplement for usage depth.
```

## Metric: valid_session_cnt/User

```yaml
group_name: Active Hours (HLT)
metric_name: valid_session_cnt/User
metric_aliases:
  - valid session cnt per user

meaning_zh: 有效 session 数/用户。
meaning_en: Average valid session count per user.

caliber_meaning: session depth per user
calculation_method: Average valid sessions per user in the window.
numerator: valid sessions
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Different from hours-based metrics; measures session quantity rather than time spent.
interpretation_notes: Useful as a complementary depth signal.
```

## Metric: VS3-last 3-day ValidSession/U

```yaml
group_name: Active Hours (HLT)
metric_name: VS3-last 3-day ValidSession/U
metric_aliases:
  - VS3

meaning_zh: 最近3天有效 session 数/用户。
meaning_en: Average valid sessions per user in the last 3 day lookback window.

caliber_meaning: short-window session depth per user
calculation_method: Average valid sessions per user within the last 3 day window.
numerator: valid sessions within last 3 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as VS7/VS14/VS30; shorter window and more sensitive to recent usage changes.
interpretation_notes: Short-cycle session-depth supplement.
```

## Metric: VS1-last 1-day ValidSession/U

```yaml
group_name: Active Hours (HLT)
metric_name: VS1-last 1-day ValidSession/U
metric_aliases:
  - VS1

meaning_zh: 最近1天有效 session 数/用户。
meaning_en: Average valid sessions per user in the last 1 day lookback window.

caliber_meaning: shortest-window session depth per user
calculation_method: Average valid sessions per user within the last 1 day window.
numerator: valid sessions within last 1 day
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as VS3/VS7/VS14/VS30; shortest lookback window.
interpretation_notes: Short-cycle session-depth supplement.
```

## Metric: VS7-last 7-day ValidSession/U

```yaml
group_name: Active Hours (HLT)
metric_name: VS7-last 7-day ValidSession/U
metric_aliases:
  - VS7

meaning_zh: 最近7天有效 session 数/用户。
meaning_en: Average valid sessions per user in the last 7 day lookback window.

caliber_meaning: core session depth per user over a one-week window
calculation_method: Average valid sessions per user within the last 7 day window.
numerator: valid sessions within last 7 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as VS3/VS14/VS30; one-week lookback window.
interpretation_notes: Core time-spent companion metric.
```

## Metric: VS14-last 14-day ValidSession/U

```yaml
group_name: Active Hours (HLT)
metric_name: VS14-last 14-day ValidSession/U
metric_aliases:
  - VS14

meaning_zh: 最近14天有效 session 数/用户。
meaning_en: Average valid sessions per user in the last 14 day lookback window.

caliber_meaning: mid-window session depth per user
calculation_method: Average valid sessions per user within the last 14 day window.
numerator: valid sessions within last 14 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as VS7 and VS30; mid-length lookback window.
interpretation_notes: Mid-cycle session-depth supplement.
```

## Metric: VS30-last 30-day ValidSession/U

```yaml
group_name: Active Hours (HLT)
metric_name: VS30-last 30-day ValidSession/U
metric_aliases:
  - VS30

meaning_zh: 最近30天有效 session 数/用户。
meaning_en: Average valid sessions per user in the last 30 day lookback window.

caliber_meaning: long-window session depth per user
calculation_method: Average valid sessions per user within the last 30 day window.
numerator: valid sessions within last 30 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as VS7 and VS14; longest standard lookback window.
interpretation_notes: Long-cycle session-depth supplement.
```
