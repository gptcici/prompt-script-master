# Output Templates

## Seedance complete prompt

```text
【正文提示词】
[景别/镜头视角 + 核心运镜 + 核心景深属性 + 人物主体 + 关键外形特征 + 核心动作 + 表情肢体联动 + 面光/骨骼光影 + 场景环境光影 + 场景环境细节 + 景深空间细节补充 + 全局一致性约束]

【负面提示词】
[compact scene-matched failures only]
```

For ordered multi-phase actions, keep the same module order inside a timeline. The first line before the timeline should lock the S-level frame package and character anchor.

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
