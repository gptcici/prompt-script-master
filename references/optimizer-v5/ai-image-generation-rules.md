# AI Image Generation Rules for Photoreal AIMV / AI Short Drama

These rules support OpenAI image-family prompts for visuals that must look real. The skill is not a general commercial prompt optimizer and not a multi-model formatter.

## Core philosophy

The goal is a frame that feels photographed or filmed.

Prompt language should sound like instructions to a cinematographer, still photographer, production designer, costume designer, and VFX supervisor working on a real shoot.

## Positive-language rule

GPT-image responds best to desired visual targets. Convert negative wishes into positive goals.

| Weak / negative wording | Strong positive target |
|---|---|
| 不要AI感 | 像真实相机在现场拍到的一帧，有真实光源、真实材质、真实皮肤和自然曝光限制 |
| 不要塑料脸 | 皮肤保留自然纹理、轻微肤色变化、真实高光和环境光色偏 |
| 不要CG | 所有元素都像真实布景、道具、服装、灯光或可信VFX被相机拍到 |
| 不要过度锐化 | 柔和真实的镜头边缘、自然景深、克制细节和真实传感器/胶片颗粒感 |
| 不要海报感 | 像现场照片、剧照、纪录式抓拍或AIMV分镜帧，而不是完美设计海报 |

## Director style anchor rule

When the user gives vague style words or a named visual style, do not leave the style as an empty label. Compile it into:

```text
one strong style anchor + 3 to 5 concrete visual features
```

Use `references/director-style-anchors.md` as the style compiler.

Strong anchors may include director/cinematography shorthand, classic genre or IP-like aesthetics, and professional media such as 35mm film, IMAX large-format, CCD retro camera, or hand-painted watercolor. The anchor must be supported by concrete visual features:

- color palette: warm neon, cyan-blue cold tone, low-saturation Morandi palette
- light behavior: side backlight, soft diffused light, high-contrast chiaroscuro, practical reflections
- camera/composition: shallow depth of field, handheld realism, slow-shutter motion softness, centered symmetry
- texture: film grain, matte surface, wet pavement reflection, soft halation, CCD noise
- movement energy when useful: low, medium, or high movement matched to the style

Use only one primary style anchor. Do not stack conflicting anchors such as multiple director styles plus cyberpunk plus fantasy. If a secondary influence is needed, express it as 1 or 2 concrete visual traits instead of another named style.

If the style is important, place it after the subject and action beat, before detailed scene and lighting. Repeat the core style idea once near the end only when needed.

## Required realism controls

For people:
- natural skin texture and uneven tone under scene light
- real catchlights from visible or plausible light sources
- hair with weight, flyaways, and imperfect styling
- believable hands, posture, and body balance
- expression caught during an emotional/action beat
- wardrobe with real seams, folds, tension, stains, shine, transparency, or weight when relevant

For scenes:
- name the actual light sources
- keep reflections, shadows, scale, and contact points plausible
- let backgrounds be readable but not evenly sharp
- include small real-world imperfections when they fit the shot

For sci-fi/fantasy:
- translate ideas into physical production design, practical lighting, LED screens, projection, smoke, rain, pyrotechnics, prosthetics, props, sets, or believable composited VFX
- ensure the non-real element casts or receives real light and obeys camera exposure

## Banned default tendencies

Avoid these unless the user explicitly asks:
- AI art, concept art, illustration, game CG, render, poster design
- ultra-detailed, hyper-detailed, 8K, HDR, ultra sharp, masterpiece, best quality
- impossible perfect lighting, flawless skin, unreal symmetry, plastic material response
- named film/director/cinematographer style references unless the user asks for that exact style; when used, always pair the anchor with concrete visual traits
- empty style filler such as `高级感`, `氛围感`, `质感好`, `大片感`, or `电影感` without visible color, light, camera, composition, or material details

## Character-shot trigger

For any OpenAI image-family prompt containing a recognizable person, apply the top-level `人物镜头强制覆盖规则`: action and expression/body linkage are required; mouth movement is required for speaking/singing/lip-sync; face lighting is required for medium close-up or closer shots; dynamic hair/wardrobe/accessory/environment materials require unified physical motion; reference identity must be locked when references exist. Keep the final image prompt as natural-language paragraphs and do not add video timecodes unless the user asks for a keyframe sequence.

## Prompt structure

Use this order when writing a full prompt:

1. Reference priority and face lock, if references exist.
2. Real shot type: AIMV frame, AI short-drama production still, live-event photo, documentary shot, behind-the-scenes-like still, etc.
3. Subject and action beat.
4. Style anchor, if requested, plus 3 to 5 concrete visual features.
5. Emotional beat.
6. Wardrobe/props/set elements translated into real materials.
7. Real light sources and exposure behavior.
8. Camera position, lens feeling, shot size, composition, and aspect ratio.
9. Physical realism controls and anti-AI feel written positively.

## One-sentence realism anchor

Chinese:
```text
整体必须像真实相机在现场拍下的一帧，有真实光源、真实皮肤、真实材质、自然曝光限制和轻微现场不完美，而不是AI概念图、CG海报或过度美化的数字渲染。
```

English:
```text
The entire frame must feel like a real camera captured it on location, with real light sources, natural skin, physical materials, believable exposure limits, and subtle live-capture imperfections, not an AI concept image, CG poster, or over-polished digital render.
```

## Self-check

Before returning a prompt, verify:
- OpenAI image-family natural language only
- real camera viewpoint exists
- light sources are plausible
- vague style words are replaced by one anchor plus concrete visual features
- reference face is locked when provided
- all non-face references are filtered through realism
- physical materials and shadows make sense
- no tag soup or other-model syntax
