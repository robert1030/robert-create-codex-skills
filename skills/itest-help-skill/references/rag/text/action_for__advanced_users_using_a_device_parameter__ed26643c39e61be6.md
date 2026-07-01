---
{
  "chunk_id": "action_for__advanced_users_using_a_device_parameter__ed26643c39e61be6",
  "source_file": "topics/action_for.htm",
  "source_original_path": "topics/action_for.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "For and ForEach loops",
    "The for action: Execute a group of steps in a loop"
  ],
  "heading_path": [
    "The for action: Execute a group of steps in a loop",
    "The for action: Execute a group of steps in a loop",
    "Advanced users: Using a device parameter to set the loop count dynamically"
  ],
  "anchor": "1518049",
  "context_ids": [
    "action_for"
  ],
  "index_keywords": [
    "for",
    "for action",
    "for loops"
  ],
  "index_keyword_paths": [
    "actions > for",
    "for action",
    "for loops",
    "loops > for"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ed26643c39e61be6",
  "level": 3
}
---

# The for action: Execute a group of steps in a loop > The for action: Execute a group of steps in a loop > Advanced users: Using a device parameter to set the loop count dynamically

In a more advanced case, you might use a parameter defined for the device that specifies the number of ports on the device (instead of the hard-coded number 10, as in the previous example).

1. Let's say that, for the session profile named router, we have defined a parameter named port_count, and, for this particular device, given it the value 4.

1. 2

1. Now, in the Command for the for step, we can replace the hard-coded value 10 with a param command that evaluates the port_count parameter. (The appropriate session must be specified for the steps in the for loop.)

{set port_number 0} {$port_number [param port_count]} {incr port_number}

As a result, the Command evaluates to:

{set port_number 0} {$port_number<4} {incr port_number}

So, the loop now repeats for exactly the number of ports on the device. The test can now be used with a device with any number of ports because the port count used to control the loop dynamically takes on the port count defined for the device by the port_count parameter.
