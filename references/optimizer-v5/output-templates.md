# Output Templates

## Seedance / 视频统一结构

Final video prompts use the current Prompt Script Master standard: **中等精简 + 强锚点 + 镜头化时间轴**.

```text
【正文提示词】
总设定 + 参考图职责 + 全局光源锚点 + 全局风向 / 柔体动力学锚点 + 镜头时间轴 + 全局一致性

【负面提示词】
人物类 + 动作类 + 风力类 + 场景类 + 风格类
```

Do not output deprecated three-block video templates for final Seedance prompts.

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


## Wind / soft-body note
When wind, hair, fabric, veils, leaves, clouds, mist, smoke, or water motion matters, use `references/seedance-wind-softbody-standard.md` for the compact physical wind-field module.


## Character-shot note
When a final video or image prompt contains a recognizable person, apply the top-level `人物镜头强制覆盖规则` first. Use expression-motion, close-up face lighting, reference fidelity, character continuity, and wind/soft-body files only as implementation sub-rules after the trigger is confirmed.
