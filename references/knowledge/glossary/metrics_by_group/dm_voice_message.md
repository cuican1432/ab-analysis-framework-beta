# Metrics By Group | DM Voice Message

These entries are confirmed, reusable formal metrics for the DM Voice Message group.

## Metric: Voice Message duration/user

```yaml
group_name: DM Voice Message
metric_name: Voice Message duration/user
metric_aliases:
  - Voice Message duration per user

meaning_zh: 语音消息时长/用户。
meaning_en: Average voice-message duration per user.

caliber_meaning: voice-message duration intensity per user
calculation_method: Average voice-message duration per user in the analysis window.
numerator: total voice-message duration
denominator: users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with the message-level duration variant below.
interpretation_notes: Voice usage depth supplement.
```

## Metric: Voice Message duration/message

```yaml
group_name: DM Voice Message
metric_name: Voice Message duration/message
metric_aliases:
  - Voice Message duration per message

meaning_zh: 语音消息时长/消息。
meaning_en: Average voice-message duration per message.

caliber_meaning: voice-message duration per message
calculation_method: Average voice-message duration per message in the analysis window.
numerator: total voice-message duration
denominator: messages

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with the per-user duration variant above.
interpretation_notes: Voice-message quality supplement.
```

## Metric: Show Voice Message Entrance pv/au

```yaml
group_name: DM Voice Message
metric_name: Show Voice Message Entrance pv/au
metric_aliases:
  - Show Voice Message Entrance

meaning_zh: 展示语音消息入口PV/活跃用户。
meaning_en: Average number of voice-message entrance exposures per active user.

caliber_meaning: voice-message entrance exposure intensity
calculation_method: Average entrance PV per active user in the analysis window.
numerator: total entrance PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant.
interpretation_notes: Entry-side exposure signal for voice messages.
```

## Metric: Show Voice Message Entrance uv/au

```yaml
group_name: DM Voice Message
metric_name: Show Voice Message Entrance uv/au
metric_aliases:
  - Show Voice Message Entrance UV

meaning_zh: 展示语音消息入口UV/活跃用户。
meaning_en: Average number of users exposed to the voice-message entrance per active user.

caliber_meaning: voice-message entrance exposure coverage
calculation_method: Average entrance UV per active user in the analysis window.
numerator: total entrance UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Entry-side coverage signal for voice messages.
```

## Metric: Start Record Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Start Record Voice Message pv/au
metric_aliases:
  - Start Record Voice Message

meaning_zh: 开始录制语音消息PV/活跃用户。
meaning_en: Average number of voice-record starts per active user.

caliber_meaning: voice-record start intensity
calculation_method: Average record-start PV per active user in the analysis window.
numerator: total record-start PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from send metrics.
interpretation_notes: Funnel-start signal for voice creation.
```

## Metric: Start Record Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Start Record Voice Message uv/au
metric_aliases:
  - Start Record Voice Message UV

meaning_zh: 开始录制语音消息UV/活跃用户。
meaning_en: Average number of users who start voice recording per active user.

caliber_meaning: voice-record start coverage
calculation_method: Average record-start UV per active user in the analysis window.
numerator: total record-start UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Funnel-start coverage signal for voice creation.
```

## Metric: UV Record/Show CTR

```yaml
group_name: DM Voice Message
metric_name: UV Record/Show CTR
metric_aliases:
  - UV Record Show CTR

meaning_zh: UV录制/展示转化率。
meaning_en: The conversion rate from entrance exposure to starting voice recording on a user basis.

caliber_meaning: user-level voice-record start conversion
calculation_method: Users who start voice recording divided by users exposed to the voice-message entrance.
numerator: users who start voice recording
denominator: users exposed to the voice-message entrance

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au exposure metrics and the send-stage metrics.
interpretation_notes: Voice-message entry conversion signal on a user basis.
```

## Metric: Cancel Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Cancel Voice Message pv/au
metric_aliases:
  - Cancel Voice Message

meaning_zh: 取消语音消息PV/活跃用户。
meaning_en: Average number of voice-message cancel events per active user.

caliber_meaning: voice-cancel intensity
calculation_method: Average cancel PV per active user in the analysis window.
numerator: total cancel PV
denominator: active users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from start-record metrics.
interpretation_notes: Funnel-friction signal for voice creation.
```

## Metric: Cancel Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Cancel Voice Message uv/au
metric_aliases:
  - Cancel Voice Message UV

meaning_zh: 取消语音消息UV/活跃用户。
meaning_en: Average number of users canceling voice messages per active user.

caliber_meaning: voice-cancel coverage
calculation_method: Average cancel UV per active user in the analysis window.
numerator: total cancel UV
denominator: active users

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Funnel-friction coverage signal for voice creation.
```

## Metric: Send Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Send Voice Message pv/au
metric_aliases:
  - Send Voice Message

meaning_zh: 发送语音消息PV/活跃用户。
meaning_en: Average number of sent voice messages per active user.

caliber_meaning: voice-send intensity
calculation_method: Average send PV per active user in the analysis window.
numerator: total voice-send PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from show/start/cancel metrics.
interpretation_notes: Voice send-chain result signal.
```

## Metric: Send Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Send Voice Message uv/au
metric_aliases:
  - Send Voice Message UV

meaning_zh: 发送语音消息UV/活跃用户。
meaning_en: Average number of users sending voice messages per active user.

caliber_meaning: voice-send coverage
calculation_method: Average send UV per active user in the analysis window.
numerator: total voice-send UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Voice send-chain coverage signal.
```

## Metric: Show Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Show Voice Message pv/au
metric_aliases:
  - Show Voice Message

meaning_zh: 展示语音消息PV/活跃用户。
meaning_en: Average number of voice-message show events per active user.

caliber_meaning: voice exposure intensity
calculation_method: Average show PV per active user in the analysis window.
numerator: total show PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from play metrics.
interpretation_notes: Voice exposure signal.
```

## Metric: Show Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Show Voice Message uv/au
metric_aliases:
  - Show Voice Message UV

meaning_zh: 展示语音消息UV/活跃用户。
meaning_en: Average number of users exposed to voice messages per active user.

caliber_meaning: voice exposure coverage
calculation_method: Average show UV per active user in the analysis window.
numerator: total show UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Voice exposure coverage signal.
```

## Metric: Play/Show Voice Message CTR

```yaml
group_name: DM Voice Message
metric_name: Play/Show Voice Message CTR
metric_aliases:
  - Play/Show CTR

meaning_zh: 语音消息播放/展示转化率。
meaning_en: Play-to-show conversion rate for voice messages.

caliber_meaning: voice play conversion
calculation_method: Played voice messages divided by shown voice messages.
numerator: voice plays
denominator: voice shows

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with play counts or completion rates.
interpretation_notes: Voice consumption conversion signal.
```

## Metric: Play Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Play Voice Message pv/au
metric_aliases:
  - Play Voice Message

meaning_zh: 播放语音消息PV/活跃用户。
meaning_en: Average number of voice-message plays per active user.

caliber_meaning: voice-play intensity
calculation_method: Average play PV per active user in the analysis window.
numerator: total play PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au and completion metrics.
interpretation_notes: Voice consumption signal.
```

## Metric: Play Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Play Voice Message uv/au
metric_aliases:
  - Play Voice Message UV

meaning_zh: 播放语音消息UV/活跃用户。
meaning_en: Average number of users playing voice messages per active user.

caliber_meaning: voice-play coverage
calculation_method: Average play UV per active user in the analysis window.
numerator: total play UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant and from finish metrics.
interpretation_notes: Voice consumption coverage signal.
```

## Metric: Finish Playing Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Finish Playing Voice Message pv/au
metric_aliases:
  - Finish Playing Voice Message

meaning_zh: 完播语音消息PV/活跃用户。
meaning_en: Average number of finished voice-message plays per active user.

caliber_meaning: voice completion intensity
calculation_method: Average finish-play PV per active user in the analysis window.
numerator: total finish-play PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from play or show counts.
interpretation_notes: Voice completion signal.
```

## Metric: Finish Playing Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Finish Playing Voice Message uv/au
metric_aliases:
  - Finish Playing Voice Message UV

meaning_zh: 完播语音消息UV/活跃用户。
meaning_en: Average number of users finishing voice-message plays per active user.

caliber_meaning: voice completion coverage
calculation_method: Average finish-play UV per active user in the analysis window.
numerator: total finish-play UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Voice completion coverage signal.
```

## Metric: Finish Playing/Play Voice Message Proportion pv/pv

```yaml
group_name: DM Voice Message
metric_name: Finish Playing/Play Voice Message Proportion pv/pv
metric_aliases:
  - Finish/Play Voice Message

meaning_zh: 语音消息完播/播放比例。
meaning_en: Completion ratio for voice-message plays.

caliber_meaning: voice completion quality
calculation_method: Finished voice plays divided by total voice plays.
numerator: finished voice plays
denominator: voice plays

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with play counts or play/show CTR.
interpretation_notes: Voice completion-quality signal.
```

## Metric: Send Private Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Send Private Voice Message pv/au
metric_aliases:
  - Send Private Voice Message

meaning_zh: 发送私聊语音消息PV/活跃用户。
meaning_en: Average number of private voice messages sent per active user.

caliber_meaning: private voice-send intensity
calculation_method: Average private voice send PV per active user in the analysis window.
numerator: total private voice-send PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from group-voice send metrics.
interpretation_notes: Private voice creation signal.
```

## Metric: Send Private Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Send Private Voice Message uv/au
metric_aliases:
  - Send Private Voice Message UV

meaning_zh: 发送私聊语音消息UV/活跃用户。
meaning_en: Average number of users sending private voice messages per active user.

caliber_meaning: private voice-send coverage
calculation_method: Average private voice send UV per active user in the analysis window.
numerator: total private voice-send UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant and from group-voice send metrics.
interpretation_notes: Private voice creation coverage signal.
```

## Metric: Send Group Voice Message pv/au

```yaml
group_name: DM Voice Message
metric_name: Send Group Voice Message pv/au
metric_aliases:
  - Send Group Voice Message

meaning_zh: 发送群聊语音消息PV/活跃用户。
meaning_en: Average number of group voice messages sent per active user.

caliber_meaning: group voice-send intensity
calculation_method: Average group voice send PV per active user in the analysis window.
numerator: total group voice-send PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from private-voice send metrics.
interpretation_notes: Group voice creation signal.
```

## Metric: Send Group Voice Message uv/au

```yaml
group_name: DM Voice Message
metric_name: Send Group Voice Message uv/au
metric_aliases:
  - Send Group Voice Message UV

meaning_zh: 发送群聊语音消息UV/活跃用户。
meaning_en: Average number of users sending group voice messages per active user.

caliber_meaning: group voice-send coverage
calculation_method: Average group voice send UV per active user in the analysis window.
numerator: total group voice-send UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant and from private-voice send metrics.
interpretation_notes: Group voice creation coverage signal.
```

## Metric: Play Voice Message in Entry pv/au

```yaml
group_name: DM Voice Message
metric_name: Play Voice Message in Entry pv/au
metric_aliases:
  - Play Voice Message in Entry

meaning_zh: 入口内播放语音消息PV/活跃用户。
meaning_en: Average number of voice-message plays in entry per active user.

caliber_meaning: entry-side voice-play intensity
calculation_method: Average in-entry voice-play PV per active user in the analysis window.
numerator: total in-entry voice-play PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from overall play metrics.
interpretation_notes: Entry-side voice consumption signal.
```

## Metric: Play Voice Message in Entry uv/au

```yaml
group_name: DM Voice Message
metric_name: Play Voice Message in Entry uv/au
metric_aliases:
  - Play Voice Message in Entry UV

meaning_zh: 入口内播放语音消息UV/活跃用户。
meaning_en: Average number of users playing voice messages in entry per active user.

caliber_meaning: entry-side voice-play coverage
calculation_method: Average in-entry voice-play UV per active user in the analysis window.
numerator: total in-entry voice-play UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Entry-side voice coverage signal.
```

## Metric: Finish Playing Voice Message in Entry pv/au

```yaml
group_name: DM Voice Message
metric_name: Finish Playing Voice Message in Entry pv/au
metric_aliases:
  - Finish Playing Voice Message in Entry

meaning_zh: 入口内完播语音消息PV/活跃用户。
meaning_en: Average number of finished in-entry voice plays per active user.

caliber_meaning: entry-side voice completion intensity
calculation_method: Average in-entry finish-play PV per active user in the analysis window.
numerator: total in-entry finish-play PV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the uv/au variant and from play metrics.
interpretation_notes: Entry-side voice completion signal.
```

## Metric: Finish Playing Voice Message in Entry uv/au

```yaml
group_name: DM Voice Message
metric_name: Finish Playing Voice Message in Entry uv/au
metric_aliases:
  - Finish Playing Voice Message in Entry UV

meaning_zh: 入口内完播语音消息UV/活跃用户。
meaning_en: Average number of users finishing in-entry voice plays per active user.

caliber_meaning: entry-side voice completion coverage
calculation_method: Average in-entry finish-play UV per active user in the analysis window.
numerator: total in-entry finish-play UV
denominator: active users

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from the pv/au variant.
interpretation_notes: Entry-side voice completion coverage signal.
```

## Metric: Play in Entry/Record Proportion pv/pv

```yaml
group_name: DM Voice Message
metric_name: Play in Entry/Record Proportion pv/pv
metric_aliases:
  - Entry Play/Record Proportion

meaning_zh: 入口播放/录制比例PV/PV。
meaning_en: The PV ratio between in-entry voice-play behavior and voice-record behavior.

caliber_meaning: entry-side play-vs-record ratio
calculation_method: In-entry play PV divided by record PV in the analysis window.
numerator: in-entry play PV
denominator: record PV

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with completion ratios or play/show CTR.
interpretation_notes: Entry-side usage balance signal for voice creation and consumption.
```

## Metric: Finish Playing in Entry/Play in Entry Proportion pv/pv

```yaml
group_name: DM Voice Message
metric_name: Finish Playing in Entry/Play in Entry Proportion pv/pv
metric_aliases:
  - Entry Finish/Play Proportion

meaning_zh: 入口完成播放/入口播放比例PV/PV。
meaning_en: The PV ratio between finished in-entry voice plays and in-entry voice plays.

caliber_meaning: entry-side completion ratio
calculation_method: Finished in-entry voice-play PV divided by in-entry play PV in the analysis window.
numerator: finished in-entry voice-play PV
denominator: in-entry play PV

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with Play/Show Voice Message CTR or completion counts.
interpretation_notes: Entry-side completion-quality signal for voice messages.
```

## Metric: Cancel/Record Proportion

```yaml
group_name: DM Voice Message
metric_name: Cancel/Record Proportion
metric_aliases:
  - Cancel/Record Proportion pv/pv
  - 录制取消率

meaning_zh: 取消/录制比例PV/PV。
meaning_en: The PV ratio of cancellation to recording-start behavior for voice messages.

caliber_meaning: voice-record cancellation ratio
calculation_method: Cancel PV divided by record-start PV in the analysis window.
numerator: cancel PV
denominator: record-start PV

polarity: lower_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with cancel coverage/count metrics or send-success CTR metrics.
interpretation_notes: Voice-record funnel friction signal.
```

## Metric: UV Send/Record CTR

```yaml
group_name: DM Voice Message
metric_name: UV Send/Record CTR
metric_aliases:
  - 发送成功率

meaning_zh: UV发送/录制转化率。
meaning_en: User-level conversion rate from starting voice recording to successfully sending a voice message.

caliber_meaning: voice-record-to-send conversion
calculation_method: Users who successfully send a voice message divided by users who start recording.
numerator: users who successfully send voice messages
denominator: users who start recording

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Do not confuse with UV Record/Show CTR; this one measures record-to-send closure rather than show-to-record conversion.
interpretation_notes: Voice-message send-chain completion signal.
```
