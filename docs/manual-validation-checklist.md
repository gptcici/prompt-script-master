# Manual Validation Checklist

## 目的

本清单用于在真实上传 `skill.zip` 后记录验证结果。

对应 issue：

```text
https://github.com/gptcici/prompt-script-master/issues/7
```

## 1. GitHub Actions 检查

- [ ] 打开仓库 Actions 页面。
- [ ] 找到 `Validate` workflow。
- [ ] 确认最新 main push 或 PR run 是否通过。
- [ ] 如果失败，记录失败 job、失败 step 和日志摘要。

## 2. 本地或仓库打包检查

推荐命令：

```bash
python scripts/validate_skill.py skill/prompt-script-master
python scripts/package_skill.py
python scripts/validate_skill.py dist/skill.zip
```

记录：

```text
打包是否成功：
zip 大小：
是否小于 25 MB：
```

## 3. ChatGPT Skills 上传检查

- [ ] 上传 `skill.zip`。
- [ ] 确认 Skill 名称显示正确。
- [ ] 确认 Skill 描述显示正确。
- [ ] 确认没有上传失败或解析失败。

记录：

```text
上传是否成功：
失败提示：
需要修改：
```

## 4. 黄金测试

执行 `docs/golden-tests.md` 中 5 条测试。

记录格式：

```text
测试编号：
是否通过：
实际表现：
失败原因：
需要修改的文件：
```

## 5. 通过标准

以下全部完成后，才能认为 `v0.3.0-skill-scaffold` 进入可试用状态：

- [ ] GitHub Actions 通过。
- [ ] `skill.zip` 上传成功。
- [ ] 5 条黄金测试全部通过，或失败项已记录成 issue。
- [ ] examples 细化仍按当前要求暂停。
