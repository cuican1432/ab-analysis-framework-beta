# Metrics By Group | TnS DM Private Sender Metrics - Msg Level

Reference entry for These entries are confirmed, reusable formal metrics for the TnS DM Private Sender Metrics - Msg Level.

## Metric: feedback_appeal_success_rate_msg

```yaml
group_name: TnS DM Private Sender Metrics - Msg Level
metric_name: feedback_appeal_success_rate_msg
metric_aliases:
  - message-level feedback appeal success rate

meaning_zh: 消息层反馈申诉成功率。
meaning_en: The success rate of feedback appeals at the message level.

caliber_meaning: appeal success rate at msg level
calculation_method: Successful appeal count divided by total appeal count for message-level feedback events.
numerator: successful appeals
denominator: total appeals

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - message_level
  - appeal_type

notes: Keep this separate from sender-side conversation-level and group-chat TnS metrics.

neighbor_metric_diff: Keep this separate from group-level or conversation-level appeal rates.
interpretation_notes: Trust-and-safety support metric for sender-side message-level review outcomes.
```
