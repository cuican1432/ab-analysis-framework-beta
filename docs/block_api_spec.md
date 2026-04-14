## Block API Spec

This file intentionally mirrors `docs/beautification_spec_v1.2.md` (full content) for convenience.

---

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

（完整内容见同目录 `beautification_spec_v1.2.md`。）

