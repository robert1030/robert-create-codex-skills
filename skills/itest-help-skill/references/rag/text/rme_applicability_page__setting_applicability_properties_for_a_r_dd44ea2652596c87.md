---
{
  "chunk_id": "rme_applicability_page__setting_applicability_properties_for_a_r_dd44ea2652596c87",
  "source_file": "topics/rme_applicability_page.htm",
  "source_original_path": "topics/rme_applicability_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Applicability page"
  ],
  "heading_path": [
    "Response Map editor: Applicability page",
    "Response Map editor: Applicability page",
    "Setting applicability properties for a response map"
  ],
  "anchor": "1106110",
  "context_ids": [
    "rme_applicability_page"
  ],
  "index_keywords": [
    "Applicability page",
    "Response Map editor",
    "specifying when to use"
  ],
  "index_keyword_paths": [
    "Applicability page > Response Map editor",
    "Response Map editor > Applicability page",
    "response maps > specifying when to use"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "dd44ea2652596c87",
  "level": 2
}
---

# Response Map editor: Applicability page > Response Map editor: Applicability page > Setting applicability properties for a response map

Whenever a test case step executes, iTest compares the session type, action, command, and other conditions of the step to the applicability conditions specified for all response maps that appear in response map libraries associated with the session profiles for sessions in the test case. For each map, if all of the conditions match, then iTest applies the map to the response in priority order.

1. To set the applicability properties, first open the Applicability page and then configure the following property settings:

| Session types | Optional: Select all session types for which this response map applies. |
| --- | --- |
| Action | Optional Specify the action in a step that results in a response to which the response map should be applied. |
| Command | Specify the text string of the command in a step that results in a response to which the response map should be applied. |
| Compare properties using | Specify how to interpret the contents of the properties. |
| Map Priority | When multiple response maps apply, iTest applies the maps in priority order. Lower number are higher in priority (for example, 1 is higher priority than 10). Specify the value so that users can choose the order in which multiple applicable maps are considered. |

1. 2

1. Save the response map.

1. 3

1. Add the response map to a response map library. The map must appear in a library because sessions and steps check configured to look for response maps will test whether this response map is applicable during test case execution.

> **Note:** Note The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
