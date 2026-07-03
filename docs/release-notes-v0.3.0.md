# Release Notes: v0.3.0-skill-scaffold

## 概览

`v0.3.0-skill-scaffold` 是《提示词脚本大师》的第一个可试用 Skill scaffold 版本。

该版本已经具备：

- 完整规则文档体系
- ChatGPT Skill 目录结构
- Skill 打包与验证脚本
- 最小测试样例
- GitHub Actions 校验流程
- 发布流程说明
- 已知限制与黄金测试文档

## 核心能力

### 1. AI 视频提示词生成

支持把简单口语想法转化为结构化中文视频提示词，默认面向 Seedance 2.0 全能参考工作流。

### 2. 导演助理式工作流

能先拆解主体、场景、情绪、镜头目标、参考素材和时间轴，再根据严重程度决定直接生成或继续确认。

### 3. 参考素材优先级

支持区分：

- 必须锁定参考
- 强参考
- 仅参考范围

### 4. 质量自检

内置 11 项质量检查维度，包括主体明确度、场景关系、动作细节、镜头语言、时间轴和一致性约束。

### 5. Skill 打包流程

可使用：

```bash
python scripts/package_skill.py
```

生成：

```text
dist/skill.zip
```

## 主要文件

```text
skill/prompt-script-master/SKILL.md
skill/prompt-script-master/agents/openai.yaml
skill/prompt-script-master/references/
skill/prompt-script-master/scripts/
scripts/validate_skill.py
scripts/package_skill.py
docs/golden-tests.md
docs/manual-validation-checklist.md
```

## 安装前检查

发布前请确认：

```bash
python scripts/validate_skill.py skill/prompt-script-master
python scripts/package_skill.py
python scripts/validate_skill.py dist/skill.zip
python scripts/prompt_checker.py tests/sample_prompt.txt
```

## 手动验证

请执行：

1. 打开 GitHub Actions，确认 `Validate` workflow 通过。
2. 上传 `dist/skill.zip` 到 ChatGPT Skills。
3. 执行 `docs/golden-tests.md` 中 5 条测试。
4. 将结果记录到 issue #7。

## 已知限制

- examples 细化仍暂停。
- Skill 真实上传测试仍需手动完成。
- CI 状态需要在 GitHub 页面确认。
- 当前测试集是最小测试，不是完整回归测试。

## 建议 Release 标题

```text
v0.3.0-skill-scaffold
```

## 建议 Release 描述

```text
First usable Skill scaffold for Prompt Script Master. Includes core prompt workflow documentation, ChatGPT Skill structure, packaging and validation scripts, GitHub Actions validation, golden tests, and manual validation checklist.
```
