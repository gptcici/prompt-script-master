# Release Process

## 目标

该流程用于发布《提示词脚本大师》的阶段性版本，并生成可上传的 ChatGPT Skill 包。

## 发布前检查

1. 确认 `examples` 是否需要继续暂停。
2. 确认 `VERSION` 是否需要更新。
3. 确认 `CHANGELOG.md` 是否记录本次变更。
4. 确认 `SKILL.md` 中 references 与 scripts 导航是否最新。

## 本地验证

```bash
python scripts/validate_skill.py skill/prompt-script-master
python scripts/package_skill.py
python scripts/validate_skill.py dist/skill.zip
python scripts/prompt_checker.py tests/sample_prompt.txt
```

全部通过后，才能发布。

## 版本号建议

```text
v0.3.x：Skill scaffold 与仓库维护增强
v0.4.x：Skill 内容稳定化与更多模板
v0.5.x：完整测试与发布自动化
v1.0.0：正式可长期使用版本
```

## GitHub Release 步骤

1. 确认 main 分支最新。
2. 运行打包命令：

```bash
python scripts/package_skill.py
```

3. 确认输出：

```text
dist/skill.zip
```

4. 创建 GitHub Release，tag 使用 `VERSION` 中的版本号。
5. Release notes 从 `CHANGELOG.md` 当前版本复制。
6. 上传 `dist/skill.zip` 作为 release asset。

## 回滚方式

如果发布后发现 Skill 有问题：

1. 记录问题。
2. 回退到上一版 tag。
3. 重新运行打包和验证。
4. 发布修复版本。

## 注意事项

- 不要把 `dist/skill.zip` 提交进仓库。
- 不要把用户真实素材、隐私内容或大型资产放入 Skill 包。
- Skill zip 必须小于 25 MB。
- 每次发布前必须确认 zip 内只有一个 Skill。
