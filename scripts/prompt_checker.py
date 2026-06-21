#!/usr/bin/env python3
"""
prompt_checker.py

A lightweight heuristic checker for AI video prompts.
It reads a text file and prints a simple pass / needs-optimization report.
This is not a replacement for the full quality-scoring workflow.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_HINTS = {
    "subject": ["主体", "人物", "产品", "歌手", "车辆", "场景"],
    "scene": ["场景", "空间", "舞台", "房间", "城市", "背景"],
    "action": ["动作", "抬", "走", "转", "推近", "握", "移动", "站", "看向"],
    "camera": ["镜头", "摄影机", "焦点", "焦段", "长焦", "广角", "推近", "跟拍"],
    "time": ["秒", "0-", "时间轴"],
    "negative": ["禁止项", "不要", "避免"],
}

CAMERA_TIMELINE_HINTS = [
    "摄影机",
    "镜头",
    "推近",
    "拉远",
    "横移",
    "跟随",
    "跟拍",
    "环绕",
    "升降",
    "变焦",
    "切焦",
    "焦点",
    "景别",
    "近景",
    "中景",
    "特写",
    "全景",
    "半身",
]

VETO_PATTERNS = [
    "高级电影感，震撼，燃，很好看",
    "很高级，很震撼，很好看",
]

TIMELINE_LINE_RE = re.compile(r"(^|\n)\s*(?:\d+\s*[-—]\s*\d+\s*秒|\d+\s*秒\s*[-—])[^\n]*")


def _timeline_lines(text: str) -> list[str]:
    return [match.group(0).strip() for match in TIMELINE_LINE_RE.finditer(text)]


def check_prompt(text: str) -> tuple[list[str], list[str]]:
    missing: list[str] = []
    warnings: list[str] = []

    for key, hints in REQUIRED_HINTS.items():
        if not any(hint in text for hint in hints):
            missing.append(key)

    for pattern in VETO_PATTERNS:
        if pattern in text:
            warnings.append("提示词过于抽象，缺少主体、场景、动作和镜头语言。")

    if len(text.strip()) < 80:
        warnings.append("提示词过短，可能缺少可执行细节。")

    if text.count("不要") > 14:
        warnings.append("禁止项可能过多，建议合并重复项。")

    lines = _timeline_lines(text)
    if lines:
        weak_lines = [line for line in lines if not any(hint in line for hint in CAMERA_TIMELINE_HINTS)]
        if weak_lines:
            warnings.append("时间轴中存在未写入镜头控制、景别变化或焦点控制的时间段。")
    elif "时间轴" in text:
        warnings.append("检测到时间轴标题，但没有识别到明确的秒数段落。")

    return missing, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description="Check an AI video prompt text file.")
    parser.add_argument("file", help="Path to prompt text file")
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    missing, warnings = check_prompt(text)

    print("提示词检查结果")
    print("=" * 20)

    if not missing and not warnings:
        print("通过：未发现明显结构问题。")
        return

    print("需要优化")
    if missing:
        print("\n缺少可能的关键模块：")
        for item in missing:
            print(f"- {item}")

    if warnings:
        print("\n提醒：")
        for item in warnings:
            print(f"- {item}")


if __name__ == "__main__":
    main()
