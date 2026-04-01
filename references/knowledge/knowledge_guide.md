# Knowledge Guide | 知识层组织与边界说明

This document explains how the knowledge layer should be organized, separated, and updated.
这个文件用于说明整个 knowledge layer 应该怎么组织、怎么分边界、以及怎么更新。

## Purpose

Use the `kb/` folder for reusable business knowledge that helps:

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
  - stable reusable business knowledge
- `references/knowledge/glossary/`
  - formal glossary content
- `references/knowledge/glossary_guide.md`
  - glossary organization and update rules
- `references/knowledge/knowledge_guide.md`
  - knowledge-layer organization and boundary rules

- `userdata/tt-ab-analysis-framework/`
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
- shared
- stable
- reusable across cases
- ready to be treated as formal knowledge

Use `userdata/tt-ab-analysis-framework/*` when the content is:
- local
- incremental
- draft
- user-specific
- not yet ready to become shared formal knowledge

Recommended local split:
- `userdata/tt-ab-analysis-framework/glossary/`
- `userdata/tt-ab-analysis-framework/kb/`
- `userdata/tt-ab-analysis-framework/custom_rules/`

## Update Style

- keep entries topic-based
- prefer concise reusable notes
- avoid mixing glossary schema with business explanation
- move only confirmed content into `kb/`
- keep `references/knowledge/kb/index.md` as the entry page instead of mixing navigation into every topic file
- do not use generic roots like `userdata/glossary/` or `userdata/kb/`; keep the skill-scoped namespace
