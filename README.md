# tt-ab-analysis-framework

Mira-installable TT A/B experiment analysis skill package.

## What this package is for

Use this package as a single front door for:

- experiment report generation
- report generation with temporary guidance
- glossary / business knowledge ingestion

## Included

- `SKILL.md`
  - main routing and behavior instructions
- `CHANGELOG.md`
  - package-level release notes
- `references/core/*`
  - workflow, rules, memory, runbook, tooling
- `references/knowledge/*`
  - glossary index, glossary guide, business knowledge, and formal glossary storage
- `references/ingestion-guidelines.md`
  - ingestion and review flow
- `references/report-template.md`
  - default report structure
- `references/glossary-schema.md`
  - storage strategy and update conventions
- `references/builtin-glossary/*`
  - lightweight portable glossary JSON

## Mira packaging note

This package is intended for Mira-style upload where `SKILL.md` must be located at the zip root.

## Sandboxed dry-run usage

Even before installing it into a live runtime, this package can be reviewed and improved by simulating:

- what a first-time user would type
- how the skill routes that request
- whether the references are enough
- whether the report / ingestion behavior is clear and consistent

## Knowledge strategy

- Stable bundled knowledge lives in `references/knowledge/*`
- Lightweight portable glossary JSON lives in `references/builtin-glossary/*`
- Dynamic incremental ingestion should go to runtime-local persistent storage such as:
  - `userdata/tt-ab-analysis-framework/ingested_glossary.jsonl`
  - `userdata/tt-ab-analysis-framework/local_overrides.json`
  - `userdata/tt-ab-analysis-framework/ingestion_log.jsonl`
- Do not casually rewrite packaged references during normal runtime ingestion
