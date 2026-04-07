# Metrics By Group | [DM] DM Sticker

Reference entry for These entries are confirmed, reusable formal metrics for the [DM] DM Sticker.

## Metric: Open Sticker Panel pv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Open Sticker Panel pv/au
metric_aliases:
  - Open Sticker Panel

meaning_zh: 打开贴纸面板的曝光/动作量。
meaning_en: The number of opens or exposures for the sticker panel.

caliber_meaning: sticker-panel exposure / action count
calculation_method: Count of sticker-panel open events per analysis window.
numerator: total open-sticker-panel events
denominator: users or actions depending on report calibration

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from sticker-send and sticker-usage metrics.
interpretation_notes: Core entry metric for the sticker path.
```

## Metric: Send Big Sticker pv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Send Big Sticker pv/au
metric_aliases:
  - Send Big Sticker

meaning_zh: 发送大贴纸的动作量。
meaning_en: The count of big-sticker send actions.

caliber_meaning: big-sticker send count
calculation_method: Count of big-sticker send events per analysis window.
numerator: total big-sticker sends
denominator: users or actions depending on report calibration

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Big Sticker uv/au.
interpretation_notes: Sticker sending signal.
```

## Metric: Send Big Sticker uv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Send Big Sticker uv/au
metric_aliases:
  - Send Big Sticker UV

meaning_zh: 发送大贴纸的去重用户量。
meaning_en: The number of unique users who send big stickers.

caliber_meaning: big-sticker sending user reach
calculation_method: Unique users with at least one big-sticker send event per analysis window.
numerator: users who sent big stickers
denominator: all users in scope

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from Send Big Sticker pv/au.
interpretation_notes: Sticker sending reach signal.
```

## Metric: Send Favourites Tab Sticker pv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Send Favourites Tab Sticker pv/au
metric_aliases:
  - Send Favourites Sticker

meaning_zh: 从收藏贴纸页发送贴纸的动作量。
meaning_en: The count of sticker send actions from the favourites tab.

caliber_meaning: favourites-tab sticker send count
calculation_method: Count of send events originating from the favourites tab.
numerator: total favourites-tab sticker sends
denominator: users or actions depending on report calibration

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from other sticker entry-path metrics.
interpretation_notes: Sticker path usage via favourites tab.
```

## Metric: Send SA uv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Send SA uv/au
metric_aliases:
  - Send SA

meaning_zh: 发送 SA 相关动作的去重用户量。
meaning_en: The number of unique users who perform the SA-related send action.

caliber_meaning: SA-related sending reach
calculation_method: Unique users with at least one SA-related send event per analysis window.
numerator: users with SA-related sends
denominator: all users in scope

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: The acronym SA is retained as shown in the report source; expand only if the source glossary confirms it.
interpretation_notes: Keep wording conservative; confirm acronym expansion before formal reporting if needed.
```

## Metric: Send Typing Recommendation Sticker uv/au

```yaml
group_name: [DM] DM Sticker
metric_name: Send Typing Recommendation Sticker uv/au
metric_aliases:
  - Typing Recommendation Sticker Send

meaning_zh: 发送打字推荐贴纸的去重用户量。
meaning_en: The number of unique users who send typing-recommendation stickers.

caliber_meaning: typing-recommendation sticker reach
calculation_method: Unique users with at least one typing-recommendation sticker send event per analysis window.
numerator: users who sent typing-recommendation stickers
denominator: all users in scope

polarity: higher_is_better
priority_hint: P2

neighbor_metric_diff: Keep distinct from other sticker-entry or recommendation metrics.
interpretation_notes: Supporting sticker-usage signal.
```
