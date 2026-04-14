# Runbook

## When Starting a New Case

1. Confirm the source materials.
   - PRD
   - raw data docs
   - screenshots / tables
   - optional live Libra page
2. Complete Stage A first.
   - extract setup / config fields from the source header
   - identify the experiment object
   - identify the main metrics and guardrails
   - consult glossary / KB
   - build the candidate metric set
3. Turn Stage A into Stage B logic.
4. Write Stage C as a decision-oriented memo.

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
6. keep unfinished parts in the current run's working context (do not pretend they are stable),
7. continue in the next round when needed.

Practical split:

- put stable, reusable items into:
  - `userdata/ab-analysis-framework-beta/glossary/`
  - `userdata/ab-analysis-framework-beta/kb/`
- keep still-evolving or partially confirmed content in:
  - the current run's working context (and keep a clear `to confirm` list)

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

Unexpected movement screening:

- When a metric shows significant movement but the metric's functional scope is outside the PRD's stated feature scope (for example, Camera send metrics move significantly but the PRD only covers text and voice bubble customization):
  - first check whether the movement can be explained by an indirect path (for example: overall chat entry frequency ↑ → all message types ↑ proportionally)
  - then check whether the movement could be a data-quality or caliber artifact
  - if neither explains it, label the movement as `[hypothesis to verify]` and do not fabricate a direct causal chain linking the feature to that metric

Practical chain template:

Follow the canonical 5-step attribution chain defined in `rules.md` (Attribution Discipline):

1. product / UX delta
2. most credible mechanism, path, or structural change
3. metric movement
4. business implication
5. remaining uncertainty or next validation step

When possible, prefer a clean chain such as:

- entry / exposure -> action -> downstream outcome
- setting / permission change -> usage path change -> metric movement
- button / layout change -> interaction error or friction -> risk metric movement

If the source only supports steps 1 and 3, do not pretend that steps 2 and 4 are fully proven. Mark the middle link as `[indirect evidence]` or `[hypothesis to verify]`.

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
      - （完整白名单见 `workflow.md` Stage A step 2）
    - 过滤条件 (Filter) 的特殊保护：
      - 寻找物料中的“生效对象”、“受众”或“过滤条件”
      - 若包含技术流代码（如 `version_code >= 440300`、`app_id in [...]` 等 SQL/Python 片段），必须用代码块包裹并原封不动保留
      - 严禁为了“排版美观”删减或口语化翻译
    - 呈现格式要求：
      - 强制以前置列表或属性表格的形式，作为报告开头背景底座展示
      - 必须保持键值对（Key-Value）的结构化呈现，不要揉进长段落
    - 缺字段处理（反幻觉）：
      - 若白名单字段在源文档头部找不到，必须标注为 `not found` 并进入 `to confirm` 列表；严禁自行推断补齐。
    - PRD 与 Raw Data 冲突处理：
      - 默认优先级：Raw Data 头部 > PRD 头部
      - 若存在冲突，必须并列展示并标注 `to confirm`，不得静默选择其一。

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
- When different arms have unequal data coverage (for example, one arm has 20 metric groups with data and another arm has only 6):
  - first, align on the metric groups that both arms have data for and produce a side-by-side comparison on those groups
  - then separately list the metric groups where only one arm has data, and explain the likely reason (for example, the arm's feature scope does not trigger certain metric groups)
  - do not force a comparison on metric groups where only one arm has data; instead, note the gap and label it as `[one-arm only]`
- Only compare fine-grained product-mechanism differences across arms when the source explicitly shows those config or description differences.

Practical writing order:

1. 总结论：直接回答 rollout / decision question（先结论后背景）
   - Every metric or signal referenced in `总结论` and `总建议` must include the full metric name as it appears in the Raw Data. Do not summarize as "N items showed significance" without listing the actual metric names. If the list is long (> 5 metrics), either list all of them or list the top 3 by impact and add "等 N 项，详见 §X.X" with a section cross-reference.
   - Add an explicit `证据完整度 (Evidence Completeness)` rating alongside the decision to avoid over-confident reading:
     - `High`: key metric groups readable, significant claims backed by p-values/flags, and `to confirm` items are minor
     - `Medium`: some key groups are summary-only or partial, or multiple `[hypothesis to verify]` remain
     - `Low`: key evidence missing/conflicting, or significant claims cannot be backed by p-values; mark the report as `初稿 / 待复核`
2. 总建议：下一步怎么做（按标准决策分级给出）
2.5 实验背景与设计：以 Key-Value 属性表格或前置列表展示实验配置底座（完整字段白名单见 `workflow.md` Stage A step 2；Stage C API 输出时按 `report_output_rules.md` 基础层使用标准 Markdown 表格）
3. 分结论（重复多次）：
   - 分结论 judgment（这段想表达的结论）
   - attribution chain（按 `rules.md` 的归因链模板组织，按源材料能支持的程度标注边界）
   - detail table（把支撑该结论的关键指标用原生表格列出来）
4. 如 multi-arm：增加“横向对比”分结论，同样用 结论 -> 归因链路 -> 细节表格
5. 收口：剩余不确定性 / to confirm / 风险项与补充验证建议

### Decision Taxonomy | 决策分级

Use one of these standard decisions in `总结论` / `总建议`:

1. `全量上线`
   - evidence is strong, core objective wins, and no blocking guardrail/risk is observed.
   - typical scenario: all Tier A metrics positive-significant, Tier B guardrails flat or positive, no unexplained anomalies.
2. `扩大灰度`
   - overall direction is positive, but more exposure or longer observation is still needed before full rollout.
   - typical scenarios:
     - core metrics positive but observation window is short (< 14 days) and the effect size is still converging
     - core metrics positive but an important secondary risk signal exists (for example: report rate ↑, performance regression on one platform) that needs a larger sample to confirm whether it converges or persists
     - multi-arm experiment where the winning arm is clear but a configuration detail needs validation at larger scale
3. `继续观测`
   - evidence is directionally useful but not stable enough yet (for example: short duration, noisy variance, or unresolved caveats).
   - typical scenarios:
     - most Tier A metrics are not significant yet, but directionally positive
     - experiment has only run for a few days; effect sizes may still be shifting
     - key dimension-level results contradict the global result and the reason is unclear
4. `补数据后再决策`
   - key setup / metric / appendix evidence is missing or conflicting; do not force a launch decision.
   - typical scenarios:
     - APP-level must-watch metrics are listed but have no data (`listed but no data provided`)
     - PRD and Raw Data conflict on experiment config and the discrepancy is unresolved
     - a critical metric group's data is clearly incomplete or shows logging issues
5. `回滚 / 不推荐上线`
   - core objective loses, major guardrails regress, or data quality / setup problems make rollout unsafe.
   - typical scenarios:
     - Tier A target metrics are negative-significant
     - company-core guardrails show significant regression with no mitigation path
     - major data-quality / caliber issues make the evidence unreliable and the rollout unsafe

Always explain:

- why this decision level is chosen,
- what condition would move it to the next level,
- what follow-up action is required.

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

### Output Rules Pointer | 输出规则指针

- Report output formatting (Feishu doc, tables, coloring, naming, callouts) is defined canonically in `references/core/report_output_rules.md`.
- Data appendix (physical clone + fallback chain) is also defined canonically in `references/core/report_output_rules.md`.

### Stage C+ (Optional): Beautification | 可选后处理：Block API 美化

If the user asks for richer visual styling and a valid Block API token is available, apply an Enhanced Layer post-processing step:

1. Document preparation:
   - do not loop DELETE to clear a large doc; use a new doc or overwrite with a blank base layer first.
2. Insert color legend:
   - use `quote_container` (block_type=34) and show the legend using colored text (no emoji).
3. Beautify top-to-bottom (each step try/except, degrade silently):
   - headings: H2 with blue decoration line
   - conclusions/risks: callout (block_type=19), values use L1 styling when possible
   - experiment info: inline text (bold key + value)
   - summary tables: 3 columns, row_count <= 8
   - appendix tables: 5 columns, row_count <= 8 (split when needed)

Significance marking degradation (core):

- L1: color+bold+bg via Block API (prefer this; do not use emoji when L1 works)
- L2: emoji fallback
- L3: plain labels fallback

Canonical spec: `references/core/beautification_spec_v1.2.md`
