---
{
  "chunk_id": "command_tbml__issues_bb82090bd65bd700",
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
    "endpoint subcommand: Return resource IDs of two endpoint resources",
    "Issues"
  ],
  "anchor": "1380077",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "bb82090bd65bd700",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > endpoint subcommand: Return resource IDs of two endpoint resources > Issues

- If the link is not found, iTest generates an onInterpreterError execution issue.

- The starting link should be unique. If multiple links are found, iTest generates an onInterpreterError execution issue.

| tbml endpoint | Returns TBML endpoint values as specified. |
| --- | --- |
| tbml endpoint -name name tbml("endpoint", "-name", "name") | Returns the two endpoint resource IDs in a list for any link object given its name. Multiple matches are found if multiple links have the same name. Note namePath argument is not supported because link elements cannot be hierarchical. Example tbml endpoint -name upstream tbml("endpoint", "-name", "upstream") Returns resource_0 and resource_1 because the two resources are at either end of the link with a name of upstream. |
| Note | namePath argument is not supported because link elements cannot be hierarchical. |
| tbml endpoint -displayName displayName tbml("endpoint", "-displayName", "displayName") | Returns the two endpoint resource IDs in a list for the link object specified by its displayName. Multiple matches are found if multiple links have the same displayName. Note displayNamePath argument is not supported because link elements cannot be hierarchical. Example tbml endpoint -displayName upstream_displayName tbml("endpoint", "-displayName", "upstream_displayName") Returns resource_0 and resource_1 if the two resources are at either end of the link with a displayName of upstream_displayName. |
| Note | displayNamePath argument is not supported because link elements cannot be hierarchical. |
| tbml endpoint -id ID tbml("endpoint", "-id", "ID") | Returns the two endpoint resource IDs in a list for the link object that is specified by ID. Note The namePath and displayNamePath arguments are not supported because link elements cannot be hierarchical. Example tbml endpoint -id link_0 tbml("endpoint", "-id", "link_0") Returns resource_0 and resource_1 because the two resources are at either end of the link. |
| Note | The namePath and displayNamePath arguments are not supported because link elements cannot be hierarchical. |
