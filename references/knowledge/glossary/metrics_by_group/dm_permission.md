# Metrics By Group | [DM] DM Permission

These entries are confirmed, reusable formal metrics for the [DM] DM Permission group.

## Metric: on_ratio

```yaml
group_name: [DM] DM Permission
metric_name: on_ratio
metric_aliases:
  - permission on ratio

meaning_zh: 私信权限开启占比。
meaning_en: Share of users with DM permission turned on.

caliber_meaning: permission-on share
calculation_method: Users with permission on divided by eligible users in the window.
numerator: users with permission on
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from off_ratio and disabled_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: off_ratio

```yaml
group_name: [DM] DM Permission
metric_name: off_ratio
metric_aliases:
  - permission off ratio

meaning_zh: 私信权限关闭占比。
meaning_en: Share of users with DM permission turned off.

caliber_meaning: permission-off share
calculation_method: Users with permission off divided by eligible users in the window.
numerator: users with permission off
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from on_ratio and disabled_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: unknown_ratio

```yaml
group_name: [DM] DM Permission
metric_name: unknown_ratio
metric_aliases:
  - permission unknown ratio

meaning_zh: 私信权限未知占比。
meaning_en: Share of users whose DM permission status is unknown.

caliber_meaning: unknown permission-state share
calculation_method: Users with unknown permission status divided by eligible users in the window.
numerator: users with unknown permission status
denominator: eligible users

polarity: descriptive_only
priority_hint: P2

neighbor_metric_diff: Keep distinct from on_ratio, off_ratio, and disabled_ratio.
interpretation_notes: Data-distribution signal rather than a directional business metric.
```

## Metric: everyone_ratio

```yaml
group_name: [DM] DM Permission
metric_name: everyone_ratio
metric_aliases:
  - everyone can message ratio

meaning_zh: 所有人可发消息占比。
meaning_en: Share of users whose DM permission is set to everyone.

caliber_meaning: everyone-access share
calculation_method: Users with everyone-access permission divided by eligible users in the window.
numerator: users with everyone-access permission
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from suggested_friends_ratio and friends_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: suggested_friends_ratio

```yaml
group_name: [DM] DM Permission
metric_name: suggested_friends_ratio
metric_aliases:
  - suggested friends ratio

meaning_zh: 推荐好友可发消息占比。
meaning_en: Share of users whose DM permission is set to suggested friends.

caliber_meaning: suggested-friends access share
calculation_method: Users with suggested-friends permission divided by eligible users in the window.
numerator: users with suggested-friends permission
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from friends_ratio and everyone_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: friends_ratio

```yaml
group_name: [DM] DM Permission
metric_name: friends_ratio
metric_aliases:
  - friends ratio

meaning_zh: 好友可发消息占比。
meaning_en: Share of users whose DM permission is set to friends.

caliber_meaning: friends-only access share
calculation_method: Users with friends-only permission divided by eligible users in the window.
numerator: users with friends-only permission
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from suggested_friends_ratio and everyone_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: no_one_ratio

```yaml
group_name: [DM] DM Permission
metric_name: no_one_ratio
metric_aliases:
  - no one ratio

meaning_zh: 无人可发消息占比。
meaning_en: Share of users whose DM permission is set to no one.

caliber_meaning: no-one access share
calculation_method: Users with no-one permission divided by eligible users in the window.
numerator: users with no-one permission
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from disabled_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: disabled_ratio

```yaml
group_name: [DM] DM Permission
metric_name: disabled_ratio
metric_aliases:
  - disabled ratio

meaning_zh: 私信权限禁用占比。
meaning_en: Share of users with DM permission disabled.

caliber_meaning: disabled permission share
calculation_method: Users with disabled permission divided by eligible users in the window.
numerator: users with disabled permission
denominator: eligible users

polarity: depends_on_context
priority_hint: P1

neighbor_metric_diff: Keep distinct from no_one_ratio.
interpretation_notes: Permission-state distribution signal.
```

## Metric: on_to_off_user/user

```yaml
group_name: [DM] DM Permission
metric_name: on_to_off_user/user
metric_aliases:
  - on to off user

meaning_zh: 从开启转为关闭的用户数/用户。
meaning_en: Average number of users switching from on to off per user.

caliber_meaning: on-to-off transition intensity per user
calculation_method: Users switching from on to off divided by users in the window.
numerator: users switching on to off
denominator: users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from unknown-to-off and off-to-on transition metrics.
interpretation_notes: Permission transition signal.
```

## Metric: unknown_to_off_user/user

```yaml
group_name: [DM] DM Permission
metric_name: unknown_to_off_user/user
metric_aliases:
  - unknown to off user

meaning_zh: 从未知转为关闭的用户数/用户。
meaning_en: Average number of users switching from unknown to off per user.

caliber_meaning: unknown-to-off transition intensity per user
calculation_method: Users switching from unknown to off divided by users in the window.
numerator: users switching unknown to off
denominator: users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from on_to_off_user/user and off_to_on_user/user.
interpretation_notes: Permission transition signal.
```

## Metric: off_to_on_user/user

```yaml
group_name: [DM] DM Permission
metric_name: off_to_on_user/user
metric_aliases:
  - off to on user

meaning_zh: 从关闭转为开启的用户数/用户。
meaning_en: Average number of users switching from off to on per user.

caliber_meaning: off-to-on transition intensity per user
calculation_method: Users switching from off to on divided by users in the window.
numerator: users switching off to on
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from on_to_off_user/user and unknown_to_on_uv/user.
interpretation_notes: Permission transition signal.
```

## Metric: unknown_to_on_uv/user

```yaml
group_name: [DM] DM Permission
metric_name: unknown_to_on_uv/user
metric_aliases:
  - unknown to on uv

meaning_zh: 从未知转为开启的去重用户数/用户。
meaning_en: Average number of unique users switching from unknown to on per user.

caliber_meaning: unknown-to-on unique-user transition intensity
calculation_method: Unique users switching from unknown to on divided by users in the window.
numerator: unique users switching unknown to on
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from off_to_on_user/user.
interpretation_notes: Permission transition signal.
```
