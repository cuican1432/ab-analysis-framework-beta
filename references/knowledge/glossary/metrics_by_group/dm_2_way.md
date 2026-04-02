# Metrics By Group | [DM] DM 2-Way

These entries are confirmed, reusable formal metrics for the [DM] DM 2-Way group.

## Metric: Group Send or Like Message 2-Way Days/Days

```yaml
group_name: [DM] DM 2-Way
metric_name: Group Send or Like Message 2-Way Days/Days
metric_aliases:
  - Group Send or Like Message 2-Way Days

meaning_zh: 群聊双向发送或点赞消息天数/天数。
meaning_en: Share of days with group-chat two-way send-or-like activity in the analysis window.

caliber_meaning: group-chat two-way coverage over days
calculation_method: Days with at least one two-way send-or-like event divided by days in the window.
numerator: days with two-way send-or-like events
denominator: days in window

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the user-based and session-based variants.
interpretation_notes: Group-chat two-way coverage signal.
```

## Metric: Group Send or Like Message 2-Way Days/User

```yaml
group_name: [DM] DM 2-Way
metric_name: Group Send or Like Message 2-Way Days/User
metric_aliases:
  - Group Send or Like Message 2-Way Days per User

meaning_zh: 群聊双向发送或点赞消息天数/用户。
meaning_en: Average number of group-chat two-way active days per user.

caliber_meaning: group-chat two-way coverage per user
calculation_method: Average two-way active days per user in the analysis window.
numerator: days with two-way send-or-like events
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the day-ratio and session-based variants.
interpretation_notes: Group-chat two-way supporting coverage signal.
```

## Metric: Group Send or Like Message 2-Way session/User

```yaml
group_name: [DM] DM 2-Way
metric_name: Group Send or Like Message 2-Way session/User
metric_aliases:
  - Group Send or Like Message 2-Way session per User

meaning_zh: 群聊双向发送或点赞消息会话数/用户。
meaning_en: Average number of group-chat two-way sessions per user.

caliber_meaning: group-chat two-way session intensity per user
calculation_method: Average two-way sessions per user in the analysis window.
numerator: total two-way sessions
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the days/user variant and from the per-message variants.
interpretation_notes: Group-chat two-way engagement signal.
```

## Metric: Group Send or Like Message 2-Way/ User

```yaml
group_name: [DM] DM 2-Way
metric_name: Group Send or Like Message 2-Way/ User
metric_aliases:
  - Group Send or Like Message 2-Way per User

meaning_zh: 群聊双向发送或点赞消息数/用户。
meaning_en: Average number of group-chat two-way send-or-like events per user.

caliber_meaning: group-chat two-way intensity per user
calculation_method: Average two-way PV per user in the analysis window.
numerator: total two-way send-or-like PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the session-based and days-based variants.
interpretation_notes: Group-chat two-way intensity signal.
```

## Metric: Muf Send or Like Message 2-Way/ User

```yaml
group_name: [DM] DM 2-Way
metric_name: Muf Send or Like Message 2-Way/ User
metric_aliases:
  - MUF Send or Like Message 2-Way per User

meaning_zh: MUF 双向发送或点赞消息数/用户。
meaning_en: Average number of MUF two-way send-or-like events per user.

caliber_meaning: MUF two-way intensity per user
calculation_method: Average MUF two-way PV per user in the analysis window.
numerator: total MUF two-way send-or-like PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the group-send variant.
interpretation_notes: MUF two-way intensity signal.
```

## Metric: Send or Like Message 2-Way/ User

```yaml
group_name: [DM] DM 2-Way
metric_name: Send or Like Message 2-Way/ User
metric_aliases:
  - Send or Like Message 2-Way per User

meaning_zh: 双向发送或点赞消息数/用户。
meaning_en: Average number of two-way send-or-like events per user.

caliber_meaning: two-way intensity per user
calculation_method: Average two-way PV per user in the analysis window.
numerator: total two-way send-or-like PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the group-chat and MUF variants.
interpretation_notes: Broad two-way interaction signal.
```
