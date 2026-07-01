---
{
  "chunk_id": "tclsh_session_editor_concept__variables_3113cfa43edb3f5a",
  "source_file": "topics/tclsh_session_editor_concept.htm",
  "source_original_path": "topics/tclsh_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Tcl Shell Sessions",
    "Tcl Shell session window"
  ],
  "heading_path": [
    "Tcl Shell session window",
    "Tcl Shell session window",
    "Variables"
  ],
  "anchor": "1091501",
  "context_ids": [
    "tclsh_session_editor_concept"
  ],
  "index_keywords": [
    "Tcl Shell",
    "session window"
  ],
  "index_keyword_paths": [
    "Tcl Shell sessions > session window",
    "session windows > Tcl Shell"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3113cfa43edb3f5a",
  "level": 2
}
---

# Tcl Shell session window > Tcl Shell session window > Variables

iTest variables are not the same as the variables in a Tcl Shell session. iTest has its own separate data model. If you start multiple Tcl Shell sessions in a test case, then each Tcl Shell session will have variables that are independent of and separate from the variables in other sessions. This isolation of data models has several benefits. For example, this makes it possible to deal with multiple traffic generators in the same test case that would not otherwise be able to co-exist in the same Tcl interpreter because of naming or library conflicts.
