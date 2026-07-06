# Seedance 2.0 Concise Execution Standard

## Status
Version: V0.9.74

This is the default final-output standard for all Seedance 2.0 / 2.1 video prompts and any video prompt that may be sent to a model with limited prompt-following bandwidth.

## Core principle
Use **medium-length prompts with strong anchors**. Do not use extreme short prompts that lose control, and do not use long director notes that dilute model attention.

Recommended target for 15-second multi-shot videos:
- Main prompt: about 1200-1800 Chinese characters.
- Negative prompt: about 120-300 Chinese characters.
- Shot count: normally 5-7 shots.
- Each shot: 2-4 compact sentences.

If the user explicitly asks for a highly detailed prompt, allow more detail, but avoid repeating the same instruction in multiple places.

## Required output structure
Always use this structure for final video prompts unless the user requests a platform-specific format:

```text
【正文提示词】
[positive, model-facing prompt only]

【负面提示词】
人物类：...
动作类：...
风力类：...
场景类：...
风格类：...
```

If the target platform does not provide a separate negative prompt field, output the negative prompt as a separate optional section and tell the user to omit it from the main prompt field.

## Main prompt modules
Write the main prompt in this order:

1. **Total setup**: duration, aspect ratio, subject, scene, style, multi-shot or single-shot.
2. **Reference roles**: list each reference once and define exactly what it controls.
3. **Global light anchor**: one physical light model with direction, color, rim light, dark-side detail, and weak bounce.
4. **Global wind / soft-body dynamics anchor**: one physical wind field; specify direction, force, continuity, subject / prop / environment responses, material speed differences, delay, rebound, and gravity.
5. **Character-shot mandatory coverage**: when a shot contains a recognizable person, apply `人物镜头强制覆盖规则` to decide whether action, expression/body linkage, mouth movement, close-up face lighting, dynamic wardrobe/accessory/environment motion, and reference identity lock are required.
6. **Shot timeline**: 5-7 shots, each 2-4 compact sentences with time ranges.
7. **Global consistency**: one short final paragraph.

## Shot sentence pattern
Each shot should cover three things without overexplaining:

1. Camera: shot size, camera position, movement, focal behavior.
2. Action: visible subject action, body/expression/material movement.
3. Environment: light, wind, depth, background motion, or transition function.

Example:

```text
2-4秒，手部特写，低角度从古筝琴弦侧面缓慢横移。右手指尖拨弦，左手轻压琴弦，琴弦产生细微震动，袖口被风轻轻掀起。夕阳侧逆光在琴弦、指节、古筝木面和金色纹样上形成细小高光，背景纱幔柔化虚化。
```

## Wind / soft-body dynamics anchor
When the scene contains hair, fabric, ribbons, veils, curtains, leaves, clouds, fog, smoke, water, or any visible wind effect, include a compact wind module after the light anchor. Use `references/seedance-wind-softbody-standard.md` as the detailed rule source.

Preferred compact pattern:

```text
全局风向 / 柔体动力学锚点：中等偏强山风从画面右前方持续吹向左后方，风向全程统一。发丝和细丝带响应最快，轻纱披帛与纱幔产生鼓起、拉伸、翻卷和回落，内层衣身与厚裙摆响应更慢，只在边缘小幅摆动。发丝分束偏移，根部稳定、发尾轻盈延迟；布料具有真实重量、惯性、回弹和重力下坠。远处云海沿同一风向缓慢横向流动，与近景风动保持统一空间逻辑。
```

Keep wind wording positive and physical. Put failure terms such as `发丝不动`, `风向混乱`, `无重量感`, `像塑料片`, or `同速漂浮` only in the negative prompt.

## Character-shot mandatory coverage

When a shot contains a recognizable person, do not rely on identity, beauty, clothing, or mood alone. Apply `人物镜头强制覆盖规则`: character action and expression/body linkage are required; mouth movement is required for speaking/singing/lip-sync; face lighting is required for medium close-up or closer shots; dynamic hair, wardrobe, accessories, and environment materials require a unified wind or motion logic; face/reference identity must be locked when references exist. Do not force non-triggered modules into distant, back-view, silhouette, or non-speaking shots.

## Required anchors
Do not remove these control anchors:
- Reference image responsibilities.
- Character identity / costume locks when a character appears.
- Global light source anchor.
- Global wind / soft-body dynamics anchor when fabric, hair, clouds, leaves, curtains, smoke, water, or crowds move.
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
- For wind scenes, describe visible material response rather than vague `风很大`: hair strand offset, fabric billow/rebound, veil curl, leaf shimmer, mist drift, and cloud flow.
- Natural-language shot paragraphs are preferred. Do not force table-like field labels into final prompts unless the user asks for audit/debug format.
