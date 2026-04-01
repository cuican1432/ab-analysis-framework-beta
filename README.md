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
  - old layout is deprecated and should not receive new writes
  - all new reads and new writes should default to:
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

## Local Userdata Protocol

Use a skill-scoped userdata root instead of generic folders such as `userdata/glossary/` or `userdata/kb/`.

Recommended local writable root:

```text
userdata/tt-ab-analysis-framework/
├── glossary/
├── kb/
└── custom_rules/
```

Why keep the `tt-ab-analysis-framework` namespace:
- avoids collisions with other skills or packages
- keeps Mira/Codex local data easier to audit
- makes migration and backup less ambiguous

### What each folder is for

- `userdata/tt-ab-analysis-framework/glossary/`
  - local glossary additions
  - partial confirmations
  - local alias mapping
  - draft polarity notes

- `userdata/tt-ab-analysis-framework/kb/`
  - local business notes
  - project-specific context
  - temporary but reusable background knowledge

- `userdata/tt-ab-analysis-framework/custom_rules/`
  - user-specific interpretation rules
  - local reusable overrides
  - temporary special handling that should not go into shared references

### Minimal file examples

Local glossary note:

```md
# click_report

- definition: risk-related complaint metric
- polarity: lower_is_better
- aliases: complaint_click, click risk report
- status: local_draft
- note: use as negative-risk metric unless the current run explicitly says otherwise
```

Local KB note:

```md
# DM risk background

- scope: DM / social safety
- summary: click_report is usually reviewed together with other negative feedback metrics
- source: local team note
```

Local custom rule:

```md
# experiment_123_rule

- applies_to: experiment_123
- rule: click_report increase means worsening risk
- priority: local_override
- duration: temporary
```

### Read precedence

Use this default order:

1. `references/core/*`
2. current-run explicit temporary guidance
3. `references/knowledge/*`
4. `userdata/tt-ab-analysis-framework/custom_rules/*`
5. `userdata/tt-ab-analysis-framework/glossary/*`
6. `userdata/tt-ab-analysis-framework/kb/*`

Notes:
- `references/core/*` is still the hard-rule layer
- local custom rules can refine interpretation, but should not override hard framework rules
- local glossary / KB files supplement the shared layer; they should not casually rewrite shared references

### Quick Rule

- 写定义、别名、polarity，放 `userdata/tt-ab-analysis-framework/glossary/`
- 写背景、场景、业务说明，放 `userdata/tt-ab-analysis-framework/kb/`
- 写本地特例和临时复用规则，放 `userdata/tt-ab-analysis-framework/custom_rules/`
