# 规则冲突/融合/重复分析 (2026-07-03)

对 SKILL.md + 52 个 reference .md 文件的系统性交叉分析报告。用于后续规则整合和维护参考。

## 冲突 (5 处)

| # | 冲突 | 涉及文件 | 状态 |
|---|---|---|---|
| 1 | 时间轴 11 项强制约束：SKILL.md 已删除但 timeline 系列文件保留 | SKILL.md / timeline-execution-rules.md / timeline-quality-gates.md | ✅ 已解决 — 替换为 Seedance 新版规则 |
| 2 | Seedance 提示词顺序不同：prompt-order-rules vs output-templates | seedance-prompt-order-rules.md / output-templates.md | ⚠️ 待处理 |
| 3 | 时间轴分段格式三份文件三种说法 | seedance-prompt-order-rules.md / seedance-camera-movement-transition-rules.md / timeline-execution-rules.md | ⚠️ 待统一命名 |
| 4 | "只输出一段" vs 多段输出 | final-prompt-purity.md / Seedance 时间轴规则 | ⚠️ 待明确 |
| 5 | 自动建议动态级别 vs 确认门控 | dynamic-level-guide.md / confirmation-gate.md | ⚠️ 待处理 |

## 可融合 (7 组)

1. **光线规则 (6→2)** — 合并 seedance-real-lighting-rules + seedance-closeup-face-lighting-rules 为统一光线理论文件
2. **镜头/摄影语言 (4→2)** — cinematic-camera-language 覆盖 camera-movement-library + shot-size-rules
3. **动作/表情库 (3 层引用)** — action-library 合并入 seedance-emotion-action-library
4. **构图规则 (2→1)** — composition-space-structure 理论层合并入 composition-reference-library 作为前言
5. **质量检查清单 (15→1 索引)** — 15 个文件各自定义自检，需统一索引
6. **参考隔离 (3→1)** — 合并 reference-isolation-rules + composition + reference-image 的隔离声明
7. **表情理论 (2→1)** — seedance-expression-motion-rules 合并入 seedance-emotion-action-library

## 重复 (8 处)

1. 表情公式逐字相同 (expression-motion-rules vs emotion-action-library)
2. "正面措辞/禁止否定词" 分布在 21 个文件中
3. 光线四层公式两处结构相同 (real-lighting vs closeup-face-lighting)
4. Library 调用规则结构在 5 个 library 文件中重复
5. 旧版独立否定栏规则已移除，相关约束统一并入全局一致性约束
6. 动态级别在 2 处平行存在 (dynamic-level-guide vs concert-performance-action-library)
7. 任务路由触发条件 2 处不同粒度 (task-routing vs command-system)
8. script-learning-index 功能空置
