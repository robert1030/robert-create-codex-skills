---
{
  "chunk_id": "analysis_rules_02__the_extractor_7406d63db2413482",
  "source_file": "topics/analysis_rules.02.htm",
  "source_original_path": "topics/analysis_rules.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "The structure of an analysis rule"
  ],
  "heading_path": [
    "The structure of an analysis rule",
    "The structure of an analysis rule",
    "The extractor"
  ],
  "anchor": "1204446",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "7406d63db2413482",
  "level": 3
}
---

# The structure of an analysis rule > The structure of an analysis rule > The extractor

The extractor is the first line in the rule — it specifies how to extract (return) a value from the response and what to extract.

- How to extract the value appears in the Action cell. In the example, we use a regex (regular expression) extractor to extract the value. Alternatively, you can use the query extractor or the contains extractor that extracts the text string that you specify. Some extractor types can return multiple values.

- What to extract appears in the Description cell. In the example, it is the regular expression that defines the text to extract from the response.

> **Note:** Limitations

The following limitations apply for the data extracted for each execution:

- Total elements stored: A maximum of 128 extracted data items per execution.

- Bytes stored: A maximum of 128 characters of any tag or value. Any tag or value that exceeds 128 characters will be truncated.

- Array elements stored: Any extracted data item whose value is an array that exceeds 128 items will be rejected (discarded).
