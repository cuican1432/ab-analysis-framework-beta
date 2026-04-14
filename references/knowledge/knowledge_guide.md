# Knowledge Guide | 知识层组织、边界与写入说明

This document explains how the knowledge layer should be organized, separated, written, and updated.
这个文件用于说明整个 knowledge layer 应该怎么组织、怎么分边界、怎么写入、以及怎么更新。

## Purpose

Use the `kb/` folder in `references/knowledge/` as a reading-layer entry that helps with:

- PRD reading
- report interpretation
- terminology clarification
- product-mechanism explanation
- domain-specific recurring patterns

Use this guide not only for `kb/`, but also for:
- glossary vs kb boundary
- references vs userdata boundary
- shared vs local knowledge split

## Recommended Structure

- `references/knowledge/kb/index.md`
  - KB 总索引，先看这里再按需读取
- `references/knowledge/kb/`
  - reading-layer files, stable patterns, indexes, and examples
- `references/knowledge/glossary/`
  - glossary reading-layer files, indexes, and migration-time examples
- `references/knowledge/glossary_guide.md`
  - glossary organization and update rules
- `references/knowledge/knowledge_guide.md`
  - knowledge-layer organization and boundary rules

- `userdata/ab-knowledge-builder-beta/`
  - actual knowledge content layer
  - local incremental knowledge
  - local overrides
  - user-specific additions

## What Belongs in KB

- business terminology
- product mechanism notes
- stable domain knowledge
- scenario definitions
- PRD reading hints

## What Does Not Belong in KB

- one-off experiment conclusions
- copied final reports
- temporary run-only instructions
- unresolved draft content

## References vs Userdata

Use `references/knowledge/*` when the content is:
- a reading guide
- an index / navigation page
- a stable interpretation pattern
- a reusable example
- a migration-time reference that helps analysis read the knowledge correctly

Use `userdata/ab-knowledge-builder-beta/*` when the content is:
- actual glossary or KB content
- local
- incremental
- draft
- user-specific
- still evolving over time

Fallback for install/runtime environments:

- If the runtime environment cannot persist `userdata/` reliably, use the packaged read-only snapshot:
  - `references/knowledge/userdata_snapshot/ab-knowledge-builder-beta/*`
- When both are present, treat `userdata/` as the source of truth and the snapshot as a safety net only.

Recommended local split:
- `userdata/ab-knowledge-builder-beta/glossary/`
- `userdata/ab-knowledge-builder-beta/kb/`
- `userdata/ab-knowledge-builder-beta/custom_rules/`

## Update Style

- keep entries topic-based
- prefer concise reusable notes
- avoid mixing glossary schema with business explanation
- keep `references/knowledge/*` focused on reading, indexing, and interpretation guidance
- let evolving knowledge accumulate in `userdata/ab-knowledge-builder-beta/*`
- keep `references/knowledge/kb/index.md` as the entry page instead of mixing navigation into every topic file
- do not use generic roots like `userdata/glossary/` or `userdata/kb/`; keep the skill-scoped namespace
