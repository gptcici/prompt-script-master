# Timeline Splitting Trigger (2026-07-03)

## Final Rule (Unified)

When expected video length > 5 seconds, or user specifies duration > X seconds, and user has NOT stated "一镜到底":

1. **Ask**: "视频时长预计超过 5 秒，是否需要分段?"
2. **Allocate**: No fixed durations. Assign time based on content weight.
3. **Self-check**: Verify action density matches allocation, total equals target, transitions flow.
4. **Confirm**: Present plan to user, proceed only after confirmation.

When user explicitly requests "一镜到底": skip asking, generate single continuous shot.

## Files Updated
- `references/timeline-execution-rules.md` — Added §分段触发条件
- `references/optimizer-v5/seedance-prompt-order-rules.md` — §Timeline splitting rewritten
- `references/optimizer-v5/seedance-camera-movement-transition-rules.md` — §时间轴适配 rewritten
- `references/optimizer-v5/seedance-prompt-order-rules.md` — Self-check item 7 updated

## Removed
All fixed-duration splits: `0-3s/3-7s/7-10s`, `0-2s/2-5s`, "只写两段", "只写三段"
