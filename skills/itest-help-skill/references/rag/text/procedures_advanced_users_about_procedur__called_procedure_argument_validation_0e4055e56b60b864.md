---
{
  "chunk_id": "procedures_advanced_users_about_procedur__called_procedure_argument_validation_0e4055e56b60b864",
  "source_file": "topics/procedures_advanced_users_about_procedures.htm",
  "source_original_path": "topics/procedures_advanced_users_about_procedures.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Advanced Users: About procedures"
  ],
  "heading_path": [
    "Advanced Users: About procedures",
    "Advanced Users: About procedures",
    "Called procedure argument validation"
  ],
  "anchor": "1429040",
  "context_ids": [
    "procedures_advanced_users_about_procedures"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "procedure_call_wizard.htm#1291944"
  ],
  "images": [
    "topics/images/proc_python_tcl_call_syntax.png"
  ],
  "content_hash": "0e4055e56b60b864",
  "level": 2
}
---

# Advanced Users: About procedures > Advanced Users: About procedures > Called procedure argument validation

Many languages validate arguments passed to procedures. But many scripting languages do not — you discover any errors at runtime. iTest does not validate any of the arguments passed to a call procedure statement. iTest is designed for procedures to have very loose, variable arguments syntax. Typical call syntax (Tcl and Python):

call procName -myArg mouse -myOtherArg rabbit cat dog

You can see that we are passing two named arguments and two unnamed arguments (cat and dog). All of the arguments are optional. The arguments become stack variables in the context of the called procedure. If you do not call the procedure with the correct arguments, your variable access in the called procedure will produce a run-time error.

Use the Procedure Call wizard to help you to avoid issue of not finding errors until run-time. See Creating a ‘call’ step using the Procedure Call wizard.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/proc_python_tcl_call_syntax.png) <!-- image_chunk: img_49101e73230a3cc3 -->
