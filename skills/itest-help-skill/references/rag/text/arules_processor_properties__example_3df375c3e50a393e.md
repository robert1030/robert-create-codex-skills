---
{
  "chunk_id": "arules_processor_properties__example_3df375c3e50a393e",
  "source_file": "topics/arules_processor_properties.htm",
  "source_original_path": "topics/arules_processor_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis rules: Properties of the processor"
  ],
  "heading_path": [
    "Analysis rules: Properties of the processor",
    "Analysis rules: Properties of the processor",
    "Assert processor",
    "Example"
  ],
  "anchor": "1220338",
  "context_ids": [
    "arules_processor_properties"
  ],
  "index_keywords": [
    "AbortExecution",
    "AbortStep",
    "AbortTest",
    "AbortThread",
    "Break",
    "CallProcedure",
    "Continue",
    "DeclareExecutionIssue",
    "Eval",
    "ExitExecution",
    "ExitProcedure",
    "FailTest",
    "PassTest",
    "PassTestIfNotAlreadyFailed",
    "PauseExecution",
    "RepeatStep",
    "ScriptEval",
    "SkipRemainingRules",
    "True or False action",
    "When True or False action",
    "analysis rules",
    "assert processor",
    "chart processor",
    "expression",
    "for events",
    "in analysis rules",
    "message processor",
    "message processor, execution issue",
    "processor properties",
    "store processor",
    "writeFile processor"
  ],
  "index_keyword_paths": [
    "AbortExecution action > for events",
    "AbortStep action > for events",
    "AbortTest action > for events",
    "AbortThread action > for events",
    "Break action > for events",
    "CallProcedure action > for events",
    "Continue action > for events",
    "DeclareExecutionIssue action > for events",
    "Eval action > for events",
    "ExitExecution action > for events",
    "ExitProcedure action > for events",
    "FailTest > When True or False action",
    "FailTest action > for events",
    "PassTest > When True or False action",
    "PassTest action > for events",
    "PassTestIfNotAlreadyFailed > When True or False action",
    "PassTestIfNotAlreadyFailed action > for events",
    "PauseExecution > When True or False action",
    "PauseExecution action > for events",
    "Perform property > in analysis rules",
    "RepeatStep > When True or False action",
    "RepeatStep action > for events",
    "ScriptEval > When True or False action",
    "ScriptEval action > for events",
    "SkipRemainingRules > When True or False action",
    "SkipRemainingRules action > for events",
    "True or False action",
    "When True or False action > AbortExecution",
    "When True or False action > AbortStep",
    "When True or False action > AbortTest",
    "When True or False action > AbortThread",
    "When True or False action > Break",
    "When True or False action > Continue",
    "When True or False action > DeclareExecutionIssue",
    "When True or False action > Eval",
    "When True or False action > ExitProcedure",
    "When True or False action > FailTest",
    "When True or False action > PassTest",
    "When True or False action > PassTestIfNotAlreadyFailed",
    "When True or False action > PauseExecution",
    "When True or False action > RepeatStep",
    "When True or False action > ScriptEval",
    "When True or False action > SkipRemainingRules",
    "actions for events > AbortExecution",
    "actions for events > AbortStep",
    "actions for events > AbortTest",
    "actions for events > AbortThread",
    "actions for events > Break",
    "actions for events > CallProcedure",
    "actions for events > Continue",
    "actions for events > DeclareExecutionIssue",
    "actions for events > Eval",
    "actions for events > ExitExecution",
    "actions for events > ExitProcedure",
    "actions for events > FailTest",
    "actions for events > PassTest",
    "actions for events > PassTestIfNotAlreadyFailed",
    "actions for events > PauseExecution",
    "actions for events > RepeatStep",
    "actions for events > ScriptEval",
    "actions for events > SkipRemainingRules",
    "analysis rules > processor properties",
    "assert processor",
    "assert processor > expression",
    "chart processor",
    "execution issue > message processor",
    "expressions > assert processor",
    "message processor",
    "processor properties > analysis rules",
    "processors > chart processor",
    "processors > message processor",
    "processors > message processor, execution issue",
    "processors > store processor",
    "processors > writeFile processor",
    "store processor",
    "writeFile processor"
  ],
  "related_links": [
    "ar_create_select_response_value.htm#1732822",
    "test_cases.04.htm#1861511"
  ],
  "images": [
    "topics/images/analysis_rule_setResponseValue-elipsis.png"
  ],
  "content_hash": "3df375c3e50a393e",
  "level": 3
}
---

# Analysis rules: Properties of the processor > Analysis rules: Properties of the processor > Assert processor > Example

1. The assert processor places the extracted data into an assertion and then tests the assertion. The assertion appears in the Description cell. For example, the assertion $value == 1 tests whether the value extracted from the response is equal to 1.

1. 2

1. If the value is equal to 1, then the assertion is True. If not, then the assertion is False.

To specify the actions that should occur upon True and False results, specify Rule Actions for When True and When False. For example, enter the Action SetResponseValue and specify a response in the Description cell. The action SetResponseValue, displays the Action Properties section.

> **Note:** Note You may open the Action Properties section in the Properties pane—right-click and then select the Show Properties View option on the menu. You may edit properties using either the Action Properties section (within the Test Case Editor) or via the Properties View tab.

You may also specify the actions response value in the Action Properties> Set Response Value section. In addition, you may specify the response value by clicking the ellipsis (on the Description cell or the Set Response Value section). iTest synchronizes the value entered on the description cell and with the value in the Set Response Value section, and vice versa. See also Select/Insert Response Value.

For Global rules, displayed in the Details cell:

| Expression (For Global rules, displayed in the Details cell) | Specify the expression to evaluate. This is typically a comparison of the query result with a particular value. Field replacements are supported. The expression can be any valid Tcl expression, provided that the command that you use is implemented by the iTest interpreter. You can use any of the iTest commands to create an expression using Tcl syntax. (For example, the iTest response command is commonly used to build an expression in assertions.) For the list of iTest interpreter commands, see iTest interpreter commands in steps. Predefined local variables used in assertions iTest populates predefined local variables while processing an analysis rule: $value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False) For the regex extractor, $value is the extracted value For the queries extractor, $value is the result of the query $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_value is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_value can be overwritten by another thread. $index is a iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. $itest_index is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_index is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_index can be overwritten by another thread. Temporary data tags {value} is a temporary data tag that stores the data that is extracted by the extractor {values} is a temporary data tag that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. {assertion} is a temporary data tag that stores the assertion that is being tested by the rule. The value of assertion appears in the Details cell for the rule. |  | $value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. |  | For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False) |  | For the regex extractor, $value is the extracted value |  | For the queries extractor, $value is the result of the query |  | $index is a iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. |  | {value} is a temporary data tag that stores the data that is extracted by the extractor |  | {values} is a temporary data tag that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. |  | {assertion} is a temporary data tag that stores the assertion that is being tested by the rule. The value of assertion appears in the Details cell for the rule. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | $value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | For the regex extractor, $value is the extracted value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | For the queries extractor, $value is the result of the query |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | $index is a iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | {value} is a temporary data tag that stores the data that is extracted by the extractor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | {values} is a temporary data tag that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | {assertion} is a temporary data tag that stores the assertion that is being tested by the rule. The value of assertion appears in the Details cell for the rule. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| When multiple matches | Some extractors can return multiple values. You can set the When multiple matches property to perform the specified action when multiple values are returned. Analyze each separately: Return the result of processing each of the responses and perform the appropriate When True or When False actions for each. Do nothing: No errors are generated and no analysis is performed. Do not return a result of processing and continue with the next analysis rule. True if all true: Return (one time) the result 1 (True) only if each of the responses evaluates to True when processed. True if any true: Return (one time) the result 1 (True) if any of the responses evaluates to True when processed. Fail test (raises OnAssertMultipleMatches event): The default actions for this option are: Set the test result to Fail Display an execution message in the Execution view and in the test report. You can configure the actions by editing the OnAssertMultipleMatches event (in the Analysis Processor: Assert group). |  | Set the test result to Fail |  | Display an execution message in the Execution view and in the test report. |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Set the test result to Fail |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Display an execution message in the Execution view and in the test report. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

![screenshot](topics/images/analysis_rule_setResponseValue-elipsis.png) <!-- image_chunk: img_7deb1268ea5defc0 -->
