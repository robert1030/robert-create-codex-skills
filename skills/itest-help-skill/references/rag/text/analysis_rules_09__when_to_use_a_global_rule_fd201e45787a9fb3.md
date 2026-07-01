---
{
  "chunk_id": "analysis_rules_09__when_to_use_a_global_rule_fd201e45787a9fb3",
  "source_file": "topics/analysis_rules.09.htm",
  "source_original_path": "topics/analysis_rules.09.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "When to use a Global rule"
  ],
  "heading_path": [
    "When to use a Global rule",
    "When to use a Global rule"
  ],
  "anchor": "1247039",
  "context_ids": [],
  "index_keywords": [
    "Global",
    "described",
    "precedence"
  ],
  "index_keyword_paths": [
    "Global analysis rules > described",
    "Global analysis rules > precedence",
    "analysis rules > Global"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "fd201e45787a9fb3",
  "level": 1
}
---

# When to use a Global rule > When to use a Global rule

At any time, for any step, a DUT can crash or can return a completely unexpected response. Ideally, the test case should capture the event, recognize its significance, and take appropriate actions (in the crash example, identify the crash message, collect the stack trace data, and then exit the test case or wait for a restart and then continue with a new test). You can design test cases to respond appropriately in these situations by using Global analysis rules—rules that are applied after analysis rules are applied and that act as catch-all rules.

For example, if you know that a certain class of devices generates a consistent message when it crashes, you can define a Global analysis rule for the session profile. Then, whenever iTest executes a step that references the session profile, iTest first applies any analysis rule for the step and then applies the Global analysis rule to see whether the crash condition exists. As a result, regardless of the step during which a crash occurs, it is handled by a rule that is designed specifically for the purpose.
