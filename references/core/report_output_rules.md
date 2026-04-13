## Report Output Rules (Single Source) | 报告输出规则（单一来源）

This file is the single source of truth for report output requirements.
If any copied text elsewhere conflicts with this file, this file wins.

### Feishu Doc Output | 飞书文档输出

- Preferred: create a Feishu/Lark doc and return the doc link.
- Fallback: if doc creation is not available due to permission/tooling limits, output a fully structured "doc body" that the user can paste into a new doc, and clearly state what capability/permission is missing.

### Tables | 表格

- Tables must be native Feishu tables, not Markdown tables.
- `<table ...>` is treated as the intermediate representation for a Feishu table node (not a Markdown table).
- Explicitly set pixel-level column widths and ensure the number of widths matches the number of columns.
- Do NOT use Markdown code blocks for tables.
- Example format: `<table header-row="true" col-widths="300,180,180"> ... </table>`

### Coloring | 染色

- Significant movements must be highlighted with colors:
  - positive significant: `<font color="green">...</font>`
  - negative significant: `<font color="red">...</font>`
- Only color-highlight when significance is supported by the source (p-value or explicit significant flag). If the source does not provide significance evidence, do not color; keep directional wording only.

### Metric Naming | 指标命名

- Metric naming must be strict: `中文名 (英文名)` (example: `发送消息量 (Send Message PV)`).
- If bilingual mapping is missing in glossary/PRD/raw, use the raw metric key as the English name and add a `to confirm` item; do not invent a translation.
- Do NOT output `[数据缺失]` unless the source data is truly missing; if missing, state what is missing and which source should contain it.

### Callouts | 高亮块

- conclusion / core insights: blue background `<callout icon="..." bgc="3" bc="..."> ... </callout>`
- risk / warning: red background `<callout icon="..." bgc="1" bc="..."> ... </callout>`

### Data Appendix (Physical Clone) | 数据附录（物理级克隆）

- Final report must include `## 数据附录 (Data Appendix)` at the end.
- The appendix is the "absolute evidence chain" for review. Do not truncate or summarize the underlying detail tables.
- Preferred path:
  - fetch all detail tables from the bottom of the Raw Data doc via API and "physically clone" the table nodes into the new doc.
- Fallback chain (do not summarize):
  1. Copy/export the full raw tables into the appendix without summarization, and explicitly list which raw tables could not be cloned and why (permission/tooling/unavailable).
  2. Link-type lowest-fidelity fallback: if full-table copy/export is not possible, place direct links to the raw doc tables (or table nodes / screenshots) and list the missing tables and reasons. This still enables review to open the original evidence.
  3. Manual fallback (last resort): manually create native Feishu tables and fill in all rows/columns as-is from the source, and explicitly state this is a manual fallback and what limitation caused it.

