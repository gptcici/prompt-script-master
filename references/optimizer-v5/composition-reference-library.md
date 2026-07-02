# Composition Reference Library

This file is the text index for a dedicated composition-reference library.

Image files live in:

```text
assets/composition-library/
```

## Purpose

Use this library to improve **AIMV / AI short-drama shot composition** for OpenAI image-family prompts. It is separate from the realism reference library.

The composition library teaches the skill how to design frames that feel shot by a real director of photography:

- actor blocking inside a real location
- camera height and camera distance
- foreground occlusion and frame-within-frame
- leading lines that exist naturally in the set
- realistic negative space and headroom
- believable crowd/stage/environment scale
- depth layering across foreground, subject plane, and background
- short-drama continuity across close-up, medium shot, wide shot, and insert shot
- AIMV lyric-frame rhythm without becoming poster-like

## Library-content quarantine

This library is internal only. Its images, filenames, labels, visible subjects, exact scenes, exact props, exact locations, watermarks, creator names, signatures, and literal text must **never** appear in normal prompt output.

Use this library only to infer abstract composition principles, then rewrite those principles into the user's own scene. Acceptable prompt language includes phrases such as: low camera height, strong foreground occlusion, natural frame-within-frame, centered vanishing point, broad negative space, small figure in a large environment, layered foreground/midground/background, macro insert framing, or reflection-based symmetry.

Do not write phrases that reveal the library image content, such as the exact landscape, object, city, tree, aircraft, bench, road, snowfield, waterfall, or any other visible subject from the library unless the user independently asked for that same subject.

## Hierarchy

Composition references are **shot-design references only**.

Priority order:

1. User instruction
2. Uploaded face reference and identity lock
3. 100% real-camera realism
4. Story/action/emotion beat
5. Composition reference library
6. General composition rules
7. Aesthetic flourish

Never let a composition reference override face lock, realistic physics, camera plausibility, or the user's scene. The final prompt should never say that it is using this library or name any internal card.

## How to use composition references

When a user asks for a scene prompt and provides no specific composition, select the closest composition pattern from this index and translate it into fresh prompt language.

Do:
- describe subject placement in the frame
- define camera height and shot size
- define foreground / middle ground / background
- name only one primary focal point
- keep the composition physically shootable
- use composition to support the emotion and story beat
- translate library examples into generic shot-design instructions matched to the user's scene

Do not:
- copy exact layout as a rigid template
- copy text, watermark, logo, username, creator marks, filenames, or card names
- mention the library image's exact objects, locations, or scenes in prompts
- turn the image into a graphic poster or concept-art layout
- use impossible overhead/drone/stage angles unless the user asks and the shot could be captured by a real camera
- make all layers equally sharp or equally important

## Composition-card template

Use this format when adding uploaded composition images:

```markdown
### comp-01: [short descriptive name]

- file: `assets/composition-library/comp-01-[slug].webp`
- category: [portrait / dialogue / stage / classroom / cafe / exterior / action / insert / crowd / fantasy-real]
- shot type: [close-up / medium shot / full shot / wide / establishing / insert]
- composition lesson: [what this image teaches about framing]
- camera placement: [height, distance, angle, lens-feeling]
- blocking cues: [where the subject sits/stands/moves; how other people/objects support the frame]
- depth cues: [foreground, subject plane, background, occlusion, haze, leading lines]
- realism guardrail: [what makes this composition feel camera-captured rather than AI-designed]
- use when: [scene types]
- do not copy: [identity / exact layout / visible subjects / text / logo / watermarks / stylized artifacts]
```

## Built-in composition patterns

Use these patterns even before user uploads a dedicated composition set.

### pattern-01: grounded eye-level medium shot

- category: short-drama / dialogue / daily life
- shot type: medium shot
- composition lesson: Keep the camera near human eye level, allow imperfect headroom, and place the actor slightly off-center so the location feels real rather than staged.
- camera placement: 35mm or 50mm lens feeling, eye-level or slight handheld height, camera close enough for emotion but wide enough to keep environment readable.
- blocking cues: Actor occupies one side or center-left/right; props, doorway, desk, or wall edges create natural frame weight.
- depth cues: soft foreground object, subject plane, readable but not overly sharp background.
- realism guardrail: Avoid perfect symmetry unless the location naturally supports it.
- use when: dialogue, confession, classroom, cafe, bedroom, office, daily short-drama scenes.

### pattern-02: close-up with motivated occlusion

- category: emotional close-up / AIMV lyric frame
- shot type: close-up
- composition lesson: A realistic close-up feels stronger when part of the frame is blocked by hair, fabric, window edge, shoulder, pillow, microphone, or another physical object.
- camera placement: 50mm or 85mm lens feeling, close camera distance, shallow depth but not beauty-retouched perfection.
- blocking cues: Face is the focal point; foreground occlusion proves camera proximity.
- depth cues: foreground blur, eyes/face plane, soft background.
- realism guardrail: Keep skin texture, uneven light, and natural eye catchlights.
- use when: emotional beats, music-video close-ups, face-reference shots, intimate short-drama moments.

### pattern-03: wide establishing shot with small human scale

- category: location / atmosphere / transition
- shot type: wide / establishing
- composition lesson: Place the person small in a real location so scale, mood, and environment carry the story.
- camera placement: 24mm or 35mm lens feeling, tripod or stable handheld viewpoint, real horizon and vertical lines.
- blocking cues: Subject is small but identifiable by silhouette, wardrobe, or movement.
- depth cues: foreground ground/texture, middle subject, background architecture/forest/stage/environment.
- realism guardrail: Keep distant detail uneven and exposure-limited; avoid fantasy matte-painting sharpness.
- use when: loneliness, arrival, performance scale, memory, transitions, travel, exterior scenes.

### pattern-04: frame-within-frame from real architecture

- category: doorway / window / vehicle / corridor / stage wing
- shot type: medium or wide
- composition lesson: Use existing architecture as a natural frame around the subject instead of artificial poster framing.
- camera placement: 35mm lens feeling, camera partly behind a doorframe, window, curtain, car seat, stage truss, or corridor wall.
- blocking cues: Subject appears through the frame; edge obstruction adds realism and voyeuristic short-drama feeling.
- depth cues: dark foreground frame, subject in midground, background light or location detail.
- realism guardrail: Foreground edges can be out of focus or underexposed.
- use when: secret observation, loneliness, entering rooms, stage backstage, cafe windows, train/car interiors.

### pattern-05: leading-line runway / corridor / road shot

- category: movement / concert / corridor / road
- shot type: full shot or wide
- composition lesson: Use real floor lines, runway edges, corridor walls, seats, rails, or light strips to guide the eye toward the subject.
- camera placement: 24mm or 35mm lens feeling, low or eye-level perspective aligned with the real physical axis.
- blocking cues: Subject stands or moves at the convergence point; crowd/props stay secondary.
- depth cues: foreground floor/lines, midground subject, background lights/environment.
- realism guardrail: Lines must come from physical set elements, not graphic overlays.
- use when: concert T-stage, school hallway, street walking, subway platform, sci-fi set built as real corridor.

### pattern-06: crowd insert with imperfect focus hierarchy

- category: concert / event / public space
- shot type: medium crowd insert
- composition lesson: Real crowd frames have uneven faces, blocked sightlines, local overexposure from phones/light sticks, and no single perfect symmetrical arrangement.
- camera placement: 35mm or 50mm lens feeling from within the audience or aisle, slight handheld viewpoint.
- blocking cues: One or two audience members can be readable while many others become supporting texture.
- depth cues: foreground hands/light sticks, midground faces, background stage lights falling out of focus.
- realism guardrail: Vary expressions, head angles, phone positions, and focus softness.
- use when: concert audience, fan reactions, public gatherings, crowd cutaways.

### pattern-07: insert shot with texture and time-of-day cue

- category: insert / transition / environment detail
- shot type: close-up or detail
- composition lesson: A non-character insert can carry realism through texture, light, and time-of-day continuity.
- camera placement: 50mm or macro/detail lens feeling, shallow depth, close to a wall, table, hand, fabric, object, water reflection, or shadow.
- blocking cues: No need for a face; the subject can be an object, light patch, hand, door, microphone, cup, costume detail, or moving shadow.
- depth cues: tactile foreground detail, soft background falloff.
- realism guardrail: Avoid decorative perfection; include dust, scratches, fingerprints, uneven shadow, or slight exposure bloom where plausible.
- use when: AIMV transition cuts, short-drama continuity, scene breathing space, emotional pauses.

### pattern-08: practical sci-fi composition

- category: sci-fi-real / fantasy-real / VFX plate
- shot type: close-up, medium, or wide
- composition lesson: Unreal elements become believable when staged like physical props, costumes, LED panels, projection, live-event lighting, or VFX plates photographed on set.
- camera placement: Use normal real-camera positions first; reserve impossible viewpoints for deliberate drone/crane shots.
- blocking cues: Actor physically interacts with the object/costume/set; contact shadows and occlusion matter.
- depth cues: foreground practical object, actor plane, real set or haze in background.
- realism guardrail: Keep reflections, shadows, scale cues, and exposure limits consistent with the camera.
- use when: futuristic armor, glowing props, magical effects, giant stage devices, cyberpunk short drama.

## Uploaded composition cards

These uploaded images are stored in the composition library only. They are not realism-library items. Do not use their visible subject matter inside normal prompts unless the user asks for that subject independently.

### comp-01: translucent foreground surface with distant silhouette

- file: `assets/composition-library/comp-01-frosted-window-sunset-silhouette.webp`
- category: insert / exterior / frame barrier
- shot type: insert / establishing detail
- composition lesson: Let a textured foreground layer dominate the frame while the distant environment stays soft behind it; the frame becomes about separation and atmosphere.
- camera placement: camera close to a transparent or semi-transparent surface, focus biased toward the foreground layer, distant subject/background defocused.
- blocking cues: The main world sits behind a physical barrier; human or location details should remain secondary.
- depth cues: tactile foreground texture, soft middle silhouette, color band or horizon in the background.
- realism guardrail: The foreground texture must be a real surface and not decorative overlay.
- use when: memory inserts, window shots, separation, winter/cold mood, quiet transitions.
- do not copy: exact window pattern, exact building silhouette, exact sunset colors, any visible artifacts.

### comp-02: organic foreground frame with distant subject

- file: `assets/composition-library/comp-02-orchard-foreground-branches-depth.webp`
- category: exterior / travel / lyric frame
- shot type: wide / full shot
- composition lesson: Use close foreground elements to wrap the frame and place the subject small inside a deeper environment.
- camera placement: wide lens feeling, camera partly inside foreground foliage or set dressing, subject placed deeper in the frame.
- blocking cues: Subject stands or moves beyond the foreground frame; background repeats create depth.
- depth cues: soft foreground occlusion, midground actor, repeating background rows or structures.
- realism guardrail: Foreground occlusion must feel accidental and physical, not a graphic border.
- use when: romantic exterior, memory walk, character alone in a location, AIMV seasonal shots.
- do not copy: exact flowers, orchard layout, dress, or location.

### comp-03: long-shadow field composition

- file: `assets/composition-library/comp-03-snow-field-long-tree-shadows.webp`
- category: exterior / scale / graphic shadow
- shot type: wide / establishing
- composition lesson: Use long natural shadows as leading lines and scale markers across a simple ground plane.
- camera placement: elevated or high viewpoint that could come from a hill, balcony, drone, or crane.
- blocking cues: Subjects can be placed small against the shadow pattern to emphasize isolation.
- depth cues: foreground ground texture, stretching shadow field, tree/location line in the background.
- realism guardrail: Shadows must come from a clear low-angle light source and obey surface shape.
- use when: loneliness, transition, winter/exterior scale, symbolic lyric frames.
- do not copy: exact snowfield, trees, signature, or winter landscape.

### comp-04: low foreground motion into background frame

- file: `assets/composition-library/comp-04-waterfall-low-angle-frame.webp`
- category: exterior / action / environment
- shot type: low-angle wide
- composition lesson: Put a moving foreground plane at the bottom of frame and let it lead upward into a framed background.
- camera placement: very low camera near moving ground/water/fabric/road surface, lens angled slightly upward.
- blocking cues: Foreground movement creates energy while background holds the scene destination.
- depth cues: moving foreground texture, middle threshold, background vertical environment.
- realism guardrail: Motion softness must match real shutter behavior, not artificial blur streaks.
- use when: movement transitions, chase beats, emotional exterior, dramatic approach shots.
- do not copy: exact waterfall, snow-covered trees, or landscape.

### comp-05: centered road-axis vanishing point

- file: `assets/composition-library/comp-05-snow-road-central-leading-lines.webp`
- category: road / travel / approach
- shot type: wide / establishing
- composition lesson: Center the physical path so tire marks, rails, floor seams, or runway lines pull the viewer toward a distant subject.
- camera placement: camera above or on the path axis, 24mm/35mm feeling, stable viewpoint.
- blocking cues: Subject or vehicle sits near the convergence point; side elements form a corridor.
- depth cues: strong foreground lines, midground subject, background haze/forest/buildings.
- realism guardrail: Lines must be real tracks or set elements with natural perspective convergence.
- use when: arrival, departure, road scenes, T-stage approach, hallway movement.
- do not copy: exact road, car, snow, or forest.

### comp-06: compressed geometric rooftops / pattern field

- file: `assets/composition-library/comp-06-snow-rooftop-geometric-pattern.webp`
- category: city / architecture / pattern
- shot type: elevated wide / establishing
- composition lesson: Use repeating roofs, windows, platforms, seats, or set modules as a compressed pattern while a few warm accents guide attention.
- camera placement: elevated telephoto or high-angle viewpoint that flattens space.
- blocking cues: Human subjects can be small or absent; the location pattern carries the scene.
- depth cues: overlapping planes, repeated geometric shapes, selective warm points.
- realism guardrail: Keep imperfect spacing and real-world clutter; avoid perfect computer tiling.
- use when: city establishing shots, venue scale, campus roofs, dense neighborhood scenes.
- do not copy: exact buildings, roof colors, or city identity.

### comp-07: vertical texture wall with top negative space

- file: `assets/composition-library/comp-07-mountain-vertical-texture-wall.webp`
- category: landscape / scale / abstract exterior
- shot type: wide / texture establishing
- composition lesson: Fill the frame with a large vertical surface and leave a thin top band to show scale and orientation.
- camera placement: distant telephoto or aerial/crane-like viewpoint facing a vertical plane.
- blocking cues: Small human/vehicle details, if used, should emphasize scale rather than become the main subject.
- depth cues: large patterned plane, vertical grooves or structural lines, minimal sky or horizon.
- realism guardrail: Texture must follow real material contours and light direction.
- use when: cliffs, stage walls, large fabric backdrops, architectural facades, sci-fi set surfaces.
- do not copy: exact mountain, snow texture, or natural formation.

### comp-08: steep urban vanishing point

- file: `assets/composition-library/comp-08-city-street-vanishing-point.webp`
- category: city / road / action
- shot type: low wide / street axis
- composition lesson: Use a street, corridor, aisle, or runway as a deep central axis framed by vertical side walls.
- camera placement: low or mid-height camera on the axis, wide lens feeling, looking toward a distant point.
- blocking cues: Subject may be centered at the far convergence point or moving along the axis.
- depth cues: foreground pavement/rail lines, vertical side structures, distant endpoint.
- realism guardrail: Keep lens distortion plausible and scene edges not overly graphic.
- use when: city chase, walking toward camera, school hallway, concert runway, dramatic arrival.
- do not copy: exact city, bridge, road markings, or color treatment.

### comp-09: foreground rhythm leading to hero shape

- file: `assets/composition-library/comp-09-snow-mounds-foreground-leading-rhythm.webp`
- category: exterior / low-angle scale / journey
- shot type: low wide
- composition lesson: Use repeated foreground shapes to create a stepping rhythm toward a taller midground subject.
- camera placement: low camera close to foreground forms, wide lens feeling, horizon kept clean.
- blocking cues: The repeated forms guide the eye to the final subject or group.
- depth cues: oversized foreground shapes, midground hero shape, distant open sky/location.
- realism guardrail: Foreground forms need varied size and natural imperfection.
- use when: stage props, rocks, snow, crowd heads, seats, corridor lamps, symbolic movement.
- do not copy: exact snow sculptures or landscape.

### comp-10: wide negative-space horizon

- file: `assets/composition-library/comp-10-winter-lake-wide-negative-space.webp`
- category: exterior / quiet establishing / negative space
- shot type: panoramic wide
- composition lesson: Keep the frame calm by placing the horizon and main subject low or off-center, allowing open space to carry mood.
- camera placement: locked-off wide camera, low-to-mid height, stable horizontal frame.
- blocking cues: A small figure or object can sit near one side while the environment breathes.
- depth cues: foreground ground plane, middle water/field, background ridge/sky.
- realism guardrail: Exposure and detail should fall off naturally in haze or distance.
- use when: reflective lyric moments, loneliness, ending shots, landscape transitions.
- do not copy: exact lake, cabin, watermark, or mountain.

### comp-11: repeating circular frame and ground-level leading lines

- file: `assets/composition-library/comp-11-bench-rings-frame-leading-lines.webp`
- category: frame-within-frame / urban / insert
- shot type: low wide / detail establishing
- composition lesson: Let repeated circular or rectangular structures frame the vanishing point while floor planks or rails add directional lines.
- camera placement: ground-level or object-level camera, wide lens, close to a real structure.
- blocking cues: Subject can appear small inside the repeated frames.
- depth cues: near frame ring, repeated middle frames, distant background light.
- realism guardrail: Structural frames must be physical objects in the set, not graphic overlays.
- use when: docks, corridors, railings, stage trusses, cafe furniture, playgrounds.
- do not copy: exact bench, waterfront, skyline, or sunset.

### comp-12: side-frame tree/branch occlusion

- file: `assets/composition-library/comp-12-snow-branch-side-frame.webp`
- category: exterior / landscape / natural frame
- shot type: wide / establishing
- composition lesson: Use a large foreground element on one edge to frame the open environment and guide the eye toward light.
- camera placement: wide camera slightly behind or beside a foreground object.
- blocking cues: Subject may occupy the open space opposite the frame edge.
- depth cues: dark foreground edge, open midground, far horizon or light source.
- realism guardrail: Foreground silhouette and shadow must match the scene light.
- use when: outdoor drama, search, arrival, quiet view, stage wing framing.
- do not copy: exact snowy trees or landscape.

### comp-13: forced perspective with hand and distant object

- file: `assets/composition-library/comp-13-hand-airplane-foreground-scale.webp`
- category: insert / playful perspective / object interaction
- shot type: close-up insert
- composition lesson: Use a near foreground hand/object aligned with a distant moving object to create a real optical relationship.
- camera placement: handheld upward or skyward angle, close focus on foreground hand/object.
- blocking cues: Foreground gesture dominates; background object remains secondary but readable.
- depth cues: near hand, distant object, clean sky/negative space.
- realism guardrail: Scale illusion must come from camera alignment, not impossible contact.
- use when: playful inserts, object metaphors, phone-native AIMV shots, travel memories.
- do not copy: exact aircraft, watch, hand pose, or sky composition.

### comp-14: foreground mounds into solitary background subject

- file: `assets/composition-library/comp-14-snow-mounds-solitary-tree-depth.webp`
- category: exterior / quiet depth / loneliness
- shot type: low wide
- composition lesson: Let soft foreground forms occupy most of the frame while a small solitary subject anchors the upper third.
- camera placement: low camera close to textured ground, wide lens, horizon above midline.
- blocking cues: A lone actor/object can become the emotional endpoint of the frame.
- depth cues: foreground texture masses, midground gap, distant subject and horizon.
- realism guardrail: Ground forms need real material texture and natural light falloff.
- use when: loneliness, memory, scenic AIMV stills, contemplative transitions.
- do not copy: exact tree, frozen lake, watermark, or snow landscape.

### comp-15: macro line abstraction

- file: `assets/composition-library/comp-15-frost-lines-macro-abstract.webp`
- category: insert / macro / texture
- shot type: macro detail
- composition lesson: Use repeated close-up lines to create an abstract insert that still feels like a real object.
- camera placement: macro/detail lens feeling, shallow depth, camera almost parallel to the textured plane.
- blocking cues: No actor needed; the line direction can bridge scenes or emotions.
- depth cues: near texture line, soft background color field, shallow focus edge falloff.
- realism guardrail: Keep the texture tied to a real surface; do not turn it into generated pattern art.
- use when: cutaways, time passage, cold mood, object detail, emotional pauses.
- do not copy: exact frost pattern or color field.

### comp-16: asymmetric street subject with open urban space

- file: `assets/composition-library/comp-16-monochrome-street-asymmetric-subject.webp`
- category: street / dialogue / short-drama
- shot type: wide medium / street establishing
- composition lesson: Place the subject off to one side while the empty street and distant background create story tension.
- camera placement: eye-level or slightly low street camera, 35mm feeling, stable frame.
- blocking cues: Subject is not centered; secondary elements provide scale and realism.
- depth cues: foreground street texture, subject plane, deep city background.
- realism guardrail: Leave imperfect street clutter and asymmetry; avoid overly polished poster balance.
- use when: urban solitude, waiting, departure, street conversation, daily drama.
- do not copy: exact vehicle, dog, storefronts, or monochrome treatment.

### comp-17: upward radial forest / overhead convergence

- file: `assets/composition-library/comp-17-upward-forest-radial-lines.webp`
- category: upward view / scale / dramatic reveal
- shot type: overhead-looking-up wide
- composition lesson: Shoot upward through vertical structures so they converge toward the center and make a small subject feel far away.
- camera placement: camera on the ground looking up, ultra-wide but physically plausible lens behavior.
- blocking cues: A small person/object can sit high in the frame to show scale.
- depth cues: foreground vertical trunks/structures, upper bridge/ceiling/sky, tiny subject.
- realism guardrail: Use only when a camera could physically lie beneath or look upward from the location.
- use when: awe, discovery, forest/stage rig/architecture, power imbalance.
- do not copy: exact trees, bridge, or red figure.

### comp-18: small figure in heavy negative space

- file: `assets/composition-library/comp-18-snowfall-person-negative-space.webp`
- category: negative space / human scale / weather
- shot type: wide / full shot
- composition lesson: Let a single figure occupy the lower frame while weather or atmosphere fills the majority of the image.
- camera placement: medium-to-long distance, eye-level or slight telephoto feeling, stable frame.
- blocking cues: Subject faces into the empty space; action is simple and readable.
- depth cues: foreground ground edge, small subject, large atmospheric background.
- realism guardrail: Weather particles should vary in size and focus with depth.
- use when: loneliness, waiting, walking away, lyric pauses, short-video vertical shots.
- do not copy: exact umbrella, clothing colors, or snow setting.

### comp-19: natural cave/frame opening toward horizon

- file: `assets/composition-library/comp-19-ice-cave-natural-frame.webp`
- category: frame-within-frame / exterior / reveal
- shot type: wide establishing
- composition lesson: Use dark near-side forms as a natural frame and reveal a bright open middle view beyond them.
- camera placement: low-to-mid camera inside or behind a physical opening, 24mm/35mm feeling.
- blocking cues: Subject or destination can sit beyond the frame opening.
- depth cues: dark foreground frame, midground surface, background horizon/sky.
- realism guardrail: Foreground frame must cast real occlusion and not become decorative border art.
- use when: reveal shots, entering a new world, stage-wing-to-stage transitions, cave/window/door compositions.
- do not copy: exact ice cave, mountain, or frozen landscape.

### comp-20: reflection symmetry from a real surface

- file: `assets/composition-library/comp-20-puddle-reflection-city-symmetry.webp`
- category: urban / reflection / low angle
- shot type: low wide / establishing insert
- composition lesson: Place the camera close to a reflective surface to create a believable mirrored lower half and a grounded upper half.
- camera placement: very low camera near wet ground, wide lens feeling, aligned with architecture or subject axis.
- blocking cues: Main structure or actor can be mirrored; reflection should be imperfect and physically distorted.
- depth cues: wet foreground reflection, subject/building plane, sky/background.
- realism guardrail: Reflections must ripple, distort, darken, or break according to the real surface.
- use when: city drama, rain scenes, emotional transitions, stage floor reflections, night exteriors.
- do not copy: exact city, building, puddle, or sunset.

## Intake workflow for uploaded composition images

When the user uploads composition reference images:

1. Save or convert them into `assets/composition-library/` using `scripts/prepare_composition_library.py`.
2. Give each file a short descriptive slug.
3. Visually inspect every image.
4. Add one composition card per image to this index.
5. Tag each card by shot type and use case.
6. State that the library uses these images only for composition, not face identity, realism-library content, prompt content, or style ownership.
7. Keep package size below 25 MB; compress or reduce image dimensions when needed.

### comp-21: handheld foreground alignment with distant light source

- file: `assets/composition-library/comp-21-handheld-object-sun-alignment.webp`
- category: insert / exterior / forced-perspective
- shot type: close-up insert with distant background
- composition lesson: A small foreground object can be aligned with a distant light source to create a motivated visual metaphor while still feeling camera-captured.
- camera placement: camera close to the hand/object, shallow focus or split attention between tactile foreground and distant background.
- blocking cues: Foreground hand/object dominates one upper area; distant environment provides horizon and light path.
- depth cues: near silhouette/hand plane, middle atmosphere, far horizon/background glow.
- realism guardrail: Alignment must feel like a real optical perspective trick, not a pasted graphic overlay.
- use when: AIMV insert shots, memory beats, lyric symbolism, object-focused transitions.
- do not copy: exact object, sea, sunset alignment, hand pose, or location.

### comp-22: circular foreground aperture framing distant center

- file: `assets/composition-library/comp-22-circular-frame-night-water-symmetry.webp`
- category: frame-within-frame / night exterior / symmetry
- shot type: wide insert / establishing
- composition lesson: A circular or architectural foreground opening can create a clean frame-within-frame around a distant centered subject.
- camera placement: camera placed behind a physical aperture or set element, lens aligned with a central distant focal point.
- blocking cues: Main subject/environment sits inside the foreground shape; horizontal reflections or background lines stabilize the frame.
- depth cues: dark foreground frame, mid-distance water/ground plane, illuminated background subject.
- realism guardrail: The frame must be a real foreground object with visible thickness and exposure falloff.
- use when: entrances, stage reveals, city/night reveals, symbolic transitions, location establishing.
- do not copy: exact architecture, water scene, boat, lighting colors, or landmark.

### comp-23: off-center vertical foreground barrier with falling particles

- file: `assets/composition-library/comp-23-vertical-trunk-offcenter-snow-depth.webp`
- category: exterior / occlusion / weather texture
- shot type: medium insert / atmospheric detail
- composition lesson: A heavy vertical foreground element can divide the frame while background particles create depth and motion.
- camera placement: medium telephoto feeling, foreground element placed near center or off-center, background softly layered.
- blocking cues: Foreground vertical mass becomes the anchor; background remains atmospheric and secondary.
- depth cues: tactile foreground edge, drifting particles, soft repeating background forms.
- realism guardrail: Particle size and focus must vary naturally with distance.
- use when: suspense, hidden observation, weather inserts, quiet winter or night beats.
- do not copy: exact tree bark, snow scene, or forest.

### comp-24: diagonal sky lines with small moving subjects

- file: `assets/composition-library/comp-24-diagonal-overhead-lines-negative-sky.webp`
- category: open-space / diagonal / minimal insert
- shot type: upward insert / wide detail
- composition lesson: Thin diagonal lines can cut through a large negative-space background and give small moving subjects direction.
- camera placement: upward-looking camera, flat sky/background plane, long diagonal graphic structure.
- blocking cues: Small moving subjects are secondary accents placed around the diagonal line rhythm.
- depth cues: foreground/near line structure, distant background, tiny moving elements crossing the field.
- realism guardrail: Lines must be real wires/edges/architecture in perspective, not graphic overlays.
- use when: transitions, movement metaphors, outdoor pauses, quiet urban inserts.
- do not copy: exact birds, wires, building corner, or sky shape.

### comp-25: hard-shadow silhouette and block geometry

- file: `assets/composition-library/comp-25-hard-shadow-urban-silhouette-blocking.webp`
- category: street / silhouette / graphic shadow
- shot type: medium-wide observational shot
- composition lesson: Large shadow blocks can carve the frame and turn a simple human figure into a strong readable silhouette.
- camera placement: static or handheld street-level camera, subject placed in a hard-lit patch or shadow edge.
- blocking cues: Subject silhouette sits against a brighter background surface; architectural edges form the frame structure.
- depth cues: dark foreground wall/edge, subject silhouette plane, lit background wall.
- realism guardrail: Shadows must correspond to a clear hard sunlight source and real architecture.
- use when: short-drama tension, street cutaways, lonely character beats, surveillance-like observation.
- do not copy: exact person, scooter, wall, signage, or urban location.

### comp-26: monochrome organic vertical rhythm

- file: `assets/composition-library/comp-26-monochrome-organic-vertical-rhythm.webp`
- category: exterior / abstract blocking / rhythm
- shot type: wide environmental pattern
- composition lesson: Irregular vertical shapes can create a natural rhythm that feels less designed than perfect symmetry.
- camera placement: level or slightly telephoto viewpoint, repeated vertical elements layered into depth.
- blocking cues: A subject can be placed between irregular vertical forms to feel hidden or emotionally trapped.
- depth cues: foreground vertical marks, midground subject slot, atmospheric background layers.
- realism guardrail: Keep shape irregularity and haze natural; avoid decorative pattern overuse.
- use when: isolation, mystery, psychological short-drama scenes, quiet exterior transitions.
- do not copy: exact trees, snow, monochrome treatment, or landscape.

### comp-27: high-contrast hanging detail against negative space

- file: `assets/composition-library/comp-27-high-contrast-hanging-detail-negative-space.webp`
- category: insert / macro / negative space
- shot type: close-up detail
- composition lesson: A vertical hanging detail can dominate against a dark empty background, creating a clean insert with strong shape readability.
- camera placement: close camera distance, shallow depth, exposure set for the bright object while background falls dark.
- blocking cues: Detail hangs from top/edge; most of the frame remains quiet negative space.
- depth cues: sharp detail plane, falling particles or soft bokeh in the background.
- realism guardrail: Highlights must clip or bloom only where a real camera would; texture must not become over-rendered.
- use when: object inserts, cold tension, emotional pauses, lyric cutaways.
- do not copy: exact ice form, black background, or particle pattern.

### comp-28: overhead radial spacing and group pattern

- file: `assets/composition-library/comp-28-overhead-radial-spacing-group-pattern.webp`
- category: overhead / crowd or group / scale
- shot type: top-down wide
- composition lesson: A true overhead view can turn many small subjects into spacing rhythm while preserving large-scale environment.
- camera placement: drone/crane/top-down production angle only when plausible for the story.
- blocking cues: Multiple tiny subjects form a loose ring or scattered pattern; environment shapes frame the group.
- depth cues: flattened overhead plane with readable scale cues from shadows and surface texture.
- realism guardrail: Use only when an overhead camera is believable; avoid impossible omniscient viewpoints for intimate scenes.
- use when: crowd choreography, battle/escape pattern, dreamlike scale, transition maps, music-video overhead beats.
- do not copy: exact snowfield, animal/group type, or radial layout.

### comp-29: foggy minimal field with distant lone subject

- file: `assets/composition-library/comp-29-foggy-minimal-lone-subject-depth.webp`
- category: exterior / minimal / atmosphere
- shot type: wide establishing
- composition lesson: A small distant subject can carry emotion when placed inside a soft atmospheric field with large negative space.
- camera placement: low-to-eye-level wide lens feeling, stable camera, subject far from camera.
- blocking cues: Subject stands or moves near the horizon/vanishing zone; foreground remains quiet and empty.
- depth cues: textured foreground, fog-softened middle distance, nearly disappearing background.
- realism guardrail: Atmospheric fade must reduce contrast and detail naturally with distance.
- use when: loneliness, memory, waiting, disappearance, quiet transition.
- do not copy: exact tree, snow field, fog color, or landscape.

### comp-30: minimal horizon and color-field split

- file: `assets/composition-library/comp-30-minimal-horizon-large-negative-space.webp`
- category: landscape / open-space / minimal
- shot type: wide establishing
- composition lesson: A low horizon can create a calm color-field composition where negative space carries mood.
- camera placement: level camera with clean horizon, minimal foreground detail.
- blocking cues: Any human subject should be tiny or absent; the frame is about stillness and scale.
- depth cues: broad foreground plane, thin horizon band, large sky/empty field.
- realism guardrail: Keep the horizon physically level and exposure simple; avoid graphic poster gradients.
- use when: calm transitions, aftermath, travel, waiting, visual breathing space between scenes.
- do not copy: exact water/landscape, moon, color palette, or location.

### comp-31: overhead canopy as natural frame for small figure

- file: `assets/composition-library/comp-31-canopy-frame-small-figure.webp`
- category: exterior / natural frame / wide human scale
- shot type: wide full-body / establishing
- composition lesson: Dense overhead foreground can create a natural ceiling that frames a small figure below.
- camera placement: wide lens, camera inside or under a physical overhead frame, subject placed deeper inside the scene.
- blocking cues: Figure stays small and centered or slightly off-center to emphasize environment scale.
- depth cues: near overhead texture, subject plane, background openings and light leaks.
- realism guardrail: Overhead elements must show real occlusion and scale, not decorative border design.
- use when: discovery, wonder, arrival, hidden path, lyric wide shot.
- do not copy: exact snow-covered branches, costume, or location.

### comp-32: reflective vehicle/object frame revealing alternate view

- file: `assets/composition-library/comp-32-mirror-frame-road-depth.webp`
- category: vehicle / reflection / frame-within-frame
- shot type: insert / travel detail
- composition lesson: A reflective or framed object can hold one layer of the story while the surrounding frame holds another.
- camera placement: close to reflective object, focus on reflection or rim depending on story beat.
- blocking cues: Reflection contains the narrative direction; nearby object body and environment create foreground mass.
- depth cues: foreground reflective frame, reflected distance, soft exterior background.
- realism guardrail: Reflections must obey angle, distortion, and focus limits.
- use when: travel, escape, looking back, road continuity, memory inserts.
- do not copy: exact vehicle mirror, snowy road, mountain view, or car.

### comp-33: monumental triangular mass with low horizon

- file: `assets/composition-library/comp-33-monumental-triangle-low-horizon.webp`
- category: exterior / scale / iconic mass
- shot type: wide establishing
- composition lesson: A large triangular or pyramidal mass can dominate the frame when the horizon is kept low and foreground stays dark.
- camera placement: distant wide/telephoto viewpoint, stable camera, low horizon line.
- blocking cues: Human or vehicle scale cues should remain small and low in the frame if used.
- depth cues: dark foreground base, dominant middle-background mass, large empty sky.
- realism guardrail: Preserve atmospheric haze, distance falloff, and exposure limits so it feels photographed.
- use when: awe, obstacle, destiny, arrival at a large place, sci-fi/fantasy grounded as landscape plate.
- do not copy: exact mountain, blue color, village lights, or landscape.

### comp-34: central soft path leading to distant focal mass

- file: `assets/composition-library/comp-34-central-soft-path-to-distant-peak.webp`
- category: exterior / leading path / night or dawn scale
- shot type: wide establishing
- composition lesson: A soft central path can lead the viewer through empty foreground into a distant focal mass without needing a visible actor.
- camera placement: low wide lens feeling, camera close to ground texture, central axis aimed at distant subject.
- blocking cues: Path or surface ridge creates the main visual movement; distant focal shape anchors the horizon.
- depth cues: tactile foreground surface, central path, background focal mass, atmospheric sky.
- realism guardrail: Path must be formed by real terrain, tracks, light, or set elements rather than drawn lines.
- use when: journey, destiny, transition, lyric wide frame, dreamlike but realistic exterior.
- do not copy: exact snowy path, mountain, stars, or color palette.

### comp-35: paired foreground objects with hard light and deep shadow

- file: `assets/composition-library/comp-35-object-pair-hard-light-shadow.webp`
- category: insert / object / hard-light still life
- shot type: close-up / medium insert
- composition lesson: Two similar objects can create visual tension through uneven light, shadow split, and asymmetrical spacing.
- camera placement: close eye-level or slightly low detail shot, light from one side, background falling dark.
- blocking cues: Object pair occupies lower or middle frame; one catches more light than the other.
- depth cues: lit foreground surfaces, dark background, small highlight details.
- realism guardrail: Use real contact shadows, dust, scratches, and imperfect reflections; avoid product-ad perfection.
- use when: props, clues, scene transition, object symbolism, daily-life insert shots.
- do not copy: exact objects, color, wall, or arrangement.
