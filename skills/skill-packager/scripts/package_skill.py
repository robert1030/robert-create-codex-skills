#!/usr/bin/env python3
"""
Package a Codex skill directory into a distributable zip file.

Usage:
    package_skill.py <path/to/skill-folder> [output-directory]
    package_skill.py <path/to/skill-folder> --output-dir dist
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - depends on local environment
    yaml = None


MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}
EXCLUDED_DIRS = {".git", ".hg", ".svn", "__pycache__"}
EXCLUDED_FILENAMES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".zip"}


def read_frontmatter(skill_md: Path) -> tuple[bool, str, dict[str, Any] | None]:
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found", None

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format", None

    frontmatter_text = match.group(1)
    if yaml is None:
        return False, "PyYAML is required to validate SKILL.md frontmatter", None

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        return False, f"Invalid YAML in frontmatter: {exc}", None

    if not isinstance(frontmatter, dict):
        return False, "Frontmatter must be a YAML dictionary", None

    return True, "OK", frontmatter


def validate_skill(skill_path: Path) -> tuple[bool, str, str | None]:
    if not skill_path.exists():
        return False, f"Skill folder not found: {skill_path}", None
    if not skill_path.is_dir():
        return False, f"Path is not a directory: {skill_path}", None

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, f"SKILL.md not found in {skill_path}", None

    ok, message, frontmatter = read_frontmatter(skill_md)
    if not ok or frontmatter is None:
        return False, message, None

    unexpected_keys = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected_keys:
        allowed = ", ".join(sorted(ALLOWED_FRONTMATTER_KEYS))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected frontmatter key(s): {unexpected}. Allowed: {allowed}",
            None,
        )

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        return False, "Missing or invalid 'name' in frontmatter", None
    name = name.strip()

    if not re.match(r"^[a-z0-9-]+$", name):
        return (
            False,
            f"Name '{name}' should use lowercase letters, digits, and hyphens only",
            None,
        )
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain '--'", None
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return (
            False,
            f"Name is too long ({len(name)} characters). Maximum is {MAX_SKILL_NAME_LENGTH}.",
            None,
        )
    if skill_path.name != name:
        return False, f"Directory name '{skill_path.name}' must match skill name '{name}'", None

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        return False, "Missing or invalid 'description' in frontmatter", None
    description = description.strip()

    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets (< or >)", None
    if len(description) > MAX_DESCRIPTION_LENGTH:
        return (
            False,
            f"Description is too long ({len(description)} characters). "
            f"Maximum is {MAX_DESCRIPTION_LENGTH}.",
            None,
        )

    return True, "Skill is valid", name


def should_include(path: Path, output_zip: Path) -> bool:
    if path == output_zip:
        return False
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    if path.name in EXCLUDED_FILENAMES:
        return False
    if path.suffix in EXCLUDED_SUFFIXES:
        return False
    return True


def package_skill(skill_path: Path, output_dir: Path | None) -> Path | None:
    skill_path = skill_path.resolve()
    valid, message, skill_name = validate_skill(skill_path)
    if not valid or skill_name is None:
        print(f"[ERROR] {message}")
        return None

    print(f"[OK] {message}")

    if output_dir is None:
        output_dir = Path.cwd()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_zip = output_dir / f"{skill_name}.zip"

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in sorted(skill_path.rglob("*")):
            if not file_path.is_file():
                continue
            if not should_include(file_path.resolve(), output_zip):
                continue

            archive_name = file_path.relative_to(skill_path.parent)
            zip_file.write(file_path, archive_name)
            print(f"  Added: {archive_name}")

    print(f"\n[OK] Packaged skill: {output_zip}")
    return output_zip


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and package a Codex skill directory into a zip file.",
    )
    parser.add_argument("skill_path", help="Path to the skill directory")
    parser.add_argument(
        "output_directory",
        nargs="?",
        help="Optional output directory for the zip file",
    )
    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        help="Optional output directory for the zip file",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir or args.output_directory
    result = package_skill(
        Path(args.skill_path),
        Path(output_dir) if output_dir else None,
    )
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
