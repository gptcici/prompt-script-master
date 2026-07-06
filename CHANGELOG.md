# Changelog
## V0.9.74 - 2026-07-07

- Added `人物镜头强制覆盖规则` as the single top-level rule for character shots.
- Unified character action, expression/body linkage, mouth/lip-sync, close-up face lighting, dynamic wardrobe/accessory/environment motion, and reference identity locking under one trigger-based rule.
- Rewrote top-level timeline, wind, and OpenAI image-family prompt rules to reference the new character-shot rule instead of maintaining scattered mandatory clauses.
- Clarified that reference fidelity, character continuity, expression-motion, close-up face lighting, and wind/soft-body files are implementation sub-rules, not competing top-level rules.
- Updated checker, wizard, templates, output docs, quality gates, README, and version metadata for V0.9.74.

## V0.9.73 - 2026-07-04

- Added `references/seedance-wind-softbody-standard.md` for wind and soft-body dynamics.
- Upgraded global motion wording to `全局风向 / 柔体动力学锚点`.
- Standardized wind prompts around one physical wind field, subject/prop/environment response layers, material speed differences, delay, rebound, and gravity.
- Updated video template, Seedance concise standard, quality-control, timeline rules, README, docs, prompt checker, and prompt wizard.
- Fixed prompt checker / wizard Python syntax and added wind-dynamics checks.

## V0.9.72 - 2026-07-04

- Set final Seedance/video prompt standard to medium-length concise execution with strong anchors and shot-based timelines.
- Updated final output template to `【正文提示词】` + `【负面提示词】`.
- Deprecated the old three-block final video template and removed conflicting 9-field mandatory final-format wording.
- Added / aligned `references/seedance2-concise-execution-standard.md`.
- Updated timeline, quality-control, output-format docs, prompt checker, and prompt wizard.


## v0.9.6-no-assets-install - 2026-07-03

### Removed

- Removed bundled bundled media payload from the install package.
- Removed internal asset-library guide and image-reference index files that pointed to bundled media.
- Rewrote composition guidance as a text-only pattern library with no local media dependency.

### Changed

- Preserved user-upload reference handling while removing references to bundled local media folders.
- Updated SKILL.md and README so the install package no longer expects internal reference images or videos.

## v0.9.5-cross-reference - 2026-07-03

### Removed

- 删除 3 个冗余库文件：`action-library.md`、`music-editing-rhythm-library.md`、`mv-story-structure-library.md`
- 清除所有文档中的孤儿引用

### Changed

- 15 个库文件全部补齐 `## Related` 交叉规则引用段，实现规则↔库双向索引
- 6 个光影文件建立互相引用关系
- 统一快照目录（`skill/prompt-script-master/`）同步，补齐缺失的 docs/ scripts/ 文件
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
