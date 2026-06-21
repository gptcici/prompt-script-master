#!/usr/bin/env python3
"""
prompt_wizard.py

A lightweight command-line helper for drafting a structured AI video prompt.
It does not call any external service. It simply gathers core inputs and prints
a Seedance 2.0 full-reference prompt skeleton.
"""

from __future__ import annotations


def ask(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def build_prompt(data: dict[str, str]) -> str:
    return f"""【生成规格】
生成 {data['duration']} 秒，{data['aspect_ratio']}，Seedance 2.0 全能参考，整体风格为{data['style']}。

【参考素材说明】
{data['references']}

【镜头目标】
本镜头主要表达{data['subject']}在{data['scene']}中的{data['goal']}。

【时间轴】
0-{data['midpoint']} 秒：{data['opening_action']}
{data['midpoint']}-{data['duration']} 秒：{data['ending_action']}

【镜头语言与摄影参数】
使用{data['camera']}，{data['lens']}，镜头进行{data['camera_move']}，焦点锁定{data['focus']}。

【灯光、场景与动态】
{data['lighting']}

【一致性要求】
保持{data['consistency']}一致，不发生漂移。

【禁止项】
{data['negative_prompt']}
"""


def main() -> None:
    print("提示词脚本大师 - 简易生成向导")
    print("按回车可使用默认值。\n")

    duration = ask("时长（秒）", "8")
    midpoint = ask("中间时间点（秒）", str(max(1, int(duration) // 2)) if duration.isdigit() else "4")

    data = {
        "duration": duration,
        "midpoint": midpoint,
        "aspect_ratio": ask("画幅", "16:9 横屏"),
        "style": ask("整体风格", "电影级写实 AI 视频"),
        "subject": ask("核心主体", "一名人物"),
        "scene": ask("场景", "明确空间中"),
        "goal": ask("镜头目标", "动作和情绪变化"),
        "references": ask("参考素材说明", "无参考素材时按专业默认生成；如有素材，请标明用途和优先级。"),
        "opening_action": ask("前半段动作", "主体完成起始动作，镜头缓慢建立空间关系。"),
        "ending_action": ask("后半段动作", "主体完成关键动作并形成稳定 ending pose。"),
        "camera": ask("摄影机", "电影级数字摄影机"),
        "lens": ask("镜头/焦段", "85mm 长焦"),
        "camera_move": ask("运镜", "缓慢推近"),
        "focus": ask("焦点", "主体眼睛或关键产品细节"),
        "lighting": ask("灯光与场景动态", "光线随动作轻微变化，背景保持稳定空间结构。"),
        "consistency": ask("一致性要求", "主体身份、服装、场景、道具和光线"),
        "negative_prompt": ask("禁止项", "不要主体漂移，不要场景结构变化，不要动作跳变，不要字幕、水印、乱码文字。"),
    }

    print("\n" + build_prompt(data))


if __name__ == "__main__":
    main()
