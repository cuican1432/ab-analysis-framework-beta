# ab-analysis-framework-beta

Source repository for the Mira version of `ab-analysis-framework-beta`.

This repo is used for:
- maintaining the source skill package
- maintaining shared references and local-write conventions
- building the installable Mira zip

---

## Quick Start | 快速安装

### Mira install path | Mira 安装方式

Recommended install package:

- `release/ab-analysis-framework-beta.zip`

Do not install the GitHub auto-generated source zip from the repository page.
Use the packaged release zip above instead.

How to install in Mira:

1. Open `Mira`
2. Open `Skills`
3. Open `Manage Skills`
4. Upload `release/ab-analysis-framework-beta.zip`

After upload, Mira should recognize:
- `SKILL.md` at the zip root
- `references/`, `userdata/`, and other package files at the same zip root level

### Package requirement | 打包要求

This package is built so that:
- `SKILL.md` is at the zip root
- `README.md`, `references/`, and `userdata/` are packaged at the same zip root level

---

## What Is In This Repo | 这个仓库里有什么

- `SKILL.md`
  - main trigger and routing instructions
- `references/core/*`
  - workflow, rules, memory, runbook, tooling
- `references/knowledge/glossary/*`
  - formal glossary content
- `references/knowledge/kb/*`
  - formal business knowledge content
- `references/knowledge/glossary_guide.md`
  - glossary organization and update rules
- `references/knowledge/knowledge_guide.md`
  - knowledge-layer organization and boundary rules
- `userdata/tt-ab-analysis-framework/*`
  - local writable layer for user-provided knowledge, local overrides, and incremental files
- `release/ab-analysis-framework-beta.zip`
  - installable Mira package built from this source repo

---

## Knowledge Layout | 知识层结构

Stable shared knowledge lives in:

```text
references/
├── core/
└── knowledge/
    ├── glossary/
    ├── kb/
    ├── glossary_guide.md
    └── knowledge_guide.md
```

Local incremental knowledge lives in:

```text
userdata/tt-ab-analysis-framework/
├── glossary/
├── kb/
└── custom_rules/
```

### Shared vs Local

- `references/core/*`
  - hard framework rules and analysis behavior
- `references/knowledge/*`
  - stable shared glossary and business knowledge
- `userdata/tt-ab-analysis-framework/*`
  - local incremental knowledge
  - local overrides
  - user-specific additions

### Compatibility note | 兼容说明

- the older flat layout under `references/glossary/*`, `references/kb/*`, and top-level guide files has been retired
- old layout is deprecated and should not receive new writes
- all new reads and new writes should go to:
  - `references/knowledge/glossary/*`
  - `references/knowledge/kb/*`
  - `references/knowledge/glossary_guide.md`
  - `references/knowledge/knowledge_guide.md`

---

## Local Userdata Protocol | 本地用户数据写入协议

Use a skill-scoped userdata root instead of generic folders such as `userdata/glossary/` or `userdata/kb/`.

Recommended writable root:

```text
userdata/tt-ab-analysis-framework/
├── glossary/
├── kb/
└── custom_rules/
```

Why keep the `tt-ab-analysis-framework` namespace:
- avoids collisions with other skills or packages
- keeps local data easier to audit
- makes migration and backup less ambiguous

### What each folder is for

- `userdata/tt-ab-analysis-framework/glossary/`
  - local glossary additions
  - partial confirmations
  - local alias mapping
  - draft polarity notes

- `userdata/tt-ab-analysis-framework/kb/`
  - local business notes
  - project-specific context
  - temporary but reusable background knowledge

- `userdata/tt-ab-analysis-framework/custom_rules/`
  - user-specific interpretation rules
  - local reusable overrides
  - temporary special handling that should not go into shared references

### Minimal file examples

Local glossary note:

```md
# click_report

- definition: risk-related complaint metric
- polarity: lower_is_better
- aliases: complaint_click, click risk report
- status: local_draft
- note: use as negative-risk metric unless the current run explicitly says otherwise
```

Local KB note:

```md
# DM risk background

- scope: DM / social safety
- summary: click_report is usually reviewed together with other negative feedback metrics
- source: local team note
```

Local custom rule:

```md
# experiment_123_rule

- applies_to: experiment_123
- rule: click_report increase means worsening risk
- priority: local_override
- duration: temporary
```

### Read precedence | 读取优先级

Use this default order:

1. `references/core/*`
2. current-run explicit temporary guidance
3. `references/knowledge/*`
4. `userdata/tt-ab-analysis-framework/custom_rules/*`
5. `userdata/tt-ab-analysis-framework/glossary/*`
6. `userdata/tt-ab-analysis-framework/kb/*`

Notes:
- `references/core/*` is still the hard-rule layer
- local custom rules can refine interpretation, but should not override hard framework rules
- local glossary / KB files supplement the shared layer; they should not casually rewrite shared references

### Quick Rule | 速记版

- 写定义、别名、polarity，放 `userdata/tt-ab-analysis-framework/glossary/`
- 写背景、场景、业务说明，放 `userdata/tt-ab-analysis-framework/kb/`
- 写本地特例和临时复用规则，放 `userdata/tt-ab-analysis-framework/custom_rules/`
