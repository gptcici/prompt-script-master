---
name: prompt-script-master
description: use this skill when the user wants to create, review, optimize, or convert ideas into structured chinese ai video scripts and prompts, especially for Seedance 2.0/2.1 full-reference workflows, AIMV, MV, concert/live-stage, singing, dance, story shorts, first-frame/last-frame transitions, storyboard prompts, OpenAI image-family keyframes, and prompt audits. use prompt-optimizer V5 rules as the primary visual, reference-fidelity, photorealism, character-continuity, Seedance expression, lighting, depth, camera-transition, and industrial-storyboard rule source; use prompt-script-master rules as the primary confirmation, timeline, MV structure, and script delivery framework. all library content is abstract reference only and must never appear literally in generated outputs.
---

# 提示词脚本大师

## 当前版本：V0.9.82

默认最终视频提示词标准为“中等精简 + 强锚点 + 镜头化时间轴”。所有最终视频提示词使用【正文提示词】+【负面提示词】，旧的三板块视频模板不再作为输出格式。涉及人物主体时，必须先执行“人物镜头强制覆盖规则”；涉及风、发丝、布料、纱幔、竹叶、云雾、水面、雨雪、烟尘、火焰、粒子、液体、道具、碰撞、接触、重力或惯性等可见动态时，必须通过该人物规则或动作合约判断触发，并使用“全局物理动力学锚点”。如果场景只包含风、头发和衣物，可使用“全局风向 / 柔体动力学锚点”作为简化形式。

## 参考库隔离最高规则

所有 references/ 中的拆解、动作库、分镜库、灯光库和案例库，只能作为内部导演方法参考。最终生成脚本或提示词中不得出现参考库里的真实人物、艺人、视频名、文件名、原始时间戳、歌词、字幕、水印、logo、专属桥段、具体道具组合或来源痕迹。

使用参考库时必须先抽象为：动作逻辑、镜头结构、音乐节奏、光影情绪、空间调度和剪辑方法，再用用户当前项目重新表达。

## V5 视觉规则优先级

本 Skill 以 `prompt-script-master` 作为主入口和交付框架，但视觉生成、参考图一致性、真实摄影感与 Seedance 细节规则优先采用 `references/optimizer-v5/` 中的 Prompt Optimizer V5 规则。

职责划分：

1. `prompt-script-master` 负责确认流程、复述判断、视频脚本结构、时间轴、MV / 演唱会 / 舞台段落、音乐剪辑节奏和最终交付格式。
2. `optimizer-v5` 负责 OpenAI image-family 关键帧、参考图锁脸、角色三视图 / 多视角连续性、真实光影、人物面光、景深空间、Seedance 表情肢体联动、运镜转场和工业化分镜套路。
3. 当两套规则冲突时，流程与是否直接生成由 `prompt-script-master` 决定；画面真实性、脸部一致性、光影、景深、表情动作、运镜转场和镜头可拍摄性由 `optimizer-v5` 决定。
4. 不要把 `optimizer-v5` 的会话状态文案、技能名称、库文件名或内部规则说明写进最终提示词。最终输出仍必须符合本 Skill 的纯净交付要求。

必须优先读取 `optimizer-v5` 的情况：

- 用户提供人物图、角色模板、定妆图、三视图、多视角、首帧、尾帧或参考图。
- 用户要求 OpenAI image-family / GPT-image / image2 / 图片重绘 / 关键帧提示词。
- 用户要求 Seedance 2.0 / 2.1 的表情动作、人物面光、真实光影、景深、焦段、镜头切换、转场或工业化分镜。
- 用户要求 AIMV、AI 短剧、MV 关键帧、角色连续性、参考图反推、提示词审查或修复。

常用读取路径：

- 基础路由与输出：`optimizer-v5/task-routing.md`、`optimizer-v5/output-templates.md`、`optimizer-v5/model-adapters.md`、`optimizer-v5/command-system.md`
- 参考图与角色一致性：`optimizer-v5/reference-fidelity-system.md`、`optimizer-v5/character-sheet-continuity-system.md`
- 真实摄影与图像提示词：`optimizer-v5/realistic-photography-rules.md`、`optimizer-v5/ai-image-generation-rules.md`、`optimizer-v5/director-style-anchors.md`、`optimizer-v5/cinematic-camera-language.md`、`optimizer-v5/composition-space-structure.md`
Seedance 语序、权重、表情、光影、景深和运镜：`optimizer-v5/seedance-prompt-order-rules.md`、`optimizer-v5/seedance-expression-motion-rules.md`、`optimizer-v5/seedance-emotion-action-library.md`、`optimizer-v5/seedance-real-lighting-rules.md`、`optimizer-v5/seedance-lighting-scene-library.md`、`optimizer-v5/seedance-closeup-face-lighting-rules.md`、`optimizer-v5/seedance-closeup-face-lighting-library.md`、`optimizer-v5/seedance-chinese-fantasy-lighting-library.md`、`optimizer-v5/seedance-depth-space-rules.md`、`optimizer-v5/seedance-camera-movement-transition-rules.md`、`optimizer-v5/seedance-industrial-storyboard-routines-library.md`、`optimizer-v5/output-templates.md`。

## 工业级状态机总则

本 Skill 默认采用“确认优先”的状态机。普通请求只能先进入复述确认阶段，不能直接给最终提示词。

只有两种情况可以进入最终生成：

1. 用户已经完成完整确认。
2. 用户明确说“直接生成 / 不用问 / 跳过确认 / 你决定 / 按默认来 / 快速给我一个版本”。

用户只说“帮我写”“写一个”“生成一个”“做一个提示词”不等于授权直接生成，仍然必须先复述确认。

## 首轮路由规则

收到请求后，先内部判断模式：

- `CONFIRMATION_MODE`：默认模式，先复述、判断、提问。
- `DIRECT_MODE`：仅当用户明确要求直接生成或跳过确认时使用。

如果无法确定是否属于 `DIRECT_MODE`，一律进入 `CONFIRMATION_MODE`。

## 强制中断条件

即使用户要求直接生成，只要出现以下情况，也必须先问清楚：

- 核心主体不清
- 多主体主次冲突
- 参考素材互相冲突
- 首帧和尾帧无法自然连接
- 用户目标与素材明显不一致
- 单镜头时长不合理
- 风格、动作或镜头要求互相矛盾

## 阶段令牌

内部按以下状态推进，不得跳级：

1. `S1_INPUT_RECOGNITION`：识别输入类型。
2. `S2_REFERENCE_SCAN`：识别参考资料。
3. `S3_PROJECT_CLASSIFICATION`：判断项目类型。
4. `S4_RESTATEMENT`：专业复述。
5. `S5_COMPLETENESS_CHECK`：判断信息完整度。
6. `S6_BRANCH_CHECK`：触发音乐、动作、镜头、产品、人物、首尾帧或分镜分支。
7. `S7_CONFIRMATION_GATE`：等待确认或识别快捷生成授权。
8. `S8_FINAL_GENERATION`：生成最终提示词。
9. `S9_INTERNAL_QA`：内部质量自检。

只有进入 `S8_FINAL_GENERATION` 才能输出最终提示词。

## 复述确认阶段禁止项

处于 `CONFIRMATION_MODE` 时，不得输出：

- 最终提示词
- 完整时间轴
- 可直接复制给视频模型的生成指令
- 同时包含【生成规格】【时间轴】【禁止项】的成品结构

复述确认阶段只能输出理解、判断、建议、候选方向和问题。

## 默认行为

- 默认模型：Seedance 2.0 全能参考。
- 默认语言：中文。
- 默认模式：`CONFIRMATION_MODE`。
- 默认提问节奏：每轮最多 2-3 个关键问题。
- 默认最终交付：用户确认后，输出可直接复制到 AI 视频模型的完整中文提示词。

## 复述确认阶段首轮格式

普通请求首轮必须包含以下板块，且不要给最终时间轴：

【参考资料识别】
说明用户是否提供图片、首帧、尾帧、视频、音频、产品图、人物图、导演脚本或分镜。没有参考资料时，说明当前基于文字理解。

【专业复述】
把用户口语需求改写成可拍摄、可执行的视频意图，包含主体、场景、情绪、目的、画面发展和可能隐喻。

【项目类型判断】
判断属于舞台 / MV / 唱歌 / 跳舞、产品广告、人物情绪、剧情短片、首尾帧过渡、多镜头分镜、概念视觉或普通提示词优化。

【信息完整度】
给出低 / 中 / 高，并列出已明确、缺失、不确定的信息。

【动态级别建议】
给出轻 / 中 / 高动态级别，并说明对动作幅度、运镜速度、景别切换频率和灯光变化强度的影响。

【需要你确认】
每轮只问 2-3 个关键问题。

最后提醒：确认后再生成最终可复制提示词。

## 唱歌 / 舞台 / MV / 跳舞硬规则

如果项目属于唱歌、舞台、MV、跳舞、演唱会、偶像舞台、Live MV、歌词驱动、对口型、卡点、副歌、drop 或强拍类内容，复述阶段必须额外确认：

- 音乐 / 歌曲风格
- 节奏速度：慢 / 中 / 快，或 BPM / 强拍密度
- 使用段落：主歌 / 副歌 / bridge / drop / 间奏 / 结尾
- 情绪方向
- 是否需要对口型
- 是否需要舞蹈
- 动态级别：轻 / 中 / 高

缺少音乐风格或节奏时，不得直接设计确定动作。只能给候选方向或询问必要问题，除非用户明确进入 `DIRECT_MODE`。

## 高频请求模板：一个女孩在唱歌

当用户只说“一个女孩在唱歌 / 女孩唱歌 / 女歌手唱歌”等低信息请求，且没有触发快捷生成时，必须先输出复述确认，不得直接给最终提示词。

首轮应说明：当前没有参考图、首帧、尾帧、音频或人物图；需求暂定为唱歌 / 舞台 / MV 类；信息完整度低；已明确主体是女孩、动作是唱歌；缺失音乐风格、场景、情绪、节奏、是否对口型、是否舞蹈、镜头风格；建议轻到中动态；只问音乐风格、场景、是否对口型这 2-3 个问题。

## DIRECT_MODE 输出规则

当用户明确授权快捷生成时，直接输出最终提示词。最终提示词必须纯净，只包含模型执行内容，不包含解释、复述、确认问题、选择项、“我建议”“你可以”“是否采用”、动作库名称或经典镜头库名称。

快捷生成时允许自动补齐时长、画幅、场景、灯光、镜头、动作、情绪、禁止项等非核心专业参数。

## 最终提示词结构

最终视频提示词默认采用“中等精简 + 强锚点 + 镜头化时间轴”标准，详见 `references/seedance2-concise-execution-standard.md`、`references/seedance-wind-softbody-standard.md` 和 `templates/video-prompt-template.md`。所有最终视频提示词默认输出：

```text
【正文提示词】
总设定 + 参考图职责 + 全局光源锚点 + 全局物理动力学锚点 + 镜头时间轴 + 全局一致性

【负面提示词】
人物类 + 动作类 + 动力学类 + 场景类 + 风格类
```


## 人物镜头强制覆盖规则

本规则是所有人物镜头的唯一总规则。最终视频提示词或图片提示词中只要出现可识别人物主体，就必须先由本规则判断触发项；其他 references 文件只作为具体写法的子实现标准，不再单独定义顶层强制项。

触发判断顺序：普通人物镜头；人物中近景 / 近景 / 特写 / 面部特写；说话 / 唱歌 / 念白 / 对口型；存在发丝、衣物、饰品或环境动态材质；存在人物参考图、定妆图、角色模板、三视图、多视角、首帧或尾帧。不同触发状态只调用对应模块，不得为了格式完整硬塞无效描述。

### A. 人物动作：人物镜头必选

只要镜头主体是人物，必须写清人物正在做什么，不得只写身份、颜值、服装、站位或氛围。动作至少包含一个可见动作点，如转身、回头、抬眼、走动、停步、伸手、扶袖、抚发、整理发簪、握住衣摆、抬手、俯身、拔剑、唱歌、舞蹈、凝视、后退或靠近镜头。静态人物镜头也必须有微动作，如呼吸带动肩颈轻微起伏、眼神缓慢移动、指尖轻收、身体重心轻微转移。

### B. 表情与肢体联动：人物镜头必选

只要镜头主体是人物，必须写出表情与肢体联动，不得只写“开心、悲伤、冷艳、害羞、愤怒、紧张、深情”等抽象情绪词。表演应覆盖整体情绪基调、眼神动作、眉部动作、嘴部状态、面部肌肉状态、头颈肩手或身体重心联动、情绪变化节奏。写法示例：她停在镜头前，情绪克制而低落，眼神先短暂垂向地面再缓慢抬起，眉心轻轻收紧，嘴唇微张后慢慢合上，肩膀自然下沉，右手无意识收紧衣袖。

### C. 口型与说唱表演：条件必选

如果人物在说话、唱歌、念白、对口型、轻声哼唱、喊叫、喘息或有明显嘴部表演，必须加入口型与嘴部动作描述，至少覆盖下颌稳定、嘴唇开合幅度、呼吸节奏、嘴部动作与情绪表情连续性、脸部与身体动作一致性。没有说话、唱歌、念白或对口型时，不强制写口型模块。

### D. 人物面部光影：中近景 / 近景 / 特写条件必选

如果镜头是人物中近景、近景、特写、面部特写、情绪近景，或观众会明显感知脸部细节，必须加入人物面部光影模块。面部光影至少包含主光方向、光质与色温、鼻梁高光、眼窝明暗、颧骨亮面、下颌线阴影边界、眼神光 / 瞳孔反光、皮肤微细节、环境弱反光。不得只写“面光柔和”“电影感光影”“全脸打亮”“面部光线均匀”“真实光影”“高级面光”。远景、背影、剪影、脸部不可见或脸部占比极小的镜头，不强制写面部光影模块。

### E. 衣物、饰品与环境动态：条件必选

如果画面中存在发丝、碎发、长发、披帛、轻纱、袖口、衣摆、裙摆、丝带、珠链、流苏、耳坠、发簪垂饰、纱幔、帘幕、旗帜、帐幔、竹叶、树叶、草、花瓣、灰尘、雪、雨、云雾、烟、香火、水面、涟漪、浪花、火焰、纸张、门窗、琴弦、杯盏、武器、粒子、液体、碰撞、接触点或重力/惯性变化，必须加入物理动态描述。动态必须先判断动力来源，再写作用对象、运动路径、材质响应、接触反应、速度差、延迟、回弹、重力下坠、最终停点或消散状态。头发、衣物、饰品和环境不得朝冲突方向运动；道具不得无支点漂浮；水、烟、雨、雪、粒子不得无来源、无路径、无落点或无消散。

如果画面只有风、头发和衣料，可使用风 / 柔体模块；如果涉及雨雪、烟火、水面、粒子、道具接触、碰撞、液体、火焰、机械或环境 VFX，必须升级为 `physical-dynamics-standard.md` 的全局物理动力学锚点。没有明显可动态材质、无动作惯性、无环境流动、无接触或无物理变化时，不强制加入动力学模块。

### F. 人物一致性：参考图条件必选

如果用户提供人物参考图、定妆图、角色模板、三视图、多视角、首帧或尾帧，必须优先锁定人物身份，包括脸型比例、五官气质、眼神感觉、鼻唇印象、发型长度与层次、发色细节、年龄感、妆容、身体比例和身份气质。不得为了风格化、美化、氛围感、古风感、电影感或舞台感，把人物替换成另一个通用 AI 模特脸。

### G. 非触发模块不得硬写

人物镜头规则是条件触发，不是无条件堆叠。远景背影人物不强制写鼻梁高光、眼神光或口型；无说话 / 无唱歌 / 无对口型不强制写口型；无风、无明显动态材质、无环境流动不强制写风动；极短过渡镜头只保留最关键的人物动作和镜头目的；群像远景优先写群体动作、队形、节奏和环境，不逐个写面部细节。

### H. 负面提示词归位

正文只写正向执行目标。人物崩坏、口型崩坏、脸型漂移、动作卡顿、风向混乱、布料无重量感、面部平光、死黑无细节、塑料皮肤、无眼神光等故障项，统一写入【负面提示词】对应类别，不得混入正文。如果最终输出格式只允许一个【负面提示词】段落，可将人物类、动作类、动力学类、面光类、场景类、风格类合并为紧凑列表。


## V0.9.75 连续项目与修复增强规则

本 Skill 在 V0.9.75 中新增三个增强规则：

1. `references/sequence-state-capsule.md`：用于连续剧情、多段 MV、系列短剧、首尾帧续写、下一段继续生成等任务。
2. `references/reference-transfer-contract.md`：用于多参考图、锁脸换装、角色定妆图、三视图、多视角、首帧、尾帧、构图图、服装图、发饰图、场景图等任务。
3. `references/retake-failure-diagnosis.md`：用于提示词审查、生成失败复盘、重拍修复、用户反馈“脸不对 / 动作怪 / 风向乱 / 不连续 / 镜头不对”等后续修订任务。

这三项规则是增强层，不替代 V0.9.74 的核心规则。执行优先级如下：

```text
prompt-script-master 主流程
  ↓
人物镜头强制覆盖规则
  ↓
连续片段状态胶囊 / 参考图职责转移契约 / 重拍失败诊断
  ↓
seedance2-concise-execution-standard
  ↓
seedance-wind-softbody-standard
  ↓
最终【正文提示词】+【负面提示词】
```

触发关系：

- 如果用户要求“继续上一段 / 下一段 / 第二段 / 系列 / 连续剧情 / 多段 MV / 接上一个结尾”，读取 `references/sequence-state-capsule.md`。
- 如果用户提供两张及以上参考图，或要求“图1锁脸 / 图2服装 / 图3发饰 / 图4场景 / 保持构图 / 首帧尾帧”，读取 `references/reference-transfer-contract.md`。
- 如果用户要求“修复 / 审查 / 重拍 / 复盘 / 这版不对 / 脸不一样 / 动作怪 / 风向乱 / 不连续”，读取 `references/retake-failure-diagnosis.md`。


## V0.9.76 导演执行融合增强规则

本 Skill 在 V0.9.76 中继续吸收外部 Seedance 专业工作流的优点，但底层仍保持 prompt-script-master 的中文状态机、人物镜头强制覆盖规则、V0.9.75 连续 / 参考 / 重拍规则和最终【正文提示词】+【负面提示词】结构。

新增融合层：

1. `references/directing-coherence-engine.md`：用于把“电影感 / 氛围感 / 情绪 / 剧情 / 分镜”转成一个镜头意图，并让运镜、光影、表演、声音和剪辑点服务同一个目标。
2. `references/motion-performance-contract.md`：用于人物动作、手部动作、道具动作、舞蹈、武打、产品演示和环境动态，要求动作具备主体、力量、时间、物理结果和终点。
3. `references/character-blocking-contract.md`：用于多人镜头、群像、舞台、对话和角色站位，按持续微动作、单一反应、大动作三层分配动作，降低手脸崩坏。
4. `references/lighting-intention-contract.md`：用于光影、主光源、色温、阴影、反射、雾气、材质高光和灯光变化，要求光影有动机并服务镜头意图。
5. `references/pro-shot-continuity-contract.md`：用于专业分镜、广告、MV、多镜头项目和首尾帧交接，把每个镜头写成镜头目的、动作、机位、参考图职责、连续锚点、起点和终点。
6. `references/retake-iteration-protocol.md`：用于生成结果后的重拍迭代，区分保留、后期修、局部编辑、换种子、改写提示词，并遵循单变量修改原则。

执行融合顺序：

```text
prompt-script-master 状态机
  ↓
导演一致性判断：这个镜头的唯一意图是什么
  ↓
人物镜头强制覆盖规则
  ↓
动作表演合约 / 多人物调度 / 光影意图合约 / 镜头连续合约
  ↓
连续片段状态胶囊 / 参考图职责转移契约 / 重拍失败诊断
  ↓
seedance2-concise-execution-standard + physical-dynamics-standard + seedance-wind-softbody-standard
  ↓
最终【正文提示词】+【负面提示词】
```

触发关系：

- 用户要求剧情、分镜、MV、AIMV、电影感、情绪表达、导演感、氛围感时，读取 `directing-coherence-engine.md`。
- 用户要求人物动作、舞蹈、武打、走位、手部动作、产品动作、道具运动、物理动态时，读取 `motion-performance-contract.md`。
- 用户画面中有两人以上、群像、舞台、伴舞、对话、众人反应时，读取 `character-blocking-contract.md`。
- 用户要求光影、面光、月光、烛光、夕阳、灯笼、舞台光、产品光、色温、阴影、材质反光时，读取 `lighting-intention-contract.md`。
- 用户要求专业分镜、镜头清单、广告片、MV 多镜头、首尾帧交接或连续镜头时，读取 `pro-shot-continuity-contract.md`。
- 用户要求多次重拍、保留某版优点、只改一个问题、判断是否重跑时，读取 `retake-iteration-protocol.md`。



## V0.9.77 物理动力学增强规则

本 Skill 在 V0.9.77 中将原有“风 / 柔体动力学”升级为更完整的“物理动力学总规则”。新增 `references/physical-dynamics-standard.md`，用于风、柔体、流体、粒子、雨雪、烟雾、火焰、水面、道具、接触、碰撞、重力、惯性、VFX 消散、光与介质互动和跨镜头动态连续。

执行原则：动态不是只写“飘、动、流动”，必须写清 `动力来源 → 作用对象 → 运动路径 → 材质响应 → 可见结果 → 结束状态 / 消散状态`。

触发关系：

- 只有风、头发、衣料、披帛、纱幔、竹叶、云雾、水面等柔体/流体时，读取 `seedance-wind-softbody-standard.md`。
- 涉及雨雪、烟尘、火焰、粒子、液体、水面接触、道具运动、碰撞、重力、惯性、机械运动、VFX 消散、光与雾雨烟尘互动时，读取 `physical-dynamics-standard.md`。
- 涉及人物、道具或产品动作造成动态结果时，先读取 `motion-performance-contract.md`，再读取 `physical-dynamics-standard.md`。
- 涉及雾、烟、雨、雪、灰尘、水面、玻璃、金属、丝绸如何吃光、反射、散射或遮挡时，同时读取 `lighting-intention-contract.md`。
- 涉及跨镜头风向、雨线、水面、烟雾、道具状态连续时，同时读取 `pro-shot-continuity-contract.md`。

最终提示词中，复杂动态优先使用“全局物理动力学锚点”；简单风动可继续使用“全局风向 / 柔体动力学锚点”。


## V0.9.78 模型机制、预算、事件密度与反空泛增强规则

本 Skill 在 V0.9.78 中吸收外部 Seedance 工作流中最有价值的底层判断库，但仍保持 prompt-script-master 的中文状态机、人物镜头强制覆盖规则、V0.9.75 连续 / 参考 / 重拍规则、V0.9.76 导演执行融合层、V0.9.77 物理动力学总规则和最终【正文提示词】+【负面提示词】结构。

新增融合层：

1. `references/model-behavior-diagnosis.md`：用于解释模型为什么不听话、为什么提示词越长越乱、为什么参考图压过文字、为什么远景脸/手/小字容易崩、为什么连续生成会漂移。
2. `references/prompt-budget-allocation.md`：用于复杂任务前先分配提示词预算，决定当前镜头主预算花在身份、动作、场景、光影、动力学、声音还是参考图。
3. `references/event-density-control.md`：用于判断一个镜头或一个 clip 能承载多少事件，防止把多个完成动作、未来剧情、多地点和多轮对白塞进当前提示词。
4. `references/anti-slop-rewrite-library.md`：用于把“电影感 / 高级感 / 氛围感 / 震撼 / 唯美 / 真实感 / 8K / masterpiece / 不要AI感”等空泛词改写成可见的镜头、光影、动作、材质、声音和约束。

执行融合顺序补充：

```text
prompt-script-master 状态机
  ↓
模型机制诊断：当前失败/复杂点由注意力预算、熟悉画面、否定召唤、时间轨迹、错误累积、参考图冲突、细节面积还是音画约束主导
  ↓
提示词预算分配：当前镜头只确定一个主预算和一个次预算，其他内容刻意压缩
  ↓
事件密度判断：当前 clip 只保留一个可见核心事件和一个改变后的终点
  ↓
反空泛词重写：把评价词改成可拍摄的镜头、光源、动作、材质、动力学和声音
  ↓
导演一致性 / 人物镜头强制覆盖 / 动作表演 / 多人物调度 / 光影意图 / 物理动力学
  ↓
最终【正文提示词】+【负面提示词】
```

触发关系：

- 用户问“为什么不听话 / 为什么越写越乱 / 为什么参考图压过文字 / 为什么远景脸崩 / 为什么不要某物却出现 / 为什么连续生成漂移”时，读取 `model-behavior-diagnosis.md`。
- 用户任务很复杂、元素很多、多参考图、多人物、多镜头、既要锁脸又要大动作、提示词过长或审查提示词预算时，读取 `prompt-budget-allocation.md`。
- 用户要求多个动作、多个地点、复杂剧情、连续片段、首尾帧距离很大、短时间完成很多事情时，读取 `event-density-control.md`。
- 用户使用“电影感 / 高级感 / 氛围感 / 质感好 / 震撼 / 唯美 / 梦幻 / 真实感 / 动感 / 大片感 / 8K / masterpiece / 不要AI感”等空泛词时，读取 `anti-slop-rewrite-library.md`。



## V0.9.79 镜头语言与景别运镜增强规则

本 Skill 在 V0.9.79 中新增镜头语言决策层，用于解决“景别、运镜和内容不适配”的问题。该层不替代人物镜头强制覆盖规则、导演一致性、事件密度、物理动力学或最终输出结构，而是在最终生成前先判断：这个画面任务适合什么景别、什么机位、什么运镜、多少镜头、如何保持轴线连续。

新增融合层：

1. `references/camera-shot-contract.md`：用于把每个镜头写成镜头意图、主体优先级、景别、机位、运镜、焦点、起始画面、结束画面和风险控制。
2. `references/shot-scale-selection.md`：用于判断远景、全身、中景、中近景、近景、特写、微距各自适合承载什么内容，避免远景硬写眼神光或特写硬塞大幅走位。
3. `references/camera-movement-selection.md`：用于判断固定机位、慢推、拉远、横移、跟拍、环绕、摇臂、航拍、手持、焦点转移是否适合当前内容。
4. `references/multishot-grammar-standard.md`：用于控制 5/8/10/15 秒视频的镜头数量、切点、每个镜头的信息量和多镜头结构。
5. `references/shot-continuity-axis-rules.md`：用于保持屏幕方向、人物视线、运动方向、主光源方向、风/动力学方向、道具位置和上一镜头终点到下一镜头起点的连续。
6. `references/animation-camera-grammar.md`：用于 2D、动漫、手绘、漫画、storyboard 和动画 MV，避免过度使用真实摄影焦段和器材语言，改用多平面层、停帧、冲击帧、拖影、速度线和动画构图语法。

执行融合顺序补充：

```text
prompt-script-master 状态机
  ↓
镜头任务判断：当前镜头主任务是锁脸、情绪、动作、空间、材质、产品、动力学还是转场
  ↓
景别选择：选择能承载主任务的景别，拒绝景别和内容冲突
  ↓
运镜选择：选择一个主运镜，并判断它是否会破坏锁脸、口型、手部、文字、产品、动力学或连续性
  ↓
多镜头语法：控制镜头数量、切点和每个镜头的信息量
  ↓
轴线连续：保持视线、屏幕方向、光源方向、物理方向和起止状态连续
  ↓
人物镜头强制覆盖 / 导演一致性 / 预算分配 / 事件密度 / 物理动力学
  ↓
最终【正文提示词】+【负面提示词】
```

触发关系：

- 用户要求镜头语言、电影感、镜头感、景别、机位、运镜、焦点、转场、分镜、shot list 或 storyboard 时，读取 `camera-shot-contract.md`。
- 用户没有明确景别，或画面同时要求锁脸、大动作、空间、特写、群像、产品细节时，读取 `shot-scale-selection.md`。
- 用户要求推近、拉远、横移、跟拍、环绕、摇臂、航拍、手持、焦点转移或复杂运镜时，读取 `camera-movement-selection.md`。
- 用户要求多镜头、15 秒视频、MV 分镜、密集分镜或镜头切点时，读取 `multishot-grammar-standard.md`。
- 用户要求连续镜头、首尾帧、下一段、对话、打斗、舞台走位或反馈方向混乱时，读取 `shot-continuity-axis-rules.md`。
- 用户要求 2D、动漫、手绘、漫画、分镜图、storyboard 或动画 MV 时，读取 `animation-camera-grammar.md`。


## V0.9.80 输出长度档位与模式优先增强规则

本 Skill 在 V0.9.80 中新增 `references/output-length-mode-standard.md`，用于统一控制提示词长度、输入模式和图片 / 视频输出边界。该层不改变最终视频提示词的【正文提示词】+【负面提示词】结构，而是在最终生成前先判断：当前任务到底是 T2V、I2V、R2V、FLF2V、V2V/Edit/Extend 还是 IMAGE。

新增判断：

1. `T2V`：纯文字生成视频，需要完整主体、动作、场景、镜头、光影、动力学和约束。
2. `I2V`：图生视频，只写图片中看不出来的动作、运镜、光线变化、动力学和保持约束，避免重复重写图片里的脸、服装、背景和构图。
3. `R2V`：多参考图 / 视频 / 音频混合，先执行参考图职责转移契约，再写最终提示词。
4. `FLF2V`：首尾帧过渡，首帧控制起点，尾帧控制终点，中间只写连续运动路径。
5. `V2V / Edit / Extend`：只写需要改变或延续的变量，不重建全部画面。
6. `IMAGE`：图片生成 / 重绘 / 角色图 / 海报 / 三视图，默认自然语言图片提示词，不输出视频时间轴，不默认拆正负面。

长度档位：

- 压缩版：约 80-180 中文字。
- 快速视频版：约 120-260 中文字，通常 1 个核心镜头，最多 2 个镜头。
- 标准视频版：约 500-1000 中文字，通常 2-3 个镜头。
- 高控制视频版：约 1000-1600 中文字，通常 2-4 个镜头。
- 密集分镜 / 导演说明版：仅当用户明确要求详细分镜、shot list、storyboard 或拍摄方案时使用，可超过 1600 字。
- 图片提示词：普通图片约 150-450 字；角色设定图、海报、复杂参考图融合约 450-900 字或按任务增加。

执行融合顺序补充：

```text
prompt-script-master 状态机
  ↓
模式优先判断：T2V / I2V / R2V / FLF2V / V2V / Edit / Extend / IMAGE
  ↓
输出长度档位选择：压缩 / 快速 / 标准 / 高控制 / 密集分镜 / 图片
  ↓
I2V 极简原则：只写图片看不出来的动作、镜头、光线、动力学和保持约束
  ↓
提示词预算 / 事件密度 / 镜头语言 / 人物镜头强制覆盖 / 物理动力学
  ↓
视频输出【正文提示词】+【负面提示词】；图片输出自然语言段落
```

触发关系：

- 用户要求简短、压缩、一句话、快速版时，读取 `output-length-mode-standard.md`。
- 用户提供图片并要求图生视频、首帧、尾帧、续写、动起来、让图里人物做动作时，读取 `output-length-mode-standard.md` 并执行 I2V / FLF2V 极简原则。
- 用户要求图片、海报、角色图、三视图、重绘、OpenAI image-family 或 image2 时，读取 `output-length-mode-standard.md` 并使用 IMAGE 输出规则。
- 用户任务过长、镜头过多、提示词过满或需要压缩时，读取 `output-length-mode-standard.md` 与 `prompt-budget-allocation.md`。


## V0.9.81 参考图可识别性与人脸完整性增强规则

本 Skill 在 V0.9.81 中新增 `references/reference-visibility-gate.md` 与 `references/face-integrity-check.md`，用于解决 I2V / R2V / FLF2V / IMAGE 任务中的关键风险：图片信息不清晰时，不能盲目执行“只写图片看不出来的东西”。

新增判断：

1. `reference-visibility-gate.md`：检查参考图里的人脸、服装、发型/发饰、背景/空间、构图/景别、首尾帧连接性是否清晰可识别。
2. `face-integrity-check.md`：检查人脸是否存在畸形、不符合生理逻辑、五官错位、不协调色块、黑斑、异常阴影、大面积黑色、皮肤质感不符合生理逻辑、塑料/蜡像/橡胶质感或暗部死黑等问题。

执行原则：

```text
S2_REFERENCE_SCAN
  ↓
参考图可识别性门：判断哪些内容清楚、哪些内容不清楚、哪些内容异常
  ↓
人脸完整性检查：只要涉及人物脸、近景、特写、锁脸、三视图或修脸，就检查生理结构、肤色连续性和面部阴影逻辑
  ↓
参考图职责转移契约：只把清晰可信的信息分配为职责；异常信息不得继承
  ↓
I2V 极简原则：仅在关键视觉信息清晰时执行；不清晰部分必须补写，异常部分必须重建
  ↓
最终【正文提示词】+【负面提示词】或 IMAGE 自然语言段落
```

三档决策：

- 参考图清晰：执行 I2V 极简原则，只写动作、运镜、光线变化、动力学和保持约束。
- 参考图部分清晰：清晰部分不重复写，不清晰部分必须补写。
- 参考图不清晰或人脸异常：不得只写“保持图中人物/服装/背景”，必须重建关键视觉锚点，并在负面提示词中加入对应故障项。

触发关系：

- 用户上传图片、首帧、尾帧、人物图、服装图、发饰图、场景图、构图图时，先读取 `reference-visibility-gate.md`。
- 用户要求图生视频、动起来、首尾帧、锁脸、换装、多参考图、角色连续、重绘、三视图或关键帧时，先读取 `reference-visibility-gate.md`。
- 用户画面涉及人脸、人物近景、特写、面部特写、锁脸、修脸、人物参考图、角色图、三视图、多视角时，读取 `face-integrity-check.md`。
- 用户反馈脸畸形、五官错位、脸上色块、黑斑、阴影怪、大面积黑色、皮肤假、皮肤塑料、蜡像感、肤色断层时，读取 `face-integrity-check.md` 与 `retake-failure-diagnosis.md`。


## V0.9.82 参考图上传后统一自检与重生建议规则

本 Skill 在 V0.9.82 中新增 `references/reference-intake-self-check.md`，把所有上传参考图后的图片规则合并为一个固定前置流程：先判断图片是否清晰可信，再判断人脸是否符合生理逻辑，再决定每张图如何作为参考使用，最后才执行 I2V 极简原则或参考图职责转移。

执行顺序：

```text
S2_REFERENCE_SCAN
  ↓
reference-intake-self-check.md：识别图片用途、主职责、关键区域和可读性
  ↓
reference-visibility-gate.md：判断人脸、服装、发型/发饰、背景、构图和首尾帧连接是否清晰
  ↓
face-integrity-check.md：检查人脸畸形、五官错位、异常色块、黑斑、死黑阴影和不符合生理逻辑的皮肤质感
  ↓
可用性决策：可直接用 / 部分可用需补写 / 异常需重建 / 建议重新生成参考图
  ↓
reference-transfer-contract.md：只把清晰可信的信息分配为职责
  ↓
output-length-mode-standard.md：再决定 I2V / R2V / FLF2V / IMAGE 输出格式
```

新增决策：

- 参考图清晰：可执行 I2V 极简原则，只写图片看不出来的动作、运镜、光线变化、动力学和保持约束。
- 参考图部分清晰：清晰部分可继承，不清晰部分必须补写。
- 参考图异常：异常色块、黑斑、死黑阴影、畸形结构、皮肤伪影不得继承，必须重建自然结构。
- 参考图多处不清晰：若人脸、服装、发型/发饰、背景/空间、构图/景别五类中三类及以上不可辨，或用户指定的主职责区域不可辨，应建议用户重新生成或上传更清晰的参考图。

触发关系：

- 只要用户上传图片、首帧、尾帧、人物图、服装图、发饰图、场景图、构图图、产品图或参考图，先读取 `reference-intake-self-check.md`。
- 用户要求图生视频、动起来、锁脸、换装、多图融合、角色连续、三视图、重绘、海报、首尾帧或关键帧时，先读取 `reference-intake-self-check.md`，再读取 `reference-transfer-contract.md`。
- 发现参考图关键区域过多不清晰、主职责区域不可辨、首尾帧严重不连续、人脸存在明显生理或肤色异常时，优先建议用户重新生成参考图；如果用户要求继续，则降低该图职责权重并补写不清晰区域。


长度原则：先判断模式和复杂度，再选择长度档位。压缩版约 80-180 中文字；快速视频版约 120-260 中文字；标准 8-15 秒视频约 500-1000 中文字；高控制多参考 / 首尾帧 / 复杂动力学视频约 1000-1600 中文字；只有用户明确要求详细分镜、shot list、storyboard 或拍摄方案时才超过 1600 字。15 秒视频默认 2-4 个镜头，锁脸、唱歌、口型、多人物或复杂动力学优先 2-3 个镜头，不再默认硬塞 5-7 个镜头。负面提示词约 120-300 中文字。

时间轴执行原则：多镜头视频必须写清镜头切点、机位、运镜、焦点、主体动作、景深或环境变化。若镜头包含人物，则人物动作、表情肢体联动、口型、人物面部光影、衣物饰品与环境动态、人物一致性等内容，统一按照《人物镜头强制覆盖规则》判断触发并补足。时间轴可以用自然语言段落呈现，不强制逐项列出固定字段，但每个镜头内部必须具有可执行动作、镜头目的和画面变化。

动力学执行原则：当镜头中出现发丝、布料、披帛、饰品、纱幔、竹叶、云雾、水面、烟、雨雪、火焰、粒子、道具接触、碰撞、重力、惯性或其他可动态元素时，必须通过《人物镜头强制覆盖规则》或动作合约判断触发。简单风 / 头发 / 衣料场景可读取 `references/seedance-wind-softbody-standard.md`；复杂动态必须读取 `references/physical-dynamics-standard.md`。负面故障统一归入【负面提示词】的“动力学类”，简单风动也可兼容写作“风力类 / 动力学类”。

正文提示词只写正向模型执行内容；负面、禁止、避免和故障描述放入【负面提示词】。如果目标平台没有独立负面提示词输入框，提示用户不要把负面段混入主提示词。

OpenAI image-family / GPT-image / image2 图片提示词默认输出自然语言段落，不输出 Midjourney、Stable Diffusion、ComfyUI、Flux 或 tag-soup 格式，也不默认拆成正负面提示词。若图片主体包含人物，则人物部分必须遵循《人物镜头强制覆盖规则》；若存在人物参考图，则同时遵循参考图一致性规则；若画面为人物中近景、近景或特写，则必须补足人物面部光影；若存在发丝、衣物、饰品或环境动态材质，则必须补足对应动态描述。图片提示词最终仍保持自然语言段落，不输出视频时间轴，除非用户明确要求关键帧序列或分镜。

## 错误 / 正确行为

错误：用户说“一个女孩在唱歌”，助手直接输出完整 8 秒视频提示词。

正确：用户说“一个女孩在唱歌”，助手进入复述确认阶段，判断为唱歌 / 舞台 / MV 类项目，说明信息完整度低，询问音乐风格、场景和是否对口型，不输出最终时间轴。

正确快捷：用户说“一个女孩在唱歌，直接生成，不用问”，助手自动补齐非核心参数，直接输出最终提示词，并确保时间轴完整可执行。


## 人物相关子规则定位

《人物镜头强制覆盖规则》是人物镜头的唯一顶层判断规则。以下 references 只作为具体写法和素材库，不再单独定义顶层强制项：

- `optimizer-v5/reference-fidelity-system.md`：用于人物参考图、定妆图、角色模板、三视图、多视角、首帧和尾帧的人物一致性实现。
- `optimizer-v5/character-sheet-continuity-system.md`：用于三视图、多视角、正面全身、角色设定图和后续角色连续性实现。
- `optimizer-v5/seedance-expression-motion-rules.md`：用于人物表情、口型、说唱表演和肢体联动的具体写法。
- `optimizer-v5/seedance-closeup-face-lighting-rules.md`：用于人物中近景、近景、特写和面部特写的人物面部光影写法。
- `optimizer-v5/seedance-closeup-face-lighting-library.md`：只作为面光预设库，单镜头最多选择一组，不得堆叠多组面光。
- `references/seedance-wind-softbody-standard.md`：用于风、发丝、布料、饰品、纱幔、云雾、水面等风场和柔体动力学实现。
- `references/physical-dynamics-standard.md`：用于雨雪、烟尘、火焰、粒子、液体、道具、碰撞、接触、重力、惯性、消散和光与动态介质互动。

执行顺序为：先由《人物镜头强制覆盖规则》判断是否触发，再读取对应子规则实现细节。

## references 读取规则

根据任务需要读取：core-workflow.md、restatement-stage-flow.md、project-type-rules.md、video-rules.md、classic-shot-library.md、templates.md、timeline-execution-rules.md、timeline-quality-gates.md、quality-control.md、reference-material-guide.md、shot-size-rules.md、final-prompt-purity.md、camera-movement-library.md、concert-live-mv-rules.md、reference-isolation-rules.md、script-learning-index.md、concert-performance-action-library.md、concert-shot-language-library.md、lighting-emotion-library.md、seedance2-concise-execution-standard.md、physical-dynamics-standard.md、seedance-wind-softbody-standard.md、sequence-state-capsule.md、reference-transfer-contract.md、retake-failure-diagnosis.md、directing-coherence-engine.md、motion-performance-contract.md、character-blocking-contract.md、lighting-intention-contract.md、pro-shot-continuity-contract.md、retake-iteration-protocol.md、model-behavior-diagnosis.md、prompt-budget-allocation.md、event-density-control.md、anti-slop-rewrite-library.md、camera-shot-contract.md、shot-scale-selection.md、camera-movement-selection.md、multishot-grammar-standard.md、shot-continuity-axis-rules.md、animation-camera-grammar.md、output-length-mode-standard.md、reference-intake-self-check.md、reference-visibility-gate.md、face-integrity-check.md。

涉及连续剧情、多段 MV、系列短剧、首尾帧续写、下一段继续时，读取 `sequence-state-capsule.md`。
涉及多参考图、锁脸换装、服装图、发饰图、场景图、动作图、构图图、首帧、尾帧或关键帧时，读取 `reference-transfer-contract.md`。
涉及提示词审查、重拍、失败复盘、用户反馈生成结果不对、脸不一致、动作怪、风向乱、连续性断裂时，读取 `retake-failure-diagnosis.md`。
涉及剧情、分镜、MV、AIMV、电影感、情绪表达、导演感、氛围感时，读取 `directing-coherence-engine.md`。
涉及人物动作、舞蹈、武打、走位、手部动作、产品动作、道具运动或物理动态时，读取 `motion-performance-contract.md`。
涉及风、发丝、布料、纱幔、竹叶、云雾、水面、雨雪、烟尘、火焰、粒子、液体、道具接触、碰撞、重力、惯性、消散或光与动态介质互动时，读取 `physical-dynamics-standard.md`。
涉及两人以上、群像、舞台、伴舞、对话、众人反应或角色站位时，读取 `character-blocking-contract.md`。
涉及光影、面光、月光、烛光、夕阳、灯笼、舞台光、产品光、色温、阴影或材质反光时，读取 `lighting-intention-contract.md`。
涉及专业分镜、镜头清单、广告片、MV 多镜头、首尾帧交接或连续镜头时，读取 `pro-shot-continuity-contract.md`。
涉及多次重拍、保留某版优点、只改一个问题、判断是否重跑时，读取 `retake-iteration-protocol.md`。
涉及模型不听话、参考图压过文字、提示词越长越乱、远景脸/手/小字崩、否定词反而召唤内容、连续生成漂移时，读取 `model-behavior-diagnosis.md`。
涉及复杂任务、多参考图、多人物、多镜头、锁脸和大动作冲突、提示词过长或需要分配控制重点时，读取 `prompt-budget-allocation.md`。
涉及一个镜头或 clip 中有过多动作、多个完成事件、多地点、复杂对白、首尾帧距离过大或未来剧情提前出现风险时，读取 `event-density-control.md`。
涉及电影感、高级感、氛围感、质感好、唯美、震撼、真实感、动感、大片感、8K、masterpiece、不要AI感、不要塑料等空泛词或图像模型词时，读取 `anti-slop-rewrite-library.md`。

涉及简短版、压缩版、图生视频、首尾帧过渡、视频续写、图片生成、海报、角色图、三视图、输出字数控制或提示词压缩时，读取 `output-length-mode-standard.md`。
涉及上传图片、首帧、尾帧、人物图、服装图、发饰图、场景图、构图图、产品图或参考图时，读取 `reference-intake-self-check.md`，先完成上传后统一自检，再判断图片如何使用。
涉及参考图清晰度、图片可识别性、主职责区域是否可辨、是否建议重新生成参考图或 I2V 是否能省略图片已有内容时，读取 `reference-visibility-gate.md`。
涉及人脸、锁脸、人物近景、特写、面部特写、脸畸形、五官错位、脸上色块、黑斑、异常阴影、大面积黑色、皮肤假、塑料皮肤、蜡像感、肤色断层时，读取 `face-integrity-check.md`。
涉及参考图、真实摄影、OpenAI image-family、Seedance 语序权重、表情动作、面光、景深、运镜转场或工业化分镜时，优先读取 `optimizer-v5/` 下的对应规则文件；这些规则作为视觉执行层，不替代本 Skill 的确认流程、时间轴结构和最终交付格式。

## 维护注意事项

- 当前最终视频提示词权威标准是《人物镜头强制覆盖规则》、`references/seedance2-concise-execution-standard.md`、`references/physical-dynamics-standard.md`、`references/seedance-wind-softbody-standard.md` 和 `templates/video-prompt-template.md`。
- 旧的三板块视频模板已废弃，不得作为最终输出结构。
- `timeline-execution-rules.md` 和 `timeline-quality-gates.md` 只作为镜头执行覆盖与质量检查，不要求最终提示词逐项列出字段。
- 修改最终输出格式、人物镜头规则或动力学规则时必须同步检查并更新：`SKILL.md`、`templates/video-prompt-template.md`、`references/seedance2-concise-execution-standard.md`、`references/physical-dynamics-standard.md`、`references/seedance-wind-softbody-standard.md`、`references/motion-performance-contract.md`、`references/lighting-intention-contract.md`、`references/pro-shot-continuity-contract.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`docs/output-format.md`、`scripts/prompt_checker.py`。
- 修改连续片段、多参考图职责或重拍修复规则时，必须同步检查并更新：`SKILL.md`、`references/sequence-state-capsule.md`、`references/reference-transfer-contract.md`、`references/retake-failure-diagnosis.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`scripts/prompt_checker.py`。
- 连续片段状态胶囊只管理多段状态，不替代人物镜头强制覆盖规则。
- 参考图职责转移契约只管理参考图各自控制什么，不替代人物锁脸和角色一致性规则。
- 重拍失败诊断只负责失败归因和修复路径，不改变最终输出结构。
- 修改导演一致性、动作表演、多人物调度、光影意图、专业镜头连续或重拍迭代规则时，必须同步检查并更新：`SKILL.md`、`references/directing-coherence-engine.md`、`references/motion-performance-contract.md`、`references/character-blocking-contract.md`、`references/lighting-intention-contract.md`、`references/pro-shot-continuity-contract.md`、`references/retake-iteration-protocol.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`scripts/prompt_checker.py`。
- V0.9.76 导演执行融合层只增强镜头意图、动作落点、多人调度、光影动机和重拍策略，不替代人物镜头强制覆盖规则、参考图职责转移契约、连续片段状态胶囊或最终输出结构。
- 修改人物镜头相关规则时，必须优先检查并同步更新：《人物镜头强制覆盖规则》、`optimizer-v5/reference-fidelity-system.md`、`optimizer-v5/character-sheet-continuity-system.md`、`optimizer-v5/seedance-expression-motion-rules.md`、`optimizer-v5/seedance-closeup-face-lighting-rules.md`、`references/seedance-wind-softbody-standard.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`scripts/prompt_checker.py`。
- `optimizer-v5/` 负责视觉执行细节；当其模板与当前最终输出标准冲突时，以当前标准为准。
- 修改模型机制、提示词预算、事件密度或反空泛词规则时，必须同步检查并更新：`SKILL.md`、`references/model-behavior-diagnosis.md`、`references/prompt-budget-allocation.md`、`references/event-density-control.md`、`references/anti-slop-rewrite-library.md`、`references/quality-control.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`scripts/prompt_checker.py`。
- V0.9.78 模型机制与预算层只负责判断为什么失败、预算该花在哪里、当前 clip 能承载多少事件、空泛词如何改写，不替代人物镜头强制覆盖规则、导演执行融合层、物理动力学总规则或最终输出结构。
- 修改镜头语言、景别、运镜、多镜头语法、轴线连续或动画镜头语法时，必须同步检查并更新：`SKILL.md`、`references/camera-shot-contract.md`、`references/shot-scale-selection.md`、`references/camera-movement-selection.md`、`references/multishot-grammar-standard.md`、`references/shot-continuity-axis-rules.md`、`references/animation-camera-grammar.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/pro-shot-continuity-contract.md`、`references/quality-control.md`、`templates/video-prompt-template.md`、`scripts/prompt_checker.py`。
- V0.9.79 镜头语言层只负责让景别、机位、运镜、切点和轴线适配内容，不替代人物镜头强制覆盖规则、导演一致性、提示词预算、事件密度、物理动力学或最终输出结构。
- 修改输出长度档位、模式优先判断、I2V 极简原则或图片 / 视频格式边界时，必须同步检查并更新：`SKILL.md`、`references/output-length-mode-standard.md`、`templates/video-prompt-template.md`、`docs/output-format.md`、`references/seedance2-concise-execution-standard.md`、`references/quality-control.md`、`scripts/prompt_checker.py`。
- V0.9.80 输出长度与模式层只负责选择格式、长度和 I2V 极简策略，不替代人物镜头强制覆盖、参考图职责转移、镜头语言、物理动力学或最终视频双段结构。
- 修改参考图可识别性、人脸完整性、I2V 省略规则、锁脸清晰度或面部异常修复规则时，必须同步检查并更新：`SKILL.md`、`references/reference-intake-self-check.md`、`references/reference-visibility-gate.md`、`references/face-integrity-check.md`、`references/reference-transfer-contract.md`、`references/output-length-mode-standard.md`、`references/retake-failure-diagnosis.md`、`references/quality-control.md`、`templates/video-prompt-template.md`、`docs/output-format.md`、`scripts/prompt_checker.py`。
- V0.9.81 参考图可识别性与人脸完整性层只负责判断图片里哪些信息能信任、哪些必须补写、哪些异常不得继承；它不替代参考图职责转移契约、人物镜头强制覆盖规则、面光规则或最终输出结构。
- V0.9.82 参考图上传后统一自检层只负责在参考图进入职责分配前判断图片可用性、是否需要补写、是否建议重新生成；它不替代用户明确指令、参考图职责契约或最终输出结构。
- 版本发布时更新 `VERSION`、`README.md` 和 `CHANGELOG.md`。
