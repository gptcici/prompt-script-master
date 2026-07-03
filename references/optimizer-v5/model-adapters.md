# Model Adapters

This skill is for **OpenAI image-family generation, including GPT-image, image, image2, and future OpenAI image models only**.

## Core rule

Always produce prompts in natural language suitable for OpenAI image-family. Do not output Midjourney, Stable Diffusion, ComfyUI, or Flux formats.

If the user mentions another model:
- Do not generate Midjourney parameters such as `--ar`, `--style`, `--v`, `--s`, or `--no`.
- Do not generate Stable Diffusion / SDXL two-column prompt blocks.
- Do not generate ComfyUI node/module structures.
- Do not generate Flux-specific prompt formats.
- Convert the request into an OpenAI image-family natural-language prompt unless the user explicitly asks not to use this skill.

## Internal reference-library safety

Prompts may not contain bundled reference-library or composition-library content. Do not write internal filenames, card names, source-image subjects, exact locations, watermarks, visible text, or copied scene descriptions into normal prompts. Use only generalized camera-capture principles learned from the libraries and adapt them to the user's own scene.

## OpenAI image-family prompt style

Use complete, direct sentences that describe a believable photographed frame.

A good OpenAI image-family prompt should include:
1. Reference-image role and priority, when references exist.
2. Subject identity and face-lock instruction, when a face reference exists.
3. Scene and action beat.
4. One style anchor plus 3 to 5 concrete visual traits when a style is requested.
5. Emotional beat for AIMV / short-drama continuity.
6. Real location or production-design logic.
7. Real light sources and exposure behavior.
8. Camera position, lens feeling, shot size, and aspect ratio when useful.
9. Physical material behavior: skin, hair, fabric, props, set, smoke, reflections, crowd, dust, rain, or light.
10. Positive anti-AI realism controls, written as desired qualities rather than denial syntax.

## No separate denial field

OpenAI image-family prompts should not include a separate denial field. Translate prevention into positive goals.

Examples:
- Instead of `no plastic skin`, write `skin keeps natural pores, subtle uneven tone, and stage-light color spill`.
- Instead of `no AI look`, write `the frame feels like a real behind-the-scenes or live-event photo captured under actual lighting constraints`.
- Instead of `no concept art`, write `all futuristic elements appear as physical props, LED panels, practical lights, costumes, and set pieces filmed by a real camera`.

## Aspect ratio language

Use natural aspect-ratio instructions when useful:
- `16:9 horizontal frame` for AIMV / short-drama establishing shots, concert stages, dialogue scenes, action scenes.
- `9:16 vertical frame` for short-video character shots or phone-native AIMV material.
- `4:5 vertical editorial frame` only when the user asks for poster/profile/social-style framing.
- `1:1 square frame` only when requested.

Do not add Midjourney-style aspect-ratio parameters.

## Direct image generation

If the user asks to generate an image, use the optimized OpenAI image-family prompt internally with the image tool. Preserve reference roles and aspect ratio. Do not answer with prompt text only.
