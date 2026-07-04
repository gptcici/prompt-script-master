#!/usr/bin/env python3
"""Lightweight prompt wizard for Prompt Script Master — v7 (2-part + 7-field timeline)."""

from __future__ import annotations


def ask(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def main() -> None:
    print("提示词脚本大师 - Skill 内置简易向导 (v7)")
    subject = ask("核心主体", "一名人物")
    scene = ask("场景", "明确空间中")
    style = ask("整体风格", "彩色写实电影摄影质感")
    duration = ask("时长", "8 秒")
    action = ask("主要动作", "主体完成可见动作并形成稳定 ending pose")
    camera = ask("运镜状态", "稳定前推，运镜柔和克制")
    consistency = ask("全局一致性约束", "全程人物造型稳定、空间连贯、运镜平稳")

    print("\n【正文提示词】")
    print(f"{16}:9 横屏，{duration}，全程{camera}。")
    print(f"@Image1 仅作为人物强参考，锁定五官、发型、发饰、服装款式与气质，不作为首帧，不参考原图构图背景，全程为同一位{subject.strip('一名')}，不生成通用AI模特脸。")
    print(f"[人物核心外形特征：{subject}]。")
    print(f"{scene}。")
    print("")
    print("[时间轴1]：[景别 + 运镜状态]，[人物核心动作]，[衣发纱幔动态]，[人物光影]，[环境细节]，[景深变化]。首段建立人物主体和关键外形特征。")
    print("")
    print(f"({style}:1.2)，真实电影摄影感，写实风格。")
    print(f"{consistency}。")
    print("")
    print("【负面提示词】")
    print("人物类：脸部变形、五官漂移、发型错乱、发饰丢失、服装变色")
    print("动作类：肢体错乱、手部畸形、手指粘连、动作僵硬")
    print("场景类：空间跳跃错位、道具错位")
    print("风格类：过度磨皮、过度CG感、卡通插画感、画面模糊低质")
    print("技术类：运镜抖动、景别突变、画幅错误")


if __name__ == "__main__":
    main()
