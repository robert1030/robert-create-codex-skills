---
{
  "chunk_id": "actions_tcl_ops__the_itest_interpreter_and_the_tcl_interp_2494295ab2901e91",
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
    "The iTest interpreter and the Tcl interpreter"
  ],
  "anchor": "1809390",
  "context_ids": [
    "actions_tcl_ops"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "2494295ab2901e91",
  "level": 2
}
---

# Actions that perform Tcl operations > Actions that perform Tcl operations > The iTest interpreter and the Tcl interpreter



Using special iTest actions to access the Tcl environment: scriptEval, scriptSet, and scriptGet

The scriptEval action uses the Tcl interpreter. If you perform set i 0, then variable i is set only in the Tcl environment — the iTest environment does not know about the variable.

> **Note:** Note Even though the variable that we just set is named i, it is a variable in the Tcl environment—a completely different and independent variable from the variable i that we earlier set in the iTest environment.

You can continue to use scriptEval to, for example, source your own Tcl script that makes use of $i. The benefit of having scriptEval is that it supports all Tcl operations.

To pass variables back and forth between the iTest interpreter and the Tcl interpreter, use scriptSet and scriptGet.

> **Note:** Note scriptEval, scriptSet, and scriptGet are not applicable in Python.



You can think of it as the “iTest world” and “Tcl world”:

- When you use the scriptEval action, you are operating in the Tcl world.

- When you use the eval action, you are operating in the iTest world.

- You use the scriptSet and scriptGet actions to peek and poke variables between the Tcl world and the iTest world.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
