# 平台能力與降級階梯

**核心原則**：不以平台名稱決定行為，一律先偵測實際能力。能力缺席不是失敗，而是切換到對應的降級分支並誠實記錄。有 Python 時可執行 `scripts/detect_capabilities.py` 取得 JSON 結果，沒有時照本文件的判斷條件人工判定。

## 能力清單與缺席時的行為

| 能力鍵 | 偵測方式 | 具備時的行為 | 缺席或未知時的降級行為 |
| --- | --- | --- | --- |
| `filesystem_write` | 實際寫入一個探測檔並回讀 | 走 agent 模式輸出檔案 | 改走 web 模式，在回覆中輸出完整 Markdown，且不宣稱已存檔 |
| `temp_dir` | 依序試 `tempfile.gettempdir()`、`TMPDIR`、`TEMP`、`TMP`、`XDG_RUNTIME_DIR`、家目錄、當前工作目錄，逐一以寫入回讀確認 | 寫入暫存目錄，不污染專案 workspace | 全部不可用時，改用使用者明確指定的路徑；仍不可用就降為 web 模式並說明原因 |
| `shell` | 找得到 `bash`、`sh` 或 `cmd` | 可用 shell 執行驗證器 | 改用宿主提供的執行方式；都沒有就人工逐節自檢 |
| `python` | 本偵測腳本跑得起來即為真 | 執行 `scripts/validate_handoff.py` 與 `scripts/validate_punct.py` | 改為照 `references/output-contract.md` 逐節自檢，並在交付時明講本次未跑機器驗證 |
| `powershell` | 找得到 `pwsh` 或 `powershell` | Windows 上可用 PowerShell 執行驗證器，注意 `references/encoding-policy.md` 的版本差異 | 改用其他可用 shell 或宿主執行方式 |
| `git` | 找得到 `git` | 可引用 commit、diff、branch 作為 artifact 佐證 | 只引用使用者或工具結果提到的 commit，不自行推測雜湊 |
| `network` | 不主動連線探測，預設回報 `UNKNOWN` | 需要查證時先取得使用者同意再連線 | 未知或不可用時，待查證事項標 `[UNVERIFIED]` 或 `[BLOCKED]` |
| `conversation_full_access` | 偵測不到，一律回報 `UNKNOWN`，由執行中的 agent 自行判斷 | 完整掃描全對話 | 只交接看得到的部分，並在第八節「脈絡涵蓋」寫明受限範圍 |
| `attachment_create` | 偵測不到，回報 `UNKNOWN` | 建立附件後先確認建立成功再回報 | 不宣稱已建立附件，改以對話內單一可複製區塊交付 |
| `plain_text_output` | 恆為真 | 最低保證的交付管道 | 無 |
| `validator_runnable` | 有 Python 且腳本可讀取 | 驗證非 0 就修到綠燈，不得請示放行 | 逐節人工自檢，並在交付時標示未跑機器驗證 |
| `reference_files_readable` | 實際開啟本 skill 根目錄下的 `references/output-contract.md` | 照 pointer 讀完逐節細則再產出 | 依 SKILL.md 的九節清單、第〇節三條閘門與狀態標記集合產出，結構不變，並在交付訊息說明未載入逐節細則 |

## 三種輸出分支

| 分支 | 判定條件 | 交付方式 | 必須做到 |
| --- | --- | --- | --- |
| agent | `filesystem_write` 且 `temp_dir` 皆可用 | 寫入暫存目錄的 `ai-session-handoff-<主題>-<日期>.md` | 寫入後回讀比對內容，再回報實際完整路徑；驗證器全綠 |
| web | 無檔案系統但可輸出文字 | 對話內單一可整塊複製的 fenced code block | 內容完整九節；可給建議檔名但標示為建議值；不假裝已建立本機檔案 |
| text-only | 連格式化輸出都受限 | 純文字九節內容 | 保留節標題與順序，說明格式受限的原因 |

## agent 模式的落地順序

1. 解析暫存目錄（順序見上表 `temp_dir` 一列），取得實際可寫路徑。
2. 以 UTF-8 without BOM、LF 寫入檔案。
3. 重新讀回檔案，比對長度與九節標題是否與預期一致。
4. 執行 `scripts/validate_punct.py` 與 `scripts/validate_handoff.py`，非 0 修到綠燈。
5. 回報實際完整路徑；沒有通過第 3 步就不得宣稱寫入成功。

使用者明確指定輸出路徑時，以使用者指定為準，並同樣走第 2 步之後的流程。

## 參考檔位置在兩類宿主的差異

pointer 內的相對路徑一律以本 skill 的根目錄為基準，而不是當前工作目錄或使用者的專案目錄。

| 宿主型態 | 參考檔取得方式 | 行為 |
| --- | --- | --- |
| agent 宿主（Claude Code、Codex 等） | skill 根目錄在檔案系統上，可直接開啟 | 照 pointer 讀取；有 Python 時 `scripts/detect_capabilities.py` 會回報 `skill_root` 實際路徑 |
| Web Chat 且宿主一併提供 skill 檔案 | 由宿主提供檔案存取 | 同上，路徑基準仍為 skill 根目錄 |
| Web Chat 只載入 SKILL.md | 取不到參考檔 | 依 SKILL.md 內的九節清單、閘門與標記集合產出，結構相同，並在交付訊息說明未載入逐節細則 |

產出的交接文件要引用 skill 內的檔案時，一律寫成「skill 名稱 ＋ 檔案名」，讓下一個 agent 在自己的宿主上自行解析位置。

## Web Chat 模式的紀律

- 直接輸出完整 Markdown，不要求使用者提供本來就能從當前對話取得的內容。
- 文件內部含三反引號時，外層改用四個反引號包覆。
- 平台支援文件 artifact 時可改用 artifact，但要先確認建立成功再回報。
- 建議檔名寫成建議值，例如「建議另存為 ai-session-handoff-2026-08-04.md」。

## Tasks 與背景工作模式

- 不假設背景工作能取得無限期的完整 conversation state。
- 必要狀態全部寫進文件本身，不依賴宿主替你記住。
- 在第八節「脈絡涵蓋」寫明來源時間與 task 執行時的可見範圍。
- 無法取得完整對話時，輸出 coverage limitation，不以推測補齊。
- 排程能力不等於 session continuation，兩者分開陳述。

## 已知平台差異提醒

- WSL2 與 Windows 原生的路徑格式不同，交接文件內的路徑要標明是哪一種，必要時兩種都給。
- Windows 路徑含空白或繁體中文時，指令範例要加引號。
- Linux 與 macOS 的暫存目錄可能受 `TMPDIR` 影響，不要寫死單一路徑。
- 宿主是否允許執行子程序、是否允許寫檔，屬執行期事實，依偵測結果而非平台名稱決定。
