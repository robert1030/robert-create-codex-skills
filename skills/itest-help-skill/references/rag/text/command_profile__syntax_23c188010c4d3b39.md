---
{
  "chunk_id": "command_profile__syntax_23c188010c4d3b39",
  "source_file": "topics/command_profile.htm",
  "source_original_path": "topics/command_profile.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "profile command: Accessing parameters that are defined in session profile"
  ],
  "heading_path": [
    "profile command: Accessing parameters that are defined in session profile",
    "profile command: Accessing parameters that are defined in session profile",
    "Syntax"
  ],
  "anchor": "1838574",
  "context_ids": [
    "command_profile"
  ],
  "index_keywords": [
    "defined in session profiles",
    "parameters defined in",
    "profile"
  ],
  "index_keyword_paths": [
    "field replacements > profile",
    "parameters > defined in session profiles",
    "session profiles > parameters defined in"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "23c188010c4d3b39",
  "level": 2
}
---

# profile command: Accessing parameters that are defined in session profile > profile command: Accessing parameters that are defined in session profile > Syntax

Tcl: profile session_ID parameter_name_or_query ?default_value?

Example: eval set a [profile s1 document/sessionProperties/@databaseType.inherit]

Python: profile('session', 'parameter_name_or_query', 'defaultValue')

Example: eval a = profile('s1', 'document/sessionProperties/@databaseType.inherit')

session_ID is the session ID for the step (associated with the session profile that defines the parameter). You can use . (the period character) to mean “the session ID associated with the current step”.

parameter_name_or_query is the name of the parameter or a query.

default_value: You have the option to specify a default value for the parameter if no value is found (for example, if the parameter inherits a blank Value).

> **Note:** Note The optional default_value argument is useful when you use the profile command in a session profile property and you expect to start manual sessions. Because the parameter is normally obtained from the execution context, and manual sessions do not have an execution context, the command will use the specified default value when you start a manual session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
