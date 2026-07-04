# Changelog

## V0.9.71 - 2026-07-05

### Added

- **锚点光源规则**（`references/anchor-light-source-rule.md`）：强制每条提示词确立唯一锚点光源（类型+方向+位置三要素），所有面光/环境光/阴影/轮廓光必须从该锚点推导，含 5 种违规判定、S8 质检沟通模板、五维物理校验（方向🔴/强度🟡/色温🟡/空间穿透🟡/夸张上限🟡）、AI 夸张尺度红线（高光 1.5 倍 / 对比 20-30% 可接受，禁止光穿透不透明体/面部凭空发光/割裂线/逆光全亮/反射超主光源）
- **技能自检流程**（`references/self-audit-procedure.md`）：标准化的旧规则残留检测、规则间冲突审计、库素材引用完整性验证流程
- **格式迁移记录**（`references/format-migration-v0.10-2026-07-04.md`）：v0.9.6→v0.10 输出结构变更的完整对照

### Changed

- **面光规则全面重写**：`seedance-closeup-face-lighting-rules.md` 从英文四层公式替换为完整的 166 行中文双模块规范（一致性锚定+四步校验+分机位点位库+6 场景模板+7 条禁写条款+负面词补丁），新增示例隔离⚠️声明
- **权重章节升级**：`seedance-prompt-order-rules.md` 权重章节从遗留英文规则替换为中文 S/A/B 三级分层体系（S:1.15-1.25 / A:1.1-1.15 / B:1.05-1.1），硬上限 1.3，含频率限制和 5 项禁止做法
- **光影描述统一**：SKILL.md、quality-control.md、timeline-quality-gates.md、output-templates.md、docs/seedance2-full-reference.md 全部从旧版"主光方向+轮廓光+面部明暗"更新为"锚点光源推导：光源方向→骨骼高光点位→暗部过渡→整体质感"四段式新格式
- **权重冲突修复**：`seedance-depth-space-rules.md` 上限 1.4→1.3，`timeline-execution-rules.md` 权重引 S/A/B 体系
- **质检体系强化**：quality-control.md 和 timeline-quality-gates.md 新增"锚点光源缺失"为一票否决/不通过首项
- **SKILL.md 完善**：扩展参考库隔离最高规则覆盖范围，更新维护注意事项（新增#17 锚点规则联动项），权重标记规则替换为完整 S/A/B 体系描述
- **脚本更新**：`prompt_checker.py` FACE_LIGHT_HINTS 从 8 个扩展至 18 个（含锚点光源/骨骼/面部点位关键词）
- **关联引用补全**：`seedance-real-lighting-rules.md` Related 段追加 `anchor-light-source-rule.md`，`quality-control.md` 断链 `final-prompt-purity.md`→`reference-isolation-rules.md`

### Fixed

- 全部示例和模板加入 ⚠️ 格式参考禁止照搬声明（6 处，三层防护：SKILL.md 全局规则→各文件头声明→每个模板/示例前警告）
- 3 个文件权重冲突：1.4→1.3 红线统一，"最高≤1.2"→S/A/B 分层引用
- 1 个文件引用不存在：`final-prompt-purity.md`→`reference-isolation-rules.md`
- 6 个文件光影描述旧版格式残留全部更新

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
