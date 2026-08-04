# 編碼測試素材

本目錄的檔案刻意使用非 canonical 編碼，供 `tests/test_encoding.py` 驗證偵測與回報行為，因此排除在 canonical 編碼檢查之外。

| 檔案 | 內容 |
| --- | --- |
| `utf8_lf.md` | UTF-8 without BOM ＋ LF |
| `utf8_bom.md` | UTF-8 with BOM |
| `crlf.md` | CRLF 換行 |
| `cp950.md` | CP950 編碼 |
| `undecodable.bin` | 兩種編碼都無法解碼的位元組 |
