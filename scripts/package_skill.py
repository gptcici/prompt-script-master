#!/usr/bin/env python3
"""Package the Prompt Script Master Skill into dist/skill.zip."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

MAX_ZIP_BYTES = 25 * 1024 * 1024


def zip_dir(source_dir: Path, target_zip: Path) -> None:
    if target_zip.exists():
        target_zip.unlink()
    target_zip.parent.mkdir(parents=True, exist_ok=True)

    root_name = source_dir.name
    with zipfile.ZipFile(target_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in source_dir.rglob("*"):
            if path.is_file():
                arcname = Path(root_name) / path.relative_to(source_dir)
                zf.write(path, arcname.as_posix())


def main() -> None:
    parser = argparse.ArgumentParser(description="Package ChatGPT Skill.")
    parser.add_argument("--skill-dir", default="skill/prompt-script-master")
    parser.add_argument("--output", default="dist/skill.zip")
    parser.add_argument("--skip-validation", action="store_true")
    args = parser.parse_args()

    repo_root = Path.cwd()
    skill_dir = repo_root / args.skill_dir
    output = repo_root / args.output

    if not skill_dir.exists():
        raise SystemExit(f"Skill directory not found: {skill_dir}")

    if not args.skip_validation:
        subprocess.run([sys.executable, "scripts/validate_skill.py", str(skill_dir)], check=True)

    zip_dir(skill_dir, output)

    if output.stat().st_size > MAX_ZIP_BYTES:
        raise SystemExit("Skill zip exceeds 25 MB limit")

    if not args.skip_validation:
        subprocess.run([sys.executable, "scripts/validate_skill.py", str(output)], check=True)

    print(f"Packaged Skill: {output}")


if __name__ == "__main__":
    main()
