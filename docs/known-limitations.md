# Known Limitations

## 当前限制

本项目当前处于 `v0.3.0-skill-scaffold` 阶段，已经具备可维护 Skill 雏形，但仍有一些已知限制。

## Skill 使用限制

- Skill 包已在本地生成和基础校验，但仍需要在 ChatGPT Skills 页面进行真实上传测试。
- 触发描述已经覆盖 AI 视频提示词、Seedance 2.0、图生视频、首尾帧、产品广告、演唱会镜头等场景，但仍需要真实对话测试确认不会误触发。
- Skill 默认不联网学习公开资料。如果用户要求基于近期影片、广告、人物或品牌资料进行反推，需要由当前 ChatGPT 环境另行决定是否联网检索。

## 脚本限制

- `prompt_checker.py` 只是轻量结构检查器，不等同于完整 11 维质量评分。
- `prompt_wizard.py` 只生成基础骨架，不替代完整导演助理工作流。
- `prompt_exporter.py` 只做文件导出，不做内容质量判断。

## 测试限制

- 当前 `tests/` 只包含最小样例。
- CI 只做基础结构校验、打包校验和示例提示词检查。
- 尚未建立完整回归测试集。

## 内容限制

- `examples` 细化当前保持暂停。
- 第一批案例主要用于结构示范，不代表最终案例库质量。
- 复杂多镜头、音乐节奏、品牌广告、电影风格反推仍需要更多实战样例验证。

## 发布限制

- 当前仓库不提交 `dist/skill.zip`。
- 正式 release 需要手动运行打包脚本，并将 `dist/skill.zip` 上传为 GitHub Release asset。

## 下一步建议

1. 在 ChatGPT Skills 页面真实上传 `skill.zip`。
2. 使用 `docs/golden-tests.md` 中的测试用例验证输出。
3. 检查 GitHub Actions 是否通过。
4. 记录真实使用反馈，再决定是否进入 `v0.4.x`。