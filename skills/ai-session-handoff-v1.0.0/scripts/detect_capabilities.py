#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""能力偵測與暫存目錄解析：決定交接文件走哪一條輸出分支。

設計原則（對應 references/platform-capabilities.md）：
  1. 不以平台名稱決定行為，一律偵測實際能力。
  2. 偵測不到的事實回報 UNKNOWN，不猜測（例如網路存取政策、
     宿主是否允許建立附件、對話可見範圍）。
  3. 暫存目錄由環境解析取得，不硬編碼任何單一路徑，
     並以實際寫入與回讀來確認可用。
  4. 能力缺席不是失敗，而是選擇對應的降級分支。

用法：
  python scripts/detect_capabilities.py          以 JSON 輸出偵測結果
"""
import json
import os
import shutil
import sys
import tempfile

UNKNOWN = "UNKNOWN"

# 需求盤點的能力清單；references/platform-capabilities.md 必須逐項說明降級行為。
CAPABILITY_KEYS = (
    "filesystem_write",
    "temp_dir",
    "shell",
    "python",
    "powershell",
    "git",
    "network",
    "conversation_full_access",
    "attachment_create",
    "plain_text_output",
    "validator_runnable",
)

# 依能力挑選輸出分支，順序即優先序。
MODES = ("agent", "web", "text-only")


def _writable(path):
    """以實際寫入、回讀、刪除確認可寫，避免只看旗標就宣稱成功。"""
    probe = None
    try:
        handle, probe = tempfile.mkstemp(prefix=".handoff-probe-", dir=path)
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("probe\n")
        with open(probe, encoding="utf-8") as fh:
            return fh.read() == "probe\n"
    except (OSError, ValueError):
        return False
    finally:
        if probe and os.path.exists(probe):
            try:
                os.unlink(probe)
            except OSError:
                pass


def resolve_temp_dir(environ=None):
    """回傳 (可用暫存目錄或 None, 嘗試過的候選清單)。

    候選來源：tempfile.gettempdir()（已涵蓋 TMPDIR／TEMP／TMP 與系統 API）、
    環境變數逐一嘗試、家目錄、當前工作目錄。全部失敗回傳 None，由呼叫端降級。
    """
    environ = os.environ if environ is None else environ
    candidates = []
    try:
        candidates.append(tempfile.gettempdir())
    except (OSError, AttributeError):
        pass
    for key in ("TMPDIR", "TEMP", "TMP", "XDG_RUNTIME_DIR"):
        value = environ.get(key)
        if value:
            candidates.append(value)
    home = environ.get("HOME") or environ.get("USERPROFILE")
    if home:
        candidates.append(home)
    candidates.append(os.getcwd())

    tried = []
    for candidate in candidates:
        if candidate in tried:
            continue
        tried.append(candidate)
        if os.path.isdir(candidate) and _writable(candidate):
            return candidate, tried
    return None, tried


def detect(environ=None, which=None, temp_resolver=None):
    """回傳能力字典。參數可注入，方便測試模擬缺能力的平台。"""
    environ = os.environ if environ is None else environ
    which = shutil.which if which is None else which
    temp_resolver = resolve_temp_dir if temp_resolver is None else temp_resolver

    temp_dir, tried = temp_resolver(environ)

    cwd_writable = _writable(os.getcwd()) if os.path.isdir(os.getcwd()) else False
    shell = bool(which("bash") or which("sh") or which("cmd") or which("cmd.exe"))
    powershell = bool(which("pwsh") or which("powershell"))

    caps = {
        "filesystem_write": bool(temp_dir) or cwd_writable,
        "temp_dir": temp_dir or False,
        "temp_dir_candidates_tried": tried,
        "shell": shell,
        "python": True,                      # 本檔跑得起來就代表有 Python
        "powershell": powershell,
        "git": bool(which("git")),
        "network": UNKNOWN,                  # 不主動連線探測，也不假設
        "conversation_full_access": UNKNOWN,  # 由執行中的 agent 自行判斷並誠實聲明
        "attachment_create": UNKNOWN,        # 宿主能力，偵測不到就不宣稱
        "plain_text_output": True,
        "validator_runnable": True,
    }
    caps["mode"] = choose_mode(caps)
    caps["degradation_path"] = degradation_path(caps)
    return caps


def write_and_verify(path, text):
    """以 UTF-8 without BOM ＋ LF 寫入後回讀比對，回傳 (是否成功, 完整路徑, 訊息)。

    回讀比對失敗或寫入失敗時回傳 False，呼叫端不得宣稱寫入成功。
    """
    full = os.path.abspath(path)
    try:
        with open(full, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    except OSError as exc:
        return False, full, "寫入失敗：{0}".format(exc)
    try:
        with open(full, encoding="utf-8", newline="") as handle:
            back = handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        return False, full, "回讀失敗：{0}".format(exc)
    if back.replace("\r\n", "\n") != text.replace("\r\n", "\n"):
        return False, full, "回讀內容與寫入內容不符，請勿宣稱寫入成功"
    return True, full, "已寫入並回讀驗證：{0}".format(full)


def choose_mode(caps):
    """依能力選分支：可寫暫存走 agent；否則走 web；連純文字都受限走 text-only。"""
    if caps.get("filesystem_write") and caps.get("temp_dir"):
        return "agent"
    if caps.get("plain_text_output"):
        return "web"
    return "text-only"


def degradation_path(caps):
    """回傳實際會採用的降級順序，供交接文件誠實記錄。"""
    ladder = []
    if caps.get("temp_dir"):
        ladder.append("寫入暫存目錄並回讀驗證")
    else:
        ladder.append("暫存目錄不可用：改為使用者明確指定的路徑")
    if not caps.get("filesystem_write"):
        ladder.append("無檔案系統：改為對話內單一 Markdown 區塊")
    if not caps.get("validator_runnable"):
        ladder.append("無法執行驗證器：改為逐節人工自檢並在交付時聲明未跑機器驗證")
    ladder.append("最低保證：純文字輸出完整九節內容")
    return ladder


def main(argv):
    from _console import configure_console
    configure_console()
    caps = detect()
    if "--mode" in argv:
        print(caps["mode"])
        return 0
    print(json.dumps(caps, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))
