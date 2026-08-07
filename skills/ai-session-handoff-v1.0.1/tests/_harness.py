#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""測試共用小工具：無外部相依，離線可跑。"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRIPTS = os.path.join(ROOT, "scripts")
FIXTURES = os.path.join(HERE, "fixtures")

sys.path.insert(0, SCRIPTS)

from _console import configure_console  # noqa: E402

configure_console()

_STATE = {"pass": 0, "fail": 0}


def check(name, cond):
    if cond:
        _STATE["pass"] += 1
        print("  [PASS] {0}".format(name))
    else:
        _STATE["fail"] += 1
        print("  [FAIL] {0}".format(name))
    return bool(cond)


def summary(title):
    print("\n{0}：{1} passed, {2} failed".format(title, _STATE["pass"], _STATE["fail"]))
    return 0 if _STATE["fail"] == 0 else 1


def temp_file(content, suffix=".md", encoding="utf-8", raw=None):
    """寫出暫存檔並回傳路徑；raw 為 bytes 時直接寫二進位。"""
    handle, path = tempfile.mkstemp(suffix=suffix)
    if raw is not None:
        with os.fdopen(handle, "wb") as fh:
            fh.write(raw)
    else:
        with os.fdopen(handle, "w", encoding=encoding, newline="") as fh:
            fh.write(content)
    return path


def read_package_file(rel):
    from check_encoding import read_text
    return read_text(os.path.join(ROOT, rel), allow_bom=True)[0]
