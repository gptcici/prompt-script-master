# Timeline Quality Gates

## Goal

Check whether final video prompts are compact, executable, and aligned with `seedance2-concise-execution-standard.md`.

## Required checks

A final video prompt should contain:

1. `【正文提示词】` and `【负面提示词】` sections.
2. A total setup with duration, aspect ratio, subject, scene, style, and multi-shot/single-shot intent.
3. Reference roles when reference images are used.
4. One global physical light anchor: direction, color, rim/highlight logic, dark-side detail, weak bounce.
5. One global physical dynamics anchor when hair, fabric, leaves, clouds, curtains, smoke, rain, snow, fire, water, particles, props, contact, collision, gravity, inertia, or crowds move.
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
- Physical dynamics direction/path changes accidentally.
- Reference images are used without stating what each reference controls.
- A character shot only describes beauty, clothing, or mood but lacks visible action.
- A medium close-up or close-up character shot lacks face lighting / bone-light structure.
- A singing, speaking, or lip-sync shot lacks mouth movement, jaw stability, lip range, or breath rhythm.

## Pass standard

The result should be readable, copy-ready, compact enough for model attention, and specific enough to control subject, references, light, wind/motion, shot order, and consistency.


## Continuation note

For continuation, multi-clip MV, story-series, or first-frame / last-frame continuation tasks, read `sequence-state-capsule.md`. The current final prompt must describe only the current clip, must not repeat completed previous actions, and must not reveal events reserved for later clips.


## V0.9.76 failure signals

- Shot only says `电影感 / 氛围感 / 高级感` but has no single intention.
- Important action has no visible physical consequence or endpoint.
- Multi-character shot lets all people perform large actions at the same time.
- Lighting has no motivated source, direction, or material/shadow behavior.
- Multi-shot / professional plan lacks continuity anchors or start/end handoff.
- Retake request changes face, action, light, wind, references, and camera all at once without isolating the failure.


## V0.9.78 density and budget note

For complex shots, first decide the prompt budget: identity, motion, scene density, lighting, dynamics, sound, or reference transfer. A single shot should not demand all categories at maximum strength. Current clips should usually contain one visible beat and one changed endpoint. Empty evaluators must be rewritten into concrete camera, light, action, material, physical-dynamics, or sound decisions before final output.


## V0.9.79 camera-language quality gates

- Every important shot has a fit between shot size and content priority.
- Close shots do not carry large locomotion or full-body dance unless clearly simplified.
- Wide shots do not demand subtle mouth, eye, or skin detail.
- Camera movement has a reason and a clear start/end frame.
- Stable identity, lip-sync, hand detail, product text, and precise first/last-frame alignment use stable or slow movement.
- Multishot plans preserve screen direction, eyeline, light direction, physical direction, and prop position.
- 2D/anime/storyboard prompts use animation layer and frame language rather than over-specific live-action lens equipment.


## V0.9.80 模式与长度检查

最终生成前检查是否已判断 T2V / I2V / R2V / FLF2V / V2V / Edit / Extend / IMAGE；检查提示词长度是否匹配任务复杂度；检查 I2V 是否只写图片看不出来的动作、镜头、光线、动力学和保持约束。
