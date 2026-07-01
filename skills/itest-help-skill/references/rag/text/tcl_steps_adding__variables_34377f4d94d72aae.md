---
{
  "chunk_id": "tcl_steps_adding__variables_34377f4d94d72aae",
  "source_file": "topics/tcl_steps_adding.htm",
  "source_original_path": "topics/tcl_steps_adding.htm",
  "toc_path": [
    "iTest Online Help",
    "Tcl Shell Sessions",
    "Creating Tcl test case steps"
  ],
  "heading_path": [
    "Creating Tcl test case steps",
    "Creating Tcl test case steps",
    "Variables"
  ],
  "anchor": "1090340",
  "context_ids": [
    "tcl_steps_adding"
  ],
  "index_keywords": [
    "Tcl Shell",
    "adding Tcl Shell",
    "test case steps"
  ],
  "index_keyword_paths": [
    "Tcl Shell sessions > test case steps",
    "steps > adding Tcl Shell",
    "test case steps > Tcl Shell"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "34377f4d94d72aae",
  "level": 2
}
---

# Creating Tcl test case steps > Creating Tcl test case steps > Variables

iTest variables are not the same as the variables in a Tcl Shell session. iTest has its own separate data model. If you start multiple Tcl Shell sessions in a test case, then each Tcl Shell session will have variables that are independent of and separate from the variables in other sessions. This isolation of data models has several benefits. For example, this makes it possible to deal with multiple traffic generators in the same test case that would not otherwise be able to co-exist in the same Tcl interpreter because of naming or library conflicts.
