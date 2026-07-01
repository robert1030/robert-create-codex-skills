---
{
  "chunk_id": "rme_table_page__locating_columns_32fc72d30b38dd35",
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
    "Locating Columns"
  ],
  "anchor": "1106740",
  "context_ids": [
    "rme_table_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_6.2.jpg",
    "topics/images/response_mapping_4.3.jpg"
  ],
  "content_hash": "32fc72d30b38dd35",
  "level": 2
}
---

# Response Map editor: Table Map page > Response Map editor: Table Map page > Locating Columns

On this page, you specify how to recognize a new column of data in the table. We’ll refer to this example table:

There are two methods for determining column boundaries:

- Delimited: Use whitespace characters (tabs and/or spaces) or some other specified character (for example, commas) to delimit column boundaries

| Whitespace | (default) A new column starts upon encountering a space or tab character. Whitespace is the most flexible setting, as it accepts tabs or spaces for separating the data entries. Our example table seems to use whitespace. |
| --- | --- |
| Tab | A new column starts upon encountering a tab character only. Note: If you specify Tab and the table actually uses a mixture of tabs and spaces as delimiters, then the mapper will map any space characters that appear between columns as a part of the token data — probably not what you want. |
| Comma/Colon | A new column starts upon encountering a comma/colon character only. |
| Custom | If you specify Custom, then specify the delimiter string in the Other delimiter text box. |
| Regex | If you specify Regex, then specify regular expression delimiter string in the Other delimiter text box. |

- Positional: Apply strict column widths based on character counts (for example, the first column is 8 characters wide, the second column is 14 characters wide, and so on).

While you work on a Table response map that uses character counts to determine column boundaries (the Positional setting), the Response view displays column markers that indicate the end of each column of data. To change the location of a column boundary, drag the marker to place it after the last character in the column, as shown in the example:

For our example table, it seems that we could use either method. Follow these suggestions:

> **Tip:** Tips The Delimited setting using whitespace is typically the easiest setting to apply, as it accepts tabs or spaces for separating the data entries. The example table can be mapped using whitespace.If you expect blank cells in the table, then you should use strict column widths (Positional) to ensure that the mapper does not miss a column boundary. (Because the actual content of a blank cell is whitespace, if you had selected to Delimited, the mapper would incorrectly interpret the space as a column boundary).The Positional setting is also useful when you expect space characters within a singe value in a cell.

![screenshot](topics/images/response_mapping_6.2.jpg) <!-- image_chunk: img_4fc5b15fb692ec45 -->

![screenshot](topics/images/response_mapping_4.3.jpg) <!-- image_chunk: img_1fbb63fa0af8cbf8 -->
