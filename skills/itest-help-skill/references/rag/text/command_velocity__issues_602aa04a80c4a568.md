---
{
  "chunk_id": "command_velocity__issues_602aa04a80c4a568",
  "source_file": "topics/command_velocity.htm",
  "source_original_path": "topics/command_velocity.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Velocity command",
    "Commands that return information from Velocity"
  ],
  "heading_path": [
    "Commands that return information from Velocity",
    "Commands that return information from Velocity",
    "velocity command syntax",
    "property subcommand: Return value of a property",
    "Issues"
  ],
  "anchor": "1384034",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "602aa04a80c4a568",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > property subcommand: Return value of a property > Issues

- If a resource or link with the specified id or name is not found, and a default value is not specified using the -default (default in Python) argument, then iTest generates an onInterpreterError execution issue.

- In the event that the resource was not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The specified resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| velocity property -id ID propertyName velocity("property", "-id", "ID", "propertyName") | For a resource or link with ID of ID, returns the value of the property with propertyName. Example velocity property -id resource_0 name velocity("property", "-id", "resource_0", "name") returns the value of the name property for the resource with ID resource_0. |
| --- | --- |
| velocity property -name name propertyName velocity("property", "-name", "name", "propertyName"",) | Returns the value of the property specified by propertyName for the resource or link specified by name. Example velocity property -name myRouter myCustomProperty velocity("property", "-name", "myRouter", "myCustomProperty") First, finds the resource card1.We specified the full name path starting from the top level resource which is myRouter. 2. Then finds the value for myCustomProperty, which is a child of the property collection group called my property collection. |
|  | First, finds the resource card1.We specified the full name path starting from the top level resource which is myRouter. |
| 2. | Then finds the value for myCustomProperty, which is a child of the property collection group called my property collection. |
