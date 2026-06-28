#!/usr/bin/env python3
"""Validate the docs-quality-gen v1.1 skill contract."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


BASE_SKILL_NAME = "docs-quality-gen"
VERSIONED_SKILL_NAME = "docs-quality-gen-v1-1"
ALLOWED_SKILL_NAMES = {BASE_SKILL_NAME, VERSIONED_SKILL_NAME}
MAX_TEXT_BYTES = 2_000_000
MAX_ZIP_ENTRIES = 200
MAX_ZIP_UNCOMPRESSED_BYTES = 10_000_000
REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/spec-rules.md",
    "references/runbook-rules.md",
    "references/markdown-html-sync.md",
    "references/word-doc-quality.md",
    "references/readability-grade7.md",
    "references/final-review-checklist.md",
    "scripts/validate_docs_quality_gen.py",
]
REQUIRED_DOC_FILES = [
    "docs/docs-quality-gen/SPEC.md",
    "docs/docs-quality-gen/runbook.md",
    "docs/docs-quality-gen/runbook.htm",
    "docs/docs-quality-gen/README.html",
]
STALE_PATTERNS = [
    "Word `.doc` or `.docx` files are out of scope",
    "Word `.doc` and `.docx` files are out of scope",
    "Word `.doc` or `.docx` documents are out of scope",
    "Word `.doc` and `.docx` documents are out of scope",
    "out of scope for v1",
    "html-basic-style",
    "command-environments",
    "v1.2",
    "HTML 基礎美化",
    "Windows/Linux 指令對照",
]


class ValidationError(AssertionError):
    """Raised when the skill contract is invalid."""


def read_text(path: Path) -> str:
    size = path.stat().st_size
    require(size <= MAX_TEXT_BYTES, f"Refusing to read oversized text file: {path} ({size} bytes)")
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def normalize(path: str) -> str:
    return path.replace("\\", "/")


def parse_frontmatter(skill_md: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---", skill_md, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def validate_required_files(root: Path, skill_name: str) -> None:
    skill_dir = root / "skills" / skill_name
    for item in REQUIRED_SKILL_FILES:
        require((skill_dir / item).is_file(), f"Missing skill file: {item}")
    for item in REQUIRED_DOC_FILES:
        require((root / item).is_file(), f"Missing mirrored doc file: {item}")


def validate_skill_contract(root: Path, skill_name: str) -> None:
    skill_dir = root / "skills" / skill_name
    skill_md = read_text(skill_dir / "SKILL.md")
    frontmatter = parse_frontmatter(skill_md)

    require(skill_name in ALLOWED_SKILL_NAMES, f"Unexpected skill directory name: {skill_name}")
    require(frontmatter.get("name") == skill_name, f"SKILL.md name must be {skill_name}")
    description = frontmatter.get("description", "")
    for token in ["Word", "doc/docx", "Word document quality checks"]:
        require(token in description, f"SKILL.md description missing trigger token: {token}")

    for token in ["v1.1", "Word `.doc` and `.docx`", "word-doc-quality.md", "Word verification level"]:
        require(token in skill_md, f"SKILL.md missing v1.1 Word contract token: {token}")

    openai_yaml = read_text(skill_dir / "agents" / "openai.yaml")
    for token in ["Word DOC/DOCX", "verification-level"]:
        require(token in openai_yaml, f"agents/openai.yaml missing token: {token}")


def validate_word_reference(root: Path, skill_name: str) -> None:
    text = read_text(root / "skills" / skill_name / "references" / "word-doc-quality.md")
    for token in [
        "same quality bar as Markdown and HTML",
        "Verification Levels",
        "Level 1",
        "Level 2",
        "Level 3",
        "Level 4",
        "minimum fallback",
    ]:
        require(token in text, f"word-doc-quality.md missing token: {token}")

    checklist = read_text(root / "skills" / skill_name / "references" / "final-review-checklist.md")
    require(
        "highest verification level reached" in checklist,
        "final-review-checklist.md must require the highest Word verification level",
    )


def validate_mirrored_docs(root: Path) -> None:
    required_by_file = {
        "docs/docs-quality-gen/SPEC.md": [
            "v1.1",
            "Word `.doc` and `.docx`",
            "word-doc-quality.md",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
        ],
        "docs/docs-quality-gen/runbook.md": [
            "Word 文件品質檢查",
            "word-doc-quality.md",
            "驗證層級",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
        ],
        "docs/docs-quality-gen/runbook.htm": [
            "Word 文件品質檢查",
            "word-doc-quality.md",
            "驗證層級",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
        ],
        "docs/docs-quality-gen/README.html": [
            "Word 文件品質",
            "驗證層級",
            "DOCX",
        ],
    }
    for file_name, tokens in required_by_file.items():
        text = read_text(root / file_name)
        for token in tokens:
            require(token in text, f"{file_name} missing token: {token}")


def validate_no_stale_claims(root: Path, skill_name: str) -> None:
    search_files = [
        root / "skills" / skill_name / "SKILL.md",
        root / "skills" / skill_name / "agents" / "openai.yaml",
        *sorted((root / "skills" / skill_name / "references").glob("*.md")),
        *[root / item for item in REQUIRED_DOC_FILES],
    ]
    for path in search_files:
        text = read_text(path)
        for pattern in STALE_PATTERNS:
            require(pattern not in text, f"Stale claim found in {path.relative_to(root)}: {pattern}")


def validate_zip(zip_path: Path, skill_name: str) -> None:
    require(zip_path.is_file(), f"Package not found: {zip_path}")
    with zipfile.ZipFile(zip_path) as archive:
        infos = archive.infolist()
        require(len(infos) <= MAX_ZIP_ENTRIES, f"Package has too many entries: {len(infos)}")
        total_size = sum(info.file_size for info in infos)
        require(
            total_size <= MAX_ZIP_UNCOMPRESSED_BYTES,
            f"Package uncompressed size is too large: {total_size} bytes",
        )
        names = {normalize(info.filename) for info in infos}
    for item in REQUIRED_SKILL_FILES:
        archive_name = f"{skill_name}/{item}"
        require(archive_name in names, f"Package missing: {archive_name}")
    require(all(name.startswith(f"{skill_name}/") for name in names), "Package must use one top-level skill folder")


def find_skill_name(start: Path) -> str:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if candidate.parent.name == "skills" and (candidate / "SKILL.md").is_file():
            return candidate.name
        if candidate.name == "scripts" and candidate.parent.parent.name == "skills":
            return candidate.parent.name
    raise ValidationError("Could not determine skill directory name")


def find_repo_root(start: Path, skill_name: str) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "skills" / skill_name / "SKILL.md").is_file():
            return candidate
    raise ValidationError("Could not find repository root")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate docs-quality-gen v1.1 contract.")
    parser.add_argument("--root", type=Path, default=None, help="Repository root")
    parser.add_argument("--package", type=Path, default=None, help="Optional packaged zip to validate")
    args = parser.parse_args()

    try:
        skill_name = find_skill_name(Path(__file__))
        root = args.root.resolve() if args.root else find_repo_root(Path(__file__), skill_name)
        validate_required_files(root, skill_name)
        validate_skill_contract(root, skill_name)
        validate_word_reference(root, skill_name)
        validate_mirrored_docs(root)
        validate_no_stale_claims(root, skill_name)
        if args.package:
            package_path = args.package.resolve()
            validate_zip(package_path, skill_name)
    except ValidationError as exc:
        print(f"[FAIL] {exc}")
        return 1
    except (OSError, UnicodeError, zipfile.BadZipFile) as exc:
        print(f"[FAIL] {type(exc).__name__}: {exc}")
        return 1
    except Exception as exc:
        print(f"[ERROR] unexpected {type(exc).__name__}: {exc}")
        return 2

    print("[OK] docs-quality-gen v1.1 contract validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
