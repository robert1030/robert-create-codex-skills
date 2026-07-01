---
{
  "chunk_id": "command_tbml__issues_729291769b243ad3",
  "source_file": "topics/command_tbml.htm",
  "source_original_path": "topics/command_tbml.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "\"tbml\" topology commands",
    "Commands that return information about topologies"
  ],
  "heading_path": [
    "Commands that return information about topologies",
    "Commands that return information about topologies",
    "Example topology",
    "sessionList subcommand: Return list of session names for a device",
    "Issues"
  ],
  "anchor": "1378547",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "729291769b243ad3",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > sessionList subcommand: Return list of session names for a device > Issues

- If the resource was not found or if multiple resources are found for the specified device, iTest generates an onInterpreterError execution issue.

| tbml sessionList -id ID tbml("sessionList", "-id", "ID") | Returns session names in a list for the specified device ID. Example tbml sessionList -id resource_0 tbml("sessionList", "-id", "resource_0") Returns names of all session profiles attached to resource_0 |
| --- | --- |
