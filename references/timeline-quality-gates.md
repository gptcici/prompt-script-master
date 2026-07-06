# Timeline Quality Gates

## Goal

Check whether final video prompts are compact, executable, and aligned with `seedance2-concise-execution-standard.md`.

## Required checks

A final video prompt should contain:

1. `【正文提示词】` and `【负面提示词】` sections.
2. A total setup with duration, aspect ratio, subject, scene, style, and multi-shot/single-shot intent.
3. Reference roles when reference images are used.
4. One global physical light anchor: direction, color, rim/highlight logic, dark-side detail, weak bounce.
5. One global wind or motion anchor when hair, fabric, leaves, clouds, curtains, smoke, water, or crowds move.
6. A shot timeline with clear time ranges and cut points for multi-shot videos.
7. Each shot paragraph should include camera, action, and environment/light/motion information.
8. Character shots should pass `人物镜头强制覆盖规则`: visible action and expression/body linkage are present; mouth movement appears for speaking/singing/lip-sync; face lighting appears for medium close-up or closer shots; dynamic hair/wardrobe/accessory/environment materials use unified motion logic; reference identity is locked when references exist.
9. Global consistency constraints.
9. A compact categorized negative prompt.

## Failure signals

- Deprecated three-block final format is used.
- The main prompt mixes many negative instructions into positive text.
- Prompt is extremely short and lacks anchors.
- Prompt is very long and repeats the same instruction in many places.
- Multi-shot intent is present but time ranges or shot cuts are unclear.
- Light direction changes accidentally.
- Wind direction changes accidentally.
- Reference images are used without stating what each reference controls.
- A character shot only describes beauty, clothing, or mood but lacks visible action.
- A medium close-up or close-up character shot lacks face lighting / bone-light structure.
- A singing, speaking, or lip-sync shot lacks mouth movement, jaw stability, lip range, or breath rhythm.

## Pass standard

The result should be readable, copy-ready, compact enough for model attention, and specific enough to control subject, references, light, wind/motion, shot order, and consistency.
