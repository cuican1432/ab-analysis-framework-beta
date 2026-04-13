---
name: ab-knowledge-builder-beta
description: A/B experiment knowledge-builder skill for glossary, KB, metric-group, caliber, and local knowledge-store maintenance. Use when the goal is to build, ingest, migrate, or normalize knowledge content rather than generate an experiment report. This skill owns the live knowledge content layer under userdata/ab-analysis-framework-beta/*.
---

# AB Knowledge Builder Beta

Use this skill when the main job is knowledge work, not experiment reporting.

It mainly supports four task types:

1. Glossary Ingestion and Cleanup
2. KB Ingestion and Topic Structuring
3. Metric-Group / Caliber Normalization
4. Knowledge Migration and Store Maintenance

## Use this skill when

- you are building or updating the glossary
- you are building or updating the KB
- you are migrating knowledge between layers
- you are normalizing metric meaning, polarity, priority, or caliber
- you are updating indexes, guides, or reading hints for the knowledge system

## Do not use this skill when

- the main goal is to generate an experiment report
- the main goal is to make an experiment decision
- the task is primarily about PRD + raw data interpretation for one experiment run

In those cases, use `ab-analysis-framework-beta`.

## Storage Ownership

- Live glossary content belongs in `userdata/ab-analysis-framework-beta/glossary/*`
- Live business knowledge belongs in `userdata/ab-analysis-framework-beta/kb/*`
- Local reusable overrides belong in `userdata/ab-analysis-framework-beta/custom_rules/*`

Treat `references/knowledge/*` as the reading layer:

- indexes
- guides
- interpretation patterns
- stable examples
- migration-time references

Do not treat `references/knowledge/*` as the default live knowledge store.

## Default Builder Behavior

- write new or evolving knowledge to `userdata/ab-analysis-framework-beta/*` by default
- keep entries reusable and topic-based
- prefer stable wording over case-specific writeups
- keep unresolved content marked as draft or to-confirm when needed
- update indexes and guides when the reading path changes

## You can say

```text
（1）指标定义入库：把“指标定义文档”写入 glossary
你提供的文档里最好包含这些维度：
- 指标名（metric name）
- 指标含义（meaning）
- 别名（aliases，可为空）
- 极性（polarity：上涨=好/坏/不确定）
- 计算说明（calculation notes，可为空）
如果缺字段，我会先 infer 一个草案并把不确定项标出来请你确认。

请使用 ab-knowledge-builder-beta 将这些指标定义写入 glossary（指标含义、别名、极性、计算说明），并在缺信息时先推断后向我确认。
指标定义文档链接（或直接粘贴表格）：[URL 或 pasted text]

（2）KB 更新：把“新来源”沉淀成可复用的产品机制知识（DM 业务）
你提供的内容里最好包含：
- 来源链接/正文（source）
- 适用范围（默认 DM，可改）
- 关键机制（用户路径、触发条件、约束、边界）
如果缺“范围/机制”，我会先按内容推断并列出 3-5 条待确认问题。

请使用 ab-knowledge-builder-beta 用这个新来源更新 DM knowledge base，并提取可复用的产品机制知识；不确定处请列出待确认问题。
新来源链接（或直接粘贴正文）：[URL 或 pasted text]

（3）指标组归一化：规范 metric group 的“组含义与使用方式”
你提供的信息里最好包含：
- 指标组名（group name）
- 组含义（group meaning：这组指标想回答什么问题）
- 业务域（business domain：如 DM/Inbox/Share 等）
- 优先级（priority：如 P0/P1/P2/P3）
- scope（这组指标覆盖的人群/场景/口径边界）
- typical usage（典型使用方式：做什么结论时优先看它）
如果缺字段，我会 infer 并把关键不确定点请你确认。

请使用 ab-knowledge-builder-beta 规范这个指标组（组含义、业务域、优先级、scope、typical usage），缺信息时先推断后向我确认。
指标组文档链接（或直接粘贴内容）：[URL 或 pasted text]

（4）口径/标签归一化：规范“指标含义 + 口径标签”
你提供的信息里最好包含：
- 指标名
- 口径标签（如 uv/au、days/days、days/user、pv/user、ratio）
- 分子/分母定义（如果是 ratio）
- 时间窗/统计口径（如 1d/7d/14d，是否去重）
如果缺“分子分母/时间窗”，我会先推断并明确标注为 to-confirm。

请使用 ab-knowledge-builder-beta 规范这些指标含义和口径标签（如 uv/au、days/days、days/user、pv/user、ratio），并把不确定处标注为 to-confirm 让我确认。
口径说明文档链接（或直接粘贴内容）：[URL 或 pasted text]
```

## Linkage Rule With `ab-analysis-framework-beta`

`ab-knowledge-builder-beta` is the source-of-truth editor for the live knowledge content layer.

Update `ab-analysis-framework-beta` only when one of these changes:

- the knowledge path changes
- the knowledge schema changes
- the read order changes
- new required indexes or reading categories are introduced
- analysis rules must adapt to newly stabilized knowledge conventions

Pure knowledge-content growth does not require a framework-skill update by default.
