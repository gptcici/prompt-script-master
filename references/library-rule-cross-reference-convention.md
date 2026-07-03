# 库-规则交叉引用规范

生效日期：2026-07-03

## 规范

所有库文件（`*-library.md`）必须在文件末尾包含 `## Related` 段，显式列出自身遵循的规则文件：

```markdown
## Related

- Rules: `xxx-rules.md` — brief description of what this rule governs
- Rules: `yyy-rules.md` — brief description
- Library: `zzz-library.md` — brief description (for library-to-library cross-refs)
```

规则文件（`*-rules.md`）也应有 `## Related` 段指向其配套库，形成双向引用。

## 已覆盖清单（15 个文件）

### 光影类（6 个）

| 文件 | 引用 |
|---|---|
| `seedance-real-lighting-rules.md` | → `scene-library`, `chinese-fantasy-library`, `closeup-face-lighting-rules` |
| `seedance-lighting-scene-library.md` | → `real-lighting-rules` |
| `seedance-closeup-face-lighting-rules.md` | → `closeup-face-lighting-library`, `real-lighting-rules` |
| `seedance-closeup-face-lighting-library.md` | → `closeup-face-lighting-rules` |
| `seedance-chinese-fantasy-lighting-library.md` | → `real-lighting-rules`, `scene-library` |
| `lighting-emotion-library.md` | → `scene-library`, `chinese-fantasy-library`, `closeup-face-lighting-library` |

### 运镜/镜头类（4 个）

| 文件 | 引用 |
|---|---|
| `classic-shot-library.md` | → `camera-movement-library`, `cinematic-camera-language`, `camera-movement-transition-rules` |
| `camera-movement-library.md` | → `classic-shot-library`, `camera-movement-transition-rules`, `cinematic-camera-language` |
| `concert-shot-language-library.md` | → `shot-size-rules`, `cinematic-camera-language`, `concert-live-mv-rules` |
| `seedance-industrial-storyboard-routines-library.md` | → `camera-movement-transition-rules`, `cinematic-camera-language`, `depth-space-rules` |

### 动作/表情类（2 个）

| 文件 | 引用 |
|---|---|
| `concert-performance-action-library.md` | → `dynamic-level-guide`, `seedance-expression-motion-rules`, `concert-shot-language-library` |
| `seedance-emotion-action-library.md` | → `seedance-expression-motion-rules`, `seedance-prompt-order-rules`, `seedance-real-lighting-rules` |

### 参考图/素材类（3 个）

| 文件 | 引用 |
|---|---|
| `asset-library-guide.md` | → `reference-isolation-rules`, `reference-material-guide` |
| `reference-image-library.md` | → `reference-fidelity-system`, `character-sheet-continuity-system` |
| `composition-reference-library.md` | → `composition-space-structure`, `cinematic-camera-language` |

## 2026-07-03 已删除库文件

以下文件已删除且所有引用已清除：

- `action-library.md` — 功能被 `concert-performance-action-library.md` 和 `seedance-emotion-action-library.md` 覆盖
- `music-editing-rhythm-library.md` — 规则已过时
- `mv-story-structure-library.md` — 规则已过时
