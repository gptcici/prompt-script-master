# 提示词脚本大师

> 一个导演助理式 AI 视频提示词生成系统，把简单口语想法转化为结构完整、镜头明确、动作细致、可直接用于 AI 视频生成工具的中文提示词。

## 当前版本

```text
v0.3.2-timeline
```

当前仓库已经包含规则文档、示范案例骨架、复用模板、本地工具脚本、ChatGPT Skill 雏形、打包验证流程和 CI 校验。v0.3.2 重点强化时间轴执行规则：每个时间段都必须写入衔接关系、主体动作、场景动态、光线变化、镜头控制、焦段 / 景别 / 焦点 / 景深和情绪节奏。

## 项目定位

《提示词脚本大师》不是普通提示词模板库，而是一个可扩展的提示词工作流项目。

它的目标是：

1. 让用户用简单口语描述想法。
2. 系统像导演助理一样只追问必要问题。
3. 通过专业默认值补齐画面、镜头、动作、灯光、参考素材、时间轴和禁止项。
4. 上传内容后先拆解、复述、确认，再生成提示词，避免误解用户目标。
5. 信息确认后自动生成完整中文提示词，并进行内部质量自检。
6. 可打包为 ChatGPT Skill 使用。

## 当前原则

- 默认输入：简单口语。
- 默认模式：自动模式。
- 默认目标模型：Seedance 2.0 全能参考。
- 提问节奏：每轮 2-3 个问题。
- 输出语言：完整中文提示词。
- 输出风格：AI 模型提示词风格，适合直接复制到生成工具。
- 单个分镜 / 单镜头时长：通常 6-15 秒。
- 负面提示词：必须包含，但只禁止关键异常，不堆砌。
- 参考素材：先自动判断用途，再让用户确认；必须标明参考内容和优先级。
- 写法原则：动词先行，形容词收束。
- 摄影语言：使用专业空间关系、运镜、器材、焦段、焦点和景深描述。
- 反推原则：无法判断镜头、基调或风格时，不硬编，先让用户提供素材或寻找参考进行反推。

## 仓库结构

```text
prompt-script-master/
├── README.md
├── INSTALL.md
├── CHANGELOG.md
├── VERSION
├── PROJECT_STATUS.md
├── docs/                 # 规则文档
├── examples/             # 第一批优秀案例骨架，第 5 项细化暂停
├── templates/            # 复用提示词模板
├── scripts/              # 本地工具、验证和打包脚本
├── skill/                # ChatGPT Skill 雏形
├── tests/                # 最小测试样例
└── .github/workflows/    # GitHub Actions 自动校验
```

## 快速开始

### 1. 检查 Skill 目录

```bash
python scripts/validate_skill.py skill/prompt-script-master
```

### 2. 打包 Skill

```bash
python scripts/package_skill.py
```

输出：

```text
dist/skill.zip
```

### 3. 检查打包文件

```bash
python scripts/validate_skill.py dist/skill.zip
```

### 4. 测试提示词结构

```bash
python scripts/prompt_checker.py tests/sample_prompt.txt
```

## 本地工具

```text
scripts/prompt_wizard.py      # 交互式提示词生成向导
scripts/prompt_checker.py     # 提示词结构检查器
scripts/prompt_exporter.py    # 提示词导出工具
scripts/validate_skill.py     # Skill 目录 / zip 基础校验
scripts/package_skill.py      # 打包 skill.zip
```

## ChatGPT Skill

Skill 目录：

```text
skill/prompt-script-master/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

上传前请先运行：

```bash
python scripts/package_skill.py
python scripts/validate_skill.py dist/skill.zip
```

安装说明见：

```text
INSTALL.md
```

## CI 校验

GitHub Actions 会在 PR 和 main push 时运行：

```bash
python scripts/validate_skill.py skill/prompt-script-master
python scripts/package_skill.py
python scripts/validate_skill.py dist/skill.zip
python scripts/prompt_checker.py tests/sample_prompt.txt
```

## 发布流程

发布流程见：

```text
docs/release-process.md
```

## 暂停项

```text
examples 细化：暂停
```

当前只保留第一批案例骨架，不继续扩写 examples。
