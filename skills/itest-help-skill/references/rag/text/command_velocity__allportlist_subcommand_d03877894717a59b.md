---
{
  "chunk_id": "command_velocity__allportlist_subcommand_d03877894717a59b",
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
    "allPortList subcommand:"
  ],
  "anchor": "1383986",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d03877894717a59b",
  "level": 3
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > allPortList subcommand:

The velocity allPortList subcommand returns all ports that were created on the device.

To make the return value useful as a session property that requires port list, the return value is a string value of comma‑separated port numbers.

Example Tcl: [velocity allPortList -id resource_0]

Example Python: velocity("allPortList", "-id", "resource_0")

You can specify the device in the same way as for the property subcommand.

> **Note:** Note The subcommand allPortList returns port numbers only and not the port names.
