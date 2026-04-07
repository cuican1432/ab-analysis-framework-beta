# TikTok - Platform Terms and Common Metrics

This page stores stable platform-level terminology and common metric meanings that are reused across many experiments.

Use this page for:
- standard metric names that appear repeatedly across product domains
- common aliases such as `DAU`, `Ret`, `VV`, `FYP`
- high-level source and caliber reminders for non-domain-specific reading

Do not use this page for:
- one-off experiment conclusions
- temporary monitoring-only definitions
- domain-specific metric logic that belongs in `dm.md`, `story.md`, or other topic pages

## User and Activity Basics

### DAU

- Chinese: 日活跃设备数
- Meaning: Number of distinct active devices in a day.
- Aliases: daily active users, daily active devices
- Source reminder: active-session based device table
- Notes: Device-level active count. In common TikTok reading, this is the baseline activity denominator for many ratio metrics.

### DNU

- Chinese: 日新激活设备数
- Meaning: Number of newly activated devices in a day.
- Aliases: daily new users, daily new activations
- Source reminder: activation table
- Notes: Usually device-level first activation. Device-level newness can differ from account-level newness.

### MAU

- Chinese: 月活跃设备数
- Meaning: Number of distinct active devices in the trailing 30-day window.
- Aliases: monthly active users, monthly active devices
- Source reminder: active device table with rolling-window aggregation
- Notes: Usually computed on a rolling 30-day basis rather than calendar-month membership.

### ActiveDays

- Chinese: 活跃天
- Aliases: LT
- Meaning: Sum of active days within the analysis window.
- Source reminder: active device table
- Notes: Often used as a frequency / habit signal. Publish Days is a sibling caliber for creation frequency.

### Login Rate

- Chinese: 登录率
- Meaning: Share of DAU that is logged in.
- Source reminder: session header / login-state fields
- Notes: Read as login penetration among active devices rather than account-system quality by itself.

### Retention

- Chinese: 留存率
- Aliases: Ret
- Meaning: Share of an earlier active cohort that returns and is active again in a later window.
- Source reminder: active-session based device table
- Notes: Always read with an explicit retention window such as 1d, 3d, 7d, 14d, or 28d.

### Session Duration

- Chinese: 设备使用时长
- Aliases: stay_duration, stay_time, duration, ST
- Meaning: Total device session duration in the day or analysis window.
- Source reminder: session logs
- Notes: Usually session-based usage time rather than a single front-end stay-time event.

## Video Consumption

### VV

- Chinese: 视频播放数
- Aliases: 消费 VV, Play
- Meaning: Total counted video plays.
- Source reminder: `video_play`
- Notes: Usually counted after first-frame play. Re-entry and replay details can differ by platform implementation.

### UVV

- Chinese: 播放视频数
- Meaning: Number of distinct videos played by a device.
- Source reminder: `video_play`
- Notes: Usually deduplicated by device and video group / content key.

### Finish/Play

- Chinese: 播放完成率
- Aliases: completion rate, `video_finish / video_play`
- Meaning: Ratio of completed plays to plays.
- Source reminder: `video_play_finish`
- Notes: Read as completion efficiency, not as absolute watch depth by itself.

### Play Duration

- Chinese: 播放时长
- Aliases: Playtime
- Meaning: Total time spent playing video.
- Source reminder: play-time duration event
- Notes: Usually stored in milliseconds in raw logs and may require unit conversion.

## Creation and Impression

### Publish Cnt

- Chinese: 投稿数
- Meaning: Number of newly created / published videos.
- Source reminder: server-side item creation records
- Notes: Can differ slightly from front-end publish intent because some attempts do not finish server-side creation.

### Publish Rate

- Chinese: 投稿率
- Meaning: Publish devices divided by DAU.
- Source reminder: server-side item creation records
- Notes: Read as creator participation rate among active devices.

### Server Impression Cnt

- Chinese: 服务端展现内容条数
- Meaning: Number of content items served to users by the recommendation server.
- Source reminder: server impression logs
- Notes: This is serving-side exposure, not client-side confirmed viewing.

## Social and Interaction

### Like

- Chinese: 点赞数
- Meaning: Number of like actions.
- Source reminder: `like`
- Notes: Re-like after unlike can be counted again depending on event logic.

### Follow

- Chinese: 关注数
- Meaning: Number of follow actions.
- Source reminder: `follow`
- Notes: Re-follow after unfollow can be counted again depending on event logic.

### Comment

- Chinese: 发布评论数
- Meaning: Number of posted comments.
- Source reminder: `post_comment`

### Download

- Chinese: 下载视频数
- Meaning: Number of video-download actions.
- Source reminder: `download`
- Notes: Can include both explicit download-panel actions and some save-related flows depending on product setup.

### Share Video

- Chinese: 分享视频数
- Meaning: Number of video-share actions.
- Source reminder: `share_video`
- Notes: Usually indicates share intent, not confirmed downstream share success.

### Internal Share

- Chinese: 站内分享视频数
- Meaning: Number of in-app share actions, typically to internal destinations such as chat.
- Source reminder: `share_video` with internal / chat-like platform tags
- Notes: Read as internal-share intent rather than guaranteed downstream delivery success.

### External Share

- Chinese: 站外分享视频数
- Meaning: Number of share actions to external channels.
- Source reminder: `share_video` with non-internal platform tags
- Notes: Read as external-share intent rather than guaranteed downstream delivery success.

## Live

### Live DAU

- Chinese: 看播人数
- Meaning: Number of distinct users who watched live content.
- Source reminder: live play UV

### Live Duration

- Chinese: 看播时长
- Meaning: Total live watching duration.
- Source reminder: live duration event

### Live Recharge Money

- Chinese: 直播充值金额（美元）
- Meaning: Recharge amount for live, in USD.
- Source reminder: live server-side recharge stats

### Live Consume Money

- Chinese: 直播消费金额（美元）
- Meaning: Audience live-consumption amount, typically converted from coins / diamonds into USD.
- Source reminder: live server-side consume stats

## Search

### Search

- Chinese: 搜索次数
- Meaning: Number of searches.
- Source reminder: search impression / search session tables
- Notes: Always read with the search-channel scope because some search families are excluded in standard dashboards.

### Active Content Search

- Chinese: 手动内容搜索次数
- Meaning: Manual content-search PV excluding people-search.
- Source reminder: search session tables
- Notes: Usually narrower than overall search because it excludes people-search and some passive search surfaces.

## User Segments and Product Terms

### Diverse User

- Chinese: 泛化用户
- Meaning: Usually refers to users whose predicted age is not L1 or L2, often including users without predicted age.
- Source reminder: predicted-age / gender user profile tables
- Notes: This is a segmentation term, not a metric by itself.

### FYP

- Chinese: 推荐页
- Aliases: hot, For You
- Meaning: The TikTok recommendation tab / For You feed.
- Notes: Product-surface term rather than a metric. Often used to describe source surface, traffic origin, or recommendation context.
