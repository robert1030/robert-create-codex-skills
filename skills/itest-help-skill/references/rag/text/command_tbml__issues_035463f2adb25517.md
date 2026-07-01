---
{
  "chunk_id": "command_tbml__issues_035463f2adb25517",
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
    "parentList subcommand: Return list of parent IDs for a resource",
    "Issues"
  ],
  "anchor": "1380105",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "035463f2adb25517",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > parentList subcommand: Return list of parent IDs for a resource > Issues

- If the resource was not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| tbml parentList | Returns TBML parentList values as specified. |
| --- | --- |
| tbml parentList -name namePath tbml("parentList", "-name", "namePath") | Example tbml parentList -name "myRouter card1 port1" tbml("parentList", "-name", "myRouter", "card1", "port1") Returns resource_0 and resource_0_0 because the specified resource is for a port, and its parents are myRouter whose ID is resource_0 and card1 whose ID is resource_0_0 |
| tbml parentList -displayName displayNamePath tbml("parentList", "-displayName", "displayNamePath") | Example tbml parentList -displayName "myRouter_displayName card1_displayName" tbml("parentList", "-displayName", "myRouter_displayName card1_displayName") Returns resource_0 because the specified ID is for a card, and its parent is myRouter whose ID is resource_0 |
| tbml parentList -id ID tbml("parentList", "-id", "ID") | Examples tbml parentList -id resource_0 tbml("parentList", "-id", "resource_0") Returns an empty list because resource_0 is a top level resource. tbml parentList -id resource_0_0_0 returns resource_0 and resource_0_0 because the specified resource is for a port, and its parents are myRouter whose ID is resource_0 and card1 whose ID is resource_0_0 |
| tbml parentList -id ID -name namePath tbml("parentList", "-id", "ID", "-name", "namePath") | Example tbml parentList id resource_0 -name card1 tbml("parentList", "id", "resource_0", "-name", "card1") Returns resource_0 because the specified ID is for myRouter, which contains a child resource named card1, and its parent is myRouter (whose ID is resource_0). |
| tbml parentList -id ID -displayName displayNamePath tbml("parentList", "-id", "ID", "-displayName", "displayNamePath") | Example tbml parentList id resource_0 -displayName "card1_displayName port1_displayName" tbml("parentList", "id", "resource_0", "-displayName", "card1_displayName port1_displayName") Returns resource_0 and resource_0_0 because the specified resource is for a port, and its parents are myRouter whose ID is resource_0 and card1 whose ID is resource_0_0 |
