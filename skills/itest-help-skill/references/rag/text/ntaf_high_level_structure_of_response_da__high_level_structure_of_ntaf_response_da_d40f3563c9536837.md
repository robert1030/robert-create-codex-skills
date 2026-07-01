---
{
  "chunk_id": "ntaf_high_level_structure_of_response_da__high_level_structure_of_ntaf_response_da_d40f3563c9536837",
  "source_file": "topics/ntaf_high_level_structure_of_response_data.htm",
  "source_original_path": "topics/ntaf_high_level_structure_of_response_data.htm",
  "toc_path": [
    "iTest Online Help",
    "Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated)",
    "High Level Structure of NTAF response data"
  ],
  "heading_path": [
    "High Level Structure of NTAF response data",
    "High Level Structure of NTAF response data"
  ],
  "anchor": "1344240",
  "context_ids": [
    "ntaf_high_level_structure_of_response_data"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/ntaf_config_and_views_7.1.jpg"
  ],
  "content_hash": "d40f3563c9536837",
  "level": 1
}
---

# High Level Structure of NTAF response data > High Level Structure of NTAF response data

NTAF structure data has two major sections.

> **Note:** Note Spirent recommends that you use the ntafResponse structure for group and item data for the reasons given in this section.



response

The response section was developed first and was available in the earliest versions of iTest that supported NTAF. It organizes data by XML element tag. While this strategy captures all the data, it can be hard to use because many tags in NTAF data are the same (like item in our example, or group). This structure is retained for compatibility with older versions.



ntafResponse

Later versions of iTest support the ntafResponse structure, which is based on group and item names. Notice how the elements of ntafResponse are named using the names contained in the items. This strategy better corresponds to NTAF structure and is much easier to navigate. By default, iTest queries are designed to refer to the ntafResponse structure.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/ntaf_config_and_views_7.1.jpg) <!-- image_chunk: img_10f8d2f26ff55a44 -->
