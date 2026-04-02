# Metrics By Group | TnS DM Private Receiver Metrics - Msg Level

Formal storage location for TnS DM Private Receiver Metrics - Msg Level group.

description_zh: 私信接收端消息层 TnS 指标组，用于记录接收侧消息申诉、审核与反馈表现。
description_en: Formal storage location for DM private-receiver message-level TnS metrics covering receive-side appeal, review, and feedback.

usage_scope: DM / trust & safety
typical_usage: formal storage location for private-receiver message-level metrics
priority_hint: P1
common_dimensions:
  - message_level
  - appeal_type
  - receiver_type

notes: Receiver-side message-level TnS bucket; keep it separate from sender-side and group-chat TnS metrics.

Keep this as the formal storage location for private-receiver message-level metrics as the glossary grows.

