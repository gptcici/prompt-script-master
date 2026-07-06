# Timeline Execution Rules

## Core principle

Timeline content is still the execution body of a video prompt, but final Seedance prompts should use compact natural-language shot paragraphs instead of rigid field-by-field blocks unless the user asks for audit/debug formatting.

Authoritative final output standard: `references/seedance2-concise-execution-standard.md`.

## Multi-shot trigger

When the user asks for multiple angles, cuts, montage, inserts, close-ups, establishing shots, or any video over 5 seconds that is not explicitly single-shot, write a clear multi-shot timeline with time ranges.

Use 5-7 shots for a typical 15-second video. Each shot should be 2-4 compact sentences.

## Per-shot coverage

Each shot paragraph should naturally cover:

- shot size, camera position, movement, and focal behavior;
- visible subject action and body / face / hand / material linkage;
- when a shot contains a recognizable person, apply `人物镜头强制覆盖规则` to decide required action, expression/body linkage, mouth movement, face lighting, dynamic materials, and identity lock;
- light behavior, physical dynamics, depth, and background motion;
- for wind shots, visible response in the relevant layers: subject hair/costume, props/veils, and environment/clouds/mist;
- transition or purpose of this shot when useful.

These are coverage requirements, not mandatory field labels in final copy-ready prompts.

## First and later shots

- First shot: establish subject, space, visual style, and the strongest reference anchors.
- Later shots: focus on changes in camera, action, focus, light, wind, and spatial reveal. Avoid repeating the full character description in every shot.

## Quality signals

A good timeline lets the video model understand:

- where the camera is and how it moves;
- what the subject does and how expression / body / hand / fabric details move, using `人物镜头强制覆盖规则` for character shots;
- where the light comes from and how it affects the subject and environment;
- how wind, fabric, smoke, rain, snow, water, cloud, fire, particles, props, contact, collision, gravity, inertia, crowd, or other moving materials behave;
- how depth, foreground, midground, and background change;
- how one shot leads into the next.

## Not acceptable

- One long unbroken paragraph for complex multi-shot videos.
- A shot that only says a mood but no visible action.
- Lighting only described globally when shot-level light changes are important.
- Physical motion without source, path, material response, contact result, or final state.
- Strong dynamics described only as a mood label without hair, fabric, veil, leaf, cloud, mist, rain, smoke, water, prop, collision, contact, or dissipation response.
- Repeating the full reference description in every shot.


## Continuation note

For continuation, multi-clip MV, story-series, or first-frame / last-frame continuation tasks, read `sequence-state-capsule.md`. The current final prompt must describe only the current clip, must not repeat completed previous actions, and must not reveal events reserved for later clips.


## V0.9.76 execution layer

For complex cinematic, emotional, professional, or multi-character shots, each shot paragraph should also satisfy:

- one shot intention: what this shot changes for the audience;
- one primary action contract: subject, action, rhythm/force, visible consequence, and endpoint;
- character blocking when multiple people appear: hero subject, background micro-motion, and no unassigned large action;
- motivated lighting: source, direction, color temperature, shadow behavior, material reflection, and any justified transition;
- continuity handoff: start state and end state when the shot belongs to a sequence or multi-shot plan.

These are internal coverage rules, not mandatory labels in the final prompt. Keep final output natural and compact.


## V0.9.78 density and budget note

For complex shots, first decide the prompt budget: identity, motion, scene density, lighting, dynamics, sound, or reference transfer. A single shot should not demand all categories at maximum strength. Current clips should usually contain one visible beat and one changed endpoint. Empty evaluators must be rewritten into concrete camera, light, action, material, physical-dynamics, or sound decisions before final output.


## V0.9.79 camera-language execution addendum

Before writing each time segment, internally choose the shot contract: intention, subject priority, shot size, angle, movement, focus plan, start frame, end frame, and risk control. A time segment must not use camera movement as decoration. The shot size must fit the task: wide shots carry space and blocking, medium shots carry behavior, close-ups carry emotion/mouth/hand/product detail, and macro shots carry material proof.

For 10-15 second Seedance clips, prefer 2-4 shots by default. Use 2-3 shots when identity, lip-sync, hand detail, product text, or multiple references must stay stable. Use dense shot counts only when the user explicitly asks for storyboard or dense previsualization.

Each shot should contain one main camera movement at most. Do not stack push, pull, pan, orbit, handheld, and rack focus in one shot unless the user explicitly requests an experimental camera move.


## V0.9.80 模式与长度检查

最终生成前检查是否已判断 T2V / I2V / R2V / FLF2V / V2V / Edit / Extend / IMAGE；检查提示词长度是否匹配任务复杂度；检查 I2V 是否只写图片看不出来的动作、镜头、光线、动力学和保持约束。
