---
{
  "chunk_id": "test_cases_store_response__options_for_storing_and_later_accessing__79831758f7f61e02",
  "source_file": "topics/test_cases_store_response.htm",
  "source_original_path": "topics/test_cases_store_response.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Test suites: Organizing tests for group execution",
    "Storing a response into a variable (for use later in the test)"
  ],
  "heading_path": [
    "Storing a response into a variable (for use later in the test)",
    "Storing a response into a variable (for use later in the test)",
    "Options for storing and later accessing the response"
  ],
  "anchor": "1565993",
  "context_ids": [
    "test_cases_store_response"
  ],
  "index_keywords": [
    "storing in variables",
    "storing responses in",
    "storing responses in variables"
  ],
  "index_keyword_paths": [
    "responses > storing in variables",
    "storing responses in variables",
    "variables > storing responses in"
  ],
  "related_links": [
    "command_response.htm#1698912",
    "field_replacement_query.htm#1679213",
    "insert_query_on_stored_response_dialog.htm#1246379",
    "test_cases_naming_variables_procedures.htm#1562803"
  ],
  "images": [],
  "content_hash": "79831758f7f61e02",
  "level": 2
}
---

# Storing a response into a variable (for use later in the test) > Storing a response into a variable (for use later in the test) > Options for storing and later accessing the response

You have the following options for storing and accessing the response data:

- By default, the variable is a complex object that includes both the text of the response and the structured data part of the response. To access the contents of the variable (in a subsequent step):

- Use a response command to return all or part of the response’s text content. See response command: Accessing response data that is stored in a variable.

- Use a query command to return the result of a query against the structured part of the response. See query command: Inserting the results of a query and Applying queries to stored responses.

- If you set the Store only the text of the response property for a step, then only the response text (and not the structured data part of the response) is stored in the variable. To access the contents of the variable (in a subsequent step):

- In Tcl test cases, use $varName or [get varName] (or, for global variables, [gget varName] or ${/data/varName}) to return the full text of the response.

- In Python test cases, use ‘varName’ (or, for global variables, gget(‘varName’) or response('/data/varName/')) to return the full text of the response.



To store a response into a variable

1. Select the step.

1. 2

1. In the Step Properties section, open the Other Post-processing > Store Response property group.

1. 3

1. In the Store the response in variable box, specify the name of a variable that should store the response. (See Naming variables and procedures.)

1. 4

1. Optional. Check the Store only the text of the response check box to save only the response text (and not the structured data part of the response) in a simple variable. As a result, you will later use as follows in Tcl and Python:

Tcl: $varName or [get varName] (or, for global variables, [gget varName] or ${/data/varName}) to return the full text of the response.

Python: varName or get(varName) (or, for global variables, gget(‘varName’) or varName) to return the full text of the response.

> **Note:** Note Do not check the box if you plan to use a response or query command on the stored response.

1. 5

1. Optional. Check the Make it global check box to make the specified variable a global variable.

Later, when it is time to read the global variable, use either:

- [response /data/varName] in Tcl and response('/data/varName') in Python if the entire response was stored. See response command: Accessing response data that is stored in a variable.

- [gget varName] or ${/data/varName} in Tcl and gget(‘varName’) or varName in Python when only the text portion of the response was stored (you checked the Store only the text of the response option). See response command: Accessing response data that is stored in a variable.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
