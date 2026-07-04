#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codex 版透明自動安裝（房規六：偵測執行環境，不寫死 --break-system-packages）。

Claude 版固定在同一個 Ubuntu 沙箱容器，pip 一律可以放心帶
--break-system-packages。Codex 常跑在使用者自己的機器或設定過的環境，
作業系統、Python 安裝方式（系統 Python／Homebrew／pyenv／虛擬環境）都不
一定，所以每次安裝前才判斷「這個環境需不需要、允許不允許」那個旗標，
而不是照抄 Claude 版的固定假設。

裝不了就誠實回報、建議手動處理，不假裝成功（呼應房規五：能力邊界誠實）。

用法（在其他 skill 的腳本裡，ensure 一定要在對應的 import 之前呼叫）：

    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import bootstrap
    if not bootstrap.ensure("playwright"):
        raise SystemExit("playwright 安裝失敗，請手動處理後再試一次。")
    from playwright.sync_api import sync_playwright
"""
import importlib.util
import os
import subprocess
import sys
import sysconfig


def _is_externally_managed() -> bool:
    """偵測 PEP 668：這個 Python 是不是『外部管理』（Debian／Homebrew 常見）。
    只有外部管理且不在虛擬環境裡時，pip 才需要 --break-system-packages。"""
    stdlib = sysconfig.get_path("stdlib")
    marker = os.path.join(stdlib, "EXTERNALLY-MANAGED")
    return os.path.exists(marker)


def _in_virtualenv() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def _have_py(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


def _pip_install(*pkgs, log=print) -> bool:
    """依環境組裝正確的 pip 指令，裝不了誠實回報，不硬裝、不假裝成功。"""
    cmd = [sys.executable, "-m", "pip", "install", "-q", *pkgs]
    if _is_externally_managed() and not _in_virtualenv():
        cmd.insert(cmd.index("install") + 1, "--break-system-packages")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as exc:
        log(f"[bootstrap] 安裝失敗：{' '.join(pkgs)}（{exc}）。")
        log("[bootstrap] 這個環境可能需要你先建立虛擬環境再試一次，不會硬裝進系統 Python。")
        return False
    except FileNotFoundError:
        log("[bootstrap] 找不到 pip，這個環境可能沒有網路或套件管理工具，請手動處理。")
        return False


def ensure(*modules, pip_names=None, log=print) -> bool:
    """分顆粒 ensure：缺哪個裝哪個，裝過秒跳過。回傳是否全數到位。

    modules：要匯入的模組名（例如 "PIL"）。
    pip_names：模組名對應到 pip 套件名的字典，模組名和套件名不同時才需要
                （例如 {"PIL": "pillow"}）。
    """
    pip_names = pip_names or {}
    missing = [m for m in modules if not _have_py(m)]
    if not missing:
        return True
    log(f"[bootstrap] 偵測到缺少：{', '.join(missing)}，準備安裝…")
    to_install = [pip_names.get(m, m) for m in missing]
    return _pip_install(*to_install, log=log)


def ensure_npm(package: str, log=print) -> bool:
    """node 相依的簡化版：檢查 node_modules 底下有沒有這個套件，缺了就裝。
    比 pip 更依賴當下工作目錄，呼叫端要自行確認執行目錄正確。"""
    target = os.path.join(os.getcwd(), "node_modules", package)
    if os.path.isdir(target):
        return True
    log(f"[bootstrap] 偵測到缺少 npm 套件：{package}，準備安裝…")
    try:
        subprocess.run(["npm", "install", "--silent", package], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        log(f"[bootstrap] npm 安裝失敗：{package}（{exc}）。請確認這個環境有 node／npm。")
        return False


# 依 skill 實際用到的重相依擴充分顆粒 ensure_*，例如：
#
# def ensure_export(log=print) -> bool:
#     ok = ensure("playwright", log=log)
#     if ok:
#         subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
#                         check=False)
#     return ok and ensure("PIL", pip_names={"PIL": "pillow"}, log=log)
#
# def ensure_math(log=print) -> bool:
#     return ensure("sympy", log=log)
