# Seedance Wind and Soft-Body Dynamics Standard

## Status
Version: V0.9.77

本文件保留为“风 / 柔体”专项入口。复杂动态请同时读取 `physical-dynamics-standard.md`。如果场景只有风、头发、衣物、披帛、纱幔、竹叶、云雾、水面等柔体或流体，本文件足够；如果涉及雨雪、烟火、粒子、道具接触、碰撞、重力、惯性、液体、VFX 消散，则以 `physical-dynamics-standard.md` 为上位标准。

## Core principle

Treat wind as a **physical field**, not an atmosphere label. First define one global wind direction and force, then describe how the subject, props, and environment respond with different mass, delay, speed, contact, rebound, and gravity.

## Positive main-prompt module

Use a compact module like this when wind is the main dynamic source:

```text
全局风向 / 柔体动力学锚点：中等偏强山风从画面右前方持续吹向左后方，风向全程统一，基础风稳定存在，间歇性风脉冲增强动态。风的作用在人物发丝、披帛、袖口、裙摆、珠链、亭内纱幔、竹叶和远处云雾中持续可见；发丝和细丝带响应最快，轻纱披帛与纱幔产生较大幅度鼓起、拉伸、翻卷和回落，内层衣身与厚裙摆响应更慢，只在边缘小幅摆动。发丝分束向风向偏移，根部稳定、发尾轻盈延迟；布料具有真实重量、拉扯、惯性和重力下坠，不同材质形成快慢节奏差。远处云海沿同一风向缓慢横向流动，山峰周围雾气贴着岩壁上升、分流和回卷，与近景风动保持统一空间逻辑。
```

When the shot also includes rain, smoke, water, particles, objects, collisions, or contact, upgrade the module name to `全局物理动力学锚点` and include source, path, material response, contact result, and end state.

## Layer order

1. **Global field**: wind force, direction, continuity, and pulse pattern.
2. **Subject response**: hair, costume, body balance, accessories.
3. **Prop / set response**: veils, curtains, banners, ribbons, flags, hanging objects.
4. **Environment response**: leaves, grass, cloud sea, mist, smoke, rain lines, water ripples.
5. **Physical realism**: mass, delay, rebound, gravity, speed differences, contact reaction.

## Material response rules

- Hair: root remains anchored; hair ends and stray strands respond more strongly. Use `分束摆动`, `发尾延迟`, `耳后碎发`, `颈侧细发` when visible.
- Light fabric: chiffon, gauze, silk ribbons, veils, and sleeves respond fast and visibly; they can billow, stretch, fold, and rebound.
- Heavy fabric: inner robes, waist cloth, thick skirt layers, and garment bodies move more slowly and with smaller amplitude.
- Accessories: tassels, pearl chains, hair ornaments, and pendants move in small arcs with rhythmic delay; do not let them whip violently unless the scene calls for storm wind.
- Curtains / veils: show `鼓起 -> 拉伸 -> 翻卷 -> 回落`; allow edge flutter and column wrap when physically plausible.
- Leaves / bamboo: create same-direction evidence of wind. Near leaves move more visibly; distant leaves create fine layered shimmer.
- Clouds / mist / smoke: move slower than foreground fabric. Use lateral drift, orographic lift, split flow, leeward curl, upward heat flow, and gradual edge dissipation when relevant.
- Rain / snow: keep direction and density consistent. Let wind angle rain lines, while wet surfaces, puddles, fabric edges, and hair respond to contact.
- Water: use local contact points. Footsteps, rain, sleeves, or dropped objects create ripples; do not make the whole surface move without cause.

## Writing rules

- Use positive physical targets in the main prompt.
- Do not write failure descriptions in the main prompt.
- Avoid vague claims such as `风感很强` unless paired with visible effects.
- Avoid `不规则乱甩`; prefer `相位不同的自然摆动` or `末端更快、根部更稳`.
- Do not add leaves, dust, petals, or debris by default. Add them only when the scene already supports them.
- Keep one wind direction unless the user explicitly asks for a storm, vortex, magical airflow, explosion, or changing weather system.
- If wind causes another phenomenon, name the chain: wind bends candle flame, candle light flickers on the face, smoke line curls toward the door.

## Negative prompt category

When wind or soft-body behavior is important, include compact failure terms such as:

```text
风力类：风向混乱、头发衣服朝不同方向飘、发丝完全不动、头发整块僵硬平移、布料无重量感、披帛像塑料片、纱幔无规律乱飞、所有物体同速漂浮、云层运动方向和近景风向冲突、雨线与风向冲突、水面无接触点乱波动、烟雾无来源无消散
```
