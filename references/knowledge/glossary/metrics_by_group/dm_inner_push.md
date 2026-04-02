# Metrics By Group | [DM] DM Inner Push

These entries are confirmed, reusable formal metrics for the [DM] DM Inner Push group.

## Metric: Send Msg from Inner Push Days/Days

```yaml
group_name: [DM] DM Inner Push
metric_name: Send Msg from Inner Push Days/Days
metric_aliases:
  - Inner Push Send Days

meaning_zh: 来自站内推送触发的发消息天数占比。
meaning_en: Share of days with at least one message send triggered by inner push.

caliber_meaning: inner-push send coverage over days
calculation_method: Days with at least one inner-push-triggered send divided by days in the window.
numerator: days with inner-push sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the user-level and PV-based variants.
interpretation_notes: Reach-to-send conversion signal for inner push.
```

## Metric: Send Msg from Inner Push Days/User

```yaml
group_name: [DM] DM Inner Push
metric_name: Send Msg from Inner Push Days/User
metric_aliases:
  - Inner Push Send Days per User

meaning_zh: 来自站内推送触发的发消息天数/用户。
meaning_en: Average number of send-active days triggered by inner push per user.

caliber_meaning: inner-push send coverage per user
calculation_method: Average inner-push-triggered send-active days per user in the analysis window.
numerator: days with inner-push sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Msg from Inner Push Days/Days.
interpretation_notes: Supporting reach-to-send conversion signal.
```

## Metric: Send Msg from Inner Push/User

```yaml
group_name: [DM] DM Inner Push
metric_name: Send Msg from Inner Push/User
metric_aliases:
  - Inner Push Send per User

meaning_zh: 来自站内推送触发的发消息量/用户。
meaning_en: Average number of sends triggered by inner push per user.

caliber_meaning: inner-push send intensity per user
calculation_method: Average inner-push-triggered sends per user in the analysis window.
numerator: total inner-push-triggered sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants.
interpretation_notes: Supporting intensity signal for inner push.
```
