# 提示词脚本大师

> 一个导演助理式 AI 视频提示词生成系统，把简单口语想法转化为结构完整、镜头明确、动作细致、可直接用于 AI 视频生成工具的中文提示词。

## 当前版本

```text
v0.6.0-script-learning-library
```

当前版本为：脚本学习库增强版本（Script Learning Library），在确认优先状态机基础上新增演唱会动作、Live MV镜头、MV叙事结构、音乐剪辑节奏、光影情绪和素材库隔离规则。

## 项目定位

《提示词脚本大师》不是普通提示词模板库，而是一个可扩展的提示词工作流项目。

它的目标是：

1. 让用户用简单口语描述想法。
2. 系统像导演助理一样只追问必要问题。
3. 通过专业默认值补齐画面、镜头、动作、灯光、参考素材、时间轴和禁止项。
4. 上传内容后先拆解、复述、确认，再生成提示词，避免误解用户目标。
5. 信息确认后自动生成完整中文提示词，并进行内部质量自检。
6. 可打包为 ChatGPT Skill 使用。

## 当前原则

- 默认输入：简单口语
- 默认模式：确认优先状态机（Confirmation-first State Machine）
- 默认目标模型：Seedance 2.0 全能参考
- 提问节奏：每轮 2-3 个问题
- 输出语言：完整中文提示词
- 单镜头时长：6-15 秒
- 负面提示词：只保留关键异常

## 状态机版本

当前系统已升级为 v0.6.0：保留工业级 fail-closed 状态机，并新增内部参考库隔离机制。参考库、图片、视频和拆解资料只用于抽象导演方法，最终生成内容不得泄露来源信息。

## Skill

见 `skill/prompt-script-master/`


## V0.6 新增参考库

- `references/reference-isolation-rules.md`：最高优先级素材隔离规则，防止参考库内容进入最终输出。
- `references/script-learning-index.md`：脚本学习库索引。
- `references/concert-performance-action-library.md`：演唱会人物动作与表演动作分级。
- `references/concert-shot-language-library.md`：演唱会主体线、观众线、空间线和景别呼吸。
- `references/mv-story-structure-library.md`：MV现实锚点、多空间幻想、五幕式结构和群像收束。
- `references/music-editing-rhythm-library.md`：音乐段落与剪辑密度、动作落点、切镜节奏。
- `references/lighting-emotion-library.md`：光影与情绪映射。
- `references/asset-library-guide.md`：图片、视频、关键帧和本地素材入库规则。

## 参考库硬规则

所有库内容只作为内部学习与抽象参考。最终生成脚本中不得出现库里的原始人物、艺人、视频名、文件名、时间戳、歌词、字幕、水印、logo、具体桥段或来源痕迹。
