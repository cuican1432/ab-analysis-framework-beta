# CHANGELOG

## [Unreleased]

### Fixed
- Userdata path resolution: added packaged read-only snapshot under `references/knowledge/userdata_snapshot/` as fallback when runtime userdata is empty.
- Stage C+ beautification: changed from opt-in to auto-trigger when Block API token is available.

### Changed
- 将 `SKILL.md` 收敛为三大主场景：`Experiment Report Generation`、`Report Generation with Temporary Guidance`、`Knowledge Ingestion`。
- 移除容易产生理解负担的独立 `Glossary` 主场景，相关能力并入 `Knowledge Ingestion` 链路。
- 将原先单独占位的 `Routing / Reference Map` 降为简短内部说明，不再作为主索引项。
- 继续保持 `SKILL.md` 为简洁、可安装、可直接触发的 index / menu 风格。
- Migrated live knowledge store namespace from `ab-analysis-framework-beta` to `ab-knowledge-builder-beta`; old paths kept as compatibility pointers.
- Deduplicated snapshot data: removed redundant `ab-analysis-framework-beta` snapshot copy and kept README pointers only.

### Added
- 在 `Knowledge Ingestion` 中明确 confirmed / draft / to confirm 的分流方式。
- 保留 `Storage Hint`，明确 shared knowledge、runtime local layer 与 memory 的边界。

### Packaging
- 当前版本适合直接重新打包并作为 Mira 可发布 skill 包使用。

## [v1.2.0] - 2026-04-14

### Added (Block API Beautification)
- Added Block API beautification proposal and canonical spec under `references/core/*`.
- Added `Stage C+` beautification pointer (Enhanced Layer post-processing) in `references/core/runbook.md`.
- Added Block API tooling quick reference + pitfalls in `references/core/tooling.md`.
- Added empty placeholder cleanup via Block API `batch_delete` (containers/table cells/doc root), enabled by default in `scripts/beautify_report.py` with `--no-cleanup-empty` escape hatch.
