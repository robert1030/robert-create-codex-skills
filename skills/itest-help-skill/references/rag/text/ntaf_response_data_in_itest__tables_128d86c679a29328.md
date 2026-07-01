---
{
  "chunk_id": "ntaf_response_data_in_itest__tables_128d86c679a29328",
  "source_file": "topics/ntaf_response_data_in_itest.htm",
  "source_original_path": "topics/ntaf_response_data_in_itest.htm",
  "toc_path": [
    "iTest Online Help",
    "Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated)",
    "NTAF Response Data in iTest"
  ],
  "heading_path": [
    "NTAF Response Data in iTest",
    "NTAF Response Data in iTest",
    "Tables"
  ],
  "anchor": "1343954",
  "context_ids": [
    "ntaf_response_data_in_itest"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/ntaf_config_and_views.05.jpg",
    "topics/images/ntaf_config_and_views.06.jpg",
    "topics/images/ntaf_config_and_views.07.jpg",
    "topics/images/ntaf_config_and_views.08.jpg",
    "topics/images/ntaf_config_and_views.09.jpg"
  ],
  "content_hash": "128d86c679a29328",
  "level": 2
}
---

# NTAF Response Data in iTest > NTAF Response Data in iTest > Tables

NTAF data that is structured as a table can have two different types of structure:



Multi-valued group

Each group contains the same set of items (attributes). In the table representation that is displayed in the Response view, the names of the items are the column headers and the item values appear as a row in the table.

In our example, the NTAF table data is contained two response groups. The items resource, connectorId, type, category, connectedResource, and connectedConnector appear in each response group. The Structure view shows the internal data structure..



Multi-valued response group with one multi-value item

You can see that this type of table has the same structure as the first type of table. Notice also that the response includes name‑value data in addition to the table data.

In this example, the NTAF table data contains three response groups — each with a multi-valued item. The first group provides the column names and contains values Port Name, Total Tx Count (Frames), Total Rx Count (Frames), and so on. Subsequent group item values define the rows. The second group contains values Port //1/1, 49079, 42414, and so on. The third group contains values Port //1/1/, 123400, 42414, and so on. The Structure view shows the internal data structure.

Here is some of the structure data for the rows of values.

![screenshot](topics/images/ntaf_config_and_views.05.jpg) <!-- image_chunk: img_797e212ceed0c037 -->

![screenshot](topics/images/ntaf_config_and_views.06.jpg) <!-- image_chunk: img_8e6a6b418730db83 -->

![screenshot](topics/images/ntaf_config_and_views.07.jpg) <!-- image_chunk: img_5ac01c755bb67781 -->

![screenshot](topics/images/ntaf_config_and_views.08.jpg) <!-- image_chunk: img_58ef1ee3ce82b7d7 -->

![screenshot](topics/images/ntaf_config_and_views.09.jpg) <!-- image_chunk: img_c3fc379427edfd8b -->
