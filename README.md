# tt-ab-analysis-framework

A Mira-installable TT A/B experiment analysis skill package.

## Included
- `SKILL.md`: main trigger and routing instructions
- `references/core/*`: workflow, rules, memory, runbook, tooling
- `references/glossary/*`: formal glossary content
- `references/kb/*`: formal business knowledge content
- `references/glossary_guide.md`: glossary organization and update rules
- `references/knowledge_guide.md`: business knowledge organization and update rules
- `README_for_Mira.md`: existing Mira-facing note from current install

## Packaging note
This package is organized so the top-level extracted directory is `tt-ab-analysis-framework/`, which is the expected skill folder root.

## Knowledge strategy
- Stable shared glossary lives in `references/glossary/*`
- Stable shared business knowledge lives in `references/kb/*`
- Maintenance guidance lives in:
  - `references/glossary_guide.md`
  - `references/knowledge_guide.md`
- Dynamic incremental ingestion should go to runtime-local persistent storage such as:
  - `userdata/tt-ab-analysis-framework/ingested_glossary.jsonl`
  - `userdata/tt-ab-analysis-framework/local_overrides.json`
  - `userdata/tt-ab-analysis-framework/ingestion_log.jsonl`
- Do not casually rewrite packaged references during normal runtime ingestion.
