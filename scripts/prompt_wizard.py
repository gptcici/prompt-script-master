#!/usr/bin/env python3
"""Lightweight prompt wizard for Prompt Script Master."""

from __future__ import annotations


def ask(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def main() -> None:
    print("提示词脚本大师 - Skill 内置简易向导")
    subject = ask("核心主体", "一名人物")
    scene = ask("场景", "明确空间中")
    style = ask("整体风格", "电影级写实 AI 视频")
    duration = ask("时长", "8 秒")
    action = ask("主要动作", "主体完成可见动作并形成稳定 ending pose")
    camera = ask("本段运镜状态", "固定机位缓慢推近，焦点锁定主体")
    consistency = ask("全局一致性约束", "主体身份、场景结构、动作连续性和画面焦点全程稳定")

    print("\n【全程总定调】")
    print(f"生成 {duration}，画幅 16:9，Seedance 2.0 全能参考。")
    print(f"镜头总基调：{style}。")
    print(f"人物核心外形特征：{subject}。")
    print(f"整体场景总设定：{scene}。")

    print("\n【时间轴分段】")
    print("首段：")
    print(f"本段景别：中景")
    print(f"本段运镜状态：{camera}")
    print(f"焦点变化：焦点锁定主体")
    print(f"核心动作：{action}")
    print("表情肢体联动：[填充]")
    print("人物面光/骨骼光影：[填充]")
    print("环境光影变化：[填充]")
    print("环境细节补充：[填充]")
    print("本段景深变化：[填充]")

    print("\n【全局收尾】")
    print(f"整体风格质感：{style}。")
    print(f"全局一致性约束：{consistency}")


if __name__ == "__main__":
    main()
