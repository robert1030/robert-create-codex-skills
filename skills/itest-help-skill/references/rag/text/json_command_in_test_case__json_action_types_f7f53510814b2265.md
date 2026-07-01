---
{
  "chunk_id": "json_command_in_test_case__json_action_types_f7f53510814b2265",
  "source_file": "topics/json_command_in_test_case.htm",
  "source_original_path": "topics/json_command_in_test_case.htm",
  "toc_path": [
    "iTest Online Help",
    "JSON Editor",
    "JSON Command in Test Case"
  ],
  "heading_path": [
    "JSON Command in Test Case",
    "JSON Command in Test Case",
    "JSON Action Types"
  ],
  "anchor": "1349831",
  "context_ids": [
    "json_command_in_test_case"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "f7f53510814b2265",
  "level": 2
}
---

# JSON Command in Test Case > JSON Command in Test Case > JSON Action Types

iTest supports five action types for the JSON step.

| JSON Action | Example |
| --- | --- |
| createJson | Creates new JSON document from file URI or JSON string. json -action createJson -documentName myJsonDocument -fileURI ’project://my_project/jsonFiles/json.txt’ Creates from JSON String: json -action createJson -documentName myJsonDocument -jsonString {’name1’:’value1’} |
| setJson | Defines parameter with ’original json’ string and ’newValue’. json -action setJsonValue -documentName myJsonDocument -pathValue {’true’:true, ’false’:false, ’nullValue’: null} Note To modify a JSON key, you may delete an existing key and insert a new key. |
| Note | To modify a JSON key, you may delete an existing key and insert a new key. |
| getJsonNode | Get the value of a JSON node json -action getJsonNode -documentName myJsonDocument -pathValue {’object/c/[1]’} Note pathValue is a string of the path. Gets value of only one JSONnode. |
| Note | pathValue is a string of the path. Gets value of only one JSONnode. |
| deleteJsonNode | Deletes an existing JSON json -action deleteJsonNode -documentName myJsonDocument -pathValue {’key1/[0]’, ’array/[4]/[1]’, ’myKey1’, ’myKey2’} Note pathValue is an array of key paths (no need JSON object syntax is required). |
| Note | pathValue is an array of key paths (no need JSON object syntax is required). |
| addJsonNode | Add new node into a JSON document json -action addJsonNode -documentName myJsonDocument -pathValue {’/’:{’newNode1’:’newValue1’, ’newNode2’:{’n2’:’V2’}}} |
