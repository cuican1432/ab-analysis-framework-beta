# Metrics By Group | [DM] MuF DM by Motivation

These entries are confirmed, reusable formal metrics for the [DM] MuF DM by Motivation group.

## Metric: MuF Active Chat Days/Days

```yaml
group_name: [DM] MuF DM by Motivation
metric_name: MuF Active Chat Days/Days
metric_aliases:
  - MuF Active Chat Days

meaning_zh: MUF 活跃聊天天数/天数。
meaning_en: Share of days with active-chat behavior in the analysis window.

caliber_meaning: MuF active-chat coverage over days
calculation_method: Days with at least one active-chat event divided by days in the window.
numerator: days with active chat
denominator: days in window

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the per-user and pure-share variants.
interpretation_notes: Motivation-based active-chat coverage signal.
```

## Metric: MuF Active Chat Days/User

```yaml
group_name: [DM] MuF DM by Motivation
metric_name: MuF Active Chat Days/User
metric_aliases:
  - MuF Active Chat Days per User

meaning_zh: MUF 活跃聊天天数/用户。
meaning_en: Average number of active-chat days per user under the MUF motivation taxonomy.

caliber_meaning: MuF active-chat coverage per user
calculation_method: Average active-chat days per user in the analysis window.
numerator: days with active chat
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from MuF Active Chat Days/Days.
interpretation_notes: Motivation-based active-chat supporting signal.
```

## Metric: MuF Active Chat/User

```yaml
group_name: [DM] MuF DM by Motivation
metric_name: MuF Active Chat/User
metric_aliases:
  - MuF Active Chat per User

meaning_zh: MUF 活跃聊天数/用户。
meaning_en: Average number of active-chat events per user under the MUF motivation taxonomy.

caliber_meaning: MuF active-chat intensity per user
calculation_method: Average active-chat PV per user in the analysis window.
numerator: total active chat PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the day-based coverage variants.
interpretation_notes: Motivation-based active-chat intensity signal.
```

## Metric: MuF Share/User

```yaml
group_name: [DM] MuF DM by Motivation
metric_name: MuF Share/User
metric_aliases:
  - MuF Share per User

meaning_zh: MUF 分享数/用户。
meaning_en: Average number of MUF share events per user.

caliber_meaning: MuF share intensity per user
calculation_method: Average MUF share PV per user in the analysis window.
numerator: total MUF share PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from active-chat metrics in this group.
interpretation_notes: Motivation-based share intensity signal.
```
