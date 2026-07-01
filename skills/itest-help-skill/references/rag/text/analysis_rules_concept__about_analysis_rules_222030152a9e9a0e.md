---
{
  "chunk_id": "analysis_rules_concept__about_analysis_rules_222030152a9e9a0e",
  "source_file": "topics/analysis_rules_concept.htm",
  "source_original_path": "topics/analysis_rules_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis rules: Validating responses and setting Pass / Fail"
  ],
  "heading_path": [
    "Analysis rules: Validating responses and setting Pass / Fail",
    "Analysis rules: Validating responses and setting Pass / Fail",
    "About analysis rules"
  ],
  "anchor": "1204423",
  "context_ids": [
    "analysis_rules_concept"
  ],
  "index_keywords": [
    "analysis rules",
    "described",
    "examples",
    "in analysis rules defined",
    "setting criteria"
  ],
  "index_keyword_paths": [
    "analysis rules > described",
    "analysis rules > examples",
    "examples > analysis rules",
    "extractors > in analysis rules defined",
    "pass/fail > setting criteria",
    "processors > in analysis rules defined",
    "validating responses > analysis rules"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "222030152a9e9a0e",
  "level": 2
}
---

# Analysis rules: Validating responses and setting Pass / Fail > Analysis rules: Validating responses and setting Pass / Fail > About analysis rules

- Analysis rules are optional. You create a rule only when you need to work with the response to a step. Typically, you define rules for only a few steps.

- Each executable step can have any number of analysis rules associated with it. Rules are applied in the order in which they are listed.

- An analysis rule applies only to the step for which it is defined. (You can define special Global rules)

- During execution, if the condition that you specify in a rule is not met, the default action is to display an execution issue in the Execution view and in the test report. You can specify additional actions (like passing or failing the test and so on).
