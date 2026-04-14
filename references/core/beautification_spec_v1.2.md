飞书 Block API 美化规范 v1.2

版本: v1.2 (2026-04-14)

变更: 相对 v1.1:
1. 颜色图例改用 quote_container (type=34) 替代 Callout — 用户偏好更轻量的视觉
2. 实验信息改用 inline text — 规避大表格(>8行)创建 invalid param 的 API 限制
3. 新增 P-19 ~ P-26 陷阱 — 文档清理、大表格、insert_table_row、emoji降级等实战踩坑
4. 明确"V3 clean 美化"策略 — 保留原始报告结构，仅叠加视觉增强，不重构章节
5. 数据附录表格保留完整列 — 分结论用3列简洁表，数据附录保留5列(含绝对变化+CI)
6. 文档清理策略 — 明确清空文档的正确方法与限制
7. 显著性标注三级降级 — 颜色文字优先 > emoji降级 > 纯文字兜底；能用颜色就不用emoji

---

## 一、架构概览

### 1.1 两层输出策略 (Two-Layer Output)

| 层级 | 描述 | 实现方式 |
|---|---|---|
| Base Layer | 标准 Markdown 报告 | LLM 输出 Markdown → upload_to_feishu_tool 写入飞书 |
| Enhanced Layer | 视觉美化 | beautify_report.py 调用飞书 Block API 后处理 |

### 1.2 美化策略: "V3 Clean" 原则

核心原则: 保持原始报告结构不变，仅叠加视觉增强。

| DO | DON'T |
|---|---|
| 对现有文字添加颜色/粗体 | 新增章节 |
| 用 Callout 包裹结论/警告 | 重新排列章节顺序 |
| 表格加 header_row + 显著性着色 | 改变原有表格的列数(附录表) |
| 章节间加 divider | 删减或合并原有内容 |
| H2 加蓝色竖线装饰 | 重写分析结论 |
| 文档头加颜色图例 | 添加原报告没有的分析维度 |

---

## 二、API 基础

### 2.1 认证

```python
TOKEN = os.environ.get("LARK_USER_ACCESS_TOKEN") or \
        os.environ.get("MIRA_LARK_USER_ACCESS_TOKEN", "").replace("Bearer ", "")
```

### 2.2 Block 类型映射表 (全部实测验证)

| block_type | 名称 | JSON 字段名 | 备注 |
|---|---|---|---|
| 2 | 文本 | text | 基础文本块 |
| 3 | 一级标题 | heading1 | 需 style.align + style.folded |
| 4 | 二级标题 | heading2 | 同上 |
| 5 | 三级标题 | heading3 | 同上 |
| 12 | 无序列表 | bullet | 不是 11 |
| 13 | 有序列表 | ordered | 不是 12 |
| 15 | 引用 | quote | — |
| 19 | Callout | callout | 不是 14; 容器Block |
| 22 | 分隔线 | divider | 必须含 "divider": {} |
| 31 | 表格 | table | cells传空; 行数<=8 |
| 32 | 表格单元格 | table_cell | 只读, API自动创建 |
| 34 | 引用容器 | quote_container | 容器Block; 用于颜色图例 |

---

## 三、颜色编码体系

### 3.1 text_color (前景色, 范围 1-7 ONLY)

| 值 | 颜色 | 用途 |
|---|---|---|
| 1 | 暗红 | 负向显著指标、风险警告 |
| 2 | 橙色 | 边际显著 (p<0.1) |
| 3 | 黄色 | 备注、注意事项 |
| 4 | 绿色 | 正向显著指标、推荐 |
| 5 | 蓝色 | 中性信息、装饰线 |
| 6 | 紫色 | 标题装饰、关键术语 |
| 7 | 灰色 | 不显著指标、辅助文本 |

### 3.2 background_color (背景色, 范围 1-15+)

| 值 | 颜色 | 用途 |
|---|---|---|
| 1 | 浅红 | 负向显著文字底色高亮 |
| 3 | 浅黄 | 注意事项 Callout 背景 |
| 4 | 浅绿 | 正向显著文字底色高亮 / Callout 背景 |
| 5 | 浅蓝 | 信息提示 Callout 背景 |
| 6 | 浅紫 | 关键结论标注 |

### 3.3 显著性样式配套规则 (核心规则)

核心: 能用颜色文字标明，就不要用 L2 前缀。L2 仅是降级手段。

三级降级策略 (Degradation Priority):

| 优先级 | 方式 | 何时使用 | 示例 |
|---|---|---|---|
| L1 首选 | 颜色+粗体+底色 (Block API) | Block API 可用时 | bold=True, color=4, bg_color=4 |
| L2 降级 | 方向箭头前缀 | 仅 Block API 颜色不可用时 | ↑ +0.16%、↓ -0.15%、↗ +0.06%、↘ -0.05% |
| L3 兜底 | 纯文字标注 | emoji 也不支持时 | [正向显著] +0.16% |

L1 首选: Block API 颜色配套

| 显著性 | 样式 | 说明 |
|---|---|---|
| 正向显著 | bold=True, color=4, bg_color=4 | 绿色粗体+绿色底色 |
| 负向显著 | bold=True, color=1, bg_color=1 | 红色粗体+红色底色 |
| 边际显著 | bold=True, color=2 | 橙色粗体，无底色 |
| 不显著 | color=7 | 灰色，非粗体 |

L2 降级标记 (仅在 L1 不可用时): ↑正向 / ↓负向 / ↗边际正向 / ↘边际负向 / ➖不显著

L3 兜底纯文字 (仅在 L1+L2 都不可用时): [正向显著] / [负向显著] / [边际显著] / [不显著]

Python 实现:

```python
def sig_tr(value, sig):
    """L1 首选: Block API 颜色配套"""
    if sig == "pos":
        return tr(value, bold=True, color=4, bg_color=4)
    elif sig == "neg":
        return tr(value, bold=True, color=1, bg_color=1)
    elif sig == "marginal":
        return tr(value, bold=True, color=2)
    else:
        return tr(value, color=7)

def sig_markdown(value, sig):
    """L2/L3 降级: Markdown fallback"""
    emoji_map = {"pos": "↑", "neg": "↓", "ns": "➖"}
    label_map = {"pos": "[正向显著]", "neg": "[负向显著]", "marginal": "[边际显著]", "ns": "[不显著]"}
    if sig == "marginal":
        return f"{'↘' if '-' in value else '↗'} {value}"  # L2
    emoji = emoji_map.get(sig, "")
    if emoji:
        return f"{emoji} {value}"  # L2
    return f"{label_map.get(sig, '')} {value}"  # L3
```

---

## 四、报告结构 · 逐元素美化规范

### 4.1 颜色图例 (quote_container, 文档最顶部)

图例内容只使用颜色文字标注，不使用 emoji。

```text
r = post(doc_id, [{"block_type": 34, "quote_container": {}}])
qid = r["data"]["children"][0]["block_id"]
post(qid, [
    txt([tr("阅读指引 | Color Legend", bold=True)]),
    txt([
        sig_tr("+X.XX%", "pos"), tr(" 正向显著（绿色粗体+绿色底色）"),
        tr("    "),
        sig_tr("-X.XX%", "neg"), tr(" 负向显著（红色粗体+红色底色）"),
        tr("    "),
        sig_tr("+X.XX%", "marginal"), tr(" 边际显著（橙色粗体）"),
        tr("    "),
        sig_tr("+X.XX%", "ns"), tr(" 不显著（灰色）"),
    ]),
])
```

### 4.2 章节标题 (H2 带蓝色装饰)

```json
{"block_type": 4, "heading2": {
  "elements": [text_run("▎", color=5), text_run(" {title}", bold=true)],
  "style": {"align": 1, "folded": false}
}}
```

### 4.3 结论 Callout

Callout 内的数值统一用 L1 颜色配套，不用 emoji 前缀。
Callout 容器本身的 emoji_id 是容器装饰，与数值标注无关。

### 4.4 实验信息 (Inline Text, 非表格)

```text
post(doc_id, [
  txt([tr("实验名称", bold=True), tr("：XXX")]),
  txt([tr("实验周期", bold=True), tr("：2025-09-12 ~ 2025-10-27")]),
])
```

### 4.5 分结论指标表 (3列)

```text
t_rows = [
  [[tr("指标", bold=True)], [tr("相对变化", bold=True)], [tr("P 值", bold=True)]],
  [[tr("Stay Duration/User")], [sig_tr("+0.1613%", "pos")], [sig_tr("0.001", "pos")]],
]
make_table(doc_id, t_rows, [300, 150, 120])
```

### 4.6 数据附录表 (5列, 完整版)

```text
appendix = [
  [[tr("指标", bold=True)], [tr("相对变化", bold=True)], [tr("绝对变化", bold=True)], [tr("95% CI", bold=True)], [tr("P 值", bold=True)]],
  [[tr("Stay Duration/User")], [sig_tr("+0.1613%", "pos")], [tr("+3.00s")], [tr("[+0.055%, +0.268%]")], [sig_tr("0.001", "pos")]],
]
make_table(doc_id, appendix, [200, 110, 90, 160, 90])
```

---

## 五、完整报告美化流程

### 5.1 V3 Clean 元素顺序 (严格遵循原始结构)

1. [quote_container] 颜色图例 (文字标注，不用emoji)
2. [H2] ▎总结论
3. [Callout] 核心结论摘要 (数值用颜色)
4. [text] v1/v2 详述
5. [Callout] 阻断提示
6. [Divider] ─────────
7. [H2] ▎总建议
8. [bullet] 建议列表
9. [Divider] ─────────
10. [H2] ▎实验背景与设计
11. [text] 实验信息 (inline)
12. [Table] 实验组（arm）(<=5行)
13-28. [H2+Table+text] 分结论1-4 (3列表)
29-34. [H2+Table+Callout] 风险与异常
35-36. [H2+Callout] DM安全护栏
37-39. [H2+ordered] 待确认
40-44. [H2+H3+Table] 数据附录 (5列表)

### 5.2 已有表格着色（L2 -> L1）

对于 Base Layer 已经写入飞书的 Markdown 表格：

- 不要重写整份报告
- 不要尝试 `<text bgcolor=...>` 这类 Markdown 内联样式
- 优先使用 `GET /documents/{doc_id}/blocks` 一次拿全量 blocks，在内存中识别目标 cell
- 优先使用 `PATCH /documents/{doc_id}/blocks/batch_update` 批量提交 `update_text_elements`
- 应遍历现有 `BLOCK_TABLE` 的 `cells`
- 对单元格文本中的 `↑` / `↓` / `↗` / `↘` / `➖` 前缀做识别
- 先移除 L2 前缀，再对纯数值应用 `sig_tr()` 的 L1 样式

这样可以在不改变表格结构的前提下，为已有表格中的显著性数值补色。

### 5.3 文档清理策略

| 方案 | 推荐度 | 说明 |
|---|---|---|
| A: 新文档 | 推荐 | 创建空白docx → 写入 → 返回新URL |
| B: 空白覆盖 | 可用 | upload_to_feishu_tool(" ") → POST blocks |
| C: 循环DELETE | 不推荐 | 大文档不可靠 |

---

## 六、Pitfall 完整清单 (P-1 ~ P-30)

| # | 陷阱 | 正确做法 |
|---|---|---|
| P-1 | Callout type | 19, 不是 14 |
| P-2 | 无序列表 type | 12 (bullet), 不是 11 |
| P-3 | 有序列表 type | 13 (ordered), 不是 12 |
| P-4 | text_color 范围 | 1-7 only |
| P-5 | background_color | 1-15+ |
| P-6 | divider 空对象 | "divider": {} |
| P-7 | heading 字段名 | heading1/2/3 对应 3/4/5 |
| P-8 | heading/list style | "style": {"align": 1, "folded": False} |
| P-9 | Callout 容器 | 先POST callout, 再POST children |
| P-10 | table cells | "cells": [], 从response读 |
| P-11 | table_cell bg | 不支持block级PATCH |
| P-12 | 替代: 文字底色 | text_element_style.background_color |
| P-13 | delete/merge index | exclusive end |
| P-14 | quote_container | type=34 |
| P-15 | text style | "style": {} 不可省 |
| P-16 | TOKEN | env读取, 禁硬编码 |
| P-17 | POST index | -1=追加末尾 |
| P-18 | 分结论表3列 | 指标/变化/P值, 无判断列 |
| P-19 | 文档清理 | 循环DELETE不可靠, 用新文档/覆盖 |
| P-20 | 大表格 | row_size>=10 可能 invalid param, <=8行 |
| P-21 | insert_table_row | 不稳定, 创建时定好行数 |
| P-22 | 中文引号 | 统一英文引号 |
| P-23 | 读table cell | 用read_lark_content一次获取 |
| P-24 | env变量名 | 做兼容 get("A") or get("B") |
| P-25 | 附录表列数 | 分结论3列, 附录5列 |
| P-26 | emoji仅降级用 | 能用颜色文字就不用emoji; L1颜色>L2emoji>L3文字 |
| P-27 | batch_delete 参数位置 | start_index/end_index 必须在 body 里，不是 query params |
| P-28 | DELETE 单个容器子 block | 容器子 block 可能 404；用父容器 batch_delete |
| P-29 | document_revision_id=-1 | batch_delete 用 -1 表示最新版本，避免版本冲突 |
| P-30 | placeholder block 清理 | Base layer 写入后 doc root 可能有 placeholder text block，需要后置清理 |

---

## 七、降级策略

### 7.1 显著性标注降级 (P-26 核心规则)

能用颜色文字标明，就不要用 L2 前缀。L2 仅是 Block API 颜色不可用时的降级手段。

如果后续还会执行 Enhanced Layer：
- Base Layer 的 `↑` / `↓` / `↗` / `↘` / `➖` 需要在应用 L1 样式前先移除
- 同一个数值上不要同时保留 L2 前缀和 L1 颜色/底色

| 优先级 | 方式 | 使用条件 |
|---|---|---|
| L1 首选 | 颜色+粗体+底色 | Block API 可用 |
| L2 降级 | ↑ ↓ ↗ ↘ ➖ | 仅 L1 不可用时 |
| L3 兜底 | [正向显著] 等文字 | L1+L2 都不可用时 |

### 7.2 功能降级

| 失败场景 | 降级行为 |
|---|---|
| Callout 失败 | 保留 Markdown 引用块 |
| Table 失败 | 保留 Markdown 表格 |
| PATCH 颜色失败 | 保留纯文本 |
| TOKEN 无效 | 跳过全部美化 |
| 大表格 invalid param | 拆分小表或 inline text |

---

## 八、已验证能力矩阵

| 操作 | 状态 | 备注 |
|---|---|---|
| 创建 9 种 block | ✅ | 全部实测 |
| 创建 table (<=8行) | ✅ | |
| 创建 table (>8行) | ⚠️ | 特定位置失败 |
| 填充 table cell | ✅ | |
| PATCH header_row/column_width | ✅ | |
| PATCH merge_cells | ✅ | exclusive end |
| PATCH update_text_elements | ✅ | 颜色+粗体+底色 |
| insert_table_row | ⚠️ | 不稳定 |
| DELETE block | ⚠️ | 大文档不可靠 |
| table_cell background | ❌ | 用text bg_color替代 |
