---
{
  "chunk_id": "action_scripteval__substitutions_in_the_command_text_3a430f911e9d6f78",
  "source_file": "topics/action_scripteval.htm",
  "source_original_path": "topics/action_scripteval.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘scriptEval’ action: Evaluate a Tcl command"
  ],
  "heading_path": [
    "The ‘scriptEval’ action: Evaluate a Tcl command",
    "The ‘scriptEval’ action: Evaluate a Tcl command",
    "Substitutions in the Command text"
  ],
  "anchor": "1520179",
  "context_ids": [
    "action_scripteval"
  ],
  "index_keywords": [
    "evaluating",
    "evaluating Tcl commands",
    "scriptEval",
    "scriptEval action"
  ],
  "index_keyword_paths": [
    "Tcl commands > evaluating",
    "actions > scriptEval",
    "evaluating Tcl commands",
    "scriptEval action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3a430f911e9d6f78",
  "level": 2
}
---

# The ‘scriptEval’ action: Evaluate a Tcl command > The ‘scriptEval’ action: Evaluate a Tcl command > Substitutions in the Command text

By default, the following types of substitution are not made to the text of the Command property before the step is executed:

- Command field replacements

- Variables

- Backslash characters used to escape special characters

To cause iTest to pre‑process the Command text and perform such substitutions before the text is interpreted as a Tcl statement, follow this procedure:

1. Select the step.

1. 2

1. On the Step Properties page, check the For the Command field, first perform command, variable, and backslash substitutions box.
