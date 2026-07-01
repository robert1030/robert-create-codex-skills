---
{
  "chunk_id": "command_velocity__arguments_8cb6d2ccf06ebedc",
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
    "setReservation",
    "Arguments:"
  ],
  "anchor": "1406366",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1404298"
  ],
  "images": [],
  "content_hash": "8cb6d2ccf06ebedc",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > setReservation > Arguments:

| reservationId | Identification number of the reservation. For example, it can be the result of findReservations subcommand. (UUID, required) Note The findReservation command returns a list of pair<id, name>, but only the id is required. For example, in order to list the id of the first reservation in list, use: eval "lrange [split $reservation] 0 0".In Python use: | Note | The findReservation command returns a list of pair<id, name>, but only the id is required. For example, in order to list the id of the first reservation in list, use: eval "lrange [split $reservation] 0 0".In Python use: |
| --- | --- | --- | --- |
| Note | The findReservation command returns a list of pair<id, name>, but only the id is required. For example, in order to list the id of the first reservation in list, use: eval "lrange [split $reservation] 0 0".In Python use: |  |  |
