# Official Web Search Interface

只在本地知識庫不足、版本不符、內容衝突或使用者要求更新資訊時呼叫。請求至少包含：

```json
{
  "query": "iTest 26.2 PowerShell Test Step",
  "official_only": true,
  "requested_version": "26.2.0"
}
```

成功結果每筆必須包含資料名稱、發布單位、適用版本、URL、查詢日期與使用範圍。只有 iTest 官方 Help、官方文件、Support Portal、Knowledge Base、Release Notes、API Reference、Command Reference、官方整合文件或官方公告可作主要依據。

工具不存在、沒有權限或沒有網路時，不得聲稱搜尋過。回應應明示「目前執行環境無法存取外部官方資料，因此無法完成外部查證。」
