# Output Templates

## Seedance 统一三段式（当前）

单镜头和多镜头统一格式，详见 `templates/video-prompt-template.md`。

```text
【全程总定调】
视频基础规格 + 镜头总基调
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
