---
{
  "chunk_id": "arw_assertion_page__analysis_rule_wizard_actions_page_1a1836e2f458d2cf",
  "source_file": "topics/arw_assertion_page.htm",
  "source_original_path": "topics/arw_assertion_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Actions page"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Actions page",
    "Analysis Rule Wizard: Actions page"
  ],
  "anchor": "1207805",
  "context_ids": [
    "arw_assertion_page"
  ],
  "index_keywords": [
    "Actions page",
    "Analysis Rule wizard"
  ],
  "index_keyword_paths": [
    "Actions page > Analysis Rule wizard",
    "Analysis Rule wizard > Actions page"
  ],
  "related_links": [],
  "images": [
    "topics/images/analysis_rules_4.1.jpg",
    "topics/images/analysis_rules_4.2.jpg"
  ],
  "content_hash": "1a1836e2f458d2cf",
  "level": 1
}
---

# Analysis Rule Wizard: Actions page > Analysis Rule Wizard: Actions page

On this page, you specify two sets of actions to take:

- The top section configures the action to take when the condition is met (for example, When Response Contains Specified Text as shown here)

- The bottom section configures the action to take when the condition is not met (for example, When Response does not Contain Specified Text as shown here)

The settings on this wizard page will generate the settings on the WhenTrue and WhenFalse properties pages in the Test Case Editor Action Properties property group.

The page appears in one of the following formats, depending on the method you selected for validating the response data:

| When the response should contain a particular string, then: | The top section is called When Response Contains Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) and The bottom section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion returns 0 (false) |  | The top section is called When Response Contains Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  | The bottom section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion returns 0 (false) |
| --- | --- | --- | --- | --- | --- |
|  | The top section is called When Response Contains Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  |  |  |  |
|  | The bottom section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion returns 0 (false) |  |  |  |  |
| When the response should not contain a particular string, then: | The top section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) and The bottom section is called When Response Contains Specified Text: You specify the actions to take when the assertion returns 0 (false) |  | The top section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  | The bottom section is called When Response Contains Specified Text: You specify the actions to take when the assertion returns 0 (false) |
|  | The top section is called When Response Does Not Contain Specified Text: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  |  |  |  |
|  | The bottom section is called When Response Contains Specified Text: You specify the actions to take when the assertion returns 0 (false) |  |  |  |  |
| When you specified a comparison between the value from the response and an expected value, then: | The top section is called When Expression is True: You specify the actions to take when the assertion that the rule is testing returns 1 (True) and The bottom section is called When Expression is False: You specify the actions to take when the assertion returns 0 (false) For example, the assertion $value == 04:00:00 tests whether the extracted value is equal to “04:00:00”. If the value is indeed equal to “04:00:00”, then the assertion is True. If the value is not equal to “04:00:00”, then the assertion is False. To specify the actions that should occur upon True and False results, you specify two sets of actions to take: In the When Expression is True section, you specify the actions to take when the assertion that the rule is testing returns 1 (True) and In the When Expression is False section, you specify the actions to take when the assertion returns 0 (false) Note that some extractor types can return multiple values. |  | The top section is called When Expression is True: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  | The bottom section is called When Expression is False: You specify the actions to take when the assertion returns 0 (false) |
|  | The top section is called When Expression is True: You specify the actions to take when the assertion that the rule is testing returns 1 (True) |  |  |  |  |
|  | The bottom section is called When Expression is False: You specify the actions to take when the assertion returns 0 (false) |  |  |  |  |
|  | In the When Expression is True section, you specify the actions to take when the assertion that the rule is testing returns 1 (True) |  |  |  |  |
|  | In the When Expression is False section, you specify the actions to take when the assertion returns 0 (false) |  |  |  |  |

![screenshot](topics/images/analysis_rules_4.1.jpg) <!-- image_chunk: img_a5e98cd390f780f5 -->

![screenshot](topics/images/analysis_rules_4.2.jpg) <!-- image_chunk: img_c8509f8995b24bf4 -->
