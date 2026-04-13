# Metrics By Group | [DM] DM Outer Push

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM Outer Push.

## Metric: Send Msg from Outer Push Days/Days

```yaml
group_name: [DM] DM Outer Push
metric_name: Send Msg from Outer Push Days/Days
metric_aliases:
  - Outer Push Send Days

meaning_zh: 来自站外推送触发的发消息天数占比。
meaning_en: Share of days with at least one message send triggered by outer push.

caliber_meaning: outer-push send coverage over days
calculation_method: Days with at least one outer-push-triggered send divided by days in the window.
numerator: days with outer-push sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the user-level and PV-based variants.
interpretation_notes: Reach-to-send conversion signal for outer push.
```

## Metric: Send Msg from Outer Push Days/User

```yaml
group_name: [DM] DM Outer Push
metric_name: Send Msg from Outer Push Days/User
metric_aliases:
  - Outer Push Send Days per User

meaning_zh: 来自站外推送触发的发消息天数/用户。
meaning_en: Average number of send-active days triggered by outer push per user.

caliber_meaning: outer-push send coverage per user
calculation_method: Average outer-push-triggered send-active days per user in the analysis window.
numerator: days with outer-push sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Msg from Outer Push Days/Days.
interpretation_notes: Supporting reach-to-send conversion signal.
```

## Metric: Send Msg from Outer Push/User

```yaml
group_name: [DM] DM Outer Push
metric_name: Send Msg from Outer Push/User
metric_aliases:
  - Outer Push Send per User

meaning_zh: 来自站外推送触发的发消息量/用户。
meaning_en: Average number of sends triggered by outer push per user.

caliber_meaning: outer-push send intensity per user
calculation_method: Average outer-push-triggered sends per user in the analysis window.
numerator: total outer-push-triggered sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants.
interpretation_notes: Supporting intensity signal for outer push.
```
