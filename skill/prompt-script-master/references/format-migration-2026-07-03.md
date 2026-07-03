# Multi-Shot Format Correction (2026-07-03)

## What Was Wrong

The old multi-shot format used separate `【分镜 1】/【分镜 2】` blocks with independent `【摄影参数】` and `【灯光、场景与动态】` sections. This was discovered to be completely incorrect.

## Corrected Format

Single-shot and multi-shot use the **same unified three-section structure**. The only difference is the number of timeline segments:

```
【全程总定调】
视频基础规格 + 镜头总基调
参考图角色精准锁定
人物核心外形特...[truncated]