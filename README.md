# ab-analysis-framework-beta

Source repository for two Mira skills that work together:

- `ab-analysis-framework-beta`
  - analysis skill for experiment reading, attribution, and decision support
- `ab-knowledge-builder-beta`
  - knowledge-builder skill for glossary / KB ingestion, normalization, and live knowledge maintenance

This repo is meant to be used as a paired setup:
- the builder skill seeds and maintains the live knowledge store under `userdata/ab-knowledge-builder-beta/*`
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
- the builder package ships seeded social KB / glossary content inside `userdata/ab-knowledge-builder-beta/*`
- the framework package can then read that knowledge layer immediately

### Step 4. What success looks like after upload
- `SKILL.md` at zip root
- `references/`, `userdata/`, `scripts/`, and package files at the same root level

---

## Quick Smoke Test | 快速烟测

If you want to quickly verify that the framework really works, use one of these public smoke test cases first:

- `Personalized Bubble / 个性化气泡`
  - Raw Data: [Lark Raw Data Doc](https://bytedance.larkoffice.com/docx/L2kwdjvt5oLCwsxbB7Wc6uMRnud)
  - PRD: [Lark PRD](https://bytedance.larkoffice.com/wiki/BT70wFcLAi5eh3k2ihJc4LCynWe)

- `DM Card UI Optimization / 私信卡片 UI 优化`
  - Raw Data: [Lark Raw Data Doc](https://bytedance.larkoffice.com/docx/GTtkd0Ixnos3VExjttecsuKEnxp)
  - PRD: [Lark PRD](https://bytedance.sg.larkoffice.com/docx/GNMUdHluloFyw3xeaSklIAaSgee)

The simplest validation flow is:

1. Install the two skills above.
2. In your Mira conversation, reference `ab-analysis-framework-beta`.
3. Pass the `PRD` link and `Raw Data` link directly into the skill.
4. Check whether it can follow the doc-first path and produce a structured experiment report.

Note (beautification):
- Conclusion / Risk callouts render their own icon. Do not keep a leading inline status emoji (e.g. `💡`, `⚠️`) in the same line, or it may show as "double emoji".
- The arrow reading guide line is included only when direction markers (e.g. `↑`, `↓`, `↗`, `↘`, `➖`) still appear in the final doc.

你可以直接复制粘贴下面任意一个 prompt：

```text
请使用 ab-analysis-framework-beta 结合这个 PRD 和 Raw Data 一起分析并生成实验报告。
烟测硬规则：每次都必须从当前链接重新读取源文档；不要复用历史文件、旧报告或之前的中间产物。
实验名称（可选）：[Personalized Bubble]
PRD 链接：https://bytedance.larkoffice.com/wiki/BT70wFcLAi5eh3k2ihJc4LCynWe
Raw Data 链接：https://bytedance.larkoffice.com/docx/L2kwdjvt5oLCwsxbB7Wc6uMRnud
```

```text
请使用 ab-analysis-framework-beta 结合这个 PRD 和 Raw Data 一起分析并生成实验报告。
烟测硬规则：每次都必须从当前链接重新读取源文档；不要复用历史文件、旧报告或之前的中间产物。
实验名称（可选）：[DM Card UI Optimization]
PRD 链接：https://bytedance.sg.larkoffice.com/docx/GNMUdHluloFyw3xeaSklIAaSgee
Raw Data 链接：https://bytedance.larkoffice.com/docx/GTtkd0Ixnos3VExjttecsuKEnxp
```

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

```text
请使用 ab-analysis-framework-beta 结合这个 PRD 和 Raw Data 一起分析并写实验报告。
```

### Usage Guide | 使用指南

#### Scenario 1. Write an experiment report

Use this when:
- the experiment observation window has ended
- the data is ready
- you want the skill to read the PRD and raw data together, then write the report

You can say:

```text
请使用 ab-analysis-framework-beta 基于这个 PRD 和 Raw Data 生成一份实验报告。

实验名称（可选）：[例如：DM Personalized Bubble]

PRD 链接：[URL]

Raw Data 链接：[URL]
```

What the system will do:
- run the doc-first analysis flow
- silently read the stored glossary and KB first
- use the existing analysis rules and report schema
- output a structured experiment report instead of scattered notes

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

#### （1）指标定义入库：把“指标定义文档”写入 glossary

维度（尽量给全；缺字段我会先推断，再把不确定项标出来让你确认）：
- 指标名（metric name）
- 指标含义（meaning）
- 别名（aliases，可为空）
- 极性（polarity：上涨=好/坏/不确定）
- 计算说明（calculation notes，可为空）

示例输入：指标定义文档（飞书链接 / 表格粘贴均可）

```text
请使用 ab-knowledge-builder-beta 将这些指标定义写入 glossary（指标含义、别名、极性、计算说明）；请先自行判断并补全，遇到不确定点再向我确认。
指标定义文档链接（或直接粘贴表格）：[URL 或 pasted text]
```

#### （2）KB 更新：把“新来源”沉淀成可复用的产品机制知识（DM 业务）

维度（尽量给全；缺字段我会先推断，并列出 3-5 条待确认问题）：
- 来源链接/正文（source）
- 适用范围（默认 DM，可改）
- 关键机制（用户路径、触发条件、约束、边界）

示例输入：一个 PRD / 复盘 / 机制说明文档

```text
请使用 ab-knowledge-builder-beta 用这个新来源更新 DM knowledge base，并提取可复用的产品机制知识；不确定处请列出待确认问题。
新来源链接（或直接粘贴正文）：[URL 或 pasted text]
```

#### （3）指标组归一化：规范 metric group 的“组含义与使用方式”

维度（尽量给全；缺字段我会先推断，再让你确认关键不确定点）：
- 指标组名（group name）
- 组含义（group meaning）
- 业务域（business domain：如 DM/Inbox/Share 等）
- 优先级（priority：如 P0/P1/P2/P3）
- scope（覆盖的人群/场景/口径边界）
- typical usage（典型使用方式：什么时候优先看它）

示例输入：指标组说明文档（或直接粘贴内容）

```text
请使用 ab-knowledge-builder-beta 规范这个指标组（组含义、业务域、优先级、scope、typical usage），缺信息时先推断后向我确认。
指标组文档链接（或直接粘贴内容）：[URL 或 pasted text]
```

#### （4）口径/标签归一化：规范“指标含义 + 口径标签”

维度（尽量给全；缺字段我会先推断，并明确标注为 to-confirm 让你确认）：
- 指标名
- 口径标签（如 uv/au、days/days、days/user、pv/user、ratio）
- 分子/分母定义（如果是 ratio）
- 时间窗/统计口径（如 1d/7d/14d，是否去重）

示例输入：口径说明文档（或直接粘贴）

```text
请使用 ab-knowledge-builder-beta 规范这些指标含义和口径标签（如 uv/au、days/days、days/user、pv/user、ratio），并把不确定处标注为 to-confirm 让我确认。
口径说明文档链接（或直接粘贴内容）：[URL 或 pasted text]
```

---

## Package Layout | 包结构

Each installable package is built so that:
- `SKILL.md` is at the zip root
- `README.md`, `references/`, `userdata/`, and `scripts/` are at the same zip-root level

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

### `userdata/ab-knowledge-builder-beta/*`

Live knowledge layer:
- actual glossary content
- actual KB content
- custom rules
- continuously updated local knowledge

Path note:

- Paths like `userdata/...` and `references/...` are relative to the installed skill root (zip root), not the sandbox/workspace `pwd`.

This is the layer that should keep growing over time.

---

## Current Live Knowledge Root | 当前 live knowledge 根目录

```text
userdata/ab-knowledge-builder-beta/
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
- writing and updating `userdata/ab-knowledge-builder-beta/*`
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
- `userdata/ab-knowledge-builder-beta/*`
  - live glossary / KB / custom rules
- `release/*.zip`
  - Mira install packages
