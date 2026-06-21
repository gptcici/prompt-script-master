# Changelog

## v0.3.2-timeline - 2026-06-22

### Updated

- Updated `prompt-script-master` Skill entrypoint with timeline-first Seedance 2.0 rules.
- Added stricter timeline execution requirements for transition relation, scene dynamics, lighting changes, camera movement, lens/focal length, shot size, focus, depth of field, and rhythm.
- Added timeline quality gates for checking whether each time segment is executable.
- Expanded prompt checking heuristics for timeline, camera, focus, lens, scene, lighting, and transition coverage.

## v0.3.0-skill-scaffold - 2026-06-22

### Added

- ChatGPT Skill scaffold under `skill/prompt-script-master/`.
- Skill entrypoint `SKILL.md`.
- Skill UI metadata `agents/openai.yaml`.
- Skill references for core workflow, video rules, quality control, examples, and templates.
- Internal Skill scripts for prompt generation, checking, and export.
- Repository-level Skill validation and packaging scripts.
- Installation instructions.

### Notes

- Examples refinement is intentionally paused.
- The Skill is now ready for local packaging and basic upload validation.

## v0.2.0-system-docs - 2026-06-22

### Added

- Core docs, examples, templates, scripts, and initial Skill scaffold.
- First maintainable GitHub version.

## v0.1.0-initial - 2026-06-21

### Added

- Initial README and project structure draft.
