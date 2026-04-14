# Tooling

## Default Tool Preference

- Prefer local files and structured docs first.
- If browser work is needed, prefer:
  - the environment's available browser / Playwright MCP
  - a scriptable remote browser tool when available
- Use direct CDP only as a fallback when the browser is already open but the gateway path is unstable.

## Tooling Principle

- Prefer scriptable, traceable steps over manual one-off handling.
- Prefer structured extraction over copy-paste summaries.
- Prefer validators when label fidelity or row fidelity matters.

## Browser Note

When live Libra extraction is required:

- reuse the same tab when possible,
- avoid repeated reopen / refocus churn,
- keep provenance when available.

## Feishu Block API (Beautification)

Use this only for Enhanced Layer post-processing (visual beautification). Stage C output should still be Base Layer Markdown.

Authentication token:

```python
TOKEN = os.environ.get("LARK_USER_ACCESS_TOKEN") or \
        os.environ.get("MIRA_LARK_USER_ACCESS_TOKEN", "").replace("Bearer ", "")
```

Hard constraints:

- table row_count <= 8 (including header)
- text_color range is 1-7 only
- callout block_type is 19 (not 14)
- bullet list block_type is 12, ordered list is 13
- divider must include `"divider": {}`

Canonical spec: `references/core/beautification_spec_v1.2.md`

Block type mapping (quick reference, keep in sync with canonical spec):

| block_type | name | json field | note |
|---|---|---|---|
| 2 | text | text | base text block |
| 3 | heading1 | heading1 | requires style.align + style.folded |
| 4 | heading2 | heading2 | requires style.align + style.folded |
| 5 | heading3 | heading3 | requires style.align + style.folded |
| 12 | bullet list | bullet | not 11 |
| 13 | ordered list | ordered | not 12 |
| 15 | quote | quote | |
| 19 | callout | callout | not 14; container block |
| 22 | divider | divider | must include `{}` |
| 31 | table | table | row_count <= 8; create with cells=[] |
| 32 | table_cell | table_cell | read-only, API creates |
| 34 | quote_container | quote_container | container block |

Pitfalls (P-1 ~ P-30):

1. Callout type is 19, not 14.
2. Bullet list type is 12 (bullet), not 11.
3. Ordered list type is 13 (ordered), not 12.
4. text_color range is 1-7 only.
5. background_color range is 1-15+.
6. divider must include `"divider": {}`.
7. heading field names: heading1/2/3 correspond to 3/4/5.
8. heading/list must include `"style": {"align": 1, "folded": False}`.
9. Callout/quote_container are container blocks: create container first, then POST children.
10. table cells: create with `"cells": []`, then read cell_ids from response.
11. table_cell background is not supported via block-level PATCH.
12. use text_element_style.background_color to highlight text instead.
13. delete/merge end_index is exclusive.
14. quote_container is block_type=34.
15. text block style: `"style": {}` must be present (can be empty but do not omit).
16. token must be read from env; never hardcode it.
17. POST index: -1 appends to the end.
18. summary tables are 3 columns (metric / relative change / p-value), no "judgment" column.
19. document cleanup: looping DELETE is unreliable; use new doc or overwrite.
20. big tables: row_size >= 10 may fail invalid param; keep <= 8 rows.
21. insert_table_row is unstable; decide row_size when creating.
22. quote style: use consistent ASCII quotes in code examples to avoid copy errors.
23. read table cells: prefer one-shot read of doc block tree if available.
24. env var names: support both `LARK_USER_ACCESS_TOKEN` and `MIRA_LARK_USER_ACCESS_TOKEN`.
25. appendix tables: summary is 3 columns, appendix is 5 columns.
26. emoji is only a fallback: L1 color > L2 emoji > L3 plain labels.
27. batch_delete indices must be in JSON body (start_index/end_index), not query params.
28. deleting container child blocks directly may 404; use parent's batch_delete instead.
29. document_revision_id=-1 means "latest" for batch_delete to avoid revision conflicts.
30. doc root may contain a placeholder text block after base-layer write; cleanup at the end.
