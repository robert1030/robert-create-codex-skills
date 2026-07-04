# LESSONS（教訓帳本）

格式與精簡規則見 SKILL.md「維護協議」第三、四節。能寫成測試的教訓一律寫成測試，這裡只留未固化與無法測試化的。

## 2026-07-04｜v1.0 打包時帶到過期驗證器
- 現象：`tests/test_validate_punct.py` 七項紅燈，驗證器自掃 exit=1（自己的說明文字含破折號）。
- 根因：打包時複製了上游 v1 驗證器，沒對照上游 v2.1 正本，也沒放回歸測試守門。
- 對策：換上 v2.1 正本、補 `tests/test_validate_punct.py`、修 `sync_validator.py` 探索路徑。
- 已固化：tests/test_validate_punct.py
