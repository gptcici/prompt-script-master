# Seedance Close-Up Face Lighting Rules

## Purpose

Make close-up faces realistic by avoiding flat all-face lighting.

## Four-layer face lighting formula

`main light direction + bone-following light/shadow + micro detail + environment bounce`.

## Layer 1: main light anchor

Name the incoming direction, softness/hardness, and color temperature. Examples: 45-degree side-front warm soft light, cold side light, single-side candle light, red-blue neon side light.

## Layer 2: bone-following structure

Place light on concrete facial areas: nose bridge highlight, nose-side shallow shadow, eye socket shadow with detail, cheekbone brightest point, jawline soft shadow boundary, cheek transition without hard breaks.

## Layer 3: micro detail

Add catchlight, natural skin texture, subtle lip sheen, brow-bone highlight, hair-edge glint. Avoid plastic smoothing.

## Layer 4: environment bounce

Use weak bounce from wall, snow, desk, clothing, water, stone, or neon reflection. It may lift the jaw/chin/neck but must remain secondary.

## Red lines

Do not write `全脸打亮`, `面部光线均匀`, or only `面光柔和`. Use positive body text; put residual failures such as flat face, dead-black shadows, overexposure, and plastic skin in a compact negative prompt if needed.

## Related

- Library: `seedance-closeup-face-lighting-library.md` — 40 curated close-up face lighting presets (F001-F040)
- Rules: `seedance-real-lighting-rules.md` — general four-layer lighting formula
