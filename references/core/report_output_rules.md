## Report Output Rules (Single Source) | 报告输出规则（单一来源）

This file is the single source of truth for report output requirements.
If any copied text elsewhere conflicts with this file, this file wins.

## Output Format Layers (CRITICAL) | 输出格式分层（关键）

### Base Layer (Standard Markdown) | 基础层（默认，API 输出时使用）

When using Feishu doc APIs to create/update docs (for example, `upload_to_feishu_tool` / `feishu_update_doc_inplace`), only standard Markdown is reliably rendered.
Do not output Feishu-native rich-text tags in Stage C. They will show up as raw text or be dropped.

Supported patterns (examples):

| Element | Pattern | Example |
|---|---|---|
| Table | Standard Markdown table | `| 指标 | 变化 | 判断 |` |
| Significant positive | direction marker | `↑ +0.1613%` |
| Significant negative | direction marker | `↓ -0.1484%` |
| Marginal result | direction marker | `↗ +0.0613%` / `↘ -0.0584%` |
| Not significant | marker/text | `➖ 不显著` |
| Conclusion highlight | blockquote + emoji + bold | `> 🤖 **结论：...**` |
| Risk highlight | blockquote + emoji + bold | `> 🚨 **风险：...**` |
| To confirm | blockquote + emoji + bold | `> 📝 **To Confirm**：...` |
| Divider | `---` | `---` |

### Enhanced Layer (Block API Post-Processing) | 增强层（Block API 后处理）

This layer is NOT produced by writing Feishu-native tags into the Stage C markdown output.
It is applied by a separate post-processing step that calls Feishu Doc Block API to add colors/callouts/tables.
If a valid token is available, this step should run automatically after the base report is written; otherwise it should be skipped silently.

Key constraints (v1.2):

- "V3 Clean": keep original report chapter structure; only overlay visual enhancement.
- Significant marking degradation: L1 (color+bold+bg via Block API) > L2 (direction markers) > L3 (plain text).
- Table hard limit: row_count <= 8 (including header); over-limit must split or use inline text.
- Experiment info prefers inline text (bold key + value) to avoid large-table API failures.
- Table modes:
  - summary tables: 3 columns (metric / relative change / p-value), widths `[300, 150, 120]`
  - data appendix tables: 5 columns (metric / relative change / absolute change / 95% CI / p-value), widths `[200, 110, 90, 160, 90]`
  - comparison tables: 4 columns (dimension / v1 / v2 / winner), widths `[180, 200, 200, 120]`

Canonical spec: `references/core/beautification_spec_v1.2.md`

### Feishu Doc Output | 飞书文档输出

- Preferred: create a Feishu/Lark doc and return the doc link.
- Fallback: if doc creation is not available due to permission/tooling limits, output a fully structured "doc body" that the user can paste into a new doc, and clearly state what capability/permission is missing.

### Document Header Block | 文档头部信息

- Near the beginning of the doc (right after `总结论 / 总建议`), include a small professional reference block.
- Recommended fields:
  - generation note: `本报告由 AI 基于 PRD 与 Raw Data 自动整理生成，结论以引用数据和原始报告为准。`
  - PRD reference: link or doc title
  - Raw Data reference: link or doc title
  - optional: data date range / generation time / source_hash
- Keep the wording professional and concise. Do not expose framework-internal terms in this block.

### Run Signature | 运行签名（防上下文污染）

- Always include a short `Run Signature` block near the beginning of the report (after `总结论/总建议`).
- Include:
  - PRD URL, Raw Data URL
  - `source_hash` (hash of normalized URLs + extracted header/config snapshot)
  - extracted data date range
- If this run is a rerun or looks similar to a prior run but has a different `source_hash`, add a `to confirm` item asking the user to confirm it is a new run.

### Tables | 表格

- Use standard Markdown tables (they may be converted into native tables by Feishu automatically).
- Do NOT use Markdown code blocks for tables.
- Avoid too-wide tables; split into sub-tables when columns exceed 6.

### Coloring | 染色

- Base layer (Stage C API output) uses plain direction markers as the visual cue (do not rely on colors).
  - positive significant: `↑ +X%`
  - negative significant: `↓ -X%`
  - marginal positive/negative: `↗ +X%` / `↘ -X%`
  - not significant: `➖ 不显著`
- Enhanced layer (Lark Block API / L1) uses styled numeric values only:
  - keep the numeric sign (`+` / `-`)
  - remove `↑` / `↓` / `↗` / `↘` / `➖`
  - express significance through color + bold (+ background when applicable), not through arrows
- L2 direction markers must reflect business meaning, not raw arithmetic direction:
  - `↑` = favorable to the business / experiment goal
  - `↓` = unfavorable to the business / experiment goal
  - `↗` = marginal favorable
  - `↘` = marginal unfavorable
- Determine this direction from glossary polarity first (`higher_is_better`, `lower_is_better`, `depends_on_context`, `descriptive_only`), not from the sign alone.
  - Example: if `block/user` is `lower_is_better`, then `-1.27%` should be written as `↑ -1.27%`
  - Example: if `MuF Share/User` is `higher_is_better`, then `-1.27%` should be written as `↓ -1.27%`
- Coloring granularity: only color the value token, not the metric name or descriptive text.
  - Base Layer: the colored unit is the marker + value token only, e.g. `↑ +0.35%`
  - Enhanced Layer: apply Block API styling only to the numeric value cell / inline value token, e.g. `+0.35%` / `-1.27%` without arrows
  - Keep metric names, descriptions, and surrounding narrative in plain text
  - When a bullet or paragraph contains multiple metrics, style each value separately; do not wrap the whole bullet / paragraph in one color
- Enhanced layer (Block API post-processing) should use colored text styles first (L1), keep only styled numeric values, and fall back to direction markers (L2) or plain labels (L3) only when Block API styling fails.
- L1/L2 must not stack on the same value. If Enhanced Layer runs, strip existing Base Layer markers such as `↑` / `↓` / `↗` / `↘` / `➖` before applying L1 styling.
- Only mark as significant when significance is supported by the source:
  - preferred: p-value is present
  - acceptable: the source provides an explicit significant flag plus a traceable source_location
  - if p-value is missing, the metric can only be described directionally (no significance claim), and it must be added into `to confirm`

### Evidence Manifest | 证据清单

- When the report contains any significant claims (`↑` / `↓` or Enhanced Layer L1 coloring), include a `## 证据清单 (Evidence Manifest)` section before `## 待确认 (To Confirm)`.
- Minimum fields per entry:
  - metric (full Raw Data name)
  - delta (relative and/or absolute)
  - p_value (required to claim significance; otherwise the entry is directional only)
  - CI (when available)
  - N / sample size signal (when available)
  - source_location (where it came from in Raw Data)
- This manifest is used to prevent inconsistent significance labeling across sections.

### Recall Manifest | 召回清单

- Include a `## 召回清单 (Recall Manifest)` section near the end of the main body when the experiment uses domain-first recall logic.
- Record at least:
  - recalled groups
  - recall reason for each recalled group
  - unmatched Raw Data group names (`[unregistered group]`)
  - groups considered but downgraded to appendix / monitoring
- This section is for auditability and new-domain debugging; keep it concise but explicit.

### Metric Naming | 指标命名

- In the report body (first appearance), use: `中文解释（完整英文指标名）` + change marker.
  - Example: `发送或点赞消息天数（Send or Like Message Days/Days） ↑ +0.0156%`
- Chinese meaning source priority:
  1. PRD Chinese description
  2. Raw Data group-name translation
  3. direct translation of the metric name
  - If Chinese meaning is uncertain, keep English name only and add to `to confirm`.
- The metric name used in the report MUST be the full name as it appears in the Raw Data source, including the denominator part (for example: `Send or Like Message Days/Days`, not `Send/Like Message Days`). Do not truncate, abbreviate, or replace with the PRD-side shorthand.
- When Raw Data provides only the English name, use the English name as-is; do not invent a Chinese translation. If a bilingual name is needed and the Chinese mapping is uncertain, add the metric to the `to confirm` list.
- Do NOT output `[数据缺失]` unless the source data is truly missing; if missing, state what is missing and which source should contain it.

### Language Discipline | 语言纪律

- The report is written for decision-makers (PM, leads, stakeholders), not for framework developers or data analysts.
- Framework-internal terms are forbidden in the report body. Translate or rephrase them:
  - ✗ `PRD scope 外` → ✓ `不在本次实验改动范围内`
  - ✗ `artifact` → ✓ `数据口径问题导致的虚假信号` 或 `统计噪声`
  - ✗ `blocking regression` → ✓ `阻断性回退` 或 `明显恶化`
  - ✗ `embedded sheets 无法解析` → ✓ `完整数据需在原始报告中逐项确认`
  - ✗ `归为 [monitoring]` → ✓ `建议持续关注，暂不作为决策阻断项`
  - ✗ `caliber artifact` → ✓ `指标口径问题导致的虚假显著`
- Metric names follow their original language in Raw Data (usually English); all other text uses Chinese.
- Avoid mid-sentence language switching. If an English term must appear (for example, a proper noun), wrap it in parentheses after the Chinese equivalent.

Terminology mapping (user-facing):

| English | Chinese (report body) | Notes |
|---|---|---|
| arm | 实验组（arm） | prefer "实验组" in Chinese; keep "(arm)" when it helps clarity |
| treatment | 实验组（treatment） | use only when needed |
| control | 对照组（control） | use in正文/表头 |

### Callouts | 高亮块

- Use blockquote + emoji + bold:
  - conclusion / core insights: `> 🤖 **结论：...**`
  - risk / warning: `> 🚨 **风险：...**`

### To Confirm | 待确认清单

- Always include a `## 待确认 (To Confirm)` section near the end of the main body (before `## 数据附录 (Data Appendix)`).
- Each item should include: what is missing/uncertain, where it should come from (PRD / Raw Data / glossary), and the impact on the decision.
- Prefer a short numbered list (do not bury to-confirm items inside paragraphs).

### Data Appendix (Physical Clone) | 数据附录（物理级克隆）

- Final report must include `## 数据附录 (Data Appendix)` at the end.
- The appendix is the "absolute evidence chain" for review. Do not truncate or summarize the underlying detail tables.
- Source format handling:
  - if the Raw Data contains structured Feishu table nodes, clone them directly
  - if the Raw Data is in text / list format (for example, `指标名 正向显著 +X% ... p值：Y`), parse the text into a structured native Feishu table before placing it in the appendix; preserve all original values without rounding or truncation
- Preferred path:
  - fetch all detail tables from the bottom of the Raw Data doc via API and "physically clone" the table nodes into the new doc.
- Fallback chain (do not summarize):
  1. Copy/export the full raw tables into the appendix without summarization, and explicitly list which raw tables could not be cloned and why (permission/tooling/unavailable).
  2. Link-type lowest-fidelity fallback: if full-table copy/export is not possible, place direct links to the raw doc tables (or table nodes / screenshots) and list the missing tables and reasons. This still enables review to open the original evidence.
  3. Manual fallback (last resort): manually create native Feishu tables and fill in all rows/columns as-is from the source, and explicitly state this is a manual fallback and what limitation caused it.
