# Runbook

## When Starting a New Case

1. Confirm the source materials.
   - PRD
   - raw data docs
   - screenshots / tables
   - optional live Libra page
2. Identify the experiment object.
3. Identify the main metrics and guardrails.
4. Build the candidate metric set.
5. Extract or read facts into Stage A.
6. Turn Stage A into Stage B logic.
7. Write Stage C as a decision-oriented memo.
8. Evaluate in Stage D when needed.

Practical reminder:

- do not start by polishing language,
- start by making sure the source set is complete,
- then make sure the metric recall set is complete,
- and only then move into writing.

## When Maintaining Glossary / Business Knowledge

- Do not expect the source to arrive in perfect glossary format.
- Start by turning raw knowledge into a structured draft.
- Keep metric groups, metrics, dimensions, and business terms separated.
- Treat business knowledge as an index, not a monolithic article.
- Pull the topic you need instead of loading everything.
- Fill only what can be confirmed from the source.
- Leave uncertain fields blank.
- Always print a short `to confirm` list for the reviewer.
- Do not make the reviewer discover gaps by rereading the whole draft.

Recommended collaboration loop:

1. source knowledge in,
2. structured draft out,
3. explicit `to confirm` list,
4. user review,
5. partial ingest of stable entries,
6. keep unfinished parts in `drafts/` or the current run's draft area,
7. continue in the next round when needed.

Practical split:

- put stable, reusable items into:
  - `references/knowledge/glossary/`
  - `references/knowledge/kb/`
- keep still-evolving or partially confirmed content in:
  - `drafts/` or the current run's draft area

## When the Source Looks Wrong

- Check whether the issue is:
  - missing data,
  - wrong extraction,
  - wrong metric match,
  - wrong interpretation.
- If source facts are wrong, rerun A from source.
- Do not patch old A output manually.

Useful triage order:

1. confirm whether the source itself is missing the field,
2. confirm whether the extraction path is wrong,
3. confirm whether the metric was matched to the wrong row,
4. confirm whether the interpretation drifted after extraction.

If the problem is in steps 1-3, fix the source read and rebuild from A.
If the problem is only in step 4, fix B/C without pretending the data changed.

## When Doing Attribution

- Start from the main movement first.
  - What is the one result that actually matters for the decision?
- Then prioritize `2-3` attribution paths that are most likely to close the loop.
- If a clear path / funnel-style chain exists, prefer considering it first because it is often easier to close the mechanism loop.
  - For example: `A -> B -> C`, such as exposure -> click -> conversion, or entry -> use -> downstream result.
- Then ask which attribution route is most promising:
  - path / funnel,
  - user composition,
  - metric formula,
  - space / cannibalization,
  - time trend,
  - data quality,
  - external or product interference.
- Use the shortest route that can explain the movement clearly.
- Do not force every case through every attribution direction.
- If a funnel chain is incomplete, use the attribution route that best explains the movement instead of forcing a funnel story.
- Prefer a closed path chain over scattered slice anecdotes when both are available.
- If attribution is still weak, label it as indirect evidence or a hypothesis to verify.

Practical chain template:

1. what changed in the product or exposure,
2. which mechanism, path, interaction node, or structural factor was most likely affected,
3. which metrics moved,
4. what business theme that movement supports,
5. what uncertainty remains,
6. what should be checked next.

When possible, prefer a clean chain such as:

- entry / exposure -> action -> downstream outcome
- setting / permission change -> usage path change -> metric movement
- button / layout change -> interaction error or friction -> risk metric movement

If the source only supports steps 1 and 3, do not pretend that steps 2 and 4 are fully proven. Mark the middle link as indirect evidence or a hypothesis to verify.

### Attribution Red Lines (Anti-Hallucination) | 归因推演红线（反幻觉）

- Attribution and logic chains must be grounded in source facts.
  - For UI/interaction experiments, prioritize PRD "physical interaction facts" when applicable to explain movements (for example: click distance, UI layer occlusion, operation steps length, interaction path change).
  - Other allowed attribution routes (must be evidence-bound):
    - funnel / path chain (A -> B -> C)
    - user composition shift
    - metric formula decomposition
    - space / cannibalization
    - time trend / seasonality / regression-to-mean checks
    - data quality / logging / sampling issues
    - external or product interference
- Absolute forbidden language:
  - do not use unsupported psych speculation like "用户觉得花里胡哨", "主观反感", "心理预期下降" unless the source has objective evidence.
- Anti-survivorship bias:
  - core secondary metrics (for example: DM sticker/camera/group chat) are not optional.
  - if any of them has significant movement, it must be fully disclosed and given a dedicated deep-analysis subsection; do not hide it just because it is not the primary headline metric.
- Experiment config must be extracted verbatim:
  - 实验背景与配置抓取红线 (MUST DO):
    - 在撰写正文 `实验背景与设计` 章节之前，必须从输入物料（Raw Data 或 PRD 的头部）进行“节点级全量提取”，严禁自行精简或舍弃。
    - 必留字段白名单化（一个不落，必须一字不漏）：
      - 实验名称与实验链接
      - 实验周期 / 数据日期
      - 实验类型 / 实验机房 (Data Center)
      - 流量分层 (Traffic Layer)
      - 分流单元 (Sharding Unit / Unit)
      - 实验原始配置总流量 / 放量信息 / 各版本流量比例
    - 过滤条件 (Filter) 的特殊保护：
      - 寻找物料中的“生效对象”、“受众”或“过滤条件”
      - 若包含技术流代码（如 `version_code >= 440300`、`app_id in [...]` 等 SQL/Python 片段），必须用代码块包裹并原封不动保留
      - 严禁为了“排版美观”删减或口语化翻译
    - 呈现格式要求：
      - 强制以前置列表或属性表格的形式，作为报告开头背景底座展示
      - 必须保持键值对（Key-Value）的结构化呈现，不要揉进长段落

## When Writing the Report

- Required report structure (strict):
  1. 总结论 + 总建议（先给决策结论，再给 rollout/下一步建议）
  2. 分结论 A：结论 -> 归因链路 -> 细节表格
  3. 分结论 B：结论 -> 归因链路 -> 细节表格
  4. （如有）风险/警示：结论 -> 归因链路 -> 细节表格

- Lead with the decision.
- Then show the strongest evidence.
- Then surface the most decision-relevant risks.
- Then state the remaining boundary or evidence gap.
- If the experiment has multiple treatment arms, do not stop at separate arm summaries.
- In multi-arm cases, add a dedicated comparison section that answers: who is better overall, who is weaker overall, and which differences actually matter for the decision.
- Only compare fine-grained product-mechanism differences across arms when the source explicitly shows those config or description differences.

Practical writing order:

1. 总结论：直接回答 rollout / decision question（先结论后背景）
2. 总建议：下一步怎么做（上线/灰度/继续观测/补数据/加监控）
3. 分结论（重复多次）：
   - 分结论 judgment（这段想表达的结论）
   - attribution chain（最可信的归因链路，按源材料能支持的程度标注边界）
   - detail table（把支撑该结论的关键指标用原生表格列出来）
4. 如 multi-arm：增加“横向对比”分结论，同样用 结论 -> 归因链路 -> 细节表格
5. 收口：剩余不确定性 / to confirm / 风险项与补充验证建议

For each major section, try to complete this mini-order:

1. section judgment,
2. representative metrics and values,
3. business interpretation,
4. attribution chain,
5. remaining caveat or next step.

Good section pattern:

- `judgment`: what this section says overall
- `evidence`: the 2-5 metrics that actually support that judgment
- `business meaning`: what kind of behavior or risk that implies
- `attribution`: the strongest chain the source can support
- `action`: what to verify, mitigate, or watch next

Do not leave the reader with raw numbers only when the report is meant to drive a decision.

What to avoid:

- opening with background instead of the decision,
- piling up every significant metric into the main conclusion,
- mixing global evidence and slice evidence without saying which is which,
- sounding more certain than the evidence allows,
- writing a section that reports numbers but never explains why they matter.

### Feishu Doc Formatting Hard Rules | 飞书文档格式硬规则

When outputting the final experiment report:

- Output must be a Feishu/Lark doc and provide the doc link.
- Tables must be native Feishu tables, not Markdown code blocks:
  - use `<table header-row="true" col-widths="300,180,180"> ... </table>` and keep explicit pixel-level widths.
- Significant movements must be highlighted with colors:
  - positive significant: `<font color="green">...</font>`
  - negative significant: `<font color="red">...</font>`
- Metric naming must be strict: `中文名 (英文名)` (example: `发送消息量 (Send Message PV)`).
  - do not output `[数据缺失]` unless truly missing in source; if missing, state what is missing and which source should contain it.
- Use callouts for decision-driving parts:
  - conclusion / core insights: `<callout icon="..." bgc="3" bc="..."> ... </callout>`
  - risk / warning: `<callout icon="..." bgc="1" bc="..."> ... </callout>`

### Data Appendix (Physical Clone) | 数据附录（物理级克隆）

- In the final stage, always add `## 数据附录 (Data Appendix)` to the end of the report.
- The appendix is the "absolute evidence chain" for review:
  - do not truncate or summarize the underlying detail tables in the appendix.
- Preferred path:
  - fetch all detail tables from the bottom of the Raw Data doc via API and "physically clone" the table nodes into the new doc.
- Fallback chain (do not summarize):
  - If API access is not available due to permission/tooling limits:
    - copy/export the full raw tables into the appendix without summarization,
    - and explicitly list which raw tables could not be cloned and why (permission/tooling/unavailable).
  - If even copying/exporting is not possible:
    - manually create native Feishu tables and fill in all rows/columns as-is from the source,
    - and explicitly state this is a manual fallback and what limitation caused it.
