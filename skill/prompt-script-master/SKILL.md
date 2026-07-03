---
name: prompt-script-master
description: use this skill when the user wants to create, review, optimize, or convert ideas into structured chinese ai video scripts and prompts, especially for Seedance 2.0/2.1 full-reference workflows, AIMV, MV, concert/live-stage, singing, dance, story shorts, first-frame/last-frame transitions, storyboard prompts, OpenAI image-family keyframes, and prompt audits. use prompt-optimizer V5 rules as the primary visual, reference-fidelity, photorealism, character-continuity, Seedance expression, lighting, depth, camera-transition, and industrial-storyboard rule source; use prompt-script-master rules as the primary confirmation, timeline, MV structure, and script delivery framework. all library content is abstract reference only and must never appear literally in generated outputs.
---

# 提示词脚本大师

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

最终提示词统一采用三段式结构（详见 `templates/video-prompt-template.md`）。单镜头和多镜头使用同一结构，唯一区别是时间轴分段数量：单镜头 = 1 段，多镜头 = n 段。

**最强格式规则，必须执行**：镜头框架之后，立刻锁死人物 + 参考图；人物核心外形特征必须紧跟参考图角色锁定，不得被环境、氛围、道具、色调或情绪描述隔开。人物权重永远高于环境。

**强制面部光影规则，必须执行**：任何情况下，只要提示词描述到角色面部、眼神、表情、眨眼、侧脸、三分之二脸、皮肤、鼻梁、颧骨、下颌线或其他可见面部区域，必须加入人物面光/骨骼细节。可结合当前内容、氛围、人物参考图和风格，调用 `optimizer-v5` 光影库与 `lighting-emotion-library.md` 作为内部参考，再改写成具体可拍摄的面部光影描述。

```text
【全程总定调】
镜头总基调 + 镜头框架
参考图角色精准锁定
人物核心外形特征
整体场景总设定

【时间轴分段】
本段景别 + 本段运镜状态 + 焦点变化 + 核心动作 + 表情肢体联动 + 人物面光/骨骼光影 + 环境光影变化 + 环境细节补充 + 本段景深变化

【全局收尾】
整体风格质感
全局一致性约束
```

**时间轴规则权威来源声明**：`references/timeline-execution-rules.md` 和 `references/timeline-quality-gates.md` 是时间轴分段规则的唯一权威来源。时间轴每段必含上述 9 项，格式以本文件为准。

OpenAI image-family / GPT-image / image2 图片提示词默认输出自然语言段落，不输出 Midjourney、Stable Diffusion、ComfyUI、Flux 或 tag-soup 格式，也不默认拆成正向栏与否定栏。图片提示词必须包含参考图角色、主体身份、场景动作、真实光源、镜头构图、材质行为、摄影真实感和一致性要求。

## 错误 / 正确行为

错误：用户说“一个女孩在唱歌”，助手直接输出完整 8 秒视频提示词。

正确：用户说“一个女孩在唱歌”，助手进入复述确认阶段，判断为唱歌 / 舞台 / MV 类项目，说明信息完整度低，询问音乐风格、场景和是否对口型，不输出最终时间轴。

正确快捷：用户说“一个女孩在唱歌，直接生成，不用问”，助手自动补齐非核心参数，直接输出最终提示词，并确保时间轴完整可执行。

## references 读取规则

根据任务需要读取：core-workflow.md、restatement-stage-flow.md、project-type-rules.md、video-rules.md、classic-shot-library.md、templates.md、timeline-execution-rules.md、timeline-quality-gates.md、quality-control.md、reference-material-guide.md、shot-size-rules.md、final-prompt-purity.md、camera-movement-library.md、concert-live-mv-rules.md、reference-isolation-rules.md、script-learning-index.md、concert-performance-action-library.md、concert-shot-language-library.md、lighting-emotion-library.md。

涉及参考图、真实摄影、OpenAI image-family、Seedance 语序权重、表情动作、面光、景深、运镜转场或工业化分镜时，优先读取 `optimizer-v5/` 下的对应规则文件；这些规则作为视觉执行层，不替代本 Skill 的确认流程、时间轴结构和最终交付格式。

## 维护注意事项

- 编辑 `references/` 下的任何 `.md` 文件时，如果存在 `skill/prompt-script-master/references/` 快照副本，必须同步覆盖，否则会造成规则不一致。
- 时间轴规则的唯一权威来源是 `references/timeline-execution-rules.md` 和 `references/timeline-quality-gates.md`。其 9 项分段格式（本段景别 + 本段运镜状态 + 焦点变化 + 核心动作 + 表情肢体联动 + 人物面光/骨骼光影 + 环境光影变化 + 环境细节补充 + 本段景深变化）基于黄金语序适配，是时间轴分段的唯一标准。
- ⚠️ 时间轴格式变更联动清单：修改时间轴规则时必须同步更新以下 **6 个文件**并覆盖快照副本：
  1. `references/timeline-execution-rules.md`（执行规则）
  2. `references/timeline-quality-gates.md`（质量门控）
  3. `SKILL.md`（权威来源声明 & 维护注意事项）
  4. `README.md`（功能描述）
  5. `docs/golden-tests.md`（全局通过标准 & 5 条测试用例）
  6. `scripts/prompt_checker.py`（校验逻辑 & 提示词库）
  **全部更新后**必须 `cp` 至 `skill/prompt-script-master/` 对应路径同步快照。
- ⚠️ `optimizer-v5/seedance-prompt-order-rules.md` 和 `optimizer-v5/seedance-camera-movement-transition-rules.md` 的 Timeline splitting / 时间轴适配规则**已降级为非权威参考**，不得作为时间轴分段格式的决策依据。黄金语序（12 模块整体提示词结构）仍由 Seedance 文件定义，但时间轴分段格式的唯一标准是本目录下的 9 项格式。
- ⚠️ **分段触发规则**（S8 阶段）：视频时长 > 5 秒且用户未声明"一镜到底"时，必须执行以下 4 步再生成时间轴：（1）**询问用户**是否需要分段；（2）**不定长分配**——不套用固定模板，根据每段内容权重合理分配时长；（3）**自行检查**——分配后自检动作密度匹配、总时长加总、段间推进逻辑；（4）**确认后继续**——将分段方案和时长展示给用户确认，确认后再写入 9 项格式的时间轴内容。用户明确要求一镜到底时跳过此步骤。
