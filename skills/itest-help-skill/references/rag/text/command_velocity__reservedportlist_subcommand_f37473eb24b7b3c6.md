---
{
  "chunk_id": "command_velocity__reservedportlist_subcommand_f37473eb24b7b3c6",
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
    "reservedPortList subcommand:"
  ],
  "anchor": "1404221",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "f37473eb24b7b3c6",
  "level": 3
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > reservedPortList subcommand:

Example Tcl: [velocity reservedPortList]

Example Python: velocity("reservedPortList")

The reservedPortList subcommand retrieves all topology ports (which might be concrete or abstract) of the specified device and then returns the list of their mappings. The return value format is the same as for the allPortList subcommand.

> **Note:** Note The subcommand reservedPortList returns port numbers only and not the port names.

You can specify the device in the same way as the property subcommand.
