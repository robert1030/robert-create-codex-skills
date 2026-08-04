#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""編碼、換行與標點測試（含 CP950 主控台模擬）。"""
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import ROOT, SCRIPTS, check, summary, temp_file  # noqa: E402
from _sample import good_doc  # noqa: E402

import check_encoding  # noqa: E402

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "encoding")
VP = os.path.join(SCRIPTS, "validate_punct.py")
VH = os.path.join(SCRIPTS, "validate_handoff.py")

MIXED = "混合內容 mixed content 100% 完成 🚀 測試 emoji 與中英夾雜。\n"

print("== 讀檔與正規化 ==")
path = temp_file("純 UTF-8 內容。\n")
text, issues = check_encoding.read_text(path)
check("UTF-8 without BOM 無警告", issues == [] and text.startswith("純"))
os.unlink(path)

path = temp_file("", raw=b"\xef\xbb\xbf" + "帶 BOM 的內容。\n".encode("utf-8"))
text, issues = check_encoding.read_text(path)
check("偵測到 BOM", any("BOM" in i for i in issues))
check("BOM 已剝除", text.startswith("帶"))
check("allow_bom 時不視為問題", check_encoding.read_text(path, allow_bom=True)[1] == [])
os.unlink(path)

path = temp_file("", raw="第一行。\r\n第二行。\r\n".encode("utf-8"))
_text, issues = check_encoding.read_text(path)
check("偵測到 CRLF", any("CRLF" in i for i in issues))
os.unlink(path)

path = temp_file("", raw="繁體中文以 CP950 儲存。\n".encode("cp950"))
text, issues = check_encoding.read_text(path)
check("CP950 明確判定後正規化", any("cp950" in i.lower() for i in issues))
check("CP950 內容正確還原", "繁體中文" in text)
os.unlink(path)

path = temp_file("", raw=b"\xff\xfe\x00\x01\x02 invalid \x81\x40\xff")
try:
    check_encoding.read_text(path)
    check("不可解碼內容拋出 DecodeFailure", False)
except check_encoding.DecodeFailure as exc:
    message = str(exc)
    check("不可解碼內容拋出 DecodeFailure", True)
    check("錯誤訊息含檔名", os.path.basename(path) in message)
    check("錯誤訊息含嘗試過的編碼", "utf-8" in message and "cp950" in message)
    check("錯誤訊息含 byte 位置", "byte" in message)
os.unlink(path)

print("== 套件 canonical 編碼 ==")
problems, checked = check_encoding.check_tree(ROOT)
if not check("套件全為 UTF-8 without BOM ＋ LF（{0} 檔）".format(checked), problems == []):
    for item in problems[:10]:
        print("      {0}".format(item))
check("刻意編碼 fixture 已排除於 canonical 檢查", os.path.isdir(FIXTURE_DIR))

print("== fixture 檔案實際內容 ==")
bom_fixture = os.path.join(FIXTURE_DIR, "utf8_bom.md")
cp950_fixture = os.path.join(FIXTURE_DIR, "cp950.md")
broken_fixture = os.path.join(FIXTURE_DIR, "undecodable.bin")
crlf_fixture = os.path.join(FIXTURE_DIR, "crlf.md")
check("BOM fixture 存在且確實帶 BOM",
      os.path.isfile(bom_fixture) and open(bom_fixture, "rb").read(3) == b"\xef\xbb\xbf")
check("CP950 fixture 存在且非 UTF-8", os.path.isfile(cp950_fixture)
      and any("cp950" in i.lower() for i in check_encoding.read_text(cp950_fixture)[1]))
check("CRLF fixture 存在且含 CRLF",
      os.path.isfile(crlf_fixture) and b"\r\n" in open(crlf_fixture, "rb").read())
ok = False
try:
    check_encoding.read_text(broken_fixture)
except check_encoding.DecodeFailure:
    ok = True
check("不可解碼 fixture 會被明確回報", ok)

print("== 標點鐵則 ==")


def run(script, target, env=None):
    merged = dict(os.environ)
    merged["PYTHONUTF8"] = "1"
    if env:
        merged.update(env)
    return subprocess.run([sys.executable, script, target], capture_output=True, env=merged)


def run_vp(content):
    path = temp_file(content)
    try:
        return run(VP, path).returncode
    finally:
        os.unlink(path)


check("全形乾淨過", run_vp("這是一句全形標點，沒有問題。\n") == 0)
check("半形夾中文擋", run_vp("這是半形,錯誤示範\n") != 0)
check("破折號擋", run_vp("這裡有破折號——不行\n") != 0)
check("半形連字號放行", run_vp("UTF-8 與 2023-2024 都合法\n") == 0)

md_files = sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
md_files = [p for p in md_files if "fixtures" + os.sep + "encoding" not in p]
dirty = [p for p in md_files if run(VP, p).returncode != 0]
if not check("套件內全部 Markdown 標點乾淨（{0} 檔）".format(len(md_files)), dirty == []):
    for item in dirty:
        print("      {0}".format(os.path.relpath(item, ROOT)))

print("== 內容型態 ==")
path = temp_file(good_doc({2: MIXED}))
try:
    check("中英夾雜與 emoji 內容通過驗證", run(VH, path).returncode == 0)
finally:
    os.unlink(path)

path = temp_file(good_doc().replace("\n", "\r\n"))
try:
    result = run(VH, path)
    check("CRLF 交接文件仍通過（僅警告）", result.returncode == 0)
    check("CRLF 有被提醒", b"WARN" in result.stdout)
finally:
    os.unlink(path)

path = temp_file("", raw=b"\xef\xbb\xbf" + good_doc().encode("utf-8"))
try:
    result = run(VH, path)
    check("帶 BOM 的交接文件仍可驗證", result.returncode == 0)
    check("BOM 有被提醒", b"WARN" in result.stdout and "BOM".encode() in result.stdout)
finally:
    os.unlink(path)

path = temp_file("", raw=b"\xff\xfe" + good_doc().encode("utf-16-le"))
try:
    result = run(VH, path)
    check("UTF-16 交接文件被擋（PowerShell 5.1 的 Out-File 預設）", result.returncode == 1)
    check("UTF-16 失敗訊息含 byte 位置", b"byte" in result.stdout)
finally:
    os.unlink(path)

print("== CP950 主控台模擬 ==")
path = temp_file(good_doc())
try:
    result = run(VH, path, env={"PYTHONUTF8": "0", "PYTHONIOENCODING": "cp950"})
    check("CP950 主控台下不崩潰（退出碼 0）", result.returncode == 0)
    check("CP950 主控台下無 traceback", b"Traceback" not in result.stderr)
finally:
    os.unlink(path)

path = temp_file(good_doc({8: "- 沒有涵蓋聲明 [UNVERIFIED]"}))
try:
    result = run(VH, path, env={"PYTHONUTF8": "0", "PYTHONIOENCODING": "cp950"})
    check("CP950 主控台下仍能回報失敗（退出碼 1）", result.returncode == 1)
    check("CP950 主控台下失敗訊息可輸出", b"FAIL" in result.stdout)
finally:
    os.unlink(path)

sys.exit(summary("test_encoding"))
