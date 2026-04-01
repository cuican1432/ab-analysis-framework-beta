# tt-ab-analysis-framework

A Mira-installable TT A/B experiment analysis skill package.

## Included
- `SKILL.md`: main trigger and routing instructions
- `references/core/*`: workflow, rules, memory, runbook, tooling
- `references/glossary/*`: formal glossary content
- `references/kb/*`: formal business knowledge content
- `references/glossary_guide.md`: glossary organization and update rules
- `references/knowledge_guide.md`: business knowledge organization and update rules

## Packaging note
This package is organized so the top-level extracted directory is `tt-ab-analysis-framework/`, which is the expected skill folder root.

## Knowledge strategy
- Stable shared glossary lives in `references/glossary/*`
- Stable shared business knowledge lives in `references/kb/*`
- Maintenance guidance lives in:
  - `references/glossary_guide.md`
  - `references/knowledge_guide.md`
- Compatibility note:
  - `references/knowledge/*` is a temporary compatibility layer from the older layout
  - new reads and new writes should default to:
    - `references/glossary/*`
    - `references/kb/*`
    - `references/glossary_guide.md`
    - `references/knowledge_guide.md`
- Dynamic incremental ingestion should go to:
  - `userdata/tt-ab-analysis-framework/glossary/`
  - `userdata/tt-ab-analysis-framework/kb/`
  - `userdata/tt-ab-analysis-framework/custom_rules/`
- Use `userdata/tt-ab-analysis-framework/` for local files provided by the user.
- Do not casually rewrite packaged references during normal runtime ingestion.
