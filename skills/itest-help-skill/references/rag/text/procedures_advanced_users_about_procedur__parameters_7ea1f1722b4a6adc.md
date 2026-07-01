---
{
  "chunk_id": "procedures_advanced_users_about_procedur__parameters_7ea1f1722b4a6adc",
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
    "Parameters"
  ],
  "anchor": "1399200",
  "context_ids": [
    "procedures_advanced_users_about_procedures"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "7ea1f1722b4a6adc",
  "level": 2
}
---

# Advanced Users: About procedures > Advanced Users: About procedures > Parameters

Parameters are distinct from variables. Parameters are loaded from parameter files, test cases, or session profiles and are “read-only”. Parameters are available to any procedure at any level. One does not have to pass parameters to a procedure.

While parameter values are accessible using the param command, the command does not allow you to set values. Even something like call myProc -arg1 [param myParam] is not used, as iTest is only passing the value — you are not touching the original parameter. In addition, there is no need to pass parameters to a procedure unless you intend the procedure to take a variable value as well, because the procedure can access the parameter myParam using [param myParam] (Tcl) or [param(‘myParam’)] (Python) in its context.
