---
{
  "chunk_id": "store__intro_292fce71d334c6cf",
  "source_file": "topics/popups/arules/store.html",
  "source_original_path": "topics/popups/arules/store.html",
  "toc_path": null,
  "heading_path": [
    "store.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/analysis_rules_concept.html"
  ],
  "images": [],
  "content_hash": "292fce71d334c6cf",
  "level": 0
}
---

# store.html

The store processor stores, into a variable, the data that is extracted while processing the rule .

- A response with zero values or multiple values is always stored in a list.
- You can specify whether to store a single extracted value in a scalar string or in a list. See the Always store data in a list property for recommendations when a single extracted value can contain whitespace.

Tip: You can store a value from the response to a step (say, step 12). In a later step (say, step 19), you can add a rule about a token in step 19 and compare its value to the value of the token extracted in step 12. So, for step 19, you can create an assertion like:

$value > $tokenStep12 * 2

Also, see: Analysis rules: Validating responses and setting Pass / Fail.
