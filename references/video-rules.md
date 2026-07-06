# Video Rules

## Final prompt format

Final video prompts use:

```text
【正文提示词】
[positive prompt]

【负面提示词】
[categorized negative prompt]
```

Use `seedance2-concise-execution-standard.md` for the default execution standard.

## Timeline

For multi-shot videos, write clear time ranges and shot numbers. Use natural-language shot paragraphs. Each shot should include camera, action, and environment/light/motion information.

## Anchors

Always preserve the strongest anchors:
- reference roles;
- global light source;
- global wind/motion field when relevant;
- character/prop/architecture consistency;
- shot order and cut points.

## Main prompt language

Use positive, visible, executable language. Put failures, prohibitions, and model-error prevention in the negative prompt.
