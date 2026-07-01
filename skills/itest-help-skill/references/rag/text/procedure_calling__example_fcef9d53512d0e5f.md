---
{
  "chunk_id": "procedure_calling__example_fcef9d53512d0e5f",
  "source_file": "topics/procedure_calling.htm",
  "source_original_path": "topics/procedure_calling.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Calling a procedure in a test case step or in a property setting"
  ],
  "heading_path": [
    "Calling a procedure in a test case step or in a property setting",
    "Calling a procedure in a test case step or in a property setting",
    "Example"
  ],
  "anchor": "1401079",
  "context_ids": [
    "procedure_calling"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "action_call.htm#1384995"
  ],
  "images": [
    "topics/images/proc_python_calling_proc_2namedNumbered.png"
  ],
  "content_hash": "fcef9d53512d0e5f",
  "level": 2
}
---

# Calling a procedure in a test case step or in a property setting > Calling a procedure in a test case step or in a property setting > Example

This example call to the ExercisePorts procedure includes two named arguments and one numbered argument. Here is the form of the procedure call:

ExercisePorts -slot slotNumber -port portNumber numberOfRepetitions

Here is the actual text that appears in the Description cell for the call step (the value of the port argument is determined dynamically by the return value of a param command).

ExercisePorts -slot 3 -port [param portInUse] 75

For details, see About arguments in procedure calls.

Python example:

![screenshot](topics/images/proc_python_calling_proc_2namedNumbered.png) <!-- image_chunk: img_7ec302dbbb69966b -->
