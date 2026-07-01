---
{
  "chunk_id": "action_write__the_write_action_adding_text_into_the_re_07aa4206a410d960",
  "source_file": "topics/action_write.htm",
  "source_original_path": "topics/action_write.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘write’ action: Adding text into the response of a call step"
  ],
  "heading_path": [
    "The ‘write’ action: Adding text into the response of a call step",
    "The ‘write’ action: Adding text into the response of a call step"
  ],
  "anchor": "1385033",
  "context_ids": [
    "action_write"
  ],
  "index_keywords": [
    "returning from",
    "returning from procedures",
    "write",
    "write action"
  ],
  "index_keyword_paths": [
    "actions > write",
    "calls > returning from",
    "procedures > returning from",
    "returning from procedures",
    "write action"
  ],
  "related_links": [
    "#1385240",
    "action_return.htm#1385020"
  ],
  "images": [],
  "content_hash": "07aa4206a410d960",
  "level": 1
}
---

# The ‘write’ action: Adding text into the response of a call step > The ‘write’ action: Adding text into the response of a call step

> **Note:** Note The write action is supported for TCL only.

A write step adds text into the response of a call step. In a called procedure, you can use one or multiple write steps to return a response that includes response data from one or more of the procedure's steps.

If you include multiple write steps in a procedure, then you can easily add a line terminator to each response so that the resulting returned response is a multi-line string. In addition, the text that appears in the Description cell of each write step is appended to the response. See Tips on using ‘write’ and ‘return’ steps to prepare useful response data for called procedures.

Contrast write with The ‘return’ action: Returning execution from the current procedure.

> **Note:** Note A write step does not write to files or involve file I/O.
