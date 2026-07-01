---
{
  "chunk_id": "parameters_custom_types__defining_custom_types_646be3ba66423bea",
  "source_file": "topics/parameters_custom_types.htm",
  "source_original_path": "topics/parameters_custom_types.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Custom Types",
    "Defining Custom Types"
  ],
  "heading_path": [
    "Defining Custom Types",
    "Defining Custom Types"
  ],
  "anchor": "1470355",
  "context_ids": [
    "parameters_custom_types"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "parameters.03.htm#1135303",
    "parameters_page.htm#1135242"
  ],
  "images": [],
  "content_hash": "646be3ba66423bea",
  "level": 1
}
---

# Defining Custom Types > Defining Custom Types

On the Custom types tab, click to add a new custom parameter type and the name field becomes available. Enter the custom type name and details as described below.

| Name | Provide a meaningful, short name. This string appears as an option in the Type dropdown list on the Parameter editor. See Step 4 on page 985, section “Working with parameters: The Parameters page”. |
| --- | --- |
| Details | Click and the Details panel appears. Enter name of the Type value and description You may define multiple item names and description. |
| Name: Enter a name of the Type value. This name will appear as a value when the custom type name (entered above) is selected on the Parameters tab. See Step 4 on page 985, section “Working with parameters: The Parameters page”. Note You cannot enter duplicate names. | Note |
| Note | You cannot enter duplicate names. |
| Description: Enter text to describe the item. |  |

Custom types page toolbar

| Add | Add a new named parameter type definition. |
| --- | --- |
| Remove | Delete the selected parameter type definition. |
| Move Up / Move Down | Move the selected parameter type/value definition up or down in the list. When you select a parameter type and then select a value, the dropdown list displays the values in the listed order. |

> **Note:** Note The custom parameter type and elements you define displays as an option that you can select to indicate the parameter types and values.

The following applies when working with parameter files that has Custom Type and Value defined:

- A parent parameter file has access to the custom parameter types and values defined in the included children parameter files.

- A child parameter file and parent parameter files cannot define identical custom Type name with different details/item name (value).

In such cases, when you select the custom type (identical Types with different values) in the parent file, a warning message displays saying that “custom type is defined in the dependent files with different items”.

- Inheritance of parameters

A session profile (e.g., Session_one) referencing another session profile (e.g., Session_two via This session profile inherits settings from another session profile) has access to the custom parameter types and values defined in the referenced session (e.g., Session_two) profile.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
