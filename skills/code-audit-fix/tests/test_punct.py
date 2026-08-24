#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
回歸測試：validate_punct.py 對 code-audit-fix/SKILL.md 的把關能力。

依房規二「驗證器自稽」：不只確認正式產出過關（正向），
還要確認驗證器餵到故意錯的內容時真的會紅燈（負向），
避免落入「自我循環」「缺輸入放行」「驗到別的東西」這三種假閘門。

用法：
    python3 tests/test_punct.py
或搭配 pytest：
    pytest tests/test_punct.py
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(ROOT, "scripts", "validate_punct.py")
SKILL_MD = os.path.join(ROOT, "SKILL.md")


def run_validator(path):
    """呼叫驗證器，回傳 (退出碼, 標準輸出)。"""
    result = subprocess.run(
        [sys.executable, VALIDATOR, path],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout


def test_skill_md_passes():
    """正向：目前的 SKILL.md 正文必須通過全形標點驗證，退出碼為 0。"""
    code, out = run_validator(SKILL_MD)
    assert code == 0, f"SKILL.md 未通過全形標點驗證：\n{out}"


def test_validator_catches_half_width_punct_in_chinese():
    """負向：中文夾半形標點時，驗證器必須紅燈（退出碼非 0），否則是假閘門。"""
    bad_content = "---\nname: fake\ndescription: 測試用\n---\n\n這是一段中文,裡面故意夾了半形逗號。\n"
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(bad_content)
        temp_path = f.name
    try:
        code, out = run_validator(temp_path)
        assert code != 0, "驗證器對半形標點夾中文的內容沒有紅燈，是假閘門"
        assert "半形" in out
    finally:
        os.remove(temp_path)


def test_validator_catches_dash():
    """負向：出現破折號時，驗證器必須紅燈，否則是假閘門。"""
    bad_content = "---\nname: fake\ndescription: 測試用\n---\n\n這是一段話，中間用破折號—做斷句。\n"
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(bad_content)
        temp_path = f.name
    try:
        code, out = run_validator(temp_path)
        assert code != 0, "驗證器對破折號沒有紅燈，是假閘門"
        assert "破折號" in out
    finally:
        os.remove(temp_path)


def test_frontmatter_only_has_name_and_description():
    """凍結契約：frontmatter 只能有 name 與 description 兩個欄位。"""
    with open(SKILL_MD, encoding="utf-8") as f:
        content = f.read()
    assert content.startswith("---\n"), "檔案第一行必須是 ---（前面不可有空白或說明文字）"
    end = content.index("\n---", 4)
    frontmatter = content[4:end]
    keys = [
        line.split(":", 1)[0].strip()
        for line in frontmatter.splitlines()
        if line and not line.startswith(" ") and ":" in line
    ]
    assert keys == ["name", "description"], f"frontmatter 欄位不符預期：{keys}"


def _run_all():
    tests = [
        test_skill_md_passes,
        test_validator_catches_half_width_punct_in_chinese,
        test_validator_catches_dash,
        test_frontmatter_only_has_name_and_description,
    ]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"✅ {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"❌ {t.__name__}：{e}")
    if failed:
        print(f"\n共 {failed} 項未通過。")
        return 1
    print(f"\n全部 {len(tests)} 項通過。")
    return 0


if __name__ == "__main__":
    sys.exit(_run_all())
