# 凍結紀錄

## v1.0.0 ｜ 2026-08-04 ｜ 已鎖定

- **鎖了什麼**：九節交接骨架的章節標題文字與順序。
  1. 〇、啟動指令（給下一個 session）
  2. 一、任務身分卡
  3. 二、核心脈絡
  4. 三、工作流現況
  5. 四、工作紀律與規範
  6. 五、邊界與禁區
  7. 六、凍結契約與關鍵閘門
  8. 七、已確認的對話決議
  9. 八、未決事項與風險
- **一併鎖定**：
  - 事實分級標記集合：`[CONFIRMED]`、`[INFERRED]`、`[UNVERIFIED]`、`[BLOCKED]`、`[SUPERSEDED]`。
  - 遮蔽標記：`[REDACTED]`。
  - 第〇節三條機器閘門：內文去空白後 200 字上限、編號條目至少 3 條、第一個編號條目同時含「讀」與「再回應」。
  - 第八節必填欄位：脈絡涵蓋。
  - web 模式交付形式：對話內單一可整塊複製的 fenced code block，內含三反引號時外層用四反引號。
- **定版檔**：`scripts/handoff_contract.py`（權威來源）、`references/output-contract.md`、`schemas/handoff.schema.json`。
- **定版雜湊**：`7f29cd5d626067c2`（sha256 前 16 碼，對象為章節清單的 JSON 序列化，`ensure_ascii=False`）。
- **守門方式**：`scripts/handoff_contract.py` 的 `assert_frozen()`；`scripts/validate_skill.py` 比對文件、schema 與程式常數三處一致；`tests/test_structure.py` 以斷言回歸。

要調整章節結構或標記集合，一律另開新版（major），舊骨架原封保留，不動本版。
