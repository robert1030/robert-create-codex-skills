---
{
  "chunk_id": "quickcalls_overview__parameters_in_quickcalls_9572105f668bc090",
  "source_file": "topics/quickcalls_overview.htm",
  "source_original_path": "topics/quickcalls_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Overview: QuickCalls",
    "Overview: QuickCalls"
  ],
  "heading_path": [
    "Overview: QuickCalls",
    "Overview: QuickCalls",
    "How QuickCalls execute",
    "Parameters in QuickCalls"
  ],
  "anchor": "1424328",
  "context_ids": [
    "quickcalls_overview"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "QuickCalls > defined"
  ],
  "related_links": [
    "procedures_advanced_users_about_procedures.htm#1399200"
  ],
  "images": [],
  "content_hash": "9572105f668bc090",
  "level": 3
}
---

# Overview: QuickCalls > Overview: QuickCalls > How QuickCalls execute > Parameters in QuickCalls

Parameters in QuickCalls are resolved as follows: Say that session A inherits from session B and both A's QuickCall library and B’s QuickCall library have parameters. If we use any QuickCall from session A (even if the QuickCall is defined in session B and given to session A by inheritance), then the parameters are resolved “down the inheritance chain” — iTest first merges the parameters from A's QuickCall Library, then merges the parameters from B's library.

> **Note:** Note For procedures, parameters are resolved differently. See Parameters

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
