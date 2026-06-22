# Changelog

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
