---
{
  "chunk_id": "command_velocity__example_python_usage_a1d46ca528e6c131",
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
    "Example Python usage:"
  ],
  "anchor": "1440644",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a1d46ca528e6c131",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand > Example Python usage:

velocity('makeReservation', '-topologyName', 'YK1', '-duration’, '10', ‘-name’, ’reservation_MEDIUM’, ’-priority’, ’MEDIUM’, 'PC.cond=template[PC] and ports(integer[Port Speed]>=10000)>=2', 'Server.cond=template[Server] and [Hostname]="xxxxx.xxxxx.com"' )
