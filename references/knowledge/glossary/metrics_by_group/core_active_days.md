# Metrics By Group | Core-Active Days

These entries are confirmed, reusable formal metrics for the Core-Active Days group.

## Metric: Active Days

```yaml
group_name: Core-Active Days
metric_name: Active Days
metric_aliases:
  - LT

meaning_zh: 用户在指定时间窗内的平均活跃天数。
meaning_en: Average active days per user in the specified lookback window.

caliber_meaning: user-level activity coverage over a lookback window
calculation_method: Count active days per user within the lookback window, then average across users.
numerator: active days within window
denominator: users

polarity: higher_is_better
priority_hint: P0
common_dimensions:
  - time_window
  - user_id

neighbor_metric_diff: Core base metric; do not confuse it with windowed variants such as Last 7-day Active Days.
interpretation_notes: Core activity coverage signal. Higher values usually indicate broader user activity coverage.
```

## Metric: Last 1-day Active Days

```yaml
group_name: Core-Active Days
metric_name: Last 1-day Active Days
metric_aliases:
  - LT1
  - LT1D

meaning_zh: 最近1天活跃天数。
meaning_en: Active days per user in the last 1 day lookback window.

caliber_meaning: short-window activity coverage
calculation_method: Count active days per user within the last 1 day window, then average across users.
numerator: active days within last 1 day
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Differs from Active Days and other variants only by the shorter lookback window.
interpretation_notes: Short-cycle supplement for activity coverage.
```

## Metric: Last 3-day Active Days

```yaml
group_name: Core-Active Days
metric_name: Last 3-day Active Days
metric_aliases:
  - LT3
  - LT3D

meaning_zh: 最近3天活跃天数。
meaning_en: Active days per user in the last 3 day lookback window.

caliber_meaning: short-window activity coverage
calculation_method: Count active days per user within the last 3 day window, then average across users.
numerator: active days within last 3 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Differs from Last 1-day Active Days and Last 7-day Active Days by the lookback window length.
interpretation_notes: Short-cycle supplement for activity coverage.
```

## Metric: Last 7-day Active Days

```yaml
group_name: Core-Active Days
metric_name: Last 7-day Active Days
metric_aliases:
  - LT7
  - LT7D

meaning_zh: 近 7 日活跃天数。
meaning_en: Active days per user in the last 7 day lookback window.

caliber_meaning: core activity coverage over a one-week window
calculation_method: Count active days per user within the last 7 day window, then average across users.
numerator: active days within last 7 days
denominator: users

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Same family as Active Days, but with a shorter lookback window that is often more sensitive to recent behavior changes.
interpretation_notes: Strong core health companion metric; keep it distinct from longer windows.
```

## Metric: Last 14-day Active Days

```yaml
group_name: Core-Active Days
metric_name: Last 14-day Active Days
metric_aliases:
  - LT14
  - LT14D

meaning_zh: 最近14天活跃天数。
meaning_en: Active days per user in the last 14 day lookback window.

caliber_meaning: mid-window activity coverage
calculation_method: Count active days per user within the last 14 day window, then average across users.
numerator: active days within last 14 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as Last 7-day Active Days and Last 30-day Active Days, but with a mid-length lookback window.
interpretation_notes: Mid-cycle supplement for activity coverage.
```

## Metric: Last 30-day Active Days

```yaml
group_name: Core-Active Days
metric_name: Last 30-day Active Days
metric_aliases:
  - LT30
  - LT30D

meaning_zh: 最近30天活跃天数。
meaning_en: Active days per user in the last 30 day lookback window.

caliber_meaning: long-window activity coverage
calculation_method: Count active days per user within the last 30 day window, then average across users.
numerator: active days within last 30 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as Active Days, but with the longest standard lookback window.
interpretation_notes: Long-cycle supplement for activity coverage.
```
