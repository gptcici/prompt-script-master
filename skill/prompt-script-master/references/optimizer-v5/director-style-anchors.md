# Director Style Anchor System

Use this reference when the user provides vague style language such as `电影感`, `复古风`, `高级感`, `氛围感`, `导演风格`, `某某式`, or any named visual style. The goal is to prevent empty style words by pairing one strong anchor with concrete visual features.

This system supports OpenAI image-family natural-language prompts only. It does not switch the output to Seedance, Midjourney, SDXL, ComfyUI, Flux, or tag-soup syntax.

## Core rule

Every style direction must become:

```text
one style anchor + 3 to 5 concrete visual features
```

The anchor gives the model a direction. The concrete features keep the result from drifting.

## Anchor priority

Use a strong recognizable anchor only when it helps the user's request. Prefer anchors with a clear visual footprint:

- director / cinematography shorthand: Wong Kar-wai-like Hong Kong neon melodrama, Nolan-like large-format realism, Villeneuve-like restrained monumental sci-fi, Wes Anderson-like centered pastel symmetry
- classic visual genre or IP-like shorthand: Ghibli-like hand-painted warmth, Blade Runner-like rain-soaked cyberpunk, Shinkai-like luminous Japanese healing atmosphere
- professional medium: 35mm film still, IMAX large-format theatrical frame, CCD retro camera capture, hand-painted watercolor texture

When the user does not ask for a named style, prefer non-name anchors such as `rain-soaked Hong Kong neon film still`, `restrained large-format sci-fi realism`, `centered pastel deadpan composition`, or `35mm film night street photography`.

Do not stack multiple competing anchors. Use one primary style anchor, then add small secondary traits only as concrete features.

## Concrete feature checklist

After the anchor, add 3 to 5 visual features from these categories:

- color palette: warm red-yellow neon, cyan-blue cold tone, low-saturation Morandi palette, muted earth colors
- light behavior: side backlight, soft diffused window light, high-contrast chiaroscuro, practical neon reflections, mixed color temperature
- camera / composition: shallow depth of field, handheld realism, slow-shutter motion softness, centered symmetry, low camera height, foreground occlusion
- material / texture: 35mm film grain, matte surface, wet pavement reflection, soft halation, CCD noise, watercolor paper bleed
- motion intensity for video-oriented prompts: low, medium, or high movement energy matched to the style

Avoid empty style words unless they are grounded by these features.

## Prompt order and weight

For full prompts, place the style signal after the subject and action beat, before detailed scene and lighting:

```text
subject + action beat + style anchor + concrete color/light/camera/texture features + scene details + camera movement or framing + realism controls
```

This preserves subject/action priority while keeping the style visible early enough.

When the style is critical, repeat the core style idea once near the end using different but consistent words. Do not repeat it more than twice.

## Movement matching

Match movement energy to the style:

- slow / atmospheric / literary / classical / healing styles: low to medium movement, stable camera, slow dolly-in feeling, restrained handheld realism
- action / cyberpunk / stage / thriller styles: medium to high movement, tracking feeling, stronger contrast, directional light, sharper spatial rhythm

Overly violent movement can destroy lighting, texture, and style coherence. Keep motion physically plausible for a real camera.

## Positive wording

Do not write negative style controls in normal prompts. Translate them into positive targets:

- `不要模糊` -> `画面锐利清晰，主体焦点稳定`
- `不要卡通` -> `写实摄影质感，真实皮肤、真实材质和真实曝光`
- `不要跑偏` -> `风格锚点明确，色调、光影、镜头和质感保持一致`

## Length discipline

Keep a single prompt concise enough that the style signal is not diluted. A good prompt is usually 30 to 100 Chinese words for simple mode, or one compact paragraph for full production mode.

Remove generic filler such as `高级感`, `氛围感`, `质感好`, `大片感`, and `震撼`, unless each word is immediately backed by concrete color, light, camera, or material details.

## Examples

Weak:

```text
王家卫风格，雨夜小巷
```

Strong:

```text
雨夜的香港老巷，一名年轻女人撑伞回头，王家卫式港风电影质感，暖红色霓虹招牌在潮湿地面反光，35mm 胶片颗粒，浅景深虚化背景，轻微手持摄影感，复古港风胶片夜景。
```

Weak:

```text
高级科幻电影感，女孩站在飞船里
```

Strong:

```text
女孩站在真实搭建的飞船走廊中回头，克制的大画幅科幻电影质感，青蓝冷色主光与舱内实用灯混合，金属墙面有磨损和指纹，35mm 自然环境镜头，低机位中景，背景深处轻微雾化。
```
