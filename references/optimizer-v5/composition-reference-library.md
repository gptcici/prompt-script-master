# Composition Pattern Library

This file is a **text-only** composition pattern library. The no-assets install package does not include bundled reference images, uploaded composition cards, or local media paths.

## Purpose

Use these patterns to improve AIMV / AI short-drama shot composition for OpenAI image-family prompts and Seedance keyframes. The patterns describe reusable camera and blocking principles only.

The library teaches the skill how to design frames that feel shot by a real director of photography:

- actor blocking inside a real location
- camera height and camera distance
- foreground occlusion and frame-within-frame
- leading lines that exist naturally in the set
- realistic negative space and headroom
- believable crowd/stage/environment scale
- depth layering across foreground, subject plane, and background
- short-drama continuity across close-up, medium shot, wide shot, and insert shot
- AIMV lyric-frame rhythm without becoming poster-like

## No bundled asset dependency

Do not look for, request, or cite any bundled files inside a bundled media directory. This package intentionally removes internal reference images and videos.

When the user uploads a reference image, first use the user's upload according to `reference-fidelity-system.md` and `character-sheet-continuity-system.md`. When no reference image is available, use only the text patterns below and general cinematography rules.

## Pattern quarantine

These patterns are internal method references only. Do not mention the library name, pattern IDs, internal headings, or rule-file names in normal final prompt output. Translate the pattern into the user's own subject, scene, action, and emotion.

## Hierarchy

Composition patterns are shot-design references only.

Priority order:

1. User instruction
2. Uploaded face reference and identity lock
3. 100% real-camera realism
4. Story/action/emotion beat
5. Text-only composition pattern
6. General composition rules
7. Aesthetic flourish

Never let a composition pattern override face lock, realistic physics, camera plausibility, or the user's scene.

## How to use composition patterns

When a user asks for a scene prompt and provides no specific composition, select the closest pattern from this file and translate it into fresh prompt language.

Do:
- describe subject placement in the frame
- define camera height and shot size
- define foreground / middle ground / background
- name only one primary focal point
- keep the composition physically shootable
- use composition to support the emotion and story beat
- translate patterns into generic shot-design instructions matched to the user's scene

Do not:
- copy a pattern as a rigid template
- mention pattern names or internal file names in prompts
- turn the image into a graphic poster or concept-art layout
- use impossible overhead/drone/stage angles unless the user asks and the shot could be captured by a real camera
- make all layers equally sharp or equally important

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

## Related

- Rules: `composition-space-structure.md` — governs spatial depth, focal hierarchy, and physically shootable frame design
- Rules: `cinematic-camera-language.md` — governs camera placement, shot size, and lens-language phrasing
