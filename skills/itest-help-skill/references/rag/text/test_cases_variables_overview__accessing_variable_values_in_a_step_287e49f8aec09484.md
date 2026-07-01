---
{
  "chunk_id": "test_cases_variables_overview__accessing_variable_values_in_a_step_287e49f8aec09484",
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
    "Accessing variable values in a step"
  ],
  "anchor": "1175353",
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
    "command_response.htm#1698912"
  ],
  "images": [
    "topics/images/test_cases_2.5.jpg",
    "topics/images/test_cases_2.6.jpg"
  ],
  "content_hash": "287e49f8aec09484",
  "level": 2
}
---

# Setting and accessing variables in test case steps > Setting and accessing variables in test case steps > Accessing variable values in a step

Steps can access variable values in either of the following ways:

- Use an eval action with the get (local) or gget (global) command, for example,

- Use an eval action with variable syntax:

${varName} ( Tcl local)

(‘varName’) (Python local)

${/data/varName} (Tcl global)

(‘/data/varName’) (Python global)

- To return data from a variable that holds the response to an earlier step, see response command: Accessing response data that is stored in a variable.

![screenshot](topics/images/test_cases_2.5.jpg) <!-- image_chunk: img_55afdac89c3283e1 -->

![screenshot](topics/images/test_cases_2.6.jpg) <!-- image_chunk: img_24f0757157ec125d -->
