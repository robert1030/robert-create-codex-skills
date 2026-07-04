#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：joan-skill-conventions 自身。執行：python3 tests/test_validate_punct.py
守三件事：① 驗證器正本自我合規 ② 四類盲區必抓、指令列長參數不誤殺 ③ sync 自動探索能找到兄弟包。
任何一項 FAIL 都不准交付或同步。"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
VP = os.path.join(ROOT, "assets", "validate_punct.py")

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


def run_vp(target):
    r = subprocess.run([sys.executable, VP, target], capture_output=True, text=True)
    return r.returncode, r.stdout


# ① 正本自我合規（掃自己與 SKILL.md 都要過）
code, _ = run_vp(VP)
check("驗證器掃自己 exit=0", code == 0)
code, _ = run_vp(os.path.join(ROOT, "SKILL.md"))
check("驗證器掃 SKILL.md exit=0", code == 0)

# ② 盲區樣本：半形句號、雙引號、單引號、緊鄰中文的雙連字號，全部要抓；
#    指令列長參數（兩側非中文）不得誤殺
with tempfile.TemporaryDirectory() as td:
    bad = os.path.join(td, "bad.html")
    with open(bad, "w", encoding="utf-8") as f:
        f.write("這句用半形句號.繼續\n連字號--當破折號\n他說\"引號\"包中文\n再用'單引號'包中文\n破折號—在此\n")
    code, out = run_vp(bad)
    check("髒樣本 exit=1", code == 1)
    check("抓到半形句號", "「.」" in out)
    check("抓到半形雙引號", '「"」' in out)
    check("抓到半形單引號", "「'」" in out)
    check("抓到雙連字號破折號", "「--」" in out)
    check("抓到 em dash", "「—」" in out)

    ok = os.path.join(td, "ok.html")
    with open(ok, "w", encoding="utf-8") as f:
        f.write("全形標點，正常。安裝時請帶 --break-system-packages 參數，小數 3.14 與網址 example.com 不受影響。\n")
    code, out = run_vp(ok)
    check("乾淨樣本 exit=0（長參數、小數、網址不誤殺）", code == 0)

# ③ sync 自動探索：在暫存環境擺兩個兄弟包，必須被找到並回報漂移
with tempfile.TemporaryDirectory() as td:
    for name in ("pkg-a", "pkg-b"):
        os.makedirs(os.path.join(td, name, "scripts"))
        with open(os.path.join(td, name, "scripts", "validate_punct.py"), "w") as f:
            f.write("OLD\n")
    me = os.path.join(td, "joan-skill-conventions")
    shutil.copytree(ROOT, me)
    r = subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py"), "--check"],
                       capture_output=True, text=True)
    check("自動探索找到 2 個兄弟包", "2 個包" in r.stdout and r.returncode == 1)
    r = subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py")],
                       capture_output=True, text=True)
    r2 = subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py"), "--check"],
                        capture_output=True, text=True)
    check("同步後再查全數一致", r2.returncode == 0)

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
