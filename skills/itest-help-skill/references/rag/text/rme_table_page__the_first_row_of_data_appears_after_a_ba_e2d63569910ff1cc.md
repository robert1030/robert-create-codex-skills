---
{
  "chunk_id": "rme_table_page__the_first_row_of_data_appears_after_a_ba_e2d63569910ff1cc",
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
    "The first row of data appears after a banner"
  ],
  "anchor": "1106676",
  "context_ids": [
    "rme_table_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "e2d63569910ff1cc",
  "level": 2
}
---

# Response Map editor: Table Map page > Response Map editor: Table Map page > The first row of data appears after a banner

If the table always starts with a recognizable line of text (typically the title of the table or a row of column headings), then you can specify this banner text as the unique identifier for the beginning of the table. Our example table includes a unique line (the headings Vlan Port, and so on) followed by an additional line (the ---+--- characters)

| Banner contains | Type or paste all or part of the banner text into this box. In our example, we would paste the following text: Vlan Port Oper Status Path Cost Role |
| --- | --- |
| Match banner using | CaseInsensitive: Match the footer text without regard to type case. CaseSensitive: Match the footer text only if all type case matches also. Regex: Match potential footer text against the regular expression that appears in the Banner contains text box. Wildcard: The * character in the Banner contains value represents any number of characters. The ? character in the Banner contains value represents a single character. |
| Number of additional lines in banner | Specify the number of lines that appear after the banner line. In our example, one additional line appears after the banner (the row of ---+--- characters), so we enter 1. |
