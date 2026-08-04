# 輸入對話｜跨平台疑難排解

使用者：我的打包腳本在 WSL2 跑得好好的，在 Windows 10 繁體中文版就爆掉。

助理：先確認錯誤訊息。你貼一下。

使用者：`UnicodeEncodeError: 'cp950' codec can't encode character`。腳本是 `tools/build.py`。

助理：這是主控台字碼頁 950 的問題。腳本印出的符號在 CP950 無法編碼。可以設 `PYTHONUTF8=1` 或改成 ASCII 標記。

使用者：我在 PowerShell 5.1 試過 `chcp 65001`，還是有問題。

助理：`chcp` 只改主控台字碼頁，不影響已啟動的子程序既定編碼。我建議兩層處理：程式自己設定輸出錯誤處理，另外環境設 `PYTHONUTF8=1`。我已改好 `tools/build.py` 的輸出部分。

使用者：改完在 WSL2 也要能跑，不要顧一邊。

助理：我在 WSL2 實測過，退出碼 0。Windows 10 我沒有環境可以實測，只能請你試。

使用者：好。另外我懷疑檔名有中文也會出事，但還沒驗證。

助理：這點我沒測過，先記著。

使用者：交接吧，下一個 session 要在 Windows 實測。
