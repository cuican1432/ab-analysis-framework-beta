# Metrics By Group | TnS DM Group Chat Sender Metrics - Msg Level

Reference entry for These entries are confirmed, reusable formal metrics for the TnS DM Group Chat Sender Metrics - Msg Level.

## Metric: report_appeal_success_rate_groupmsg

```yaml
group_name: TnS DM Group Chat Sender Metrics - Msg Level
metric_name: report_appeal_success_rate_groupmsg
metric_aliases:
  - group message report appeal success rate

meaning_zh: 群聊消息层举报申诉成功率。
meaning_en: The success rate of report appeals at the group-message level.

caliber_meaning: report appeal success rate at group-message level
calculation_method: Successful group-message appeal count divided by total group-message appeals.
numerator: successful appeals
denominator: total appeals

polarity: higher_is_better
priority_hint: P1
common_dimensions:
  - message_level
  - appeal_type

notes: Use this group only for sender-side group-chat message-level signals; keep it separate from conversation-level and receiver-side variants.

neighbor_metric_diff: Keep distinct from group-conversation level or receiver-side appeal rates.
interpretation_notes: Trust-and-safety support metric for group-chat sender-side message level.
```
