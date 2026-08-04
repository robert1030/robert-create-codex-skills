#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""執行全部回歸測試並匯總為單一退出碼。

用法：
  python tests/run_all.py
"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from _console import configure_console  # noqa: E402

ORDER = [
    "test_structure.py",
    "test_redaction.py",
    "test_encoding.py",
    "test_platform_fallbacks.py",
    "test_invocation.py",
    "test_golden.py",
    "test_legacy_absence.py",
]


def main():
    configure_console()
    found = {os.path.basename(p) for p in glob.glob(os.path.join(HERE, "test_*.py"))}
    missing = found - set(ORDER)
    if missing:
        print("[WARN] 未列入執行順序的測試檔：{0}".format(sorted(missing)))
    results = []
    for name in ORDER + sorted(missing):
        path = os.path.join(HERE, name)
        if not os.path.isfile(path):
            print("[FAIL] 找不到測試檔：{0}".format(name))
            results.append((name, 1))
            continue
        print("\n===== {0} =====".format(name))
        proc = subprocess.run([sys.executable, path])
        results.append((name, proc.returncode))
    print("\n===== 匯總 =====")
    failed = [name for name, code in results if code != 0]
    for name, code in results:
        print("  {0} {1}".format("[OK]  " if code == 0 else "[FAIL]", name))
    if failed:
        print("\n[FAIL] {0} 支測試檔未通過：{1}".format(len(failed), failed))
        return 1
    print("\n[OK] 全部 {0} 支測試檔通過。".format(len(results)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
