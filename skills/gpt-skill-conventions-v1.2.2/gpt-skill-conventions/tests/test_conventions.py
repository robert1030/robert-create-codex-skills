#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：gpt-skill-conventions 本包（房規二不豁免自己）。
執行：python tests/test_conventions.py
不需重相依：驗證器行為、bootstrap 分支（攔截不真裝）、sync 漂移偵測、manifest 完整性。
"""
import json
import importlib
import os
import subprocess
import sys
import tempfile
import types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "assets"))

PASS = 0
FAIL = 0
EM = chr(0x2014)
EN = chr(0x2013)


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


def run_punct(content, suffix):
    path = tempfile.mktemp(suffix=suffix)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "assets", "validate_punct.py"), path],
                       capture_output=True)
    os.remove(path)
    return r.returncode


print("== 1. validate_punct 行為 ==")
check("乾淨 HTML 通過", run_punct("<p>你好，世界。數字 1,000 與 3.14 合法。</p>", ".html") == 0)
check("中文夾半形逗號被擋", run_punct("<p>你好,世界</p>", ".html") == 1)
check("中文夾半形句點被擋", run_punct("<p>結束了.然後呢</p>", ".html") == 1)
check("em dash 被擋", run_punct("<p>hello " + EM + " world</p>", ".html") == 1)
check("en dash 被擋", run_punct("<p>pages 3" + EN + "5</p>", ".html") == 1)
check("半形連字號放行", run_punct("<p>2023-2024 與 e-mail 合法。</p>", ".html") == 0)
check("style 區塊內半形不算錯", run_punct("<style>a{color:red;}</style><p>正文。</p>", ".html") == 0)
check("md 程式碼區塊略過", run_punct("正文合法。\n```python\nprint('a,b')  # " + EM + " here\n```\n", ".md") == 0)
check("md 內文破折號被擋", run_punct("正文" + EM + EM + "不合法。\n", ".md") == 1)
check("md inline code 略過", run_punct("指令 `a,b " + EM + " c` 合法。\n", ".md") == 0)

print("== 2. bootstrap 分支（攔截，不真的安裝）==")
import bootstrap
calls = []
bootstrap._pip = lambda *p, **k: calls.append(("pip", p)) or True
bootstrap._npm = lambda *p, **k: calls.append(("npm", p)) or True
bootstrap.subprocess = types.SimpleNamespace(run=lambda *a, **k: None)

bootstrap._have_py = lambda m: True
bootstrap._have_npm = lambda p: True
calls.clear()
bootstrap.ensure_export(log=lambda *a: None)
bootstrap.ensure_katex(log=lambda *a: None)
bootstrap.ensure_math(log=lambda *a: None)
check("相依已在 → 不重裝", calls == [])

bootstrap._have_py = lambda m: False
bootstrap._have_npm = lambda p: False
calls.clear()
bootstrap.ensure_export(log=lambda *a: None)
check("相依缺少 → 嘗試安裝", len(calls) >= 1)

logged = []
calls.clear()
bootstrap.ensure_math(log=lambda *a: logged.append(a))
check("實際安裝有留 log", len(logged) >= 1)

print("== 2a. bootstrap 跨平台 pip 參數 ==")
windows_cmd = bootstrap._pip_command(
    "sympy", platform_name="win32", externally_managed=True, in_virtualenv=False
)
linux_cmd = bootstrap._pip_command(
    "sympy", platform_name="linux", externally_managed=True, in_virtualenv=False
)
venv_cmd = bootstrap._pip_command(
    "sympy", platform_name="linux", externally_managed=True, in_virtualenv=True
)
check("Windows 不帶 --break-system-packages", "--break-system-packages" not in windows_cmd)
check("Linux PEP 668 環境帶 --break-system-packages", "--break-system-packages" in linux_cmd)
check("虛擬環境不帶 --break-system-packages", "--break-system-packages" not in venv_cmd)

print("== 2b. bootstrap 失敗降級 ==")
bootstrap = importlib.reload(bootstrap)

def raise_install_error(*args, **kwargs):
    raise subprocess.CalledProcessError(1, args[0] if args else "install")

bootstrap.subprocess = types.SimpleNamespace(
    run=raise_install_error,
    CalledProcessError=subprocess.CalledProcessError,
)
logged = []
check("pip 失敗回傳 False", bootstrap._pip("sympy", log=logged.append) is False)
check("pip 失敗留 log", bool(logged))

bootstrap.subprocess = types.SimpleNamespace(
    run=lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError("npm")),
    CalledProcessError=subprocess.CalledProcessError,
)
logged = []
check("npm 不存在回傳 False", bootstrap._npm("katex", log=logged.append) is False)
check("npm 不存在留 log", bool(logged))

bootstrap._have_py = lambda module: module == "PIL"
bootstrap._pip = lambda *pkgs, **kwargs: True
bootstrap.subprocess = types.SimpleNamespace(
    run=raise_install_error,
    CalledProcessError=subprocess.CalledProcessError,
)
logged = []
check("Chromium 失敗回傳 False", bootstrap.ensure_export(log=logged.append) is False)
check("Chromium 失敗留 log", bool(logged))

print("== 3. manifest 完整性 ==")
with open(os.path.join(ROOT, "assets", "manifest.json"), encoding="utf-8") as f:
    manifest = json.load(f)
check("manifest 至少含兩個正本", len(manifest["assets"]) >= 2)
ok = all(os.path.exists(os.path.join(ROOT, a["canonical"])) for a in manifest["assets"])
check("manifest 所列正本檔皆存在", ok)

print("== 4. sync 漂移偵測 ==")
with tempfile.TemporaryDirectory() as tmp:
    pkg = os.path.join(tmp, "fake-skill", "scripts")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "validate_punct.py"), "w", encoding="utf-8") as f:
        f.write("# drifted copy\n")
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "sync_validator.py"),
                        "--check", os.path.join(tmp, "fake-skill")], capture_output=True)
    check("漂移副本 --check 退出碼 1", r.returncode == 1)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "sync_validator.py"),
                        os.path.join(tmp, "fake-skill")], capture_output=True)
    check("同步後寫入成功", r.returncode == 0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "sync_validator.py"),
                        "--check", os.path.join(tmp, "fake-skill")], capture_output=True)
    check("同步後 --check 全一致", r.returncode == 0)

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
