# Output Templates

## Seedance 统一三段式（当前）

单镜头和多镜头统一格式，详见 `templates/video-prompt-template.md`。

> 最强格式规则：镜头框架之后立刻锁死人物 + 参考图；人物核心外形特征必须早于环境、氛围、道具和色调；人物权重永远高于环境。

> 强制面部光影规则：任何情况下，只要提示词描述到角色面部、眼神、表情、眨眼、侧脸、三分之二脸、皮肤、鼻梁、颧骨、下颌线或其他可见面部区域，必须加入人物面光/骨骼细节。面光内容应结合当前场景、氛围、人物参考图和风格，从光影库中抽取或改写为具体可拍摄描述。

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

## Revision / audit output

```text
## 正文提示词
[revised prompt]

## 负面提示词
[compact negative prompt]

## 自检发现
- [issues found]

## 已修改
- [what changed]
```

## Session footer

After prompt workflow outputs only:

`【当前状态】Prompt Optimizer 会话中。你可以直接继续说：加强光影 / 修改表情 / 背景虚化更强 / 压缩长度 / 退出技能。`

Do not place the footer inside copy-ready prompt text.
