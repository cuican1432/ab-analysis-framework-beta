# Glossary Index | 指标字典索引

这里是 **glossary reading layer** 的入口页。  
This is the entry page for the glossary reading layer.

这里放的是：
- glossary 索引
- glossary 阅读顺序
- glossary 维护入口
- 迁移阶段保留的正式示例条目

这里不放的是：
- glossary 的维护说明
- `to confirm`
- placeholder
- 某一次实验的结论
- 长期持续增长的 live glossary 主库

如果你要看“怎么维护 glossary、字段是什么意思、draft 和 formal 怎么流转”，请看：
- `references/knowledge/glossary_guide.md`

如果你要写入或持续积累实际 glossary 内容，请优先写到：
- `userdata/ab-analysis-framework-beta/glossary/`

---

## What Is In The Glossary | 正式字典里有什么

### 1. Metric Group Index | 指标组索引
- `references/knowledge/glossary/metric_groups.md`
- 用来说明一个指标组是什么、通常在哪些实验里出现、常见维度有哪些。

### 2. Dimension Index | 维度索引
- `references/knowledge/glossary/dimensions.md`
- 用来说明维度名称、含义、常见取值和解读边界。

### 3. Dimension Value Index | 维度值索引
- `references/knowledge/glossary/dimension_values.md`
- 用来说明维度值本身的业务含义；如果当前没有内容，可以先留空。

### 4. Metrics By Group | 按指标组拆分的正式指标
- `references/knowledge/glossary/metrics_by_group/*.md`
- 每个文件对应一个正式指标组，存该组下已经确认、可复用的指标条目。

---

## Reading Order | 推荐读取顺序

1. 先看指标组：这组指标大概是什么
2. 再看具体指标：这个指标是什么意思、怎么解读
3. 再看维度：可以怎么拆、拆出来代表什么
4. 把这里优先当成阅读和导航层，而不是长期 live glossary 主库

---

## Current Files | 当前已拆出的文件

- `references/knowledge/glossary/metric_groups.md`
- `references/knowledge/glossary/dimensions.md`
- `references/knowledge/glossary/dimension_values.md`
- `references/knowledge/glossary/metrics_by_group/dm_core.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat.md`
- `references/knowledge/glossary/metrics_by_group/dm_voice_message.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera_by_entrance.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera_private_chat.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera_private_chat_by_entrance.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera_group_chat.md`
- `references/knowledge/glossary/metrics_by_group/dm_camera_group_chat_by_entrance.md`
- `references/knowledge/glossary/metrics_by_group/dm_by_entrance.md`
- `references/knowledge/glossary/metrics_by_group/dm_by_msg_type.md`
- `references/knowledge/glossary/metrics_by_group/dm_quality_reply_rates.md`
- `references/knowledge/glossary/metrics_by_group/dm_quality_reply_rates_new.md`
- `references/knowledge/glossary/metrics_by_group/dm_receive_new.md`
- `references/knowledge/glossary/metrics_by_group/dm_receive.md`
- `references/knowledge/glossary/metrics_by_group/dm_send_load_fail.md`
- `references/knowledge/glossary/metrics_by_group/dm_leave_chat.md`
- `references/knowledge/glossary/metrics_by_group/dm_2_way.md`
- `references/knowledge/glossary/metrics_by_group/muf_dm_by_motivation.md`
- `references/knowledge/glossary/metrics_by_group/muf_dm_enter_from_as_dim.md`
- `references/knowledge/glossary/metrics_by_group/muf_dm_msg_type_as_dim.md`
- `references/knowledge/glossary/metrics_by_group/dm_growth_pairs_key_metrics.md`
- `references/knowledge/glossary/metrics_by_group/dm_growth_pairs_active_days.md`
- `references/knowledge/glossary/metrics_by_group/dm_growth_pairs_retention.md`
- `references/knowledge/glossary/metrics_by_group/muf_growth_dm_pairs_by_time.md`
- `references/knowledge/glossary/metrics_by_group/dm_quick_share.md`
- `references/knowledge/glossary/metrics_by_group/dm_share_type.md`
- `references/knowledge/glossary/metrics_by_group/internal_share_all.md`
- `references/knowledge/glossary/metrics_by_group/inbox_element_metrics.md`
- `references/knowledge/glossary/metrics_by_group/inbox_element_metrics_uid.md`
- `references/knowledge/glossary/metrics_by_group/inbox_message_metrics_uid.md`
- `references/knowledge/glossary/metrics_by_group/b2c_business_message_key_metrics.md`
- `references/knowledge/glossary/metrics_by_group/muf_dm_lifecycle.md`
- `references/knowledge/glossary/metrics_by_group/quick_share_recall.md`
- `references/knowledge/glossary/metrics_by_group/internal_share_funnel_metrics.md`
- `references/knowledge/glossary/metrics_by_group/internal_share_search_funnel_metrics.md`
- `references/knowledge/glossary/metrics_by_group/core_interaction_growth_pairs_active_days.md`
- `references/knowledge/glossary/metrics_by_group/core_interaction_growth_pairs_retention.md`
- `references/knowledge/glossary/metrics_by_group/internal_share_to_chat.md`
- `references/knowledge/glossary/metrics_by_group/activity_status_metrics.md`
- `references/knowledge/glossary/metrics_by_group/activity_status_user_metrics.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_private_receiver_metrics_msg_level.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_group_chat_receiver_metrics_msg_level.md`
- `references/knowledge/glossary/metrics_by_group/key_project_dm.md`
- `references/knowledge/glossary/metrics_by_group/dm_permission.md`
- `references/knowledge/glossary/metrics_by_group/dm_inner_push.md`
- `references/knowledge/glossary/metrics_by_group/dm_outer_push.md`
- `references/knowledge/glossary/metrics_by_group/dm_sticker.md`
- `references/knowledge/glossary/metrics_by_group/dm_streak.md`
- `references/knowledge/glossary/metrics_by_group/dm_conversion_funnel.md`
- `references/knowledge/glossary/metrics_by_group/dm_message_pairs.md`
- `references/knowledge/glossary/metrics_by_group/dm_by_link.md`
- `references/knowledge/glossary/metrics_by_group/dm_negative_feedback.md`
- `references/knowledge/glossary/metrics_by_group/dm_core_performance_android.md`
- `references/knowledge/glossary/metrics_by_group/dm_core_performance_ios.md`
- `references/knowledge/glossary/metrics_by_group/dm_core_performance_latency.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_private_sender_metrics_msg_level.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_private_sender_metrics_conv_level.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_group_chat_sender_metrics_conv_level.md`
- `references/knowledge/glossary/metrics_by_group/tns_dm_group_chat_sender_metrics_msg_level.md`
- `references/knowledge/glossary/metrics_by_group/core_active_days.md`
- `references/knowledge/glossary/metrics_by_group/active_hours_hlt.md`
- `references/knowledge/glossary/metrics_by_group/core_publish_days.md`
- `references/knowledge/glossary/metrics_by_group/core_key_metrics.md`
- `references/knowledge/glossary/metrics_by_group/b2c_creator_message_key_metrics.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_by_msg_type.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_3d_retention.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_7d_retention.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_14d_retention.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_28d_retention.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_3d_retention_new_gt3_users.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_7d_retention_new_gt3_users.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_14d_retention_new_gt3_users.md`
- `references/knowledge/glossary/metrics_by_group/dm_group_chat_28d_retention_new_gt3_users.md`
