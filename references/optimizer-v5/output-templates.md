# Output Templates

## Seedance 统一输出格式（当前）

单镜头和多镜头统一分为正文提示词和负面提示词两部分，详见 `templates/video-prompt-template.md`。

> **旧版三段式（全程总定调/时间轴分段/全局收尾）和旧版 9 项时间轴格式已废弃。**

> 最强格式规则：视频规格 + @Image1 参考图指令之后，必须立刻写人物核心外形特征；人物权重永远高于环境。

> 正文禁止出现导演创作思路、心理感受、逻辑说明等非视觉化抽象描述；禁止出现"禁止""不要""避免""不得"类否定词（统一放入负面提示词）。

> 人物光影规则：必须从锚点光源推导（见 `anchor-light-source-rule.md`），按光源方向→骨骼高光点位（鼻梁/眉骨/颧骨/下颌线等）→暗部过渡→整体质感顺序书写；触发条件、分机位点位库、禁写条款见 `seedance-closeup-face-lighting-rules.md`。

```text
【正文提示词】
视频规格 + 全程运镜总基调
@Image1 参考图标准化指令
人物核心外形特征
整体场景总设定

【时间轴分段】
每段 7 项连成一整段自然语言：
景别 + 运镜状态 + 人物核心动作 + 衣发纱幔动态 + 人物光影 + 环境细节 + 景深变化

[权重标记] 整体风格质感 + 全局一致性约束

【负面提示词】
人物类：[脸部变形、五官漂移、发型错乱...]
动作类：[肢体错乱、手部畸形...]
场景类：[空间跳跃错位...]
风格类：[过度磨皮、过度CG感...]
技术类：[运镜抖动、景别突变...]
```

## Revision / audit output

```text
## 正文提示词
[revised prompt]

## 自检发现
- [issues found]

## 已修改
- [what changed]
```

## Session footer

After prompt workflow outputs only:

`【当前状态】Prompt Optimizer 会话中。你可以直接继续说：加强光影 / 修改表情 / 背景虚化更强 / 压缩长度 / 退出技能。`

Do not place the footer inside copy-ready prompt text.
