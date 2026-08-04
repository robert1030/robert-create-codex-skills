#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transparent, idempotent dependency installer for the RAG chunker."""

from __future__ import annotations

import argparse
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

CORE_PYTHON = {
    "fitz": "pymupdf",
    "bs4": "beautifulsoup4",
    "lxml": "lxml",
    "PIL": "pillow",
    "cv2": "opencv-python-headless",
    "pillow_heif": "pillow-heif",
    "pytesseract": "pytesseract",
    "charset_normalizer": "charset-normalizer",
    "yaml": "pyyaml",
}
VIDEO_PYTHON = {
    "faster_whisper": "faster-whisper",
}
SYSTEM_EXECUTABLES = {
    "ffmpeg": "ffmpeg",
    "ffprobe": "ffmpeg",
    "libreoffice": "libreoffice",
    "tesseract": "tesseract-ocr",
}
APT_PACKAGES = [
    "ffmpeg",
    "libreoffice",
    "tesseract-ocr",
    "tesseract-ocr-eng",
    "tesseract-ocr-chi-tra",
    "tesseract-ocr-chi-sim",
]
BREW_PACKAGES = ["ffmpeg", "libreoffice", "tesseract", "tesseract-lang"]
WINGET_PACKAGES = [
    "Gyan.FFmpeg",
    "TheDocumentFoundation.LibreOffice",
    "UB-Mannheim.TesseractOCR",
]


def log(message: str) -> None:
    print(message, flush=True)


def _have_module(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


def _externally_managed_python() -> bool:
    if sys.prefix != getattr(sys, "base_prefix", sys.prefix):
        return False
    if os.name == "nt":
        return False
    candidates = [
        Path(sys.prefix) / "EXTERNALLY-MANAGED",
        Path(sys.prefix) / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "EXTERNALLY-MANAGED",
    ]
    return any(path.exists() for path in candidates)


def _pip_install(packages: list[str]) -> None:
    if not packages:
        return
    command = [sys.executable, "-m", "pip", "install"]
    if _externally_managed_python():
        command.append("--break-system-packages")
    command.extend(packages)
    log(f"[bootstrap] 安裝 Python 套件：{' '.join(packages)}")
    subprocess.run(command, check=True)


def ensure_python(group: str = "all") -> None:
    requirements = dict(CORE_PYTHON)
    if group in {"video", "all"}:
        requirements.update(VIDEO_PYTHON)
    missing = [package for module, package in requirements.items() if not _have_module(module)]
    _pip_install(missing)
    if not missing:
        log("[bootstrap] Python 相依已齊備。")


def _run_as_root(command: list[str]) -> None:
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        subprocess.run(command, check=True)
        return
    sudo = shutil.which("sudo")
    if sudo:
        subprocess.run([sudo, *command], check=True)
        return
    raise PermissionError("system_install_requires_root_or_sudo")


def _install_apt() -> None:
    log(f"[bootstrap] 使用 apt 安裝系統套件：{' '.join(APT_PACKAGES)}")
    _run_as_root(["apt-get", "update"])
    _run_as_root(["apt-get", "install", "-y", *APT_PACKAGES])


def _install_brew() -> None:
    log(f"[bootstrap] 使用 Homebrew 安裝系統套件：{' '.join(BREW_PACKAGES)}")
    subprocess.run(["brew", "install", *BREW_PACKAGES], check=True)


def _install_winget() -> None:
    for package in WINGET_PACKAGES:
        log(f"[bootstrap] 使用 winget 安裝：{package}")
        subprocess.run([
            "winget", "install", "--exact", "--id", package,
            "--accept-package-agreements", "--accept-source-agreements",
        ], check=True)


def ensure_system() -> None:
    missing = [name for name in SYSTEM_EXECUTABLES if not shutil.which(name)]
    if not missing:
        log("[bootstrap] 系統程式已齊備。")
        return
    log(f"[bootstrap] 缺少系統程式：{' '.join(missing)}")
    if shutil.which("apt-get"):
        _install_apt()
    elif shutil.which("brew"):
        _install_brew()
    elif shutil.which("winget"):
        _install_winget()
    else:
        raise RuntimeError("unsupported_system_package_manager")


def verify_tesseract_languages() -> None:
    executable = shutil.which("tesseract")
    if not executable:
        raise RuntimeError("missing_system_dependency:tesseract")
    completed = subprocess.run(
        [executable, "--list-langs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    available = set(completed.stdout.split())
    required = {"chi_tra", "chi_sim", "eng"}
    missing = sorted(required - available)
    if missing:
        raise RuntimeError(f"missing_tesseract_languages:{','.join(missing)}")
    log("[bootstrap] Tesseract 語言資料已包含 chi_tra、chi_sim、eng。")


def write_log(path: Path, message: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(message + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install multiformat-rag-chunker dependencies.")
    parser.add_argument("--group", choices=["core", "video", "all"], default="all")
    parser.add_argument("--no-system", action="store_true", help="Skip system package installation.")
    parser.add_argument("--log-file", type=Path, default=Path("bootstrap.log"))
    args = parser.parse_args()
    try:
        ensure_python(args.group)
        if not args.no_system:
            ensure_system()
            verify_tesseract_languages()
        message = "[bootstrap] 相依安裝與驗證完成。"
        log(message)
        write_log(args.log_file, message)
        return 0
    except Exception as exc:
        message = f"[bootstrap] 失敗：{exc}"
        log(message)
        write_log(args.log_file, message)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
