---
{
  "chunk_id": "action_while__the_while_action_repeat_the_steps_in_a_w_ec8053cb552da8c9",
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
    "The while action: Repeat the steps in a ‘while’ loop"
  ],
  "anchor": "1518303",
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
    "topics/images/loops_4.1.jpg",
    "topics/images/while_python.jpg"
  ],
  "content_hash": "ec8053cb552da8c9",
  "level": 1
}
---

# The while action: Repeat the steps in a ‘while’ loop > The while action: Repeat the steps in a ‘while’ loop

A while loop repeats a group of steps until a specified condition is no longer true. The while loop consists of a group of steps and a condition. The condition is first evaluated. If the condition is true, then the steps are executed. This repeats until the condition becomes false.

Tcl example, while $port < param portCount means: While the value of the port variable is less than the number of ports on the card (the value of the portCount parameter), repeat the loop. As soon as the port number is greater than or equal to portCount, leave the loop and continue executing at the first step after the while loop.

Nested loops (if, for, foreach, and while) are supported.

Python example, while port < [param(‘PortCount’)] means: While the value of the port variable is less than the number of ports on the card (the value of the PortCount parameter), repeat the loop. As soon as the port number is greater than or equal to PortCount, leave the loop and continue executing at the first step after the while loop.

Nested loops (if, for, and while) are supported.

![screenshot](topics/images/loops_4.1.jpg) <!-- image_chunk: img_6d6f072f839836f0 -->

![screenshot](topics/images/while_python.jpg) <!-- image_chunk: img_8e19eae86ef54de3 -->
