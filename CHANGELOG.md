# Changelog

## v0.5.0-state-machine - 2026-06-22

### Changed

- Upgraded core Skill to industrial fail-closed state machine architecture.
- Introduced CONFIRMATION_MODE vs DIRECT_MODE routing system.
- Added strict gating rules preventing premature final prompt generation.
- Strengthened reference-stage and workflow enforcement logic.
- Added explicit state tokens (S1–S9) execution model.

### Notes

- This version represents a structural upgrade from guidance-based workflow to enforced state-machine behavior.
- All previous concert/live MV reference behavior is now integrated into core flow as optional rules.

## v0.4.6-concert-live-mv-reference

- Previous lightweight enhancement version.
