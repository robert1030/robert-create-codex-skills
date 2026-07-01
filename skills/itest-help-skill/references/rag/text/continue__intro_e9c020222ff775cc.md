---
{
  "chunk_id": "continue__intro_e9c020222ff775cc",
  "source_file": "topics/popups/arules/Continue.html",
  "source_original_path": "topics/popups/arules/Continue.html",
  "toc_path": null,
  "heading_path": [
    "Continue.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/arules_processor_properties.html",
    "help::/com.fnfr.svt.help/topics/analysis_rules_concept.html",
    "help::/com.fnfr.svt.help/topics/actions_on_events.html"
  ],
  "images": [],
  "content_hash": "e9c020222ff775cc",
  "level": 0
}
---

# Continue.html

The Continue action causes the current script to be aborted out to the innermost containing for, foreach, or while loop command. The loop then continues with the next iteration of the loop.

Use the Continue action when you want to execute particular steps for some iterations of the loop, but not for other iterations.

- The asynchronous property of a continue step is ignored
- Steps nested inside a continue step are never used

No configurable properties.

For details on using this action and other actions for the assert processor in analysis rules, see Analysis rules: Properties of the processor. Also, see: Analysis rules: Validating responses and setting Pass / Fail.

For details on using this action and other actions for events, see Actions on events: Definitions.
