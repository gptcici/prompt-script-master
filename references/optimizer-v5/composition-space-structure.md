# Photoreal Composition Override

Use composition terms only to improve believable camera control for OpenAI image-family prompts. Composition must support a real AIMV / AI short-drama frame, live photo, or production still. Do not make the image feel like a graphic poster, concept art layout, or AI showcase.

# Composition and Spatial Structure Rules

## Composition library override

When `composition-reference-library.md` contains a closer text-only shot-design pattern, use that pattern first. Use this file as the fallback language system for naming composition, spatial depth, and focal point. Never let composition language create a poster-like AI layout; keep every frame physically shootable for AIMV / AI short-drama production.


Every generated image prompt must include professional composition, spatial structure, and a clearly assigned focal point.

## Core rule

Every prompt must answer three questions:

1. Composition rule: how the image is organized inside the frame.
2. Spatial structure: how foreground, middle ground, and background create depth.
3. Focal point: exactly where the viewer's eye should land first.

## Composition rule library

Choose one primary composition rule based on the subject and scene.

### Rule of thirds

Use for portraits, travel scenes, landscapes, people in environments, and realistic production stills.

Chinese: 三分法构图，主体落在左/右三分线交点；人物眼睛靠近上三分线，保留视线方向的留白。

English: rule-of-thirds composition, subject placed on the left/right third intersection; eyes near the upper third line, lead room in the direction of gaze.

### Centered symmetry

Use for iconic, solemn, architectural, sci-fi, ritual, product, and poster-like images.

Chinese: 中心对称构图，主体位于画面中央，左右结构平衡；轴线式构图，背景线条向主体汇聚。

English: centered symmetrical composition, subject anchored in the center, balanced left-right structure; axial composition with background lines converging toward the subject.

### Leading lines

Use for streets, corridors, roads, rivers, railways, architecture, sci-fi interiors, and movement.

Chinese: 引导线构图，道路/墙面/光线从前景延伸到主体；透视线汇聚到主体焦点，增强空间纵深。

English: leading-line composition, road/walls/light beams guiding the eye from foreground to subject; perspective lines converging toward the focal subject.

### Frame within frame

Use for windows, doors, mirrors, cars, caves, arches, hallways, and interior/exterior contrast.

Chinese: 框中框构图，门框/窗框/阴影边界包围主体；前景框架形成自然遮罩，突出主体。

English: frame-within-frame composition, doorway/window/shadow edges enclosing the subject; foreground frame isolates the focal subject.

### Open space composition

Use for lonely, minimal, surreal, luxury, editorial, poster, product, and emotional scenes.

Chinese: 留白构图，大面积空白压低画面噪声；主体偏置，背景以大色块承托情绪。

English: open-space composition, large empty areas reducing visual noise; off-center subject supported by broad clean color fields.

### Diagonal / triangular composition

Use for action, tension, running, falling, conflict, fashion poses, and dynamic movement.

Chinese: 对角线构图，身体动势沿画面对角线展开；三角形构图，人物姿态与光影形成稳定视觉结构。

English: diagonal composition, body movement traveling across the frame diagonal; triangular composition, pose and light forming a stable visual structure.

### Golden-ratio spiral

Use for elegant portraits, editorial images, nature, high-end realistic photographed scenes, and refined layouts.

Chinese: 黄金螺旋构图，视觉动线从前景弧线引向主体焦点；主体落在黄金比例视觉重心处。

English: golden-ratio spiral composition, visual flow curving from foreground into the focal subject; subject placed near the golden-ratio visual center.

## Spatial structure rules

Every prompt must contain a spatial-depth phrase.

### Foreground / middle ground / background layering

Chinese: 前景为[物体/光影/虚化遮挡]，中景为主体，远景为[环境/地平线/建筑/海面]；前景、中景、远景层次清晰，空间纵深自然展开。

English: foreground contains [object/light/shadow blur], middle ground holds the subject, background recedes into [environment/horizon/buildings/sea]; clear foreground, middle ground, and background separation.

### Deep focus / deep staging

Chinese: 深景构图，前景、中景、远景都有可读信息但主体焦点最清晰；深焦拍摄感，空间从近处延伸到远处。

English: deep staging composition, foreground, middle ground, and background all readable while the subject remains the clearest focal point; deep-focus real-camera feeling.

### Shallow depth / subject isolation

Chinese: 浅景深，焦点落在人物眼睛/产品标识/主体轮廓，背景柔和退后；近景拍摄，前景轻微虚化，主体清晰，远景化为柔和色块。

English: shallow depth of field, focus locked on the eyes/product label/main silhouette, background gently receding; soft foreground blur, crisp subject, distant background reduced to soft color blocks.

### Long shot / establishing shot

Chinese: 远景/大全景拍摄，人物在巨大环境中显得渺小，空间尺度清晰；广角远景，前景地面纹理引出空间，远景地平线承托情绪。

English: long shot / wide establishing shot, the figure appears small within a vast environment; wide-angle distant shot, foreground ground texture leads into space, horizon supports the mood.

### Medium shot

Chinese: 中景拍摄，保留人物上半身和环境关系，动作与空间同时清楚。

English: medium shot, preserving the upper body and environmental relationship, action and space both readable.

### Close-up / detail focus

Chinese: 近景/特写拍摄，焦点集中在[眼睛/手部/物件细节]，背景退成柔和氛围。

English: close-up / detail shot, focus concentrated on [eyes/hands/object detail], background receding into soft atmosphere.

## Focal point rules

Portrait/person: focus on eyes and micro-expression.
Full-body person: focus on face, with body movement as secondary visual cue.
Action scene: focus on mid-action subject and body/gesture tension.
Product: focus on product label, silhouette highlight, or key material.
Animal: focus on eyes and head silhouette.
Landscape: focus on horizon, vanishing point, architectural silhouette, or light source.
Architecture/interior: focus on vanishing point or spatial axis.
Sci-fi/space: focus on scale relationship between figure and vast structure.

## Mandatory prompt formula

Chinese: 构图：[构图规则]；空间结构：[前景/中景/远景或景深说明]；焦点：[主体焦点]。

English: Composition: [composition rule]; spatial structure: [foreground/middle/background or depth-of-field structure]; focal point: [subject-specific focal point].

## Quality check

Before returning any prompt, ensure:

- A professional composition rule is named.
- Foreground, middle ground, and background or depth-of-field structure is described.
- The focal point is assigned to the correct subject feature.
- The focus hierarchy has only one primary focal point.
- Composition supports the emotion and story instead of being generic.
