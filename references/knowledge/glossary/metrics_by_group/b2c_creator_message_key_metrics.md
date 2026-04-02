# Metrics By Group | [B2C] Creator Message Key Metrics

These entries are confirmed, reusable formal metrics for the [B2C] Creator Message Key Metrics group.

## Metric: Cr2C DM pv / DAU

```yaml
group_name: [B2C] Creator Message Key Metrics
metric_name: Cr2C DM pv / DAU
metric_aliases:
  - Creator DM pv / DAU

meaning_zh: 创作者消息私信 PV / DAU。
meaning_en: Creator-message DM page views per DAU.

caliber_meaning: creator DM reach intensity per DAU
calculation_method: Average creator-message DM PV per DAU in the analysis window.
numerator: total creator DM PV
denominator: DAU

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - product_type
  - user_id

neighbor_metric_diff: Keep distinct from the MUF variant below.
interpretation_notes: Creator-message reach/support signal.
```

## Metric: Cr2C MuF DM pv / DAU

```yaml
group_name: [B2C] Creator Message Key Metrics
metric_name: Cr2C MuF DM pv / DAU
metric_aliases:
  - Creator MuF DM pv / DAU

meaning_zh: 创作者消息 MUF 私信 PV / DAU。
meaning_en: Creator-message MUF DM page views per DAU.

caliber_meaning: creator MUF DM reach intensity per DAU
calculation_method: Average creator-MUF DM PV per DAU in the analysis window.
numerator: total creator MUF DM PV
denominator: DAU

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the plain creator DM PV/DAU variant.
interpretation_notes: Creator-message MUF support signal.
```
