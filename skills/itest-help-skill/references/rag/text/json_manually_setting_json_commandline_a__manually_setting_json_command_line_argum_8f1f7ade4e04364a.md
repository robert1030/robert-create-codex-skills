---
{
  "chunk_id": "json_manually_setting_json_commandline_a__manually_setting_json_command_line_argum_8f1f7ade4e04364a",
  "source_file": "topics/json_manually_setting_json_commandline_arguments.htm",
  "source_original_path": "topics/json_manually_setting_json_commandline_arguments.htm",
  "toc_path": [
    "iTest Online Help",
    "JSON Editor",
    "Manually setting JSON command line arguments"
  ],
  "heading_path": [
    "Manually setting JSON command line arguments",
    "Manually setting JSON command line arguments"
  ],
  "anchor": "1332205",
  "context_ids": [
    "json_manually_setting_json_commandline_arguments"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/json_manually_enter_description.png"
  ],
  "content_hash": "8f1f7ade4e04364a",
  "level": 1
}
---

# Manually setting JSON command line arguments > Manually setting JSON command line arguments

When you manually insert a JSON step (when editing a Test Case) a popup of arguments with their descriptions displays under these circumstances:

- When you enter a JSON action as a step and the description field is empty, press Ctrl + space.

- When you enter a JSON action as a step, then enter a hyphen (-) in the description.

> **Note:** Note No validation is performed for the pathValue syntax when you manually enter a pathValue argument. Your input value will be automatically be filled under the Step Properties. The pathValue under Step Properties is validated for correct syntax. If you input invalid syntax, this field will be flagged with the error.

The following rules apply when parsing the manually entered description:

- If the set of arguments is invalid, the Test Case Editor erases the text typed into the description field and the Step Properties window will not be updated.

- If the set of arguments is valid, the Test Case Editor updates (synchronizes) the Step Properties window.

> **Note:** Note The JSON step executor only uses the Step Properties for execution. Description field and step command field is only used for parsing value to Step Properties.

iTest support these command line actions to be entered manually for the JSON step.

| Command | Description |
| --- | --- |
| -action | Enter the name of Json Action Mandatory. Allowed values: createJson, getJsonNode, addJsonNode, deleteJsonNode, setJsonValue |
| -fromFile | Create json document from an existing file. Allowed value: true/false This is enabled only when action = createJson |
| -fromURI | File path used to retrieve file. This is enabled and required if action = createJson and fromFile = true. |
| -jsonString | Original Json content which is input manually. This is enabled and required if action = createJson and fromFile = false. |
| -pathValue | Path-Value used to query json node. This is enabled and required if action = getJsonNode, addJsonNode, deleteJsonNode, setJsonValue. |
| -editResponseStructure | Perform action on response structure. Allowed value: true/false This is enabled if action = getJsonNode, addJsonNode, deleteJsonNode, setJsonValue. |
| -documentName | Json Document Name. Mandatory. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/json_manually_enter_description.png) <!-- image_chunk: img_8343c75df199b931 -->
