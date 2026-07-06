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
- light behavior, wind or material dynamics, depth, and background motion;
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
- how wind, fabric, smoke, water, cloud, crowd, or other moving materials behave;
- how depth, foreground, midground, and background change;
- how one shot leads into the next.

## Not acceptable

- One long unbroken paragraph for complex multi-shot videos.
- A shot that only says a mood but no visible action.
- Lighting only described globally when shot-level light changes are important.
- Wind or fabric motion without a single consistent direction.
- Strong wind described only as a mood label without hair, fabric, veil, leaf, cloud, mist, or water response.
- Repeating the full reference description in every shot.
