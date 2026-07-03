# Reference Fidelity System

Use this whenever uploaded images or reference roles are part of the task.

## Core rule

References are constraints, but not all references have equal priority.

The face reference is the strongest constraint. Everything else is filtered through photorealism.

## Priority order

1. Explicit user instructions.
2. Uploaded face / character reference: force-lock identity, face, hairstyle, age impression, and temperament.
3. Real camera realism and physical plausibility.
4. Outfit reference: preserve silhouette/material/accessory ideas only if they can exist as real wardrobe.
5. Scene reference: preserve layout/scale/light sources only if they can be photographed.
6. Pose/action reference: preserve performance intent while keeping body balance and anatomy real.
7. Style/mood reference: preserve mood only if it does not create AI-art, CG, illustration, or poster feeling.

## Face-lock language

Use direct language in the prompt when a face reference is provided.

Chinese:
```text
以上传的人物定妆图作为脸部与发型强参考，锁定她的脸型比例、五官气质、眼神感觉、鼻唇印象、短款层次黑发、紫色挑染和冷感清透的年龄气质；不得把她美化成另一个通用AI女模特。
```

English:
```text
Use the uploaded character sheet as a strict face and hairstyle reference, locking her facial proportions, feature impression, gaze quality, nose-and-lip impression, short layered black hair, subtle purple highlights, and cool delicate age impression; do not beautify her into a different generic AI model.
```

## Non-face reference language

For outfit, stage, environment, and sci-fi references, use inspiration plus realism filtering.

Chinese:
```text
其他参考图作为服装、场景、灯光和氛围的设计参考，但所有元素都必须服从真实摄影逻辑：真实材质、真实结构、真实重量、真实光源、真实阴影、真实反射和可被相机拍下的物理存在感。
```

English:
```text
Treat all non-face references as design references for wardrobe, scene, lighting, and mood, but every element must obey real photography logic: real material, real structure, real weight, real light sources, real shadows, real reflections, and a physical presence that a camera could capture.
```

## What to preserve by reference type

### Face / character reference

Preserve strongly:
- face shape and proportions
- eye shape, gaze quality, and expression temperament
- nose and lip impression
- hairstyle length, layering, texture, color accents
- age impression and identity aura
- skin tone range under the target scene light

Do not name or identify real people. Describe visible traits only.

### Outfit reference

Preserve as realistic wardrobe:
- silhouette and asymmetry
- neckline and shoulder structure
- fabric weight, transparency, gloss, seams, wrinkles
- hardware, chains, belts, in-ear monitors, microphones, footwear
- signs of real wear, tension, and stage movement

### Scene / stage reference

Preserve as a real location or production set:
- spatial layout and camera direction
- central axis, runway, set pieces, LED screens, trusses, lights
- crowd density and scale
- practical light sources and color spill
- haze, smoke, pyrotechnics, rain, dust, or atmosphere when plausible

### Style / mood reference

Preserve only:
- color temperature and contrast direction
- exposure mood
- atmosphere density
- documentary/live-event/short-drama feeling

Do not preserve AI-looking render artifacts.

## Multi-reference prompt pattern

Chinese:
```text
参考图优先级：人物定妆图用于强行锁定女歌手的脸部、发型和身份气质；舞台/服装/场景参考图只作为真实制作设计参考。生成结果必须像真实相机在现场拍到的一帧，而不是AI概念图或舞台海报。
```

English:
```text
Reference priority: use the character sheet to strictly lock the singer's face, hairstyle, and identity temperament; use stage, outfit, and scene references only as realistic production-design references. The result must look like a real camera captured the moment on location, not an AI concept image or stage poster.
```

## Failure prevention

Add positive controls when fidelity matters:
- consistent reference face and hairstyle
- real skin under the target light
- believable human proportions and hands
- wardrobe behaves like physical fabric or leather or metal
- scene elements cast real light and shadows
- background supports the subject rather than competing with the face
- one primary focal point, usually the face for character shots
