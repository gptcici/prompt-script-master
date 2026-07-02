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
    camera = ask("镜头语言", "电影级数字摄影机，缓慢推近，焦点锁定主体")
    negative = ask("禁止项", "不要主体漂移，不要场景结构变化，不要字幕、水印、乱码文字")

    print("\n【生成规格】")
    print(f"生成 {duration}，Seedance 2.0 全能参考，{style}。")
    print("\n【镜头目标】")
    print(f"表达{subject}在{scene}中的{action}。")
    print("\n【镜头语言与摄影参数】")
    print(camera)
    print("\n【禁止项】")
    print(negative)


if __name__ == "__main__":
    main()
