---
{
  "chunk_id": "actions_tcl_ops__about_the_itest_interpreter_and_the_tcl__bdf22b6a29991673",
  "source_file": "topics/actions_tcl_ops.htm",
  "source_original_path": "topics/actions_tcl_ops.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "Actions that perform Tcl operations"
  ],
  "heading_path": [
    "Actions that perform Tcl operations",
    "Actions that perform Tcl operations",
    "About the iTest interpreter and the Tcl interpreters"
  ],
  "anchor": "1809385",
  "context_ids": [
    "actions_tcl_ops"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "bdf22b6a29991673",
  "level": 2
}
---

# Actions that perform Tcl operations > Actions that perform Tcl operations > About the iTest interpreter and the Tcl interpreters



Actions that operate in the iTest environment: eval, set, get

The iTest interpreter performs tasks that are useful in the iTest environment. We designed the syntax to be very much like Tcl so that the commands would be easier to understand. You can use iTest interpreter commands to perform a variety of tasks; some commands set a variable value (set), get a variable value (get), perform mathematical operations (math.abs), return information about iTest (info), or access the response to an earlier step (response).

Some iTest interpreter commands have Tcl counterparts and some do not. For example, you can use set i 0 (which uses the same syntax as Tcl) to assign the value 0 to the variable i. You can then use i as a local variable in your test case with the value $i.

You can use the iTest eval action to evaluate the iTest commands (actually, statements) that are specified in the Description cell.
