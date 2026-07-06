---
name: prompt-script-master
description: use this skill when the user wants to create, review, optimize, or convert ideas into structured chinese ai video scripts and prompts, especially for Seedance 2.0/2.1 full-reference workflows, AIMV, MV, concert/live-stage, singing, dance, story shorts, first-frame/last-frame transitions, storyboard prompts, OpenAI image-family keyframes, and prompt audits. use prompt-optimizer V5 rules as the primary visual, reference-fidelity, photorealism, character-continuity, Seedance expression, lighting, depth, camera-transition, and industrial-storyboard rule source; use prompt-script-master rules as the primary confirmation, timeline, MV structure, and script delivery framework. all library content is abstract reference only and must never appear literally in generated outputs.
---

# 提示词脚本大师

## 当前版本：V0.9.74

默认最终视频提示词标准为“中等精简 + 强锚点 + 镜头化时间轴”。所有最终视频提示词使用【正文提示词】+【负面提示词】，旧的三板块视频模板不再作为输出格式。涉及人物主体时，必须先执行“人物镜头强制覆盖规则”；涉及风、发丝、布料、纱幔、竹叶、云雾、水面等动态材质时，必须通过该人物规则判断触发，并使用“全局风向 / 柔体动力学锚点”。

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
总设定 + 参考图职责 + 全局光源锚点 + 全局风向 / 柔体动力学锚点 + 镜头时间轴 + 全局一致性

【负面提示词】
人物类 + 动作类 + 风力类 + 场景类 + 风格类
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

如果画面中存在发丝、碎发、长发、披帛、轻纱、袖口、衣摆、裙摆、丝带、珠链、流苏、耳坠、发簪垂饰、纱幔、帘幕、旗帜、帐幔、竹叶、树叶、草、花瓣、灰尘、雪、雨、云雾、烟、香火、水面、涟漪或浪花，必须加入动态描述。动态必须服从统一的全局风向或动作惯性，不得让头发、衣物、饰品和环境朝冲突方向运动。必须区分材质重量和响应速度：发丝、碎发、细丝带响应最快；轻纱、披帛、宽袖可鼓起、拉伸、翻卷、回落；厚重衣身和外袍主体响应较慢；珠链、流苏、发饰小幅延迟摆动；云雾、水面、远景环境变化更慢；所有动态都应具有延迟、惯性、回弹和重力。

如果画面没有明显可动态材质，也没有风、动作惯性或环境流动，不强制加入风动模块。

### F. 人物一致性：参考图条件必选

如果用户提供人物参考图、定妆图、角色模板、三视图、多视角、首帧或尾帧，必须优先锁定人物身份，包括脸型比例、五官气质、眼神感觉、鼻唇印象、发型长度与层次、发色细节、年龄感、妆容、身体比例和身份气质。不得为了风格化、美化、氛围感、古风感、电影感或舞台感，把人物替换成另一个通用 AI 模特脸。

### G. 非触发模块不得硬写

人物镜头规则是条件触发，不是无条件堆叠。远景背影人物不强制写鼻梁高光、眼神光或口型；无说话 / 无唱歌 / 无对口型不强制写口型；无风、无明显动态材质、无环境流动不强制写风动；极短过渡镜头只保留最关键的人物动作和镜头目的；群像远景优先写群体动作、队形、节奏和环境，不逐个写面部细节。

### H. 负面提示词归位

正文只写正向执行目标。人物崩坏、口型崩坏、脸型漂移、动作卡顿、风向混乱、布料无重量感、面部平光、死黑无细节、塑料皮肤、无眼神光等故障项，统一写入【负面提示词】对应类别，不得混入正文。如果最终输出格式只允许一个【负面提示词】段落，可将人物类、动作类、风力类、面光类、场景类、风格类合并为紧凑列表。


长度原则：不要极简，也不要写成超长导演说明书。15 秒多镜头视频的正文优先控制在约 1200-1800 中文字，负面提示词约 120-300 中文字，通常 5-7 个镜头，每个镜头 2-4 句。用户明确要求更详细时可以增加，但不得重复堆叠同类信息。

时间轴执行原则：多镜头视频必须写清镜头切点、机位、运镜、焦点、主体动作、景深或环境变化。若镜头包含人物，则人物动作、表情肢体联动、口型、人物面部光影、衣物饰品与环境动态、人物一致性等内容，统一按照《人物镜头强制覆盖规则》判断触发并补足。时间轴可以用自然语言段落呈现，不强制逐项列出固定字段，但每个镜头内部必须具有可执行动作、镜头目的和画面变化。

风动执行原则：当镜头中出现发丝、布料、披帛、饰品、纱幔、竹叶、云雾、水面、烟、雨雪或其他可动态材质时，必须通过《人物镜头强制覆盖规则》判断触发，并以 `references/seedance-wind-softbody-standard.md` 作为具体实现标准。顶层规则只负责触发条件与覆盖要求；具体风场、材质重量、响应速度、延迟、回弹和负面风力类故障词，以风动标准为准。

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
- `references/seedance-wind-softbody-standard.md`：用于发丝、布料、饰品、纱幔、云雾、水面等动态材质的风场和柔体动力学实现。

执行顺序为：先由《人物镜头强制覆盖规则》判断是否触发，再读取对应子规则实现细节。

## references 读取规则

根据任务需要读取：core-workflow.md、restatement-stage-flow.md、project-type-rules.md、video-rules.md、classic-shot-library.md、templates.md、timeline-execution-rules.md、timeline-quality-gates.md、quality-control.md、reference-material-guide.md、shot-size-rules.md、final-prompt-purity.md、camera-movement-library.md、concert-live-mv-rules.md、reference-isolation-rules.md、script-learning-index.md、concert-performance-action-library.md、concert-shot-language-library.md、lighting-emotion-library.md、seedance2-concise-execution-standard.md、seedance-wind-softbody-standard.md。

涉及参考图、真实摄影、OpenAI image-family、Seedance 语序权重、表情动作、面光、景深、运镜转场或工业化分镜时，优先读取 `optimizer-v5/` 下的对应规则文件；这些规则作为视觉执行层，不替代本 Skill 的确认流程、时间轴结构和最终交付格式。

## 维护注意事项

- 当前最终视频提示词权威标准是《人物镜头强制覆盖规则》、`references/seedance2-concise-execution-standard.md`、`references/seedance-wind-softbody-standard.md` 和 `templates/video-prompt-template.md`。
- 旧的三板块视频模板已废弃，不得作为最终输出结构。
- `timeline-execution-rules.md` 和 `timeline-quality-gates.md` 只作为镜头执行覆盖与质量检查，不要求最终提示词逐项列出字段。
- 修改最终输出格式或人物镜头规则时必须同步检查并更新：`SKILL.md`、`templates/video-prompt-template.md`、`references/seedance2-concise-execution-standard.md`、`references/seedance-wind-softbody-standard.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`docs/output-format.md`、`scripts/prompt_checker.py`。
- 修改人物镜头相关规则时，必须优先检查并同步更新：《人物镜头强制覆盖规则》、`optimizer-v5/reference-fidelity-system.md`、`optimizer-v5/character-sheet-continuity-system.md`、`optimizer-v5/seedance-expression-motion-rules.md`、`optimizer-v5/seedance-closeup-face-lighting-rules.md`、`references/seedance-wind-softbody-standard.md`、`references/timeline-execution-rules.md`、`references/timeline-quality-gates.md`、`references/quality-control.md`、`scripts/prompt_checker.py`。
- `optimizer-v5/` 负责视觉执行细节；当其模板与当前最终输出标准冲突时，以当前标准为准。
- 版本发布时更新 `VERSION`、`README.md` 和 `CHANGELOG.md`。
