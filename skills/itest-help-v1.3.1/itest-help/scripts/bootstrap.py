#!/usr/bin/env python3
"""iTest Help skill 的 runtime 檢查。此包只使用 Python 標準函式庫。"""

from __future__ import annotations

import sys


def ensure_runtime() -> bool:
    if sys.version_info < (3, 9):
        print("[bootstrap] Python 3.9 或更高版本為必要條件。")
        return False
    print("[bootstrap] 不需要安裝額外相依套件。")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if ensure_runtime() else 1)
