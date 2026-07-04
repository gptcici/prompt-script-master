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

## 权重规范标准化

> `(关键词:权重值)` 语法只对「有明确视觉对应、可被模型识别为具体画面特征」的元素生效。抽象规则、逻辑指令、主观感受、否定描述类内容，加权完全无效，甚至引发画面异常。

### 权重分层体系（S/A/B 三级，严格对应优先级）

按「人物核心 > 质感光影 > 环境氛围」分为三档，权重值随优先级递减，**环境类权重永远不得高于人物类权重**。

| 权重档位 | 数值范围 | 适用元素 | 使用频率 |
|----------|---------|---------|---------|
| **S 级**（核心必保） | 1.15 - 1.25 | 人物核心识别特征：标志性发饰、核心服装部件、五官关键特征 | 单段 1-2 个，全文不超 3 个 |
| **A 级**（质感强化） | 1.1 - 1.15 | 关键面光关键词、核心材质质感、主风格定位 | 单段 1 个，全文不超 4 个 |
| **B 级**（氛围补充） | 1.05 - 1.1 | 次要环境元素、细节氛围点缀 | 尽量不用，非必要不加 |

### 强制书写规范

**仅给精准名词短语加权：** 禁止给长句子、整句话、逻辑描述加权，只给单个核心元素加。

| 正确 | 错误 |
|------|------|
| `(金色花冠发饰:1.2)` | `(人物造型全程保持一致:1.3)` |
| `(透明披帛:1.15)` | `(运镜稳定:1.2)` |
| `(肩线发丝金边:1.1)` | `(叙事连续:1.3)` |

**放置位置跟随所属模块：**

- **人物特征加权** → 紧跟人物外形描述，和对应元素绑定
- **光影质感加权** → 紧跟光影描述段落
- **风格整体加权** → 放在全局风格收尾段

**权重上限红线：** 所有元素权重最高不超过 1.3，超过视为违规。

**负面提示词加权规则：** 高频崩点可加 1.2-1.3 权重，如 `(手部畸形:1.3)`，仅放负面栏，正文禁止出现否定加权。

### 标准套用示例（对应山顶凉亭场景）

> ⚠️ **以下示例仅用于参考 S/A/B 三级权重的放置位置和数值用法，严禁直接照搬场景设定、人物身份、具体文本内容。** 实际生成时必须根据当前镜头的人物特征、光源类型和场景细节独立分配权重——哪些元素归 S 级（核心必保）、哪些归 A 级（质感强化）、哪些归 B 级（氛围补充）完全由当前场景决定，禁止套用此示例中的具体加权对象和数值。

```text
16:9 横屏，10 秒，全程背后跟拍稳定前推。
@Image1 仅作为人物强参考，锁定五官发型服装，不作为首帧。
纤细身形，黑色长发高髻，(金色花冠珠链:1.2)，身着浅金白色轻纱古装，(透明披帛:1.15)，布料层次真实，清冷气质。
山顶悬崖古亭，柱间悬挂轻薄纱幔，悬崖外云海与红金夕阳，山风持续吹动。

0-5s：中近景背后跟拍，镜头稳定前推，角色缓步走向亭口；发丝、衣袖、裙摆随风轻扬。
夕阳侧逆光从亭柱缝隙切入，(肩线发丝金边:1.1)，发饰金属带细碎高光，亭内外明暗层次分明。
浅景深跟随人物，前景纱幔虚化擦镜，远景云海天光柔和透出。

(彩色写实电影摄影质感:1.2)，东方仙侠写实风格，真实布料重量，自然景深。
全程人物造型稳定，光影逻辑自洽，运镜平稳。
```

### 权重禁止项

| # | 禁止项 | 原因 |
|---|--------|------|
| 1 | 给规则类、指令类、逻辑类描述加权 | 非视觉元素，加权无效且挤占语义 |
| 2 | 给否定词、负面描述在正文加权 | 可能触发不想要的画面特征 |
| 3 | 同维度重复加权 | 如同时给写实质感、电影质感、摄影质感各加 1.2 |
| 4 | 环境元素权重高于人物核心元素权重 | 违反主次逻辑 |
| 5 | 单段加权词超过 3 个，全文加权词超过 6 个 | 权重稀释，失去优先级意义 |

### 完全无效、绝对不要加权的元素

#### 规则类 / 指令类描述

- ❌ `(人物造型一致:1.3)` `(叙事连续:1.3)` `(运镜稳定:1.2)`
- ❌ `(不抢人物焦点:1.3)` `(动作连贯:1.2)` `(必须保持一致:1.3)`
- ✅ 替代方案：将规则转为具体可视特征加权，如用 `(金色花枝发冠:1.2)` 代替 `(造型一致:1.3)`

#### 抽象情绪 / 感受类

- ❌ `(氛围感拉满:1.3)` `(诗意感:1.2)` `(清冷气质:1.3)`
- ✅ 替代方案：`(冷青灰调:1.2)` + `(低饱和画面:1.15)` 代替"清冷感"

#### 否定描述

- ❌ `(不要穿模:1.3)` `(不要崩坏:1.2)`
- ✅ 替代方案：写正面可视目标，如 `手部结构自然清晰`、`五官比例稳定`

#### 生成参数类

- ❌ `(参考强度0.7:1.2)` `(创意度0.4:1.2)` `(采样步数30:1.2)`
- ✅ 面板参数不在提示词中生效，应在界面设置

### 加权核心原则（语序前置 > 加权）

核心元素靠前放置的优先级 > 加 1.2 权重。加权是增强手段，不是补救手段。一个靠前未加权的 S 级元素，影响力高于一个靠后加 1.2 的同级元素。

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
