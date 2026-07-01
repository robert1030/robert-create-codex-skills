---
{
  "chunk_id": "command_json_select__syntax_4c61c2364b93a4f5",
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
    "Syntax"
  ],
  "anchor": "1847409",
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
  "content_hash": "4c61c2364b93a4f5",
  "level": 2
}
---

# jsonSelect command: Get the node value from json string based on the query xpath > jsonSelect command: Get the node value from json string based on the query xpath > Syntax

Tcl:

jsonSelect json_string query_xpath

json_string is the valid json string.

Query_xpath is the valid xpath for xml.

Python:

jsonSelect('jsonString', 'queryXpath')

json_str is the valid json string.

xpath is the valid xpath for xml.

Example: eval jsonSelect("{'key1':'value1'}", "key1")

> **Note:** Note If the xpath location is not a single value, then an assembled version of sub values will be retrieved.
