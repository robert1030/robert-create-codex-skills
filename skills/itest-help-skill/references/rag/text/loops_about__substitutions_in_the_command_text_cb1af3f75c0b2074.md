---
{
  "chunk_id": "loops_about__substitutions_in_the_command_text_cb1af3f75c0b2074",
  "source_file": "topics/loops_about.htm",
  "source_original_path": "topics/loops_about.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic"
  ],
  "heading_path": [
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic",
    "Substitutions in the Command text"
  ],
  "anchor": "1530407",
  "context_ids": [
    "loops_about"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "for loop > defined",
    "foreach loop > defined",
    "if-then logic > defined",
    "while loop > defined"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "cb1af3f75c0b2074",
  "level": 2
}
---

# Overview: Loops and flow‑control logic > Overview: Loops and flow‑control logic > Substitutions in the Command text

The command for while, forEach, for, and if actions is directed at the iTest interpreter. To ensure that iTest commands like [tcl ] or [tclexpr ] will be correctly interpreted, the text for the Command property (that appears in the Description cell) is interpreted as literal text. The property that controls substitution for the step is disabled (the For the Command field, perform command, variable, and backslash substitution property).

As a result, the text is not processed for the following substitution types before the step is executed (substitution occurs during execution):

- Command field replacements (for example, char, expr, param, query, or response)

- Variables

- Backslash characters used to escape special characters

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
