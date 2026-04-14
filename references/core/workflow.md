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

8. Turn Stage A facts into Stage B logic.

### Stage C: Final Report

9. Write Stage C report.

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
