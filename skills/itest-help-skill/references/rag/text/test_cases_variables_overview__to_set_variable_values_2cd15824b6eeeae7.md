---
{
  "chunk_id": "test_cases_variables_overview__to_set_variable_values_2cd15824b6eeeae7",
  "source_file": "topics/test_cases_variables_overview.htm",
  "source_original_path": "topics/test_cases_variables_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Test suites: Organizing tests for group execution",
    "Setting and accessing variables in test case steps"
  ],
  "heading_path": [
    "Setting and accessing variables in test case steps",
    "Setting and accessing variables in test case steps",
    "To set variable values"
  ],
  "anchor": "1266126",
  "context_ids": [
    "test_cases_variables_overview"
  ],
  "index_keywords": [
    "accessing in steps",
    "in steps",
    "saving response data into",
    "setting",
    "setting value of",
    "setting variable values"
  ],
  "index_keyword_paths": [
    "accessing variables > in steps",
    "global variables > accessing in steps",
    "global variables > saving response data into",
    "global variables > setting",
    "setting variable values",
    "variables > accessing in steps",
    "variables > saving response data into",
    "variables > setting value of"
  ],
  "related_links": [
    "test_cases_store_response.htm#1320078"
  ],
  "images": [
    "topics/images/test_cases_9.1.jpg",
    "topics/images/test_cases_2.4.jpg"
  ],
  "content_hash": "2cd15824b6eeeae7",
  "level": 2
}
---

# Setting and accessing variables in test case steps > Setting and accessing variables in test case steps > To set variable values

You can create variables in any of the following ways:



Set the value directly

Use an eval action with the set (local) or gset (global) command, for example,

> **Note:** Note The global variables and parameter values are always type string. When language is Python, variables must be type casted when used as any other type.



Save an entire response into a variable:

See Storing a response into a variable (for use later in the test).



Save the result of a query or other extractor in an analysis rule

1. 1

1. In an analysis rule Perform property, specify Store.

1. 2

1. Click to access the Analysis Rule Properties section. It changes to .

1. 3

1. In the Processors group, select Store.

1. 4

1. In the step properties, check or uncheck the Make it global property as appropriate.

![screenshot](topics/images/test_cases_9.1.jpg) <!-- image_chunk: img_bf99f5d4b02441ef -->

![screenshot](topics/images/test_cases_2.4.jpg) <!-- image_chunk: img_79d7b081a1844a5c -->
