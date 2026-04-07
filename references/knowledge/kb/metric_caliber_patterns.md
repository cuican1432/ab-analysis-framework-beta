# Metric Caliber Patterns | 常见指标口径模式

This page stores reusable reading rules for common multi-day cumulative metric types used in experiment judgment.

Use this page when:
- the report includes `days/days`, `days/user`, `pv/user`, or `uv/user`
- the experiment is judged on multi-day cumulative metrics
- you need to explain why a metric moved and what the denominator really means

## Default Aggregation Strategy

- penetration / coverage metrics
  - default reading: multi-day average
  - rationale: in experiment reading, both `uv/au` and `uv/user` are used as penetration-like views; cumulative reading can drift away from daily coverage meaning, and cross-day dedup can make window-level penetration hard to compare with daily dashboard views
  - if the tool only exposes cumulative views, keep the read correspondingly conservative and consider skipping it for final judgment if misread risk is high
- intensity / depth metrics
  - default reading: multi-day cumulative
- stickiness / frequency metrics
  - default reading: multi-day cumulative

Typical grouping:

- penetration / coverage
  - common forms: `uv/au`, `uv/user`
  - manual override examples: some transition or reporter-coverage metrics may still belong here even when the suffix is `/user`, such as `click_report_user/user`, `on_to_off_user/user`, `unknown_to_off_user/user`, and `off_to_on_user/user`
- intensity / depth
  - common forms: `pv/au`, `xxx/user`, `xxx/u`, `pv/user`, `pair/user`
- stickiness / frequency
  - common forms: `days/days`, `days/user`

## Common Metric Types

### `XXX days/days`

- Meaning: ratio of behavior days to active days
- Numerator: `SUM(behavior days)`
- Denominator: `SUM(active days)`
- Reading rule:
  - this is a ratio-type penetration metric whose denominator is LT active days
  - it is usually aligned with dashboard-style penetration logic
  - under multi-day cumulative experiment reading, the standard interpretation is: sum the multi-day numerator, sum the multi-day denominator, then divide
- Example:
  - `send or like msg days/days`
  - active send-or-like days divided by active days

### `XXX days/user`

- Meaning: average number of behavior days per cumulative distinct user
- Numerator: `SUM(behavior days)`
- Denominator: cumulative distinct users
- Reading rule:
  - this is a per-user behavior-frequency metric measured in days
  - it is often useful together with LT / active days when `days/days` changes
- Example:
  - `send or like msg days/user`
  - average active send-or-like days per user

### `XXX/user` or `XXX pv/user`

- Meaning: average behavior count or PV per cumulative distinct user
- Numerator: `SUM(behavior PV)`
- Denominator: cumulative distinct users
- Reading rule:
  - this is a per-user intensity metric
  - it is additive across many drilldown dimensions, so it is suitable for contribution decomposition
- Example:
  - `send or like msg/user`
  - `duration/user`

### `XXX uv/user`

- Meaning: share of cumulative distinct users who had the behavior in the selected experiment window
- Numerator: cumulative distinct users with the behavior across days
- Denominator: cumulative distinct users
- Reading rule:
  - in experiment reading, treat this as a penetration / coverage family member, even though it is window-level rather than day-grain
  - this is an overall penetration metric over the whole selected window, not a day-grain penetration metric
  - because the numerator is cross-day deduplicated, it loses much of the day-level retention and repeated-behavior information
  - for multi-day cumulative experiment judgment, this type is usually weaker than `days/days`
- Example:
  - `send or like msg uv/user`
  - share of users who had send-or-like behavior in the selected window

## When To Read `days/days` vs `days/user`

- Use `days/days` when you want penetration and LT is not moving significantly.
- When LT moves significantly, read `days/days` together with `days/user` and LT direction.
- In that case:
  - `days/days` helps show penetration change
  - `days/user` helps explain whether the change came from user-level behavior days versus denominator movement

## Why `uv/user` Is Usually Weaker For Final Multi-Day Judgment

- Cross-day deduplication removes much of the repeated-behavior and retention information.
- A multi-day `uv/user` metric describes overall-window penetration, not daily penetration.
- Because multi-day averages are often not a sound significance-reading target, the safer default is:
  - prefer `days/days` over `uv/user` for final multi-day experiment judgment when both attempt to describe penetration

## Quick Reading Rule

- if the metric is `uv/au` or `uv/user`, treat it as penetration / coverage and prefer multi-day average
- if the source only exposes a multi-day cumulative view for this family, do not use it as a final judgment metric by default, because the read is too easy to distort
- if the metric is `pv/au`, `days/days`, `days/user`, `pv/user`, `xxx/user`, or other depth / frequency forms, prefer multi-day cumulative
- if the metric is a custom ratio such as `Finish/Play`, `LoginRate`, `CTR`, or `_ratio`, read it by its own numerator / denominator definition instead of forcing it into one family

## Using `pv/user` For Drilldown Contribution

- `pv/user` is additive across many dimension buckets, so it is suitable for contribution decomposition.
- If the target metric is `Y = pv/user`, and it moves significantly from `Y0` to `Y1`, a drilldown can estimate how much each dimension bucket contributed.
- Standard logic:
  - `Y = sum(X_i)`
  - relative lift of target: `(Y1 - Y0) / Y0`
  - contribution of bucket `X_i`: `(X_i^1 - X_i^0) / Y0`
- Typical use:
  - if `send or like msg pv/user` rises, decompose contribution by message type such as text vs voice

## Reading Hint

- Do not mix these caliber families casually.
- Always align:
  - numerator grain
  - denominator grain
  - cross-day dedup rule
  - whether the metric is penetration, frequency, or intensity
