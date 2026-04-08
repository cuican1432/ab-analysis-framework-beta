# Current Formalized Metric Caliber Classification

This page classifies the currently formalized metrics by inferred caliber family using naming-pattern heuristics plus a small set of manual business overrides when a metric's true caliber does not match its suffix.

Use this page as a working inventory, not as a replacement for direct metric definitions when a metric is ambiguous.

## Family Counts

- `custom / other`: 0
- `custom ratio/rate`: 44
- `days/days`: 19
- `days/user`: 31
- `intensity / depth`: 77
- `penetration / coverage`: 22

## Inventory

| Group | Metric | Inferred family | Default observation principle | Reading logic |
| --- | --- | --- | --- | --- |
| [B2C] Creator Message Key Metrics | Cr2C DM pv / DAU | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [B2C] Creator Message Key Metrics | Cr2C MuF DM pv / DAU | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM 2-Way | Group Send or Like Message 2-Way Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM 2-Way | Group Send or Like Message 2-Way Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM 2-Way | Group Send or Like Message 2-Way session/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM 2-Way | Group Send or Like Message 2-Way/ User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM 2-Way | Muf Send or Like Message 2-Way/ User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM 2-Way | Send or Like Message 2-Way/ User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Entrance | Send Msg from Inbox Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Entrance | Send Msg from Inbox Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Entrance | Send Msg from Inbox/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Entrance | Send Msg from Inner Push Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Entrance | Send Msg from Inner Push Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Entrance | Send Msg from Inner Push/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Entrance | Send Msg from Outer Push Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Entrance | Send Msg from Outer Push Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Entrance | Send Msg from Outer Push/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Msg Type | Send Camera Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Msg Type | Send Camera Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Msg Type | Send Camera/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Msg Type | Send Emoji Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Msg Type | Send Emoji Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Msg Type | Send Text Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Msg Type | Send Text Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Msg Type | Send Text/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM by Msg Type | Send Voice_message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM by Msg Type | Send Voice_message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM by Msg Type | Send Voice_message/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Camera | Enter DM Camera video shoot page uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Camera | Send Camera Message Upload pv/uv | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Camera | Send Camera Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Core Performance - Android | chat_list_frame_drop_level_4 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | chat_list_load_latency_compliance_rate_threshold_ig | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | chat_list_load_latency_compliance_rate_threshold_p90 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | chat_room_load_latency_compliance_rate_threshold_ig | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | chat_room_load_latency_compliance_rate_threshold_p90 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | send_message_latency_compliance_rate_threshold_p50 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - Android | send_message_latency_compliance_rate_threshold_p90 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Core Performance - iOS | chat_room_load_latency_compliance_rate_threshold_p90 | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Inner Push | Send Msg from Inner Push Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM Inner Push | Send Msg from Inner Push Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM Inner Push | Send Msg from Inner Push/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Negative Feedback | block/user | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Negative Feedback | block_user/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Negative Feedback | click_report/user | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Negative Feedback | click_report_user/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Negative Feedback | mute_user/user | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Negative Feedback | unmute/user | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Negative Feedback | unmute_user/user | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Outer Push | Send Msg from Outer Push Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] DM Outer Push | Send Msg from Outer Push Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] DM Outer Push | Send Msg from Outer Push/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Permission | disabled_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | everyone_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | friends_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | no_one_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | off_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | off_to_on_user/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Permission | on_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | on_to_off_user/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Permission | suggested_friends_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | unknown_ratio | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Permission | unknown_to_off_user/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Permission | unknown_to_on_uv/user | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Quality & Reply Rates New | 1h Response Rate（会话粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Quality & Reply Rates New | 1h Response Rate（轮次粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Quality & Reply Rates New | 24h Camera Msg Response Rate（轮次粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Quality & Reply Rates New | 24h Response Rate（轮次粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Quality & Reply Rates New | 24h text Msg Response Rate（轮次粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Quality & Reply Rates New | 7h Response Rate（轮次粒度） | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| [DM] DM Sticker | Open Sticker Panel pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Sticker | Send Big Sticker pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Sticker | Send Big Sticker uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Sticker | Send Favourites Tab Sticker pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] DM Sticker | Send SA uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] DM Sticker | Send Typing Recommendation Sticker uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| [DM] MuF DM by Motivation | MuF Active Chat Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] MuF DM by Motivation | MuF Active Chat Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] MuF DM by Motivation | MuF Active Chat/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] MuF DM by Motivation | MuF Share/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Enter From as Dim | Message/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Enter From as Dim | MUF Send or Like Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| [DM] Muf DM Enter From as Dim | MUF Send or Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] Muf DM Enter From as Dim | MUF Send or Like Message Pair/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Enter From as Dim | MUF Send or Like Message/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Msg Type as Dim | Message/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Msg Type as Dim | MUF Send or Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| [DM] Muf DM Msg Type as Dim | MUF Send or Like Message Pair/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| [DM] Muf DM Msg Type as Dim | MUF Send or Like Message/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | HLT - active hours | days/user | multi-day cumulative | per-user behavior-day frequency |
| Active Hours (HLT) | HLT1-last 1-day active hours/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | HLT14-last 14-day active hours/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | HLT3-last 3-day active hours/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | HLT30-last 30-day active hours/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | HLT7-last 7-day active hours/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | valid_session_cnt/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | VS1-last 1-day ValidSession/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | VS14-last 14-day ValidSession/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | VS3-last 3-day ValidSession/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | VS30-last 30-day ValidSession/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Active Hours (HLT) | VS7-last 7-day ValidSession/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Active Days | Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Active Days | Last 1-day Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Active Days | Last 14-day Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Active Days | Last 3-day Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Active Days | Last 30-day Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Active Days | Last 7-day Active Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Key Metrics | Finish/Play | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Finish/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | LoginRate | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Play/I | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Play/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | PlayTime/Play | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | PlayTime/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | Publish/Play | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Publish/PubUser | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Publish/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | PubUser/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | RspLatency | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | Session/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Key Metrics | StayDuration/U | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Core-Key Metrics | UVV/U | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Core-Publish Days | Last 1-day Publish Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Publish Days | Last 30-day Publish Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Publish Days | Last 7-day Publish Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| Core-Publish Days | Publish Days | days/user | multi-day cumulative | per-user behavior-day frequency |
| DM Core | Chat Play PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | Enter Chat PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | Internal Share Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| DM Core | Internal Share Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| DM Core | Internal Share PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | Like Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| DM Core | Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| DM Core | Like Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | New Enter Chat PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | New Send Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | Send Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| DM Core | Send Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| DM Core | Send Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Core | Stay Duration/User | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Group Chat | Create GC pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Group Chat | Create GC uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Group Chat | GC Enter Chat pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Group Chat | GC Send Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Group Chat | GC Send or Like pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Cancel Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Cancel Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Cancel/Record Proportion | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Finish Playing in Entry/Play in Entry Proportion pv/pv | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Finish Playing Voice Message in Entry pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Finish Playing Voice Message in Entry uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Finish Playing Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Finish Playing Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Finish Playing/Play Voice Message Proportion pv/pv | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Play in Entry/Record Proportion pv/pv | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Play Voice Message in Entry pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Play Voice Message in Entry uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Play Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Play Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Play/Show Voice Message CTR | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Send Group Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Send Group Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Send Private Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Send Private Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Send Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Send Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Show Voice Message Entrance pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Show Voice Message Entrance uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Show Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Show Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | Start Record Voice Message pv/au | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| DM Voice Message | Start Record Voice Message uv/au | penetration / coverage | multi-day average preferred | penetration-style read; daily or window-level coverage depending on exact denominator |
| DM Voice Message | UV Record/Show CTR | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | UV Send/Record CTR | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Voice Message duration/message | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| DM Voice Message | Voice Message duration/user | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| Key Project-DM | FYP Internal Share PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Key Project-DM | Group Send or Like Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| Key Project-DM | Group Send or Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| Key Project-DM | Last 7-day Social MUF Send or Like Message Pair/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Key Project-DM | Receive or Liked Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| Key Project-DM | Receive or Liked Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| Key Project-DM | Receive or Liked Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Key Project-DM | Send or Like Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| Key Project-DM | Send or Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| Key Project-DM | Send or Like Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Key Project-DM | Social MUF Send or Like Message Days/Days | days/days | multi-day cumulative | behavior-day penetration over active days |
| Key Project-DM | Social MUF Send or Like Message Days/User | days/user | multi-day cumulative | per-user behavior-day frequency |
| Key Project-DM | Social MUF Send or Like Message Pair/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| Key Project-DM | Social MUF Send or Like Message PV/User | intensity / depth | multi-day cumulative | per-user or per-active-user depth / intensity |
| TnS DM Group Chat Sender Metrics - Conv Level | notice_rate_groupcov | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| TnS DM Group Chat Sender Metrics - Conv Level | report_appeal_success_rate_groupcov | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| TnS DM Group Chat Sender Metrics - Msg Level | report_appeal_success_rate_groupmsg | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
| TnS DM Private Sender Metrics - Msg Level | feedback_appeal_success_rate_msg | custom ratio/rate | metric-specific | custom numerator/denominator or rate form |
