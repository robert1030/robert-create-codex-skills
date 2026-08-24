# HTML／XML 工作規格

本文件是 `SKILL.md` 的按需細節。它定義 HTML 與 XML 的工作紀律、路由策略、流程、工具、限制與驗證邊界。它不改變既有 chunk、metadata、Markdown 或 ZIP 交付契約。

## 共同決策邊界

- 這兩個 adapter 只負責來源抽取、結構保留與 locator。共用切片層仍負責 `chunk_size=256`、`overlap=40`、`min_len=30`、摘要、metadata、品質狀態與兩種交付檔名。
- 產物可供 RAG ingestion 使用，但 `quality_status: PASS` 只表示結構與 deterministic checks 通過，不代表已完成 embedding、retrieval、reranking 或 source-bound accuracy benchmark。
- 不引入模型式 HTML pruning、XML embedding、BM25、reranking 或外部服務。這些屬於下游或另一個版本的範圍。
- 所有來源預設是本機檔案。skill 不自行抓取 URL，不執行 HTML script，不解析外部 XML 資源。

## HTML

### 模式選擇

| 模式 | Adapter | 保留目標 | 不保證 |
|---|---|---|---|
| `document` | MarkItDown | 文件標題、段落、清單、表格、連結與程式碼的 Markdown 語意 | 像素級版面、完整 DOM 屬性、圖片內文字 |
| `article` | Trafilatura | 文章主文、標題、段落、清單、引用與表格 | 導覽列、側欄、完整 DOM、技術標記與非文章內容 |

使用 `document` 的理由是保留技術文件或整份 HTML 的內容。只有使用者明確指定文章型主文抽取時才使用 `article`，因為 boilerplate removal 可能同時移除使用者需要的技術內容。

### 編碼紀律

1. 先檢查檔案大小，不超過 `_MAX_HTML_BYTES`。
2. 優先使用 UTF-32、UTF-16 或 UTF-8 BOM。
3. 沒有 BOM 時讀取檔案前段的 `meta charset` 宣告。
4. 沒有宣告時只接受嚴格 UTF-8。
5. 解碼失敗或產生 U+FFFD 時停止，不使用 `errors="replace"`。

這個策略可避免抽取層把實際遺失的字元偽裝成可用文字。它不會推測未宣告的 Big5、Shift-JIS 或其他本地編碼。這些來源應補上正確 charset 或先轉為 UTF-8。

### Locator 與 block

MarkItDown 與 Trafilatura 都先輸出 Markdown，再由 `_markdown_blocks()` 建立 normalized blocks：

- heading：保留 heading stack 作為 `section_title`。
- table：保留 Markdown table block。
- list：保留連續清單文字。
- paragraph：將同一段的轉換行合併為正文。
- `source_locator` 使用 `converted-line:NNNN` 或 `converted-line:NNNN-NNNN`。

`converted-line` 是轉換後 Markdown 的行範圍，不是原始 HTML DOM 行號。它提供可重現的轉換定位，不能被描述成瀏覽器或 DOM 的精確座標。

### HTML 安全與品質限制

- HTML 只從本機路徑讀取，URL、script 執行與外部資源抓取不屬於本 adapter。
- MarkItDown 的安全範圍是文字分析，不是高保真轉檔。輸入應限制在使用者信任的本機檔案，並以最低必要權限執行。
- Trafilatura 的文章模式是選擇性抽取，不適合 XML-like markup、完整 API 文件或需要每個屬性的情境。
- 若轉換結果為空，adapter 會停止，不輸出空切片。
- 抽取完成後，quality gate 仍檢查空正文、locator、replacement character、Private Use Area 與品質錨點。預設異常標為 `REVIEW` 並仍交付原有兩種檔案，`--strict_quality` 才阻斷品質警告。

## XML

### 安全 parser 契約

safe 路由使用 `lxml.etree.XMLParser`，固定設定：

```text
resolve_entities=False
no_network=True
load_dtd=False
dtd_validation=False
recover=False
huge_tree=False
```

在 parser 前另行拒絕 `DOCTYPE` 與 `ENTITY` 宣告。這是針對本地 RAG ingestion 的保守邊界，避免外部 DTD、外部 entity、網路取檔或修復模式改寫來源。解析失敗時回報錯誤，不以 `recover=True` 產生不完整結果。

### 資源限制

| 限制 | 預設值 | 超過時行為 |
|---|---:|---|
| XML 檔案大小 | 10 MiB | 停止 |
| XML 元素數 | 100,000 | 停止 |
| XML 巢狀深度 | 128 層 | 停止 |

這些是執行資源與拒絕服務風險的工程限制，不是任何單一論文宣稱的通用安全閾值。若來源合法但超過限制，應先分割來源或另行評估，不應把限制錯誤解讀成 XML 格式本身不支援。

### Namespace、順序與 mixed content

- 無 namespace 的 locator 維持 `/catalog/book[1]`，保留前版相容性。
- 有 namespace 的 tag 使用 Clark notation，例如 `/{urn:example}catalog/{urn:example}book[1]`。這避免不同 namespace 的同名元素被誤合併。
- 同名兄弟只在 namespace 與 local name 都相同時計算 `[1]`、`[2]` 索引。
- 屬性保留在元素 block 中。namespaced attribute 使用 `@{uri}local=value`，無 namespace attribute 使用 `@local=value`。
- 元素的直接文字與 child tail 形成 mixed-content context，使用 `itertext()` 依原始順序保留內容；子元素另外建立自己的 locator block。父子 block 的重疊是結構上下文，不是資料遺失。
- 沒有屬性、直接文字或 mixed-content context 的純容器元素不單獨產生空 block，子元素仍會被遍歷。

### XML fallback

`--xml_backend markitdown` 只在使用者明確指定時呼叫 MarkItDown。它適合需要一般文字分析的 XML，不保證 namespace、屬性、元素順序或 XML locator 的完整保留。安全預設永遠是 lxml-safe。

## 驗證矩陣

| 層級 | HTML | XML |
|---|---|---|
| 純邏輯測試 | charset、replacement character、mode routing、Markdown blocks | namespace locator、attribute、mixed content、sibling index、limits |
| 負向測試 | 無法嚴格解碼必須非 0／例外 | DOCTYPE／ENTITY、超過大小／元素數／深度必須停止 |
| runtime fixture | document 與 article，各產生 `.md`／`.zip` | namespaced mixed XML 產生 `.md`／`.zip` |
| 交付驗證 | `validate_output.py`、ZIP artifact binding | 同左，另確認 locator 與安全限制 |

## 證據與批判性限制

目前可讀取的主要參考包括：

- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)：支援 HTML 與文字型 XML 的 Markdown 轉換，並明確把用途定位在文字分析，不是高保真排版複製。
- [Trafilatura](https://github.com/adbar/trafilatura)：主文抽取、標題、段落、清單、連結與表格輸出。其文章模式不能直接支持完整 DOM 保留的結論。
- [HtmlRAG](https://arxiv.org/html/2411.02959)：說明 HTML 結構在純文字化時可能遺失，並研究結構壓縮與後續 pruning。它支持保留結構的方向，但不直接證明本 adapter 或任何特定套件的轉錄準確率。
- [OpenAI Knowledge Retrieval](https://github.com/openai/openai-knowledge-retrieval)：展示 heading、recursive、hybrid 與 XML-aware chunking 的工程路線。它是設計參考，不是本 skill 的 runtime 相依，也不會把下游 retrieval 演算法混入抽取 adapter。

批判性檢查結論如下：上述主張的證據主要是官方 README、原始論文與本地 fixture 行為，足以支持「採用語意保留、嚴格解碼與安全 XML parser 作為工程策略」，不足以支持「一定改善所有來源的 RAG 召回率」或「任何固定工具在所有 HTML／XML 上都較佳」。沒有把相關性當作因果性，也沒有把 downstream retrieval 研究當成 extraction runtime 證據。研究資料的限制是來源類型、語言、編碼、namespace 複雜度與樣本規模仍有限，未完成跨語料 benchmark 或 retrieval GOLDEN 評估。若缺少 charset、原始 DOM 對照或完整 XML schema，品質判斷只能保持 `REVIEW` 或 `PARTIAL`。

依目前可讀取內容，未發現重大內部矛盾；但這不代表其所有主張都已經外部驗證。
