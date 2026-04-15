---
name: ab-analysis-framework-beta
description: A/B 实验分析框架主入口技能。主要用于实验报告生成，以及基于 PRD 与 Raw Data 联合解读后输出标准化实验报告。用户提到 A/B 实验分析、实验复盘、实验报告、PRD + 数据联合解读并希望直接写报告时，应优先使用本技能。
---

# AB Analysis Framework

It mainly supports two task types:

1. Experiment Report Generation
2. Report Generation with Temporary Guidance

You do not need to remember the internal helper skills. In most cases, calling `ab-analysis-framework-beta` directly is enough.

If the main goal is to build or normalize the knowledge store itself rather than run experiment analysis, use `ab-knowledge-builder-beta`.

## 1) Experiment Report Generation

### Use this when
- 实验观测期结束，数据已经就绪
- 需要基于 PRD + raw data 文档快速生成标准化实验报告

### You can say
- Please use `ab-analysis-framework-beta` to generate an experiment report.
- Experiment name (optional): [xxx]
- PRD link (Feishu/Lark docx preferred): [URL]
- Raw Data link (Feishu/Lark docx preferred): [URL]

### Hard Constraints | 关键硬约束
- Output the final result as a Feishu/Lark doc when tooling permits; otherwise return a fully structured doc body the user can paste.
- Input priority: treat Feishu/Lark doc links (PRD + Raw Data docx) as the primary inputs. If the user did not provide links, ask for them before making interpretation claims.
- Follow the strict report structure: `总结论 + 总建议` first, then repeat `分结论 -> 归因链路 -> 细节表格`.
- Keep attribution evidence-bound. No unsupported psych speculation.
- Fully disclose significant movements of core secondary metrics; do not hide them because they are not the headline metric.
- Before writing `实验背景与设计`, extract required setup/config fields from the source header verbatim. Missing fields must be `not found`; PRD/Raw Data conflicts must be shown side-by-side with `to confirm`.
- Do not truncate the raw detail tables in `## 数据附录 (Data Appendix)`. Follow the fallback chain in `references/core/report_output_rules.md`.
- For detailed output/formatting/appendix rules, use `references/core/report_output_rules.md` as the single source of truth.
- Enhanced Layer (auto when token available): after the base report is written, if a valid Block API token is available, apply the Enhanced Layer rules in `references/core/beautification_spec_v1.2.md` without changing report structure ("V3 Clean"). If Block API is not available, keep Base Layer Markdown output only.
- User prompt precedence: if the user's current prompt specifies structure, emphasis, writing style, or temporary interpretation preferences, follow the user's prompt by default as long as it does not violate `Absolute Hard Rules`. Current-run user instructions override reusable `custom_rules` and framework default preferences.
- Override handling: if a user instruction or `custom_rules` only conflicts with default guardrails, warn about the consequence and confirm whether they still want to proceed. If it conflicts with `Absolute Hard Rules`, do not follow it; explain the reason and offer the closest safe alternative.
- Framework-only mode note: if knowledge files are not available/installed, do not guess caliber/polarity/domain mapping. Use Raw Data names as-is; push unresolved items into `to confirm`. Significant claims require verifiable evidence (p-value or explicit significant flag + source_location); otherwise keep directional wording only.

### What the system will do
- run the doc-first analysis workflow
- silently prioritize stored metric glossary and business knowledge
- recall core-flag metric groups by default, especially any group marked as company-core, business-core, or sub-business-core
- identify the experiment's primary business domain first, then apply domain-first recall before ordering metric groups
- perform attribution, risk review, and evidence-boundary labeling when needed
- output a structured experiment report as a Feishu/Lark doc using standard Markdown (tables, direction markers, bold emphasis) rather than scattered analysis fragments

### Beautification Rules (Auto When Token Available) | 美化规则（有 token 自动执行）

What is the token:

- `token` means your Feishu/Lark access token, used to let the tool modify the doc style via Block API after the base report is written.
- If you do not provide a token, the report will still be generated, but it will stay in the base (Markdown) style.

Default behavior:

- If a valid token is available in the environment, the framework will automatically run the beautification post-processing step after writing the doc.
- If token is missing/invalid, the framework will skip beautification and keep the base output, and add a short note in `to confirm` / report header.

How to provide the token:

- Set one of these environment variables (do not paste tokens into the report body or share in chat):
  - `LARK_USER_ACCESS_TOKEN="Bearer <token>"`
  - `MIRA_LARK_USER_ACCESS_TOKEN="Bearer <token>"`

Execution rule (make it automatic, do not rewrite scripts):

- After `upload_to_feishu_tool` returns a doc link, ALWAYS run the built-in post-processing step to beautify the same doc when token is available.
- Extract `<doc_id>` from the returned doc link `https://.../docx/<doc_id>` before calling the beautification script.
- CRITICAL: You MUST call the packaged script for beautification. Do NOT write custom Block API code during the run.
- CRITICAL: Do NOT attempt Markdown-only inline styling such as `<text bgcolor=...>` for Feishu doc beautification.
- Do not write a new "beautification script" in the report run. Reuse the packaged script:
  - `python3 scripts/beautify_report.py --doc-id <doc_id> --decorate-headings`
  - If running from a sandbox/workspace where relative paths do not point to the skill root, locate the skill root first:
    - `SKILL_ROOT=$(python3 scripts/find_skill_root.py) && cd "$SKILL_ROOT"`
- The beautification script is idempotent by default: if the doc already appears beautified, skip mutating steps instead of beautifying again.
- Only use `--force-reapply` when you explicitly need to re-run beautification on an already beautified doc.

MUST DO:

- ✅ use Block API only as post-processing (Enhanced Layer); Base Layer stays standard Markdown
- ✅ keep "V3 Clean": do not add/remove/reorder chapters
- ✅ token from env (no hardcode): `LARK_USER_ACCESS_TOKEN` or `MIRA_LARK_USER_ACCESS_TOKEN`
- ✅ significance marking: L1 (color+bold+bg) > L2 (direction markers: `↑` / `↓` / `↗` / `↘` / `➖`) > L3 (plain labels)
- ✅ format split: Base Layer Markdown uses `↑` / `↓` / `↗` / `↘` / `➖`; Enhanced Layer L1 removes those markers and keeps only styled `+/-` numeric values
- ✅ summary tables: 3 columns; appendix tables: 5 columns; row_count <= 8 (split when needed)
- ✅ even when a metric is `不显著`, keep relative change / absolute change / CI / p-value whenever the source provides them; `—` only means the source value is truly missing
- ✅ experiment info: inline text (bold key + value)
- ✅ degrade silently when Block API fails
- ✅ emit at most one legend / reading-guide block in Base Layer; let the packaged beautification script own legend replacement/deduplication
- ✅ use plain paragraph emphasis for conclusion / risk highlights (for example `💡 **结论：...**` / `⚠️ **风险：...**`), not Markdown blockquote

MUST NOT:

- ❌ stack L2 markers (`↑` / `↓` / `↗` / `↘` / `➖`) on top of L1 color styling
- ❌ add a "judgment" column to summary tables
- ❌ restructure original chapters
- ❌ create tables > 8 rows
- ❌ hardcode tokens or log tokens

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

## Internal reference map

- Report Generation →
  - `references/core/*`
  - `references/knowledge/glossary/index.md`
  - `references/knowledge/kb/index.md`
  - then follow default read order steps `3-6` below when the case needs knowledge recall
- Temporary Guidance Report →
  - `references/core/*`
  - `references/knowledge/glossary/index.md`
  - `references/knowledge/kb/index.md`
  - current-run temporary guidance first, then follow default read order steps `3-6` below

## Core Read Order

When reading `references/core/*`, use this order:

1. `workflow.md`
2. `rules.md`
3. `memory.md`
4. `runbook.md`
5. `report_output_rules.md`
6. `tooling.md`

## Storage Hint

- Knowledge reading layer → `references/knowledge/*`
- Packaged userdata snapshot (read-only fallback) → `references/knowledge/userdata_snapshot/ab-knowledge-builder-beta/*`
- Long-term live glossary content → `userdata/ab-knowledge-builder-beta/glossary/*`
- Long-term live business knowledge → `userdata/ab-knowledge-builder-beta/kb/*`
- Glossary maintenance rules → `references/knowledge/glossary_guide.md`
- Business knowledge maintenance rules → `references/knowledge/knowledge_guide.md`
- Runtime local incremental layer → `userdata/ab-knowledge-builder-beta/*`
- Memory can help recall, but it is not the main glossary store

Path note:

- Paths like `userdata/...` and `references/...` are relative to the skill install root (zip root), not the sandbox/workspace `pwd`.

## Userdata Boundary

When the user wants to inject local knowledge, local data files, or run-specific reusable notes, use `userdata/ab-knowledge-builder-beta/` as the default writable layer.

- Local glossary additions / partial confirmations → `userdata/ab-knowledge-builder-beta/glossary/`
- Local business notes / project context → `userdata/ab-knowledge-builder-beta/kb/`
- User-specific interpretation rules / temporary reusable overrides → `userdata/ab-knowledge-builder-beta/custom_rules/`

Do not casually rewrite packaged shared references during normal ingestion:

- packaged knowledge guides and reading indexes stay in `references/knowledge/*`
- local evolving and long-term live knowledge should go to `userdata/ab-knowledge-builder-beta/*`

Default read order:

1. `references/core/*`
2. current-run explicit temporary guidance
3. `references/knowledge/*`
4. `references/knowledge/userdata_snapshot/ab-knowledge-builder-beta/*` (read-only fallback when userdata is missing)
5. `userdata/ab-knowledge-builder-beta/custom_rules/*`
6. `userdata/ab-knowledge-builder-beta/glossary/*`
7. `userdata/ab-knowledge-builder-beta/kb/*`

If both snapshot and userdata exist, prefer `userdata/` (writable/live) and treat snapshot as a safety net for install/runtime environments that lose userdata.

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

`ab-analysis-framework-beta` reads the live knowledge layer under `userdata/ab-knowledge-builder-beta/*`, but it does not own detailed knowledge-content editing.

Compatibility note: some older installs may still place knowledge under `userdata/ab-analysis-framework-beta/*`. If both paths exist, prefer the `ab-knowledge-builder-beta` namespace.

Update this framework skill when one of these changes:

- the knowledge path changes
- the knowledge schema changes
- the read order changes
- new required indexes or reading categories are introduced
- analysis rules must adapt to newly stabilized knowledge conventions

Do not update this framework skill for pure knowledge-content growth by default.
