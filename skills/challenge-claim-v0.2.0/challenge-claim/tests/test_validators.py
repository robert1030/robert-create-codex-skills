#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_validators.py — challenge-claim v0.2.0 兩支驗證器的回歸測試。

pytest 可收集（函式以 test_ 開頭），也支援 `python3 tests/test_validators.py` 直跑。

涵蓋：
  1. validate_punct.py：半形標點夾中文、破折號兩類負向測試，加程式碼區塊不誤擋的正向測試。
  2. check_output_contract.py：缺元件、順序錯誤、七標題齊全但內容空殼、判定詞不合法、
     confirmed 缺可觀察訊號、反例缺影響說明、空泛挑錯、自行補證據、來源不可追溯、
     空檔案、檔案不存在共十一類負向測試，加一個完整正向測試。

其中「七標題齊全但內容空殼」為本包的關鍵負向案例：上一代驗證器只比對標題存在與否，
這種產出會被誤判為通過，因此本案例必須紅燈，否則視為驗證器未完成。
"""
import os
import sys
import io
import contextlib
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
sys.path.insert(0, SCRIPTS)

import validate_punct  # noqa: E402
import check_output_contract as coc  # noqa: E402


# ---------------------------------------------------------------------------
# 共用工具
# ---------------------------------------------------------------------------
def _run(func, content: str) -> int:
    with tempfile.TemporaryDirectory() as tmp:
        fp = os.path.join(tmp, "case.md")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = func(fp)
        return code


def _run_punct(content: str) -> int:
    return _run(validate_punct.check, content)


def _run_contract(content: str) -> int:
    return _run(coc.run, content)


# ---------------------------------------------------------------------------
# 產出樣本：完整合格產出（正向基準），其餘負向案例由此變形而來
# ---------------------------------------------------------------------------
GOOD = """# 論點挑戰分析

## 核心主張
C1：導入遠距辦公制度可提升員工留任率，應全公司推行。主張類型為因果加規範建議。

## 論證結構
E1 離職率下降三成　→　R1 遠距辦公改善留任　→　IP1 其他條件未同時變動　→　C1 應全面推行。
本節依據類型：邏輯分析。

## 前提與證據檢查
P1 顯性前提：統計期間內離職定義前後一致，狀態為待查證。
IP1 隱含前提：同期間沒有其他人事政策變動，狀態為未驗證，重要性高。
E1 證據等級 E1，限制為單一組織單一年度，無對照組。依據類型：使用者提供資訊。

## 反方壓力測試
X1 邊界反例：同業在相同期間離職率普遍下降。影響：削弱把降幅歸因於遠距制度的推論。
X2 機制反例：同年度另有調薪與獎金調整。影響：提供同樣能解釋資料的替代機制。

## 偏誤與缺口
問題一：事後歸因，判定 confirmed。可觀察訊號：原文以導入時點先於離職率下降作為因果依據，未處理同期變因。
問題二：過度外推，判定 possible。尚缺跨部門與跨年度資料，無法定性。

## 校準結論
判定：部分支持
信心：中低
限制條件：僅適用於原始資料涵蓋的單一組織與單一年度，不宜外推至全公司。

## 驗證計畫
1. 取得同業同期離職率作為基準情境。
2. 分部門拆解離職率，檢查是否集中於特定單位。
3. 取得同期薪酬政策異動紀錄，區分兩個變因。
停止條件：若同業基準顯示相同降幅，即判定原主張不成立，停止補證。
"""


# ---------------------------------------------------------------------------
# validate_punct.py
# ---------------------------------------------------------------------------
def test_punct_half_width_comma_in_chinese_fails():
    assert _run_punct("這是一段測試,裡面混了半形逗號。") != 0


def test_punct_dash_fails():
    assert _run_punct("這裡用了破折號——來斷句，這是違規的。") != 0


def test_punct_full_width_passes():
    assert _run_punct("這是一段完全使用全形標點的正常文字，沒有任何問題。") == 0


def test_punct_code_block_half_width_ok():
    ok = "說明文字都是全形。\n```python\nprint(1, 2)\n```\n"
    assert _run_punct(ok) == 0


# ---------------------------------------------------------------------------
# check_output_contract.py：正向
# ---------------------------------------------------------------------------
def test_contract_good_case_passes():
    assert _run_contract(GOOD) == 0


# ---------------------------------------------------------------------------
# check_output_contract.py：負向
# ---------------------------------------------------------------------------
def test_contract_missing_section_fails():
    bad = GOOD.split("## 驗證計畫")[0]
    assert _run_contract(bad) != 0


def test_contract_wrong_order_fails():
    body = GOOD
    calib = body[body.index("## 校準結論"):body.index("## 驗證計畫")]
    body = body.replace(calib, "")
    body = body.replace("## 反方壓力測試", calib + "## 反方壓力測試")
    assert _run_contract(body) != 0


def test_contract_hollow_shell_fails():
    """關鍵案例：七元件標題齊全，內容全是佔位字樣，必須紅燈。"""
    hollow = """## 核心主張
略

## 論證結構
略

## 前提與證據檢查
無

## 反方壓力測試
略

## 偏誤與缺口
無

## 校準結論
判定：部分支持

## 驗證計畫
略
"""
    assert _run_contract(hollow) != 0


def test_contract_invalid_verdict_fails():
    bad = GOOD.replace("判定：部分支持", "判定：大致同意")
    assert _run_contract(bad) != 0


def test_contract_confirmed_without_signal_fails():
    bad = GOOD.replace(
        "可觀察訊號：原文以導入時點先於離職率下降作為因果依據，未處理同期變因。",
        "這一段就是典型的事後歸因。",
    )
    assert _run_contract(bad) != 0


def test_contract_counterexample_without_impact_fails():
    bad = GOOD.replace(
        "影響：削弱把降幅歸因於遠距制度的推論。", "這件事值得注意。"
    ).replace("影響：提供同樣能解釋資料的替代機制。", "這件事也值得注意。")
    assert _run_contract(bad) != 0


def test_contract_vague_attack_fails():
    bad = GOOD.replace(
        "問題二：過度外推，判定 possible。尚缺跨部門與跨年度資料，無法定性。",
        "問題二：這份報告看起來就是有問題，整體邏輯很薄弱，建議重寫。",
    )
    assert _run_contract(bad) != 0


def test_contract_fabricated_evidence_fails():
    bad = GOOD.replace(
        "E1 證據等級 E1，限制為單一組織單一年度，無對照組。依據類型：使用者提供資訊。",
        "E1 證據不足，推測應為樣本數過少所致，估計約在五十人左右。",
    )
    assert _run_contract(bad) != 0


def test_contract_untraceable_source_fails():
    bad = GOOD.replace(
        "X1 邊界反例：同業在相同期間離職率普遍下降。影響：削弱把降幅歸因於遠距制度的推論。",
        "X1 邊界反例：有研究指出同業離職率普遍下降。影響：削弱原推論。",
    )
    assert _run_contract(bad) != 0


def test_contract_severity_only_retention_fails():
    bad = GOOD.replace(
        "X2 機制反例：同年度另有調薪與獎金調整。影響：提供同樣能解釋資料的替代機制。",
        "X2 雖然查無明確反例，但因為影響重大仍保留此條。影響：待確認。",
    )
    assert _run_contract(bad) != 0


def test_contract_missing_confidence_fails():
    bad = GOOD.replace("信心：中低\n", "")
    assert _run_contract(bad) != 0


def test_contract_empty_file_fails_closed():
    assert _run_contract("   \n\n") != 0


def test_contract_missing_file_fails_closed():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = coc.run("/tmp/this-path-does-not-exist-xyz.md")
    assert code != 0


def test_contract_self_test_passes():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = coc.self_test()
    assert code == 0


# ---------------------------------------------------------------------------
# 直跑進入點
# ---------------------------------------------------------------------------
def _main() -> int:
    tests = [(n, f) for n, f in sorted(globals().items())
             if n.startswith("test_") and callable(f)]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"[PASS] {name}")
            passed += 1
        except AssertionError:
            print(f"[FAIL] {name}")
            failed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"[ERROR] {name}：{exc}")
            failed += 1
    print(f"\n{passed} 通過 / {failed} 失敗（共 {len(tests)} 項）")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(_main())
