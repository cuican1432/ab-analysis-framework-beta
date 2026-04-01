# tt-ab-analysis-framework

A Mira-installable TT A/B experiment analysis skill package.

## Included
- `SKILL.md`: main trigger and routing instructions
- `references/core/*`: workflow, rules, memory, runbook, tooling
- `references/knowledge/*`: metric glossary, glossary guide, business knowledge
- `README_for_Mira.md`: existing Mira-facing note from current install

## Packaging note
This package is organized so the top-level extracted directory is `tt-ab-analysis-framework/`, which is the expected skill folder root.

## Knowledge strategy
- Stable shared knowledge lives in `references/knowledge/*`
- Dynamic incremental ingestion should go to runtime-local persistent storage such as:
  - `userdata/tt-ab-analysis-framework/ingested_glossary.jsonl`
  - `userdata/tt-ab-analysis-framework/local_overrides.json`
  - `userdata/tt-ab-analysis-framework/ingestion_log.jsonl`
- Do not casually rewrite packaged references during normal runtime ingestion.
