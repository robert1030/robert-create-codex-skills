# 凍結契約

## v1.0.0

- Skill 名稱固定為 `itest-help`。
- 產品與文件版本固定為 `iTest Help 26.2.0`。
- 唯一可作為內部主要依據的 RAG archive 為 `itest-help_26.2.0-rag-v1.2.1.zip`，SHA-256 為 `309BA7AACF41000C242FD0FBD1AF0B8B548F1EAB14A055284A3615DDE82BBC70`。
- 原始 source ZIP 的 7,004 個 member 路徑與 member SHA-256 已和 collection manifest 全數對齊。
- 本地優先、引用必填、外部資料揭露、版本不可混用與不確定性降級是不可移除的行為契約。
- 原始 collection 只有 1 個 `source_missing_target`，維持 `partial_success`。不得補造目標或將它宣稱為完整成功。

後續變更知識庫、版本政策、來源優先順序、引用格式或外部查證規則時，必須新增 skill 版本並重新執行驗證與封裝。

## v1.1.0

本版只加佈署相容層，**v1.0.0 的凍結內容一項未動**，以下三項經 `tests/test_deploy_contract.py` 斷言守門：

- RAG archive SHA-256 仍為 `309BA7AACF41000C242FD0FBD1AF0B8B548F1EAB14A055284A3615DDE82BBC70`。
- `knowledge/retrieval-index.jsonl` 的 SHA-256 仍為 `7CF0F4ECD8A9E9943AB1E9467D9E2B0CCED68D8FA2C0A872BA3C4EAFC48832F0`，1,522 筆記錄。
- `knowledge/chat-web-knowledge.md` 的 SHA-256 仍為 `B0645A3856DFD9E3A319C2D97F61F3BFAEA1765E6CD0F561923C75E0E52BBB4E`；原始 source ZIP 的 7,004 個 member 對齊結果與 `partial_success` 已知限制均未改寫。

### 新凍結項

- 三個佈署 profile 的定義：`runtime`（不含 `knowledge/rag/`，含 `chat-web-knowledge.md`）、`chatweb`（兩者都不含）、`full`（原樣含 `knowledge/rag/` 的 9,329 檔）。三者的知識內容完全相同，差別只在 provenance 素材與 Chat Web 知識檔。
- skill 目錄名固定為 `itest-help`，`SKILL.md` frontmatter 固定只有 `name` 與 `description` 兩個欄位。加入 `allowed-tools` 等 Claude Code 專屬欄位會改變對 ChatGPT Codex 的相容基準，屬於新版本才能做的變更。
- 檢索指令必須與工作目錄無關。`scripts/search_itest_help.py` 與 `scripts/inspect_chunk.py` 以 `__file__` 定位索引，這個性質不得移除。
- 所有隨附檔案為無 BOM 的 UTF-8、LF 換行，`.py` 只 import 標準函式庫。
- `runtime` 與 `chatweb` profile 安裝到 Windows 個人 skill 目錄後，最長完整路徑必須低於 260 字元。

### 誠實聲明

`runtime` 與 `chatweb` profile 不隨附 `knowledge/rag/`，因此在這兩個 profile 下**無法**重跑 index 對 chunk 的逐筆雜湊比對，只能以 `knowledge/retrieval-index-manifest.json` 的凍結 SHA-256 確認索引未被竄改。完整來源鏈驗證必須使用 `full` profile：

```text
python scripts/validate_itest_help.py --profile full <full-profile-root>
```

`full` profile 有 1,136 個檔案路徑在安裝到使用者家目錄下的 skill 目錄後會超過 Windows 的 260 字元上限，全部落在 `knowledge/rag/` 的 `chunks/` 子目錄。它是存證與驗證用途，請解壓到短路徑，不得放進 `~/.claude/skills/`。

### 未變更項

`core/` 的八份政策檔、`agents/openai.yaml`、`knowledge/` 下的任何資料檔、既有 adapter 的原有內容一律未改。`adapters/chat-web/knowledge-configuration.md` 只在開頭追加一段路徑導引，原有段落原封不動。

## v1.2.0

本版修的是**檢索層迴歸**。v1.0.0 重做本包時，遺失了 2026-07-03 版 `itest-help-skill` 已具備並驗證有效的兩條檢索紀律，導致中文提問時關鍵來源排不進回傳範圍，不同執行環境拿到不同證據集而給出分歧答案。

### 根因量測（2026-08-02）

以使用者原問句「itest tcl 本地變數 hash 判定包含 sha true Action」實測檢索排名：

| 來源檔 | 中文原問句 | 抽英文技術詞後 |
| --- | ---: | ---: |
| `topics/action_scriptget.htm` | 排 5，25 分 | 排 7，29 分 |
| `topics/command_syntax.htm` | 排 9，23 分 | 排 1，35 分 |
| `topics/action_if.htm` | 排 47，16 分 | 排 18，23 分 |
| `popups/regexp.html` | 未命中 | 排 65，17 分 |
| `popups/string.html` | 未命中 | 排 90，15 分 |

當時 `--limit` 預設為 5，top-8 分數落在 24 至 27 的窄區間。以中文查詢一次即作答，看得到 `scriptGet` 卻看不到 `action_if`、`regexp` 與 `string`。`tokenize()` 把連續中文合併成單一 token，對全英文知識庫永遠不命中，中文查詢實際生效的只有夾雜的英文詞。

### 修補後量測（同一題，照新政策執行）

| 步驟 | 查詢 | 關鍵來源命中 |
| --- | --- | --- |
| 第一輪，抽英文技術詞 | `local variable regexp string match if action true` | `command_syntax.htm` 由排 9 升至**排 1**，定義 iTest world 與 Tcl world 的關鍵文件進入回傳範圍 |
| 第二輪，鎖定 if 構造 | `if action expression Description cell evaluate true false` | `action_if.htm` 由排 47 升至**排 3** |
| 第二輪，鎖定指令定義 | `regexp command returns 1 if expression matches Java` | `command_syntax.htm` **排 1**，其指令表已完整涵蓋 `regexp` 的 Java regex 說明 |
| 第二輪，鎖定 string 限制 | `string match glob pattern limitation iTest interpreter` | `command_syntax.htm` **排 1**，其指令表已完整涵蓋 `string match` 只支援 `*` 與 `?` 的限制 |

單輪查詢仍不足以取得 `action_if.htm`，這正是多輪檢索紀律不可省略的實證依據。`popups/regexp.html` 與 `popups/string.html` 在兩輪後仍排在回傳範圍外，但 `command_syntax.htm` 已承載相同事實，屬冗餘來源而非缺漏。

### 本版新增的凍結項

- **查詢構詞紀律**：知識庫全文為英文，中文問題必須抽出對應的英文技術詞一起查。
- **多輪檢索紀律**：無結果、分數普遍偏低、分數擠在很窄的區間、回傳的 `heading_path` 都不是問題指向的功能區塊，或問題涉及多個功能區塊時，必須換關鍵字再查；不得因為第一次查不到就宣告知識庫沒有答案。
- 上述兩條紀律必須同時存在於 `core/retrieval-policy.md`、`SKILL.md`、`adapters/agent/instructions.md` 與 `adapters/chat-web/instructions.md` 四處，由 `tests/retrieval-discipline-tests.jsonl` 的 8 個案例與 `tests/test_deploy_contract.py` 的斷言雙重守門。
- `scripts/search_itest_help.py` 的 `--limit` 預設值不得低於 10。

### 未變更項

`knowledge/` 下的任何資料檔、v1.0.0 與 v1.1.0 的所有凍結雜湊、`agents/openai.yaml`、其餘 `core/` 政策檔一律未改。`core/retrieval-policy.md` 的來源優先順序五條與最後一段降級規則原句保留，本版只在其後追加新章節。

### 能力邊界

回歸測試驗的是「紀律文字存在於指定檔案中」，**不驗「模型執行時真的照做」**。這與既有的版本歧義規則同一強度。修補是否真的改善行為，只能以同一問題在多個執行環境重測後比較引用來源，屬行為測試，不在自動化閘門涵蓋範圍。

## v1.3.0

v1.2.0 修好了「查得到哪些文件」，v1.3.0 修的是「每份文件看得到多少」。

### 根因量測（2026-08-02）

v1.2.0 上線後於 Claude Chat Web 重測，`command_syntax.htm` 確實被引用了，但被定性為「iTest 直譯器指令設計貼近 Tcl 語法之背景說明」，且該題的 `【知識庫來源】` 與 Chunk ID 遭整段撤除，改列為「參照 htm 檔名」。追查原因：

| 量測項 | 數值 |
| --- | ---: |
| `command_syntax.htm` chunk-0001 全文長度 | 30,499 字元 |
| 舊版單筆回傳長度（取前綴） | 1,200 字元 |
| `regexp` 定義所在位置 | 第 23,060 字元 |
| `string match` 限制所在位置 | 第 27,042 字元 |
| 全庫 1,522 筆中被截斷的筆數 | 739 筆，48.6% |
| 預設查詢下看不到的內容占全庫比例 | 60.1% |

模型看到的 1,200 字元正好是開頭的概述段，因此它對來源的定性完全吻合它收到的證據，但對知識庫的陳述是錯的。v1.2.0 新增的「只有在來源文字直接支持該操作或語法時，才可寫進 `【知識庫來源】`」在這個前提下造成過度降級，本版一併修正。

### 本版新增的凍結項

- **`search_itest_help.py` 的 `text` 語意由「前綴截斷」改為「命中詞為中心的取窗」**。視窗寬 300 字元、最多 5 個，以查詢詞在該 Chunk 內的出現次數倒數平方根加權挑選，相鄰視窗必須合併成連續段落，視窗之間以 `…` 分隔。加權是必要的：不加權時開頭的高頻詞會把所有視窗吃光。相鄰合併也是必要的：不合併時分隔符會把跨界的詞句攔腰切斷。
- **回應新增 `text_length` 欄位**，`text_truncated` 改以「回傳長度是否小於全文長度」判定。
- **片段處理紀律**：不得以「片段沒有提到」為由斷定知識庫沒有該內容；`text_truncated` 為 `true` 且來源可能切題時必須取完整 Chunk 再判斷；不得因片段未涵蓋而撤除 `【知識庫來源】`，部分超出範圍的內容應單獨標示而非整段撤掉引用。
- 上述紀律必須同時存在於 `core/retrieval-policy.md`、`SKILL.md`、`adapters/agent/instructions.md` 與 `adapters/chat-web/instructions.md`，由 `tests/retrieval-discipline-tests.jsonl` 的 14 個案例與 `tests/test_deploy_contract.py` 的斷言雙重守門。

### 修補後量測

同一查詢 `local variable regexp string match if action true` 對 `command_syntax.htm`：

| 事實 | 舊版取前綴 | 本版取窗 |
| --- | --- | --- |
| `Returns 1 if the expression matches, 0 otherwise` | 看不到 | **可見** |
| `java/util/regex/Pattern` | 看不到 | **可見** |
| `[string match args] supports only * and ?` 限制 | 看不到 | 仍看不到，候選視窗排名 18，超出預算 |
| 回傳長度 | 1,200 字元 | 1,509 字元 |

token 預算幾乎未變，而該題最關鍵的 `regexp` 回傳值定義與引擎歸屬都進入了預設輸出。

### 能力邊界

取窗只提高「切題來源看起來切題」的機率，**不保證單次回傳涵蓋該 Chunk 的全部相關內容**。30,499 字元的 Chunk 無法壓進 1,500 字元。完整性仍依賴 `text_truncated` 觸發的 `inspect_chunk.py` 呼叫，而那一步靠的是政策文字而非程式強制，與既有紀律同一強度。

### 未變更項

`knowledge/` 下的任何資料檔、v1.0.0 至 v1.2.0 的所有凍結雜湊、`agents/openai.yaml` 一律未改。`score()` 排序邏輯、`--limit` 預設值 10、v1.2.0 的查詢構詞與多輪檢索紀律原句保留。

## v1.3.1

本版只加行為紀律，不動任何程式邏輯。修的是使用者長期觀察到的錯誤模式：**把原生 Tcl 的指令行為套用到 iTest 直譯器環境**，即使提問已明說「iTest Tcl」。

### v1.3.0 取窗修補的隔離驗證

以「`math` 運算式過大」為隔離題（該事實只存在於長 chunk 深處，無 popup 短檔備援）：

| 事實 | 位置 | 舊版取前綴 1,200 字元 | v1.3.0 取窗 |
| --- | ---: | --- | --- |
| `Cannot convert to number` 限制 | 第 20,639 字元 | 看不到 | **可見** |
| `math.wide` 分段變數 workaround | 第 20,872 字元 | 看不到 | **可見** |

兩份載有該事實的來源分別為 30,499 與 8,396 字元，舊版皆被截斷，因此該事實在舊版從任何來源都取不到。取窗修補的效果由此隔離確認。

### 本版新增的凍結項

- **iTest 直譯器指令與原生 Tcl 不等價**：回答任何 iTest 指令用法前，必須先取得該指令在 `command_syntax.htm` 指令表中的條目，確認有無 `Limitation`、`not supported` 或 `syntax differs from Tcl` 條款；未查證前不得以原生 Tcl 行為作答。政策內列出的每個不等價項目都由 `tests/test_deploy_contract.py` 反向斷言其在知識庫中確有明文。
- **三個執行環境不可混用**：iTest 直譯器、Tcl 直譯器、Tcl Shell Session 各自獨立。
- **不得把某一環境的寫法宣告為另一環境的錯誤寫法**，除非知識庫有明文依據。
- 上述紀律必須同時存在於 `core/retrieval-policy.md`、`SKILL.md`、`adapters/agent/instructions.md` 與 `adapters/chat-web/instructions.md`，由 `tests/retrieval-discipline-tests.jsonl` 的 21 個案例與 `tests/test_deploy_contract.py` 的斷言雙重守門。

### 能力邊界

本版新增的規則能降低「把原生 Tcl 行為套進 iTest」這一類錯誤的機率，**但擋不住憑空產生沒有來源的斷言**。那是不同的病：前者是套用錯誤的既有知識，後者是無中生有。後者是否需要另立規則，待累積更多樣本後再評估，本版不處理。

### 未變更項

`knowledge/` 下的任何資料檔、v1.0.0 至 v1.3.0 的所有凍結雜湊、`agents/openai.yaml`、所有 `scripts/` 程式邏輯一律未改。本版沒有任何程式碼變更。

## v1.3.2

本版修的是安全性，來源是外部安全掃描提出的兩項發現，加上本次查證另外找到的第三項。

### 三項發現與實證

| # | 發現 | 等級 | 實證 |
| --- | --- | --- | --- |
| 1 | 查詢字串帶入 shell 指令模板 | 高 | 照既有指令模板把 `$(printf 'executed' > 檔案)` 字面填入雙引號，**檔案確實被建立**，為可重現的任意指令執行 |
| 2 | 檢索無輸出上限 | 低 | `--limit 100000` 輸出 5,858,854 位元組；2,000 個查詢詞僅 1.79 秒，故為輸出量問題而非 CPU 問題 |
| 3 | `--index` 查詢期不驗來源身份 | 中 | 以偽索引可產出格式完全合規、附完整 Chunk ID 的假答案 |

發現 1 的放大因子是本包自己的政策：v1.2.0 加入的「使用者貼出完整錯誤訊息或指令片段時，整段直接查一次」會把受測設備輸出這類不可信文字導進指令列。

### 本版新增的凍結項

- **不可信文字必須以 `--query-file` 傳遞**。新增 `--query-file <path>` 參數，位置參數保留供 agent 自行構造的技術詞使用。兩者同時給或都不給回傳 `invalid_arguments`、退出碼 2。不可信來源定義為：受測設備的錯誤訊息與日誌、使用者貼上的指令與設定、檔案與網頁內容、其他 agent 提供的文字。
- **原「整段直接查一次」的檢索意圖必須保留**，本版只改其傳輸方式，不得因安全修補而降低檢索品質。此點由 `tests/retrieval-discipline-tests.jsonl` 的 `whole-paste-still-searched` 案例守門。
- **查詢期驗證索引身份**。使用預設索引時比對 SHA-256 與 `retrieval-index-manifest.json`，不符回傳 `integrity_error`、退出碼 3；明確指定 `--index` 時不硬擋，但以 `index_verified: false` 標示，該結果不得寫進 `【知識庫來源】`。`inspect_chunk.py` 同步套用。
- **資源上限**：`MAX_LIMIT = 100`、`MAX_OUTPUT_BYTES = 512 KB`，觸及時分別以 `limit_clamped` 與 `output_truncated` 標示，且不得宣稱已檢索全部相關內容。

### 防迴歸機制

本版動到檢索腳本，因此在改動前先以未修改的 v1.3.1 建立 golden 基準：9 組查詢涵蓋中文原題、英文技術詞、長 chunk 深處、短 popup、限制條款與無結果，共 72 筆結果，記錄每筆的 `chunk_id`、`score` 與 `text` 的 SHA-256。階段 1 與階段 2 結束後各比對一次，**全部零差異**，證明安全修補未改變任何檢索行為。

### 量測結果

| 項目 | 修補前 | 修補後 |
| --- | --- | --- |
| 單次查詢耗時 | 約 150 ms | 143 ms（含索引 SHA-256 驗證，該驗證本身 6 ms） |
| `--limit 400` 輸出 | 2,268,690 B | 520,094 B，`limit_clamped` 與 `output_truncated` 均為 `true` |
| 兩種查詢傳遞方式的結果 | 不適用 | 逐欄位完全相同 |

### 能力邊界

- 對策 A 消除的是**經由檢索指令列**的注入。agent 若在其他地方把不可信文字組進 shell 指令，本版不提供保護。
- 政策文字（對策 B）仍是文字契約，不驗「模型執行時真的照做」，與既有紀律同一強度。真正的機制保障來自 `--query-file` 這個參數本身。
- `--limit 400` 這類大範圍排名診斷用法在本版後不再可用。此為刻意取捨：該用法屬開發期除錯，不是 skill 的執行路徑，需要時應另寫包外腳本直接讀索引。
- 索引身份驗證只涵蓋預設路徑。明確指定 `--index` 時僅標示不阻擋，這是為保留測試彈性所做的取捨。

## v1.3.3

本版把 v1.3.1 的「iTest 直譯器指令與原生 Tcl 不等價」與「三個執行環境不可混用」兩節，合併改寫為一節通用的「兩層執行模型」，並把涵蓋範圍從 Tcl 側擴到 Python 側。起因是同一個錯誤在 Claude.ai chat 與 Claude Code 兩個 surface 重現：`if` Action 的 Command 欄被多寫一層 `if {...}`，而 `if` 並不在 iTest 直譯器的指令表內。v1.3.1 當時把第一次出現判定為單次筆誤，該判斷被第二次重現證明為錯誤，本版按機制性缺口處理。

### 改寫前的查證

| 問題 | 查證結果 | 知識庫依據 |
| --- | --- | --- |
| Python 側的 `if` Action Command 欄語意 | 與 Tcl 側相同，Command 欄放的是運算式 | `action_if.htm`：`An if step evaluates the expression that appears in the Description cell (the value of the Command property)`，同頁並列 Tcl example 與 Python example，並寫明 `elseif` 在 Python 為 `elif` |
| Python 側是否有自己的指令表 | 有，11 個指令，同樣不含 `if` | `command_syntax_python.htm`：`char`、`gget`、`gset`、`info`、`param`、`profile`、`query`、`response`、`tbml`、`velocity`、`xpatheval` |
| Python 側是否有兩層的明文 | 有 | 同頁：`Using square brackets ([]) in Python syntax: Required in session steps and session profiles fields. Not required in non-session steps (eg: eval)`，以及「Some iTest interpreter commands have Tcl/Python counterparts and some do not」 |
| PowerShell 側 | 知識庫沒有 PowerShell 直譯器層 | 全庫 1,522 個 chunk 中，檔名含 `powershell` 者 0 個，內文提及者 4 處，全部是 session type 描述 |

因此本版規則涵蓋 iTest 層、Tcl 側與 Python 側，**不涵蓋 PowerShell**。v1.3.2 交接文件所列的「Python 與 PowerShell 側尚未查證」到此結案：Python 側查證完成並納入，PowerShell 側是知識庫本來就沒有該層，不是尚未查。

### A/B 措辭實驗

改寫前以兩份 staging 副本跑對照，A 版為純抽象原則，B 版為抽象原則加上保留 v1.3.1 的具體不等價清單。兩版各由一個獨立 agent 回答同一組四題，四題分別檢查：擋不擋得住 `if {...}`、會不會誤擋 `scriptEval` 內合法的 `if`、拿掉具體清單後 `regexp` 的 Java 不等價紀律還在不在、以及新措辭會不會讓 agent 無據宣告某寫法錯誤。

結果兩版四題全部正確，行為面打平。採 B 版的理由在測試面：A 版會讓 `tests/test_deploy_contract.py` 中 `Java`、`string match`、`array names`、`lsort` 四個字面斷言同時失效，等於改測試去遷就實作，守門強度下降；B 版保留清單，四個斷言原樣通過。既然行為打平，就沒有理由付這個代價。

實驗過程另外暴露一個知識庫結構問題：`action_if.htm` 的 Tcl example 與 Python example 在原始文件中是螢幕截圖，RAG 只保留圖片標記，沒有可引用的文字。兩版 agent 都是靠 `action_then.htm` 的 `$port_count < 4` 與 `action_while.htm` 的 `$i < 5` 跨頁佐證才拿到正確形狀。因此本版第 6 條規則明文要求跨頁取證。

**證據強度誠實聲明**：本實驗為 n=1 的單次觀測，每版只跑一次四題，執行者為 subagent 而非真人在實際 session 中操作，代表性弱於實機實測。措辭改寫對 LLM 的壓制力**未經統計驗證**，只證明了在這一組題目上兩版都不劣化。

### 本版新增的凍結項

- **兩層執行模型**：iTest 層（Action 欄位、iTest 直譯器指令、field replacement）與原生語言層（`scriptEval`、`scriptSet`、`scriptGet`、session 步驟等進入點之後的內容）。回答前必須先判定問題落在哪一層。
- **不得把原生語言的語法形狀套進 iTest 層**。某個關鍵字在原生語言寫成什麼形狀，不構成它在 iTest 層要寫成同樣形狀的理由。
- **指令表沒有列出的名稱，不是 iTest 直譯器指令**。這類名稱屬於某個 Action 或欄位的語意，必須查該 Action 的說明頁。
- **Python 側的指令表為 `command_syntax_python.htm`**，與 Tcl 側的 `command_syntax.htm` 同等對待。
- **範例形狀可能不在該 Action 自己的頁面上**。該頁範例是螢幕截圖時，必須到同一功能區塊的其他頁面取得佐證，不得因該頁沒有文字範例就宣告知識庫沒有規定，也不得改用原生語言的形狀填補。
- 上述紀律必須同時存在於 `core/retrieval-policy.md`、`SKILL.md`、`adapters/agent/instructions.md` 與 `adapters/chat-web/instructions.md`，由 `tests/retrieval-discipline-tests.jsonl` 的 39 個案例與 `tests/test_deploy_contract.py` 的兩項新斷言雙重守門。

### 附帶修補：契約測試的 profile 判斷

`tests/test_deploy_contract.py` 的 `test_no_file_exceeds_the_windows_path_limit` 原本對三個 profile 一視同仁，斷言所有路徑短於 260 字元，因此在 `full` profile 上必然失敗：最長模擬安裝路徑為 314 字元，全部落在 `knowledge/rag/` 的 chunk 檔。此失敗自 v1.1.0 引入 `full` profile 起即存在，**非本版造成**，v1.3.2 的 full 封裝實測同為 314 字元。真正的代價不是那一個紅燈，而是無法用同一套契約測試一致地驗三個 profile，每次都要人工判斷該紅燈是否為預期。

本版改為 profile-aware：安裝用的 `runtime` 與 `chatweb` 維持「零超限」的嚴格斷言；`full` 改為斷言超限路徑必須全部落在 `knowledge/rag/` 之下，RAG 以外任何檔案超限仍然紅燈。

守門強度以負向驗證確認，注入一個 208 字元檔名的探針後三個情境皆符合預期：

| 情境 | 注入前 | 注入後 | 移除後 |
| --- | --- | --- | --- |
| `runtime` 的 `docs/` | PASS | FAIL | PASS |
| `full` 的 `docs/` | PASS | FAIL | PASS |
| `full` 的 `knowledge/rag/` | PASS | PASS | PASS |

**取捨誠實聲明**：新斷言對 `full` 比原字面斷言寬鬆，它承認 RAG chunk 路徑超限是既定事實。這與 v1.1.0 已凍結的「`full` 不供安裝」一致。若日後 `full` 需要可安裝，此斷言必須連同 RAG 檔名長度一併重新設計，不能只放寬測試。

### 防迴歸機制

- v1.3.1 與 v1.3.2 的所有 `required_policy_text` 字串**全數原樣保留**，包含 `iTest 直譯器指令與原生 Tcl 不等價`、`必須先取得該指令在 command_syntax.htm 指令表中的條目`、`不得以原生 Tcl 的行為作答`、`三個執行環境不可混用`、`不得把某一環境的寫法宣告為另一環境的錯誤寫法`。新措辭把舊句子包含進去，因此舊的 21 個紀律案例與 `test_deploy_contract.py` 既有斷言一個都不必修改，覆蓋強度不會因改寫而弱化。
- 新增 8 個紀律案例（31 增至 39），新增 2 項契約斷言（25 增至 27）。其中 `test_python_command_table_backs_the_two_layer_rule` 反向驗證知識庫真的有 Python 指令表與那兩句明文，並斷言該表**不含** `if`，一旦知識庫改版列入 `if`，該測試會紅燈提醒規則需重新檢視。
- 本版**未改動任何 `scripts/` 程式邏輯**。仍依紀律以 9 組查詢、72 筆結果建立 golden 基準（記錄 `chunk_id`、`score` 與 `text` 的 SHA-256），改寫後比對**零差異**。

### 能力邊界

- 本版把兩節合併為一節抽象原則，抽象原則對 LLM 的操控力在真實 session 中是否等同具體禁令，**尚未實機驗證**。若日後在實際使用中再次出現把原生語法形狀套進 iTest 層的錯誤，應優先考慮補具體禁令，而不是再抽象一層。
- 規則涵蓋 iTest 層、Tcl 側與 Python 側。**PowerShell 不在涵蓋範圍**，因為知識庫沒有 PowerShell 直譯器層的任何明文。使用者若問 PowerShell Test Step 的語法，應依不確定性政策處理，不得以本規則外推。
- 第 6 條的跨頁佐證指引只列出 `action_then.htm`、`action_while.htm`、`action_switch.htm` 與 `loops_about.htm` 四個已知有文字範例的頁面，**不是窮舉**。其他 Action 是否同樣以截圖呈現範例未逐頁清查。

### 未變更項

`knowledge/` 下的任何資料檔、v1.0.0 至 v1.3.2 的所有凍結雜湊、`agents/openai.yaml`、所有 `scripts/` 程式邏輯一律未改。三個 profile 的定義與檔案組成不變，仍為 49、48、9,378 檔。

## v1.3.4

本版動的是檢索腳本，目的是降低「只看片段就宣告知識庫沒有該內容」的發生率。這條紀律 v1.3.0 已寫進政策，但在 v1.3.3 的實機驗證中仍被違反一次，因此本版替純文字契約補上一個機制側的提示。

### 起因與證據強度

v1.3.3 安裝後的實機驗證中，一個 Sonnet 5 的 agent 回答「如何新增 Tcl Test Step」時，檢索到 `test_case_editor_steps_page.htm`（分數 63），但因 `text_truncated` 為 `true` 只看了片段，未執行 `inspect_chunk.py`，就判定「知識庫沒有 GUI 操作明文，證據不足」。經 loop 查核，該 chunk 的完整內容確實含有 `Insert Step | Add a new step immediately following the selected step or procedure. Ctrl-Enter` 的明文，該判定為誤。

**證據強度誠實聲明**：此為單次觀測，且該輪 prompt 中含有「保持精簡，不要過度推理」的指示，該指示本身可能就是省略 `inspect_chunk` 的真正原因。因此「腳本需要補提示」這個因果**並未被證實**，本版修改基於合理推斷而非已驗證的因果，效果同樣未經 A/B 驗證。

### 本版變更

`scripts/search_itest_help.py` 在回應頂層新增兩個欄位：

- `truncated_count`：本次回傳結果中 `text_truncated` 為 `true` 的筆數。
- `next_action`：僅在 `truncated_count` 大於 0 時出現，內容為一句提示與取完整內容的指令。

### 設計取捨

初版構想是在每一筆結果附上含絕對路徑的完整指令，經審查後否決，原因有二：

- **輸出膨脹**：`--limit 100` 時最多多出約 25 KB，會擠壓 `MAX_OUTPUT_BYTES` 的 512 KB 預算，使 `output_truncated` 提早發生，等於為了修一個問題去惡化另一個。
- **資訊揭露**：把絕對路徑寫進檢索輸出，等於讓輸出帶上使用者家目錄結構，而該輸出可能被轉貼給其他服務。v1.3.2 才完成安全修補，不應在本版新增揭露面。

改為頂層單一提示，且指令路徑一律相對。實測膨脹為 213 位元組，輸出不含家目錄。`tests/test_deploy_contract.py` 的 `test_truncated_results_carry_a_next_action_hint` 對絕對路徑標記做反向斷言，防止日後改回絕對路徑。

### 防迴歸機制

本版動到檢索腳本，因此依紀律先以未修改的 v1.3.3 建立 golden 基準（9 組查詢、72 筆結果的 `chunk_id`、`score` 與 `text` 的 SHA-256），修改後比對**零差異**，證明新增欄位未改變任何檢索行為、排序或取窗結果。

紀律案例 39 增至 41，契約斷言 27 增至 28。v1.0.0 至 v1.3.3 的所有 `required_policy_text` 字串全數原樣保留，舊案例一個都未修改。

### 能力邊界

- 新欄位是提示不是強制。模型仍可無視它，強度與既有政策文字相同。真正的機制保障需要改變介面契約，例如不主動回傳片段，那會破壞 v1.3.0 凍結的取窗設計，本版不做。
- 本版未改動 `snippets()` 的任何參數與演算法。取窗契約（視窗 300 字元、最多 5 個、以出現次數倒數平方根加權、相鄰視窗必須合併）維持 v1.3.0 凍結值。
- 本版不改變 `--query-file` 既有的行為與其已知揭露面：該參數會讀取指定路徑的檔案並把內容原樣回顯於 `query` 欄位，此性質自 v1.3.2 起即如此。

### 未變更項

`knowledge/` 下的任何資料檔、v1.0.0 至 v1.3.3 的所有凍結雜湊與紀律、`agents/openai.yaml` 一律未改。三個 profile 的定義與檔案組成不變，仍為 49、48、9,378 檔。
