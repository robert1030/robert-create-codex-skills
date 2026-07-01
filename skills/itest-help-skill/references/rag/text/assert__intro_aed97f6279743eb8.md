---
{
  "chunk_id": "assert__intro_aed97f6279743eb8",
  "source_file": "topics/popups/arules/assert.html",
  "source_original_path": "topics/popups/arules/assert.html",
  "toc_path": null,
  "heading_path": [
    "assert.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/analysis_rules_concept.html"
  ],
  "images": [],
  "content_hash": "aed97f6279743eb8",
  "level": 0
}
---

# assert.html

The assert processor places the extracted data into an assertion and then tests the assertion. For example, the assertion $value == 42 tests whether the value is equal to 42.

If the value is equal to 42, then the assertion returns the value 1 (True). If not, then the assertion returns the value 0 (False). In the lines following the processor, you specify the actions that should occur based on the returned value:

- In the When True section, you specify the actions to take when the assertion returns 1 (True)
- In the When False section, you specify the actions to take when the assertion returns 0 (False)

Also, see: Analysis rules: Validating responses and setting Pass / Fail.
