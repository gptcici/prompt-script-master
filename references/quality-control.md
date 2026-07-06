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
4. Length is controlled: for a typical 15-second multi-shot video, main prompt about 1200-1800 Chinese characters and negative prompt about 120-300 Chinese characters.

### Anchors
5. Reference image responsibilities are explicit when references exist.
6. Character identity / costume / prop locks are concise and near the beginning.
7. Global light source anchor has one physical source, direction, color, dark-side detail, and weak bounce.
8. Global wind / soft-body dynamics anchor exists when hair, fabric, veils, leaves, clouds, mist, smoke, water, or other wind-driven materials are important.
9. Wind scenes define one direction and force, then layer subject, prop, and environment responses with material speed differences, delay, rebound, and gravity.

### Shot execution
10. Multi-shot videos have clear time ranges and cut points.
11. Each shot covers camera, action, and environment/light/motion.
12. Body, head, hand, expression, fabric, hair, or object actions are visible and non-mechanical.
13. Character shots comply with `人物镜头强制覆盖规则`: action and expression/body linkage are present; mouth movement appears when speaking/singing/lip-sync; face lighting appears for medium close-up or closer shots; dynamic hair/wardrobe/accessory/environment materials follow unified motion; reference identity is locked when references exist.
14. Focus and depth behavior are described where important.
15. Shot descriptions avoid overloaded explanation and repeated style adjectives.

### Consistency
16. Light direction remains consistent unless intentionally changed.
17. Wind/motion direction remains consistent unless intentionally changed.
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
- missing light or wind / soft-body dynamics anchors;
- missing character action or expression/body linkage when a person is the shot subject;
- missing mouth movement for speaking, singing, or lip-sync;
- missing close-up face lighting for medium close-up or closer character shots;
- vague actions;
- vague wind claims such as `大风` or `风很强` without visible material response;
- negative instructions accidentally placed in the main prompt;
- excessive negative prompt duplicates.
