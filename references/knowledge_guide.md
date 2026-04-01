# Knowledge Guide | 业务知识维护说明

This document explains how the business knowledge layer should be organized and updated.
这个文件用于说明业务知识层应该怎么组织、怎么更新。

## Purpose

Use the `kb/` folder for reusable business knowledge that helps:

- PRD reading
- report interpretation
- terminology clarification
- product-mechanism explanation
- domain-specific recurring patterns

## Recommended Structure

- `references/kb/index.md`
  - KB 总索引，先看这里再按需读取
- `references/kb/`
  - stable reusable business knowledge
- `references/glossary/`
  - formal glossary content
- `references/glossary_guide.md`
  - glossary organization and update rules
- `references/knowledge_guide.md`
  - business-knowledge organization and update rules

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

## Update Style

- keep entries topic-based
- prefer concise reusable notes
- avoid mixing glossary schema with business explanation
- move only confirmed content into `kb/`
- keep `kb/index.md` as the entry page instead of mixing navigation into every topic file
