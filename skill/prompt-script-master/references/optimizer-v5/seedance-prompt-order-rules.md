# Seedance Prompt Order and Weight Rules

## Core rule

Seedance prompt weight decays from left to right. Put the strongest visual anchor first. Do not open a prompt with secondary effects such as atmosphere, bokeh, texture, or mood when a human character is the core subject.

**Strongest mandatory format rule**: after the camera framework / shot framework is written, immediately lock the character and the character reference image. The character anchor must come before environment, atmosphere, scenery, decorative lighting, props, or mood description. When a human character is the subject, character priority is always higher than environment priority.

**Strong face-lighting rule**: whenever a prompt describes the character face in any way, it must include concrete face-lighting and bone-structure details. This is mandatory for close-up, medium close-up, half-body, visible-face side/back-three-quarter, singing, expression, eye-contact, blink, tear, rain-on-face, and any shot where eyes, brows, nose bridge, cheekbones, jawline, lips, or skin texture are mentioned. Select the face-lighting structure by combining the current scene, mood, character reference image, style, and relevant lighting libraries such as `seedance-closeup-face-lighting-rules.md`, `seedance-closeup-face-lighting-library.md`, `seedance-real-lighting-rules.md`, `seedance-lighting-scene-library.md`, `seedance-chinese-fantasy-lighting-library.md`, and `lighting-emotion-library.md`.

## Golden order

Use this exact order for Seedance main prompts. Weight decays from left to right, so the opening sentence must lock the frame structure before any decorative detail.

```text
景别/镜头视角 + 核心运镜 + 核心景深属性 -> 参考图人物强锁定 + 人物主体 + 关键外形特征 -> 核心动作 + 表情肢体联动 -> 面光/骨骼光影 -> 场景环境光影 -> 场景环境细节 -> 景深空间细节补充 -> 全局一致性约束
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

When a character reference exists, the character anchor must appear immediately after the camera framework in the first high-weight sentence. Do not insert environment, atmosphere, scene details, color grading, or mood between the camera framework and the reference-character lock:

```text
中近景，身后侧方视角，极慢匀速向前跟随推进，三层景深虚实分明；上传人物造型图中的女性角色为画面核心，严格匹配她的脸型比例、五官气质、黑色长发、银色花形头饰、垂落珍珠链、暗红宝石点缀和黑白轻薄古风服装。
```

### 2. 参考图人物强锁定 + 人物主体 + 关键外形特征

This module must directly follow the camera framework. It is the highest-priority content after shot framing. If a character reference image exists, lock it here before any environment description. Character visual anchors and character-related weights must outrank environment, weather, scenery, props, and atmosphere.

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

**Mandatory trigger**: any prompt that describes the character face must write concrete face-lighting and bone-structure details. Do not limit this rule to close-ups. Trigger it whenever the prompt mentions or shows eyes, brows, nose bridge, cheekbones, jawline, lips, facial expression, eye contact, blink, tears, rain on face, skin texture, side face, three-quarter face, singing face, or any visible facial area.

Must include:

- 人物主光方向
- 骨骼明暗锚点：鼻梁、眼窝、颧骨、下颌线、脸颊转折中的 2-4 个具体部位
- 眼神光 when eyes are visible
- skin/hair/fabric detail when relevant
- environment bounce that matches the scene, mood, style, and character reference

Use the current scene, atmosphere, character reference, and style to select a compatible lighting structure. When needed, consult `seedance-closeup-face-lighting-rules.md`, `seedance-closeup-face-lighting-library.md`, `seedance-real-lighting-rules.md`, `seedance-lighting-scene-library.md`, `seedance-chinese-fantasy-lighting-library.md`, and `lighting-emotion-library.md`.

For medium close-up or closer shots, always mention facial structure, such as nose bridge, cheekbone, jawline, eye socket, and hair rim light.

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

Do not create a separate denial field. Stability requirements must be written as positive, visible consistency targets.

## Reference role language

Do not write vague phrases such as `强参考` alone. Specify exactly what the reference controls and what it does not control.

Use:

```text
人物面部、发型、头饰、珠链和服饰造型严格匹配上传人物参考图；参考图只用于锁定人物外形特征，不干预本镜头的构图、光影、动作和场景。
```

If the platform has reference-strength controls, recommend `人物参考强度 0.7-0.8` outside the copy-ready prompt, not inside the main prompt unless the user asks for parameter notes.

## Positive-only main prompt

The main prompt must not include negative wording or human-facing rules.

Rewrite these as positive consistency targets:

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

### Splitting trigger

When the expected video length is > 5 seconds, or the user specifies a duration > X seconds, and they have NOT stated "一镜到底" (single continuous shot):

1. **Ask the user**: "视频时长预计超过 5 秒，是否需要分段？"
2. **No fixed durations**: Do NOT assign fixed splits (e.g. 0-3s / 3-7s / 7-10s). Allocate time for each segment based on its content weight — heavier action or space reveals get more time, simple transitions get less.
3. **Self-check before delivering**: After allocating durations, verify:
   - Does the time allocation match the action density of each segment?
   - Does the total add up to the target video length?
   - Is the progression logical across segments?
4. **Confirm with user**: Present the segmentation plan and duration allocations to the user for confirmation before writing the timeline.

When the user explicitly requests "一镜到底", skip the splitting question and write a single continuous shot timeline.

Each segment must preserve the same character anchor and motion continuity without repeating the full identity description.

## Weight syntax

Seedance 的 `(关键词:权重值)` 语法只对「有明确视觉对应、可被模型识别为具体画面特征」的元素生效。本质是提升该语义在图像特征空间的占比，让模型更倾向于生成这个元素。

抽象规则、逻辑指令、主观感受、否定描述类内容，加权完全无效，甚至会挤占有效语义权重、引发画面异常。

### 加权有效的元素分类

#### 1. 人物外形类

所有可被视觉化的人物实体特征，加权后能明显提升该特征的还原度。它是解决人物细节丢失、配饰消失的核心手段。

Valid examples:

- 五官 / 脸型：`(鹅蛋脸:1.1)`, `(细长眉眼:1.1)`
- 发型发饰：`(高盘发:1.15)`, `(金色花枝发冠:1.2)`, `(珍珠流苏:1.2)`, `(额前湿润碎发:1.1)`
- 服装配饰：`(米白刺绣纱裙:1.15)`, `(深金腰封:1.2)`, `(半透明纱质披帛:1.1)`

Recommended weight range: `1.1-1.25`, maximum `1.3`. Higher values can cause feature distortion, shape errors, or cloth/accessory intersections.

#### 2. 光影色调类

色彩、光影方向、光影强度这类强视觉特征，加权后色调倾向和光影对比会明显增强。它是调氛围的高效手段。

Valid examples:

- 整体色调：`(冷青灰调:1.2)`, `(暖金色暮色:1.15)`
- 人物面光：`(发丝轮廓金边:1.2)`, `(下颌线明暗交界:1.1)`, `(鼻梁清冷高光:1.15)`
- 环境光影：`(水面暖光倒影:1.2)`, `(雨雾暖光晕:1.15)`

Recommended weight range: `1.1-1.3`. Color tone can be slightly higher. Face-lighting and bone-lighting should usually stay at `1.1-1.2` to avoid broken lighting or unnatural facial separation.

#### 3. 镜头光学与景深类

景深、虚化、焦段质感这类光学视觉属性，加权后能强化虚实对比，比单独写“浅景深”更稳定。

Valid examples:

- 虚化景深：`(背景重度散焦:1.25)`, `(三层景深层次:1.2)`, `(前景纱帘虚化:1.2)`
- 镜头质感：`(50mm电影镜头质感:1.1)`, `(胶片颗粒感:1.2)`

Recommended weight range: `1.15-1.3`. This is useful for countering the model's tendency toward full-depth sharpness.

#### 4. 场景元素与动态道具类

具体环境实体、天气动态、道具细节可以加权，但不要超过人物核心特征，避免背景或道具抢主体。

Valid examples:

- 天气动态：`(细密雨丝:1.2)`, `(低空薄雾:1.1)`, `(湖面雨涟漪:1.15)`
- 场景道具：`(青石板湿滑反光:1.2)`, `(石灯笼暖光:1.15)`, `(油纸伞淡金纹样:1.2)`

Recommended weight range: `1.1-1.2`. Scene element weights must stay below key character-feature weights unless the shot is a pure environment shot.

#### 5. 风格质感类

画面整体的风格、材质质感可以加权，用于强化风格统一，避免画风跳变。

Valid examples:

- 写实类：`(真实电影摄影质感:1.15)`, `(皮肤真实肌理:1.2)`
- 艺术类：`(水墨淡彩质感:1.2)`, `(工笔古风质感:1.15)`

Recommended weight range: `1.1-1.2`. Higher values can make the image over-stylized, distorted, or visually exaggerated.

### 完全无效、绝对不要加权的元素

#### 1. 规则类 / 指令类描述

These are logical requirements for humans, not visual elements the model can directly render.

Invalid examples:

- `(人物造型一致:1.3)`
- `(叙事连续:1.3)`
- `(运镜稳定:1.2)`
- `(不抢人物焦点:1.3)`
- `(上传人物造型图角色一致:1.3)`
- `(人物面部与头饰一致:1.3)`
- `(石桥雨中行走叙事连续:1.3)`
- `(动作连贯:1.2)`
- `(过肩视角稳定跟拍:1.3)`
- `(运镜匀速极慢:1.2)`
- `(必须保持一致:1.3)`
- `(禁止跑偏:1.3)`
- `(人物始终为画面视觉核心:1.2)`

Replacement rule: convert the rule into concrete visible features before weighting. For example, to stabilize hair accessories, weight `(金色花枝发冠:1.2)` instead of `(造型一致:1.3)`.

#### 2. 抽象情绪 / 感受类

Subjective feelings do not have a single stable visual representation and should not be weighted.

Invalid examples:

- `(氛围感拉满:1.3)`
- `(诗意感:1.2)`
- `(清冷气质:1.3)`

Replacement rule: translate the feeling into visible elements. For “清冷感”, use concrete visual features such as `(冷青灰调:1.2)` plus `(低饱和画面:1.15)`.

#### 3. 否定描述

Negative wording inside the main prompt is weak. Weighting negative phrases can even trigger the unwanted feature. Convert failure prevention into positive visible targets instead.

Invalid examples in the main prompt:

- `(不要穿模:1.3)`
- `(不要崩坏:1.2)`

Replacement rule: describe the desired stable result in positive language, for example `手部结构自然清晰`, `五官比例稳定`, `道具与手部接触自然`.

#### 4. 生成参数类

Panel/settings parameters do not work when written in prompt text.

Invalid examples:

- `(参考强度0.7:1.2)`
- `(创意度0.4:1.2)`
- `(采样步数30:1.2)`

### 加权使用规则

1. **语序前置 > 加权**  
   Put core elements early. Front-loading brings stronger and more stable priority than adding `1.2`. Weighting is an enhancement, not a rescue mechanism.

2. **只给精准关键词加权，不给长句子加权**  
   Use `(金色花枝发冠:1.2)`, not a whole sentence in parentheses. Long weighted phrases cause semantic confusion.

3. **权重范围控制在 `1.05-1.3`**  
   - Light emphasis: `1.05-1.1`
   - Medium emphasis: `1.1-1.2`
   - Strong emphasis: `1.2-1.3`
   - Values above `1.4` are not recommended and can cause deformation, color spill, or image breakdown.

4. **权重层级必须符合主次逻辑，人物永远高于环境**  
   Recommended hierarchy: character core features > character face/hair/clothing/accessory lighting > key carried prop > environmental lighting > scene elements > style/texture.  
   When a human character is the subject, character visual weights must always be equal to or higher than environment weights. Do not make background rain `1.3` while the main hair accessory is only `1.1`, unless the shot is explicitly a pure environment or weather shot.

5. **数量控制**
   Use only the most important concrete visual stability points. Prefer `1-4` weighted phrases per prompt. Too many weights dilute priority.

### Correct example for the user's ancient female character scene

Correct:

```text
@Image1 仅作为女主形象参考，不作为首帧，不参考原图构图背景。
东方古风女性，(高盘发:1.15)，(金色花枝发冠:1.2)，(珍珠流苏:1.2)，象牙白刺绣纱裙，(深金腰封:1.15)，清冷气质。
(冷青灰暮色:1.2)，细雨朦胧，(背景湖面散焦虚化:1.2)，真实电影质感。
```

Incorrect:

```text
(人物造型一致:1.3)，(叙事连续:1.3)，(氛围感很强:1.2)，古风女子撑伞走在桥上。
```

For identity consistency, narrative continuity, camera movement, and behavioral instructions, use high-priority natural-language placement instead of numeric weights: place them early, state them clearly, and restate only when needed in timeline transitions.

## Output self-check

Before finalizing a Seedance prompt, verify:

1. Does the first sentence contain shot/view, main camera movement, and immediately afterward the character + reference-image lock before any environment description?
2. Are reference roles explicit and limited?
3. Is the main prompt free of negative wording?
4. Are human-facing rule phrases removed?
5. Are expressions visible through eyes, brows, mouth, face muscles, head/neck/shoulder/body?
6. If the prompt describes or shows the character face in any way, does it include concrete face-lighting and bone-structure details selected from the scene/mood/reference/style lighting logic?
7. For videos > 5s without 一镜到底, has the user been asked about segmentation? If segmented, have durations been allocated based on content weight, self-checked, and confirmed with the user?
8. Are failure-prevention ideas rewritten as positive consistency targets instead of a separate denial field?
9. Are simple weights used only for the most important concrete visual stability points when useful?
10. If both character and environment are weighted, are character visual weights equal to or higher than environment weights?
