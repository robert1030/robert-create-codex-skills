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
