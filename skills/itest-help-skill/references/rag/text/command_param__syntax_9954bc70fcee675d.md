---
{
  "chunk_id": "command_param__syntax_9954bc70fcee675d",
  "source_file": "topics/command_param.htm",
  "source_original_path": "topics/command_param.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "param command: Returning parameter values"
  ],
  "heading_path": [
    "param command: Returning parameter values",
    "param command: Returning parameter values",
    "Syntax"
  ],
  "anchor": "1679188",
  "context_ids": [
    "command_param"
  ],
  "index_keywords": [
    "accessing",
    "param",
    "param field replacement",
    "using in steps"
  ],
  "index_keyword_paths": [
    "field replacements > param",
    "param field replacement",
    "parameters > accessing",
    "parameters > using in steps"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9954bc70fcee675d",
  "level": 2
}
---

# param command: Returning parameter values > param command: Returning parameter values > Syntax

Tcl: param parameterNameOrQuery ?defaultValue?

Python: param('parameterNameOrQuery', 'defaultValue')

parameterNameOrQuery is the name of the parameter or of a query. If the parameter is a child of a node in a structure, then use parentNode/paramName

defaultValue: You have the option to specify a default value for the parameter if no value is found (for example, if the parameter inherits a blank Value).

> **Note:** Note The optional defaultValue argument is useful when you use the param command in a session profile property and you expect to start manual sessions. Because the parameter is normally obtained from the execution context, and manual sessions do not have an execution context, the command will use the specified default value when you start a manual session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
