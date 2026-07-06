# Golden Tests

## Global pass standard

A final video prompt passes when it uses the current standard:

- `【正文提示词】` + `【负面提示词】`.
- Medium length with strong anchors, not extreme short and not long repetitive director notes.
- Reference roles are explicit.
- One global physical light anchor exists.
- One global wind/motion anchor exists when moving materials are present.
- Multi-shot videos have clear time ranges and cut points.
- Each shot compactly covers camera, action, and light/wind/depth/environment behavior.
- Negative prompt is categorized and compact.

## Test 1: low-information singing request

User: 一个女孩在唱歌

Pass: ask confirmation questions first; do not directly output final prompt unless user authorizes direct mode.

## Test 2: Seedance multi-shot reference prompt

Pass: output a medium-length prompt with reference roles, global light anchor, global wind/motion anchor, 5-7 shot timeline, and categorized negative prompt.

## Test 3: prompt audit

Pass: identify missing anchors, excessive length, unclear shot cuts, light-direction conflicts, wind-direction conflicts, and negative wording in the main prompt.

## Test 4: product video

Pass: use the same structure but adapt anchors to product, material, reflection, camera, and scene consistency.

## Test 5: storyboard / MV workflow

Pass: respect confirmation workflow first; final output uses clear shot order, camera/action/environment per shot, and concise negative prompt.
