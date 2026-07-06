# 提示词脚本大师 (Prompt Script Master) V0.9.82

导演助理式的 AI 视频提示词生成 Skill，为 Seedance 2.0/2.1、OpenAI image-family 等模型提供结构化的中文视频脚本与提示词。

## 项目结构

```text
prompt-script-master/
├── SKILL.md                          # Skill 主入口
├── agents/openai.yaml                # Agent 配置
├── scripts/                          # 工具脚本
│   ├── prompt_checker.py             # 提示词校验
│   ├── prompt_exporter.py            # 提示词导出
│   └── prompt_wizard.py              # 提示词向导
├── references/                       # 核心规则库
│   ├── core-workflow.md              # 核心工作流
│   ├── restatement-stage-flow.md     # 复述阶段流程
│   ├── project-type-rules.md         # 项目类型规则
│   ├── video-rules.md                # 视频规则
│   ├── quality-control.md            # 质量控制
│   ├── reference-material-guide.md   # 用户上传参考素材指南
│   ├── reference-isolation-rules.md  # 参考库隔离规则
│   ├── templates.md                  # 模板库
│   ├── examples-guide.md             # 案例库指南
│   ├── script-learning-index.md      # 脚本学习索引
│   ├── confirmation-gate.md          # 确认门控
│   ├── dynamic-level-guide.md        # 动态级别指南
│   ├── final-prompt-purity.md        # 最终提示词纯净性
│   ├── shot-size-rules.md            # 景别规则
│   ├── classic-shot-library.md       # 经典镜头库
│   ├── concert-live-mv-rules.md      # 演唱会/Live MV规则
│   ├── concert-performance-action-library.md  # 演唱会表演动作库
│   ├── concert-shot-language-library.md       # 演唱会镜头语言库
│   └── lighting-emotion-library.md            # 灯光情绪库
├── references/optimizer-v5/         # Prompt Optimizer V5 视觉规则
│   ├── task-routing.md               # 任务路由
│   ├── output-templates.md           # 输出模板
│   ├── model-adapters.md             # 模型适配器
│   ├── command-system.md             # 命令系统
│   ├── conversation-edit-flow.md     # 对话编辑流
│   ├── reference-fidelity-system.md  # 参考图一致性系统
│   ├── character-sheet-continuity-system.md  # 角色连续性
│   ├── realistic-photography-rules.md        # 真实摄影规则
│   ├── ai-image-generation-rules.md          # AI图像生成规则
│   ├── director-style-anchors.md             # 导演风格锚点
│   ├── cinematic-camera-language.md          # 电影摄影语言
│   ├── composition-space-structure.md        # 构图空间结构
│   ├── composition-reference-library.md      # 纯文本构图模式库
│   ├── seedance-prompt-order-rules.md        # Seedance 语序规则
│   ├── seedance-expression-motion-rules.md   # 表情动作规则
│   ├── seedance-emotion-action-library.md    # 情绪动作库
│   ├── seedance-real-lighting-rules.md       # 真实光影规则
│   ├── seedance-lighting-scene-library.md    # 灯光场景库
│   ├── seedance-closeup-face-lighting-rules.md     # 近景面光规则
│   ├── seedance-closeup-face-lighting-library.md   # 近景面光灯库
│   ├── seedance-chinese-fantasy-lighting-library.md # 国风灯光库
│   ├── seedance-depth-space-rules.md               # 景深空间规则
│   ├── seedance-camera-movement-transition-rules.md # 运镜转场规则
│   └── seedance-industrial-storyboard-routines-library.md # 工业化分镜套路
├── templates/                        # 提示词模板
├── tests/                            # 测试
├── examples/                         # 示例
├── docs/                             # 文档
└── requirements.txt                  # Python 依赖
```


## V0.9.78 模型机制与提示词预算增强

V0.9.78 新增四个底层判断库：

- `model-behavior-diagnosis.md`：解释注意力预算、否定召唤、参考图压过文字、细节面积不足、错误累积、音画联合约束等模型行为。
- `prompt-budget-allocation.md`：在复杂任务前判断当前镜头主预算是身份、动作、场景、光影、动力学、声音还是参考图，并决定哪些内容要压缩或拆分。
- `event-density-control.md`：控制一个镜头或 clip 的事件密度，防止短视频塞入多个完成动作、未来剧情、多地点和多轮对白。
- `anti-slop-rewrite-library.md`：把电影感、高级感、氛围感、真实感、震撼、唯美、8K、masterpiece 等空泛词改写成可见镜头、光影、动作、材质、动力学和声音。

这四项规则不会替代 V0.9.77 的物理动力学、V0.9.76 的导演执行融合层或 V0.9.75 的连续/参考/重拍规则，而是作为“为什么失败、预算如何分配、事件是否过载、空泛词如何落地”的前置判断层。


## V0.9.77 物理动力学增强

V0.9.77 将原有“风 / 柔体动力学”扩展为“物理动力学总规则”：除风、头发、衣物、披帛、纱幔外，还覆盖雨雪、烟尘、火焰、粒子、水面、液体、道具接触、碰撞、重力、惯性、光与动态介质互动和跨镜头动态连续。复杂动态默认使用 `references/physical-dynamics-standard.md`；简单风动继续使用 `references/seedance-wind-softbody-standard.md`。

## 当前输出标准 (V0.9.82)

最终视频提示词默认采用 **中等精简 + 强锚点 + 镜头化时间轴**：

```text
【正文提示词】
总设定 + 参考图职责 + 全局光源锚点 + 全局物理动力学锚点 + 镜头时间轴 + 全局一致性

【负面提示词】
人物类 + 动作类 + 动力学类 + 场景类 + 风格类
```

长度先按任务模式选择：压缩版约 80-180 中文字，快速视频版约 120-260 中文字，标准视频版约 500-1000 中文字，高控制视频版约 1000-1600 中文字。15 秒视频默认 2-4 个镜头，锁脸 / 对口型 / 多人物 / 复杂动力学优先 2-3 个镜头。旧的三板块视频模板已废弃。

新增“人物镜头强制覆盖规则”：只要画面中出现人物主体，先按条件判断是否需要人物动作、表情肢体联动、口型、人物面部光影、衣物饰品与环境动态、人物一致性。该规则是人物镜头唯一顶层判断入口；参考图一致性、角色连续性、表情动作、面光和风动文件只作为子实现标准。

V0.9.76 新增连续片段状态胶囊、参考图职责转移契约和重拍失败诊断：连续项目会记录已发生事件、当前片段、未来保留事件和连续性锁；多参考图任务会先分配 identity / costume / hairstyle / accessory / pose / environment / composition / first_frame / last_frame 等职责；修复或重拍任务会先归因身份漂移、服装漂移、动作口型失败、面光失败、风动冲突、连续性断裂或镜头问题，再生成修复提示词。

涉及风、发丝、衣料、披帛、纱幔、竹叶、云雾、水面或烟雾时，默认通过人物镜头规则判断触发，再使用 `references/seedance-wind-softbody-standard.md` 的“全局风向 / 柔体动力学锚点”：先定统一风场，再按主体、道具、环境分层描述受力速度差、延迟、回弹、重量和重力下坠，故障描述放入风力类负面提示词。


## V0.9.76 导演执行融合层

V0.9.76 在保持 prompt-script-master 中文状态机、人物镜头强制覆盖规则、连续片段 / 参考图 / 重拍规则和最终输出格式不变的前提下，新增一层更专业的导演执行规则：

- `directing-coherence-engine.md`：把电影感、氛围感、剧情情绪转成单一镜头意图。
- `motion-performance-contract.md`：让人物、手部、道具和环境动作具备力量、时间、物理结果和终点。
- `character-blocking-contract.md`：处理多人镜头、群像、舞台、对话和手脸稳定。
- `lighting-intention-contract.md`：把光影写成有动机的主光源、色温、阴影、反射、空气介质和变化。
- `pro-shot-continuity-contract.md`：把专业分镜、多镜头、首尾帧和广告/MV镜头写成可交接的镜头合约。
- `retake-iteration-protocol.md`：把重拍分为保留、后期修、局部编辑、换种子和改写提示词，并遵循单变量修改。

这些规则只增强导演执行质量，不替代 V0.9.75 的连续片段状态胶囊、参考图职责转移契约和重拍失败诊断，也不替代 V0.9.74 的人物镜头强制覆盖规则。

## 功能清单

### 🎬 核心框架
- **工业级状态机**：S1→S9 九阶段严格推进，不得跳级
- **确认优先模式**：默认先复述、判断、提问，确保理解一致再生成
- **快捷生成模式**：用户授权后自动补齐参数，直接输出可执行提示词
- **参考库隔离**：所有内部规则库和用户上传参考素材仅作导演方法参考，最终输出不留痕迹

### 📽️ 支持项目类型
- 🎤 唱歌 / 舞台 / MV / 跳舞 / 演唱会 / Live MV
- 🎭 人物情绪短片 / 剧情短片
- 📦 产品广告
- 🖼️ 首尾帧过渡 / 关键帧生成
- 📋 多镜头分镜 / 故事板
- 🌌 概念视觉
- 🔧 提示词审查 / 优化 / 修复

### 🎨 视觉生成（Prompt Optimizer V5）
- **OpenAI image-family 关键帧**：GPT-image / image2 自然语言提示词
- **角色连续性系统**：三视图、多视角、定妆图锁脸
- **用户上传参考图一致性**：参考图反推、多图融合、风格锚定
- **真实摄影规则**：物理光源、材质行为、焦段、曝光
- **电影摄影语言**：景别、构图、镜头运动、视角
- **导演风格锚点**：王家卫、韦斯·安德森等多种风格模板
- **AI 图像生成规则**：通用图像生成约束与质量门

### 🎥 Seedance 专项
- **提示词语序规则**：权重顺序、语序优化
- **人物镜头强制覆盖规则**：统一触发人物动作、表情肢体、口型、面光、动态材质和参考图锁脸
- **表情动作联动**：表情 + 肢体同步描述
- **面光规则**：骨骼光、面光、近景人脸灯光
- **真实光影规则**：物理光源、阴影、光质
- **灯光场景库**：20+ 标准灯光场景
- **国风灯光库**：中式奇幻特化灯光方案
- **景深空间规则**：前景/中景/背景层次、虚化控制
- **运镜转场规则**：推拉摇移跟升降、转场衔接
- **工业化分镜套路库**：专业分镜动作模式
- **情绪动作库**：情绪驱动的标准化动作描述

### 🛠️ 工具脚本
- `prompt_checker.py`——提示词格式与规则校验
- `prompt_exporter.py`——提示词导出与格式化
- `prompt_wizard.py`——交互式提示词生成向导

### 📊 输出模板
- Seedance 单镜头 / 多镜头模板
- 首尾帧过渡模板
- OpenAI image-family 图片提示词模板
- 修改 / 审查 / 修复模板
- 完整时间轴多段脚本模板
- 多种模型适配器

### ✅ 质量保障
- 内部 9 阶段自检流程
- 镜头化时间轴质量门（机位/运镜、焦点、主体动作、表情肢体、光影、风/柔体动态、环境与景深覆盖）
- 最终提示词纯净交付（不含解释、建议、选项）
- 强制中断条件（冲突检测、信息缺失拦截）
- 内部规则库引用验证

### 🎵 音乐 / 节奏专项
- 音乐风格识别
- BPM / 节奏速度匹配
- 歌词段落划分（主歌 / 副歌 / bridge / drop）
- 对口型支持
- 舞蹈动作编排
- 音乐剪辑节奏库

### 📚 知识库
- **演唱会 / Live MV**：舞台规则、表演动作库、镜头语言库
- **MV 故事结构**：叙事型 / 情绪型 / 卡点型等多种结构
- **灯光情绪**：情绪驱动的灯光方案
- **经典镜头**：标准化镜头类型库
- **动态级别**：轻 / 中 / 高三级，影响动作幅度、运镜速度、景别切换频率
- **景别系统**：远景→特写的完整景别规则

### 🖼️ 视觉素材库
- **构图参考库**：35 张专业构图范例（剪影、引导线、前景框、对称、负空间等）
- **参考图库**：19 张高质量参考图（人物、场景、灯光、氛围）

## 默认行为

| 配置 | 值 |
|------|-----|
| 默认模型 | Seedance 2.0 全能参考 |
| 默认语言 | 中文 |
| 默认模式 | CONFIRMATION_MODE（确认优先） |
| 提问节奏 | 每轮 ≤ 3 个关键问题 |
| 交付格式 | 可直接复制的完整中文提示词 |

## License

MIT


## V0.9.79 镜头语言与景别运镜增强

新增镜头语言决策层：`camera-shot-contract.md`、`shot-scale-selection.md`、`camera-movement-selection.md`、`multishot-grammar-standard.md`、`shot-continuity-axis-rules.md`、`animation-camera-grammar.md`。该版本用于让景别、机位、运镜、镜头数量、切点、轴线和动画镜头语法与内容任务匹配，避免远景硬写面部细节、特写硬塞大动作、运镜破坏锁脸/口型/手部/产品稳定性。


## V0.9.80 更新

新增 `references/output-length-mode-standard.md`，用于模式优先判断、输出长度档位、I2V 极简原则和图片 / 视频格式边界。视频继续使用【正文提示词】+【负面提示词】，图片默认使用自然语言段落。


## V0.9.82 参考图可识别性与人脸完整性

新增 `references/reference-visibility-gate.md` 与 `references/face-integrity-check.md`。图生视频、首尾帧、锁脸、换装、角色图和重绘任务会先判断参考图中的人脸、服装、发型、背景、构图是否清晰可识别。清晰部分可以执行 I2V 极简原则；不清晰部分必须补写；人脸畸形、五官错位、异常色块、黑斑、异常阴影、大面积死黑、皮肤塑料/蜡像/橡胶质感或肤色断层不得继承，必须重建自然面部结构、肤色连续性和面部光影逻辑。


## V0.9.82 参考图上传后统一自检

新增 `references/reference-intake-self-check.md`。所有上传参考图后的任务会先进入统一自检流程：判断图片用途、主职责、关键区域是否清晰、人脸是否符合生理逻辑、哪些内容可继承、哪些内容必须补写、是否建议用户重新生成参考图。

当人脸、服装、发型/发饰、背景/空间、构图/景别五类中三类及以上不清晰，或用户指定的主职责区域不可辨时，技能会建议用户重新生成 / 上传更清晰的参考图，而不是盲目执行 I2V 极简原则。
