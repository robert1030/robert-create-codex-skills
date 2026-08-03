# Collection 補件契約

## 定位

本契約定義 `v1.2.0-dev-r3` 如何接收已驗證的缺失目標補件。補件是原始 collection 之外、可回查來源的附加檔案，不能覆寫原始 member、不能刪除原始失效關聯，也不能把未取得的內容寫成占位文字後宣稱完成。

目前 `scripts/supplement_manifest.py` 僅驗證補件宣告，尚未接入 CLI、Package IR、Adapter、Chunker 或正式 Validator。它不是補件已套用的宣稱。

## 不可變更的原始證據

針對 r2 驗證證據中的 iTest Help collection，補件宣告的 `base.collection_sha256` 必須等於 `3ca1b2a6807776080842cec3d87e16781469e4353c6a6d0871793ae100122073`。這個值綁定 r2 報告記錄的原始 collection，而非只依檔名判定。

原始 6 個 `source_missing_target` occurrence 必須保留原始 source、reference、關聯型別、fragment 與位置。它們對應 5 個不同的虛擬目標：

| 原始 source member | 原始參照 | 需要的補件虛擬路徑 | 類別 | occurrence |
|---|---|---|---|---:|
| `popups/appium_send_to_background.html` | `../images/appium_send_to_background.png` | `images/appium_send_to_background.png` | resource | 1 |
| `topics/popups/scriptget.html` | `../images/scriptget.jpg` | `topics/images/scriptget.jpg` | resource | 1 |
| `topics/popups/scriptset.html` | `../images/scriptset.jpg` | `topics/images/scriptset.jpg` | resource | 1 |
| `topics/sb_manually_installing_cs_type.htm` | `preferences.14.htm#1256571` | `topics/preferences.14.htm` | content | 1 |
| `topics/ui_menus_itest.htm` | `preferences.14.htm#1256571` | `topics/preferences.14.htm` | content | 1 |
| `contexts.xml` | `topics/stc_sessions_and_rest_api_mapping.htm#1420396` | `topics/stc_sessions_and_rest_api_mapping.htm` | content | 1 |

`topics/preferences.14.htm` 必須同時明確指派給兩個 original occurrence。只補一個檔案但只記錄其中一個引用，仍不可視為完整補件。

## 補件來源策略

優先順序如下：

1. 同一產品版本的原廠發行包或原廠修補包。
2. 可證明版本與來源的內部發行庫、原始碼庫或建置產物。
3. 具版本與授權資訊的歷史封存包。
4. 由文件維護者提供的原始目標檔。

不得自動從網路猜測下載，不得用其他版本同名檔替代，不得由 LLM 重寫缺頁或補畫圖片。若無法取得可驗證來源，該 occurrence 維持 `source_missing_target`，collection 維持 `partial_success`。

## 補件宣告格式

每個補件都必須提供 `collection-supplement.json`，至少包含：

```json
{
  "schema_version": "1.0",
  "base": {
    "collection_sha256": "<64 個十六進位字元>"
  },
  "members": [
    {
      "target_member": "topics/preferences.14.htm",
      "category": "content",
      "content_sha256": "<補件檔內容的 SHA-256>",
      "origin": {
        "kind": "vendor_release",
        "artifact_sha256": "<取得補件之來源包的 SHA-256>"
      },
      "resolves": [
        {
          "source_member": "topics/sb_manually_installing_cs_type.htm",
          "raw_reference": "preferences.14.htm#1256571",
          "relationship_type": "html_a_href",
          "fragment": "1256571",
          "location": "<原始 occurrence 位置>"
        }
      ]
    }
  ]
}
```

`target_member` 必須由原始 relative reference 重新推導。每個補件 member 必須具有自身內容 SHA-256、來源 artifact SHA-256、來源種類與至少一個原始缺失 occurrence。補件 member 不可指派未知的 occurrence，不可重複指派同一 occurrence，也不可使用與原始 relative path 不符的虛擬路徑。

## 未來 runtime 接入硬閘門

補件宣告通過不等於 collection 可升為 `success`。正式接入時必須依序完成：

1. 驗證 base collection、來源 artifact 與每個補件 member 的 SHA-256。
2. 把補件 member 以 `origin: supplement` 加入新的 Package IR revision，保留原始 Package IR 與原始缺失 edge。
3. 重新解析每個被補件影響的關聯，記錄原始 `source_missing_target` 與新的 `resolved_by_supplement` provenance。
4. content 補件必須通過既有 Adapter、Document IR、Chunk 前及 Chunk 後硬閘門。resource 補件必須驗證 byte hash、member 身分與引用關聯。
5. 由原始 collection 加補件重跑獨立 Validator。只有全部原始缺失 occurrence 已被有效補件覆蓋、所有內容來源成功、六項 collection gate 均通過時，才可升為 `success`。

只覆蓋部分 occurrence 時，Validator 必須輸出仍未覆蓋的清單，且最終狀態維持 `partial_success`。任何 SHA-256、base binding、路徑、關係指派或內容驗證失敗都必須是 `fatal_error`。
