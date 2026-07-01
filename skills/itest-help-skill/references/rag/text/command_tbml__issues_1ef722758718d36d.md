---
{
  "chunk_id": "command_tbml__issues_1ef722758718d36d",
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
    "linkList subcommand: Returns list of IDs of link objects",
    "Issues"
  ],
  "anchor": "1380119",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "1ef722758718d36d",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > linkList subcommand: Returns list of IDs of link objects > Issues

- In the event that the resource was not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| tbml linkList | Returns TBML linkList values as specified. |
| --- | --- |
| tbml linkList -id ID tbml("linkList", "-id", "ID") | Example tbml linkList -id resource_0 tbml("linkList -id", "resource_0") returns link_0 and link_1 because resource_0 contains card1 which is connected using link_0, and card1 contains port1 which is connected to something using link_1 |
| tbml linkList -name namePath tbml("linkList", "-name", "namePath") | Example tbml linkList -name "myRouter card1" tbml("linkList", "-name", "myRouter", "card1") Returns link_0 and link_1 because card1 is connected using link_0, and card1 contains port1 which is connected using link_1 |
| tbml linkList -displayName displaynamePath tbml("linkList", "-displayName", "displaynamePath") | Example tbml linkList -displayName myRouter_displayName tbml("linkList", "-displayName", "myRouter_displayName") Returns link_0 and link_1 because myRouter contains card1 which is connected using link_0, and card1 contains port1 which is connected using link_1 |
| tbml linkList -id ID -name nameList tbml("linkList", "-id", "ID", "-name", "nameList") | Example tbml linkList -id myRouter -name "card1 port1" tbml("linkList", "-id", "myRouter", "-name", "card1", "port1") Returns link_1 because card1 contains port1 which is connected using link_1 |
| tbml linkList -id ID -displayName displayNamePath tbml("linkList", "-id", "ID", "-displayName", "displayNamePath") | Example tbml linkList -id myRouter -displayName "card1_displayName port1_displayName" tbml("linkList", "-id", "myRouter", "-displayName", "card1_displayName port1_displayName") Returns link_1 because card1 contains port1 which is connected using link_1 |
