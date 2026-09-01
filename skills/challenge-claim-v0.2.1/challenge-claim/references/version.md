# 版本沿革

SKILL.md 只保留最新版的版號戳記，歷史版本一律記在本檔，遵循最小揭露：只記錄「哪一版改了什麼、影響哪些檔案」，不保留舊版全文。

## v0.2.1｜2026-09-01

更名版。只動名稱與版號，方法論、輸出契約、三條鐵則與兩支驗證器的邏輯完全未動。

**變更**

- 技能名稱由 `critical-argument-challenger` 改為 `challenge-claim`，資料夾名與交付 zip 檔名一併更名。
- `SKILL.md` 的 frontmatter `version` 與 `metadata.version` 由 0.2.0 提升為 0.2.1，版號戳記改為只載本版資訊。
- 兩支 Python 檔的 docstring 標頭同步更新版號。

**名稱字串替換對帳**

改名共替換 9 處名稱字串，分布於 7 個檔案：

| 檔案 | 處數 | 位置 |
|---|---|---|
| `SKILL.md` | 3 | frontmatter `name`、`metadata.domain`、H1 標題 |
| `references/argument-analysis-framework.md` | 1 | 第 3 行的技能名引用 |
| `references/bias-and-fallacy-catalog.md` | 1 | 第 3 行的技能名引用 |
| `references/critical-thinking-question-bank.md` | 1 | 第 3 行的技能名引用 |
| `references/evidence-calibration-and-output-schema.md` | 1 | 第 3 行的技能名引用 |
| `scripts/check_output_contract.py` | 1 | docstring 標頭 |
| `tests/test_validators.py` | 1 | docstring 標頭 |

**與 v0.2.0 的累計關係**

四份既有 reference 的字串級替換為累計 14 處：v0.2.0 的 10 處（見下節逐條替換清單），加上本版的 4 處名稱替換。下節「四份既有 reference 共 10 處字串級替換」一句的計數範圍僅限 v0.2.0，屬於已凍結的版本紀錄，本版不予變更。

**已知限制**

- 本版與評測用的另一支同名 skill 撞名。若兩者需並存於同一個 skills 目錄，其中一支必須再更名。

## v0.2.0｜2026-08-31

契約收斂與防造假版。

**新增**

- 輸出契約優先序宣告：SKILL.md 的輸出契約為唯一交付格式，`references/` 內的格式一律降級為內部分析工作表。
- 三條防造假鐵則：禁止為呈現批判性而刻意挑錯、禁止自行補上缺失證據、禁止杜撰來源。
- `scripts/check_output_contract.py`：輸出契約驗證器，含九案例內建負向自檢。
- `scripts/validate_punct.py`：全形標點與禁破折號驗證器，複製自 `joan-skill-conventions` 正本，不另開分歧版。
- `examples/bad-example.md`：違規寫法對照檔，逐條標註違反哪一條鐵則。
- `tests/test_validators.py`：兩支驗證器的正負向回歸測試，共十九項。
- SKILL.md 新增「能力邊界」與「交付前驗證清單」兩節。

**變更**

- 四份 reference 的引用句由同一句泛用敘述改為四句互不相同的條件式路由。
- 四份 reference 中自稱交付格式的段落共 5 處更名並加註以 SKILL.md 為準，避免與交付契約撞名：framework 兩處（第 473、531 行）、bias 一處（第 82 行）、question-bank 一處（第 146 行）、evidence 一處（第 417 行）。其中只有 framework 第 473 行原文寫「標準輸出契約」、evidence 第 417 行原文寫「最終輸出契約」；`critical-thinking-question-bank.md` 與 `bias-and-fallacy-catalog.md` 原文並未出現這兩個字樣，更名的分別是「輸出分層問題」與「論證分析記錄格式」兩個小節標題。
- 另有 5 處屬於全形標點閘門修正，與自稱更名無關：framework 第 715 行、bias 第 1221 行的英文文獻標題改以反引號包覆，question-bank 第 915 行與 evidence 第 176、351 行的破折號改為中文寫法。
- 步驟 2 明確要求先寫最強合理重述；步驟 3 明確要求每條反例寫出對原論證的影響。
- frontmatter 的 `version` 由 0.1.0 提升為 0.2.0，`metadata` 移除與 description 重複的欄位。

**移除**

- `references/quality_checklist.md`：內容為建置期工具鏈的自報結果，對執行期沒有約束力，且含建置機器的本機路徑。其角色由 `tests/test_validators.py` 與兩支驗證器取代。

**變更範圍對帳**

| 檔案 | 變更方式 | 變更行數 |
|---|---|---|
| `SKILL.md` | 改寫 | 全檔 |
| `references/argument-analysis-framework.md` | 字串級替換 | 3 |
| `references/bias-and-fallacy-catalog.md` | 字串級替換 | 2 |
| `references/critical-thinking-question-bank.md` | 字串級替換 | 2 |
| `references/evidence-calibration-and-output-schema.md` | 字串級替換 | 3 |
| `references/quality_checklist.md` | 刪除 | 全檔 |

**逐條替換清單**

四份既有 reference 共 10 處字串級替換，全數列於下表，行號為 v0.1.0 原檔行號。

| 檔案 | 行號 | 原字串 | 新字串 | 變更類型 |
|---|---|---|---|---|
| `references/argument-analysis-framework.md` | 473、475 | `## 10. 標準輸出契約` 與 `完整分析使用下列順序：` | `## 10. 分析工作表格式` 與優先序引言（全文見註一） | 自稱更名 |
| `references/argument-analysis-framework.md` | 531 | `## 11. 短版輸出格式` | `## 11. 短版分析工作表` | 自稱更名 |
| `references/argument-analysis-framework.md` | 715 | 以書名號包覆的英文文獻標題 `Missing Premise exacerbates Overthinking: Are Reasoning Models losing Critical Thinking Skill?` | 同一標題改以反引號包覆 | 標點修正 |
| `references/bias-and-fallacy-catalog.md` | 82 | `## 二、論證分析記錄格式` | `## 二、論證分析工作表格式（內部使用，交付格式依 SKILL.md 的輸出契約）` | 自稱更名 |
| `references/bias-and-fallacy-catalog.md` | 1221 | 以書名號包覆的英文文獻標題 `Missing Premise exacerbates Overthinking: Are Reasoning Models losing Critical Thinking Skill?` | 同一標題改以反引號包覆 | 標點修正 |
| `references/critical-thinking-question-bank.md` | 146 | `### 步驟五：輸出分層問題` | `### 步驟五：整理分層問題（內部工作表，交付格式依 SKILL.md 的輸出契約）` | 自稱更名 |
| `references/critical-thinking-question-bank.md` | 915 | `「挑戰—修正」` | `「挑戰與修正」` | 標點修正 |
| `references/evidence-calibration-and-output-schema.md` | 417、419 | `## 9. 最終輸出契約` 與 `最終回覆依下列固定順序：` | `## 9. 分析工作表格式` 與優先序引言（全文見註一） | 自稱更名 |
| `references/evidence-calibration-and-output-schema.md` | 176 | `E1–E2` | `E1 至 E2` | 標點修正 |
| `references/evidence-calibration-and-output-schema.md` | 351 | `E0–E3` | `E0 至 E3` | 標點修正 |

註一：framework 第 475 行與 evidence 第 419 行的引言，兩處替換為同一句：

> 本節為內部分析工作表，不是交付格式。交付一律依 SKILL.md 的輸出契約七元件，兩者衝突時以 SKILL.md 為準。工作表依下列順序整理：

小計：自稱更名 5 處（framework 2、bias 1、question-bank 1、evidence 1），標點修正 5 處（framework 1、bias 1、question-bank 1、evidence 2），合計 10 處，與上表變更行數欄逐檔相符。

## v0.1.0

首發版，由 SkillNow 工具鏈產出。內容為四份 reference 的方法論本體：論證分析框架、偏誤與謬誤判準目錄、批判思考問題庫、證據校準與輸出格式，以及 SKILL.md 的四步工作流程與觸發邊界。

已知限制（v0.2.0 已處理）：SKILL.md 與四份 reference 各自宣告了彼此不同的最終輸出格式，未指定優先序；四份 reference 使用同一句引用敘述，缺少讀取條件；全部品質保證依賴人工檢查清單，沒有可執行閘門。
