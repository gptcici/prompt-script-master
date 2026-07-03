# Changelog

## V0.9.6 - 2026-07-04

### Changed

- 版本号更新至 V0.9.6。

## v0.9.5-cross-reference - 2026-07-03

### Removed

- 删除 3 个冗余库文件：`action-library.md`、`music-editing-rhythm-library.md`、`mv-story-structure-library.md`
- 清除所有文档中的孤儿引用

### Changed

- 15 个库文件全部补齐 `## Related` 交叉规则引用段，实现规则↔库双向索引
- 6 个光影文件建立互相引用关系
- 统一快照目录（`skill/prompt-script-master/`）同步，补齐缺失的 assets/ docs/ scripts/ 文件
- 版本号更新至 v0.9.5

### Fixed

- `seedance-chinese-fantasy-lighting-library.md` 补注册至 SKILL.md 规则列表
- 修复 prompt-script-master 快照歧义导致 skill_view 加载失败问题（快照同步）

## v0.6.0-script-learning-library - 2026-06-22

### Added

- Introduced script learning library system for concert / MV / live-stage workflows.
- Added concert performance action library abstraction layer.
- Added MV story structure (5-act model + multi-space narrative system).
- Added music editing rhythm mapping system (beat-aware shot density).
- Added lighting-emotion mapping system (emotion-driven lighting presets).
- Added asset library system (images / videos / keyframes / breakdowns).

### Changed

- Upgraded README version section to v0.6.0-script-learning-library.
- Strengthened reference isolation rules across all generation pipelines.
- Improved Skill description alignment with internal reference architecture.

### Notes

- All reference materials are strictly abstracted and MUST NOT appear in generated outputs.
- This version formalizes the separation between "reference learning" and "prompt generation" layers.

## v0.5.0-state-machine - 2026-06-22

### Changed

- Upgraded core Skill to industrial fail-closed state machine architecture.
- Introduced CONFIRMATION_MODE vs DIRECT_MODE routing system.
- Added strict gating rules preventing premature final prompt generation.
- Strengthened reference-stage and workflow enforcement logic.
- Added explicit state tokens (S1–S9) execution model.

### Notes

- This version represents a structural upgrade from guidance-based workflow to enforced state-machine behavior.
