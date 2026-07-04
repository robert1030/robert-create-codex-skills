#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 validate_punct.py 正本（assets/validate_punct.py）一鍵同步到各 skill 包。

避免「每包各放一份、其中一份漏改」的分歧（這正是禁破折號漏網事件的成因）。
正本只有一處：本 skill 的 assets/validate_punct.py。其餘各包一律從這裡複製。

用法：
  # 同步到指定的 skill 根目錄（會寫進 <目錄>/scripts/validate_punct.py）
  python scripts/sync_validator.py /path/dex-card-generator /path/knowledge-card-generator

  # 不傳目標：自動探索「上層目錄底下、已經有 scripts/validate_punct.py」的同類包
  python scripts/sync_validator.py

  # 只檢查不寫入：列出哪些包與正本不一致（有漂移退出碼 1，可接 CI）
  python scripts/sync_validator.py --check [目標 ...]
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CANONICAL = os.path.normpath(os.path.join(HERE, "..", "assets", "validate_punct.py"))


def _md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def _target_file(skill_dir):
    """目標包的驗證器位置：<skill_dir>/scripts/validate_punct.py。"""
    return os.path.join(skill_dir, "scripts", "validate_punct.py")


def discover(start):
    """從「所有 skill 的共同上層」往下找已含 scripts/validate_punct.py 的兄弟包，排除自己。"""
    base = os.path.normpath(os.path.join(start, "..", ".."))  # v1.1 修正：start 是 scripts 目錄，需上兩層才到各 skill 的共同上層
    found = []
    for root, dirs, files in os.walk(base):
        depth = root[len(base):].count(os.sep)
        if depth > 3:
            dirs[:] = []
            continue
        if os.path.basename(root) == "scripts" and "validate_punct.py" in files:
            cand = os.path.normpath(os.path.join(root, "validate_punct.py"))
            if cand != CANONICAL:
                found.append(os.path.dirname(root))  # skill 根目錄
    return sorted(set(found))


def main(argv):
    if not os.path.exists(CANONICAL):
        print(f"找不到正本：{CANONICAL}")
        return 2

    check_only = "--check" in argv
    targets = [a for a in argv if a != "--check"]

    if not targets:
        targets = discover(HERE)
        if not targets:
            print("沒有指定目標，也沒自動探索到任何含 scripts/validate_punct.py 的包。")
            print("請改用：python scripts/sync_validator.py <skill 根目錄> ...")
            return 2
        print(f"自動探索到 {len(targets)} 個包：")
        for t in targets:
            print(f"  · {t}")

    canon_hash = _md5(CANONICAL)
    drift = 0
    synced = 0
    for skill_dir in targets:
        dst = _target_file(skill_dir)
        name = os.path.basename(os.path.normpath(skill_dir))
        if os.path.exists(dst) and _md5(dst) == canon_hash:
            print(f"  [一致] {name}")
            continue
        drift += 1
        if check_only:
            state = "缺少" if not os.path.exists(dst) else "不一致"
            print(f"  [漂移] {name}（{state}）")
        else:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(CANONICAL, dst)
            synced += 1
            print(f"  [已同步] {name}")

    print()
    if check_only:
        if drift:
            print(f"結果：{drift} 個包與正本不一致（執行不帶 --check 即可同步）。")
            return 1
        print("結果：全部與正本一致。")
        return 0
    print(f"結果：同步 {synced} 個包，其餘已一致。正本雜湊 {canon_hash[:8]}。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
