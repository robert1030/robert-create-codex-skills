# normalized-document.md 契約

每個來源必須產生一份獨立的 `normalized-document.md`。多個來源不得合併成同一份標準化文件。

## 必須保留

- 正確 Heading hierarchy。
- 完整段落。
- Markdown table。
- Table Caption 與表格所在 Heading context。
- 完整清單。
- 程式碼區塊。
- 已驗證的圖片 OCR、QR payload 或圖形描述。
- 必要失敗占位。

## 必須排除

- 印刷頁碼及重複頁首頁尾。
- 已知 OCR 亂碼。
- Logo OCR 垃圾。
- 無法追溯的 LLM 補寫。
- 為填滿 Token 而重複的正文。

## 失敗占位

```markdown
> [內容擷取未完成]
>
> - 來源位置：第 8 頁
> - 單元：page-008-image-002
> - 類型：infographic
> - 狀態：failed
> - 嘗試次數：3
> - 原因：OCR 文字品質未達門檻
> - 詳細紀錄：failed-items.jsonl
```

## 正規化追蹤

一般模式至少在 Block 中保存：

- `raw_text`
- `text`
- `transformation_summary`

Forensic 模式可保存完整 before／after 及中間影像。
