# Workflow

## Default Order

Use this default order for experiment analysis:

### Stage A: Source Extraction

1. Read the experiment inputs first.
   - Prefer Feishu/Lark doc links (PRD + Raw Data docx) as the primary inputs.
   - If links are missing, ask the user to provide the PRD and Raw Data doc links before doing interpretation.
   - Screenshots / exported tables are only fallbacks when doc links are unavailable.
2. Generate a Run Signature (anti-contamination).
   - Record the source URLs (PRD + Raw Data) and a `source_hash` for this run.
   - The `source_hash` should be computed from:
     - normalized source URLs, plus
     - a verbatim snapshot of the extracted header/config block.
   - Store it under `experiment/<experiment_id>/version_<yyyymmdd>/run_signature.json` when local files are available.
3. Extract experiment setup / config facts from the source header first.
   - Must extract when available:
     - experiment name / experiment link
     - experiment period / data date
     - experiment object
     - experiment type / data center / platform
     - traffic layer
     - sharding unit / split unit
     - total traffic / rollout info / arm traffic split
     - per-arm parameter config (arm-level config differences)
     - target metrics / guardrails
     - experiment hypothesis / expected outcome (infer from PRD if Raw Data does not state it explicitly; mark the inferred version as `[inferred from PRD]`)
     - filter / audience conditions
     - sample size / DAU scale signals when the source exposes them
   - Data date cross-check:
     - the observation start date must equal the experiment start date (launch / rollout timestamp)
     - if the header-level data date and the per-metric-group data date differ, use the per-metric-group date range as the truth and flag the discrepancy in `to confirm`
   - Missing required fields stay `not found`.
   - If PRD and Raw Data conflict, show both and mark `to confirm`.
4. Extract metric-level evidence fields when the source exposes them.
   - For every metric that will be marked as significant (`↑` / `↓` / `↗` / `↘` or Block API L1 coloring), capture this minimum evidence set:
     - metric (full name from Raw Data)
     - delta (relative and/or absolute)
     - p_value (required to claim significance; if missing, the metric can only be described directionally)
     - CI (optional when the source provides it)
     - N / sample size signal (optional when the source provides it)
     - source_location (where in the Raw Data this evidence came from: table name / section / screenshot reference)
   - If p_value is missing, do not claim significance even if the source uses words like "显著"; add it into `to confirm`.
5. Consult the glossary and KB.
   - Disambiguate metric names, metric groups, business-domain terms, and caliber rules.
   - Resolve `userdata/...` and `references/...` paths relative to the skill install root (zip root), not the workspace/sandbox CWD.
   - Use `references/knowledge/glossary/index.md` and `references/knowledge/kb/index.md` as the reading-order entry pages.
   - If live `userdata/ab-knowledge-builder-beta/*` is unavailable, fall back to `references/knowledge/userdata_snapshot/ab-knowledge-builder-beta/*`.
6. Read the PRD carefully.
   - Identify target metrics, guardrails, mechanism clues, and experiment object details.
7. Build the recall set.
   - Keep explicit targets.
   - Keep mechanism-implied metrics.
   - Keep core guardrails.
   - Keep important significant groups.

### Stage B: Logic and Attribution

Stage B converts Stage A facts into decision-ready reasoning.
Before writing Stage C, the system MUST fill in the Stage B template: `references/core/stage_b_template.md`.
If evidence is insufficient for any section, write `[insufficient evidence]` rather than skipping.

8. Validity sanity check (B0).
   - SRM (sample ratio mismatch): record `Not Available` unless the source exposes sample sizes per arm. Do not fabricate a pass.
   - Pre-period balance: check if baseline/pre-period is available; otherwise record `Not Available`.
   - Rollout anomalies: single ramp vs multiple ramps/pauses/reverts; if unknown, record `Unknown`.
   - Metric coverage: compare Stage A recall set vs available groups; flag `listed but no data provided`.
9. Attribution chains (B1) for each Tier A / Tier B significant group.
   - Product/UX delta: cite a specific PRD anchor (entry point / trigger / interaction change).
   - Most credible mechanism: PRD delta and/or intermediate metrics; label `[direct evidence]` / `[indirect evidence]` / `[hypothesis to verify]`.
   - Metric movement: cite relative change, absolute change (if available), p-value, CI (if available).
   - Business implication: one sentence actionable interpretation.
   - Uncertainty & alternatives: at least one competing explanation and maturity risk when applicable.
10. Cross-signal analysis (B2): contradictions, tradeoffs, PRD-expected regressions, unexpected movements.
11. Effect size & practical significance (B3): baseline context, small-base screening, consistency across platform/segment/time, precision (CI width).
12. Temporal & maturity analysis (B4): maturity ratio, novelty/decay, early-read risk, external events, launch artifact.
13. Segment & dimension deep-dive (B5): top deviations, direction flips, null segments; do not over-read slices.
14. Multi-arm comparison (B6, if applicable): explain WHY arms differ (product delta + mechanism), not just counts.
15. Decision frame (B7): ship recommendation + confidence + blocking risks + monitoring + next actions + rollout strategy.

### Stage C: Final Report

16. Write Stage C report.
   - Preserve the L2 direction marker from Stage A evidence whenever a value is meant to be beautified later.
   - This applies especially to conclusion/risk lines, evidence-manifest rows, and any inline metric citation reused from the evidence table.
   - Do not strip `↑` / `↓` / `↗` / `↘` / `➖` in Stage C; Enhanced Layer removes them only after L1 styling succeeds.

## Live Libra Branch

Use live Libra extraction only when:

- the task explicitly requires live report reading,
- the available docs are insufficient,
- or a validation task requires DOM-backed extraction.

When live Libra extraction is needed:

1. Open the browser in the same session.
2. Reuse the same stable tab when possible.
3. Prefer browser MCP / Playwright first.
4. Fall back to direct CDP only when the browser is already open but the gateway is unstable.

## Stage Boundaries

- `A`: extract facts from the source, lock setup/config fields, consult glossary/KB, and finish the recall set.
- `B`: organize logic and decision structure.
- `C`: write the final report.

## Rerun Rule

- Do not rerun A casually.
- Only rerun A when the source facts, extraction output, or metric caliber are proven wrong.
- If A reruns, rebuild downstream stages from the new A.
- Never patch an old A with backfill numbers.
