## V0.9.82 - 2026-07-07

### Added
- 新增 `references/reference-intake-self-check.md`，作为所有上传参考图后的统一自检入口。
- 新增参考图重生建议逻辑：当关键区域不清晰较多、主职责区域不可辨、首尾帧无法连接或人脸存在严重异常时，建议用户重新生成/上传更清晰的参考图。

### Changed
- `reference-visibility-gate.md` 从三档决策升级为四档决策：清晰可用、部分可用需补写、异常需重建、建议重新生成参考图。
- `reference-transfer-contract.md` 改为只把清晰可信的信息分配为职责；低清或异常参考图会降级为弱参考。
- `output-length-mode-standard.md` 强化：I2V 极简原则必须排在参考图上传后自检之后。
- `quality-control.md`、`retake-failure-diagnosis.md`、模板、文档和 `prompt_checker.py` 同步加入参考图重生建议与主职责可读性检查。

### Notes
- 本版本不改变最终视频双段结构；它只增强上传参考图后的自检、补写、排除异常和重生建议流程。

## V0.9.81 - 2026-07-07

### Added
- 新增 `references/reference-visibility-gate.md`，在 I2V / R2V / FLF2V / IMAGE 任务中先判断参考图人脸、服装、发型/发饰、背景/空间、构图/景别、首尾帧连接性是否清晰可识别。
- 新增 `references/face-integrity-check.md`，专门检查人脸畸形、五官错位、不协调色块、黑斑、异常阴影、大面积死黑、皮肤塑料/蜡像/橡胶质感、肤色断层和不符合生理逻辑的皮肤质感。

### Changed
- I2V 极简原则改为有条件执行：只有参考图关键视觉信息清晰时，才只写图片看不出来的动作、运镜、光线变化和动力学；不清晰部分必须补写，异常部分必须重建。
- `reference-transfer-contract.md` 在分配参考图职责前先执行可识别性检查，避免把模糊或异常信息当成职责继承。
- `quality-control.md`、`retake-failure-diagnosis.md`、`output-length-mode-standard.md`、`templates/video-prompt-template.md` 和 `prompt_checker.py` 同步加入参考图清晰度与人脸完整性检查。

### Notes
- 本版本不改变最终视频双段结构；它只决定参考图里哪些信息可省略、哪些必须补写、哪些异常不得继承。

# V0.9.80 - 输出长度档位与模式优先增强

- Added `references/output-length-mode-standard.md`.
- Added mode-first routing for T2V, I2V, R2V, FLF2V, V2V/Edit/Extend, and IMAGE tasks.
- Added output length tiers for compressed, quick video, standard video, high-control video, dense storyboard, and image prompts.
- Strengthened I2V principle: only describe what the image cannot show.
- Standardized complex dynamic negative category toward 动力学类 while keeping checker compatibility with 风力类.
- Fixed the older default 5-7 shot guidance by aligning 15-second video defaults with 2-4 shots, or 2-3 shots for lock-face/lip-sync/multi-character/complex dynamics tasks.

## V0.9.79 - 2026-07-07

### Added

- Added `camera-shot-contract.md` for shot intention, subject priority, shot size, angle, movement, focus, start frame, end frame, and risk control.
- Added `shot-scale-selection.md` for matching shot size to identity, emotion, action, space, product, material, or detail tasks.
- Added `camera-movement-selection.md` for choosing stable, push-in, pull-back, track, follow, orbit, crane, aerial, handheld, or rack-focus movement based on content fit.
- Added `multishot-grammar-standard.md` for controlling shot count, cut points, and per-shot information density in 5/8/10/15-second videos.
- Added `shot-continuity-axis-rules.md` for screen direction, eyeline, axis, entry/exit, light direction, physical direction, prop state, and start/end handoff continuity.
- Added `animation-camera-grammar.md` for 2D, anime, hand-drawn, comic, storyboard, and animation MV camera language.

### Changed

- Extended `SKILL.md` routing so camera-language, shot-size, camera movement, multishot, axis-continuity, and animation-camera requests load the appropriate reference files.
- Updated timeline, quality, template, and checker rules to evaluate whether camera decisions match content instead of only checking that camera words exist.

### Fixed

- Reduced risk of mismatched shot size, unstable movement for lip-sync/identity/product tasks, excessive shot count, screen-direction flips, and inappropriate live-action lens language in 2D/storyboard prompts.

# Changelog
## V0.9.78 - 2026-07-07

- Added `references/model-behavior-diagnosis.md` for model-behavior diagnosis: attention budget, negation-summoning, reference dominance, capacity limits, compounding drift, time-trajectory priors, and audio-video coupling.
- Added `references/prompt-budget-allocation.md` to decide whether a shot spends its budget on identity, motion, scene density, lighting, dynamics, sound, or reference transfer before writing the final prompt.
- Added `references/event-density-control.md` to keep each clip focused on one visible beat and one changed endpoint, with splitting triggers for overpacked actions, dialogue, locations, and future events.
- Added `references/anti-slop-rewrite-library.md` to convert empty evaluators and image-model tokens into observable camera, lighting, action, material, physical-dynamics, and sound language.
- Updated `SKILL.md`, README, quality gates, timeline rules, and prompt checker triggers for V0.9.78.

## V0.9.77 - 2026-07-07

- Added `references/physical-dynamics-standard.md` as the top-level physical dynamics rule for wind, soft-body, fluid, particle, prop, contact, collision, gravity, inertia, VFX dissipation, and light-medium interaction.
- Expanded the former wind / soft-body system so dynamic scenes require source, affected object, motion path, material response, visible result, and end / dissipation state.
- Updated Seedance concise execution, output template, docs, timeline rules, quality gates, motion contract, lighting contract, pro shot continuity, retake diagnosis, README, and prompt checker for V0.9.77.
- Kept `seedance-wind-softbody-standard.md` as the simplified wind / fabric / hair entry while making `physical-dynamics-standard.md` the broader authority for complex dynamics.

## V0.9.76 - 2026-07-07

### Added

- Added `directing-coherence-engine.md` for converting vague cinematic/emotional requests into one clear shot intention and aligned camera, light, performance, sound, and edit choices.
- Added `motion-performance-contract.md` for action subjects, force, timing, visible physical consequence, continuity, and endpoint.
- Added `character-blocking-contract.md` for multi-character blocking, three-tier action hierarchy, crowd/multi-person stability, and hand/face safety.
- Added `lighting-intention-contract.md` for motivated light sources, color temperature, shadow behavior, material reflection, atmosphere, and lighting transitions.
- Added `pro-shot-continuity-contract.md` for shot contracts, continuity ledgers, first/last-frame handoffs, and professional multi-shot planning.
- Added `retake-iteration-protocol.md` for keep/fix-in-post/local-edit/reroll/rewrite decisions and one-variable retake control.

### Changed

- Extended `SKILL.md` routing so director, motion, character-blocking, lighting, professional shot continuity, and retake-iteration requests load the new fused references.
- Strengthened timeline and quality-control expectations around shot intention, action endpoints, lighting motivation, multi-character action tiers, and retake strategy.
- Updated `prompt_checker.py` to warn when strong action, multi-character, lighting, director-intent, professional shot, or retake-iteration tasks lack the corresponding control anchors.

### Notes

- V0.9.76 keeps prompt-script-master as the base: Chinese confirmation workflow, character-shot mandatory coverage, V0.9.75 sequence/reference/retake rules, and final `【正文提示词】 + 【负面提示词】` format remain authoritative.


## V0.9.75 - 2026-07-07

### Added

- Added `sequence-state-capsule.md` for continuation, multi-clip MV, sequence video, first-frame / last-frame continuation, and story-series state tracking.
- Added `reference-transfer-contract.md` for assigning each reference image a clear transfer role and ignore scope.
- Added `retake-failure-diagnosis.md` for retake, failure analysis, prompt audit, continuity repair, reference pollution diagnosis, and generated-result repair.

### Changed

- Extended `SKILL.md` branch routing so sequence projects trigger state capsules, multi-reference tasks trigger reference transfer contracts, and retake/audit requests trigger failure diagnosis.
- Clarified that the new V0.9.75 rules are enhancement layers and do not replace V0.9.74 character-shot coverage, wind / soft-body dynamics, or final prompt output structure.

### Fixed

- Reduced risk of repeated actions across continuation clips.
- Reduced risk of future events leaking into the current clip.
- Reduced risk of multi-reference image pollution.
- Improved diagnosis paths for face drift, costume drift, mouth failure, wind conflict, camera-axis errors, and continuity breaks.

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
