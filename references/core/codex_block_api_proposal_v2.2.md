Codex 修改提案 V2.2: Block API 美化层完整实现

目标: 在 ab-analysis-framework-beta 仓库中实现飞书文档 Block API 美化能力。

v2.2 变更 (相对 v2.1):
1. 颜色图例改用 quote_container (type=34)
2. 实验信息改用 inline text (bold key + value) — 规避大表格 API 限制
3. 新增 文档清理策略 — "新文档"或"空白覆盖"替代不可靠的循环删除
4. 新增 P-19 ~ P-26 陷阱 — 大表格、insert_table_row、env变量、emoji降级
5. "V3 Clean" 美化策略 — 保留原始报告结构，仅叠加视觉增强
6. 数据附录保留 5列完整表 (指标/相对变化/绝对变化/95%CI/P值)
7. 表格行数硬性约束: <=8行，超出拆分或改 inline text
8. 显著性标注三级降级: 颜色文字(L1) > emoji(L2) > 纯文字(L3)；能用颜色就不用emoji

前提: 所有 pattern 已通过 1400+ 次实际 API 调用验证。

---

M-1: 新增 docs/block_api_spec.md

文件路径: docs/block_api_spec.md

内容: 纳入 beautification_spec_v1.2.md 完整内容。v1.2 vs v1.1 关键变更:

| 变更项 | v1.1 | v1.2 |
|---|---|---|
| 颜色图例容器 | Callout (19) | quote_container (34) |
| 实验信息展示 | 15行大表格 | inline text |
| 表格行数限制 | 无限制 | <=8行 |
| 数据附录表 | 3列 | 5列 (保留绝对变化+CI) |
| 文档清理 | 循环DELETE | 新文档/空白覆盖 |
| Pitfall 数量 | P-1~P-18 | P-1~P-26 |
| 美化策略 | 重构+美化 | V3 Clean: 仅美化不重构 |
| 显著性标注 | 颜色+emoji混用 | 三级降级: 颜色>emoji>文字 |

---

M-2: 修改 docs/report_output_rules.md

2a. Enhanced Layer + V3 Clean 原则

## Enhanced Layer: Block API 美化 (post-processing)

### "V3 Clean" 美化原则
- ✅ 保留原始报告章节结构和顺序
- ✅ 对已有内容叠加视觉增强
- ❌ 不新增/删减/重排章节

### 显著性标注规则

能用颜色文字标明，就不要用 emoji:

- L1 (首选): Block API 颜色+粗体+底色
- L2 (降级): emoji (✅🔻⚠️➖) — 仅 L1 不可用时
- L3 (兜底): 纯文字 [正向显著] 等 — 仅 L1+L2 都不可用时

2b. 表格规范 (v1.2 双模式)

### 表格规范

分结论表 (3列): 指标 | 相对变化 | P值，列宽 [300, 150, 120]

数据附录表 (5列): 指标 | 相对变化 | 绝对变化 | 95%CI | P值，列宽 [200, 110, 90, 160, 90]

共同规则:
- header_row: true
- 行数 <=8 (超出拆分)
- 相对变化+P值列用 L1 颜色配套

### 实验信息 (v1.2: inline text)

bold key + value 逐行展示，不用大表格。
仅实验臂配置 (<=5行) 保留表格。

---

M-3: 修改 docs/tooling.md

## 飞书 Block API

### 认证

TOKEN = os.environ.get("LARK_USER_ACCESS_TOKEN") or \
        os.environ.get("MIRA_LARK_USER_ACCESS_TOKEN", "").replace("Bearer ", "")

### Block类型速查

| type | 名称 | 字段名 | 备注 |
|---|---|---|---|
| 2 | 文本 | text | |
| 3/4/5 | H1/H2/H3 | heading1/2/3 | 需style |
| 12 | 无序列表 | bullet | 非11 |
| 13 | 有序列表 | ordered | 非12 |
| 19 | Callout | callout | 非14; 容器 |
| 22 | 分隔线 | divider | 必须含{} |
| 31 | 表格 | table | <=8行 |
| 34 | 引用容器 | quote_container | 容器; 图例 |

### 显著性配套 (L1 首选, 能用颜色就不用emoji)
- 正向显著: bold=True, color=4, bg_color=4
- 负向显著: bold=True, color=1, bg_color=1
- 边际显著: bold=True, color=2
- 不显著: color=7

### Top 5 陷阱
1. Callout type 19 不是 14
2. text_color 1-7, >=8 报错
3. 表格 <=8行
4. divider `"divider": {}`
5. 文档清理用空白覆盖不用循环DELETE

---

M-4: 修改 docs/runbook.md

## Stage C+: 报告美化

### 文档准备
不要循环DELETE (P-19)。用新文档或空白覆盖。

### 美化流程
1. 插入颜色图例 (quote_container, 文字标注不用emoji)
2. 逐章节执行:
   - 标题 → H2 + 蓝色▎
   - 结论 → Callout (数值用 L1 颜色, 不用emoji)
   - 实验信息 → inline text
   - 分结论 → 3列指标表 + 显著性着色
   - 风险 → warning Callout
   - 附录 → 5列完整表
3. 每步独立 try-except

### 显著性标注降级 (核心)
L1: 颜色+粗体+底色 ← 首选, 能用颜色就不用emoji
L2: emoji (✅🔻⚠️➖) ← 仅L1不可用时
L3: 纯文字 ← 仅L1+L2都不可用时

### 表格约束
- 分结论: 3列 | 附录: 5列 | 对比: 4列
- 行数 <=8, 超出拆分
- 所有表 header_row: true

---

M-5: 修改 SKILL.md

### 报告美化 Hard Constraints

MUST DO:
- ✅ Block API 美化, TOKEN 从 env 读取
- ✅ "V3 Clean" — 保留原始结构，仅叠加美化
- ✅ 颜色图例: quote_container, 文字标注不用emoji
- ✅ 显著性标注: L1颜色(首选) > L2 emoji(降级) > L3文字(兜底)
- ✅ 分结论3列, 附录5列, 行数<=8
- ✅ 实验信息: inline text
- ✅ 美化失败静默降级

MUST NOT:
- ❌ 在颜色可用时使用emoji标注显著性
- ❌ 添加"判断"列
- ❌ 重构原始章节结构
- ❌ 创建超8行表格
- ❌ 硬编码 TOKEN
- ❌ text_color >= 8
- ❌ block_type=14 作 Callout (是19)
- ❌ block_type=11 作列表 (bullet=12)
- ❌ 省略 divider 空对象 / heading style
- ❌ 循环DELETE清空大文档

---

M-6: 新增 scripts/beautify_report.py

6a. create_color_legend() — quote_container, 纯文字标注

6b. create_experiment_info() — inline text

6c. create_metric_table() — 双模式

6d. colorize_value() — L1 首选

6e. prepare_document() — 清理

---

给 Codex 的 Top 10 提醒
1. Callout type 19 不是 14
2. text_color 1-7 only
3. 表格 <=8行
4. divider "divider": {}
5. heading/list 需 style
6. table_cell bg不可PATCH — 用text bg_color
7. 颜色图例用 quote_container (34)
8. 实验信息用 inline text
9. 文档清理用空白覆盖
10. 能用颜色文字就不用emoji; emoji仅是降级手段

