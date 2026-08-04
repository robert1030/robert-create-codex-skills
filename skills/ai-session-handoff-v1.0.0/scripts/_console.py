#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""主控台輸出自保：讓驗證器在 CP950／Big5 主控台也不會因為編碼而崩潰。

作法是保留主控台原本的編碼，只把錯誤處理改成 backslashreplace：
繁體中文在 CP950 可正常編碼，少數無法編碼的字元會以跳脫字串顯示，
不會拋 UnicodeEncodeError，也不會靜默吞掉訊息。
本套件自己的訊息一律使用 ASCII 標記（[OK]／[FAIL]／[WARN]）而不用符號圖示。
"""
import sys


def configure_console():
    """在程式入口呼叫一次。舊版 Python 或非 TextIO 串流時安靜跳過。"""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(errors="backslashreplace")
        except (ValueError, OSError):
            pass
