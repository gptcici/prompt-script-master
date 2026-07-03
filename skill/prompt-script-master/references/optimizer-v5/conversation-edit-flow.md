# Conversation Edit Flow

## Goal

Support continuous prompt editing without forcing the user to re-mention the skill every turn.

## Direct revision triggers

When the previous assistant output contains a prompt and the user says: 修改, 继续, 加强, 弱化, 替换, 压缩, 扩写, 换成近景, 加强光影, 修改表情, 背景虚化更强, treat the message as a revision of the previous prompt.

## Ambiguous edit trigger

If a new conversation starts with only `帮我修改一下` or `优化一下` and no target prompt is present, ask whether the user wants to modify the previous prompt.

## Maintenance guardrail

Do not trigger prompt revision when the user is adding rules, adding libraries, updating the skill, checking workflow conflicts, asking for GitHub sync, or discussing Skill architecture.

## Revision output

Use:

`## 正文提示词`

`## 自检发现`

`## 已修改`

Then append the session mode footer when appropriate.
