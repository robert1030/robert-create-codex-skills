---
{
  "chunk_id": "arules_processor_properties__store_processor_70447d3d29dc8b32",
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
    "Store processor"
  ],
  "anchor": "1641520",
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
    "return_value_dialog.htm#1292200",
    "procedures_overview.htm#",
    "ar_create_select_response_value.htm#1732822",
    "command_json_select.htm#1848239",
    "command_return_json_xpath_return_value_dialog.htm#1849628"
  ],
  "images": [],
  "content_hash": "70447d3d29dc8b32",
  "level": 2
}
---

# Analysis rules: Properties of the processor > Analysis rules: Properties of the processor > Store processor

The store processor stores the data that is extracted while processing the rule as a variable or a response value.

- A response with zero values or multiple values is always stored in a list.

- You can specify whether to store a single extracted value in a scalar string or in a list. See the Always store data in a list property for recommendations when a single extracted value can contain whitespace.

- Store processor also supports response value from the JSON response (see Procedure Properties > Inputs and Outputs > Response in section Defining a procedure of “Procedures”).

> **Tip:** Tip You can store a value from the response to a step (e.g., step 12). In a later step (e.g., step 19), you can add a rule about a token in step 19 and compare its value to the value of the token extracted in step 12. So, for step 19, you can create an assertion like: $value > $tokenStep12 * 2

> **Note:** Note You may open the context specific information—Processor Properties section in the Properties pane. Right-click and select the Show Properties View option from the menu. You may edit properties using either the Processor Properties section (within the Test Case Editor) or via the Properties View tab.

| Variable | Specify the variable into which to store the extracted value. A response with zero values or multiple values is always stored in a list. See the Always store data in a list property for recommendations when a single extracted value can contain whitespace. |
| --- | --- |
| Secret: Hide the value in views and reports | Selecting to store the variable value as a secret parameter type does not hide this in the reports. If an analysis rule uses the 'store' processor which stores the result into a secret variable is applied to the step, the response does not became secret as of iTest Release 8.4. |
| Global: Make the variable accessible in other procedures | Check the box to make the variable a Global variable. Global variables are available to any step in the test case. When you define a Global variable, the Data view displays the variable under the data node in the heap (instead of the stack section). This is what makes the variable. In contrast, local variables are created in the stack node in the heap. The stack section is transient, that is, it can be “popped” off and therefore lose all variable information. |
| Always store a single match in a list | This setting is important when you're using the response as the argument to a foreach statement. Specify how to store the extracted value when it is a single value. The default setting of unchecked (false) means that a single extracted value is stored in a scalar string, rather than as a list with a single element. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single extracted value can contain whitespace. With the default setting, a foreach statement that iterates over the stored variable will loop for each word in the single match, rather than once for the match. To avoid this behavior, check Always store a single match in a list. In contrast, if the desired behavior is to iterate over the individual words in a single match, then leave the box unchecked. |
| Response value | Specify the XPath that is using the extracted value to replace the sample json string (defined in Procedure Properties > Inputs and Outputs > Response. See section Defining a procedure in “Procedures”). You may enter the response value in the Processor Properties > Store section or click the ellipsis to select or add a new response value. See Select/Insert Response Value. The return value is a field substitution of [return query_xpath] in which the query_xpath is the same with jsonSelect command (page 508). Once the return value is defined, during execution, iTest will replace the sample json values evaluated by the query_xpath. Use Return Value dialog (See iTest Commands, page 510) to get the XPath easily. |
