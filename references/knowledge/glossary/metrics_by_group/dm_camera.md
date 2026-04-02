# Metrics By Group | [DM] DM Camera

These entries are confirmed, reusable formal metrics for the [DM] DM Camera group.

## Metric: Send Camera Message uv/au

```yaml
group_name: [DM] DM Camera
metric_name: Send Camera Message uv/au
metric_aliases:
  - Send Camera Message

meaning_zh: 使用 DM Camera 发送消息的用户占比/强度。
meaning_en: User share or intensity of sending messages via DM Camera.

caliber_meaning: DM Camera send-chain usage
calculation_method: Source-defined ratio or intensity measure of DM Camera send behavior.
numerator:
denominator:

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the upload-chain and shoot-page-entry variants in the same group.
interpretation_notes: Useful for understanding whether DM Camera sending is being driven.
```

## Metric: Send Camera Message Upload pv/uv

```yaml
group_name: [DM] DM Camera
metric_name: Send Camera Message Upload pv/uv
metric_aliases:
  - Send Camera Message Upload

meaning_zh: DM Camera 上传链路强度。
meaning_en: Upload-chain strength for DM Camera.

caliber_meaning: DM Camera upload efficiency
calculation_method: Source-defined ratio or intensity measure of upload behavior after entering DM Camera.
numerator:
denominator:

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the send and entry variants in the same group.
interpretation_notes: Useful for understanding whether DM Camera deep usage is being strengthened.
```

## Metric: Enter DM Camera video shoot page uv/au

```yaml
group_name: [DM] DM Camera
metric_name: Enter DM Camera video shoot page uv/au
metric_aliases:
  - Enter DM Camera shoot page

meaning_zh: 进入 DM Camera 拍摄页的用户占比/强度。
meaning_en: User share or intensity of entering the DM Camera video shoot page.

caliber_meaning: DM Camera shoot-page entry
calculation_method: Source-defined ratio or intensity measure of shoot-page entry behavior.
numerator:
denominator:

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from the edit-page entry variant.
interpretation_notes: Useful for understanding DM Camera entry usage.
```
