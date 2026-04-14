# Metrics By Group | Key Project-DM

Reference entry for These entries are confirmed, reusable formal metrics for the Key Project-DM.

## Metric: Social MUF Send or Like Message PV/User

```yaml
group_name: Key Project-DM
metric_name: Social MUF Send or Like Message PV/User
metric_aliases:
  - Social MUF Send or Like Message/User

meaning_zh: 社交MUF发送或点赞消息数/用户。
meaning_en: Average number of social-MUF send-or-like messages per user.

caliber_meaning: core social DM interaction intensity per user
calculation_method: Average social MUF send-or-like PV per user in the analysis window.
numerator: total social MUF send-or-like message PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with Send or Like Message PV/User or Send Message PV/User; this one is the social-MUF variant.
interpretation_notes: Core social-interaction strength signal.
```

## Metric: Social MUF Send or Like Message Days/Days

```yaml
group_name: Key Project-DM
metric_name: Social MUF Send or Like Message Days/Days
metric_aliases:
  - Muf DM Penetration
  - Muf DM Pen

meaning_zh: 社交MUF发送或点赞消息天数/天数。
meaning_en: Share of days with social-MUF send-or-like activity in the analysis window.

caliber_meaning: social DM penetration over days
calculation_method: Days with at least one social MUF send-or-like event divided by days in the window.
numerator: days with social MUF send-or-like events
denominator: days in window

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Do not confuse with Send or Like Message Days/Days or Group Send or Like Message Days/Days.
interpretation_notes: Core DM penetration signal.
```

## Metric: Social MUF Send or Like Message Days/User

```yaml
group_name: Key Project-DM
metric_name: Social MUF Send or Like Message Days/User
metric_aliases:
  - Social MUF Send or Like Message Days per User

meaning_zh: 社交MUF发送或点赞消息天数/用户。
meaning_en: Average number of social-MUF send-or-like active days per user.

caliber_meaning: social DM penetration per user
calculation_method: Average social MUF send-or-like active days per user in the analysis window.
numerator: days with social MUF send-or-like events
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with Social MUF Send or Like Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Supporting penetration signal for the social-MUF family.
```

## Metric: Social MUF Send or Like Message Pair/User

```yaml
group_name: Key Project-DM
metric_name: Social MUF Send or Like Message Pair/User
metric_aliases:
  - Last 7-day Social MUF Send or Like Message Pair/User

meaning_zh: 社交MUF发送或点赞消息对/用户。
meaning_en: Average number of social-MUF send-or-like message pairs per user.

caliber_meaning: social relationship interaction intensity per user
calculation_method: Average social MUF send-or-like pairs per user in the analysis window.
numerator: total social MUF send-or-like message pairs
denominator: users

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Do not confuse with Social MUF Send or Like Message PV/User; this one is pair-count based.
interpretation_notes: Strong core relationship-strength signal.
```

## Metric: Send or Like Message PV/User

```yaml
group_name: Key Project-DM
metric_name: Send or Like Message PV/User
metric_aliases:
  - Send or Like Message/User

meaning_zh: 发送或点赞消息数/用户。
meaning_en: Average number of send-or-like messages per user.

caliber_meaning: broad DM interaction intensity per user
calculation_method: Average send-or-like PV per user in the analysis window.
numerator: total send-or-like message PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Social MUF Send or Like Message PV/User; this is the broader non-social-MUF variant.
interpretation_notes: Broad DM interaction signal.
```

## Metric: Send or Like Message Days/Days

```yaml
group_name: Key Project-DM
metric_name: Send or Like Message Days/Days
metric_aliases:
  - DM Penetration
  - DM Pen
  - 私信渗透（包括群聊）

meaning_zh: 发送或点赞消息天数/天数。
meaning_en: Share of days with send-or-like activity in the analysis window.

caliber_meaning: broad DM penetration over days
calculation_method: Days with at least one send-or-like event divided by days in the window.
numerator: days with send-or-like events
denominator: days in window

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with the social-MUF or group-chat-specific variants.
interpretation_notes: Broad DM penetration signal.
```

## Metric: Send or Like Message Days/User

```yaml
group_name: Key Project-DM
metric_name: Send or Like Message Days/User
metric_aliases:
  - Send or Like Message Days per User

meaning_zh: 发送或点赞消息天数/用户。
meaning_en: Average number of send-or-like active days per user.

caliber_meaning: broad DM penetration per user
calculation_method: Average send-or-like active days per user in the analysis window.
numerator: days with send-or-like events
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send or Like Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Supporting penetration signal.
```

## Metric: Receive or Liked Message Days/Days

```yaml
group_name: Key Project-DM
metric_name: Receive or Liked Message Days/Days
metric_aliases:
  - Receive or Liked Message Days

meaning_zh: 接收或被点赞消息天数/天数。
meaning_en: Share of days with receive-or-liked activity in the analysis window.

caliber_meaning: receive-side coverage over days
calculation_method: Days with at least one receive-or-liked event divided by days in the window.
numerator: days with receive-or-liked events
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Receive or Liked Message Days/User; this one is a day-ratio coverage metric.
interpretation_notes: Receive-side coverage signal.
```

## Metric: Receive or Liked Message Days/User

```yaml
group_name: Key Project-DM
metric_name: Receive or Liked Message Days/User
metric_aliases:
  - Receive or Liked Message Days per User

meaning_zh: 接收或被点赞消息天数/用户。
meaning_en: Average number of receive-or-liked active days per user.

caliber_meaning: receive-side coverage per user
calculation_method: Average receive-or-liked active days per user in the analysis window.
numerator: days with receive-or-liked events
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Receive or Liked Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Supporting receive-side coverage signal.
```

## Metric: Receive or Liked Message PV/User

```yaml
group_name: Key Project-DM
metric_name: Receive or Liked Message PV/User
metric_aliases:
  - Receive or Liked Message/User

meaning_zh: 接收或被点赞消息数/用户。
meaning_en: Average number of receive-or-liked messages per user.

caliber_meaning: receive-side interaction intensity per user
calculation_method: Average receive-or-liked PV per user in the analysis window.
numerator: total receive-or-liked message PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Social MUF Send or Like Message PV/User; this is the receive-side variant.
interpretation_notes: Supporting receive-side intensity signal.
```

## Metric: FYP Internal Share PV/User

```yaml
group_name: Key Project-DM
metric_name: FYP Internal Share PV/User
metric_aliases:
  - FYP Internal Share/User

meaning_zh: FYP站内分享PV/用户。
meaning_en: Average number of in-app shares from FYP per user.

caliber_meaning: FYP share intensity per user
calculation_method: Average FYP internal-share PV per user in the analysis window.
numerator: total FYP internal-share PV
denominator: users

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Do not confuse with Internal Share PV/User; this one is explicitly FYP-sourced.
interpretation_notes: Core share-intensity signal.
```

## Metric: Group Send or Like Message Days/Days

```yaml
group_name: Key Project-DM
metric_name: Group Send or Like Message Days/Days
metric_aliases:
  - GC Penetration
  - Group Chat Penetration
  - Group Chat Pen

meaning_zh: 群组发送或点赞消息天数/天数。
meaning_en: Share of days with group-chat send-or-like activity in the analysis window.

caliber_meaning: group-chat coverage over days
calculation_method: Days with at least one group send-or-like event divided by days in the window.
numerator: days with group send-or-like events
denominator: days in window

polarity: higher_is_better
priority_hint: P0

neighbor_metric_diff: Do not confuse with Send or Like Message Days/Days; this one is group-chat specific.
interpretation_notes: Core group-chat penetration signal.
```

## Metric: Group Send or Like Message Days/User

```yaml
group_name: Key Project-DM
metric_name: Group Send or Like Message Days/User
metric_aliases:
  - Group Send or Like Message Days per User

meaning_zh: 群组发送或点赞消息天数/用户。
meaning_en: Average number of group-chat send-or-like active days per user.

caliber_meaning: group-chat coverage per user
calculation_method: Average group send-or-like active days per user in the analysis window.
numerator: days with group send-or-like events
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with Group Send or Like Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Supporting group-chat coverage signal.
```

## Metric: Last 7-day Social MUF Send or Like Message Pair/User

```yaml
group_name: Key Project-DM
metric_name: Last 7-day Social MUF Send or Like Message Pair/User
metric_aliases:
  - Last 7-day Social MUF Send or Like Message Pair

meaning_zh: 最近7天社交MUF发送或点赞消息对/用户。
meaning_en: Average number of social-MUF send-or-like message pairs per user in the last 7 days.

caliber_meaning: short-window social relationship intensity per user
calculation_method: Average social MUF send-or-like pairs per user within the last 7 day window.
numerator: total social MUF send-or-like message pairs within last 7 days
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Same family as Social MUF Send or Like Message Pair/User, but with a shorter lookback window.
interpretation_notes: Short-cycle supplement for relationship strength.
```
