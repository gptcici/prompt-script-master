#!/usr/bin/env python3
"""Lightweight checker for current Prompt Script Master video prompts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SECTION_HINTS = {
    "正文提示词": ["【正文提示词】"],
    "负面提示词": ["【负面提示词】"],
    "光源锚点": ["光源", "主光源", "夕阳", "侧逆光", "补光"],
    "风向/柔体锚点": ["风向", "山风", "柔体", "发丝", "披帛", "纱幔", "吹向", "重量", "回弹"],
    "镜头时间轴": ["镜头一", "0-", "秒"],
}

NEGATIVE_CATEGORIES = ["人物类", "动作类", "风力类", "场景类", "风格类"]
SHOT_RE = re.compile(r"\d+\s*[-—]\s*\d+\s*秒[^\n。]*")
DEPRECATED_MARKERS = ["【全程" + "总定调】", "【时间轴" + "分段】", "【全局" + "收尾】"]

CAMERA_HINTS = ["镜头", "机位", "运镜", "推", "拉", "横移", "环绕", "跟拍", "俯视", "特写", "远景", "中景", "近景"]
ACTION_HINTS = ["动作", "走", "坐", "弹", "拨", "抬", "转", "看", "凝视", "回头", "停步", "伸手", "表情", "头部", "手", "身体", "肩", "衣", "发"]
ENV_HINTS = ["光", "阴影", "风", "云", "景深", "虚化", "背景", "纱幔", "环境", "透光"]
PERSON_HINTS = ["人物", "她", "他", "女孩", "少女", "女性", "男性", "歌手", "演员", "角色", "主角", "女主", "男主"]
EXPRESSION_HINTS = ["眼神", "眉", "嘴", "唇", "表情", "面部", "肩", "手", "身体", "重心", "情绪"]
MOUTH_TRIGGER_HINTS = ["唱", "演唱", "说话", "念白", "对口型", "口型", "台词", "喊", "哼唱"]
MOUTH_DETAIL_HINTS = ["下颌", "嘴唇", "唇部", "开合", "呼吸", "口型", "气息"]
CLOSEUP_HINTS = ["中近景", "近景", "特写", "面部特写", "情绪近景", "半身近景"]
FACE_LIGHT_HINTS = ["鼻梁", "眼窝", "颧骨", "下颌", "眼神光", "瞳孔", "皮肤", "面部光影", "面光", "骨骼"]
WIND_OBJECT_HINTS = ["发丝", "头发", "碎发", "披帛", "袖口", "裙摆", "衣摆", "丝带", "珠链", "流苏", "纱幔", "竹叶", "云雾", "云海", "水面", "烟", "雨", "雪"]
WIND_PHYSICS_HINTS = ["风向", "吹向", "重量", "惯性", "延迟", "回弹", "下坠", "鼓起", "拉伸", "翻卷", "速度差"]
FAILURE_WORDS_IN_MAIN = ["不要", "避免", "不能", "不得", "不允许", "无卡顿", "不会"]


def contains_any(text: str, hints: list[str]) -> bool:
    return any(h in text for h in hints)


def check_prompt(text: str) -> tuple[list[str], list[str]]:
    missing: list[str] = []
    warnings: list[str] = []

    for marker in DEPRECATED_MARKERS:
        if marker in text:
            warnings.append(f"检测到已废弃输出模板：{marker}")

    for label, hints in SECTION_HINTS.items():
        if not contains_any(text, hints):
            missing.append(label)

    if "【负面提示词】" in text:
        neg = text.split("【负面提示词】", 1)[1]
        for cat in NEGATIVE_CATEGORIES:
            if cat not in neg:
                warnings.append(f"负面提示词缺少分类：{cat}")
        if "风力类" in neg and not contains_any(neg, ["风向", "发丝", "布料", "纱幔", "云层", "同速", "重量"]):
            warnings.append("风力类负面提示词较弱，建议加入风向混乱、发丝不动、布料无重量、同速漂浮等故障词。")

    main = text.split("【负面提示词】", 1)[0]
    if sum(main.count(w) for w in FAILURE_WORDS_IN_MAIN) > 2:
        warnings.append("正文提示词含较多负面/故障措辞，建议移入负面提示词。")

    has_person = contains_any(main, PERSON_HINTS)
    if has_person:
        if not contains_any(main, ACTION_HINTS):
            warnings.append("检测到人物主体，但缺少人物核心动作。")
        if not contains_any(main, EXPRESSION_HINTS):
            warnings.append("检测到人物主体，但缺少表情与肢体联动。")
        if contains_any(main, MOUTH_TRIGGER_HINTS) and not contains_any(main, MOUTH_DETAIL_HINTS):
            warnings.append("检测到说话/唱歌/对口型，但缺少下颌稳定、嘴唇开合、呼吸节奏等口型细节。")
        if contains_any(main, CLOSEUP_HINTS) and not contains_any(main, FACE_LIGHT_HINTS):
            warnings.append("检测到人物中近景/近景/特写，但缺少鼻梁、眼窝、颧骨、下颌、眼神光等人物面部光影。")

    if contains_any(main, WIND_OBJECT_HINTS):
        if not contains_any(main, WIND_PHYSICS_HINTS):
            warnings.append("检测到动态材质，但缺少风向/重量/惯性/回弹/速度差等柔体动力学锚点。")
        if "风向" in main and "统一" not in main:
            warnings.append("检测到风向描述，但未明确风向全程统一。")

    shots = SHOT_RE.findall(text)
    if shots:
        for shot in shots:
            idx = text.find(shot)
            window = text[idx: idx + 380]
            if not contains_any(window, CAMERA_HINTS):
                warnings.append(f"{shot} 附近缺少机位/运镜信息。")
            if contains_any(window, PERSON_HINTS):
                if not contains_any(window, ACTION_HINTS):
                    warnings.append(f"{shot} 附近有人物但缺少人物动作。")
                if not contains_any(window, EXPRESSION_HINTS):
                    warnings.append(f"{shot} 附近有人物但缺少表情/肢体联动。")
            elif not contains_any(window, ACTION_HINTS):
                warnings.append(f"{shot} 附近缺少主体动作/肢体信息。")
            if not contains_any(window, ENV_HINTS):
                warnings.append(f"{shot} 附近缺少光影/风/环境信息。")
    elif "镜头" in text:
        warnings.append("检测到镜头描述，但没有识别到明确秒数段落。")

    main_len = len(main.strip())
    if main_len < 500:
        warnings.append("正文偏短，复杂视频可能缺少控制锚点。")
    if main_len > 2600:
        warnings.append("正文偏长，建议压缩重复说明，保留强锚点和镜头化时间轴。")

    return missing, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a Prompt Script Master video prompt text file.")
    parser.add_argument("file", help="Path to prompt text file")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    missing, warnings = check_prompt(text)

    print("提示词检查结果")
    print("=" * 20)
    if not missing and not warnings:
        print("通过：符合当前中等精简 + 强锚点 + 镜头化时间轴 + 人物镜头强制覆盖 + 风向/柔体动力学标准。")
        return
    print("需要优化")
    if missing:
        print("\n缺少关键模块：")
        for item in missing:
            print(f"- {item}")
    if warnings:
        print("\n提醒：")
        for item in warnings:
            print(f"- {item}")


if __name__ == "__main__":
    main()
