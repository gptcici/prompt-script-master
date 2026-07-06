# Retake / Failure Diagnosis 重拍失败诊断规则

## 目的

本规则用于生成结果复盘、提示词审查、失败修复、重拍提示词生成和用户反馈处理。

它解决的问题：

- 用户说“这版不对”，但没有明确指出哪里错。
- 生成结果脸变了、服装变了、动作怪、口型怪、风向乱。
- 连续片段接不上。
- 参考图职责被污染。
- 修复提示词只是在原提示词上堆更多词，导致更乱。

## 启动条件

只要出现以下任一情况，就启动本规则：

```text
用户说：这版不对 / 这个怪 / 帮我修 / 重新来 / 重拍 / retake / 修复提示词 / 审查提示词 / 复盘失败原因
用户反馈：脸不像 / 衣服不对 / 动作不连贯 / 口型不对 / 风向乱 / 光影平 / 镜头怪 / 不像上一段 / 首尾接不上
用户上传失败结果图并要求继续改
S9_INTERNAL_QA 自检发现明显缺失或冲突
```

## 状态机挂接位置

本规则在以下阶段启动：

```text
S9_INTERNAL_QA
后续修订轮次
提示词审查 / 修复任务
用户上传失败结果后的参考图扫描阶段
```

## 诊断顺序

重拍诊断必须先归因，再修复。
不要直接堆更多形容词。

诊断顺序如下：

```text
1. 目标偏差：生成结果和用户目标哪里不一致？
2. 参考图职责：是否有参考图污染？
3. 人物身份：脸、年龄感、发型、妆容是否漂移？
4. 人物表演：动作、表情、口型、身体联动是否成立？
5. 人物面光：近景 / 特写是否缺少面部光影结构？
6. 风 / 柔体动态：发丝、衣物、饰品、环境动态是否统一？
7. 连续片段：是否重复旧动作、提前出现未来事件或无法衔接？
8. 镜头语言：机位、景别、运镜、轴线、焦点是否清楚？
9. 提示词结构：是否过短、过长、负面混入正文或旧模板残留？
```

## 失败类型表

### A. 身份类失败

```text
identity drift：脸型漂移、五官变化、年龄感变化、人物变成通用 AI 脸。
makeup drift：妆容、肤色、眉眼风格偏移。
hair drift：发型、发色、发量、发饰位置变化。
```

修复方向：

```text
强化参考图职责：人物参考图只锁定脸、五官、眼神、鼻唇、发型、年龄感和气质。
把“不得换脸 / 不得通用 AI 模特脸”放入人物类负面。
减少会污染身份的风格化形容词。
```

### B. 服装 / 饰品类失败

```text
costume drift：衣服结构、胸口形状、袖口、裙摆、层次不对。
accessory drift：头饰、发带、耳饰、流苏、珠链位置错误。
material drift：材质从真实布料变成塑料、纸片或游戏装甲。
```

修复方向：

```text
明确服装参考图只控制服装，不控制脸。
写清真实可穿戴结构、布料重量、缝线、分层、褶皱和金属/玉石/纱料反应。
把服装漂移、饰品错位、材质塑料感放入负面。
```

### C. 动作 / 表情 / 口型失败

```text
action weak：动作不明确，只站着或摆拍。
action repeat：重复上一段已经完成的动作。
expression flat：只有情绪标签，没有眼神、眉、嘴、脸部肌肉和身体联动。
mouth failure：唱歌/说话没有口型，下颌乱动，嘴部与情绪脱节。
body-face mismatch：身体动作和脸部表情不一致。
```

修复方向：

```text
执行人物镜头强制覆盖规则。
补足人物核心动作、眼神、眉部、嘴部、头颈肩手、身体重心。
唱歌/说话时补足下颌稳定、嘴唇开合幅度、呼吸节奏和脸身连续性。
把动作卡顿、嘴部崩坏、口型脱节放入动作类负面。
```

### D. 人物面光失败

```text
flat face：面部平光，全脸均匀打亮。
dead shadow：眼窝或下颌死黑无细节。
overexposed face：脸部过曝惨白。
no catchlight：无眼神光。
plastic skin：皮肤塑料磨皮。
```

修复方向：

```text
中近景 / 近景 / 特写必须补足人物面部光影。
写主光方向、光质与色温、鼻梁、眼窝、颧骨、下颌线、眼神光、皮肤微细节和环境弱反光。
把平光脸、死黑、过曝、无眼神光、塑料皮肤放入负面。
```

### E. 风 / 柔体 / 物理动力学失败

```text
wind conflict：头发、衣服、纱幔、云雾朝不同方向运动。
physical dynamics failure：动态无动力来源、无路径、无接触点、无结果或无消散。
static material：发丝、披帛、纱幔完全不动。
weightless fabric：布料无重量，像塑料片或纸片。
same-speed drift：所有物体同速漂浮。
environment mismatch：远景云雾或水面和近景风向冲突。
contact failure：脚步、手部、道具碰撞没有涟漪、震动、位移、摩擦或停点。
fluid/particle failure：雨雪、烟尘、火焰、粒子没有来源、方向、密度、受光、落点或消散。
```

修复方向：

```text
补全全局物理动力学锚点。
先定义动力来源和运动路径，再写发丝、披帛、袖口、裙摆、珠链、纱幔、竹叶、云雾、水面、雨雪、烟尘、火焰、粒子、道具、接触点、碰撞、重力、惯性、消散的速度差、延迟、回弹、重量、反作用和最终状态。
把风向混乱、发丝不动、布料无重量、所有物体同速漂浮、烟雾无来源、水面无接触点乱波动、粒子无落点、硬道具无支点放入动力学类或对应负面类别。
```

### F. 连续性失败

```text
state jump：人物位置、姿态、道具状态突然跳变。
event repeat：上一段已经完成的动作被重复。
future leak：未来段落事件提前出现。
emotion break：情绪从上一段到当前段断裂。
prop mismatch：道具状态不连续。
light/wind jump：光源方向或风向突然变化。
```

修复方向：

```text
建立连续片段状态胶囊。
写清 already_happened、current_clip_only、reserved_for_later、planned_start_state、planned_end_state。
当前提示词只写当前片段，不重复旧动作，不泄露未来段。
```

### G. 镜头语言失败

```text
camera unclear：机位、景别、运镜不清。
axis flip：镜头方向或人物朝向突然翻转。
focus missing：焦点没有控制。
cut weak：镜头切点不明确。
oVERcrowded shot：一个镜头塞太多动作。
```

修复方向：

```text
时间轴每个镜头写清景别、机位、运镜、焦点、主体动作、环境变化。
一个镜头只承担一个核心动作或情绪推进。
连续镜头保持轴线、空间方向和视觉动线。
```

### H. 提示词结构失败

```text
too short：提示词过短，缺少锚点。
too long：提示词过长，重复堆叠。
negative in main：负面词混入正文。
old format：使用旧三板块模板。
missing negative：缺少负面提示词分类。
```

修复方向：

```text
回到 V0.9.74 最终结构：
【正文提示词】总设定 + 参考图职责 + 全局光源锚点 + 全局物理动力学锚点 + 镜头时间轴 + 全局一致性
【负面提示词】人物类 + 动作类 + 动力学类 + 场景类 + 风格类
```

## 重拍输出格式

当用户要求“帮我修 / 重拍 / retake”时，建议输出：

```text
【失败归因】
1. ...
2. ...

【修复策略】
1. ...
2. ...

【重拍提示词】
【正文提示词】
...

【负面提示词】
...
```

如果用户明确只要最终提示词，则只输出重拍提示词，不输出解释。

## 重拍原则

1. 不要简单堆更多形容词。
2. 先找失败类别，再改对应模块。
3. 人物失败优先修身份、动作、表情、口型、面光。
4. 风动失败优先修统一风场和材质响应。
5. 连续性失败优先修状态胶囊。
6. 多参考图失败优先修参考图职责契约。
7. 负面只放故障项，不混入正文。
8. 保持最终提示词中等精简，不因修复变成超长说明书。

## V0.9.76 expanded diagnosis

新增诊断维度：

### 导演意图失败

```text
shot intention missing：镜头只有电影感/氛围感标签，没有明确观众感受变化。
craft mismatch：镜头、光、动作、声音服务不同情绪方向。
```

修复方向：读取 `directing-coherence-engine.md`，先写一句镜头意图，再改运镜、光影、动作和声音。

### 动作合约失败

```text
motion no endpoint：动作没有终点。
motion no consequence：动作没有造成可见结果。
```

修复方向：读取 `motion-performance-contract.md`，补足主体、力量/节奏、物理结果和动作终点。

### 多人物调度失败

```text
crowd overaction：多人同时大幅动作。
unclear blocking：人物站位、视线、主次不清。
```

修复方向：读取 `character-blocking-contract.md`，给主角单一反应，背景人物保持持续微动作。

### 光影意图失败

```text
unmotivated lighting：灯光来源不明。
lighting emotion mismatch：光影和情绪目标不匹配。
reflection missing：材质没有合理反射或高光。
```

修复方向：读取 `lighting-intention-contract.md`，补足主光源、方向、色温、阴影、反射和灯光变化原因。

### 迭代策略失败

```text
too many changes：一次重拍同时改了脸、动作、光、风、镜头和参考图。
reroll loop：连续多次失败但仍只换版本不改提示词。
```

修复方向：读取 `retake-iteration-protocol.md`，先判定保留/后期修/局部编辑/换种子/改写提示词，并一次只改一个变量。


## V0.9.81 face integrity failure

When the user says the face is dirty, malformed, dark, blotchy, waxy, plastic, biologically wrong, or has black spots / color blocks / abnormal shadows, diagnose it as one or more of:

- `reference artifact inherited`: the source image contains artifacts that were copied as identity.
- `face anatomy failure`: eyes, nose, mouth, jaw, head angle, or neck connection violates natural facial structure.
- `skin continuity failure`: skin tone is broken by color patches, black spots, dirty blotches, banding, or wax/plastic texture.
- `face-lighting failure`: shadows do not match a motivated light source, creating dead-black facial regions or unnatural hard patches.
- `attention budget failure`: face is too small, prompt is overloaded, camera moves too much, or action/multi-character demands reduce face stability.

Fix with one primary variable at a time: strengthen `face-integrity-check.md`, simplify camera motion, improve face-lighting anchor, reduce prompt budget elsewhere, or stop inheriting abnormal reference artifacts.


## V0.9.82 参考图低清导致失败

当生成结果出现锁脸失败、服装漂移、背景混乱、首尾帧衔接失败、人脸黑斑、异常色块、死黑阴影或皮肤伪影时，先判断是否由参考图本身不清晰或异常导致。

诊断问题：

- 原参考图是否承担了超出其清晰度的职责。
- 是否在参考图不清晰时仍执行 I2V 极简原则。
- 是否把参考图中的异常色块、黑斑、死黑或畸形结构当作身份特征继承。
- 是否应该建议用户重新生成参考图，而不是继续改写提示词。

如果主职责区域不可辨，优先建议重新生成参考图；如果只有局部不清晰，则补写局部锚点并降低该参考图职责权重。
