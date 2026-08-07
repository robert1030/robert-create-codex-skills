# Error Handling and Fallback

| 狀態 | Agent 行為 | 對使用者揭露 |
| --- | --- | --- |
| `tool_unavailable` | 不嘗試假裝呼叫；使用已可讀的知識檔案或無答案格式 | 說明目前缺少該工具 |
| `permission_denied` | 不繞過權限；不讀取未授權資料 | 說明無法存取指定資料 |
| `no_results` | 檢查同義詞與版本 filter，仍無結果才進外部資格判斷 | 說明知識庫沒有可靠結果 |
| `index_invalid` 或 `integrity_error` | 停止引用受影響資料，改用仍可驗證的結果 | 說明來源鏈不完整 |
| `network_unavailable` | 不改用模型記憶 | 說明外部官方查證不可用 |
| `version_conflict` | 分開來源和版本，請求或揭露版本資訊 | 說明不能混用版本 |

所有降級都要保留已確認內容、知識缺口與外部查證狀態。不得生成未被來源支持的 iTest 步驟或語法。
