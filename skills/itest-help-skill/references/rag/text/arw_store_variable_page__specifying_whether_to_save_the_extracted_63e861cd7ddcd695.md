---
{
  "chunk_id": "arw_store_variable_page__specifying_whether_to_save_the_extracted_63e861cd7ddcd695",
  "source_file": "topics/arw_store_variable_page.htm",
  "source_original_path": "topics/arw_store_variable_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Save Data as variable or Response Value page"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Save Data as variable or Response Value page",
    "Analysis Rule Wizard: Save Data as variable or Response Value page",
    "Specifying whether to save the extracted data as variable or response value"
  ],
  "anchor": "1177853",
  "context_ids": [
    "arw_store_variable_page"
  ],
  "index_keywords": [
    "Analysis Rule wizard",
    "Variable page"
  ],
  "index_keyword_paths": [
    "Analysis Rule wizard > Variable page",
    "Variable page > Analysis Rule wizard"
  ],
  "related_links": [
    "return_value_dialog.htm#1292200",
    "procedures_overview.htm#",
    "command_json_select.htm#1848239",
    "arules_processor_properties.htm#1641520"
  ],
  "images": [],
  "content_hash": "63e861cd7ddcd695",
  "level": 2
}
---

# Analysis Rule Wizard: Save Data as variable or Response Value page > Analysis Rule Wizard: Save Data as variable or Response Value page > Specifying whether to save the extracted data as variable or response value

Because the rule will store the extracted data as a variable or a response value, you will now configure the variable. This wizard page has the effect of setting Perform (the Processor property) to store for the resulting analysis rule.

| Variable name | Specify the variable into which to store the extracted value. A response with zero values or multiple values is always stored in a list. See the Always store data in a list property for recommendations when a single extracted value can contain whitespace. |
| --- | --- |
| Global: Make the variable accessible in other procedures | Check the box to make the variable a Global variable. Global variables are available to any step in the test case. When you define a Global variable, the Data view displays the variable under the data node in the heap (instead of the stack section). This is what makes the variable. In contrast, local variables are created in the stack node in the heap. The stack section is transient, that is, it can be “popped” off and therefore lose all variable information. |
| Always store single match in a list | This setting is important when you're using the response as the argument to a foreach statement. Specify how to store the extracted value when it is a single value. The default setting of unchecked (false) means that a single extracted value is stored in a scalar string, rather than as a list with a single element. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single extracted value can contain whitespace. With the default setting, a foreach statement that iterates over the stored variable will loop for each word in the single match, rather than once for the match. To avoid this behavior, check Always store a single match in a list. In contrast, if the desired behavior is to iterate over the individual words in a single match, then leave the box unchecked. |
| Response value | Specify the XPath that is using the extracted value to replace the sample JSON string defined in the Procedure properties > Input and Outputs > Response (Defining a procedure, in “Procedures”). The return value is a field substitution of [return query_xpath] in which the query_xpath is the same with jsonSelect command (iTest Commands, page 508). Once the return value is defined, during execution, iTest will replace the sample json values that is evaluated by the query_xpath, see Store processor for more details |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
