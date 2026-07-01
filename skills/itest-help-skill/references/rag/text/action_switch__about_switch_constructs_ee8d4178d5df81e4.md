---
{
  "chunk_id": "action_switch__about_switch_constructs_ee8d4178d5df81e4",
  "source_file": "topics/action_switch.htm",
  "source_original_path": "topics/action_switch.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Switch logic",
    "The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl)"
  ],
  "heading_path": [
    "The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl)",
    "The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl)",
    "About ‘switch’ constructs"
  ],
  "anchor": "1608029",
  "context_ids": [
    "action_switch"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "ee8d4178d5df81e4",
  "level": 2
}
---

# The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl) > The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl) > About ‘switch’ constructs

- switch steps support iTest variables ($i), parameters ([param]), expressions ($a + $b), constant values, and field substitutions

- To specify a multi-line expression for a switch control clause, use the Advanced settings for the Command property

- You can nest switch constructs

- If a switch step is skipped, then the entire switch construct is skipped. You can skip any individual case step within a switch construct.

- The case and default steps in a switch construct use the Start this step in a new thread and proceed to the next step (asynchronous execution) property of the switch step. The asynchronous execution settings of case and default steps are ignored.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
