# 快照同步规程

## 背景

本 Skill 的 `skill/prompt-script-master/` 快照目录是 Hermes 运行时的真实副本。主目录和快照目录不一致是最高危的维护陷阱——任何遗漏都会导致规则漂移。

## 历史教训

- **2026-07-03**：发现 optimizer-v5/ 完整子目录、assets/（composition-library、reference-library、reference-images、reference-videos、source-breakdowns）、docs/（24个文件）、scripts/（3个文件）、templates/（3个文件）在快照中完全缺失，原因是逐文件手动 cp 而非全量校验。
- 此后改为 `diff -rq` 全量对比 + 批量 cp。

## 同步规程

### 每次编辑后必做

```bash
# 1. 复制修改过的文件到快照
SRC="D:/HermesAgent/skills/prompt-script-master"
DST="$SRC/skill/prompt-script-master"

# 2. 全量校验（排除项目级文件）
diff -rq "$SRC/" "$DST/" \
  -x .git -x __pycache__ -x '*.bak' -x '.gitignore' -x '.github' \
  2>/dev/null

# 3. Only in SRC = 快照缺失，立即补齐
#    Only in DST = 快照多余（罕见），核实后删除

# 4. 再次 diff 确认零差异
```

### 排除项

以下项目级文件只存在于主目录，快照无需包含：

- `CHANGELOG.md`、`INSTALL.md`、`LICENSE.md`、`PROJECT_STATUS.md`
- `VERSION`、`requirements.txt`
- `tests/`、`examples/`
- `skill/`（快照目录本身）
- `.git/`、`.gitignore`、`.github/`

### 快照目录必须包含的全部路径

```
skill/prompt-script-master/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── icon.svg
│   ├── composition-library/     (35 .webp + README)
│   ├── reference-library/       (19 .webp + README)
│   ├── reference-images/        (concert-case-a/*.jpg + README)
│   ├── reference-videos/        (concert-case-a/*.mp4 + README)
│   └── source-breakdowns/       (3 .md)
├── docs/                        (24 .md files)
├── references/
│   ├── *.md                     (17 files)
│   └── optimizer-v5/
│       └── *.md                 (20 files)
├── scripts/
│   ├── prompt_checker.py
│   ├── prompt_wizard.py
│   ├── package_skill.py
│   ├── validate_skill.py
│   └── README.md
└── templates/
    ├── video-prompt-template.md
    ├── prompt-review-checklist.md
    └── reference-material-template.md
```

### 快照缺失文件的核心原因

1. `optimizer-v5/` 规则文件：主目录的 optimizer-v5/ 完整，但最初只同步了部分文件到快照
2. `assets/` 二进制资源：项目初期 assets/ 在快照目录中完全未创建
3. `docs/`、`scripts/` 中后期新增文件：逐文件 cp 容易遗漏
