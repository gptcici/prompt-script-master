# Seedance 2.0 Concise Execution Standard

## Status
Version: V0.9.80

This is the default final-output standard for all Seedance 2.0 / 2.1 video prompts and any video prompt that may be sent to a model with limited prompt-following bandwidth.

## Core principle
Use **medium-length prompts with strong anchors**. Do not use extreme short prompts that lose control, and do not use long director notes that dilute model attention.

Recommended length is selected by `references/output-length-mode-standard.md`:
- Compressed: about 80-180 Chinese characters.
- Quick video: about 120-260 Chinese characters, usually 1 core shot, at most 2 shots.
- Standard 8-15 second video: about 500-1000 Chinese characters, usually 2-3 shots.
- High-control video: about 1000-1600 Chinese characters, usually 2-4 shots.
- Dense storyboard / shot list / production treatment: only when explicitly requested by the user.
- Negative prompt: about 120-300 Chinese characters.

If the user explicitly asks for a highly detailed prompt, allow more detail, but avoid repeating the same instruction in multiple places.

## Required output structure
Always use this structure for final video prompts unless the user requests a platform-specific format:

```text
【正文提示词】
[positive, model-facing prompt only]

【负面提示词】
人物类：...
动作类：...
动力学类：...
场景类：...
风格类：...
```

If the target platform does not provide a separate negative prompt field, output the negative prompt as a separate optional section and tell the user to omit it from the main prompt field.

## Main prompt modules
Write the main prompt in this order:

1. **Total setup**: duration, aspect ratio, subject, scene, style, multi-shot or single-shot.
2. **Reference roles**: list each reference once and define exactly what it controls.
3. **Global light anchor**: one physical light model with direction, color, rim light, dark-side detail, and weak bounce.
4. **Global physical dynamics anchor**: one physical dynamics model. For simple wind scenes, specify wind direction, force, continuity, subject / prop / environment responses, material speed differences, delay, rebound, and gravity. For complex scenes, also specify fluid / particle / object / contact / collision / gravity / inertia / VFX dissipation and light-medium interaction.
5. **Physical dynamics coverage**: when visible motion includes wind, soft body, fluid, particle, smoke, rain, snow, fire, water, props, contact, collision, gravity, or inertia, apply `references/physical-dynamics-standard.md`; simple wind / fabric scenes may use `references/seedance-wind-softbody-standard.md`.
6. **Character-shot mandatory coverage**: when a shot contains a recognizable person, apply `人物镜头强制覆盖规则` to decide whether action, expression/body linkage, mouth movement, close-up face lighting, dynamic wardrobe/accessory/environment motion, and reference identity lock are required.
7. **Shot timeline**: choose shot count according to `output-length-mode-standard.md`; 15-second videos normally use 2-4 shots, or 2-3 shots for lock-face, lip-sync, multi-character, or complex dynamics tasks.
8. **Global consistency**: one short final paragraph.

## Shot sentence pattern
Each shot should cover three things without overexplaining:

1. Camera: shot size, camera position, movement, focal behavior.
2. Action: visible subject action, body/expression/material movement.
3. Environment: light, wind, depth, background motion, or transition function.

Example:

```text
2-4秒，手部特写，低角度从古筝琴弦侧面缓慢横移。右手指尖拨弦，左手轻压琴弦，琴弦产生细微震动，袖口被风轻轻掀起。夕阳侧逆光在琴弦、指节、古筝木面和金色纹样上形成细小高光，背景纱幔柔化虚化。
```

## Physical dynamics anchor
When the scene contains hair, fabric, ribbons, veils, curtains, leaves, clouds, fog, smoke, water, rain, snow, fire, particles, props, collisions, contact, liquid, gravity, inertia, or any visible physical effect, include a compact physical dynamics module after the light anchor. Use `references/physical-dynamics-standard.md` as the top rule source; use `references/seedance-wind-softbody-standard.md` for simple wind / fabric scenes.

Preferred compact pattern:

```text
全局物理动力学锚点：主要动力来源为右前方山风与人物手部动作。山风持续吹向左后方，风向全程统一；发丝和细丝带响应最快，轻纱披帛与纱幔产生鼓起、拉伸、翻卷和回落，内层衣身与厚裙摆响应更慢。右手拨弦时琴弦先向内弯曲再回弹，袖口因动作惯性抬起后自然下坠；远处云海同向慢速流动，近景风动、手部接触、水面涟漪或烟雾消散都保持同一物理空间逻辑。
```

Keep wind wording positive and physical. Put failure terms such as `发丝不动`, `风向混乱`, `无重量感`, `像塑料片`, or `同速漂浮` only in the negative prompt.

## Character-shot mandatory coverage

When a shot contains a recognizable person, do not rely on identity, beauty, clothing, or mood alone. Apply `人物镜头强制覆盖规则`: character action and expression/body linkage are required; mouth movement is required for speaking/singing/lip-sync; face lighting is required for medium close-up or closer shots; dynamic hair, wardrobe, accessories, and environment materials require a unified wind or motion logic; face/reference identity must be locked when references exist. Do not force non-triggered modules into distant, back-view, silhouette, or non-speaking shots.

## Required anchors
Do not remove these control anchors:
- Reference image responsibilities.
- Character identity / costume locks when a character appears.
- Global light source anchor.
- Global physical dynamics anchor when fabric, hair, clouds, leaves, curtains, smoke, rain, snow, water, particles, props, contact, collision, gravity, inertia, or crowds move.
- Shot timeline with clear cut points.
- Key body, head, hand, and expression behavior for all character shots.
- Mouth movement with jaw stability, lip range, breath rhythm, and face/body continuity for speaking, singing, or lip-sync shots.
- Face lighting with main direction, bone-following light/shadow, catchlight, skin micro-detail, and weak environment bounce for medium close-up or closer character shots.
- Negative prompt categories.

## Compress or remove
Compress or remove:
- Repeated style adjectives.
- Repeated claims such as `真实电影感` in every shot.
- Long explanations of why a visual should happen.
- Multiple equivalent negative terms.
- Human-facing notes such as `我建议`, `注意`, `符合规则`.
- Overloaded shot descriptions with more than 4 sentences.

## Seedance practical notes
- Put the strongest visual anchors near the beginning.
- Use positive language in the main prompt.
- Keep negative wording in the negative prompt.
- Do not mix platform syntax from Midjourney, Stable Diffusion, ComfyUI, or Flux.
- For multi-shot videos, state it positively as `由多个镜头切换组成`.
- Keep one consistent light direction and one consistent wind direction unless the user asks for a change.
- For dynamic scenes, describe visible physical cause and result rather than vague `动感很强`: hair strand offset, fabric billow/rebound, veil curl, leaf shimmer, smoke drift/dissipation, rain direction, water ripples, prop contact, collision reaction, and final state.
- Natural-language shot paragraphs are preferred. Do not force table-like field labels into final prompts unless the user asks for audit/debug format.

## V0.9.76 director execution layer

For cinematic, emotional, professional, multi-character, or action-heavy prompts, apply this layer before writing the final timeline:

1. **Shot intention**: identify what the shot changes for the audience, such as reveal, decision, intimacy, pressure, material proof, or emotional turn.
2. **Motion contract**: important actions need a subject, concrete verb, rhythm/force, visible consequence, and endpoint.
3. **Character blocking**: two or more visible people require clear labels, hero subject, background micro-motion, and no unassigned large action.
4. **Lighting intention**: light needs a motivated source, direction, color temperature, shadow behavior, material reflection, atmosphere, and justified transition when it changes.
5. **Professional shot continuity**: multi-shot or commercial/MV prompts should keep shot purpose, reference roles, continuity anchors, start state, and end state clear.
6. **Retake iteration**: when repairing a failed generation, diagnose the failure and change one variable at a time.

This layer does not change the final output structure. It improves the content inside the existing `【正文提示词】 + 【负面提示词】` format.


## V0.9.80 输出长度与模式

最终视频提示词长度不再默认按固定 5-7 个镜头扩写，而是先读取 `output-length-mode-standard.md` 判断模式和长度档位。I2V / FLF2V 只写图片看不出来的动作、镜头、光线变化、动力学和保持约束；图片生成使用自然语言段落，不套视频时间轴。
