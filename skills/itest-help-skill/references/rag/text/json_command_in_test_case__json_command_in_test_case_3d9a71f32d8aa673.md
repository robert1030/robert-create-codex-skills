---
{
  "chunk_id": "json_command_in_test_case__json_command_in_test_case_3d9a71f32d8aa673",
  "source_file": "topics/json_command_in_test_case.htm",
  "source_original_path": "topics/json_command_in_test_case.htm",
  "toc_path": [
    "iTest Online Help",
    "JSON Editor",
    "JSON Command in Test Case"
  ],
  "heading_path": [
    "JSON Command in Test Case",
    "JSON Command in Test Case"
  ],
  "anchor": "1327517",
  "context_ids": [
    "json_command_in_test_case"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "field_replacements_tasks.htm#",
    "test_case_editor_overview.htm#",
    "tce_step_properties_general.htm#1973025",
    "#1349831"
  ],
  "images": [
    "topics/images/json_testCase.png"
  ],
  "content_hash": "3d9a71f32d8aa673",
  "level": 1
}
---

# JSON Command in Test Case > JSON Command in Test Case

Once you have competed including all the information as required on the wizard, only one JSON command will be inserted into the test case.

The arguments would appear both in the Description column of the test case and the Step Properties, and be synchronized.

JSON command does not support command field level substitution.When using field replacements, ensure that you enable field substitution from the sections:

Step Properties > EXEC json Properties > Json Step Properties.

See also Chapter , “Field Replacements” and Chapter , “Test Case Editor”, section Step Properties section: General properties group.

Json Step Properties

| Action | The session-specific action specified for the step. See JSON Action Types. |
| --- | --- |
| From File | Select file and the file URL becomes available. |
| File URL | Enter the file URL or click browse and select a file either from Workspace or File location. |
| Json String | For example, {‘newField’:5} from a JSON document: action='createJson', documentName='demo', fromFile='false', jsonString='{’newField’:5}' |
| Path-Value | Set JSON value in the document. Example, {[i]:’OK’} |
| Perform action on response structure | Select true or false, as required. Perform this action on the procedure's response structure is enabled if action = getJsonNode, addJsonNode, deleteJsonNode, setJsonValue. |
| Document Name | Enter the JSON document name |
| Global scope | Select to indicate whether the JSON command performs thread-safe operations on a document in local or global space. That is, to reference a simple variable name that either exists in local namespace (Global scope is un-checked) or global namespace (Global scope is checked). |

![screenshot](topics/images/json_testCase.png) <!-- image_chunk: img_87a9b67de4c8c962 -->
