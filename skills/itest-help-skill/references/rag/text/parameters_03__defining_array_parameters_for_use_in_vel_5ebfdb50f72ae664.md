---
{
  "chunk_id": "parameters_03__defining_array_parameters_for_use_in_vel_5ebfdb50f72ae664",
  "source_file": "topics/parameters.03.htm",
  "source_original_path": "topics/parameters.03.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Defining and managing parameters",
    "Defining a parameter"
  ],
  "heading_path": [
    "Defining a parameter",
    "Defining a parameter",
    "Defining array parameters for use in Velocity"
  ],
  "anchor": "1620622",
  "context_ids": [],
  "index_keywords": [
    "defining",
    "multiple values",
    "multiple values for parameter",
    "setting values"
  ],
  "index_keyword_paths": [
    "multiple values for parameter",
    "parameter > multiple values",
    "parameters > defining",
    "parameters > setting values"
  ],
  "related_links": [],
  "images": [
    "topics/images/array_param_PythonSplit.png",
    "topics/images/array_param_TCLSplit.png"
  ],
  "content_hash": "5ebfdb50f72ae664",
  "level": 2
}
---

# Defining a parameter > Defining a parameter > Defining array parameters for use in Velocity

Array parameters in iTest are defined as sets of parameters with duplicated names or paths. Velocity and Network DevOps Agent do not support array parameters defined as sets of parameters with duplicated names or paths.

If you wish to run your testcase on Velocity and Network DevOps Agent, define an array as a single parameter value and then use expressions inside the testcase to split the value into array elements.

For example, a string value with delimiters separating individual elements can be used along with a Python/Tcl expression in the testcase steps to split the single value into multiple elements. iTest built-in actions (for, foreach) may be used to iterate over split values. The testcase and parameter file when exported to Velocity preserves the element order.

The examples below show array parameter definition using single parameter value in Python and Tcl.

Example: Parameter array—Python definition

Example: Parameter array—Tcl definition.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/array_param_PythonSplit.png) <!-- image_chunk: img_00bbf5a242b150fb -->

![screenshot](topics/images/array_param_TCLSplit.png) <!-- image_chunk: img_0e2b197bfe484f69 -->
