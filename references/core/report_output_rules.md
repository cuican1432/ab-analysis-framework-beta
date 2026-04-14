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
| Significant positive | emoji + bold | `**✅ +0.1613%**` |
| Significant negative | emoji + bold | `**🔻 -0.1484%**` |
| Not significant | emoji/text | `➖ 不显著` |
| Conclusion highlight | blockquote + emoji + bold | `> 🤖 **结论：...**` |
| Risk highlight | blockquote + emoji + bold | `> 🚨 **风险：...**` |
| To confirm | blockquote + emoji + bold | `> 📝 **To Confirm**：...` |
| Divider | `---` | `---` |

### Enhanced Layer (Block API Post-Processing) | 增强层（Block API 后处理）

This layer is NOT produced by writing Feishu-native tags into the Stage C markdown output.
It is applied by a separate post-processing step that calls Feishu Doc Block API to add colors/callouts/tables.

Key constraints (v1.2):

- "V3 Clean": keep original report chapter structure; only overlay visual enhancement.
- Significant marking degradation: L1 (color+bold+bg via Block API) > L2 (emoji) > L3 (plain text).
- Table hard limit: row_count <= 8 (including header); over-limit must split or use inline text.
- Experiment info prefers inline text (bold key + value) to avoid large-table API failures.
- Table modes:
  - summary tables: 3 columns (metric / relative change / p-value), widths `[300, 150, 120]`
  - data appendix tables: 5 columns (metric / relative change / absolute change / 95% CI / p-value), widths `[200, 110, 90, 160, 90]`

Canonical spec: `references/core/beautification_spec_v1.2.md`

### Feishu Doc Output | 飞书文档输出

- Preferred: create a Feishu/Lark doc and return the doc link.
- Fallback: if doc creation is not available due to permission/tooling limits, output a fully structured "doc body" that the user can paste into a new doc, and clearly state what capability/permission is missing.

### Tables | 表格

- Use standard Markdown tables (they may be converted into native tables by Feishu automatically).
- Do NOT use Markdown code blocks for tables.
- Avoid too-wide tables; split into sub-tables when columns exceed 6.

### Coloring | 染色

- Base layer (Stage C API output) uses emoji + bold as the visual cue (do not rely on colors).
  - positive significant: `**✅ +X%**`
  - negative significant: `**🔻 -X%**`
  - not significant: `➖ 不显著`
- Enhanced layer (Block API post-processing) should use colored text styles first (L1), and only fall back to emoji (L2) or plain labels (L3) when Block API styling fails.
- Only mark as significant when significance is supported by the source (p-value or explicit significant flag). If the source does not provide significance evidence, keep directional wording only.

### Metric Naming | 指标命名

- In the report body (first appearance), use: `中文解释（完整英文指标名）` + change marker.
  - Example: `发送或点赞消息天数（Send or Like Message Days/Days） **✅ +0.0156%**`
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
