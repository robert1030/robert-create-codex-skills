---
{
  "chunk_id": "command_velocity__getreservationdetails_subcommand_eeccccaec57f3724",
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
    "getReservationDetails subcommand"
  ],
  "anchor": "1588261",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "eeccccaec57f3724",
  "level": 3
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > getReservationDetails subcommand

The Velocity getReservationDetails subcommand returns reservation details in JSON format. Returned JSON corresponds to the JSON response returned by the following Velocity API call:

GET /velocity/api/reservation/v23/reservation/{reservationId}

You may use the Velocity getReservationDetails subcommand to poll the status of a reservation created with makeReservation command.
