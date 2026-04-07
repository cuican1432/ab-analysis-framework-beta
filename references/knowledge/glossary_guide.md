# Glossary Guide | 指标字典维护说明

这个文件用于解释：
- glossary 怎么组织
- 字段是什么意思
- draft 和 formal 怎么流转
- 用户怎么更新 glossary

正式 glossary 内容请看：
- `references/knowledge/glossary/index.md`
- `references/knowledge/glossary/`

## Design Principle | 设计原则

glossary 不建议揉成一张大表。推荐按正式内容拆成多层文件：

1. `Metric Group Index | 指标组索引`
2. `Metric Index | 指标索引`
3. `Dimension Index | 维度索引`

原因：

- 指标组是召回和组织单位
- 指标是解释和归因单位
- 维度是下钻和切片单位

## Key Terms | 关键字段说明

### `polarity`

表示这个指标往哪个方向变通常更好。

建议只用：
- `higher_is_better`
- `lower_is_better`
- `depends_on_context`
- `descriptive_only`

### `typical_usage`

表示这个组或指标通常怎么被使用，不是当前实验的最终角色。

### `priority_hint`

表示这项内容在组内或解释时的常见优先级提示。

## Priority and Business-Domain View | 优先级与业务域视角

- glossary 中记录的 `importance` 或 `priority_hint` 应理解为 base priority，而不是所有实验下都不变的绝对优先级
- 同一个指标组在不同 primary business domain 下，实际召回顺序和报告优先级可以变化
- 如果当前 priority 主要是从某个业务域视角校准出来的，例如 `DM`，切到 `Share&Repost`、`Sticker`、`Inbox` 等视角时，需要重新排序，不要直接照抄
- 实验分析时应先判断 primary business domain，再做 domain-first recall 和优先级提升

## Templates | 模板

### Metric Group Template

```yaml
group_name:
group_aliases:
  -

description_zh:
description_en:

usage_scope:
is_company_core:
is_business_core:
is_sub_business_core:

typical_usage:
priority_hint:

common_dimensions:
  -

notes:
```

For `common_dimensions`, only record dimensions that are explicitly present in the raw data, source table, or stable formal source. Do not invent default dimensions from habit or prior cases.

### Metric Template

```yaml
group_name:
metric_name:
metric_aliases:
  -

meaning_zh:
meaning_en:

caliber_meaning:
calculation_method:
numerator:
denominator:

polarity:
priority_hint:

neighbor_metric_diff:
interpretation_notes:
```

### Dimension Template

```yaml
dimension_name:
dimension_aliases:
  -

meaning_zh:
meaning_en:

applies_to_groups:
  -

applies_to_metrics:

value_examples:
  -

warnings:
```

## Draft vs Formal | 草稿和正式库

### Formal

放在：
- `references/knowledge/glossary/`

特点：
- 已确认
- 可复用
- 不带待确认项
- 不带 case-specific 结论
- `references/knowledge/glossary/index.md` 只做索引，不承载维护说明

### Draft

放在：
- `drafts/` 或当前运行环境的待确认草稿区

特点：
- 已整理但未定稿
- 允许空字段
- 允许 `to confirm`
- 允许 placeholder

## Update Loop | 更新流程

推荐协作方式：

1. 用户给原始知识库或零散知识
2. 先整理成 glossary draft
3. 主动输出 `to confirm`
4. 用户用中文优先确认关键字段
5. confirmed 条目分批进入正式库
6. unfinished 内容继续留在 drafts

不要让用户自己通篇找问题。
