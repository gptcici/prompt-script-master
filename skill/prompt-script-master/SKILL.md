---
name: prompt-script-master
description: Use this skill when the user wants to create, review, optimize, or convert simple ideas into structured Chinese AI video prompts, especially for Seedance 2.0 full-reference workflows. The skill generates copy-ready prompts whose timeline embeds transition relation, scene changes, lighting changes, camera movement, lens and focal length, shot size, focus, and rhythm.
---

# 提示词脚本大师

## 触发场景

当用户需要生成、优化、检查或拆解 AI 视频提示词时，使用本 Skill。

典型请求包括：

- 把口语想法改成视频提示词
- 根据参考图、首帧、尾帧或分镜图写提示词
- 优化 Seedance 2.0 全能参考提示词
- 设计单镜头或多镜头视频分镜
- 检查提示词是否可执行
- 把抽象情绪转化为可见镜头语言

## 默认行为

- 默认模型：Seedance 2.0 全能参考
- 默认语言：中文
- 默认模式：导演助理式自动模式
- 默认提问节奏：每轮最多 2-3 个关键问题
- 默认输出：可直接复制到 AI 视频模型的完整中文提示词

## 工作阶段状态机

1. 识别输入类型
2. 识别项目类型
3. 识别参考资料
4. 专业复述
5. 补齐信息
6. 音乐确认
7. 动作方案确认
8. 高潮镜头建议
9. 用户确认闸门
10. 最终生成
11. 自检

## 时间轴结构

单镜头默认结构：

1. 生成规格
2. 参考素材说明
3. 整体目标与风格基调
4. 时间轴（含镜头/光线/动作/节奏）
5. 全局摄影基调
6. 一致性
7. 禁止项

## 用户沟通隔离规则

最终提示词不得包含解释性内容或确认语。

## 一票否决项

出现结构冲突或信息不足时不得生成最终提示词。

## references 读取规则

- core-workflow.md
- restatement-stage-flow.md
- project-type-rules.md
- video-rules.md
- action-library.md
- classic-shot-library.md
- templates.md
- timeline-execution-rules.md
- timeline-quality-gates.md
- quality-control.md
- reference-material-guide.md
- shot-size-rules.md
- final-prompt-purity.md
- camera-movement-library.md
- **concert-live-mv-rules.md（可选参考，不改变主流程）**
