# itest-help dist 清單

產生日期：2026-08-09（v1.3.5 第三批就地覆蓋，前次為 2026-08-06）

## v1.3.5（現行版，減量與預算契約，分支限定詞可見度）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.5-runtime.zip` | 49 | 2.23 MB | `9E72798DB8EEE1E2DE319D9038E0695AB2AFD5492B25CC6F7BC1D91B645E48EE` |
| `itest-help-v1.3.5-chatweb.zip` | 48 | 1.19 MB | `1BD4ACF1D78913959AC832C3F65901CB94D7E47F1D4F77587A5E3305FC74EADA` |
| `itest-help-v1.3.5-full.zip` | 9,378 | 18.76 MB | `424A9D4839D4CAFCA4A48A6AF87712C90582FDC35667DAB910638019EED39939` |

上表為第三批加統計更正後的雜湊。同為 2026-08-09 的前一次建置雜湊為 `32E41951…`、`058386FA…`、`3417FF3A…`，2026-08-06 第二批為 `952CFD86…`、`AF8DF3F1…`、`DFD04FAA…`，兩者的 zip 都已被覆蓋，不再存在。

## v1.3.4（片段自報）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.4-runtime.zip` | 49 | 2.22 MB | `2C8AB9B0056F826133719DCA61CEA5B91C6F4865DE36079BDCCA87D7CE79A564` |
| `itest-help-v1.3.4-chatweb.zip` | 48 | 1.18 MB | `16BA80677CF7362B7F9B8F7CF2D628CB06E92FDD8C9F0A4B523C392F828B2E4D` |
| `itest-help-v1.3.4-full.zip` | 9,378 | 18.75 MB | `AD81F497E9A450E35121ED9AE6EE139725C2ADAD0727C405F28D64BDB6876CCB` |

## v1.3.3（兩層執行模型）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.3-runtime.zip` | 49 | 2.22 MB | `24B1C1F434D081C11104E96977E0D79603AACA573D0567479F9D8535FAEAEA3C` |
| `itest-help-v1.3.3-chatweb.zip` | 48 | 1.18 MB | `F72DF4CAA02CBFE89D15323FC4CB4FEDF20FF2A705E18ED99BC94CF88A6CC2E5` |
| `itest-help-v1.3.3-full.zip` | 9,378 | 18.75 MB | `ED276E6DDD464D712C3E54CD1F3427A368F4D4DA4B9930C2ABF804E8BA9143AD` |

## v1.3.2（安全修補）

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.2-runtime.zip` | 49 | 2.19 MB | `4D8C656A31418F6F32D338C5FDDDC1010970C02BEF86E1AD9BD951B795CAC11C` |
| `itest-help-v1.3.2-chatweb.zip` | 48 | 1.16 MB | `7C5052E7FBE5C1F60B4D54D4FE6C303E43A2FBFC2910A0D9FD8F466B8D44D506` |
| `itest-help-v1.3.2-full.zip` | 9,378 | 18.60 MB | `E562C6810E26D46AD3D08751ED3C022035E407D5879427F129CBFC18DDA7BF4C` |

## v1.3.1

| 檔案 | 檔案數 | 大小 | SHA-256 |
| --- | ---: | ---: | --- |
| `itest-help-v1.3.1-runtime.zip` | 49 | 2.14 MB | `A28792CD48EA77795107389751064C37778B6DF463A5EB42CEEBA77056A25753` |
| `itest-help-v1.3.1-chatweb.zip` | 48 | 1.13 MB | `4AFEACF335D4B749E74FF69DC04B0CB27BACBF3FF78D36970E5483134A0B5963` |
| `itest-help-v1.3.1-full.zip` | 9,378 | 19.60 MB | `169562390CD68C7789758D88DD33FA341270F351C1FA5FF8E3C542FCFB957626` |

安裝請用 v1.3.5。zip 內部為扁平結構，`SKILL.md` 位於壓縮檔根目錄，此結構經實測可正常載入。

**重建指令**：`python tools/build_itest_help_profiles.py skills/itest-help-v1.3.5 claude-skills/dists --source-zip work/dist/itest-help.zip`

**原始封裝**：`work/dist/itest-help.zip`（SHA-256 `6EEB3CAD7DDC63B6F89BE7B434312141375EFEBA24D0E5CB2F257F4FAAC6A344`，9,370 檔，內含 `itest-help/` 頂層資料夾），`full` profile 的 9,329 個 RAG 檔案自該檔串流產生，不可刪除。`dist/itest-help-v26.2.0.zip` 是同一份封裝的扁平版副本（SHA-256 `1E2F59DFAA638A7BA38B4E4E7E39548DEEC833F6553EFD21420C368CCE4AF20C`），經逐 member 比對，9,370 個路徑與內容雜湊與前者完全一致，整檔雜湊不同只因少了頂層資料夾。**兩者的整檔 SHA-256 不可互相套用**。RAG archive 本體為 `work/dist/itest-help_26.2.0-rag-v1.2.1.zip`（SHA-256 `309BA7AA…`），即 `source-manifest.json` 所記載者。

來源樹保留於 `skills/itest-help-v1.3.x/`，為權威副本；dist zip 可重建。

**存放位置**：`claude-skills/dists/` 放完整三個 profile；`dist/` 依既有做法只放可安裝的 `runtime` 與 `chatweb`，不放體積較大的 `full`。本檔在 `claude-skills/dists/`、`dist/` 與 repo 根目錄各有一份，內容相同。

**v1.3.3 的變更**：把 v1.3.1 的兩節紀律合併為一節「兩層執行模型」，涵蓋範圍擴至 Python 側，不涵蓋 PowerShell。未改任何 `scripts/` 程式邏輯，golden diff 零差異。詳見 `FROZEN.md` 的 v1.3.3 條目。

**v1.3.4 的變更**：`search_itest_help.py` 在回應頂層新增 `truncated_count` 與 `next_action`，讓片段結果自報並提示取完整內容的指令，指令一律用相對路徑不含家目錄。golden diff 零差異，取窗演算法未動。效果未經 A/B 驗證，詳見 `FROZEN.md` 的 v1.3.4 條目。

**v1.3.5 的變更**：分兩批。第一批是減法：壓縮重複表述並移除 `SKILL.md` 中給人看的兩節，agent 每次啟動必讀量由 16,316 降至 14,942 字元（減 8.4%）。**規則一條未刪**，41 條守門字串全數保留。新增 `test_agent_startup_context_budget_is_capped`，把必讀量上限訂為 15,500 字元，日後加規則必須先刪等量內容。第二批（同日追加，依裁決不另開版）：`search_itest_help.py` 新增排在 `results` 之前的 `result_index`，並把檢索結果的 `locators` 精簡為前 2 個代表項加 `locators_total`，完整清單仍由 `inspect_chunk.py` 提供。單次輸出 53,320 降至 24,079 位元組，前 2 KB 可辨識的結果筆數由 2/8 增至 8/8。兩批皆未改變排序與取窗，golden diff 零差異。詳見 `FROZEN.md` 的 v1.3.5 條目。

**v1.3.5 第三批的變更**（2026-08-09，依裁決同樣就地覆蓋）：起因是同一題在 Claude Chat Web 與 Codex 各失敗一次，兩者都把 Analysis Rule Wizard 的 `Custom` 分支與 `Store data in a variable or a JSON response value` 分支混寫。全庫查證顯示 `Custom Extractor` 一詞只出現 1 次，就在該頁標題，知識庫沒有記載 wizard 的分支路徑。

實際落地三件事：一是 `query` 回顯移到 `result_index` 之後，讓數百字元的貼上查詢不再把索引末幾筆推出 2 KB 預覽；二是新增 2 個檢索回歸案例（70 增至 72）與 1 項長查詢契約斷言（32 增至 33）；三是把來源文件的兩處缺陷記入 `knowledge/validation-report.md`，包含 `Extraction group number` 起算基準在兩份 26.2.0 頁面中互相矛盾（一份寫 1，一份寫 zero），以及 wizard 沒有記載分支路徑。

**曾試過但已退回**：`result_index` 加頁面 title。A/B 對照 4 輪（唯一變因是有無 title），無 title 組一對一錯，有 title 組零對一錯加一部分正確，沒有觀察到方向性效果，依事前寫下的退回條件移除。**沒有動 `SKILL.md` 與任何政策檔**，必讀量維持 14,942 字元。golden diff 零差異，三個 profile 六道閘門全綠。詳見 `FROZEN.md` 的 v1.3.5 第三批條目。

**統計更正（2026-08-09 同日追加）**：第三批初次記載的「內文含 Custom 佔 2.3%」是錯的，pattern `\bCustom\b` 大小寫敏感，漏掉全部小寫的 `custom`。正確值為 165 chunk／136 檔＝**10.5%**；「選項決定後續欄位」由 8.2% 重算為 8.5%。決定性證據（`Custom Extractor` 片語全庫只命中 1 個檔案）以不分大小寫重驗後仍成立，結論未變。同時完成知識庫覆蓋率查核：原始 Help 的 1,286 個 HTML 內容頁**全數在索引內，零遺漏**，內容量比率中位數 1.15、`topics/` 全部不低於 0.79，**無內容流失**。`FROZEN.md` 已補上所有統計的 pattern 原文，日後可重算。詳見 `FROZEN.md` 的 v1.3.5 第三批條目。
