# tests

这里保存最小测试样例，用于验证脚本和 Skill 输出结构。

## 文件

- `sample_input.txt`：简单用户输入。
- `sample_prompt.txt`：符合当前规则的示例提示词。

## 推荐检查

```bash
python scripts/prompt_checker.py tests/sample_prompt.txt
python scripts/prompt_exporter.py tests/sample_prompt.txt --format md
```

## 说明

当前测试只做基础结构检查，不替代完整质量评分。