# Task Routing

## Primary routes

- OpenAI image prompt generation or optimization: use OpenAI image-family natural-language prompt rules.
- Reference image / face lock / character continuity: load reference fidelity and character continuity rules.
- Seedance video prompt: load `seedance-prompt-order-rules.md` before other Seedance rules.
- Seedance emotion or acting: load expression-motion rules and the emotion action library.
- Lighting: load real lighting rules; then select one general, Chinese fantasy, or face-lighting module as needed.
- Close-up face / 面光: load close-up face lighting rules before environment lighting.
- Depth / lens / bokeh / spatial hierarchy: load depth-space rules.
- Camera movement / transition: load camera movement and transition rules.
- Industrial storyboard / multi-shot routine: load the 60-routine storyboard library.
- Previous prompt edit: load conversation edit flow.
- User asks whether they are still in the skill: load session mode.

## Trigger separation

Single-shot movement requests such as `镜头慢慢推近` do not trigger storyboard routines.

Multi-shot phrases such as `分镜`, `镜头组`, `工业化分镜`, `标准分镜`, `10秒流程`, or `开场-过渡-结尾` trigger storyboard routines.

Skill maintenance phrases such as `加入规则`, `更新项目`, `上传 GitHub`, `自检流程`, and `固化到 Skill` do not trigger prompt revision or visible session mode.
