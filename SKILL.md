---
name: ab-analysis-framework-beta
description: TT A/B 实验分析框架主入口技能。主要用于实验报告生成，以及基于 PRD 与 Raw Data 联合解读后输出标准化实验报告。用户提到 A/B 实验分析、实验复盘、实验报告、PRD + 数据联合解读并希望直接写报告时，应优先使用本技能。
---

# TT AB Analysis Framework

It mainly supports three task types:

1. Experiment Report Generation
2. Report Generation with Temporary Guidance
3. Knowledge Ingestion

You do not need to remember the internal helper skills. In most cases, calling `ab-analysis-framework-beta` directly is enough.

If the main goal is to build or normalize the knowledge store itself rather than run experiment analysis, use `ab-knowledge-builder-beta`.

## 1) Experiment Report Generation

### Use this when
- 实验观测期结束，数据已经就绪
- 需要基于 PRD + raw data 文档快速生成标准化实验报告

### You can say
- Please use `ab-analysis-framework-beta` to generate an experiment report.
- Experiment name (optional): [xxx]
- PRD link: [URL]
- Raw Data link: [URL]

### Report Output Hard Rules (Feishu Doc) | 报告输出硬规则（飞书文档）

When generating an experiment report, the output must be a Feishu/Lark doc (not a plain chat message). Return the Feishu doc link.

Single source note:
- The detailed and maintained output rules live in `references/core/report_output_rules.md`. If any wording conflicts, that file wins.

Doc output fallback (do not block delivery):
- Prefer: create a Feishu/Lark doc and return the doc link.
- If doc creation is not available due to permission/tooling limits, output a fully structured "doc body" (with the same tables/callouts/code blocks rules) that the user can paste into a new doc, and clearly state what capability/permission is missing.

Hard structure rules (strict):
- Start with `总结论` + `总建议` (decision and rollout suggestion first).
- Then repeat for each sub-conclusion: `分结论 -> 归因链路 -> 细节表格`.
  - Do not dump detail tables before stating the sub-conclusion and its attribution chain.

Attribution hard rules (anti-hallucination):
- Any attribution / logic chain must be grounded in verifiable source facts.
  - For UI/interaction experiments, prioritize PRD "physical interaction facts" when applicable (for example: click distance, UI layer occlusion, operation steps length, interaction path changes).
  - For other cases, allowed attribution routes include: funnel/path chain, user composition, metric formula decomposition, space/cannibalization, time trend, data quality checks, external/product interference (must be evidence-bound).
- Absolute forbidden language: do not use unsupported psych speculation such as "用户觉得花里胡哨", "主观反感", "心理预期下降" unless the source has objective evidence.
- Anti-survivorship bias: if any core secondary metric (for example: DM sticker/camera/group chat) has significant movement, it must be fully disclosed and given its own dedicated deep-analysis subsection. Do not hide it just because it is not the primary headline metric.
- Experiment background & config extraction red lines (MUST DO):
  - Before writing `实验背景与设计`, you must perform node-level full extraction from the header area of the input materials (Raw Data or PRD). Do not trim or rewrite.
  - Required fields whitelist (extract all, verbatim):
    - 实验名称与实验链接
    - 实验周期 / 数据日期
    - 实验类型 / 实验机房 (Data Center)
    - 流量分层 (Traffic Layer)
    - 分流单元 (Sharding Unit / Unit)
    - 实验原始配置总流量 / 放量信息 / 各版本流量比例
  - Filter conditions special protection:
    - find and extract "生效对象 / 受众 / 过滤条件"
    - if it contains technical code (e.g. `version_code >= 440300`, `app_id in [...]`), keep it verbatim in a code block; do not paraphrase or shorten for formatting.
  - Presentation requirement:
    - show these metadata as a structured Key-Value list or an attribute table at the beginning of the report; do not bury them in long paragraphs.
  - Missing-field handling (anti-hallucination):
    - if a required field is not found in the source header, mark it as `not found` and add it into a `to confirm` list; do not infer or fill it.
  - Conflict handling (PRD vs Raw Data):
    - default priority: Raw Data header > PRD header
    - if conflicts exist, show both values side-by-side and add a `to confirm` item instead of silently picking one.

Data appendix hard rules (physical-level evidence):
- Final report must include `## 数据附录 (Data Appendix)` at the end.
- Do not truncate or summarize the underlying detail tables in the appendix.
- Prefer: fetch and "physically clone" all detail tables from the bottom of the Raw Data doc via API and paste them as-is into the appendix.
- If API access is not available due to permission/tooling limits, use this fallback chain (do not summarize):
  1. Copy/export the full raw tables into the appendix, and explicitly list which raw tables could not be cloned and why (permission/tooling/unavailable).
  2. Link-type lowest-fidelity fallback: if full-table copy/export is not possible, place direct links to the raw doc tables (or table nodes / screenshots) and list the missing tables and reasons.
  3. If even link/copy/export is not possible, manually create native Feishu tables and fill in all rows/columns as-is from the source, and explicitly state this is a manual fallback and what limitation caused it.

Hard formatting rules:
- Tables:
  - Must use native Feishu tables. The `<table ...>` form is treated as the intermediate representation for a Feishu table node (not a Markdown table).
  - Explicitly set pixel-level column widths and ensure the number of widths matches the number of columns.
  - Do NOT use Markdown code blocks for tables.
  - Example format: `<table header-row="true" col-widths="300,180,180"> ... </table>`
- Significant movements must be color-highlighted:
  - positive significant: `<font color="green">...</font>`
  - negative significant: `<font color="red">...</font>`
- Only color-highlight when significance is supported by the source (p-value or explicit significant flag). If the source does not provide significance evidence, do not color; keep directional wording only.
- Metric naming must follow: `中文名 (英文名)` (example: `发送消息量 (Send Message PV)`).
  - If one side is missing (no bilingual mapping in glossary/PRD/raw), use the raw metric key as the English name and add a `to confirm` item (do not invent a translation).
  - Do NOT output `[数据缺失]` unless the source data is truly missing; if missing, state what is missing and where it should come from.
- Use callouts for key sections:
  - conclusion / core insights: blue background `<callout icon="..." bgc="3" bc="..."> ... </callout>`
  - risk / warning: red background `<callout icon="..." bgc="1" bc="..."> ... </callout>`

### What the system will do
- run the doc-first analysis workflow
- silently prioritize stored metric glossary and business knowledge
- recall core-flag metric groups by default, especially any group marked as company-core, business-core, or sub-business-core
- identify the experiment's primary business domain first, then apply domain-first recall before ordering metric groups
- perform attribution, risk review, and evidence-boundary labeling when needed
- output a structured experiment report as a Feishu/Lark doc (with native tables/callouts/colors) rather than scattered analysis fragments

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

- Knowledge reading layer → `references/knowledge/*`
- Long-term live glossary content → `userdata/ab-analysis-framework-beta/glossary/*`
- Long-term live business knowledge → `userdata/ab-analysis-framework-beta/kb/*`
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

- packaged knowledge guides and reading indexes stay in `references/knowledge/*`
- local evolving and long-term live knowledge should go to `userdata/ab-analysis-framework-beta/*`

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

## Linkage Rule With `ab-knowledge-builder-beta`

`ab-analysis-framework-beta` reads the live knowledge layer under `userdata/ab-analysis-framework-beta/*`, but it does not own detailed knowledge-content editing.

Update this framework skill when one of these changes:

- the knowledge path changes
- the knowledge schema changes
- the read order changes
- new required indexes or reading categories are introduced
- analysis rules must adapt to newly stabilized knowledge conventions

Do not update this framework skill for pure knowledge-content growth by default.
