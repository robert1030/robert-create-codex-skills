#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""相依自動安裝器（唯一正本，房規六）。

原則：
  1. 分顆粒 ensure_*：偵測缺哪個裝哪個，裝過秒跳過（冪等）。
  2. 透明不等於隱瞞：每次實際安裝必留 log 訊息，使用者不動手但看得見。
  3. ensure_* 必須在對應的 import 之前呼叫。
  4. 依平台、PEP 668 與虛擬環境決定是否帶 --break-system-packages。

各包複製到自己的 scripts/bootstrap.py 後，依相依裁剪 ensure_* 顆粒。
"""
import importlib.util
import os
import subprocess
import sys
import sysconfig


def _have_py(module_name):
    return importlib.util.find_spec(module_name) is not None


def _have_npm(pkg):
    return os.path.isdir(os.path.join(os.getcwd(), "node_modules", pkg))


def _in_virtualenv():
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def _is_externally_managed():
    """Detect the PEP 668 marker used by managed Python installations."""
    stdlib = sysconfig.get_path("stdlib")
    return bool(stdlib) and os.path.exists(os.path.join(stdlib, "EXTERNALLY-MANAGED"))


def _pip_command(*pkgs, platform_name=None, externally_managed=None, in_virtualenv=None):
    """Build a portable pip command without applying Linux flags on Windows."""
    platform_name = platform_name or sys.platform
    if externally_managed is None:
        externally_managed = _is_externally_managed()
    if in_virtualenv is None:
        in_virtualenv = _in_virtualenv()

    cmd = [sys.executable, "-m", "pip", "install", "-q", *pkgs]
    if platform_name != "win32" and externally_managed and not in_virtualenv:
        cmd.insert(cmd.index("install") + 1, "--break-system-packages")
    return cmd


def _pip(*pkgs, log=print):
    try:
        subprocess.run(_pip_command(*pkgs), check=True)
        return True
    except (subprocess.CalledProcessError, OSError) as exc:
        log(f"[bootstrap] pip 安裝失敗：{' '.join(pkgs)}（{exc}）。")
        log("[bootstrap] 未能安裝相依；不會把腳本存在誤報為安裝成功。")
        return False


def _npm(*pkgs, log=print):
    try:
        subprocess.run(["npm", "install", "--silent", *pkgs], check=True)
        return True
    except (subprocess.CalledProcessError, OSError) as exc:
        log(f"[bootstrap] npm 安裝失敗：{' '.join(pkgs)}（{exc}）。")
        log("[bootstrap] 未能安裝相依；請改走不需要該套件的降級路徑。")
        return False


def ensure_export(log=print):
    """HTML 轉 PDF／PNG 匯出鏈：playwright＋chromium＋pillow。"""
    if not _have_py("playwright"):
        log("[bootstrap] 安裝 playwright...")
        if not _pip("playwright", log=log):
            return False
        log("[bootstrap] 安裝 chromium...")
        try:
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
                           check=True)
        except (subprocess.CalledProcessError, OSError) as exc:
            log(f"[bootstrap] chromium 安裝失敗（{exc}）。")
            log("[bootstrap] 未能建立匯出環境；請改用當下可用的原生匯出工具或回報未能匯出。")
            return False
    if not _have_py("PIL"):
        log("[bootstrap] 安裝 pillow...")
        if not _pip("pillow", log=log):
            return False
    return True


def ensure_katex(log=print):
    """KaTeX 伺服端預渲染。"""
    if not _have_npm("katex"):
        log("[bootstrap] 安裝 katex...")
        return _npm("katex", log=log)
    return True


def ensure_math(log=print):
    """數理驗證（SymPy 重算）。"""
    if not _have_py("sympy"):
        log("[bootstrap] 安裝 sympy...")
        return _pip("sympy", log=log)
    return True


def ensure_font_tools(log=print):
    """字型子集化為 woff2 內嵌。"""
    need = []
    if not _have_py("fontTools"):
        need.append("fonttools")
    if not _have_py("brotli"):
        need.append("brotli")
    if need:
        log(f"[bootstrap] 安裝 {' '.join(need)}...")
        return _pip(*need, log=log)
    return True


def ensure_chem(log=print):
    """化學結構繪製與驗證。"""
    if not _have_py("rdkit"):
        log("[bootstrap] 安裝 rdkit...")
        return _pip("rdkit", log=log)
    return True
