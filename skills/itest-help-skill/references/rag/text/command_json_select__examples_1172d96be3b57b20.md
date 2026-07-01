---
{
  "chunk_id": "command_json_select__examples_1172d96be3b57b20",
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
    "jsonSelect command: Get the node value from json string based on the query xpath",
    "Examples"
  ],
  "anchor": "1847414",
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
  "content_hash": "1172d96be3b57b20",
  "level": 2
}
---

# jsonSelect command: Get the node value from json string based on the query xpath > jsonSelect command: Get the node value from json string based on the query xpath > Examples

Tcl: {"array":[1,2.4,"null1":null,"i":"j","k":"l"}],"boolean":true,"new":"notNull","number":123,"object":{"a":"b","c":"d","e":"f"},"string":"Hello World","null2":null}

Python:

eval jsonSelect("{'array':[1,2.4,{'null1':'None','i':'j','k':'l'}],'boolean':'True','new':'notNull','number':123,'object':{'a':'b','c':'d','e':'f'},'string':'Hello World','null2':'None'}", "array/item[3]/i")

| xpath | value | comment |
| --- | --- | --- |
| number | 123 | - |
| array/item[1] | 1 | The array type in json will be converted to xml string with an additional "item" key. |
| array/item[3]/i | j |  |
| object/c | d | - |
| object | bdf | The xpath "object" represents an object type in json, thus we can only get the values based on the converted xml contents. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
