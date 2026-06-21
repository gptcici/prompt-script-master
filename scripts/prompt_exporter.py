#!/usr/bin/env python3
"""
prompt_exporter.py

Export a prompt into a timestamped Markdown, TXT, or JSON file.
This is a local utility and does not call any external service.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def export_markdown(prompt: str, output_dir: Path, title: str) -> Path:
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-prompt.md"
    path = output_dir / filename
    path.write_text(f"# {title}\n\n{prompt.strip()}\n", encoding="utf-8")
    return path


def export_txt(prompt: str, output_dir: Path) -> Path:
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-prompt.txt"
    path = output_dir / filename
    path.write_text(prompt.strip() + "\n", encoding="utf-8")
    return path


def export_json(prompt: str, output_dir: Path, title: str) -> Path:
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-prompt.json"
    path = output_dir / filename
    payload = {
        "title": title,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "prompt": prompt.strip(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a prompt to md, txt, or json.")
    parser.add_argument("file", help="Path to source prompt text file")
    parser.add_argument("--format", choices=["md", "txt", "json"], default="md")
    parser.add_argument("--title", default="AI Video Prompt")
    parser.add_argument("--output-dir", default="exports")
    args = parser.parse_args()

    source = Path(args.file)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    prompt = source.read_text(encoding="utf-8")

    if args.format == "md":
        path = export_markdown(prompt, output_dir, args.title)
    elif args.format == "txt":
        path = export_txt(prompt, output_dir)
    else:
        path = export_json(prompt, output_dir, args.title)

    print(f"已导出：{path}")


if __name__ == "__main__":
    main()
