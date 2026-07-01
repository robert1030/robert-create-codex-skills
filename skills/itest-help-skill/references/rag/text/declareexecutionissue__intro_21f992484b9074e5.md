---
{
  "chunk_id": "declareexecutionissue__intro_21f992484b9074e5",
  "source_file": "popups/arules/DeclareExecutionIssue.html",
  "source_original_path": "popups/arules/DeclareExecutionIssue.html",
  "toc_path": null,
  "heading_path": [
    "DeclareExecutionIssue.html"
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
  "content_hash": "21f992484b9074e5",
  "level": 0
}
---

# DeclareExecutionIssue.html

Display an execution message in the Execution view, in the Step Issues view, and in test reports. Specify the message text in the Description cell.

Properties:

- Severity: This setting determines the type of message that is displayed in the Execution view and in test reports. Select the type of message: OK, Information, Warning, Error
- Message: Specify the text message to display in the Execution view and in test reports. Field replacements are supported. iTest can generate a plain language sentence for the execution message (for example, "Extracted value $value is equal to "Up"). To use this feature, use {auto_message_true} or {auto_message_false}, as appropriate.

For details on using this action and other actions for the assert processor in analysis rules, see Analysis rules: Properties of the processor. Also, see: Analysis rules: Validating responses and setting Pass / Fail.

For details on using this action and other actions for events, see Actions on events: Definitions.
