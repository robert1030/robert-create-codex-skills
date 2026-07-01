---
{
  "chunk_id": "deferred_actions__about_deferred_actions_afc319cacbdfbce0",
  "source_file": "topics/deferred_actions.htm",
  "source_original_path": "topics/deferred_actions.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "About deferred actions"
  ],
  "heading_path": [
    "About deferred actions",
    "About deferred actions"
  ],
  "anchor": "1733621",
  "context_ids": [
    "deferred_actions"
  ],
  "index_keywords": [
    "deferred",
    "deferred actions"
  ],
  "index_keyword_paths": [
    "actions > deferred",
    "analysis rules > deferred actions",
    "deferred actions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "afc319cacbdfbce0",
  "level": 1
}
---

# About deferred actions > About deferred actions

Because some analysis rule actions alter the flow of execution, they are deferred — they are placed in a queue and are not executed until all other actions for the step are executed.

Such an action is deferred even if it appears before other actions in the list of actions for the event and if there are additional analysis rules listed for the step after the current rule. For example, CallProcedure actions are deferred because other actions may need to occur before a CallProcedure should happen.
