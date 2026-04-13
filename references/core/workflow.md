# Workflow

## Default Order

Use this default order for experiment analysis:

### Stage A: Source Extraction

1. Read the experiment inputs first.
   - Prefer PRD, raw-data docs, screenshots, and tables.
2. Extract experiment setup / config facts from the source header first.
   - Must extract when available:
     - experiment name / experiment link
     - experiment period / data date
     - experiment object
     - experiment type / data center / platform
     - traffic layer
     - sharding unit / split unit
     - total traffic / rollout info / arm traffic split
     - target metrics / guardrails
     - experiment hypothesis / expected outcome (infer from PRD if Raw Data does not state it explicitly; mark the inferred version as `[inferred from PRD]`)
     - filter / audience conditions
     - sample size / DAU scale signals when the source exposes them
   - Data date cross-check:
     - the observation start date must equal the experiment start date (launch / rollout timestamp)
     - if the header-level data date and the per-metric-group data date differ, use the per-metric-group date range as the truth and flag the discrepancy in `to confirm`
   - Missing required fields stay `not found`.
   - If PRD and Raw Data conflict, show both and mark `to confirm`.
3. Consult the glossary and KB.
   - Disambiguate metric names, metric groups, business-domain terms, and caliber rules.
4. Read the PRD carefully.
   - Identify target metrics, guardrails, mechanism clues, and experiment object details.
5. Build the recall set.
   - Keep explicit targets.
   - Keep mechanism-implied metrics.
   - Keep core guardrails.
   - Keep important significant groups.

### Stage B: Logic and Attribution

6. Turn Stage A facts into Stage B logic.

### Stage C: Final Report

7. Write Stage C report.

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
