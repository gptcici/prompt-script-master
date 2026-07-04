---
name: prompt-script-master
description: use this skill when the user wants to create, review, optimize, or convert ideas into structured chinese ai video scripts and prompts, especially for Seedance 2.0/2.1 full-reference workflows, AIMV, MV, concert/live-stage, singing, dance, story shorts, first-frame/last-frame transitions, storyboard prompts, OpenAI image-family keyframes, and prompt audits. use prompt-optimizer V5 rules as the primary visual, reference-fidelity, photorealism, character-continuity, Seedance expression, lighting, depth, camera-transition, and industrial-storyboard rule source; use prompt-script-master rules as the primary confirmation, timeline, MV structure, and script delivery framework. all library content is abstract reference only and must never appear literally in generated outputs.
---

# 提示词脚本大师

## 参考库隔离最高规则

所有 references/ 中的拆解、动作库、分镜库、灯光库和案例库，以及各规则文件中的所有示例（⚠️ 标记或代码块中的文本），**只能作为内部导演方法参考，严禁直接照搬到生成的提示词中**。最终生成脚本或提示词不得出现参考库里的真实人物、艺人、视频名、文件名、原始时间戳、歌词、字幕、水印、logo、专属桥段、具体道具组合或来源痕迹。规则中的模板仅参考结构和格式，实际内容必须根据用户的场景、人物、光源独立创作。

**锚点光源强制规则**：每条提示词必须确立唯一锚点光源（类型+方向+位置三要素齐全），所有人物面光、环境光影、阴影、轮廓光必须从该锚点光源推导，禁止出现第二个不相关的主光源。具体规则见 `references/anchor-light-source-rule.md`。

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
- 同时包含【正文提示词】【时间轴分段】【负面提示词】的成品结构

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

当用户明确授权快捷生成时，直接输出最终提示词。最终提示词必须纯净，只包含模型执行内容，不包含解释、复述、确认问题、选择项、"我建议""你可以""是否采用"、动作库名称或经典镜头库名称。

快捷生成时允许自动补齐时长、画幅、场景、灯光、镜头、动作、情绪等非核心专业参数。

最终提示词必须分为「正文提示词」和「负面提示词」两部分输出。正文只写正向描述，不得出现"禁止、不要、避免、不得"类词汇；所有禁止项统一放在负面提示词中。

## 最终提示词结构

最终提示词统一分为「正文提示词」和「负面提示词」两部分（详见 `templates/video-prompt-template.md`）。单镜头和多镜头使用同一结构，唯一区别是时间轴分段数量：单镜头 = 1 段，多镜头 = n 段。

> **旧版三段式（全程总定调/时间轴分段/全局收尾）已废弃。** 禁止使用旧版结构。

### 正文提示词语序权重（黄金优先级，绝对不能乱）

按权重从高到低排列，顺序固定：

1. **第一梯队（开头最高权重）**：视频基础规格 + 全程运镜总基调 + 参考图标准化指令（@Image1 格式） + 人物核心外形特征
2. **第二梯队**：整体场景总设定（一句话概括大环境与核心元素）
3. **第三梯队**：时间轴分段叙事
4. **第四梯队（末尾最低权重）**：整体风格质感 + 正向全局一致性约束

**最强格式规则，必须执行**：第一梯队中，参考图指令之后必须立刻写人物核心外形特征，不得被环境、氛围、道具、色调或情绪描述隔开。人物权重永远高于环境。

### 无效语义清理规则（必须执行）

最终提示词中不得出现以下非视觉化描述，必须全部转化为可被画面呈现的具象内容：

- **导演创作思路类**（如"延续上一镜头的空间关系""形成天地开阔的推进感"）→ 只保留景别、运镜、焦点变化等具象结果
- **心理感受类**（如"像被云光吸引""有进入圣地般的仪式感"）→ 转化为"头部微抬""步伐轻柔克制"等可视动作
- **逻辑说明类**（如"体现角色从封闭到开阔的心境变化"）→ 只保留景深释放、空间展开等视觉变化

### 同类信息聚合规则（必须执行）

相同维度的内容必须集中描述，禁止分散在全文重复提及：

- **人物衣发动态**：统一跟在人物动作之后，集中描述风带动的发丝、衣袖、裙摆、披帛、珠链等
- **光影效果**：统一放在动作之后、环境之前，先人物面光/轮廓光，再环境光影
- **景深变化**：统一放在每段末尾，明确说明焦点位置和虚实变化

### 参考图标准化指令

人物参考图必须使用固定 @Image 格式，放在人物核心外形特征之前：

```text
@Image1 仅作为人物强参考，锁定五官、发型、发饰、服装款式与[气质]，不作为首帧，不参考原图构图背景，全程为同一位[角色身份]，不生成通用AI模特脸。
```

禁止使用"上传定妆图作为参考""锁定参考图角色"等模糊描述。

### 时间轴分段格式

`【时间轴分段】` 中，每一段按固定顺序书写以下 7 项，连成一整段自然语言，禁止拆成冒号字段列表：

```text
景别 + 运镜状态 + 人物核心动作 + 衣发纱幔动态 + 人物光影 + 环境细节 + 景深变化
```

首段需要建立人物主体和关键外形特征；后续段落只写本段变化，保持人物连续性，不重复首段已经建立的角色外貌。

人物光影必须从锚点光源推导（见 `anchor-light-source-rule.md`），按光源方向→骨骼高光点位（鼻梁/眉骨/颧骨/下颌线等）→暗部过渡→整体质感顺序书写。触发条件、分机位点位库、禁写条款见 `seedance-closeup-face-lighting-rules.md`。

### 权重标记规则

权重标记遵循 S/A/B 三级分层体系，详见 `seedance-prompt-order-rules.md` 权重规范标准化章节：

- S 级（1.15-1.25）：核心人物面部特征、身份标识物，单段最多 1-2 个，全文 ≤ 3 个
- A 级（1.1-1.15）：材质质感、关键光影效果、核心服饰细节，单段最多 1 个，全文 ≤ 4 个
- B 级（1.05-1.1）：环境氛围、非核心装饰，尽量不用
- 全局红线：所有权重 ≤ 1.3
- 禁止：给人/给负面描述加权、同一个词重复加权、环境权重大于人物权重

### 负面提示词

所有禁止项、负面规避描述必须从正文完全剥离，统一放到独立的「负面提示词」模块。正文只写正向描述，绝对不出现"禁止、不要、避免、不得"类词汇。

负面提示词按类别罗列：人物类（脸部变形、五官漂移、发型错乱…）、动作类（肢体错乱、手部畸形…）、场景类（空间跳跃错位、纱幔无重力漂浮…）、风格类（过度磨皮、过度CG感、卡通插画感…）、技术类（运镜抖动、景别突变…）。

### 时间轴规则权威来源声明

`references/timeline-execution-rules.md` 和 `references/timeline-quality-gates.md` 是时间轴分段规则的唯一权威来源。时间轴每段必含上述 7 项，格式以本文件为准。

> **旧版 9 项格式（本段景别 + 本段运镜状态 + 焦点变化 + 核心动作 + 表情肢体联动 + 人物面光/骨骼光影 + 环境光影变化 + 环境细节补充 + 本段景深变化）已废弃。** 禁止使用旧版 9 项格式。

OpenAI image-family / GPT-image / image2 图片提示词默认输出自然语言段落，不输出 Midjourney、Stable Diffusion、ComfyUI、Flux 或 tag-soup 格式，也不默认拆成正向栏与否定栏。图片提示词必须包含参考图角色、主体身份、场景动作、真实光源、镜头构图、材质行为、摄影真实感和一致性要求。

## 错误 / 正确行为

错误：用户说“一个女孩在唱歌”，助手直接输出完整 8 秒视频提示词。

正确：用户说“一个女孩在唱歌”，助手进入复述确认阶段，判断为唱歌 / 舞台 / MV 类项目，说明信息完整度低，询问音乐风格、场景和是否对口型，不输出最终时间轴。

正确快捷：用户说“一个女孩在唱歌，直接生成，不用问”，助手自动补齐非核心参数，直接输出最终提示词，并确保时间轴完整可执行。

## references 读取规则

根据任务需要读取：core-workflow.md、restatement-stage-flow.md、project-type-rules.md、video-rules.md、classic-shot-library.md、templates.md、timeline-execution-rules.md、timeline-quality-gates.md、quality-control.md、reference-material-guide.md、shot-size-rules.md、final-prompt-purity.md、camera-movement-library.md、concert-live-mv-rules.md、reference-isolation-rules.md、script-learning-index.md、concert-performance-action-library.md、concert-shot-language-library.md、lighting-emotion-library.md。

涉及参考图、真实摄影、OpenAI image-family、Seedance 语序权重、表情动作、面光、景深、运镜转场或工业化分镜时，优先读取 `optimizer-v5/` 下的对应规则文件；这些规则作为视觉执行层，不替代本 Skill 的确认流程、时间轴结构和最终交付格式。

## 维护注意事项

- 编辑 `references/` 下的任何 `.md` 文件时，必须同步覆盖 `skill/prompt-script-master/references/` 快照副本，否则会造成规则不一致。
- ⚠️ **示例隔离铁律**：在任意规则文件中新增或编辑示例、模板、范例文本（包括代码块中的提示词片段）时，必须在该示例前添加 ⚠️ 免责声明，明确标注"仅供参考格式和写作手法，严禁直接照搬内容"。漏加声明会导致未来 session 的 agent 直接把示例文本复制到生成提示词中，造成严重的规则污染。声明格式：`> ⚠️ **以下[模板/示例/范例]仅用于参考[格式结构/写作手法/权重用法]，严禁直接照搬[具体内容/场景设定/人物身份/光影描述]。**`
- ⚠️ **快照 SKILL.md 已删除**：`skill/prompt-script-master/SKILL.md` 已删除以消除与主 `SKILL.md` 的 `name` 字段歧义（两者同名会导致 `skill_view` 拒绝加载）。快照同步时**不得**将 `SKILL.md` 复制到快照目录。详细同步规程见 `references/snapshot-sync-procedure.md`。
- 重大规则变更或用户要求自检时，按 `references/self-audit-procedure.md` 执行三步审计（旧规则残留扫描→跨文件冲突检查→引用链路完整性），确保无残留/冲突/断链。
- 时间轴规则的唯一权威来源是 `references/timeline-execution-rules.md` 和 `references/timeline-quality-gates.md`。其 7 项分段格式（景别 + 运镜状态 + 人物核心动作 + 衣发纱幔动态 + 人物光影 + 环境细节 + 景深变化）基于 Seedance 权重逻辑优化，是时间轴分段的唯一标准。其中「人物光影」项的具体书写规范（光源锚定、分机位点位库、一致性四步校验、结构化顺序、禁写条款）的唯一权威来源是 `references/optimizer-v5/seedance-closeup-face-lighting-rules.md`。权重标记的分层体系（S/A/B 三级、使用频率上限、禁止项）的权威来源是 `references/optimizer-v5/seedance-prompt-order-rules.md`（权重规范标准化章节）。
- > **旧版 9 项格式已废弃。** 禁止在任何文件中使用或引用旧版 9 项格式。
- ⚠️ 格式变更联动清单：当输出结构（三段式⇄两段式）或时间轴格式（7 项字段）发生变更时，必须同步更新以下 **全部文件**并覆盖快照副本：
  1. `SKILL.md`（最终提示词结构 & 维护注意事项）
  2. `templates/video-prompt-template.md`（输出模板）
  3. `references/timeline-execution-rules.md`（执行规则）
  4. `references/timeline-quality-gates.md`（质量门控）
  5. `references/templates.md`（结构参考）
  6. `references/video-rules.md`（视频规则）
  7. `references/quality-control.md`（质量控制清单）
  8. `references/optimizer-v5/output-templates.md`（V5 输出模板）
  9. `scripts/prompt_checker.py`（校验逻辑）
  10. `scripts/prompt_wizard.py`（向导输出模板）
  11. `docs/output-format.md`（输出格式文档）
  12. `docs/seedance2-full-reference.md`（Seedance 参考文档）
  13. `docs/golden-tests.md`（全局通过标准 & 测试用例）
  14. `README.md`（功能描述）
  15. `references/optimizer-v5/seedance-closeup-face-lighting-rules.md`（人物光影→面光规范联动）
  16. `references/optimizer-v5/seedance-prompt-order-rules.md`（权重规范标准化章节→S/A/B 三级体系联动）
  17. `references/anchor-light-source-rule.md`（锚点光源强制规则→所有光影规则的"唯一圆心"）
  **全部更新后**按 `references/snapshot-sync-procedure.md` 同步快照（`skill/prompt-script-master/` 下对应路径），但排除 `SKILL.md`（快照中已删除以避免 `name` 歧义）。快照同步切勿遗漏 `docs/` 和 `references/optimizer-v5/` 子目录。

  ⚠️ **快照同步工具限制**：`skill_manage` 的 `write_file` 和 `patch` 仅支持在技能自身的 `assets/`、`references/`、`scripts/`、`templates/` 子目录下操作，不支持 `docs/` 子目录和 `skill/prompt-script-master/` 快照嵌套路径。同步 `docs/` 和快照副本必须通过 `terminal` 执行 `cp` 命令。
- ⚠️ `optimizer-v5/seedance-prompt-order-rules.md` 的 Timeline splitting / 时间轴适配规则**已降级为非权威参考**（7 项格式是本目录唯一标准），但其「权重规范标准化」章节是权重标记的**唯一权威来源**。`optimizer-v5/seedance-camera-movement-transition-rules.md` 同理降级。
- ⚠️ **锚点光源强制规则**：`references/anchor-light-source-rule.md` 是技能级约束层规则——不包含具体面光/环境光写法，唯一作用是确保每条提示词先确立锚点光源，所有其他光影规则（面光、骨骼光影、环境光、权重）生成前必须先对齐锚点。本规则不修改任何现有光影规则文件的内部内容，仅要求生成时以锚点为"唯一圆心"推导。
- ⚠️ **分段触发规则**（S8 阶段）：视频时长 > 5 秒且用户未声明"一镜到底"时，必须执行以下 4 步再生成时间轴：（1）**询问用户**是否需要分段；（2）**不定长分配**——不套用固定模板，根据每段内容权重合理分配时长；（3）**自行检查**——分配后自检动作密度匹配、总时长加总、段间推进逻辑；（4）**确认后继续**——将分段方案和时长展示给用户确认，确认后再写入 7 项格式的时间轴内容。用户明确要求一镜到底时跳过此步骤。
