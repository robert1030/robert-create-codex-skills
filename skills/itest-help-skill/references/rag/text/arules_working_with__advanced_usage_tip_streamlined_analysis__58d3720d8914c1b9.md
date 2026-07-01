---
{
  "chunk_id": "arules_working_with__advanced_usage_tip_streamlined_analysis__58d3720d8914c1b9",
  "source_file": "topics/arules_working_with.htm",
  "source_original_path": "topics/arules_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Adding and working with analysis rules"
  ],
  "heading_path": [
    "Adding and working with analysis rules",
    "Adding and working with analysis rules",
    "Advanced usage tip—streamlined Analysis rules"
  ],
  "anchor": "1741465",
  "context_ids": [
    "arules_working_with"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/tce_add_rule.png"
  ],
  "content_hash": "58d3720d8914c1b9",
  "level": 2
}
---

# Adding and working with analysis rules > Adding and working with analysis rules > Advanced usage tip—streamlined Analysis rules

You may define Analysis Rule before executing a test case by defining QuickCall procedures or custom session with JSON Response, and inserting these calls in a Test Case. The inserted step populates the Response View with the JSON response format from the called procedure (the Response View background is light grey before running a test case). The Queries and Structure views are also populated with contents for the response.

You may insert Analysis Rule as required before executing the test case. Using the Quick Analysis Rule feature to specify an analysis rule for a step

In this example, we'll add a regex rule that checks whether a value is correct and then takes action based on the result.

1. 1

1. In the Steps section of the test case editor, select the step. The response appears in the Response view:

1. 2

1. iTest places the response to the step (from the last execution) into the Response view. Select the text to analyze. Right-click the selection and then choose Quick Analysis Rule > Regular expression > Compare and take action accordingly.

A new rule is added to the step, specifying the regular expression as the extractor, and assert as the processor, This rule will place the extracted data into the assertion listed in the Details property and then test the assertion.

1. 3

1. Now, check whether the rule works as you expect. Open the Step Issues view to see the execution message that results for the response text from the most recent execution of the step (that is, the response text in the Response view that you used to help you to create the rule). This method saves you from having to iteratively execute the test case to see whether the rule works correctly.

![screenshot](topics/images/tce_add_rule.png) <!-- image_chunk: img_07471369807f6e3f -->
