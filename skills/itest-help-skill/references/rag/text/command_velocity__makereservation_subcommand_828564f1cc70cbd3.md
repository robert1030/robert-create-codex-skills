---
{
  "chunk_id": "command_velocity__makereservation_subcommand_828564f1cc70cbd3",
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
    "makeReservation subcommand"
  ],
  "anchor": "1402785",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "828564f1cc70cbd3",
  "level": 3
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand

The velocity makeReservation subcommand returns the reservation and topology ID. You may use the optional 'priority’ argument to specify the reservation priority (reservation is outside the scope of iTest).

Tcl: velocity makeReservation -topologyName <topologyName> -duration <duration> -name <reservationName>, -priority, <priorityLevel>, <conditions>

Python: velocity('makeReservation', '-topologyName', '<topologyName', '-duration', '<duration>', '-name', '<reservation_name>', '-priority', '<priorityLevel>', '<conditions>')
