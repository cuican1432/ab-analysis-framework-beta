# Knowledge Base Index | 业务知识索引

这里是 **knowledge reading layer** 里的 KB 入口页。  
This is the entry page for the KB reading layer.

这里放的是：
- 业务知识索引
- 产品机制阅读入口
- PRD 阅读提示
- 稳定口径模式与通用术语参考
- 迁移阶段保留的示例性知识页

这里不放的是：
- glossary schema
- case-specific 结论
- 临时 run-only 规则
- 持续增长的 live knowledge 正文

如果你要看“KB 怎么维护、什么该进 KB、什么不该进 KB”，请看：
- `references/knowledge/knowledge_guide.md`

如果你要写入或持续积累实际业务知识，请优先写到：
- `userdata/ab-analysis-framework-beta/kb/`

---

## Current KB Topics | 当前知识主题

- `references/knowledge/kb/platform_terms_outline.md`
  - TikTok - Platform Terms Outline Source
- `references/knowledge/kb/metric_caliber_patterns.md`
  - Common Multi-Day Metric Caliber Patterns
- `references/knowledge/kb/metric_caliber_metric_inventory.md`
  - Current Formalized Metric Caliber Classification
Live KB topics (writable, source-of-truth):
- `userdata/ab-analysis-framework-beta/kb/business_kb.md`
- `userdata/ab-analysis-framework-beta/kb/dm.md`
- `userdata/ab-analysis-framework-beta/kb/messaging_support.md`
- `userdata/ab-analysis-framework-beta/kb/platform_terms.md`
- `userdata/ab-analysis-framework-beta/kb/story.md`
- `userdata/ab-analysis-framework-beta/kb/ur.md`

---

## Reading Hint | 使用提示

- 先看这个索引，再按需进入具体 topic
- 不需要默认把整个 KB 通读一遍
- 只拿当前 case 真正需要的知识页
- 把这里优先当成阅读和导航层，而不是长期 live knowledge 主库
- Core Interaction holds shared cross-domain concepts; DM / Story / UR hold direction-specific concepts and their group mappings
- Use `userdata/ab-analysis-framework-beta/kb/platform_terms.md` when you need stable meanings for repeated platform-level metrics and product terms such as `DAU`, `MAU`, `Retention`, `VV`, `FYP`, `Internal Share`, or `Search`.
- Use `platform_terms_outline.md` when you need the source outline for future expansion of platform-wide metric terminology (reading/pattern layer).
- Use `metric_caliber_patterns.md` when you need to interpret common experiment metric families such as `days/days`, `days/user`, `pv/user`, and `uv/user`.
- Use `metric_caliber_metric_inventory.md` when you want the current formalized metrics classified by inferred caliber family.
- Use `userdata/ab-analysis-framework-beta/kb/messaging_support.md` when you need stable, support-documented messaging, notification, or adjacent sharing mechanics rather than metric definitions.
- `userdata/ab-analysis-framework-beta/kb/messaging_support.md` also covers official support-backed streak mechanics, sticker mechanics, push/inbox notification rules, and share/repost feature links.
