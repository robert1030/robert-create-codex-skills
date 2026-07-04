#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：codex-skill-conventions 自身。
執行方式依平台：Linux／macOS 用 python3，Windows 用 py 或 python，指令為 <啟動器> tests/test_validate_punct.py。
測試內部子程序一律走 sys.executable，與啟動器名稱無關。
守五件事：① 驗證器正本自我合規（掃遍本包全部文件與腳本，tests 除外）
② 四類盲區必抓、指令列長參數不誤殺 ③ sync 自動探索能找到兄弟包
④ bootstrap 旗標邏輯（不觸發真實安裝） ⑤ 轉換器 frontmatter 檢查與 yaml 草稿。
任何一項 FAIL 都不准交付或同步。"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
VP = os.path.join(ROOT, "assets", "validate_punct.py")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

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


# ① 正本自我合規：掃遍本包全部文件與腳本（tests 目錄除外，因測試內含故意的髒樣本字串）
scan_targets = [VP, os.path.join(ROOT, "SKILL.md")]
for sub in ("references", "scripts", "agents"):
    d = os.path.join(ROOT, sub)
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith((".md", ".py", ".yaml")):
                scan_targets.append(os.path.join(d, fn))
lessons = os.path.join(ROOT, "LESSONS.md")
if os.path.exists(lessons):
    scan_targets.append(lessons)
for tgt in scan_targets:
    code, out = run_vp(tgt)
    check(f"掃 {os.path.relpath(tgt, ROOT)} exit=0", code == 0)

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

# ③ sync 自動探索：在暫存環境擺兩個兄弟包，必須被找到並回報漂移，同步後一致
with tempfile.TemporaryDirectory() as td:
    for name in ("pkg-a", "pkg-b"):
        os.makedirs(os.path.join(td, name, "scripts"))
        with open(os.path.join(td, name, "scripts", "validate_punct.py"), "w") as f:
            f.write("OLD\n")
    me = os.path.join(td, "codex-skill-conventions")
    shutil.copytree(ROOT, me)
    r = subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py"), "--check"],
                       capture_output=True, text=True)
    check("自動探索找到 2 個兄弟包", "2 個包" in r.stdout and r.returncode == 1)
    subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py")],
                   capture_output=True, text=True)
    r2 = subprocess.run([sys.executable, os.path.join(me, "scripts", "sync_validator.py"), "--check"],
                        capture_output=True, text=True)
    check("同步後再查全數一致", r2.returncode == 0)

# ④ bootstrap 旗標邏輯：攔截 subprocess，不觸發真實安裝
import bootstrap

calls = []
_orig_run = bootstrap.subprocess.run


def _fake_run(cmd, *a, **k):
    calls.append(list(cmd))
    class R:
        returncode = 0
    return R()


bootstrap.subprocess.run = _fake_run
try:
    check("已裝模組不重裝（ensure 回 True 且不呼叫 pip）",
          bootstrap.ensure("json") is True and not calls)

    _em, _venv = bootstrap._is_externally_managed, bootstrap._in_virtualenv
    bootstrap._is_externally_managed = lambda: True
    bootstrap._in_virtualenv = lambda: False
    bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None)
    check("外部管理且非 venv：帶 --break-system-packages",
          calls and "--break-system-packages" in calls[-1])

    calls.clear()
    bootstrap._is_externally_managed = lambda: False
    bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None)
    check("非外部管理：不帶 --break-system-packages",
          calls and "--break-system-packages" not in calls[-1])

    calls.clear()
    bootstrap._is_externally_managed = lambda: True
    bootstrap._in_virtualenv = lambda: True
    bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None)
    check("在 venv 內：不帶 --break-system-packages",
          calls and "--break-system-packages" not in calls[-1])

    check("pip_names 對映生效（PIL 對映 pillow）",
          (calls.clear() or bootstrap.ensure("this_module_never_exists_xyz",
                                             pip_names={"this_module_never_exists_xyz": "pillow"},
                                             log=lambda *a: None) or True) and "pillow" in calls[-1])
finally:
    bootstrap.subprocess.run = _orig_run
    bootstrap._is_externally_managed = _em
    bootstrap._in_virtualenv = _venv

# ⑤ 轉換器 frontmatter 檢查與 yaml 草稿
import convert_from_claude_skill as conv

check("合法 frontmatter 無問題",
      conv.validate_frontmatter({"name": "good-name", "description": "x" * 30}) == [])
check("抓到大寫 name",
      any("不符合" in p for p in conv.validate_frontmatter({"name": "BadName", "description": "x"})))
check("抓到連續連字號",
      any("連續連字號" in p for p in conv.validate_frontmatter({"name": "a--b", "description": "x"})))
check("抓到 description 超過上限",
      any("超過" in p for p in conv.validate_frontmatter({"name": "ok", "description": "x" * 1025})))
check("抓到多餘欄位",
      any("不認得的欄位" in p for p in conv.validate_frontmatter({"name": "ok", "description": "x", "version": 1})))
_short = conv.guess_short_description("這是一段夠長的描述句，用來測試截取邏輯是否落在合理長度之內，並且不會超過上限。後面還有第二句。")
check("short_description 草稿落在二十五至六十四字", 25 <= len(_short) <= 64)
_yaml = conv.build_openai_yaml("my-skill", "描述文字，測試用的一段夠長的描述文字，超過二十五個字以便通過檢查。")
check("yaml 草稿 default_prompt 含 $skill-name", "$my-skill" in _yaml)

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
