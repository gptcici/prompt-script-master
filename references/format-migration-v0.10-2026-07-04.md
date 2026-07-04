# Format Migration: v0.9.6 → v0.10 (2026-07-04)

## What Changed

| Aspect | Old (v0.9.6) | New (v0.10) |
|--------|-------------|-------------|
| Output structure | Three-section: 全程总定调 / 时间轴分段 / 全局收尾 | Two-part: 正文提示词 + 负面提示词 |
| Timeline fields | 9 fields | 7 fields |
| Negatives | Inline in body text | Separate 负面提示词 block |
| Reference image | Vague ("上传定妆图作为参考") | Standardized @Image1 syntax |
| Abstract semantics | Allowed (心理感受, 导演思路) | Forbidden — must convert to concrete visual |
| Info organization | Scattered, repeated | Aggregated: fabric/fx in one place, lighting in one place, DoF at end |
| Weight marking | Undefined | Core nouns only, max 5 total |

## New Timeline Format (7 fields)

```
景别 + 运镜状态 + 人物核心动作 + 衣发纱幔动态 + 人物光影 + 环境细节 + 景深变化
```

vs old 9-field:
```
本段景别 + 本段运镜状态 + 焦点变化 + 核心动作 + 表情肢体联动 + 人物面光/骨骼光影 + 环境光影变化 + 环境细节补充 + 本段景深变化
```

## New Rules Added

1. **语序权重（黄金优先级）** — Spec+Reference+Character > Scene > Timeline > Style
2. **无效语义清理** — No director commentary, psychological feelings, logic explanations
3. **同类信息聚合** — Fabric/fx together, lighting together, DoF at paragraph end
4. **参考图标准化** — `@Image1 仅作为人物强参考...` fixed format
5. **权重标记** — Core nouns only, ≤5 total, no abstract/rule weighting
6. **负面提示词分离** — All negatives in dedicated block, zero negatives in body
7. **时间轴 7 项标准化** — Fixed field order per segment

## Files Updated (14 primary)

1. `SKILL.md` — Structure section rewritten + 7 new rule sections
2. `templates/video-prompt-template.md` — Complete rewrite
3. `references/timeline-execution-rules.md` — 9→7 fields + examples
4. `references/timeline-quality-gates.md` — 9→7 checklists
5. `references/templates.md` — Structure reference updated
6. `references/video-rules.md` — Timeline description updated
7. `references/quality-control.md` — Checklist 9→7 + new checks
8. `references/optimizer-v5/output-templates.md` — Template updated
9. `scripts/prompt_checker.py` — 9→7 validation logic
10. `scripts/prompt_wizard.py` — Output template updated
11. `docs/output-format.md` — Format docs updated
12. `docs/seedance2-full-reference.md` — Output format section updated
13. `docs/golden-tests.md` — Test standards 9→7
14. `README.md` — Quality gate description updated

## Snapshot Sync Status

### Synced (via terminal cp)
- `skill/prompt-script-master/templates/video-prompt-template.md` ✓
- `skill/prompt-script-master/references/timeline-execution-rules.md` ✓
- `skill/prompt-script-master/references/timeline-quality-gates.md` ✓
- `skill/prompt-script-master/references/video-rules.md` ✓
- `skill/prompt-script-master/references/templates.md` ✓
- `skill/prompt-script-master/scripts/prompt_checker.py` ✓
- `skill/prompt-script-master/scripts/prompt_wizard.py` ✓

### NOT Synced (skill_manage path limitation — requires terminal cp)
- `skill/prompt-script-master/docs/output-format.md` ✗
- `skill/prompt-script-master/docs/seedance2-full-reference.md` ✗
- `skill/prompt-script-master/docs/golden-tests.md` ✗
- `skill/prompt-script-master/references/quality-control.md` ✗
- `skill/prompt-script-master/references/optimizer-v5/output-templates.md` ✗

## Source of Requirements

Professional Seedance optimization feedback identifying:
1. Weight inversion (character too late in text)
2. Invalid semantics (abstract descriptions model can't parse)
3. Scattered info (diluted weights)
4. Inline negatives (ineffective in body text)
5. Non-standard reference image syntax

## Related

- `snapshot-sync-procedure.md` — Full sync workflow
- `format-migration-2026-07-03.md` — Previous migration (broken format → three-section)
