---
{
  "chunk_id": "command_tbml__issues_ea3af44301f134c6",
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
    "deviceList subcommand: Return device ID",
    "Issues"
  ],
  "anchor": "1380064",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "ea3af44301f134c6",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > deviceList subcommand: Return device ID > Issues

- If the resource was not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| tbml deviceList | Returns a list of the top-level device IDs. |
| --- | --- |
| tbml deviceList -name namePath tbml("deviceList", "-name", "namePath") | Returns device IDs in a list for the specified device. Example tbml deviceList -name "myRouter card1" tbml("deviceList", "-name", "myRouter card1") Finds immediate children of card1. In the example, returns resource_0_0_0 (the ID for port1) |
| tbml deviceList -displayName displayNamePath tbml("deviceList", "-displayName", "displayNamePath") | Returns device IDs in a list for the specified device. Example tbml deviceList -name "myRouter_displayName card1_displayName" tbml("deviceList", "-name", "myRouter_displayName", "card1_displayName") Finds immediate children of card1 and returns their IDs. In the example, returns resource_0_0_0(the ID for port1) |
| tbml deviceList -id ID tbml("deviceList", "-id", "ID") | Returns device IDs in a list for the specified device. Example tbml deviceList -id resource_0 tbml("deviceList", "-id", "resource_0") Finds immediate children of resource_0. In the example, returns resource_0_0 (the ID for card1) |
| tbml deviceList -id ID -name namePath tbml("deviceList", "-id", "ID", "-name", "namePath") | Returns device IDs in a list for the specified device. Example tbml deviceList -id resource_0 -name card1 tbml("deviceList", "-id", "resource_0", "-name", "card1") Finds immediate children of card1 and returns their IDs. In the example, returns resource_0_0_0 (the ID for port1) |
| tbml deviceList -id ID -displayName displayNamePath tbml("deviceList", "-id", "ID", "-displayName", "displayNamePath") | Returns device IDs in a list for the specified device. Example tbml deviceList -id resource_0 -displayName card1_displayName tbml("deviceList", "-id", "resource_0", "-displayName", "card1_displayName") Finds immediate children of card1 and returns their IDs. In the example, returns resource_0_0_0 (the ID for port1) |
