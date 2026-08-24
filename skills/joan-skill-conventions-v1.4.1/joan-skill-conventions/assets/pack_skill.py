#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pack_skill.py：把一個 skill 資料夾打包成 Windows 與 macOS 都能順利解開的 zip。

用法：
    python3 pack_skill.py <skill_dir> [-o out.zip] [--max-path 200]
    python3 pack_skill.py <skill_dir> --check-only     # 只檢查不打包
    python3 pack_skill.py <existing.zip> --audit       # 稽核既有 zip

設計原則（對應 Joan skill 房規二：驗證即閘門，絕不靠肉眼）：
    打包「之前」先全量檢查路徑合法性，任何一條不過就不產出檔案。
    打包「之後」重新開檔回讀，比對名單與 CRC，確認沒有靜默漏檔。

退出碼：0 全通過；1 有硬錯（不產出 zip）。
"""

import argparse
import os
import sys
import zipfile

# Windows 檔名非法字元（冒號、問號、星號等在 macOS 合法，在 Windows 會解壓縮失敗）
ILLEGAL_CHARS = set('<>:"|?*') | {chr(c) for c in range(32)}

# Windows 保留裝置名稱，含副檔名也一樣不合法（例如 con.txt）
RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL"} | {
    f"{p}{i}" for p in ("COM", "LPT") for i in range(1, 10)
}

# 一律排除的垃圾檔（macOS 與 Windows 各自的殘留物）
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}
EXCLUDE_DIRS = {"__pycache__", ".git", ".idea", ".vscode", "node_modules", ".pytest_cache"}
EXCLUDE_SUFFIX = {".pyc", ".pyo", ".swp", ".orig", ".rej"}


def collect(root):
    """走訪資料夾，回傳 [(絕對路徑, zip 內相對路徑)]，並過濾垃圾檔。"""
    items = []
    root = os.path.abspath(root)
    base = os.path.basename(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in EXCLUDE_DIRS and d not in EXCLUDE_NAMES)
        for fn in sorted(filenames):
            if fn in EXCLUDE_NAMES:
                continue
            if os.path.splitext(fn)[1] in EXCLUDE_SUFFIX:
                continue
            full = os.path.join(dirpath, fn)
            if os.path.islink(full):
                continue  # 符號連結在 Windows 解不開，一律略過
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            items.append((full, f"{base}/{rel}"))
    return items


def check(items, max_path):
    """回傳錯誤訊息清單，空清單代表全數通過。"""
    errors = []
    seen_lower = {}

    for _, arc in items:
        # 一、全 ASCII（skill 上傳器硬限制，非 ASCII 路徑整包退件）
        try:
            arc.encode("ascii")
        except UnicodeEncodeError:
            errors.append(f"[非 ASCII 路徑] {arc}")

        # 二、路徑總長度（Windows 傳統上限 260，留餘裕給使用者的解壓縮目錄）
        if len(arc) > max_path:
            errors.append(f"[路徑過長 {len(arc)} 字元] {arc}")

        # 三、絕對路徑與跳脫路徑
        if arc.startswith("/") or ".." in arc.split("/"):
            errors.append(f"[不安全路徑] {arc}")

        for seg in arc.split("/"):
            # 四、非法字元
            bad = sorted(set(seg) & ILLEGAL_CHARS)
            if bad:
                shown = " ".join(repr(c) for c in bad)
                errors.append(f"[Windows 非法字元 {shown}] {arc}")

            # 五、保留裝置名稱
            if seg.split(".")[0].upper() in RESERVED_NAMES:
                errors.append(f"[Windows 保留名稱 {seg}] {arc}")

            # 六、結尾句點或空格（Windows 無法建立這種檔名）
            if seg != seg.rstrip(". "):
                errors.append(f"[結尾為句點或空格 {seg!r}] {arc}")

        # 七、大小寫碰撞（Windows 不分大小寫，會少解出檔案）
        low = arc.lower()
        if low in seen_lower and seen_lower[low] != arc:
            errors.append(f"[大小寫碰撞] {seen_lower[low]} 與 {arc}")
        seen_lower[low] = arc

    return errors


def pack(items, out_path):
    """只用 Deflate，不加密、不走 zip64 以外的特殊方法，確保內建解壓縮吃得下。"""
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6) as zf:
        for full, arc in items:
            info = zipfile.ZipInfo.from_file(full, arcname=arc)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 0          # 宣告為 FAT／Windows，避免權限位元干擾
            info.external_attr = 0o644 << 16
            with open(full, "rb") as fh:
                zf.writestr(info, fh.read())


def verify(out_path, items):
    """打包後回讀自檢：名單一致、CRC 正確、沒有目錄項殘留。"""
    errors = []
    expected = {arc for _, arc in items}
    with zipfile.ZipFile(out_path) as zf:
        broken = zf.testzip()
        if broken:
            errors.append(f"[CRC 損毀] {broken}")
        actual = set(zf.namelist())
        for miss in sorted(expected - actual):
            errors.append(f"[漏檔] {miss}")
        for extra in sorted(actual - expected):
            errors.append(f"[多餘項目] {extra}")
        for info in zf.infolist():
            if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                errors.append(f"[不相容壓縮法] {info.filename}")
            if info.flag_bits & 0x1:
                errors.append(f"[含加密項目] {info.filename}")
    return errors


def audit(zip_path, max_path):
    """稽核既有 zip，不重新打包。"""
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
    items = [(None, n) for n in names if not n.endswith("/")]
    errors = check(items, max_path)
    for n in names:
        if n.startswith("__MACOSX/") or n.endswith("/.DS_Store"):
            errors.append(f"[macOS 殘留物] {n}")
    return errors


def main():
    ap = argparse.ArgumentParser(description="跨平台安全的 skill 打包器")
    ap.add_argument("target", help="skill 資料夾，或搭配 --audit 時給既有 zip")
    ap.add_argument("-o", "--output", default=None, help="輸出 zip 路徑")
    ap.add_argument("--max-path", type=int, default=200, help="zip 內路徑長度上限")
    ap.add_argument("--check-only", action="store_true", help="只檢查不打包")
    ap.add_argument("--audit", action="store_true", help="稽核既有 zip")
    args = ap.parse_args()

    if args.audit:
        errs = audit(args.target, args.max_path)
        if errs:
            print(f"❌ 稽核未通過，共 {len(errs)} 項：")
            for e in errs:
                print("   " + e)
            return 1
        print("✅ 稽核通過，此 zip 在 Windows 與 macOS 皆可正常解壓縮。")
        return 0

    root = os.path.abspath(args.target.rstrip("/"))
    if not os.path.isdir(root):
        print(f"❌ 找不到資料夾：{root}")
        return 1

    items = collect(root)
    if not items:
        print("❌ 資料夾內沒有可打包的檔案。")
        return 1

    errs = check(items, args.max_path)
    if errs:
        print(f"❌ 路徑檢查未通過，共 {len(errs)} 項，未產出 zip：")
        for e in errs:
            print("   " + e)
        return 1

    if args.check_only:
        print(f"✅ 路徑檢查通過，共 {len(items)} 個檔案。")
        return 0

    out = args.output or (root + ".zip")
    pack(items, out)

    errs = verify(out, items)
    if errs:
        os.remove(out)
        print(f"❌ 回讀自檢未通過，共 {len(errs)} 項，已刪除瑕疵 zip：")
        for e in errs:
            print("   " + e)
        return 1

    size = os.path.getsize(out) / 1024
    print(f"✅ 打包完成：{out}")
    print(f"   檔案數 {len(items)}，大小 {size:.1f} KB，全 ASCII 路徑，Deflate 未加密。")
    print("   已通過回讀自檢，Windows 內建解壓縮與 macOS 皆可正常展開。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
