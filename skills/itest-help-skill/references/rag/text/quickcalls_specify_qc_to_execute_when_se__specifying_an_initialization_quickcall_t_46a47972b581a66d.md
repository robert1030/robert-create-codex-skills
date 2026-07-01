---
{
  "chunk_id": "quickcalls_specify_qc_to_execute_when_se__specifying_an_initialization_quickcall_t_46a47972b581a66d",
  "source_file": "topics/quickcalls_specify_qc_to_execute_when_session_starts.htm",
  "source_original_path": "topics/quickcalls_specify_qc_to_execute_when_session_starts.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "Specifying an initialization QuickCall that executes immediately when a session starts"
  ],
  "heading_path": [
    "Specifying an initialization QuickCall that executes immediately when a session starts",
    "Specifying an initialization QuickCall that executes immediately when a session starts"
  ],
  "anchor": "1403635",
  "context_ids": [
    "quickcalls_specify_qc_to_execute_when_session_starts"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "46a47972b581a66d",
  "level": 1
}
---

# Specifying an initialization QuickCall that executes immediately when a session starts > Specifying an initialization QuickCall that executes immediately when a session starts

In the definition of any topology device or session profile that refers to a QuickCall library, you can configure one of the QuickCalls in the library to execute immediately after the session starts (before any other step).

When you open a session manually (by double-clicking the session profile) the initialization QuickCall executes as soon as the connection to the session is made. The QuickCall is captured as a single step. If you save the captured session to a test case, the initialization QuickCall appears immediately after the open step for the session.



To specify an initialization QuickCall

1. From the topology device or session profile that the QuickCall library is associated with:

Open the Misc page on the Session Profile editor.

1. 2

1. In the QuickCall section, select the QuickCall from the drop-down list for the Initialization QuickCall property.

> **Caution:** CAUTION Do not use the open action (open a session) in an initialization QuickCall (or in any QuickCall).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
