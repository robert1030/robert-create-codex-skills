---
{
  "chunk_id": "jsonselect__intro_c387ed154096d003",
  "source_file": "popups/jsonSelect.html",
  "source_original_path": "popups/jsonSelect.html",
  "toc_path": null,
  "heading_path": [
    "jsonSelect.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_json_select.html"
  ],
  "images": [],
  "content_hash": "c387ed154096d003",
  "level": 0
}
---

# jsonSelect.html

Use jsonSelect command to get the node value from the json_string, based on the provided query_xpath. The command returns the value of the specific node based on the provided xpath.

Note: The xpath should be a valid xpath for XML (not the JsonPath - http://goessner.net/articles/JsonPath/), otherwise no value is returned. The provided json string will be converted to xml first, and then evaluated using the xpath and gets the specific value.

Syntax: jsonSelect json_string query_xpath json_string is the valid json string. Query_xpath is the valid xpath for xml. Note: If the xpath location is not a single value, then an assembled version of sub values will be retrieved.

For details on Get the node value from json string, see the online help: jsonSelect command.
