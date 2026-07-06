# Seedance Wind and Soft-Body Dynamics Standard

## Status
Version: V0.9.74

Use this reference whenever a video prompt includes wind, hair, fabric, ribbons, veils, curtains, banners, leaves, clouds, fog, smoke, water, or any other soft or fluid material.

## Core principle
Treat wind as a **physical field**, not an atmosphere label. First define one global wind direction and force, then describe how the subject, props, and environment respond with different mass, delay, and speed.

## Positive main-prompt module
Use a compact module like this in the main prompt when wind is important:

```text
全局风向 / 柔体动力学锚点：中等偏强山风从画面右前方持续吹向左后方，风向全程统一，基础风稳定存在，间歇性风脉冲增强动态。风的作用在人物发丝、披帛、袖口、裙摆、珠链、亭内纱幔、竹叶和远处云雾中持续可见；发丝和细丝带响应最快，轻纱披帛与纱幔产生较大幅度鼓起、拉伸、翻卷和回落，内层衣身与厚裙摆响应更慢，只在边缘小幅摆动。发丝分束向风向偏移，根部稳定、发尾轻盈延迟；布料具有真实重量、拉扯、惯性和重力下坠，不同材质形成快慢节奏差。远处云海沿同一风向缓慢横向流动，山峰周围雾气贴着岩壁上升、分流和回卷，与近景风动保持统一空间逻辑。
```

Adapt the direction, force, objects, and environment to the current scene. Keep it concise; do not paste every possible object if the scene does not contain it.

## Layer order
When writing wind behavior, use this order:

1. **Global wind field**: force level, direction, continuity, and pulse pattern.
2. **Subject response**: hair, costume, body balance, accessories.
3. **Prop / set response**: veils, curtains, banners, ribbons, flags, hanging objects.
4. **Environment response**: leaves, grass, cloud sea, mist, smoke, water ripples.
5. **Physical realism**: mass, delay, rebound, gravity, speed differences.

## Material response rules
- Hair: root remains anchored; hair ends and stray strands respond more strongly. Use `分束摆动`, `发尾延迟`, `耳后碎发`, `颈侧细发` when visible.
- Light fabric: chiffon, gauze, silk ribbons, veils, and sleeves respond fast and visibly; they can billow, stretch, fold, and rebound.
- Heavy fabric: inner robes, waist cloth, thick skirt layers, and garment bodies move more slowly and with smaller amplitude.
- Accessories: tassels, pearl chains, hair ornaments, and pendants move in small arcs with rhythmic delay; do not let them whip violently unless the scene calls for storm wind.
- Curtains / veils: show `鼓起 -> 拉伸 -> 翻卷 -> 回落`; allow edge flutter and column wrap when physically plausible.
- Leaves / bamboo: create same-direction evidence of wind. Near leaves move more visibly; distant leaves create fine layered shimmer.
- Clouds / mist: move slower than foreground fabric. Use lateral drift, orographic lift, split flow, and leeward curl around mountains.

## Writing rules
- Use positive physical targets in the main prompt.
- Do not write failure descriptions in the main prompt.
- Avoid vague claims such as `风感很强` unless paired with visible effects.
- Avoid `不规则乱甩`; prefer `相位不同的自然摆动` or `末端更快、根部更稳`.
- Do not add leaves, dust, petals, or debris by default. Add them only when the scene already supports them.
- Keep one wind direction unless the user explicitly asks for a storm, vortex, or magical airflow.

## Negative prompt category
When wind is important, include `风力类` in the negative prompt. Use compact failure terms such as:

```text
风力类：风向混乱、头发衣服朝不同方向飘、发丝完全不动、头发整块僵硬平移、布料无重量感、披帛像塑料片、纱幔无规律乱飞、所有物体同速漂浮、云层运动方向和近景风向冲突
```
