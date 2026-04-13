---
name: ab-analysis-framework-beta
description: TT A/B 实验分析框架主入口技能。用于实验报告生成、PRD 与 Raw Data 联合分析、业务知识入库、以及带临时规则的单次实验分析。用户提到 A/B 实验分析、实验复盘、实验报告、metric glossary、knowledge ingestion、业务术语整理、PRD + 数据联合解读时，应优先使用本技能。
---

# TT AB Analysis Framework

It mainly supports three task types:

1. Experiment Report Generation
2. Report Generation with Temporary Guidance
3. Knowledge Ingestion

You do not need to remember the internal helper skills. In most cases, calling `ab-analysis-framework-beta` directly is enough.

## 1) Experiment Report Generation

### Use this when
- 实验观测期结束，数据已经就绪
- 需要基于 PRD + raw data 文档快速生成标准化实验报告

### You can say
- Please use `ab-analysis-framework-beta` to generate an experiment report.
- Experiment name (optional): [xxx]
- PRD link: [URL]
- Raw Data link: [URL]

### What the system will do
- run the doc-first analysis workflow
- silently prioritize stored metric glossary and business knowledge
- recall core-flag metric groups by default, especially any group marked as company-core, business-core, or sub-business-core
- identify the experiment's primary business domain first, then apply domain-first recall before ordering metric groups
- perform attribution, risk review, and evidence-boundary labeling when needed
- output a structured experiment report rather than scattered analysis fragments

## 2) Report Generation with Temporary Guidance

### Use this when
- 本期实验有临时监控指标
- 本次需要一个临时极性或解释规则
- 你不希望把它永久写入知识库

### You can say
- Please use `ab-analysis-framework-beta` to generate an experiment report with this temporary metric/rule guidance.
- Experiment name (optional): [xxx]
- PRD link: [URL]
- Raw Data link: [URL]
- Temporary metric guidance: [example: click_report increasing means worsening risk in this experiment]

### What the system will do
- apply the temporary instruction only for the current run
- prioritize it during attribution and polarity judgment
- do not write it back into the long-term knowledge base unless explicitly asked
- still obey hard framework rules and never relax data discipline because of a temporary note

## 3) Knowledge Ingestion

### Use this when
- 刚整理好新版指标字典，想提前存入知识库
- 想把某些指标的 polarity 提前定好
- 想把业务术语、口径说明、召回提示沉淀下来

### You can say
- Please use `ab-analysis-framework-beta` to ingest experiment knowledge.
- Metric glossary / knowledge input: [Feishu URL or pasted text]

### What the system will do
- perform lightweight knowledge extraction
- extract reusable mappings such as `<metric name -> meaning / polarity / note>`
- write stable confirmed content into the right knowledge layer
- keep unfinished or uncertain parts as `draft` / `to confirm`
- place user-provided local knowledge files under `userdata/ab-analysis-framework-beta/` by default instead of rewriting packaged references
- return a short confirmation by default instead of a long write-up

## Internal reference map

- Report Generation → `references/core/*`
- Temporary Guidance Report → `references/core/*`
- Knowledge Ingestion → `references/knowledge/glossary/index.md` + `references/knowledge/kb/index.md` + `references/knowledge/glossary_guide.md` + `references/knowledge/knowledge_guide.md` + `references/core/runbook.md`

## Storage Hint

- Stable shared glossary → `references/knowledge/glossary/*`
- Stable shared business knowledge → `references/knowledge/kb/*`
- Glossary maintenance rules → `references/knowledge/glossary_guide.md`
- Business knowledge maintenance rules → `references/knowledge/knowledge_guide.md`
- Runtime local incremental layer → `userdata/ab-analysis-framework-beta/*`
- Memory can help recall, but it is not the main glossary store

## Userdata Boundary

When the user wants to inject local knowledge, local data files, or run-specific reusable notes, use `userdata/ab-analysis-framework-beta/` as the default writable layer.

- Local glossary additions / partial confirmations → `userdata/ab-analysis-framework-beta/glossary/`
- Local business notes / project context → `userdata/ab-analysis-framework-beta/kb/`
- User-specific interpretation rules / temporary reusable overrides → `userdata/ab-analysis-framework-beta/custom_rules/`

Do not casually rewrite packaged shared references during normal ingestion:

- packaged shared knowledge stays in `references/knowledge/glossary/*` and `references/knowledge/kb/*`
- local evolving knowledge should go to `userdata/ab-analysis-framework-beta/*`

Default read order:

1. `references/core/*`
2. current-run explicit temporary guidance
3. `references/knowledge/*`
4. `userdata/ab-analysis-framework-beta/custom_rules/*`
5. `userdata/ab-analysis-framework-beta/glossary/*`
6. `userdata/ab-analysis-framework-beta/kb/*`

Do not use generic roots such as `userdata/glossary/` or `userdata/kb/`; keep the skill-scoped namespace to avoid collisions with other packages.

Metric recall reminder:

- do not narrow the recall set only to the experiment's most obvious business theme
- any glossary metric group marked as company-core, business-core, or sub-business-core should be recalled by default
- for the experiment's own subdomain, also recall the related `001`, `011`, and `111` metric groups by default
- if a flagged core group is missing from the source, state that it is unavailable instead of silently dropping it
- treat glossary `importance` as a base priority
- do not treat one domain's stored priority table as universal; a `DM`-scoped ordering may need to be re-ranked when the experiment's primary business domain is `Share&Repost`, `Sticker`, `Inbox`, or another domain
- identify the experiment's primary business domain first, then order metric groups with a domain-first lens:
  - same-domain groups first
  - adjacent-domain groups next
  - distant-domain groups after that
- do not assume a group that is `P3` in one domain should stay `P3` when the experiment's primary business domain changes
