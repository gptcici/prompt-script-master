#!/usr/bin/env python3
"""Export prompt text to a timestamped Markdown file."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--output-dir", default="exports")
    args = parser.parse_args()

    src = Path(args.file)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-prompt.md"
    target.write_text("# AI Video Prompt\n\n" + src.read_text(encoding="utf-8").strip() + "\n", encoding="utf-8")
    print(f"已导出：{target}")


if __name__ == "__main__":
    main()
