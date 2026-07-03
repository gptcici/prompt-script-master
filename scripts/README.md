# scripts

这里放置《提示词脚本大师》的本地辅助工具。

## 文件

- `prompt_wizard.py`：交互式提示词生成向导。
- `prompt_checker.py`：提示词结构检查器。
- `prompt_exporter.py`：提示词导出工具。

## 使用

```bash
python scripts/prompt_wizard.py
python scripts/prompt_checker.py path/to/prompt.txt
python scripts/prompt_exporter.py path/to/prompt.txt --format md
```

## 说明

这些脚本不调用外部模型，只用于本地辅助生成、检查和导出提示词。

后续可继续扩展 11 维评分、参考素材说明、全局一致性约束和完整 Skill 工作流。
