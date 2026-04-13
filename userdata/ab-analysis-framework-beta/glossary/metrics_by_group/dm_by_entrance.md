# Metrics By Group | [DM] DM by Entrance

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM by Entrance.

## Metric: Send Msg from Inbox Days/Days

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inbox Days/Days
metric_aliases:
  - Inbox Send Days

meaning_zh: 来自 Inbox 入口的发消息天数占比。
meaning_en: Share of days with at least one message send from the Inbox entrance.

caliber_meaning: inbox-entry send coverage over days
calculation_method: Days with at least one Inbox-triggered send divided by days in the window.
numerator: days with Inbox sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the user-level and PV-based variants, and from inner/outer-push variants.
interpretation_notes: Inbox-entry send coverage signal.
```

## Metric: Send Msg from Inbox Days/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inbox Days/User
metric_aliases:
  - Inbox Send Days per User

meaning_zh: 来自 Inbox 入口的发消息天数/用户。
meaning_en: Average number of send-active days from the Inbox entrance per user.

caliber_meaning: inbox-entry send coverage per user
calculation_method: Average Inbox-triggered send-active days per user in the analysis window.
numerator: days with Inbox sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Msg from Inbox Days/Days.
interpretation_notes: Supporting inbox-entry coverage signal.
```

## Metric: Send Msg from Inbox/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inbox/User
metric_aliases:
  - Inbox Send per User

meaning_zh: 来自 Inbox 入口的发消息量/用户。
meaning_en: Average number of sends from the Inbox entrance per user.

caliber_meaning: inbox-entry send intensity per user
calculation_method: Average Inbox-triggered sends per user in the analysis window.
numerator: total Inbox-triggered sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants and from the push-based variants.
interpretation_notes: Supporting inbox-entry intensity signal.
```

## Metric: Send Msg from Inner Push Days/Days

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inner Push Days/Days
metric_aliases:
  - Inner Push Send Days

meaning_zh: 来自站内推送入口的发消息天数占比。
meaning_en: Share of days with at least one message send from the inner-push entrance.

caliber_meaning: inner-push entry send coverage over days
calculation_method: Days with at least one inner-push-triggered send divided by days in the window.
numerator: days with inner-push sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the user-level and PV-based variants, and from Inbox/Outer Push variants.
interpretation_notes: Supporting entrance signal for inner push.
```

## Metric: Send Msg from Inner Push Days/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inner Push Days/User
metric_aliases:
  - Inner Push Send Days per User

meaning_zh: 来自站内推送入口的发消息天数/用户。
meaning_en: Average number of send-active days from the inner-push entrance per user.

caliber_meaning: inner-push entry send coverage per user
calculation_method: Average inner-push-triggered send-active days per user in the analysis window.
numerator: days with inner-push sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Msg from Inner Push Days/Days.
interpretation_notes: Supporting entrance signal for inner push.
```

## Metric: Send Msg from Inner Push/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Inner Push/User
metric_aliases:
  - Inner Push Send per User

meaning_zh: 来自站内推送入口的发消息量/用户。
meaning_en: Average number of sends from the inner-push entrance per user.

caliber_meaning: inner-push entry send intensity per user
calculation_method: Average inner-push-triggered sends per user in the analysis window.
numerator: total inner-push-triggered sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants and from Inbox/Outer Push variants.
interpretation_notes: Supporting entrance signal for inner push.
```

## Metric: Send Msg from Outer Push Days/Days

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Outer Push Days/Days
metric_aliases:
  - Outer Push Send Days

meaning_zh: 来自站外推送入口的发消息天数占比。
meaning_en: Share of days with at least one message send from the outer-push entrance.

caliber_meaning: outer-push entry send coverage over days
calculation_method: Days with at least one outer-push-triggered send divided by days in the window.
numerator: days with outer-push sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the user-level and PV-based variants, and from Inbox/Inner Push variants.
interpretation_notes: Supporting entrance signal for outer push.
```

## Metric: Send Msg from Outer Push Days/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Outer Push Days/User
metric_aliases:
  - Outer Push Send Days per User

meaning_zh: 来自站外推送入口的发消息天数/用户。
meaning_en: Average number of send-active days from the outer-push entrance per user.

caliber_meaning: outer-push entry send coverage per user
calculation_method: Average outer-push-triggered send-active days per user in the analysis window.
numerator: days with outer-push sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Msg from Outer Push Days/Days.
interpretation_notes: Supporting entrance signal for outer push.
```

## Metric: Send Msg from Outer Push/User

```yaml
group_name: [DM] DM by Entrance
metric_name: Send Msg from Outer Push/User
metric_aliases:
  - Outer Push Send per User

meaning_zh: 来自站外推送入口的发消息量/用户。
meaning_en: Average number of sends from the outer-push entrance per user.

caliber_meaning: outer-push entry send intensity per user
calculation_method: Average outer-push-triggered sends per user in the analysis window.
numerator: total outer-push-triggered sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the day-based variants and from Inbox/Inner Push variants.
interpretation_notes: Supporting entrance signal for outer push.
```
