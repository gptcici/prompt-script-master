# 提示词脚本大师 (Prompt Script Master) V0.9.6

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
│   ├── reference-material-guide.md   # 参考素材指南
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
│   ├── lighting-emotion-library.md            # 灯光情绪库
│   └── asset-library-guide.md                 # 素材库指南
├── references/optimizer-v5/         # Prompt Optimizer V5 视觉规则
│   ├── task-routing.md               # 任务路由
│   ├── output-templates.md           # 输出模板
│   ├── model-adapters.md             # 模型适配器
│   ├── command-system.md             # 命令系统
│   ├── conversation-edit-flow.md     # 对话编辑流
│   ├── reference-fidelity-system.md  # 参考图一致性系统
│   ├── reference-image-library.md    # 参考图库
│   ├── character-sheet-continuity-system.md  # 角色连续性
│   ├── realistic-photography-rules.md        # 真实摄影规则
│   ├── ai-image-generation-rules.md          # AI图像生成规则
│   ├── director-style-anchors.md             # 导演风格锚点
│   ├── cinematic-camera-language.md          # 电影摄影语言
│   ├── composition-space-structure.md        # 构图空间结构
│   ├── composition-reference-library.md      # 构图参考库
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
├── assets/                           # 视觉参考素材
│   ├── composition-library/          # 构图参考库（35张）
│   └── reference-library/            # 参考图库（19张）
├── templates/                        # 提示词模板
├── tests/                            # 测试
├── examples/                         # 示例
├── docs/                             # 文档
└── requirements.txt                  # Python 依赖
```

## 功能清单

### 🎬 核心框架
- **工业级状态机**：S1→S9 九阶段严格推进，不得跳级
- **确认优先模式**：默认先复述、判断、提问，确保理解一致再生成
- **快捷生成模式**：用户授权后自动补齐参数，直接输出可执行提示词
- **参考库隔离**：所有参考素材仅作内部导演方法参考，最终输出不留痕迹

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
- **参考图一致性**：参考图反推、多图融合、风格锚定
- **真实摄影规则**：物理光源、材质行为、焦段、曝光
- **电影摄影语言**：景别、构图、镜头运动、视角
- **导演风格锚点**：王家卫、韦斯·安德森等多种风格模板
- **AI 图像生成规则**：通用图像生成约束与质量门

### 🎥 Seedance 专项
- **提示词语序规则**：权重顺序、语序优化
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
- 时间轴质量门（7 项：景别 + 运镜 + 动作 + 衣发 + 人物光影 + 环境 + 景深）
- 最终提示词纯净交付（不含解释、建议、选项）
- 强制中断条件（冲突检测、信息缺失拦截）
- 案例库引用验证

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
