# Seedance Depth and Space Rules

## Core idea

Seedance responds better to visible depth effects than bare camera parameters. Convert `f/1.8`, `50mm`, or `大光圈` into visual instructions.

## Placement

Depth and lens cues belong in the opening high-weight shot/view area.

## Useful phrasing

- Background heavily blurred into soft bokeh color blocks.
- Subject face and edges remain sharp and stable.
- Foreground leaves/rain/silk are slightly blurred.
- Middle-ground subject is crisp; far background melts into soft color.
- Three-layer depth: foreground blur, sharp middle-ground subject, softened far background.

## Conflict repair

Do not combine heavy background blur with clear readable background crowds, signs, or detailed architecture. Choose one priority.

## 权重规则

深度关键词的权重遵循 S/A/B 三级分层体系（见 `seedance-prompt-order-rules.md` 权重规范标准化章节），属于 B 级环境类（1.05-1.1，尽量不用），不可高于人物类权重。

示例：`(背景重度虚化散景:1.1)`、`(主体边缘锐利:1.1)`、`(三层景深层次分明:1.1)`。上限 1.3（全局红线）。
