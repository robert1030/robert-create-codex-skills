---
{
  "chunk_id": "commands_itest_interpreter__itest_interpreter_commands_01b89a20e5cd38de",
  "source_file": "topics/commands_itest_interpreter.htm",
  "source_original_path": "topics/commands_itest_interpreter.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest interpreter commands"
  ],
  "heading_path": [
    "iTest interpreter commands",
    "iTest interpreter commands"
  ],
  "anchor": "1697343",
  "context_ids": [
    "commands_itest_interpreter"
  ],
  "index_keywords": [
    "iTest",
    "iTest commands",
    "inserting into test case steps",
    "inserting variables and parameters into"
  ],
  "index_keyword_paths": [
    "iTest > command syntax > command syntax > iTest",
    "parameters > inserting into test case steps",
    "steps > inserting variables and parameters into",
    "syntax > iTest commands",
    "variables > inserting into test case steps"
  ],
  "related_links": [
    "action_run.htm#1809404"
  ],
  "images": [],
  "content_hash": "01b89a20e5cd38de",
  "level": 1
}
---

# iTest interpreter commands > iTest interpreter commands

The iTest interpreter performs tasks that are useful in the iTest environment. We designed the syntax to be very much like Tcl or Python so that the commands would be easier to understand. You can use iTest interpreter commands to perform a variety of tasks; in Tcl test cases, some commands set a variable value (set), get a variable value (get), perform mathematical operations (math.abs). Both Tcl and Python return information about iTest (info), or access the response to an earlier step (response).

Some iTest interpreter commands have both Tcl and Python counterparts and some do not. For example, you can use set i 0 (which uses the same syntax as Tcl) to assign the value 0 to the variable i. You can then use i as a local variable in your test case with the value $i.

The built-in Python interpreter starts with the following modules loaded: basic math functions, random number generation, time methods, regular expressions, file reads and writes, stdio, data structure manipulations, and JSON structure processing.

> **Note:** Note To learn how the iTest environment and the Tcl environment relate, see About the iTest interpreter and the Tcl interpreters.
