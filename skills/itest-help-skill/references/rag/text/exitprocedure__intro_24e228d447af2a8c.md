---
{
  "chunk_id": "exitprocedure__intro_24e228d447af2a8c",
  "source_file": "popups/exitprocedure.html",
  "source_original_path": "popups/exitprocedure.html",
  "toc_path": null,
  "heading_path": [
    "exitprocedure.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/global_events_page.html",
    "help::/com.fnfr.svt.help/topics/arules_processor_properties.html"
  ],
  "images": [],
  "content_hash": "24e228d447af2a8c",
  "level": 0
}
---

# exitprocedure.html

Stop executing the current procedure and return execution from the current procedure to the caller.

Important: Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after an ExitProcedure action, the ExitProcedure action does not execute until the FailTest action is finished executing.

An appropriate execution message appears in the Execution view and in test reports.

Return value: Specify the value to return for the procedure. The text string can contain field replacements (for example, [response var_name]).

For details, see the online help:

Global Events page

Analysis rules: Properties of the processor
