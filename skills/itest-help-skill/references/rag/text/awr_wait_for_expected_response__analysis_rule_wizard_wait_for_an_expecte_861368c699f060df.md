---
{
  "chunk_id": "awr_wait_for_expected_response__analysis_rule_wizard_wait_for_an_expecte_861368c699f060df",
  "source_file": "topics/awr_wait_for_expected_response.htm",
  "source_original_path": "topics/awr_wait_for_expected_response.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Wait for an expected reponse"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Wait for an expected reponse",
    "Analysis Rule Wizard: Wait for an expected reponse"
  ],
  "anchor": "1755484",
  "context_ids": [
    "awr_wait_for_expected_response"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "arules_processor_properties.htm#1707206"
  ],
  "images": [
    "topics/images/arw_waitForExpectedResponse.png",
    "topics/images/arw_wfer_events_queryFailure.png",
    "topics/images/arw_wfer_restReport.png"
  ],
  "content_hash": "861368c699f060df",
  "level": 1
}
---

# Analysis Rule Wizard: Wait for an expected reponse > Analysis Rule Wizard: Wait for an expected reponse

The Wait for an expected response option of the Analysis Rules wizard and the Quick Analysis Rule provides you with an option to set up the wait for logic to ensure that execution does not continue until specified condition is met.

The Wait for an expected response adds an analysis rule that invokes an action rule to repeat (RepeatStep rule action) a set of steps and an INFO level message indicating that the test case is waiting until the specified condition is met. This saves you the effort of having to manually insert these action rules.

Use the Quick Analysis Rule or Analysis Rule wizard to add the Wait for an expected response for a test case step. The settings on this wizard page will generate the settings on the WhenTrue and WhenFalse properties pages in the Test Case Editor Action Properties property group.

The analysis rule will use these actions.

1. Use the default analysis rule actions to add the When True condition (When True / When False)

1. 2

1. Use the following rule actions to add the When False condition.

DeclareExecutionIssue INFO:{auto_message_wait}

RepeatStep max:30 delay:2

1. 3

1. Create a new auto_message called auto_message_wait with one message per extractor:

- Contains: Waiting for response to contain "$value"

- Regular expression: Waiting for value to match "$value"

- Query: Waiting for query to match value "$value"

> **Note:** Note When manually inserting a RepeatStep rule action, the defaults are changes from max:10, delay:1 to max:30, delay:2.

The Wait for an expected response supports all 3 extractors— contains, regex, and query. In addition supports the condition where regex and query fail while waiting (OnQueryExtractorInvalidQuery and OnNoMatchesFound). For example:

The execution report message shows that the test cases wait for the expected response until the specified condition is met.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/arw_waitForExpectedResponse.png) <!-- image_chunk: img_b534dcdf9102c2c9 -->

![screenshot](topics/images/arw_wfer_events_queryFailure.png) <!-- image_chunk: img_9b808001724a2316 -->

![screenshot](topics/images/arw_wfer_restReport.png) <!-- image_chunk: img_13640d88013d4289 -->
