# Metrics By Group | [DM] DM Negative Feedback

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM Negative Feedback.

## Metric: block/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: block/user
metric_aliases:
  - block
  - 拉黑/用户数

meaning_zh: 拉黑次数/用户。
meaning_en: Average number of block events per user.

caliber_meaning: negative-feedback intensity per user
calculation_method: Average block events per user in the analysis window.
numerator: total block events
denominator: users

polarity: lower_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from mute/unmute and report metrics in the same group.
interpretation_notes: Core negative-feedback signal; decreases are favorable.
```

## Metric: block_user/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: block_user/user
metric_aliases:
  - block_user
  - 拉黑用户数/用户

meaning_zh: 拉黑用户数/用户。
meaning_en: Share of users who triggered block behavior in the analysis window.

caliber_meaning: block-user penetration / coverage
calculation_method: Blocking users divided by users in the analysis window.
numerator: total blocking users
denominator: users

polarity: lower_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from block/user; this one is blocker-coverage based.
interpretation_notes: Core negative-feedback signal; increases are unfavorable.
```

## Metric: unmute/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: unmute/user
metric_aliases:
  - unmute
  - 取消静音/用户数

meaning_zh: 取消静音数/用户。
meaning_en: Average number of unmute events per user.

caliber_meaning: negative-feedback reverse-action intensity per user
calculation_method: Average unmute events per user in the analysis window.
numerator: total unmutes
denominator: users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from block_user/user and mute_user/user.
interpretation_notes: Supporting negative-feedback signal.
```

## Metric: mute_user/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: mute_user/user
metric_aliases:
  - mute_user
  - 静音/用户数

meaning_zh: 静音用户数/用户。
meaning_en: Average number of mute-user actions per user.

caliber_meaning: negative-feedback intensity per user
calculation_method: Average mute-user events per user in the analysis window.
numerator: total mute-user events
denominator: users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from block_user/user and unmute/user.
interpretation_notes: Supporting negative-feedback signal.
```

## Metric: unmute_user/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: unmute_user/user
metric_aliases:
  - unmute_user
  - 取消静音用户/用户数

meaning_zh: 取消静音用户数/用户。
meaning_en: Average number of unmute-user actions per user.

caliber_meaning: negative-feedback reverse-action intensity per user
calculation_method: Average unmute-user events per user in the analysis window.
numerator: total unmute-user events
denominator: users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from unmute/user and mute_user/user.
interpretation_notes: Supporting negative-feedback signal.
```

## Metric: click_report/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: click_report/user
metric_aliases:
  - click_report
  - 举报点击/用户数

meaning_zh: 举报点击数/用户。
meaning_en: Average number of report clicks per user.

caliber_meaning: report-click intensity per user
calculation_method: Average report-click events per user in the analysis window.
numerator: total report clicks
denominator: users

polarity: lower_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from click_report_user/user; this one is click-count based.
interpretation_notes: Core user-risk signal; increases are unfavorable.
```

## Metric: click_report_user/user

```yaml
group_name: [DM] DM Negative Feedback
metric_name: click_report_user/user
metric_aliases:
  - click_report_user
  - 举报用户/用户数

meaning_zh: 举报用户数/用户。
meaning_en: Share of users who triggered report behavior in the analysis window.

caliber_meaning: report-user penetration / coverage
calculation_method: Reporting users divided by users in the analysis window.
numerator: total reporting users
denominator: users

polarity: lower_is_better
priority_hint: P0

neighbor_metric_diff: Keep distinct from click_report/user; this one is reporter-coverage based.
interpretation_notes: Core user-risk signal; increases are unfavorable.
```
