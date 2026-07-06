#!/usr/bin/env python3
"""Minimal wizard for the current Prompt Script Master video prompt format."""

from __future__ import annotations


def ask(label: str, default: str) -> str:
    value = input(f"{label} [{default}]: ").strip()
    return value or default


def main() -> None:
    duration = ask("时长", "15秒")
    aspect = ask("画幅", "16:9")
    subject = ask("主体/动作", "东方少女坐在亭中弹奏古筝，指尖拨弦，眼神低垂后缓慢抬起")
    style = ask("风格", "东方仙侠写实电影质感，空灵庄严")
    refs = ask("参考图职责", "Mixed 1/2 锁定人物；Mixed 3 锁定服装；Mixed 4 锁定亭子结构")
    light = ask("全局光源锚点", "唯一主光源来自画面右侧低角度夕阳，暖金侧逆光，云海弱补光")
    wind = ask(
        "全局物理动力学锚点",
        "主要动力来源为山风与人物动作；风从右前方吹向左后方，发丝、丝带、披帛、纱幔按重量和固定点产生速度差、延迟、回弹和下坠；若有雨雪、水面、烟尘、粒子或道具接触，写清运动路径、接触反应、落点和消散",
    )

    print("\n【正文提示词】")
    print(f"{duration}，{aspect}，{style}。{subject}，由多个镜头切换组成。")
    print(f"\n参考图职责：{refs}。")
    print(f"\n全局光源锚点：{light}。")
    print(f"\n全局物理动力学锚点：{wind}。")
    print("\n0-2秒，镜头一：[景别/机位/运镜]。[主体动作/表情/身体或材质联动]。[光影/风/景深/环境变化]。")
    print("2-4秒，镜头二：[同上，每镜头2-4句]。")
    print("\n全局一致性：[角色、服装、道具、建筑、光源、风向和空间关系保持一致]。")
    print("\n【负面提示词】")
    print("人物类：...")
    print("动作类：表情僵硬、嘴部崩坏、口型与情绪脱节、动作卡顿、肢体与表情脱节")
    print("动力学类：风向混乱、发丝不动、布料无重量感、纱幔无规律乱飞、所有物体同速漂浮、道具无支点漂浮、粒子无落点、烟雾无消散")
    print("场景类：...")
    print("风格类：...")


if __name__ == "__main__":
    main()
