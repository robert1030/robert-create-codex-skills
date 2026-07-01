---
{
  "chunk_id": "callprocedure__intro_91d836eacbcf75bc",
  "source_file": "popups/callProcedure.html",
  "source_original_path": "popups/callProcedure.html",
  "toc_path": null,
  "heading_path": [
    "callProcedure.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/procedure_calling.html",
    "help::/com.fnfr.svt.help/topics/action_call.html"
  ],
  "images": [],
  "content_hash": "91d836eacbcf75bc",
  "level": 0
}
---

# callProcedure.html

You can use a call step or CallProcedure action to execute a local or foreign procedure. You cannot use the run action to execute a procedure. See Calling a procedure in a test case step or in a property setting.

See also call action definitions in The �call� action: Calling a procedure.

For call steps or CallProcedure actions, the Command cell contains the target procedure name and any arguments and argument values. Procedures can call procedures in a nested fashion.

Procedure call syntax procedureName [-namedArg1 arg1Value -namedArg2 arg2Value ...] [numberedArg1 numberedArg2 ...]

- Arguments are optional
- Any named arguments must appear before any numbered arguments
