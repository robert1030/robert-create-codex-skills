---
{
  "chunk_id": "command_velocity__arguments_0ed108c4c70518e4",
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
    "findReservations subcommand",
    "Arguments:"
  ],
  "anchor": "1404302",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "0ed108c4c70518e4",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > findReservations subcommand > Arguments:

| name | Name of the reservation. Search with using wildcard. I.e. use substring in place of real reservation name. (String, optional) |
| --- | --- |
| status | The following lists the valid values (string, optional): STANDBY: Reservation will wait until the work order is completed. PENDING_APPROVAL: Valid only for future reservations, that is, the reservation is waiting for approval and will fail if not approved. SCHEDULED: Reservation is scheduled for a future date and time. ACTIVATING: Reservation is in the process of being activated. That is, the activation procedures are in progress (including startup tasks). ACTIVE: Reservation is currently active. DEACTIVATING: The deactivation procedures are in progress (including teardown tasks). COMPLETED: Reservation was completed (past). SUSPENDED: Applies only for recurring reservations; For example, Canceling a recurring reservation cancels future events, and the reservation shows as in a Suspended status. DECLINED: Reservation was declined FAILED: Reservation failed due to an of these reasons: not approved before start. CANCELLED: Reservation is canceled (by user, by admin, as part of a declined escalation request, etc.) TERMINATED: Reservation was aborted by an Escalation Manager. UNKNOWN: Applies to private reservations. That is, the details are hidden form the requesting users. |
|  | STANDBY: Reservation will wait until the work order is completed. |
|  | PENDING_APPROVAL: Valid only for future reservations, that is, the reservation is waiting for approval and will fail if not approved. |
|  | SCHEDULED: Reservation is scheduled for a future date and time. |
|  | ACTIVATING: Reservation is in the process of being activated. That is, the activation procedures are in progress (including startup tasks). |
|  | ACTIVE: Reservation is currently active. |
|  | DEACTIVATING: The deactivation procedures are in progress (including teardown tasks). |
|  | COMPLETED: Reservation was completed (past). |
|  | SUSPENDED: Applies only for recurring reservations; For example, Canceling a recurring reservation cancels future events, and the reservation shows as in a Suspended status. |
|  | DECLINED: Reservation was declined |
|  | FAILED: Reservation failed due to an of these reasons: not approved before start. |
|  | CANCELLED: Reservation is canceled (by user, by admin, as part of a declined escalation request, etc.) |
|  | TERMINATED: Reservation was aborted by an Escalation Manager. |
|  | UNKNOWN: Applies to private reservations. That is, the details are hidden form the requesting users. |
| owner | Creator of the reservation (string, optional) |
| startTime | Search reservation that start after specified time. time format: HH:mm:ss dd.MM.yyyy Example: 08:05:00 21.09.2015 t<number> - offset from the current time in minutes Examples: 10 minutes later: t10, 10 minutes ago: t-10 |
| endTime | Search reservation that end before the specified time |
| Result (List of pair) | : <reservation_id>SPACE<reservation_name> |
