---
{
  "chunk_id": "showtable__intro_f496c6f839fdc938",
  "source_file": "topics/popups/showtable.html",
  "source_original_path": "topics/popups/showtable.html",
  "toc_path": null,
  "heading_path": [
    "showtable.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/web_test_cases_creating.html"
  ],
  "images": [],
  "content_hash": "f496c6f839fdc938",
  "level": 0
}
---

# showtable.html

| Action Name | Target | Command | Description |
| --- | --- | --- | --- |
| showTable | Required | Optional | For the specified table, return all table contents in table form. Columns are delimited using the tab character. The Command property specifies the ranges of rows and columns to return. Use the following format. (Index numbers are 1-based -- the first row is number 1, and so on.) startingRow startingColumn numberOfRows numberOfColumns If Command is empty, the whole table is displayed. Example Action Target Command showTable portTable 1,1,6,3 Response Only text is returned, images and merged cells in the source are ignored. If the specified number of rows and columns exceeds the limits of the data, then, the whole table is displayed. Indexes for row and column start at 1. |
| Action | Target | Command |  |
| showTable | portTable | 1,1,6,3 |  |

For details, see the online help: Creating Web test case steps.
