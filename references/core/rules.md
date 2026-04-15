# Rules

## Absolute Hard Rules

Maintainer-owned. Do not casually change this section.

- Never fabricate metrics, setup fields, or conclusions.
- Keep missing data missing.
- Keep non-significant results directional, not overstated.
- If the PRD includes product images, screenshots, or visual comparison tables, treat them as part of the source evidence when the runtime can read images.
- Finished outputs from one experiment belong to that experiment only.
- Never reuse an old experiment's finished tables, conclusions, or report as evidence for a new experiment.

## Escalatable Guardrails

Default guardrails should be followed in normal runs, but they may be overridden for the current run if:

1. the user gives an explicit instruction,
2. the agent clearly warns about the consequence,
3. the user confirms they still want the override,
4. the override does not violate `Absolute Hard Rules` or explicit source facts.

Typical examples:

- report structure order,
- section emphasis,
- how much detail stays in main body vs appendix,
- temporary interpretation preference,
- temporary narrowing / widening of recall scope,
- wording style or presentation style.

## Default Rules

Framework defaults live here. These rules are stable and should be changed carefully, but they are not as absolute as the rules above.

### Instruction Precedence

Use this precedence when instructions conflict:

1. `Absolute Hard Rules`
2. the user's current prompt / current-run explicit instruction
3. current-run temporary guidance
4. reusable user overrides in `userdata/ab-knowledge-builder-beta/custom_rules/*`
5. framework default rules in this file and `runbook.md`
6. stored glossary / KB defaults such as base priority, aliases, or interpretation hints

Practical reading:

- if the user asks for a different report structure, emphasis, wording style, or temporary interpretation preference, follow it by default
- unless it violates `Absolute Hard Rules`, causes fabrication, or conflicts with explicit source facts
- reusable `custom_rules` are long-term defaults, but the current prompt still wins for the current run

### Override Protocol

When the user's current prompt or `custom_rules` conflicts with framework defaults:

- if the conflict is only with `Escalatable Guardrails` or `Default Rules`:
  - warn the user about the likely consequence,
  - ask whether they still want to keep their override,
  - if they confirm, follow the user's instruction for the current run.
- if the conflict is with `Absolute Hard Rules`:
  - do not follow the conflicting instruction,
  - explain why it cannot be honored,
  - offer the closest safe alternative.

### Priority of Truth

Use this default priority:

1. prevent fabrication and copying mistakes
2. keep experiment object and target intent aligned with the PRD
3. keep observed setup / rollout / data-date facts aligned with Raw Data when the source exposes them
4. optimize interpretation quality only after the first three are secure

Source priority by fact type:

- experiment object / target intent / stated tradeoff expectation:
  - PRD first
- observed setup / rollout facts / traffic split / data date / arm config:
  - Raw Data header first when exposed
- if PRD and Raw Data conflict on the same field:
  - show both side-by-side and mark `to confirm`

### Evidence Discipline

- Global evidence drives the decision.
- Multi-dimensional evidence explains why the global result holds.
- A single extreme slice is supporting evidence only.
- Do not mix global evidence and slice evidence at the same level without labeling the distinction.
- If platform-level guardrails are missing, keep the final recommendation correspondingly conservative.

For significance reading:

- treat global metrics with the standard `p < 0.05` threshold unless the source specifies otherwise
- treat key slice / segment signals more conservatively, defaulting to `p < 0.03`
- even when a slice passes `p < 0.03`, do not elevate it alone unless direction, adjacent metrics, and business logic also support it
- if a narrow slice is significant but the global result and nearby slices do not support it, treat it as monitoring or a hypothesis to verify
- when a metric shows a relative change > 100% but the absolute difference is extremely small (for example, +733% but absolute diff = +0.88%), always report both the relative and absolute values side by side, note the baseline level, and label it as `[small base effect]`; do not use it as primary evidence for the main conclusion
- when checking heterogeneity, it is valid to note that some local gains may not fully show up at the overall level; if structure information is incomplete, keep this as a cautious heterogeneity note or a hypothesis to verify

Multi-dimensional data handling:

- global significant + slices consistent in direction → include in the main section table; add a brief note that slice support is present
- global not significant but one or more slices significant → only include when the slice passes `p < 0.03` AND the business logic provides a credible explanation; place it in a risk / anomaly subsection, not the main conclusion
- when the source has more than 3 dimension × slice combinations that are significant, consolidate them into a summary table in the main section and put the full slice-level detail tables into the data appendix
- a single extreme slice → reference it only when it is needed for attribution; do not list it as standalone evidence
- slice-level summaries from the Raw Data (e.g., "显著指标总结" per dimension) belong in the data appendix, not the main body

When metric group data exists in the source but cannot be fully parsed by the current toolchain (for example, embedded sheet tokens, image-only tables):

- use whatever summary-level information is available (for example, significant-metric summaries at the top of each group)
- clearly distinguish between "full evidence" (all metrics readable) and "partial evidence" (only summary available)
- for decision purposes: significant signals extracted from summaries can be used, but the absence of other metrics in that group cannot be treated as "flat / no regression" — label as `完整数据需在原始报告中逐项确认`
- add partially-available groups to the `to confirm` list
- if the doc contains embedded `<sheet token="..."/>` tables, treat those sheets as the primary evidence source for appendix reconstruction, not as optional extras
- do NOT rebuild a 5-column appendix row from summary bullets alone when the embedded sheet still exists but has not been read yet
- if sheet access is temporarily unavailable, mark the group as `部分证据 / 待从嵌入表补齐`, rather than converting unavailable fields into `—`

### Metric Tiering

Use three default tiers:

- `Tier A`
  - PRD targets, business-core metrics, and success metrics
  - used for the main conclusion and deeper attribution
- `Tier B`
  - company-core metrics, app-level must-watch metrics, DAU, retention, performance, and major side effects
  - used for guardrails, transmission effects, and rollout-risk judgment
- `Tier C`
  - long-tail metrics and important slice anomalies not already covered by Tier A or Tier B
  - used for monitoring, risk supplementation, and anomaly logging

Do not let Tier C dominate the main conclusion unless the source explicitly proves it should.

PRD expected regression handling:

- if the PRD explicitly states that a metric is expected to decline as a known tradeoff (for example, "video card click might slightly -"), that metric's observed decline should not be counted as a guardrail regression in the decision
- label it as `PRD 预期 tradeoff` and evaluate whether the observed decline is within the PRD's stated tolerance
- if the observed decline is significantly larger than the PRD's expectation, escalate to a risk signal despite the PRD expectation
- this rule only applies when the PRD explicitly names the metric and the expected direction; do not infer expected regressions that the PRD did not state

Tier / core-flag mapping:

- `is_company_core = 1`
  - default to `Tier B`
  - elevate to `Tier A` only when the PRD or source explicitly names it as a target / success metric
- `is_business_core = 1`
  - if it belongs to the same primary business domain, treat it as a strong `Tier A` candidate
  - if it belongs to a different business domain, default to `Tier B`
- `is_sub_business_core = 1`
  - default to `Tier B` when it is same-domain or directly adjacent-domain
  - otherwise keep it in `Tier C` unless the PRD or source makes it central
- no core flag
  - default to `Tier C` unless explicitly targeted, materially significant, or clearly required as a guardrail
- if a metric group is both flagged and explicitly named in the PRD target / success-metric set
  - prioritize the PRD and elevate it to `Tier A`

If a flagged group also has a low stored `importance` / `priority_hint`, do not treat this as a contradiction:

- core flags decide baseline recall obligation
- tier decides analysis role in the current case
- stored priority helps order peers within the same tier, but does not override PRD targets or hard guardrail obligations

### Recall and Priority

Metric group name resolution:

When matching a metric group name from the Raw Data to the glossary, use this order:

1. exact match on `group_name`
2. match on `aliases`
3. strip common prefixes such as `[DM]`, `[B2C]`, `TnS`, `Key Project-` and retry steps 1-2
4. if still unmatched, mark it as `[unregistered group]`, default to `Tier C`, and add it to the `to confirm` list

Do not skip a group just because its Raw Data name does not exactly match a glossary entry.

Separate these two questions:

1. what must be recalled into the analysis universe
2. what deserves to be elevated into the main conclusion

Use a domain-first recall lens before interpreting priority:

1. identify the experiment's primary business domain from the PRD, raw data, title, or explicit user note
2. treat glossary `importance` as a base priority, not a universal fixed priority across every domain
3. if the current stored priority was calibrated under a specific business-domain view such as `DM`, do not blindly reuse it as the final ordering for `Share&Repost`, `Sticker`, `Inbox`, or other primary domains
4. re-rank by the current experiment's primary business domain before deciding what should count as the effective `P0 / P1 / P2 / P3 / P4` order in the live report
5. then adjust recall order by domain relationship:
   - same-domain groups first
   - adjacent-domain groups next
   - distant-domain groups after that
6. keep flagged core groups in the universe even when their business domain is not the primary one

Default recall universe:

- `Tier A`
- `Tier B` core / must-watch metrics
- any metric group explicitly marked as company-core, business-core, or sub-business-core in the glossary
- metrics explicitly named in the PRD as targets or guardrails
- global significant results, defaulting to `p < 0.05`
- key-dimension significant results, defaulting to `p < 0.03`

Core-flag handling:

- if a metric group is marked `is_company_core = 1`, `is_business_core = 1`, or `is_sub_business_core = 1`, do not skip it just because the experiment theme looks narrower
- treat flagged core groups as default recall items and review them as guardrails or decision-relevant context
- `111` groups should be assumed must-watch unless the source explicitly proves they are out of scope for the current experiment
- for the experiment's own subdomain, also recall the related `001`, `011`, and `111` metric groups by default
- do not reduce the subdomain recall set to only the most obvious head group when adjacent core groups in the same subdomain are flagged
- if a flagged core group is unavailable in the source, say it is unavailable; do not silently omit it
- if a metric group is listed in the Raw Data (for example, in an "APP必看指标" or "实验决策指标" section) but has no metric values at all, mark it as `listed but no data provided` and add it to the `to confirm` list; do not assume all metrics are non-significant, and do not assume the data is missing from the platform

Priority rules:

- recall does not automatically mean elevation
- a group's stored `importance` is its base priority, not a domain-blind absolute priority
- the stored priority can reflect a domain-scoped base view; for example, a `DM`-scoped priority table should not be treated as the final ordering for a `Share&Repost` experiment
- if the experiment's primary business domain matches a metric group's `business_domain`, it is valid to elevate that group above its base priority during recall
- if the metric group belongs to an adjacent business domain, keep it in the recall universe but usually below same-domain groups unless the PRD or source makes it central
- if the metric group belongs to a distant business domain, usually keep it as guardrail, monitoring, or appendix material unless the source explicitly makes it a target
- the main conclusion should usually keep only `1-3` top results
- ordering should follow the primary PRD objective
- recalled-but-nonprimary metrics should be downgraded into:
  - monitoring and risk,
  - long-tail anomaly sections,
  - stable guardrail lists,
  - or appendices

Recall manifest requirement:

- Every run should output a `Recall Manifest` that records:
  - recalled groups
  - recall reason for each group (same-domain / adjacent-domain / core-flag / PRD-target / significant-result / guardrail)
  - unmatched groups (for example `[unregistered group]`)
  - non-recalled groups that were considered but intentionally downgraded to appendix / monitoring
- Use this manifest to make recall decisions reviewable when onboarding a new business domain or debugging alias/domain drift.

### Attribution Discipline

Use evidence from three equal routes:

- physical / layout evidence,
- mechanism / transmission-chain evidence,
- drilldown / slice evidence.

These three routes are the evidence organization frame. The attribution "directions" listed later (path/user/formula/space/time/data-quality/external) are concrete methods under this frame.

When useful, label claims as:

- `[direct evidence]`,
- `[indirect evidence]`,
- `[hypothesis to verify]`.

Use whichever route closes the explanation loop best.

Do not invent psychology or user motivation without hard support.
When reading product-mechanism differences from a PRD, read concrete deltas at the feature level: entry points, triggers, page flow, permissions, supported objects, interaction changes, and effect scope.
When possible, connect attribution as a usable chain rather than a loose observation list:

- product / UX delta,
- the most credible mechanism, path, or structural change,
- metric movement,
- business implication,
- and the remaining uncertainty or next validation step.

Prefer this kind of chain when the source supports it, but do not force a fake chain when the middle steps are missing.

Mechanism anchoring requirement (Step 2):

- The Step 2 mechanism/path claim MUST be bound to a source anchor:
  - PRD anchor: a specific feature delta / exposure rule / entry point / interaction change that plausibly enables the mechanism
  - Raw Data anchor: a supporting intermediate metric / funnel step / slice pattern that matches the mechanism
- If Step 2 has no direct anchor, the chain must be downgraded:
  - put the mechanism into a "possible path" subsection
  - label it as `[indirect evidence]`
  - do not treat it as the "main attribution" for the decision
- Always add `Alternative explanations:` after the chain:
  - at least 1 competing explanation that could also produce the same metric movement (for example: external events, time trend, data-quality artifacts, cross-module spillover)

When investigating attribution, check the most relevant of these directions:

- path attribution
  - funnel breaks, step-level explosions, and downstream linkage
- user attribution
  - segment composition, new vs existing users, platform / device / frequency layers
- formula attribution
  - factor decomposition, stock vs incremental effects
- space attribution
  - internal cannibalization, module competition, spillover effects
- time attribution
  - novelty effects, delayed effects, and trend decay
- data-quality attribution
  - when available, check SRM, outliers, pre-period imbalance, and instrumentation issues
  - if the source does not expose assignment counts, split quality, or baseline checks, do not pretend this validity check was completed
- external / product attribution
  - app version changes, bugs, campaigns, ops interference, button conflicts, or accidental taps

Do not try to force every attribution through all directions. Use the directions that can actually explain the movement.

### Metric-Caliber Discipline

Before interpreting an anomaly, align:

- definition,
- denominator,
- dedup rule,
- window,
- time granularity.

If caliber is unclear, do not make a strong claim.

Treat `DAU` as a scale / sample-size signal, not as a direct treatment-effect conclusion.

Performance metric polarity quick reference:

- `compliance_rate` / `达标率` → `higher_is_better` (higher means better performance)
- `frame_drop` / `丢帧率` → `lower_is_better` (lower means better performance)
- `latency` / `耗时` → `lower_is_better` (lower means faster)
- `crash_rate` / `崩溃率` → `lower_is_better`
- `success_rate` / `成功率` → `higher_is_better`

When the glossary does not specify polarity for a performance metric, infer from the metric name using the rules above. If still ambiguous, mark it as `[polarity to confirm]`.

For common multi-day cumulative caliber families:

- `days/days`
  - usually read as behavior-day penetration over active days
- `days/user`
  - usually read as per-user behavior-day frequency
- `pv/user`
  - usually read as per-user behavior intensity and is often the preferred base for additive drilldown contribution
- `uv/user`
  - in experiment reading, treat it the same way as `uv/au`: a penetration / coverage metric that should usually be read with a multi-day average view

Default reading preference:

- if the metric is `uv/au` or `uv/user`, treat it as penetration / coverage and prefer multi-day average
- if the source only exposes a multi-day cumulative view for this family, do not use it as a final judgment metric by default unless the source explicitly requires it
- if the metric is `pv/au`, read it with the intensity / depth family rather than the penetration family
- if the goal is multi-day penetration judgment and LT is stable, prefer `days/days`
- if LT changes materially, interpret `days/days` together with `days/user` and LT direction
- if the metric is a custom ratio or rate such as `Finish/Play`, `LoginRate`, `CTR`, or `_ratio`, read it from its explicit numerator / denominator definition rather than forcing it into `uv/au`, `days/days`, or `pv/user`

### Report Discipline

- Write the report as a decision memo, not a data dump.
- Use business themes, not raw page order, as the main narrative structure.
- Keep risk and benefit at the same level of visibility.
- When the same metric group contains both positive-significant and negative-significant metrics (contradictory signals):
  - analyze them separately; do not use positive signals to mask or offset negative signals
  - if the negative signal involves safety / compliance metrics (for example: report rate, spam rate, abuse rate), it must get a dedicated risk subsection regardless of the positive signals in the same group
  - label the contradiction explicitly so the reader does not assume the group is uniformly good or bad
- Name representative metrics and values when making a business-theme claim.
- For each major benefit or risk, try to explain not just what moved, but what business theme it represents.
- When the source is strong enough, push the write-up one layer deeper than metric listing:
  - what changed in the product,
  - which user path was likely affected,
  - which metrics moved,
  - what that means for the business,
  - and what still needs validation.
- For multi-arm experiments, do not describe each arm in isolation only.
- For multi-arm experiments, explicitly state which arm is better, which arm is weaker, and what the decision implication is.
- If there are multiple treatment arms, include a dedicated comparison section so the reader can see the strict arm-to-arm differences, not just separate summaries.
- Only make detailed product-mechanism comparisons when the source explicitly exposes the relevant configuration or description differences for those arms.
- Do not stop at "risk exists" or "benefit exists" when the report needs to support action. If the source allows it, add the most reasonable next action, validation ask, or rollout implication.
- When evidence is insufficient, explicitly separate:
  - what is confirmed,
  - what is not confirmed,
  - and what is only directional.
- Prefer conservative, clear, reviewable writing over polished but weakly supported writing.

Non-significant handling:

- `Tier A`: still must appear. Explain what "not significant" implies for the decision (for example: no clear penetration gain, or effect not stable yet).
- `Tier B`: can be summarized as "guardrail flat / no significant regression" unless the business context requires deeper discussion.
- `Tier C`: can be omitted unless it is needed for attribution, anomaly tracking, or risk logging.

Significance judgment and effect size description must be separated:

- significance judgment: `正向显著` / `负向显著` / `不显著` — determined solely by p-value threshold (default 0.05)
- effect size description: `效果量较大` / `效果量较小` — determined by the absolute or relative magnitude of the change
- do not combine them into hybrid terms such as `微正向显著` or `弱显著`; these are ambiguous and can mislead the reader into thinking the statistical significance is weak
- correct pattern: `正向显著（效果量较小，+0.016%）` or `正向显著，但绝对变化幅度有限（+0.016%）`
