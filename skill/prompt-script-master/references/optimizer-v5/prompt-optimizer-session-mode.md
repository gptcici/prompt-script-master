# Prompt Optimizer Session Mode

Purpose: make users visibly aware when they are still inside the prompt-optimization workflow.

## Activation

Enter visible session mode after prompt generation, prompt revision, prompt audit, or direct prompt repair.

Do not enter session mode during skill maintenance, rule library updates, GitHub sync, documentation edits, or workflow self-audit.

## Visible footer

After prompt-generation/revision tasks, append outside the copy-ready prompt:

`【当前状态】Prompt Optimizer 会话中。你可以直接继续说：加强光影 / 修改表情 / 背景虚化更强 / 压缩长度 / 退出技能。`

## Exit phrases

Exit when the user says: 退出技能, 结束优化, 停止修改, 不用这个技能了, 换个话题, 新任务.

## Guardrails

If the user provides new rules, a new library, a self-check request, or GitHub upload instructions, treat it as skill maintenance and do not display session mode.
