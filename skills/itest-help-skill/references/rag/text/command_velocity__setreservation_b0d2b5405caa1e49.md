---
{
  "chunk_id": "command_velocity__setreservation_b0d2b5405caa1e49",
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
    "setReservation"
  ],
  "anchor": "1405989",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b0d2b5405caa1e49",
  "level": 3
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > setReservation

The setReservation subcommand allows you to specify (programmatically) an active reservation ID to be used in a test case so that you can run a test case against a reservation made outside the scope of iTest.

For example, assign reservation with current testcase:

Tcl: velocity setReservation -reservationId <reservationId>

Python: velocity("setReservation", "-reservationId", "<reservationId>")
