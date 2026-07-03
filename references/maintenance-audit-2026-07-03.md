# Maintenance Checklist - Full Audit Results

When changing the timeline format (9-item structure), the following files were found to have stale content beyond the original 6-file checklist during the 2026-07-03 audit:

## Files Caught by Original Checklist (6)
1. `references/timeline-execution-rules.md`
2. `references/timeline-quality-gates.md`  
3. `SKILL.md`
4. `README.md`
5. `docs/golden-tests.md`
6. `scripts/prompt_checker.py`

## Files Found Stale During Full Audit (+3)
7. `references/video-rules.md` — Line 16-25 contained old "衔接关系+主体动作+场景动态" format
8. `references/quality-control.md` — Entire file used "11 项检查" and referenced old fields (焦段, 摄影机视角, etc.)
9. `references/templates.md` — Line 16-17 and 32 contained old concatenated format

## Verification Command
After any timeline format change, run a full-warehouse grep:
```bash
rg "衔接关系|焦段|摄影机视角|每个时间段必须写出|摄影机、焦段、景别或焦点" --glob '!.git' --glob '!*.bak'
```

## Snapshot Sync
All changes must be mirrored to `skill/prompt-script-master/` subdirectory to prevent snapshot drift.
