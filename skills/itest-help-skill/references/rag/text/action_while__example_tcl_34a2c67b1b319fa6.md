---
{
  "chunk_id": "action_while__example_tcl_34a2c67b1b319fa6",
  "source_file": "topics/action_while.htm",
  "source_original_path": "topics/action_while.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "While loops",
    "The while action: Repeat the steps in a ‘while’ loop"
  ],
  "heading_path": [
    "The while action: Repeat the steps in a ‘while’ loop",
    "The while action: Repeat the steps in a ‘while’ loop",
    "Example Tcl"
  ],
  "anchor": "1518344",
  "context_ids": [
    "action_while"
  ],
  "index_keywords": [
    "while",
    "while loops"
  ],
  "index_keyword_paths": [
    "actions > while",
    "loops > while",
    "while loops"
  ],
  "related_links": [],
  "images": [
    "topics/images/loops_2.4.jpg"
  ],
  "content_hash": "34a2c67b1b319fa6",
  "level": 3
}
---

# The while action: Repeat the steps in a ‘while’ loop > The while action: Repeat the steps in a ‘while’ loop > Example Tcl

The first eval command initializes the port variable.

In the while command, the expression $port<[param portCount] (port < [param(‘PortCount’)] in Python) compares port to the upper limit of port count for the device to ensure that port is a reasonable port number for the device. (The port count for the device is determined by a command field replacement that evaluates the portCount parameter [whose value is set in the device definition].)

The interface ethernet $port action performs the interface ethernet command for the current port number.

The last eval action implements a intrepreter (Tcl or Python) command field replacement. Tcl interprets incr port to increment the port variable and return its new value. Python and interprets port+=1 to increment the port variable and return its new value. This action fetches the value for the show interfaces command, and also has the side-effect of providing the new value for the while command to test.

When the CLI command analysis ends, the while command is again evaluated. Once the value of port exceeds the portCount for the device, the while command ends and execution continues at the step after the while construct.

![screenshot](topics/images/loops_2.4.jpg) <!-- image_chunk: img_167203892dc06318 -->
