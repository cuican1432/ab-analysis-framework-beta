# Metrics By Group | DM Core

These entries are confirmed, reusable formal metrics for the DM Core group.

## Metric: Send Message PV/User

```yaml
group_name: DM Core
metric_name: Send Message PV/User
metric_aliases:
  - Send Message/User

meaning_zh: 每用户发送消息量。
meaning_en: Average number of message sends per user.

caliber_meaning: send intensity per user
calculation_method: Average send PV per user in the analysis window.
numerator: total send message PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send or Like Message PV/User, Social MUF Send or Like Message PV/User, or the day-based variants.
interpretation_notes: Core DM send-intensity signal.
```

## Metric: Send Message Days/Days

```yaml
group_name: DM Core
metric_name: Send Message Days/Days
metric_aliases:
  - Send Message Days

meaning_zh: 发送消息天数/天数。
meaning_en: Share of days with at least one send event in the analysis window.

caliber_meaning: send coverage over days
calculation_method: Days with at least one send event divided by days in the window.
numerator: days with sends
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send Message Days/User; this one is a day-ratio coverage metric.
interpretation_notes: Useful for judging whether send behavior becomes broader across days.
```

## Metric: Send Message Days/User

```yaml
group_name: DM Core
metric_name: Send Message Days/User
metric_aliases:
  - Send Message Days per User

meaning_zh: 发送消息天数/用户。
meaning_en: Average number of send-active days per user.

caliber_meaning: send coverage per user
calculation_method: Average send-active days per user in the analysis window.
numerator: days with sends
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Useful as a supporting signal for send coverage.
```

## Metric: Like Message Days/Days

```yaml
group_name: DM Core
metric_name: Like Message Days/Days
metric_aliases:
  - Like Message Days

meaning_zh: 点赞消息天数/天数。
meaning_en: Share of days with at least one like event in the analysis window.

caliber_meaning: like coverage over days
calculation_method: Days with at least one like event divided by days in the window.
numerator: days with likes
denominator: days in window

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Like Message Days/User; this one is a day-ratio coverage metric.
interpretation_notes: Useful for judging whether like behavior becomes broader across days.
```

## Metric: Like Message Days/User

```yaml
group_name: DM Core
metric_name: Like Message Days/User
metric_aliases:
  - Like Message Days per User

meaning_zh: 点赞消息天数/用户。
meaning_en: Average number of like-active days per user.

caliber_meaning: like coverage per user
calculation_method: Average like-active days per user in the analysis window.
numerator: days with likes
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Like Message Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Useful as a supporting signal for like coverage.
```

## Metric: Like Message PV/User

```yaml
group_name: DM Core
metric_name: Like Message PV/User
metric_aliases:
  - Like Message/User

meaning_zh: 每用户点赞消息量。
meaning_en: Average number of likes per user.

caliber_meaning: like intensity per user
calculation_method: Average like PV per user in the analysis window.
numerator: total like message PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send Message PV/User or Internal Share PV/User; this one is the like-intensity signal.
interpretation_notes: Core DM like-intensity signal.
```

## Metric: Internal Share Days/Days

```yaml
group_name: DM Core
metric_name: Internal Share Days/Days
metric_aliases:
  - Internal Share Days

meaning_zh: 内部分享天数/天数。
meaning_en: Share of days with at least one internal share event in the analysis window.

caliber_meaning: internal-share coverage over days
calculation_method: Days with at least one internal share event divided by days in the window.
numerator: days with internal shares
denominator: days in window

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with Internal Share Days/User or Internal Share PV/User; this is the day-ratio coverage metric.
interpretation_notes: Core share coverage signal.
```

## Metric: Internal Share Days/User

```yaml
group_name: DM Core
metric_name: Internal Share Days/User
metric_aliases:
  - Internal Share Days per User

meaning_zh: 内部分享天数/用户。
meaning_en: Average number of internal-share-active days per user.

caliber_meaning: internal-share coverage per user
calculation_method: Average internal-share-active days per user in the analysis window.
numerator: days with internal shares
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with Internal Share Days/Days; this one is per-user coverage rather than day-ratio coverage.
interpretation_notes: Supporting signal for share coverage.
```

## Metric: Internal Share PV/User

```yaml
group_name: DM Core
metric_name: Internal Share PV/User
metric_aliases:
  - Internal Share/User

meaning_zh: 内部分享PV/用户。
meaning_en: Average number of internal shares per user.

caliber_meaning: internal-share intensity per user
calculation_method: Average internal-share PV per user in the analysis window.
numerator: total internal share PV
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with FYP Internal Share PV/User; this one is the generic internal-share variant.
interpretation_notes: Supporting share-intensity signal.
```

## Metric: Chat Play PV/User

```yaml
group_name: DM Core
metric_name: Chat Play PV/User
metric_aliases:
  - Chat Play/User

meaning_zh: 会话框内聊天视频播放PV/用户。
meaning_en: Average chat video plays per user inside the conversation surface.

caliber_meaning: in-chat video consumption intensity
calculation_method: Average chat-play PV per user in the analysis window.
numerator: total chat play PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep separate from general Play/U and PlayTime/U metrics.
interpretation_notes: Supporting video-consumption signal within DM chat.
```

## Metric: Stay Duration/User

```yaml
group_name: DM Core
metric_name: Stay Duration/User
metric_aliases:
  - StayDuration/U

meaning_zh: 每用户停留时长。
meaning_en: Average stay duration per user.

caliber_meaning: core consumption depth
calculation_method: Average stay duration per user over the analysis window.
numerator: total stay duration
denominator: users

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Do not confuse with PlayTime/U; this one is a broader stay-depth signal.
interpretation_notes: Frequently used as a core consumption guardrail.
```

## Metric: Enter Chat PV/User

```yaml
group_name: DM Core
metric_name: Enter Chat PV/User
metric_aliases:
  - Enter Chat/User

meaning_zh: 每用户进入聊天次数。
meaning_en: Average number of chat-entry events per user.

caliber_meaning: chat entry intensity per user
calculation_method: Average enter-chat PV per user in the analysis window.
numerator: total enter chat PV
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with New Enter Chat PV/User; this is the general-entry variant.
interpretation_notes: Useful for judging whether entry usage increases.
```

## Metric: New Send Message PV/User

```yaml
group_name: DM Core
metric_name: New Send Message PV/User
metric_aliases:
  - New Send Message/User

meaning_zh: 新发送消息PV/用户。
meaning_en: Average number of send events per new user.

caliber_meaning: new-user send intensity
calculation_method: Average send PV per new user in the analysis window.
numerator: total new-user send PV
denominator: new users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Send Message PV/User; this one is restricted to new users.
interpretation_notes: Useful for detecting whether the experiment changes new-user sending.
```

## Metric: New Enter Chat PV/User

```yaml
group_name: DM Core
metric_name: New Enter Chat PV/User
metric_aliases:
  - New Enter Chat/User

meaning_zh: 新进入聊天PV/用户。
meaning_en: Average number of chat-entry events per new user.

caliber_meaning: new-user chat-entry intensity
calculation_method: Average enter-chat PV per new user in the analysis window.
numerator: total new-user enter-chat PV
denominator: new users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Enter Chat PV/User; this one is restricted to new users.
interpretation_notes: Useful for new-user entry behavior analysis.
```
