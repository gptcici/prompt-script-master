#!/usr/bin/env python3
"""Validate a ChatGPT Skill directory for basic packaging readiness."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

MAX_ZIP_BYTES = 25 * 1024 * 1024


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_skill_dir(skill_dir: Path) -> None:
    if not skill_dir.exists() or not skill_dir.is_dir():
        fail(f"Skill directory not found: {skill_dir}")

    required = [
        skill_dir / "SKILL.md",
        skill_dir / "agents" / "openai.yaml",
    ]
    for path in required:
        if not path.exists():
            fail(f"Missing required file: {path}")

    skill_md = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if not skill_md.startswith("---"):
        fail("SKILL.md must start with YAML frontmatter")
    if "name:" not in skill_md or "description:" not in skill_md:
        fail("SKILL.md frontmatter must include name and description")

    print("OK: Skill directory passed basic validation")


def validate_zip(zip_path: Path) -> None:
    if not zip_path.exists():
        fail(f"Zip not found: {zip_path}")
    if zip_path.stat().st_size > MAX_ZIP_BYTES:
        fail("Skill zip exceeds 25 MB limit")

    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
        skill_entries = [name for name in names if name.endswith("SKILL.md")]
        if len(skill_entries) != 1:
            fail(f"Expected exactly one SKILL.md in zip, found {len(skill_entries)}")
        root = skill_entries[0].split("/")[0]
        required = [f"{root}/SKILL.md", f"{root}/agents/openai.yaml"]
        for name in required:
            if name not in names:
                fail(f"Missing required zip entry: {name}")

    print("OK: Skill zip passed basic validation")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a ChatGPT Skill directory or zip.")
    parser.add_argument("path", help="Path to skill directory or skill zip")
    args = parser.parse_args()

    path = Path(args.path)
    if path.suffix == ".zip":
        validate_zip(path)
    else:
        validate_skill_dir(path)


if __name__ == "__main__":
    main()
