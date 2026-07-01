---
{
  "chunk_id": "action_call__example_ce1422d15e6f3565",
  "source_file": "topics/action_call.htm",
  "source_original_path": "topics/action_call.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘call’ action: Calling a procedure"
  ],
  "heading_path": [
    "The ‘call’ action: Calling a procedure",
    "The ‘call’ action: Calling a procedure",
    "About arguments in procedure calls",
    "Example:"
  ],
  "anchor": "1385004",
  "context_ids": [
    "action_call"
  ],
  "index_keywords": [
    "call",
    "call action",
    "calling",
    "calling procedures"
  ],
  "index_keyword_paths": [
    "actions > call",
    "call action",
    "calling procedures",
    "procedures > calling"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ce1422d15e6f3565",
  "level": 3
}
---

# The ‘call’ action: Calling a procedure > The ‘call’ action: Calling a procedure > About arguments in procedure calls > Example:

This example call to the ExercisePorts procedure includes two named arguments and one numbered argument. Here is the form of the call:

procedureName -slot slotNumber -port portNumber numberOfRepetitions (Tcl)

myProc -myArg slotNum1 -myOtherArg [param('myParam')] slotNum2 slotNum3 (Python)

Here is an actual call: The value of the port argument is determined dynamically by the return value of a param command.

ExercisePorts -slot 3 -port [param portInUse] 75

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
