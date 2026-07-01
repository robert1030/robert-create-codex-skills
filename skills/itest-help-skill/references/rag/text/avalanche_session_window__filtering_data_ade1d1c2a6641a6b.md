---
{
  "chunk_id": "avalanche_session_window__filtering_data_ade1d1c2a6641a6b",
  "source_file": "topics/avalanche_session_window.htm",
  "source_original_path": "topics/avalanche_session_window.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Spirent Avalanche session window"
  ],
  "heading_path": [
    "Spirent Avalanche session window",
    "Spirent Avalanche session window",
    "Data section",
    "Filtering data"
  ],
  "anchor": "1211247",
  "context_ids": [
    "avalanche_session_window"
  ],
  "index_keywords": [
    "Avalanche",
    "Spirent Avalanche",
    "interactive sessions"
  ],
  "index_keyword_paths": [
    "Avalanche > interactive sessions",
    "Spirent Avalanche > interactive sessions",
    "session windows > Spirent Avalanche",
    "sessions > Avalanche"
  ],
  "related_links": [],
  "images": [
    "topics/images/spirent_avalanche.07.jpg",
    "topics/images/spirent_avalanche.08.jpg"
  ],
  "content_hash": "ade1d1c2a6641a6b",
  "level": 4
}
---

# Spirent Avalanche session window > Spirent Avalanche session window > Data section > Filtering data

By default, one “page” of data (10 columns and 100 rows) appears at a time. You can use the row and column filter features to display a subset of the table data.

If you select a new file in the Data Files tree, iTest resets the filter settings and captures a selectTable action.

| Column filter | Specify filter text to display a subset of table columns. When you click Apply, iTest captures a filter action with the appropriate Column filter property setting. The filter is case-sensitive. The ? wildcard character matches any single character, and * matches any number of characters. Because the <space> character is used to separate column titles, you must use a wildcard character to represent a <space> character. Syntax To display two columns: <column1Title><space><column9Title> To display all columns between 1 and 9, use ... <column1Title>...<column9Title> Example Column title to filter: Desired Load (SimUsers) Use the following filter text: Desired?Load?(SimUsers) or Desired*Load*(SimUsers) |  | The filter is case-sensitive. |  | The ? wildcard character matches any single character, and * matches any number of characters. Because the <space> character is used to separate column titles, you must use a wildcard character to represent a <space> character. |
| --- | --- | --- | --- | --- | --- |
|  | The filter is case-sensitive. |  |  |  |  |
|  | The ? wildcard character matches any single character, and * matches any number of characters. Because the <space> character is used to separate column titles, you must use a wildcard character to represent a <space> character. |  |  |  |  |
| Row filter Start Count | Use the Start and Count properties to limit the display to particular rows within the table data. When you click Apply, iTest captures a filter action with the appropriate Start row and Row count property settings. Start: Specify the number of a particular row at which to start the data display. If no value is specified, then the display starts with the first row of data. Count: Specify the number of rows to display. If no value is specified, then all rows are displayed. |  |  |  |  |
| vertical paging | Because Avalanche data sets are very large, iTest displays one “page” of data at a time (10 columns by 100 rows). Use the vertical paging buttons to move one page at a time. iTest captures the appropriate paging action: pageFirst pageUp pageDown pageLast |  |  |  |  |
| horizontal paging | Because Avalanche data sets are very large, iTest displays one “page” of data at a time (10 columns by 100 rows). Use the horizontal paging buttons to move one page at a time. iTest captures the appropriate paging action: pageLeftMost pageLeft pageRight pageRightMost |  |  |  |  |
| Apply | Click Apply to apply the specified row and column filter settings to the table. iTest captures a filter action with appropriate row and column property settings. |  |  |  |  |
| Clear | Click Clear to clear the Column filter and Row filter values and display the entire table. iTest captures a clearFilter action. |  |  |  |  |
| First column is key column | Check the box to ensure that the first column of the table will always be visible when you move to another page in the table. iTest captures a lockColumn action. |  |  |  |  |

![unknown](topics/images/spirent_avalanche.07.jpg) <!-- image_chunk: img_8023aac6ca06b190 -->

![unknown](topics/images/spirent_avalanche.08.jpg) <!-- image_chunk: img_9b588fbfcedf39a1 -->
