---
{
  "chunk_id": "analysis_rules_02__the_processor_b3e9f6247534f584",
  "source_file": "topics/analysis_rules.02.htm",
  "source_original_path": "topics/analysis_rules.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "The structure of an analysis rule"
  ],
  "heading_path": [
    "The structure of an analysis rule",
    "The structure of an analysis rule",
    "The processor"
  ],
  "anchor": "1221973",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b3e9f6247534f584",
  "level": 3
}
---

# The structure of an analysis rule > The structure of an analysis rule > The processor

The processor is the second line in the rule — it specifies the type of action to take and the details of the action to take on the extracted data.

- The type of action to take appears in the Action cell. In the example, the action is to use the assert processor to test an assertion about the extracted value. Other processors chart the value, display an execution message, or store the value in a variable.

- The details of the action to take appear in the Description cell. In the example, we specify the assertion to be tested: test whether the extracted data equals 42. The When True and When False substeps are a part of the assert processor that tell iTest to take a particular action when the assertion is true and a different action when the assertion is false.

If we had specified a message processor, the details of the action would be the text to display in the message.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
