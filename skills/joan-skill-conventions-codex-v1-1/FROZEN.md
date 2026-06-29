# 凍結紀錄

## Codex v1.1 ｜ 2026-06-29 ｜ 已鎖定

- 鎖定觸發契約：新建、檢視、升級、重構 skill 時，必須立即讀取本 skill，並同步設計、建立或更新驗證器與回歸測試。
- 鎖定最低測試契約：每支 skill 至少需要 `scripts/validate_punct.py` 與 `tests/test_*.py`，或在缺少原始碼時交付 `tests/test_contract.py` 與 `tests/test_validation_inventory.py`。
- 鎖定授權式相依契約：未取得授權不得執行 pip、npm 或瀏覽器資產安裝。
- 後續若要放寬以上契約，必須另開新版，不得就地修改本版。
