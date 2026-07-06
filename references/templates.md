# Templates

## Default final video prompt template

Use the template in `templates/video-prompt-template.md`.

Short form:

```text
【正文提示词】
[总设定]

参考图职责：[...]

全局光源锚点：[...]

全局物理动力学锚点：[...]

0-2秒，镜头一：[景别/机位/运镜]。[主体动作/表情/身体或材质联动]。[光影/风/景深/环境变化]。
2-4秒，镜头二：...

全局一致性：...

【负面提示词】
人物类：...
动作类：...
风力类：...
场景类：...
风格类：...
```

Do not use deprecated three-block video templates for final prompts.


## Wind / soft-body note
When wind, hair, fabric, veils, leaves, clouds, mist, smoke, or water motion matters, use `references/seedance-wind-softbody-standard.md` for the compact physical wind-field module.
