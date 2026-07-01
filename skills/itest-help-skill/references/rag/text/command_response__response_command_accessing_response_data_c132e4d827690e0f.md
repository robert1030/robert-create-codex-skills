---
{
  "chunk_id": "command_response__response_command_accessing_response_data_c132e4d827690e0f",
  "source_file": "topics/command_response.htm",
  "source_original_path": "topics/command_response.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "response command: Accessing response data that is stored in a variable"
  ],
  "heading_path": [
    "response command: Accessing response data that is stored in a variable",
    "response command: Accessing response data that is stored in a variable"
  ],
  "anchor": "1698912",
  "context_ids": [
    "command_response"
  ],
  "index_keywords": [
    "accessing response text stored in",
    "creating assertions",
    "response",
    "response command",
    "stored in variables",
    "using response command to create"
  ],
  "index_keyword_paths": [
    "assertion > using response command to create",
    "commands > response",
    "field replacements > response command",
    "response command",
    "response command > creating assertions",
    "response content > stored in variables",
    "variables > accessing response text stored in"
  ],
  "related_links": [
    "test_cases_store_response.htm#1320078"
  ],
  "images": [],
  "content_hash": "c132e4d827690e0f",
  "level": 1
}
---

# response command: Accessing response data that is stored in a variable > response command: Accessing response data that is stored in a variable

To cause iTest to store the response to a step into a variable, you set the Store response in variable property for the step. By default, the variable is a complex object that includes both the text of the response and the structured data part of the response. (See Storing a response into a variable (for use later in the test) for details.)

Now, to return the stored response content from the variable, use the response command. The response command can return the entire response text and structured data for analysis or it can return particular data from the response text (for example, return a list of matches by applying a regex to the response).

> **Note:** Note If you set the Store only the text of the response property for a step, then only the response text (and not the structured data part of the response) is stored in a simple variable.

In Tcl test cases, you cannot use a [response varName] field replacement to return data. Instead, you must use $varName or [get varName] to return the full response text.

In Python test cases, for example, when using eval print("This string will be stored in a variable"), stores the response in a variable named “output”.

eval response("output")

> **Note:** Do not check the option Store only the text of the response, in Step Properties > Other Post-processing.
