---
{
  "chunk_id": "arules_global_working_with__adding_a_global_analysis_rule_ed861faa11cb0f6a",
  "source_file": "topics/arules_global_working_with.htm",
  "source_original_path": "topics/arules_global_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Adding and working with Global analysis rules"
  ],
  "heading_path": [
    "Adding and working with Global analysis rules",
    "Adding and working with Global analysis rules",
    "Adding a Global analysis rule"
  ],
  "anchor": "1186648",
  "context_ids": [
    "arules_global_working_with"
  ],
  "index_keywords": [
    "Global analysis rules",
    "adding",
    "editing",
    "editing Global rule"
  ],
  "index_keyword_paths": [
    "Global analysis rules > adding",
    "Global analysis rules > editing",
    "adding > Global analysis rules",
    "analysis rules > editing Global rule"
  ],
  "related_links": [
    "arules_extractor_properties.htm#1540431",
    "arules_processor_properties.htm#1186331"
  ],
  "images": [
    "topics/images/analysis_rules.02.jpg"
  ],
  "content_hash": "ed861faa11cb0f6a",
  "level": 2
}
---

# Adding and working with Global analysis rules > Adding and working with Global analysis rules > Adding a Global analysis rule

1. 1

1. In the editor, click the Global Rules tab.

1. 2

1. Click Add . iTest adds a default rule.

1. 3

1. Click in the Extract using cell to select an extractor type for the rule. Based on your selection, iTest places default text in the What to extract cell. Replace the text with the value that the extractor should use to get the data from the response.

Important For query extractors, do not use right-click to insert a query value into the What to Extract cell. Instead, paste or type a query from the Queries view.

1. 4

1. Click in the Perform cell to select a processor type for the rule. Based on your selection, iTest places default text in the Details cell. If appropriate, replace the text with the value that the processor should use to process the data that is returned by the extractor.

1. 5

1. Now, you have the option to modify the property settings of the rule’s extractors and processors. Click More to open the Analysis Rule Properties section. In the example, we selected Regex so that we could edit the properties associated with the Regex extractor. For details, see Analysis rules: Properties of the extractor and Analysis rules: Properties of the processor.

1. 6

1. Optional: You can use the Skip check box or Skip to skip the rule while developing/debugging a test case.

1. 7

1. Optional: You can use Move Up/Move Down to move a selected rule in the list. Rules are applied in the listed order.

![screenshot](topics/images/analysis_rules.02.jpg) <!-- image_chunk: img_059cfc874c63e03e -->
