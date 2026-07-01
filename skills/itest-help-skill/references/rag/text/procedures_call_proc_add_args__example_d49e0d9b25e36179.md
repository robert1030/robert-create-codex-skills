---
{
  "chunk_id": "procedures_call_proc_add_args__example_d49e0d9b25e36179",
  "source_file": "topics/procedures_call_proc_add_args.htm",
  "source_original_path": "topics/procedures_call_proc_add_args.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Creating a procedure ‘call’ step using in-line editing"
  ],
  "heading_path": [
    "Creating a procedure ‘call’ step using in-line editing",
    "Creating a procedure ‘call’ step using in-line editing",
    "Example"
  ],
  "anchor": "1401343",
  "context_ids": [
    "procedures_call_proc_add_args"
  ],
  "index_keywords": [
    "adding to a procedure call"
  ],
  "index_keyword_paths": [
    "arguments > adding to a procedure call"
  ],
  "related_links": [
    "action_call.htm#1384995"
  ],
  "images": [],
  "content_hash": "d49e0d9b25e36179",
  "level": 2
}
---

# Creating a procedure ‘call’ step using in-line editing > Creating a procedure ‘call’ step using in-line editing > Example

This example call to the ExercisePorts procedure includes two named arguments and one numbered argument. Here is the form of the procedure call:

procedureName -slot slotNumber -port portNumber numberOfRepetitions (Tcl)

myProc -myArg slotNum1 -myOtherArg [param('myParam')] slotNum2 slotNum3 (Python)

Here is the actual text that appears in the Description cell for the call step (the value of the port argument is determined dynamically by the return value of a param command).

ExercisePorts -slot 3 -port [param portInUse] 75

For details, see About arguments in procedure calls.
