# ab-analysis-framework-beta

Source repository for two Mira skills that work together:

- `ab-analysis-framework-beta`
  - analysis skill for experiment reading, attribution, and decision support
- `ab-knowledge-builder-beta`
  - knowledge-builder skill for glossary / KB ingestion, normalization, and live knowledge maintenance

This repo is meant to be used as a paired setup:
- the builder skill seeds and maintains the live knowledge store under `userdata/ab-analysis-framework-beta/*`
- the framework skill reads that knowledge store and applies the analysis schema

---

## Quick Start | 快速开始

### Step 1. Download these two packages

- [Download `ab-knowledge-builder-beta.zip`](https://github.com/cuican1432/ab-analysis-framework-beta/raw/main/release/ab-knowledge-builder-beta.zip)
- [Download `ab-analysis-framework-beta.zip`](https://github.com/cuican1432/ab-analysis-framework-beta/raw/main/release/ab-analysis-framework-beta.zip)

Do not use the GitHub auto-generated source zip from the repo page.

### Step 2. Install the two packages in Mira

1. Open `Mira`
2. Open `Skills`
3. Open `Manage Skills`
4. Upload `ab-knowledge-builder-beta.zip`
5. Wait until the first upload finishes
6. Upload `ab-analysis-framework-beta.zip`
7. Wait until the second upload finishes

Install them in this order:
- upload the knowledge-builder package first
- then upload the analysis framework package

### Step 3. Why this order matters
- the builder package ships seeded social KB / glossary content inside `userdata/ab-analysis-framework-beta/*`
- the framework package can then read that knowledge layer immediately

### Step 4. What success looks like after upload
- `SKILL.md` at zip root
- `references/`, `userdata/`, and package files at the same root level

---

## What Each Skill Is For | 两个 Skill 分别做什么

### 1. `ab-analysis-framework-beta`

Use this when the main job is:
- generating an experiment report
- reading PRD + raw data together in order to write the report
- applying the stored glossary / KB during that report-writing workflow

Typical use cases:
- A/B 实验观测结束，需要输出实验报告
- 已经有 PRD 和 raw data，想直接写实验报告

Example prompts:
- `Please use ab-analysis-framework-beta to generate an experiment report.`
- `Please use ab-analysis-framework-beta to analyze this PRD and raw data together.`

### 2. `ab-knowledge-builder-beta`

Use this when the main job is:
- building or updating the glossary
- building or updating KB topics
- migrating knowledge into the live store
- normalizing metric meaning / polarity / caliber / priority
- maintaining indexes and reading guides

Typical use cases:
- 想把新整理的指标定义沉淀到知识库
- 想把一批 KB 文档整理进 live knowledge store
- 想统一某个 metric group 的含义、priority、caliber

Example prompts:
- `Please use ab-knowledge-builder-beta to ingest this glossary content.`
- `Please use ab-knowledge-builder-beta to update the DM knowledge base with this new source.`
- `Please use ab-knowledge-builder-beta to normalize these metric meanings and caliber tags.`

---

## Package Layout | 包结构

Each installable package is built so that:
- `SKILL.md` is at the zip root
- `README.md`, `references/`, and `userdata/` are at the same zip-root level

Current packaged files:
- `release/ab-analysis-framework-beta.zip`
- `release/ab-knowledge-builder-beta.zip`

---

## Layering Model | 分层模型

### `references/core/*`

Hard analysis layer:
- workflow
- rules
- runbook
- memory / tooling guidance

### `references/knowledge/*`

Reading layer:
- indexes
- guides
- interpretation patterns
- stable examples
- migration-time references

This layer tells the skills:
- how to read knowledge
- how to navigate knowledge
- how to interpret common patterns

### `userdata/ab-analysis-framework-beta/*`

Live knowledge layer:
- actual glossary content
- actual KB content
- custom rules
- continuously updated local knowledge

This is the layer that should keep growing over time.

---

## Current Live Knowledge Root | 当前 live knowledge 根目录

```text
userdata/ab-analysis-framework-beta/
├── glossary/
│   ├── metric_groups.md
│   ├── metric_groups_table.md
│   ├── dimensions.md
│   ├── dimension_values.md
│   └── metrics_by_group/*.md
├── kb/
│   ├── business_kb.md
│   ├── dm.md
│   ├── messaging_support.md
│   ├── platform_terms.md
│   ├── story.md
│   └── ur.md
└── custom_rules/
```

The builder package includes this seeded live knowledge so that a new user starts with a usable social KB instead of an empty userdata layer.

---

## Read / Write Responsibility | 读写职责

### `ab-knowledge-builder-beta`

Owns:
- writing and updating `userdata/ab-analysis-framework-beta/*`
- normalizing live knowledge content
- maintaining seeded knowledge quality over time

### `ab-analysis-framework-beta`

Owns:
- reading the live knowledge layer
- applying experiment-analysis rules
- using domain-first recall and metric interpretation logic
- producing report-ready analysis

---

## Linkage Rule | 联动规则

This repo uses a one-way linkage rule:

- `ab-knowledge-builder-beta` is the source-of-truth editor for live knowledge content
- `ab-analysis-framework-beta` is the consumer of that knowledge layer

Update the framework skill only when one of these changes:
- the knowledge path changes
- the knowledge schema changes
- the read order changes
- new required indexes or reading categories are introduced
- analysis rules must adapt to newly stabilized knowledge conventions

Do not update the framework skill for pure knowledge-content growth by default.

---

## Repo Contents | 仓库主要内容

- `SKILL.md`
  - framework skill entry
- `skills/ab-knowledge-builder-beta/SKILL.md`
  - knowledge-builder skill entry
- `references/core/*`
  - analysis rules and workflow
- `references/knowledge/*`
  - reading-layer indexes, guides, and patterns
- `userdata/ab-analysis-framework-beta/*`
  - live glossary / KB / custom rules
- `release/*.zip`
  - Mira install packages
