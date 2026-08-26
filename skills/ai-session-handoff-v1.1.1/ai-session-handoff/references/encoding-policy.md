# 編碼與換行政策

## Canonical 規格

- 所有原始碼、Markdown、JSON、YAML 與測試資料：**UTF-8 without BOM**。
- 換行：**LF**。
- 封裝時維持上述規格，不依宿主系統改成區域編碼。
- 交接文件輸出時同樣採 UTF-8 without BOM ＋ LF。Windows 環境產生的檔案若帶 BOM 或 CRLF，`scripts/validate_handoff.py` 會以 `[WARN]` 提醒但不視為失敗；套件檔案則由 `scripts/check_encoding.py` 視為錯誤。

## 讀檔規則

- 一律明確指定編碼，不依賴系統預設。
- 先偵測 UTF-8 BOM 並剝除，同時記錄這件事。
- UTF-8 解碼失敗時，明確嘗試 CP950；判定成立才正規化為 UTF-8，並記錄「本檔原為 CP950」。
- 兩種編碼都失敗時，回報檔名、嘗試過的編碼與出錯的 byte 位置，不以替換字元靜默略過。
- 判定邏輯的單一真實來源是 `scripts/check_encoding.py` 的 `read_text()`。

## Windows 繁體中文環境

CP950 主控台是最常見的破口。防護分兩層：

1. **程式自保**：本套件的驗證器啟動時呼叫 `scripts/_console.py` 的 `configure_console()`，保留主控台原編碼但把錯誤處理改為 `backslashreplace`，並一律使用 ASCII 標記 `[OK]`、`[FAIL]`、`[WARN]`，不用符號圖示。
2. **環境設定**：執行 Python 前設定 `PYTHONUTF8=1`，可一併解決子程序輸出與檔案讀寫的預設編碼問題。

各 shell 的設定方式不同，不可假設三者一致：

| 環境 | 設定 UTF-8 的方式 | 注意事項 |
| --- | --- | --- |
| Windows PowerShell 5.1 | `$env:PYTHONUTF8 = "1"` | 寫檔行為見下方實測表：`Out-File` 與 `>` 會寫出 UTF-16LE，交接文件會直接驗證失敗；請改用 .NET 的 `WriteAllText` 搭配不含 BOM 的 UTF8 編碼，或改由 Python 寫檔 |
| PowerShell 7 以上 | `$env:PYTHONUTF8 = "1"` | 預設輸出已是 UTF-8 without BOM，行為與 5.1 不同，腳本不要共用同一套假設 |
| `cmd.exe` | `set PYTHONUTF8=1` | 主控台字碼頁可能仍是 950，`chcp 65001` 會改變顯示但不改變既有子程序的既定編碼 |
| Linux 與 WSL2 | 通常已是 UTF-8 | 確認 `LANG` 或 `LC_ALL` 未被設成非 UTF-8 語系 |

## PowerShell 5.1 寫檔行為實測

實測環境：Windows 10 Pro 19045 繁體中文版，PowerShell 5.1.19041，主控台字碼頁 950。同一份交接文件以四種方式寫出後，以 `scripts/validate_handoff.py` 驗證：

| 寫法 | 實際位元組開頭 | 編碼判定 | 驗證結果 |
| --- | --- | --- | --- |
| `$doc \| Out-File $path` | `ff fe` | UTF-16LE | 失敗（退出碼 1，回報兩種編碼都無法解碼於 byte 0） |
| `$doc > $path` | `ff fe` | UTF-16LE | 失敗（退出碼 1） |
| `$doc \| Set-Content -Encoding utf8 $path` | `ef bb bf` | UTF-8 with BOM ＋ CRLF | 通過，但有 BOM 與 CRLF 兩則警告 |
| `[IO.File]::WriteAllText($path, $doc, (New-Object Text.UTF8Encoding($false)))` | 內容首位元組 | UTF-8 without BOM | 通過，無警告 |

**建議寫法**：

```powershell
[IO.File]::WriteAllText($path, $doc, (New-Object Text.UTF8Encoding($false)))
$doc = [IO.File]::ReadAllText($path, [Text.Encoding]::UTF8)
```

讀檔同理：PowerShell 5.1 的 `Get-Content` 在 CP950 主控台下會以區域編碼解讀 UTF-8 檔案而產生亂碼，改用 `[IO.File]::ReadAllText` 並明確指定 UTF8。PowerShell 7 以上的預設值不同，不要沿用 5.1 的假設。

## 其他風險點與處置

| 風險 | 處置 |
| --- | --- |
| 路徑含繁體中文 | 以 Python 的路徑 API 處理，不自行拼字串；指令範例加引號 |
| 路徑含空白 | 指令範例一律加引號 |
| CRLF 與 LF 混用 | 套件檔案一律 LF；讀檔時偵測並回報，不靜默轉換 |
| Git `core.autocrlf` | 專案內建議設為 `false` 或以 `.gitattributes` 指定 `* text eol=lf`，避免簽出時被改成 CRLF |
| ZIP entry 名稱編碼 | 封裝時 entry 名稱一律 ASCII 且用正斜線，`scripts/validate_skill.py --zip` 會檢查 |
| 子程序輸出解碼 | 呼叫子程序時明確指定 `encoding` 與 `errors`，不吃系統預設 |
| stdout 與 stderr 解碼 | 由 `configure_console()` 處理，訊息主體使用 ASCII 標記 |

## 檢查指令

以下 `<python>` 代表當前環境可用的直譯器：

```text
<python> scripts/check_encoding.py .
<python> scripts/validate_skill.py .
```
