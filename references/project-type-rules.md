# 项目类型规则

用于在复述阶段判断用户项目类型，并决定哪些特定环节需要触发。

## 常见项目类型

- 舞台 / 唱歌 / MV / 跳舞：必须触发音乐 / 节奏信息确认、动态级别判断、动作 / 表演方案预览。
- 产品广告：必须触发产品卖点、材质、品牌调性和产品 hero shot 方向判断。
- 人物情绪：必须触发人物状态、情绪路径、表情动作和景别节奏判断。
- 剧情短片：必须触发人物关系、故事转折、场景调度和连续性判断。
- 首尾帧过渡：必须触发首帧、尾帧、中间变化路径和一致性分析。
- 多镜头分镜：必须触发镜头结构规划和镜头间连续性判断。
- 概念视觉 / 奇幻视觉：必须触发核心视觉隐喻、空间逻辑和风格一致性判断。

## 不确定时

如果项目类型可能跨越多个类型，先说明暂定类型，并请用户确认；不得直接跳过复述阶段进入最终提示词。


## V0.6 音乐视频细分类型

当项目属于舞台 / 唱歌 / MV / 跳舞时，继续细分：

- 演唱会 / Live MV：读取 `concert-live-mv-rules.md`、`concert-performance-action-library.md`、`concert-shot-language-library.md`。
- 多场景 MV / AIMV：读取 `mv-story-structure-library.md`。
- 节奏驱动视频：读取 `music-editing-rhythm-library.md`。
- 强光影情绪项目：读取 `lighting-emotion-library.md`。
- 上传图片、视频、脚本拆解或关键帧时：读取 `reference-isolation-rules.md` 与 `asset-library-guide.md`。

所有细分类型都必须遵守 `reference-isolation-rules.md`，不得把参考库中的来源内容写入最终提示词。
