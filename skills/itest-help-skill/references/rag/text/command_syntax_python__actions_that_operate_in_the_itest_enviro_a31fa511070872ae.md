---
{
  "chunk_id": "command_syntax_python__actions_that_operate_in_the_itest_enviro_a31fa511070872ae",
  "source_file": "topics/command_syntax_python.htm",
  "source_original_path": "topics/command_syntax_python.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest interpreter and Python commands"
  ],
  "heading_path": [
    "iTest interpreter and Python commands",
    "iTest interpreter and Python commands",
    "About the iTest interpreter and the Python interpreters",
    "Actions that operate in the iTest environment: eval"
  ],
  "anchor": "2038696",
  "context_ids": [
    "command_syntax_python"
  ],
  "index_keywords": [
    "char",
    "char command",
    "commands",
    "gget",
    "gget command",
    "gset",
    "gset command",
    "iTest Python interpreter",
    "iTest, Python",
    "interpreter commands",
    "param",
    "param command",
    "profile",
    "profile command",
    "response",
    "response command",
    "xpatheval (Python) command",
    "xpatheval, Python"
  ],
  "index_keyword_paths": [
    "char command",
    "command syntax > iTest Python interpreter",
    "command syntax > iTest, Python",
    "commands > char",
    "commands > gget",
    "commands > gset",
    "commands > param",
    "commands > profile",
    "commands > response",
    "commands > xpatheval, Python",
    "gget command",
    "gset command",
    "iTest > interpreter commands",
    "param command",
    "profile command",
    "response command",
    "syntax > iTest > commands",
    "xpatheval (Python) command"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a31fa511070872ae",
  "level": 3
}
---

# iTest interpreter and Python commands > iTest interpreter and Python commands > About the iTest interpreter and the Python interpreters > Actions that operate in the iTest environment: eval

The iTest interpreter performs tasks that are useful in the iTest environment. The built-in Python interpreter starts with these modules: basic math functions, random number generation, time methods, regular expressions, file reads and writes, stdio, data structure manipulations, and JSON structure processing.

In addiiton to using the iTest interpreter commands to perform a variety of tasks, you may may assign global data structures (iTest QuickCall setting a global variable), which can be read and written to by Python interpreter (a test case in Python syntax that calls the QuickCall).

Some iTest interpreter commands have Tcl/Python counterparts and some do not. For example, you can use assign i = 0 to assign the value 0 to the variable i.

You can use the iTest Python eval action to evaluate the iTest commands (actually, statements) that are specified in the Description cell.
