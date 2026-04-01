# tt-ab-analysis-framework

Source repository for the Mira TT A/B experiment analysis skill package.

## Included
- `SKILL.md`: main trigger and routing instructions
- `references/core/*`: workflow, rules, memory, runbook, tooling
- `references/knowledge/glossary/*`: formal glossary content
- `references/knowledge/kb/*`: formal business knowledge content
- `references/knowledge/glossary_guide.md`: glossary organization and update rules
- `references/knowledge/knowledge_guide.md`: business knowledge organization and update rules

## Packaging note
This package is organized so the top-level extracted directory is `tt-ab-analysis-framework/`, which is the expected skill folder root.

## Knowledge strategy
- Stable shared glossary lives in `references/knowledge/glossary/*`
- Stable shared business knowledge lives in `references/knowledge/kb/*`
- Maintenance guidance lives in:
  - `references/knowledge/glossary_guide.md`
  - `references/knowledge/knowledge_guide.md`
- Compatibility note:
  - the older flat layout under `references/glossary/*`, `references/kb/*`, and top-level guide files has been retired
  - new reads and new writes should default to:
    - `references/knowledge/glossary/*`
    - `references/knowledge/kb/*`
    - `references/knowledge/glossary_guide.md`
    - `references/knowledge/knowledge_guide.md`
- Dynamic incremental ingestion should go to:
  - `userdata/tt-ab-analysis-framework/glossary/`
  - `userdata/tt-ab-analysis-framework/kb/`
  - `userdata/tt-ab-analysis-framework/custom_rules/`
- Use `userdata/tt-ab-analysis-framework/` for user-provided local knowledge, incremental files, and local overrides.
- Do not casually rewrite packaged references during normal runtime ingestion.
