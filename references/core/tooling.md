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
