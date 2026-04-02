# Metrics By Group | Core-Key Metrics

These entries are confirmed, reusable formal metrics for the Core-Key Metrics group.

## Metric: StayDuration/U

```yaml
group_name: Core-Key Metrics
metric_name: StayDuration/U
metric_aliases:
  - Stay Duration/User

meaning_zh: 人均停留时长。
meaning_en: Average stay duration per user.

caliber_meaning: core consumption depth
calculation_method: Average stay duration per user over the analysis window.
numerator: total stay duration
denominator: users

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - time_window
  - user_id

neighbor_metric_diff: Do not confuse with PlayTime/U; this one is a broader stay-depth signal.
interpretation_notes: Frequently used as a core consumption guardrail.
```

## Metric: PubUser/U

```yaml
group_name: Core-Key Metrics
metric_name: PubUser/U
metric_aliases:
  - Publish User/User

meaning_zh: 发布视频用户数/用户。
meaning_en: Average number of publish users per user.

caliber_meaning: publish-user coverage
calculation_method: Ratio of publish-user count to users in the analysis window.
numerator: publish users
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Publish/U or Publish/PubUser; this is the user-count coverage variant.
interpretation_notes: Creative participation supplement.
```

## Metric: Publish/U

```yaml
group_name: Core-Key Metrics
metric_name: Publish/U
metric_aliases:
  - Publish/User

meaning_zh: 发布视频数/用户。
meaning_en: Average publish count per user.

caliber_meaning: publish intensity
calculation_method: Average number of publishes per user in the analysis window.
numerator: total publishes
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with PubUser/U; this is publish volume rather than publish-user coverage.
interpretation_notes: Creative intensity supplement.
```

## Metric: Play/U

```yaml
group_name: Core-Key Metrics
metric_name: Play/U
metric_aliases:
  - Play/User

meaning_zh: 播放视频数/用户。
meaning_en: Average number of plays per user.

caliber_meaning: video consumption breadth
calculation_method: Average number of plays per user in the analysis window.
numerator: total plays
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with PlayTime/U; this measures count rather than time spent.
interpretation_notes: Consumption breadth supplement.
```

## Metric: UVV/U

```yaml
group_name: Core-Key Metrics
metric_name: UVV/U
metric_aliases:
  - UVV/User

meaning_zh: 唯一视频播放数/用户。
meaning_en: Average unique video plays per user.

caliber_meaning: unique consumption breadth
calculation_method: Average unique video plays per user in the analysis window.
numerator: unique video plays
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Play/U; this is the unique-play variant.
interpretation_notes: Consumption breadth supplement.
```

## Metric: PlayTime/U

```yaml
group_name: Core-Key Metrics
metric_name: PlayTime/U
metric_aliases:
  - PlayTime/User

meaning_zh: 播放视频时长/用户。
meaning_en: Average play time per user.

caliber_meaning: video consumption depth
calculation_method: Average play time per user in the analysis window.
numerator: total play time
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Play/U; this measures duration rather than count.
interpretation_notes: Consumption depth supplement.
```

## Metric: Finish/Play

```yaml
group_name: Core-Key Metrics
metric_name: Finish/Play
metric_aliases:
  - Finish/Play Rate

meaning_zh: 视频完播率。
meaning_en: Video completion rate.

caliber_meaning: video completion quality
calculation_method: Completed plays divided by total plays.
numerator: finished plays
denominator: plays

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Finish/U; this one is a completion ratio rather than a per-user count.
interpretation_notes: Consumption quality supplement.
```

## Metric: Session/U

```yaml
group_name: Core-Key Metrics
metric_name: Session/U
metric_aliases:
  - Session/User

meaning_zh: Session数/用户。
meaning_en: Average session count per user.

caliber_meaning: session frequency
calculation_method: Average number of sessions per user in the analysis window.
numerator: total sessions
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with valid_session_cnt/User; this is the broad session-count variant.
interpretation_notes: Usage-frequency supplement.
```

## Metric: LoginRate

```yaml
group_name: Core-Key Metrics
metric_name: LoginRate
metric_aliases:
  - Login Rate

meaning_zh: APP 登录率。
meaning_en: App login rate.

caliber_meaning: login coverage
calculation_method: Logged-in users divided by active or eligible users, depending on the source definition.
numerator: logged-in users
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep the exact source caliber in mind; this is a generic login-coverage signal.
interpretation_notes: Basic product-state supplement.
```

## Metric: PlayTime/Play

```yaml
group_name: Core-Key Metrics
metric_name: PlayTime/Play
metric_aliases:
  - Play Time/Play

meaning_zh: 播放视频时长/播放。
meaning_en: Average watch time per play.

caliber_meaning: per-play watch depth
calculation_method: Average play time per play in the analysis window.
numerator: total play time
denominator: plays

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with PlayTime/U; this is per-play rather than per-user depth.
interpretation_notes: Consumption quality supplement.
```

## Metric: Play/I

```yaml
group_name: Core-Key Metrics
metric_name: Play/I
metric_aliases:
  - Play/Impression

meaning_zh: 播放视频数/曝光。
meaning_en: Average plays per impression.

caliber_meaning: impression-to-play conversion
calculation_method: Plays divided by impressions in the analysis window.
numerator: plays
denominator: impressions

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Play/U; this one is a conversion metric, not per-user activity.
interpretation_notes: Conversion supplement.
```

## Metric: Finish/U

```yaml
group_name: Core-Key Metrics
metric_name: Finish/U
metric_aliases:
  - Finish/User

meaning_zh: 完播视频数/用户。
meaning_en: Average number of finished videos per user.

caliber_meaning: completion volume per user
calculation_method: Average number of completed videos per user in the analysis window.
numerator: finished videos
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Finish/Play; this is a per-user count rather than a completion ratio.
interpretation_notes: Consumption quality supplement.
```

## Metric: Publish/PubUser

```yaml
group_name: Core-Key Metrics
metric_name: Publish/PubUser
metric_aliases:
  - Publish per PubUser

meaning_zh: 发布视频数/发布用户。
meaning_en: Average publish count per publish user.

caliber_meaning: publishing intensity per publish user
calculation_method: Average number of publishes per publish user in the analysis window.
numerator: publishes
denominator: publish users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Publish/U or PubUser/U; this is the publish-user-normalized variant.
interpretation_notes: Creative intensity supplement.
```

## Metric: Publish/Play

```yaml
group_name: Core-Key Metrics
metric_name: Publish/Play
metric_aliases:
  - Publish per Play

meaning_zh: 发布视频数/播放。
meaning_en: Average publishes per play.

caliber_meaning: publish-to-play ratio
calculation_method: Publishes divided by plays in the analysis window.
numerator: publishes
denominator: plays

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Play/I and Publish/U; this is a cross-behavior ratio.
interpretation_notes: Creative conversion supplement.
```

## Metric: RspLatency

```yaml
group_name: Core-Key Metrics
metric_name: RspLatency
metric_aliases:
  - Response Latency

meaning_zh: 响应延迟。
meaning_en: Response latency.

caliber_meaning: system response latency
calculation_method: Source-defined latency measurement.
numerator:
denominator:

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: System-experience metric; do not interpret as user engagement.
interpretation_notes: Performance supplement.
```
