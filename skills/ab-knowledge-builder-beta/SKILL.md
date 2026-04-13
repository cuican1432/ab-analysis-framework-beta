---
name: ab-knowledge-builder-beta
description: A/B experiment knowledge-builder skill for glossary, KB, metric-group, caliber, and local knowledge-store maintenance. Use when the goal is to build, ingest, migrate, or normalize knowledge content rather than generate an experiment report. This skill owns the live knowledge content layer under userdata/ab-analysis-framework-beta/*.
---

# AB Knowledge Builder Beta

Use this skill when the main job is knowledge work, not experiment reporting.

It mainly supports four task types:

1. Glossary Ingestion and Cleanup
2. KB Ingestion and Topic Structuring
3. Metric-Group / Caliber Normalization
4. Knowledge Migration and Store Maintenance

## Use this skill when

- you are building or updating the glossary
- you are building or updating the KB
- you are migrating knowledge between layers
- you are normalizing metric meaning, polarity, priority, or caliber
- you are updating indexes, guides, or reading hints for the knowledge system

## Do not use this skill when

- the main goal is to generate an experiment report
- the main goal is to make an experiment decision
- the task is primarily about PRD + raw data interpretation for one experiment run

In those cases, use `ab-analysis-framework-beta`.

## Storage Ownership

- Live glossary content belongs in `userdata/ab-analysis-framework-beta/glossary/*`
- Live business knowledge belongs in `userdata/ab-analysis-framework-beta/kb/*`
- Local reusable overrides belong in `userdata/ab-analysis-framework-beta/custom_rules/*`

Treat `references/knowledge/*` as the reading layer:

- indexes
- guides
- interpretation patterns
- stable examples
- migration-time references

Do not treat `references/knowledge/*` as the default live knowledge store.

## Default Builder Behavior

- write new or evolving knowledge to `userdata/ab-analysis-framework-beta/*` by default
- keep entries reusable and topic-based
- prefer stable wording over case-specific writeups
- keep unresolved content marked as draft or to-confirm when needed
- update indexes and guides when the reading path changes

## You can say

- `Please use ab-knowledge-builder-beta to ingest these metric definitions into the glossary, including metric meaning, aliases, polarity, and calculation notes.`
- `Please use ab-knowledge-builder-beta to update the DM knowledge base with this new source and extract reusable product-mechanism knowledge.`
- `Please use ab-knowledge-builder-beta to normalize this metric group, including group meaning, business domain, priority, scope, and typical usage.`
- `Please use ab-knowledge-builder-beta to normalize these metric meanings and caliber tags, such as uv/au, days/days, days/user, pv/user, and ratio.`

## Linkage Rule With `ab-analysis-framework-beta`

`ab-knowledge-builder-beta` is the source-of-truth editor for the live knowledge content layer.

Update `ab-analysis-framework-beta` only when one of these changes:

- the knowledge path changes
- the knowledge schema changes
- the read order changes
- new required indexes or reading categories are introduced
- analysis rules must adapt to newly stabilized knowledge conventions

Pure knowledge-content growth does not require a framework-skill update by default.
