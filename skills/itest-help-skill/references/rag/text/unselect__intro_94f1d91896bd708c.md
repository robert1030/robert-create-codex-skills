---
{
  "chunk_id": "unselect__intro_94f1d91896bd708c",
  "source_file": "popups/unselect.html",
  "source_original_path": "popups/unselect.html",
  "toc_path": null,
  "heading_path": [
    "unselect.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/web_test_cases_creating.html"
  ],
  "images": [],
  "content_hash": "94f1d91896bd708c",
  "level": 0
}
---

# unselect.html

| Action Name | Target | Command property value | Description |
| --- | --- | --- | --- |
| unselect | Required | Not Required | Unselect specified list items. You can specify the item by name, by alias, or by index. Index is 0-based. The Command property specifies the set of labels to unselect. Example Action Target Command Unselect ListOfOptions index=2,4,7,9 Unselect ListOfOptions index=4:9 (4:9 or 4,9 represent indexes 4 though 9, inclusive) Special cases To select content that includes the equal, colon, or comma characters (= : ,), use the backslash character \ to escape the character. For example, to select "23:18", use "23\:18". ? marks a single character in the content as wild. * marks the remainder of the string as wild. |

For details, see the online help: Creating Web test case steps.
