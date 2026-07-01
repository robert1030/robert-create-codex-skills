---
{
  "chunk_id": "quickcalls_overview__how_quickcalls_execute_f39d1b8c3d672e51",
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
    "How QuickCalls execute"
  ],
  "anchor": "1465797",
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
    "procedures_how_to_execute.htm#1518702"
  ],
  "images": [],
  "content_hash": "f39d1b8c3d672e51",
  "level": 2
}
---

# Overview: QuickCalls > Overview: QuickCalls > How QuickCalls execute

QuickCalls are procedures and they execute like procedures. iTest captures each QuickCall execution as a single high-level action (just like a keyword). So, when you save a captured manual session as a test case, each QuickCall is added as a single step. The resulting test case is much more readable and understandable than it would have been if each step that makes up the QuickCall had been listed.

iTest does not enforce timeout settings for any call step associated with a QuickCall.

In test reports, you can expand a QuickCall to view all of the steps that executed.

For other details, see How procedures execute.

> **Note:** Note If a call step in a child test case B (begun by a run step in a grandparent test case A) calls grandchild test case C: The called test case C will use the shared session from test case A in its open step if the Session ID in C is same as the Session ID in A. If you do not want to use the shared session, then change the Session ID in C to be different from the Session ID in A.
