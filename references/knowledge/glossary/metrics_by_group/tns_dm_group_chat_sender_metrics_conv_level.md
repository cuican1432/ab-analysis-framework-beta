# Metrics By Group | TnS DM Group Chat Sender Metrics - Conv Level

These entries are confirmed, reusable formal metrics for the TnS DM Group Chat Sender Metrics - Conv Level group.

## Metric: notice_rate_groupcov

```yaml
group_name: TnS DM Group Chat Sender Metrics - Conv Level
metric_name: notice_rate_groupcov
metric_aliases:
  - group conversation notice rate

meaning_zh: 群聊会话层通知率。
meaning_en: The notice rate at the group-conversation level.

caliber_meaning: group-conversation notice coverage
calculation_method: Notice-triggered count divided by eligible group-conversation count in the window.
numerator: notice-triggered group-conversation events
denominator: eligible group-conversation events

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - conversation_level
  - appeal_type

notes: Use this group only for sender-side group-chat conversation-level signals; keep it separate from message-level variants.

neighbor_metric_diff: Keep distinct from report appeal success metrics in the same group.
interpretation_notes: TnS support metric for group-chat sender-side conversation level.
```

## Metric: report_appeal_success_rate_groupcov

```yaml
group_name: TnS DM Group Chat Sender Metrics - Conv Level
metric_name: report_appeal_success_rate_groupcov
metric_aliases:
  - group conversation report appeal success rate

meaning_zh: 群聊会话层举报申诉成功率。
meaning_en: The success rate of report appeals at the group-conversation level.

caliber_meaning: report appeal success rate at group-conversation level
calculation_method: Successful group-conversation appeal count divided by total group-conversation appeals.
numerator: successful appeals
denominator: total appeals

polarity: higher_is_better
priority_hint: P1

neighbor_metric_diff: Keep distinct from message-level or receiver-side appeal rates.
interpretation_notes: Trust-and-safety support metric for group-chat sender-side conversation level.
```
