---
{
  "chunk_id": "command_call__syntax_638b512212ff4ad4",
  "source_file": "topics/command_call.htm",
  "source_original_path": "topics/command_call.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "call command: Call a procedure and get the return value from that procedure"
  ],
  "heading_path": [
    "call command: Call a procedure and get the return value from that procedure",
    "call command: Call a procedure and get the return value from that procedure",
    "Syntax"
  ],
  "anchor": "1846004",
  "context_ids": [
    "command_call"
  ],
  "index_keywords": [
    "call",
    "call command"
  ],
  "index_keyword_paths": [
    "call command",
    "commands > call",
    "field replacements > call command"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "638b512212ff4ad4",
  "level": 2
}
---

# call command: Call a procedure and get the return value from that procedure > call command: Call a procedure and get the return value from that procedure > Syntax

call testcase_path#procedure_name -arg value

testcase_path: is the uri of the test case that will be executed, typically starting with project://..

procedure_name: is the name of the procedure in the test case. Default will be main if not specified.

-arg value: is the series of arguments defined for the procedure.

The procedure will be executed in a separate thread, and the main execution thread will wait for the procedure to be finished so that the return value can be retrieved.

> **Caution:** CAUTION To avoid the execution loop, make sure that the called procedure does not invoke the current procedure. If you use the call command in open step, for example, use the field substitution in session profile properties, make sure that the open step session id is different with the called procedure's open step session id, otherwise there will be an execution loop. For example, in the following test cases (see illustration below), main.fftc opens a session profile call_1.ffsp whose IP address uses call command to get the value, and the call_1.fftc also has an open step, notice that these two open steps session ids are different: one is s1, the other is t1.
