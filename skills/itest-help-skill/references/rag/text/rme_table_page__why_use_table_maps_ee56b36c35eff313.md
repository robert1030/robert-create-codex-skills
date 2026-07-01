---
{
  "chunk_id": "rme_table_page__why_use_table_maps_ee56b36c35eff313",
  "source_file": "topics/rme_table_page.htm",
  "source_original_path": "topics/rme_table_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Table Map page"
  ],
  "heading_path": [
    "Response Map editor: Table Map page",
    "Response Map editor: Table Map page",
    "Why use Table maps?"
  ],
  "anchor": "1106635",
  "context_ids": [
    "rme_table_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences_response_map.htm#1318143"
  ],
  "images": [],
  "content_hash": "ee56b36c35eff313",
  "level": 2
}
---

# Response Map editor: Table Map page > Response Map editor: Table Map page > Why use Table maps?

The goal for mapping a table is: For a particular response that includes data in a table format (even if there are other tables or other non-table data in the response), to be able to extract a token value from any cell in a table (some cells might even contain more than one token value).

- You'll use the Table Map editor for each type of table to specify:

- The method for identifying the beginning and end of the data in the table

- The method for delimiting columns: for example, by tab characters or by fixed column widths

- Whether the table can expand/contract with additional columns to cover additional data

- The minimum and maximum number of instances of this type of table to expect in a response

- Once you have defined the properties for the table, you will specify properties for each column in the table:

- The width of the column (for the case that the table boundaries are based on column width)

- A default value for the data in the cell

- Methods for dealing with non-standard, too wide, or blank contents

> **Tip:** Tip You can set preferences for table mapping. See Setting preferences for response mapping.
