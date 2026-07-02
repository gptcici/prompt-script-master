# Character Sheet Continuity System

Use this reference whenever the user asks for character sheets, multi-view references, front/full-body views, three-view sheets, turnaround sheets, model sheets, pose sheets, costume reference sheets, or repeated character images across AIMV / AI short-drama shots.

## Core goal

A character sheet is not a beauty poster. It is a continuity tool.

The output must help the image model keep one believable actor or character consistent across views, poses, outfits, and later shots while still looking like real camera capture.

## Trigger wording

Route here when the user says or implies:

- 三视图 / 多视角图 / 正面全身 / 背面 / 侧面 / 半侧面
- 角色设定图 / 人物设定图 / 定妆图 / 角色参考图 / 人物参考图
- full body / character sheet / model sheet / turnaround / front view / side view / back view
- 保持同一个人物 / 保持脸 / 保持发型 / 服装一致 / 后续分镜保持一致
- 按照模板生成三视图 / 多角度展示 / 参考图用于后续生图

## Priority order

1. Explicit user instructions.
2. Uploaded face or character reference: lock identity, face, hairstyle, age impression, makeup, and temperament.
3. Same-person continuity across all views or panels.
4. Real-camera studio capture and physical plausibility.
5. Wardrobe silhouette, construction, fabric weight, accessories, and hair behavior.
6. Clean readability for future reuse.
7. Style, decoration, and background mood.

Face lock and same-person continuity always outrank decorative styling.

## Multi-view sheet rules

When creating a multi-view or three-view prompt:

- Describe a single character reference sheet in one image.
- Use the same actor, same face, same hairstyle, same makeup, same body proportions, and same costume across all views.
- Prefer a clean neutral studio background, soft even real studio lighting, and consistent camera height unless the user requests a scene background.
- Use physically plausible full-body standing poses: front view, three-quarter view, side view, and back view when needed.
- Keep clothing seams, belts, sleeves, collars, ornaments, shoes, weapons, and hair length consistent from view to view.
- Keep long hair weight believable: it should fall with gravity, wrap around shoulders or back naturally, and not look like a floating illustration shape.
- If the character has colored hair accents, unusual makeup, armor, fantasy costume, or ancient costume, describe them as real wig work, real makeup, stitched fabric, metal ornaments, layered garments, or practical costume construction.
- Do not request visible labels, panel numbers, or typography unless the user explicitly asks for a labeled sheet; text rendering can damage the image.

## Single full-body reference rules

When the user asks for a front full-body reference:

- Lock the face and hairstyle from the reference first.
- Use a straight-on or slight three-quarter camera angle at natural human height.
- Show the whole body from head to shoes without cropping.
- Keep the pose simple enough to reveal costume structure.
- Use real studio photography language: seamless paper backdrop, softbox, practical fill light, natural shadows, believable skin and fabric response.
- The image should be useful as a future identity/wardrobe reference, not just a glamorous portrait.

## Ancient costume / fantasy character realism

For 古风, 仙侠, fantasy, stage, or mythic character sheets:

- Translate fantasy styling into real costume department language.
- Mention fabric layers, embroidery, stitched seams, hairpieces, pins, ornaments, wig lace, makeup texture, and garment weight.
- Keep silhouettes wearable and physically supported.
- Avoid impossible fabric that floats without support unless it is described as staged wind, wire support, or a captured motion moment.
- Avoid poster lighting; prefer real studio or real set light.

## Prompt pattern: multi-view sheet

Chinese:

```text
以用户上传的人物参考作为脸部、发型、妆容和身份气质强锁定，生成一张真实摄影感的人物三视图/多视角定妆参考图。同一个角色在同一张图中展示正面全身、半侧面/侧面、背面视图；所有视图必须保持同一张脸、同一发型、同一发色细节、同一身高比例、同一服装结构、同一鞋履和配饰。使用干净中性影棚背景，柔和真实棚拍光，统一相机高度和自然透视，完整显示从头到脚。服装必须像真实可穿戴服装：真实布料重量、缝线、褶皱、金属/玉石/皮革/纱料反应，长发受重力自然下垂。整体像专业服装定妆摄影和角色参考照，不像AI插画、游戏立绘或海报。
```

English:

```text
Use the uploaded character reference as a strict lock for the face, hairstyle, makeup, and identity temperament. Create one photoreal character turnaround reference sheet showing the same character in front full-body view, three-quarter or side view, and back view within a single image. Every view must keep the same face, same hairstyle, same hair-color details, same body proportions, same costume construction, same shoes, and same accessories. Use a clean neutral studio background, soft real studio lighting, consistent camera height, natural perspective, and full head-to-toe visibility. The costume must feel physically wearable, with real fabric weight, seams, wrinkles, embroidery, metal or jade ornaments, leather, gauze, and natural gravity on long hair. The result should look like professional wardrobe fitting photography and a usable character reference sheet, not AI illustration, game concept art, or a poster.
```

## Prompt pattern: front full-body reference

Chinese:

```text
以上传人物参考强锁定脸部、发型、妆容和身份气质，生成真实摄影感的正面全身定妆照。人物正面站立，完整显示头发、脸、身体、服装结构、袖口、腰部、裙摆/裤装、鞋履和配饰，不裁切。干净纯色或中性影棚背景，柔和真实棚拍光，轻微自然阴影，真实皮肤、真实发丝、真实布料重量和真实妆容质感。整体用于后续角色一致性参考，不像AI立绘或过度修图海报。
```

English:

```text
Strictly lock the uploaded character reference for the face, hairstyle, makeup, and identity temperament. Create a photoreal front full-body wardrobe reference photo. The character stands facing the camera, fully visible from hair and face to body, outfit structure, cuffs, waist, skirt or trousers, shoes, and accessories, with no cropping. Use a clean solid-color or neutral studio background, soft real studio lighting, slight natural shadow, real skin, real hair strands, real fabric weight, and believable makeup texture. The image should work as a future character-consistency reference, not an AI standing illustration or over-retouched poster.
```

## Failure prevention checklist

Before finalizing, verify:

- Is the same face preserved across every view?
- Are hairstyle length, hair volume, and color accents identical across views?
- Are costume pieces consistent from front to side to back?
- Is the full body visible without cropping?
- Does the sheet look photographed in a real studio or production environment?
- Is the background simple enough for future reference use?
- Are there no unintended labels, watermarks, random text, or poster graphics?
- Is the character usable for later AIMV / AI short-drama shot continuity?
