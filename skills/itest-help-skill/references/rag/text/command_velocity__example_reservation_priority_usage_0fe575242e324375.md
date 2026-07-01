---
{
  "chunk_id": "command_velocity__example_reservation_priority_usage_0fe575242e324375",
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
    "Example Reservation Priority usage"
  ],
  "anchor": "1584118",
  "context_ids": [
    "command_velocity"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/topologies_9.1.jpg",
    "topics/images/velo_topo_makeReservation_withPriority_testExecution.png"
  ],
  "content_hash": "0fe575242e324375",
  "level": 4
}
---

# Commands that return information from Velocity > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand > Example Reservation Priority usage

The following is an example of Velocity makeReservation command usage with reservation priority.

When executing the test, iTest displays an error if the priority specified is greater than the level defined for user (by Admin user in Velocity) and if there is reservation conflict.

The test execution step executes and returns reservation ID if the priority level specified in the test case step is the within the range of priority level assigned to the user. See Velocity Online Help for details of Reservation Priority

![screenshot](topics/images/topologies_9.1.jpg) <!-- image_chunk: img_b50e4c6bd517a8a3 -->

![screenshot](topics/images/velo_topo_makeReservation_withPriority_testExecution.png) <!-- image_chunk: img_64b26031af6dde56 -->
