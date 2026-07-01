---
{
  "chunk_id": "command_tbml__issues_d95c41bcf1a03966",
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
    "remoteEndpoint subcommand: Return the resource ID of connected resource",
    "Issues"
  ],
  "anchor": "1380036",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d95c41bcf1a03966",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > remoteEndpoint subcommand: Return the resource ID of connected resource > Issues

- If the resource is not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| tbml remoteEndpoint | Returns TBML remoteEndpointvalues as specified. |
| --- | --- |
| tbml remoteEndpoint -name namePath tbml("remoteEndpoint", "-name", "namePath") | Example tbml remoteEndpoint -name "myRouter card1" tbml("remoteEndpoint", "-name", "myRouter card1") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -displayName displayNamePath tbml("remoteEndpoint", "-displayName", "displayNamePath") | Example tbml remoteEndpoint -displayName "myRouter_displayName card1_displayName" tbml("remoteEndpoint", "-DisplayName", "myRouter_displayName card1_displayName") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID tbml("remoteEndpoint", "-id", "ID") | Example tbml remoteEndpoint -id resource_0_0 tbml("remoteEndpoint", "-id", "resource_0_0") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID -name namePath tbml("remoteEndpoint", "-id", "ID", "-name", "namePath") | Example tbml remoteEndpoint -id resource_0 -name card1 tbml("remoteEndpoint", "-id", "resource_0", "-name", "card1") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID -displayName displayNamePath tbml("remoteEndpoint", "-id", "ID" "-displayName", "displayNamePath") | Example tbml remoteEndpoint -id resource_0 -displayName card1_displayName tbml("remoteEndpoint", "-id", "resource_0", "-displayName", "card1_displayName") Returns resource_1_0 because card1 is connected to card1 on mySwitch |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
