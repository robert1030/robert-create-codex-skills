---
{
  "chunk_id": "command_velocity__example_tcl_usage_db1214a798e5e3cc",
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
    "makeReservation subcommand",
    "Example Tcl usage:"
  ],
  "anchor": "1402650",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "db1214a798e5e3cc",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand > Example Tcl usage:

velocity makeReservation -topologyName "YK1" -duration 10 -name "reservation_MEDIUM" -priority "MEDIUM" "PC.cond=template\[PC\] and ports(integer\[Port Speed\]>=10000)>=2" "Server.cond=template\[Server\] and \[Hostname\]=\"xxxxx.xxxxx.com\""
