# 安装与验证说明

## 安装 Skill

1. 在仓库中运行打包命令：

```bash
python scripts/package_skill.py
```

2. 生成文件：

```text
dist/skill.zip
```

3. 在 ChatGPT 的 Skills 页面上传 `skill.zip`。

## 本地验证

验证 Skill 目录：

```bash
python scripts/validate_skill.py skill/prompt-script-master
```

验证 Skill zip：

```bash
python scripts/validate_skill.py dist/skill.zip
```

## 测试提示词

上传 Skill 后，可以用以下请求测试：

```text
帮我把这个想法写成 Seedance 2.0 全能参考视频提示词：一个女歌手站在演唱会舞台中央唱副歌，背后有巨大的时间环，灯光很震撼。
```

预期行为：

- 先拆解主体、场景、情绪、镜头目的。
- 如果信息足够，可以按专业默认值生成。
- 输出中文视频提示词，包含时间轴、镜头语言和全局一致性约束。

## 常见问题

如果上传失败，请检查：

- zip 内是否只有一个 Skill。
- Skill 目录内是否包含 `SKILL.md`。
- 是否包含 `agents/openai.yaml`。
- zip 是否小于 25 MB。
