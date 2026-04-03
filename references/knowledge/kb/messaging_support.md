# Business Knowledge Topic: TikTok - Social - Messaging and Sharing Support Mechanics

This file stores stable, reusable messaging, notification, and adjacent sharing rules that are explicitly documented in TikTok Support.

If you want the KB overview first, start here:
- `references/knowledge/kb/index.md`

Primary external source:
- [Manage direct messages | TikTok Support](https://www.tiktok.com/support/faq_detail?category=web_using_tiktok&id=7543897461052529158&lang=en#7)
- [Direct messages | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/direct-message-settings)
- [Notifications | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/notifications)
- [TikTok stickers | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/tiktok-stickers)
- [Streaks | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/streaks#1)
- [Joining bulletin boards | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/joining-bulletin-boards)
- [Mentions on TikTok | TikTok Support](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/mentions-on-tiktok)
- [Sharing on TikTok | TikTok Support](https://support.tiktok.com/en/using-tiktok/exploring-videos/sharing)
- [Repost | TikTok Support](https://support.tiktok.com/en/using-tiktok/exploring-videos/repost)

## What Belongs Here

- support-documented DM permission rules,
- support-documented message-request rules,
- support-documented DM safety controls,
- support-documented read-status behavior,
- support-documented delete / mute / block / report mechanics,
- support-documented streak mechanics,
- support-documented notification mechanics,
- support-documented sticker mechanics,
- support-documented bulletin-board mechanics,
- support-documented mention mechanics,
- support-documented sharing mechanics,
- support-documented repost mechanics,
- support-documented messaging, notification, and sharing feature links that are useful for further knowledge lookup.

## What Does Not Belong Here

- experiment-local conclusions,
- inferred product behavior that is not stated in the support source,
- metric rows that belong in glossary,
- temporary run-only assumptions.

---

## Stable Messaging, Notification, and Sharing Mechanics

### Who can message you directly

- Friends (followers you follow back) can message you directly.
- Accounts you follow can also message you directly.
- If you have a private account, accounts you follow cannot message you until they follow you back.

### Who can send message requests

- People you may know can send message requests.
- Potential connections (followers) can send message requests.
- Other people on TikTok can also send message requests.
- If you have a private account, potential connections and others on TikTok cannot send you message requests unless they follow you.

### DM permission settings

- TikTok exposes DM permission controls under `Settings and privacy -> Privacy -> Direct messages`.
- Users can decide whether potential connections and others on TikTok can send requests.
- For eligible Business or Organization Accounts, TikTok may expose an `Inbox` option for receiving messages from potential connections and others.

### Direct-message baseline rules

- TikTok direct messaging is available only to eligible account holders; the support article explicitly states that registered users must be at least 16 years old to use direct messaging.
- Family Pairing can impose additional restrictions.
- Existing chat history can remain visible even when a user changes DM settings to stop receiving new messages.
- Shared TikTok videos, effects, hashtags, and sounds can be sent through DMs.
- Private content may become unavailable in chat if the original content visibility later changes.

### Message requests

- Message requests can be accepted, deleted, or reported.
- Some requests may appear in filtered requests.
- Blocked accounts cannot send message requests.

### Read status

- Read status is a two-sided mechanic.
- Read status only becomes visible when both people have it turned on.
- For people aged 18 and older, the setting is on by default according to the support article.

### Safe mode and filtered keywords

- TikTok provides a DM safe mode for hiding messages that may contain sensitive content.
- Safe mode is on by default according to the support article.
- Users can add filtered keywords to hide messages containing those words or phrases.
- Filtered requests can be reviewed, accepted, deleted, reported, or used to block the sender.

### Delete, mute, block, and report mechanics

- Chats can be deleted.
- Individual direct messages can be deleted for self, and in some cases for everyone within a limited send-time window.
- Chats can be muted.
- Accounts can be blocked from messaging.
- Direct messages and accounts can be reported through inbox and chat-level actions.

### Youth safety and abuse-prevention notes

- The support article explicitly states that TikTok applies detection and enforcement for CSAM, grooming, sextortion, and sexual solicitation involving young people in direct messages.
- The support article also points to separate under-18 privacy and safety settings.

### Streaks

- Streaks track people or group chats that exchange messages for multiple consecutive days.
- According to the support article, a streak badge appears after 3 consecutive days of messaging in a direct message or a group chat.
- The streak grows as messages continue to be exchanged.
- The badge fades if messages are not exchanged before the day ends, and the streak ends if there is still no interaction for 24 hours after the fade.
- TikTok may allow streak restoration within a limited recovery window; the support article states a 48-hour restore window and a limited number of restores per month.
- Streak eligibility can vary by age and location; the support article explicitly notes additional limits for some under-16 or under-18 group-chat cases.
- Use this concept when a DM experiment touches continuity, recurrence, pair strength, or chat-retention behavior.

### Streak Pet

- A Streak Pet is an optional virtual companion tied to an active streak.
- It is not required to keep a streak active.
- Streak Pet availability is not universal.
- Streak Pet state is coupled to streak state: when the streak ends, the pet can be removed unless the streak is restored.
- In group chats, some pet-management actions are restricted to the owner or admin according to the support article.
- Treat this as feature-mechanism context for streak-related experiments, not as a default assumption for all DM chats.

### Notifications

- TikTok separates inbox notifications from push notifications.
- Inbox notifications cover activities such as likes, comments, mentions, and related activity streams.
- Inbox notifications can be filtered by activity type; the support article explicitly lists filters such as `Likes and Favorites`, `Comments`, `Add Yours`, and `Mentions and tags`.
- Push notifications can be turned on or off in app settings, and users can also mute them on a schedule.
- The support article states that teen push-notification schedules have default quiet hours that cannot be manually changed in the same way as adult schedules.
- Use this topic when a messaging experiment may interact with awareness, re-entry, inbox load, or notification burden.

### TikTok stickers

- TikTok supports multiple sticker-related mechanisms in messaging, including sticker sets, custom stickers, and video stickers.
- Sticker sets are reusable graphics for direct messaging.
- Custom stickers can be created from personal photos or GIFs.
- Video stickers are created from TikTok videos, and sticker creation depends on sticker permissions and age eligibility.
- Public discoverability and recommendation of stickers are configurable at creation time for some sticker flows.
- The support article explicitly ties video-sticker creation to `Allow reuse of content` style permissions and notes that turning reuse off also affects related reuse surfaces such as Stitch, Duet, and Story reuse.
- Use this topic when a DM or sharing experiment touches sticker creation, sticker sending, or sticker-surface engagement.

### Bulletin boards

- Bulletin boards are creator-to-follower communication channels that live alongside inbox experiences.
- Users can join a bulletin board from inbox invitations or from a creator profile.
- Joining a bulletin board can also trigger an automatic follow relationship if the user was not already following the creator, according to the support article.
- Bulletin board history remains visible after leaving, but future bulletins stop.
- Bulletin reactions are emoji-based and visible to all participants in the bulletin board.
- Use this topic when inbox, creator communication, or message-adjacent surfaces are part of the scenario.

### Mentions

- Mentions are a notification and interaction mechanic that can appear in comments, stories, posts, stickers, and descriptions.
- TikTok lets users configure who can mention them.
- Mention permissions are managed separately from DM permissions.
- Use this topic when a messaging or notification scenario overlaps with directed attention, identity targeting, or social re-engagement.

### Sharing on TikTok

- TikTok supports sharing of posts, profiles, sounds, and hashtags.
- Shared posts can be sent through TikTok surfaces or through external social platforms.
- For some For You posts, TikTok may prompt users to share directly with people they may know or have interacted with.
- The support article states that cross-platform sharing can also send the shared post to the same person on TikTok if they open the shared link and allow direct messages from others.
- Downloading a shared post depends on the original post's download permissions.
- Use this topic when an experiment touches internal share surfaces, quick-share prompts, profile sharing, sound sharing, or hashtag sharing.

### Repost

- Repost is a redistribution mechanic rather than a private-message mechanic.
- Reposted videos can appear on friends' or followers' For You feeds and are labeled with the reposter's profile information.
- TikTok allows repost through multiple entry points, including the `Share` menu, long-press actions, and some friend-repost surfaces.
- Users can remove reposts after the fact.
- The support article states that repost visibility on profile and feed is more limited for private accounts.
- Use this topic when an experiment changes redistribution, amplification, or friend-to-friend content propagation rather than direct-message behavior.

### Related official support topics used by this page

These pages are useful adjacent sources when a messaging, notification, or sharing analysis needs official product-mechanism grounding beyond the glossary:

- `Direct messages`
- `Notifications`
- `TikTok stickers`
- `Streaks`
- `Joining bulletin boards`
- `Mentions on TikTok`
- `Sharing on TikTok`
- `Repost`

Use them as support-backed context pages, especially when a report needs a stable explanation of a messaging, notification, or sharing feature that is not fully described in PRD or raw-data artifacts.

---

## How To Use This Topic In Analysis

- Use this page when a report needs a stable explanation of messaging permissions, request flow, read status, filtering, safety controls, inbox/push notification behavior, or official sharing/repost behavior.
- Prefer this page for product-mechanism grounding when the source question is about what TikTok officially allows or blocks across messaging, notification, and adjacent sharing surfaces.
- Do not turn these support rules into experiment conclusions by themselves; they are context, not evidence of experimental effect.
