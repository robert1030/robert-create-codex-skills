---
{
  "chunk_id": "procedures_advanced_users_about_procedur__parameters_in_procedures_edbcac9d36662a0e",
  "source_file": "topics/procedures_advanced_users_about_procedures.htm",
  "source_original_path": "topics/procedures_advanced_users_about_procedures.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Advanced Users: About procedures"
  ],
  "heading_path": [
    "Advanced Users: About procedures",
    "Advanced Users: About procedures",
    "Parameters",
    "Parameters in procedures"
  ],
  "anchor": "1428835",
  "context_ids": [
    "procedures_advanced_users_about_procedures"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "quickcalls_overview.htm#1465797"
  ],
  "images": [],
  "content_hash": "edbcac9d36662a0e",
  "level": 3
}
---

# Advanced Users: About procedures > Advanced Users: About procedures > Parameters > Parameters in procedures

Parameters are loaded in by call steps, so a parameter’s resolved value depends on the order in which procedures are called. For example, two procedures use the same parameters with different values: If you call a procedure from test case B and then call a procedure from test case A, then the parameter values for B are resolved first. If A is called before B, then A’s values are resolved first.

> **Note:** Note For QuickCalls, parameters are resolved differently. See How QuickCalls execute.
