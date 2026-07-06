# Quality Control

## Default principle

Quality checks are performed internally. Do not show scoring unless the user asks for an audit.

## Current final-output standard

Use `references/seedance2-concise-execution-standard.md` as the primary final prompt quality standard.

## Checklist

### Structure
1. Final video prompts use `【正文提示词】` and `【负面提示词】`.
2. Main prompt is positive, model-facing, and free of conversational notes.
3. Negative wording is placed in the negative prompt.
4. Length is controlled by `output-length-mode-standard.md`: compressed 80-180 Chinese characters, quick video 120-260, standard video 500-1000, high-control video 1000-1600, dense storyboard only on explicit request; negative prompt about 120-300 Chinese characters.

### Anchors
5. Reference image responsibilities are explicit when references exist.
6. Character identity / costume / prop locks are concise and near the beginning.
7. Global light source anchor has one physical source, direction, color, dark-side detail, and weak bounce.
8. Global physical dynamics anchor exists when hair, fabric, veils, leaves, clouds, mist, smoke, rain, snow, fire, water, particles, props, contact, collision, gravity, inertia, or other visible physical motion is important.
9. Dynamic scenes define one source and path, then layer subject, prop, environment, fluid, particle, and contact responses with material speed differences, delay, rebound, gravity, friction, contact reaction, and final/消散 state.

### Shot execution
10. Multi-shot videos have clear time ranges and cut points.
11. Each shot covers camera, action, and environment/light/motion.
12. Body, head, hand, expression, fabric, hair, or object actions are visible and non-mechanical.
13. Character shots comply with `人物镜头强制覆盖规则`: action and expression/body linkage are present; mouth movement appears when speaking/singing/lip-sync; face lighting appears for medium close-up or closer shots; dynamic hair/wardrobe/accessory/environment materials follow unified motion; reference identity is locked when references exist.
14. Focus and depth behavior are described where important.
15. Shot descriptions avoid overloaded explanation and repeated style adjectives.

### Consistency
16. Light direction remains consistent unless intentionally changed.
17. Physical motion direction remains consistent unless intentionally changed, including wind, rain, smoke, water, particles, props, contact, gravity, and inertia.
18. Character, costume, prop, architecture, and scene remain continuous.
19. The final prompt is copy-ready.

## Hard stops

Do not output a final prompt if:
- core subject is unclear;
- reference images conflict and cannot be prioritized;
- target format is unclear and the user has not authorized default assumptions;
- requested single-shot duration or action density is physically unreasonable;
- the prompt would use deprecated final structure.

## Auto-fix

Automatically fix:
- overly long repeated wording;
- missing light or physical dynamics anchors;
- missing character action or expression/body linkage when a person is the shot subject;
- missing mouth movement for speaking, singing, or lip-sync;
- missing close-up face lighting for medium close-up or closer character shots;
- vague actions;
- vague dynamics claims such as `大风`, `动感很强`, `烟雾缭绕`, `水面波动` without source, path, material response, contact result, or dissipation;
- negative instructions accidentally placed in the main prompt;
- excessive negative prompt duplicates.


## Sequence / reference / retake checks

When the task is a continuation or multi-clip project, internally check for:

- `already_happened`, `current_clip_only`, and `reserved_for_later` separation.
- no repeated previous action unless the user explicitly asks for a replay.
- no future event leak into the current final prompt.
- stable character, costume, prop, scene, light direction, wind direction, mood, and camera axis.

When the task uses multiple references, internally check for:

- each reference image has a primary transfer role.
- identity references do not accidentally transfer old costume or background.
- costume / scene / pose / style references do not overwrite the identity reference.
- first frame controls start state and last frame controls end state.

When the task is a retake or audit, diagnose before rewriting:

- identity drift, costume drift, action/expression/mouth failure, face-lighting failure, wind conflict, continuity break, camera-axis issue, or output-structure issue.


### V0.9.76 director execution checks
20. Complex cinematic / emotional shots have one clear shot intention, not only generic style labels.
21. Important actions include a subject, concrete verb, force or rhythm, visible consequence, and endpoint.
22. Multi-character shots assign one action tier per visible person: persistent micro-motion, one focused response, or one core large action.
23. Lighting has a motivated source, direction, color temperature, shadow behavior, material reflection, and transition when the light changes.
24. Professional multi-shot projects use shot contracts or equivalent coverage: purpose, action, camera, references, continuity anchors, start state, end state, and risk.
25. Retake workflows diagnose the issue and change one variable at a time instead of stacking many fixes.

## V0.9.76 auto-fix additions

Automatically fix:
- generic cinematic language without shot intention;
- action wording without physical consequence or endpoint;
- multi-character shots where everyone performs large actions;
- lighting without visible source or direction;
- professional shot lists without continuity anchors;
- retake prompts that change many variables at once.


## V0.9.78 model / budget / density / anti-slop checks

Before final generation, internally check:

- Model behavior: if the user asks why a result failed, diagnose whether the cause is attention dilution, negation-summoning, reference conflict, event trajectory failure, compounding drift, detail-area limits, or audio-video overload.
- Prompt budget: every complex shot has one primary spend and one secondary spend; identity, motion, scene density, lighting, dynamics, and sound are not all treated as equal priorities in the same shot.
- Event density: the current clip performs one visible beat with one changed endpoint; completed past actions are not repeated and future events are not leaked.
- Anti-slop: empty evaluators such as `电影感`, `高级感`, `氛围感`, `唯美`, `震撼`, `真实感`, `8K`, `masterpiece`, and similar filler are converted into observable camera, light, action, material, sound, or physical-dynamics language.
- Positive replacement: quality prevention is written as desired visible properties in the main prompt; fault names remain in the negative prompt.


## V0.9.79 camera-language checks

Before final generation, internally check:

- Shot contract: key shots have a clear intention, shot size, angle, movement, focus, start frame, end frame, and risk control.
- Shot scale fit: the selected shot size can actually carry the requested identity, emotion, action, space, product, material, or detail task.
- Movement fit: the selected movement does not undermine face, mouth, hand, text, product, first/last-frame, or physical-dynamics stability.
- Multishot grammar: the number of shots and cut points fit the duration and event density.
- Axis continuity: screen direction, eyeline, motion direction, light direction, physical direction, prop state, and start/end handoff remain stable unless intentionally changed.
- Animation grammar: 2D/anime/storyboard prompts use layer, frame, and animation timing language instead of inappropriate live-action lens equipment.

Auto-fix camera mismatches by changing the shot size, simplifying movement, reducing shot count, splitting the clip, or replacing live-action lens language with animation camera grammar.


## V0.9.80 模式与长度检查

最终生成前检查是否已判断 T2V / I2V / R2V / FLF2V / V2V / Edit / Extend / IMAGE；检查提示词长度是否匹配任务复杂度；检查 I2V 是否只写图片看不出来的动作、镜头、光线、动力学和保持约束。


## V0.9.81 reference visibility / face integrity checks

Before applying I2V minimal prompting, internally check:

- Reference visibility: face, costume, hairstyle/accessory, environment, composition, and first/last-frame connection are clear enough to trust.
- Partial clarity: clear parts may stay implicit; unclear parts must be written as explicit visual anchors.
- Face integrity: faces do not contain malformed anatomy, displaced features, incompatible color patches, black spots, unnatural shadows, large dead-black areas, dirty blotches, plastic/wax/rubber skin, broken skin-tone transitions, or non-biological texture.
- Abnormal reference handling: if the reference face contains artifacts, inherit only usable identity cues and rebuild natural facial structure, skin tone continuity, and motivated face lighting.
- Negative placement: face malformation, black spots, abnormal shadows, dead-black facial areas, dirty color patches, plastic skin, waxy skin, over-smoothed skin, and skin-tone banding belong in `人物类` negative prompt, not in the main prompt.

Auto-fix by adding a reference visibility note, explicit anchors for unclear reference regions, natural face-structure anchors, motivated face-lighting anchors, or face-integrity negative terms.


## V0.9.82 reference intake self-check

上传参考图后的内部质量检查：

1. 是否先判断每张图的用途和主职责。
2. 是否检查人脸、服装、发型/发饰、背景/空间、构图/景别、首尾帧连接性。
3. 是否检查人脸生理结构、肤色连续、异常色块、黑斑、死黑阴影和皮肤伪影。
4. 是否只把清晰可信的信息分配为参考图职责。
5. 如果三类以上关键信息不清晰，或主职责区域不可辨，是否建议用户重新生成/上传更清晰的参考图。
6. I2V 极简原则是否只在参考图关键视觉信息清晰时执行。

自动修正：若发现“保持图中人物/服装/背景”但参考图描述同时包含模糊、遮挡、过暗、过曝、死黑、色块、黑斑、不可辨等问题，应改为“清晰部分继承，不清晰部分补写；主职责不可辨时建议重新生成参考图”。
