#!/usr/bin/env python3
"""Lightweight prompt checker for Prompt Script Master."""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = ["主体", "场景", "镜头", "秒", "不要"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    missing = [word for word in REQUIRED if word not in text]

    if not missing:
        print("通过：未发现明显结构缺失。")
    else:
        print("需要优化：")
        for item in missing:
            print(f"- 缺少可能的关键内容：{item}")


if __name__ == "__main__":
    main()
