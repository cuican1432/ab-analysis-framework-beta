# Metrics By Group | Core-Publish Days

These entries are confirmed, reusable formal metrics for the Core-Publish Days group.

## Metric: Publish Days

```yaml
group_name: Core-Publish Days
metric_name: Publish Days
metric_aliases:
  - publish days

meaning_zh: 指定时间窗内的发布视频天数。
meaning_en: Number of days with at least one publish event in the specified lookback window.

caliber_meaning: publish coverage over a lookback window
calculation_method: Count days with at least one publish event within the lookback window.
numerator: days with publishes
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Core base metric; do not confuse it with the shorter or longer lookback-window variants.
interpretation_notes: Creative coverage signal. Higher values usually indicate broader publishing coverage.
```

## Metric: Last 1-day Publish Days

```yaml
group_name: Core-Publish Days
metric_name: Last 1-day Publish Days
metric_aliases:
  - LT1 Publish Days

meaning_zh: 最近1天发布视频天数。
meaning_en: Publish days per user in the last 1 day lookback window.

caliber_meaning: short-window publish coverage
calculation_method: Count publish days per user within the last 1 day window.
numerator: publish days within last 1 day
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Differs from Publish Days and other variants only by the shorter lookback window.
interpretation_notes: Short-cycle supplement for publishing coverage.
```

## Metric: Last 7-day Publish Days

```yaml
group_name: Core-Publish Days
metric_name: Last 7-day Publish Days
metric_aliases:
  - LT7 Publish Days

meaning_zh: 近 7 日发布视频天数。
meaning_en: Publish days per user in the last 7 day lookback window.

caliber_meaning: core publish coverage over a one-week window
calculation_method: Count publish days per user within the last 7 day window.
numerator: publish days within last 7 days
denominator: users

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Same family as Publish Days, but with a one-week lookback window that is often more sensitive to recent publishing changes.
interpretation_notes: Strong core health companion metric; keep it distinct from longer windows.
```

## Metric: Last 30-day Publish Days

```yaml
group_name: Core-Publish Days
metric_name: Last 30-day Publish Days
metric_aliases:
  - LT30 Publish Days

meaning_zh: 最近30天发布视频天数。
meaning_en: Publish days per user in the last 30 day lookback window.

caliber_meaning: long-window publish coverage
calculation_method: Count publish days per user within the last 30 day window.
numerator: publish days within last 30 days
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Same family as Publish Days, but with the longest standard lookback window.
interpretation_notes: Long-cycle supplement for publishing coverage.
```
