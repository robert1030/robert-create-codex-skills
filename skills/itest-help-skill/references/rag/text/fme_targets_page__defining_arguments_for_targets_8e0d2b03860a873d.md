---
{
  "chunk_id": "fme_targets_page__defining_arguments_for_targets_8e0d2b03860a873d",
  "source_file": "topics/fme_targets_page.htm",
  "source_original_path": "topics/fme_targets_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Form Maps",
    "Form Map editor: Targets page"
  ],
  "heading_path": [
    "Form Map editor: Targets page",
    "Form Map editor: Targets page",
    "Defining arguments for targets"
  ],
  "anchor": "1099568",
  "context_ids": [
    "fme_targets_page"
  ],
  "index_keywords": [
    "Form Map editor",
    "Targets page",
    "on Web pages defining"
  ],
  "index_keyword_paths": [
    "Form Map editor > Targets page",
    "Targets page > Form Map editor",
    "targets > on Web pages defining"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "8e0d2b03860a873d",
  "level": 2
}
---

# Form Map editor: Targets page > Form Map editor: Targets page > Defining arguments for targets

Targets like table cells require arguments (for example, row number and column number) to identify the cell to act upon.

A table query might therefore have the following syntax: //TR[row]/TD[column]

In queries, arguments indexes are 0-based.

For example, the response for a captured target might be

//TR[3]/TD[4]

(that is, row 3, column 4).

In the form map, you might define a query that uses the following syntax: //TR{0}/TD{1}

A test case step that gets to the same cell uses the following syntax:

tableTest:tableCell("3", "4")

(that is, use the tableTest form map which has a target called tableCell with two arguments)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
