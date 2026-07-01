---
{
  "chunk_id": "command_json_select__jsonselect_command_get_the_node_value_fr_e62ca5a43d456fb3",
  "source_file": "topics/command_json_select.htm",
  "source_original_path": "topics/command_json_select.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "jsonSelect command: Get the node value from json string based on the query xpath"
  ],
  "heading_path": [
    "jsonSelect command: Get the node value from json string based on the query xpath",
    "jsonSelect command: Get the node value from json string based on the query xpath"
  ],
  "anchor": "1848239",
  "context_ids": [
    "command_json_select"
  ],
  "index_keywords": [
    "jsonSelect",
    "jsonSelect command"
  ],
  "index_keyword_paths": [
    "commands > jsonSelect",
    "field replacements > jsonSelect command",
    "jsonSelect command"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e62ca5a43d456fb3",
  "level": 1
}
---

# jsonSelect command: Get the node value from json string based on the query xpath > jsonSelect command: Get the node value from json string based on the query xpath

Use jsonSelect command to get the node value from the json_string, based on the provided query_xpath. The command returns the value of the specific node based on the provided xpath.

> **Note:** Note The xpath should be a valid xpath for XML (not the JsonPath - http://goessner.net/articles/JsonPath/), otherwise no value is returned. The provided json string will be converted to xml first, and then evaluated using the xpath and gets the specific value.
