#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把共用正本（assets/manifest.json 所列）一鍵同步到各 skill 包。

避免「每包各放一份、其中一份漏改」的分歧（這正是禁破折號漏網事件的成因）。
正本只有一處：本 skill 的 assets/。其餘各包一律從這裡複製。
v1.2 起改為依 manifest 同步多個正本（validate_punct、bootstrap...），
新增共用資產只要在 manifest 加一筆。

用法：
  # 同步到指定的 skill 根目錄
  python scripts/sync_validator.py /path/dex-card-generator /path/knowledge-card-generator

  # 不傳目標：自動探索上層目錄底下、已含 scripts/validate_punct.py 的同類包
  #（探索最深到上層目錄之下三層）
  python scripts/sync_validator.py

  # 只檢查不寫入：列出哪些包與正本不一致（有漂移退出碼 1，可接 CI）
  python scripts/sync_validator.py --check [目標 ...]
"""
import hashlib
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
MANIFEST = os.path.join(ROOT, "assets", "manifest.json")


def _md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        data = json.load(f)
    items = []
    for a in data["assets"]:
        canonical = os.path.normpath(os.path.join(ROOT, a["canonical"]))
        if not os.path.exists(canonical):
            print(f"找不到正本：{canonical}")
            sys.exit(2)
        items.append((canonical, a["target"]))
    return items


def discover():
    """從上層目錄往下找已含 scripts/validate_punct.py 的包（最深三層），排除自己。"""
    base = os.path.normpath(os.path.join(ROOT, ".."))
    found = []
    for root, dirs, files in os.walk(base):
        depth = root[len(base):].count(os.sep)
        if depth > 3:
            dirs[:] = []
            continue
        if os.path.basename(root) == "scripts" and "validate_punct.py" in files:
            skill_dir = os.path.dirname(root)
            if os.path.normpath(skill_dir) != ROOT:
                found.append(skill_dir)
    return sorted(set(found))


def main(argv):
    items = load_manifest()
    check_only = "--check" in argv
    targets = [a for a in argv if a != "--check"]

    if not targets:
        targets = discover()
        if not targets:
            print("沒有指定目標，也沒自動探索到任何含 scripts/validate_punct.py 的包。")
            print("請改用：python scripts/sync_validator.py <skill 根目錄> ...")
            return 2
        print(f"自動探索到 {len(targets)} 個包：")
        for t in targets:
            print(f"  · {t}")

    drift = 0
    synced = 0
    for skill_dir in targets:
        name = os.path.basename(os.path.normpath(skill_dir))
        for canonical, target_rel in items:
            dst = os.path.join(skill_dir, target_rel)
            label = f"{name}/{target_rel}"
            if os.path.exists(dst) and _md5(dst) == _md5(canonical):
                print(f"  [一致] {label}")
                continue
            drift += 1
            if check_only:
                state = "缺少" if not os.path.exists(dst) else "不一致"
                print(f"  [漂移] {label}（{state}）")
            else:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(canonical, dst)
                synced += 1
                print(f"  [已同步] {label}")

    print()
    if check_only:
        if drift:
            print(f"結果：{drift} 個檔案與正本不一致（執行不帶 --check 即可同步）。")
            return 1
        print("結果：全部與正本一致。")
        return 0
    print(f"結果：同步 {synced} 個檔案，其餘已一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
