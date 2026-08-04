# Agent Tool Contracts

| 工具 | 用途 | 輸入 | 成功輸出 | 無結果 | 錯誤與權限 | 降級方式 |
| --- | --- | --- | --- | --- | --- | --- |
| `knowledge_retrieval` | 查詢已驗證本地知識庫 | `query`、可選 `version`、`component`、`limit` | 附 Chunk ID 與來源欄位的結果陣列 | `status: no_results` | `tool_unavailable`、`permission_denied`、`index_invalid` | 說明本地無法檢索，不以模型記憶作答 |
| `metadata_filter` | 以版本、元件、來源檔案縮小結果 | filters JSON | 符合條件的 metadata | `status: no_results` | 同上 | 回到未過濾結果，明示無法套用 filter |
| `source_document` | 讀取指定 Chunk 或原始來源記錄 | `chunk_id` | 完整內容與引用欄位 | `status: not_found` | `permission_denied`、`integrity_error` | 不引用未讀到的內容 |
| `official_web_search` | 在本地證據不足時查官方資料 | query、可選 version | 官方 URL、發布單位、日期、適用版本與摘要 | `status: no_results` | `tool_unavailable`、`network_unavailable`、`permission_denied` | 顯示外部查證不可用，輸出知識缺口 |
| `citation_builder` | 以既有 metadata 建立引用區塊 | 已驗證 source record | 來源格式文字 | `status: insufficient_metadata` | `integrity_error` | 手動列出可驗證欄位，不能補造頁碼 |

這些是能力契約，不是保證目前 runtime 已提供的工具名稱。Agent 必須在實際呼叫前確認工具可用與授權。
