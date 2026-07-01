---
{
  "chunk_id": "arw_message_page__analysis_rule_wizard_execution_message_p_f1781ed45f9fabed",
  "source_file": "topics/arw_message_page.htm",
  "source_original_path": "topics/arw_message_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Execution Message page"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Execution Message page",
    "Analysis Rule Wizard: Execution Message page"
  ],
  "anchor": "1208124",
  "context_ids": [
    "arw_message_page"
  ],
  "index_keywords": [
    "Analysis Rule wizard",
    "Execution Message page"
  ],
  "index_keyword_paths": [
    "Analysis Rule wizard > Execution Message page",
    "Execution Message page > Analysis Rule wizard"
  ],
  "related_links": [],
  "images": [
    "topics/images/analysis_rules_3.5.jpg"
  ],
  "content_hash": "f1781ed45f9fabed",
  "level": 1
}
---

# Analysis Rule Wizard: Execution Message page > Analysis Rule Wizard: Execution Message page

The rule will create an execution issue and associated message for display in the Execution view, the Step Issues view, and in test reports, you will now specify the details of the message. This wizard page has the effect of setting Perform (the Processor property) to message for the resulting analysis rule.

> **Note:** Note Enabling this feature inserts the tag name/value pair into ElasticSearch when running from Velocity. This may be rendered in Kibana dashboards so that you can trend measurements and results across multiple test runs. See Velocity Deployment Guide (on Spirent Knowledge Base). to set up Kibana visualization.

| Severity | Specifies the severity of the execution issue to associate with the execution message that is displayed in the Execution view, in the Step Issues view, and in test reports: OK Error Warning Information |
| --- | --- |
| Use auto-generated message | Checked: The text in the Message box becomes dim and read-only. The box displays the message that will be generated as a plain language sentence (for example, Extracted value $value is equal to “Up”). In the resulting analysis rule as viewed in the Test Case editor, the text appears as {auto_message_true} and {auto_message_false}, as shown in this example: Unchecked: The text in the Message box becomes read-write. You can change the message as needed. The message will appear in the When True and When False property pages for Analysis rules in the Test Case editor. The {value} text is replaced with the value of the built-in variable named value. If the extracted value is a member of a list, then you can use {index}. The {index} text is replaced with the value of the built-in variable named index, which holds the index of the extracted value. Use {assertion} to display the assertion that was tested to determine the Pass/Fail outcome. Default: Checked |
| Message | If you do not check Use auto-generated message, then you can specify the text message to display in the Execution view, in the Step Issues view, and in test reports. Field replacements are supported. The {value} text is replaced with the value of the built-in variable named value. If the extracted value is a member of a list, then you can use {index}. The {index} text is replaced with the value of the built-in variable named index, which holds the index of the extracted value. Use {assertion} to display the assertion that was tested to determine the Pass/Fail outcome. About the predefined variables iTest populates predefined variables while processing an analysis rule: $value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. For string comparisons, $value is 1 (True, the string matches) or 0 (zero, False) For regex, $value is the extracted value For queries, $value is the result of the query $values is a iTest interpreter variable that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. $index: When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. |
|  | $value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. |
|  | For string comparisons, $value is 1 (True, the string matches) or 0 (zero, False) |
|  | For regex, $value is the extracted value |
|  | For queries, $value is the result of the query |
|  | $values is a iTest interpreter variable that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. |
|  | $index: When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. |
|  | $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. |
| Add to report and ElasticSearch (when running from Velocity) | Select Add to report and ElasticSearch (when running from Velocity and enter a value (a single string, number, or list) for the Extracted Data Tag (mandatory). Inserts the tag name/value pair into ElasticSearch when running from Velocity. This may be rendered in Kibana dashboards so that you can trend measurements and results across multiple test runs. See Velocity Deployment Guide (on Spirent Knowledge Base). to set up Kibana visualization. When an execution message adds extracted data to the test report, the tag is treated as a key, where that tag can have only one value (a single string, number, or list). When a test case generates multiple execution messages with the same Extracted Data Tag, only the latest tag value will show in the test report. |

> **Note:** Limitations

The following limitations apply for the data extracted for each execution:

- Total elements stored: A maximum of 128 extracted data items per execution.

- Bytes stored: A maximum of 128 characters of any tag or value. Any tag or value that exceeds 128 characters will be truncated.

- Array elements stored: Any extracted data item whose value is an array that exceeds 128 items will be rejected (discarded).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/analysis_rules_3.5.jpg) <!-- image_chunk: img_354136cb36f444c2 -->
