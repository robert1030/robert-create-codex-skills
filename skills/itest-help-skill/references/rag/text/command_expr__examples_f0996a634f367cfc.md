---
{
  "chunk_id": "command_expr__examples_f0996a634f367cfc",
  "source_file": "topics/command_expr.htm",
  "source_original_path": "topics/command_expr.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "expr command: Evaluating expressions"
  ],
  "heading_path": [
    "expr command: Evaluating expressions",
    "expr command: Evaluating expressions",
    "Examples"
  ],
  "anchor": "1679157",
  "context_ids": [
    "command_expr"
  ],
  "index_keywords": [
    "evaluating",
    "evaluating expressions",
    "expr",
    "in field replacements"
  ],
  "index_keyword_paths": [
    "evaluating expressions",
    "expr > in field replacements",
    "expressions > evaluating",
    "field replacements > expr"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "f0996a634f367cfc",
  "level": 2
}
---

# expr command: Evaluating expressions > expr command: Evaluating expressions > Examples

[expr 5 + 5]: replaced by 10

[expr $i + 1]: $i is first substituted with the value of the variable i. If i has value 10, then the result of this command is 11

[expr i + j]: i and j must be nodes in the local stack frame both must contain numbers. This returns their sum.

[expr $i + $j]: Produces the same answer as [expr i + j]

[expr (($packetsSent - $packetsRcvd)/$packetsSent)*100] is replaced by the packet loss percentage.

expr {[math.sin $i]/2}: Notice that the syntax for the iTest expr command differs from the Tcl syntax: expr {sin($i)/2}

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
