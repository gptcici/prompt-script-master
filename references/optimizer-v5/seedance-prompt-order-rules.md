# Seedance Prompt Order and Weight Rules

## Core rule

Seedance prompt weight decays from left to right. Put the strongest visual anchor first. Do not open a prompt with secondary effects such as atmosphere, bokeh, texture, or mood when a human character is the core subject.

## Golden order

Use this exact order for Seedance main prompts. Weight decays from left to right, so the opening sentence must lock the frame structure before any decorative detail.

```text
景别/镜头视角 + 核心运镜 + 核心景深属性 -> 人物主体 + 关键外形特征 -> 核心动作 + 表情肢体联动 -> 面光/骨骼光影 -> 场景环境光影 -> 场景环境细节 -> 景深空间细节补充 -> 全局一致性约束
```

## Module boundaries

### 1. 镜头基础属性

This is the S-level opening module. Write it in the first sentence.

Must include:

- 景别
- 拍摄视角
- 主运镜方式
- 核心虚实强度

Use short, direct phrasing:

```text
中近景，身后侧方视角，极慢匀速向前跟随推进，三层景深虚实分明。
```

Do not write concrete foreground or background objects here. Save them for the later depth-space detail module.

When a character reference exists, the character anchor must appear in the first high-weight sentence:

```text
中近景，身后侧方视角，极慢匀速向前跟随推进，三层景深虚实分明；上传人物造型图中的女性角色为画面核心，严格匹配她的脸型比例、五官气质、黑色长发、银色花形头饰、垂落珍珠链、暗红宝石点缀和黑白轻薄古风服装。
```

### 2. 人物主体 + 关键外形特征

Must include:

- 主体身份
- 3-5 个最核心外形特征
- 参考图匹配说明

Do not list more than 6 appearance anchors unless the user explicitly asks for strict costume inventory. Too many anchors dilute the character signal.

### 3. 核心动作 + 表情肢体联动

Write the large action first, then micro-expression and body linkage.

Must include:

- 核心动作轨迹
- 动作节奏
- 五官表情细节
- 头颈肩手或身体重心联动

For ordered multi-phase actions, split into a timeline.

### 4. 面光 / 骨骼光影

Must appear immediately after the character action and expression module.

Must include:

- 人物主光方向
- 骨骼明暗锚点
- 眼神光 when face is visible
- skin/hair/fabric detail when relevant

For medium close-up or closer shots, mention facial structure, such as nose bridge, cheekbone, jawline, eye socket, and hair rim light.

### 5. 场景环境光影

Must include:

- 环境主光源
- 整体色温
- 环境反光 or atmosphere light

The character light and environment light must share a coherent source and direction.

### 6. 场景环境细节

Must include only essential story-space elements:

- location
- core background elements
- weather or atmosphere when relevant

Do not overfill the background with props that compete with the character.

### 7. 景深空间细节补充

The core depth strength is already fixed in the opening module. This later module only assigns concrete objects to foreground/middle-ground/background:

```text
前景半透明纱帘轻微虚化，中景人物始终清晰锐利，远景水面与薄雾柔和散焦，前后景过渡自然。
```

### 8. 全局一致性约束

Write only positive visual constraints:

```text
全程运镜平稳顺滑，人物造型稳定一致，动作流畅连续，画面写实。
```

All negative constraints belong in the negative prompt field.

## Reference role language

Do not write vague phrases such as `强参考` alone. Specify exactly what the reference controls and what it does not control.

Use:

```text
人物面部、发型、头饰、珠链和服饰造型严格匹配上传人物参考图；参考图只用于锁定人物外形特征，不干预本镜头的构图、光影、动作和场景。
```

If the platform has reference-strength controls, recommend `人物参考强度 0.7-0.8` outside the copy-ready prompt, not inside the main prompt unless the user asks for parameter notes.

## Positive-only main prompt

The main prompt must not include negative wording or human-facing rules.

Move these to the negative prompt:

- 不要、不许、避免、防止、不能、不要改变、不要出现
- 反向 descriptions of failures

Rewrite these as positive instructions:

- `不要改变人物身份和整体气质` -> `严格保留人物清冷气质与造型特征`
- `不抢人物焦点` -> `人物始终为画面视觉核心`
- `不要动作过快` -> `动作缓慢连续`

Remove human-facing rule text from main prompts:

- `整个镜头只有一个主运镜`
- `贴合慢歌节奏`
- `遵循黄金语序`
- `符合 Seedance 规则`

Replace abstract rhythm with visible motion parameters:

```text
运镜匀速极慢，全程平稳无顿挫。
```

## Expression and face lighting granularity

For medium close-up or closer shots, replace abstract emotion labels with visible face and body details:

```text
眼睑平缓舒展，目光平静平视前方，眉峰自然无紧绷，唇瓣自然微张，面部肌肉放松，肩颈自然下沉，神情清冷克制。
```

Attach lighting to facial structure:

```text
清冷月光擦过她的侧脸，鼻梁带细碎高光，下颌线明暗交界柔和，暗部保留细腻层次，无死黑。
```

## Timeline splitting

If one prompt contains multiple ordered action phases, use a timeline even for a single continuous shot.

Examples of ordered phases:

- 推帘 -> 走出门 -> 显露室外空间
- 抬手 -> 触碰道具 -> 回头
- 起身 -> 转身 -> 离开画面

For 8-10 seconds, use three segments:

```text
0-3s 起始：建立人物与第一动作
3-7s 过渡：推进动作与空间变化
7-10s 落点：动作结果与情绪/空间揭示
```

Each segment must preserve the same character anchor and motion continuity without repeating the full identity description.

## Weight syntax

Use simple weights only for crucial details that need extra stability. Do not use complex nesting. Do not exceed 1.4.

Recommended Seedance weights:

- `(人物面部与头饰一致:1.3)`
- `(人物始终为画面视觉核心:1.2)`
- `(主体边缘锐利:1.2)`
- `(三层景深层次分明:1.2)`
- `(背景重度虚化散景:1.3)`
- `(前景纱帘轻微虚化:1.2)`
- `(运镜匀速极慢:1.2)`

Use 1-4 weighted phrases per prompt. Too many weights dilute the prompt.

## Output self-check

Before finalizing a Seedance prompt, verify:

1. Does the first sentence contain shot/view, main camera movement, and the character anchor?
2. Are reference roles explicit and limited?
3. Is the main prompt free of negative wording?
4. Are human-facing rule phrases removed?
5. Are expressions visible through eyes, brows, mouth, face muscles, head/neck/shoulder/body?
6. Does face lighting mention facial structure when the shot is medium close-up or closer?
7. Are ordered action phases split into a timeline?
8. Are negative terms placed only in the negative prompt field?
9. Are simple weights used for the most important stability points when useful?
