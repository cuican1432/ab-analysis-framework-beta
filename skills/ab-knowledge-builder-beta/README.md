# ab-knowledge-builder-beta

This package is the knowledge-builder companion skill.

Use it when the main job is knowledge maintenance (glossary / KB), not writing an experiment report.

## What This Skill Owns

- Live glossary content (writable): `userdata/ab-knowledge-builder-beta/glossary/*`
- Live business knowledge (writable): `userdata/ab-knowledge-builder-beta/kb/*`
- Local reusable overrides (writable): `userdata/ab-knowledge-builder-beta/custom_rules/*`
- For install/runtime environments, the framework skill may fall back to a packaged snapshot under `references/knowledge/userdata_snapshot/ab-knowledge-builder-beta/*` when userdata is missing.

Reading guides live in `references/knowledge/*`.

## You Can Paste

```text
（1）指标定义入库：把“指标定义文档”写入 glossary
请使用 ab-knowledge-builder-beta 将这些指标定义写入 glossary（指标含义、别名、极性、计算说明）；请先自行判断并补全，遇到不确定点再向我确认。
指标定义文档链接（或直接粘贴表格）：[URL 或 pasted text]

（2）KB 更新：把“新来源”沉淀成可复用的产品机制知识（DM 业务）
请使用 ab-knowledge-builder-beta 用这个新来源更新 DM knowledge base，并提取可复用的产品机制知识；不确定处请列出待确认问题。
新来源链接（或直接粘贴正文）：[URL 或 pasted text]
```
