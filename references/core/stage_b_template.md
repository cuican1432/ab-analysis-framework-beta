# Stage B Template — Attribution & Reasoning Working Notes

## Instructions

Before writing Stage C, fill in each section below. These notes ensure rigorous reasoning before report writing.
If evidence is insufficient for any section, write `[insufficient evidence — reason]` and add it into B8 To Confirm.
Do not skip sections.

These are internal working notes. Do not paste this template verbatim into the final report.

---

## B0. Validity Pre-Check

| Check | Status | Notes |
|---|---|---|
| SRM (sample ratio mismatch) | Not Available / Pass / Fail | Default to `Not Available` unless sample sizes per arm are explicitly present in the source. Do not fabricate a pass. |
| Pre-period balance | Not Available / Pass / Fail | |
| Rollout cleanliness | Clean / Multiple ramps / Unknown | |
| Metric coverage vs recall set | X/Y groups available | List missing groups marked `listed but no data provided`. |

Issues found (if any):
- (list issues that affect interpretation reliability)

---

## B1. Attribution Chains

For each Tier A/B metric group with significant movement, fill one chain.

### [Metric Group Name] — [Tier]

| Element | Content |
|---|---|
| Product/UX Delta | (Specific PRD anchor: what feature, entry point, trigger changed?) |
| Most Credible Mechanism | (User path: A -> B -> C -> metric moves. Source anchor: PRD feature / intermediate metric) |
| Evidence Label | `[direct evidence]` / `[indirect evidence]` / `[hypothesis to verify]` |
| Metric Movement | (relative: `↑ +X.XX%`, absolute: `+Y` (if available), p=Z.ZZ, CI: [...] (if available)) |
| Business Implication | (So what? One sentence for the decision-maker) |
| Uncertainty | (Data maturity? Novelty? Confounders?) |
| Alternative Explanations | (>= 1 competing explanation) |

(Repeat for each significant group)

---

## B2. Cross-Signal Analysis

### Within-Domain Contradictions

| Signal A (direction + data) | Signal B (direction + data) | Relationship | Net Assessment |
|---|---|---|---|
| | | offset / coexist / one dominates | |

### Benefit-Cost Tradeoffs

| Benefit (metric + magnitude) | Cost (metric + magnitude) | Net judgment |
|---|---|---|
| | | benefit >> cost / marginal / cost dominant |

### Unexpected Movements

| Metric | Why unexpected? | Explanation attempt | Confidence |
|---|---|---|---|
| | Outside PRD feature scope | | `[direct evidence]` / `[indirect evidence]` / `[hypothesis to verify]` |

---

## B3. Effect Size & Practical Significance

### Absolute Magnitude Context

| Metric | Relative Change | Absolute Change | Baseline Level | Assessment |
|---|---|---|---|---|
| | | | | |

### Small Base Effect Flags

- (list any metric with huge relative change but tiny absolute)

### Effect Consistency

| Dimension | Consistent? | Notable deviation |
|---|---|---|
| iOS vs Android | Yes / No / Not Available | |
| New vs Existing users | Yes / No / Not Available | |
| Time trend (stable/decaying/growing) | | |

---

## B4. Temporal & Maturity Assessment

| Field | Value |
|---|---|
| Experiment start date | |
| Data end date | |
| Observation days | |
| Planned experiment duration | |
| Maturity ratio | (obs_days / planned_days) |
| Novelty risk | Yes / No — reasoning |
| Launch artifact (first 1-3 days) | Included / Excluded / Unknown |
| Day-over-day trend available? | Yes (describe) / No |
| Seasonality/external events | None / (describe) |

---

## B5. Segment & Dimension Insights

### Top-3 Effect Deviations

| Rank | Segment | Dimension | Segment Effect | Global Effect | Deviation | Business Hypothesis |
|---:|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

### Direction Flips

| Segment | Global Direction | Segment Direction | Magnitude | Risk Level | Action |
|---|---|---|---|---|---|
| | | | | Monitor / Investigate / Block | |

### Null Segments (key segments with no effect)

- (list segments where effect is surprisingly absent)

---

## B6. Multi-Arm Comparison (if applicable)

| Dimension | Arm 1 | Arm 2 | Gap Driver |
|---|---|---|---|
| Significant metrics count | | | |
| Core metric effect | | | |
| Key product difference | | | |
| Why the gap? | | | (mechanism explanation) |

Recommendation:
- (Ship which arm? Why not the other? Can the weaker arm be improved?)

---

## B7. Decision Frame

| Question | Answer | Key Evidence |
|---|---|---|
| Ship? | Yes / No / Conditional | |
| Which arm? | | |
| Confidence | High / Medium / Low | |
| Blocking risks | | |
| Monitoring items | | |
| Rollout strategy | Full / Phased / Segment-first | |
| Next actions | | (who + what + when — be specific) |

---

## B8. To Confirm (from Stage B reasoning)

- [ ] (items that need human verification — specific owner/team)
- [ ] (items that need longer data — specify how long)
- [ ] (items that need cross-team input — specify which team)
- [ ] (items from validity pre-check — B0 gaps)

