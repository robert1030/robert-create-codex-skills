# Dense-text extraction、獨立驗證與 Retrieval 契約

## 適用範圍

當 PDF 掃描頁是字典、教材、表格、名錄、規格或其他高密度文字頁，且任務要求單字、音標、欄位、例句或正文可以實際搜尋時，使用本契約。`semantic_summary` 只適合概念檢索，不能滿足 dense-text corpus。

## 角色分離

1. Main Agent 修改 Skill、測試與契約，不生產 RAG，也不驗證自己的產物。
2. Extraction Agent 查看 `visual-review-request.json` 指定的每張原頁，只建立 `REVIEW.json`。
3. Validation Agent 從原 PDF 與頁面 asset 重新核對全部單元，只建立 `VALIDATION.json` 與 retrieval `GOLDEN.json`。
4. RAG Runner 在兩份 sidecar 通過後執行 Chunker 與所有 Validator。
5. Main Agent 只整合原始命令、退出碼、Hash、計數、失敗與限制。

Extraction Agent 與 Validation Agent 必須不同。欄位中的方法名稱不能取代實際角色分離。

## Extraction sidecar

`REVIEW.json` 使用：

```json
{
  "schema": "multiformat-rag-chunker.visual-semantics.v2",
  "input_sha256": "64 位小寫十六進位",
  "reviews": [
    {
      "reference": "pages/page-001.png",
      "source_asset_sha256": "64 位小寫十六進位",
      "review_method": "native_visual_nonverbatim",
      "review_mode": "dense_text",
      "required_review_mode": "dense_text",
      "density_metrics": {},
      "text_units": [
        {
          "unit_id": "p001-u001",
          "unit_type": "lexical_entry",
          "reading_order": 1,
          "text": "abandon /əˈbændən/ v. 放棄；He abandoned the car.",
          "fields": {
            "headword": "abandon",
            "ipa": "/əˈbændən/",
            "part_of_speech": "v.",
            "definition_zh": "放棄",
            "example_en": "He abandoned the car."
          },
          "uncertain_spans": []
        }
      ]
    }
  ]
}
```

`unit_type` 只接受 `heading`、`lexical_entry`、`phrase`、`example`、`paragraph`、`footer`、`other`。`fields` 只接受 `headword`、`ipa`、`part_of_speech`、`definition_zh`、`phrase`、`example_en`、`example_zh`、`label`、`body`。每個欄位值必須實際存在於同一單元的 `text`，確保欄位不是無法搜尋的旁路 metadata。

同頁 unit ID 必須唯一，reading order 必須從 1 連續遞增。`uncertain_spans` 非空表示仍有未解問題；Producer 必須拒絕 admission，不得把不確定內容偽裝成成功正文。

## Independent validation sidecar

`VALIDATION.json` 使用：

```json
{
  "schema": "multiformat-rag-chunker.visual-text-validation.v1",
  "input_sha256": "64 位小寫十六進位",
  "extraction_manifest_sha256": "REVIEW.json 的 SHA-256",
  "validations": [
    {
      "reference": "pages/page-001.png",
      "source_asset_sha256": "64 位小寫十六進位",
      "validation_method": "independent_native_visual",
      "status": "passed",
      "checked_unit_ids": ["p001-u001"],
      "missing_units": [],
      "unexpected_units": [],
      "mismatched_units": [],
      "reading_order_status": "passed",
      "mode_appropriate": true
    }
  ]
}
```

`checked_unit_ids` 必須與該頁 extraction units 依序完全相同。missing、unexpected、mismatched 任一非空，reading order 非 passed，或 mode appropriate 非 true，都不得建立成功 `llm_visual_text`。

## RAG admission 與輸出

通過時，每個 text unit 建立一個既有 `paragraph` 或 `heading` Block：

- `content_origin` 為 `llm_visual_text`。
- `required` 與 `status` 分別為 true、`success`。
- `verbatim` 固定為 false。
- Metadata 保存 reference、asset Hash、unit ID、unit type、reading order、fields、density metrics 與兩份 sidecar evidence。

這些 Block 可以依 Heading 與 Token 邏輯組成 Chunk，但單一 Block 不得被拆開，且每個非 overlap Block 只能精確映射一次。

## Retrieval golden

`GOLDEN.json` 使用：

```json
{
  "schema": "multiformat-rag-chunker.dense-retrieval-golden.v1",
  "input_sha256": "64 位小寫十六進位",
  "extraction_manifest_sha256": "REVIEW.json 的 SHA-256",
  "queries": [
    {
      "id": "headword-abandon",
      "query_type": "headword",
      "query": "abandon",
      "expected_unit_id": "p001-u001",
      "expected_reference": "pages/page-001.png",
      "expected_page": 1,
      "expected_anchor": "abandon /əˈbændən/",
      "top_k": 1
    }
  ]
}
```

`headword` 的 `top_k` 固定為 1；`definition`、`example` 與非詞彙頁使用的 `content` 固定為 3。Golden 必須涵蓋每個必要頁面，並在來源實際具有該類內容時涵蓋 headword、definition 與 example 三種詞彙 query type。

成功門檻全部為 1.0：critical anchor preservation、headword Recall@1、definition Recall@3、example Recall@3、citation page accuracy。缺少某種來源內容時該指標可為 `null`；不得用 `null` 冒充 1.0。

## 驗證命令

```bash
python scripts/rag_chunker.py INPUT.pdf -o OUTPUT --visual-semantics REVIEW.json --visual-text-validation VALIDATION.json --require-original-binary
python scripts/validate_output.py OUTPUT --json
python scripts/validate_against_source.py INPUT.pdf OUTPUT_SOURCE_DIR --require-complete --json
python scripts/validate_dense_retrieval.py OUTPUT_SOURCE_DIR --golden GOLDEN.json
```

任一命令退出碼非 0，都不得宣稱 dense-text 完整成功。

## 證據邊界

合成 Fixture 的文字由測試建立，可作為確定 ground truth。真實 PDF 若沒有作者提供的逐字答案，只能宣稱所有必要頁面已經 Extraction Agent 轉錄、Validation Agent 全量核對，且本次 golden retrieval 全數通過。這不是數學意義的零錯誤保證。

v1.2.3-dev-r1 不改變本契約。合法的 extraction 與 validation sidecar 本身是已實際使用原生 LLM 視覺的 hash-bound evidence，對應 routing event 必須是 `native_llm_multimodal`、`llm_visual_attempted: true`、`ocr_admitted: false`。OCR 不得替代 dense-text 雙 Agent admission。
