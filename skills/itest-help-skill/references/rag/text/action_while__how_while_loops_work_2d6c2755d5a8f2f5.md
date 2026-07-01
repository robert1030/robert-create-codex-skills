---
{
  "chunk_id": "action_while__how_while_loops_work_2d6c2755d5a8f2f5",
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
    "How While loops work"
  ],
  "anchor": "1518319",
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
    "topics/images/loops_3.3.jpg"
  ],
  "content_hash": "2d6c2755d5a8f2f5",
  "level": 3
}
---

# The while action: Repeat the steps in a ‘while’ loop > The while action: Repeat the steps in a ‘while’ loop > How While loops work

A while loop repeats a group of steps until a specified condition is no longer true. The while loop consists of a group of steps and a condition. The condition is first evaluated. If the condition is true, then the steps are executed. This repeats until the condition becomes false.

For example, while the value of the port variable is less than the number of ports on the card (the value of the portCount/PortCount parameter), repeat the loop. As soon as the port number is greater than or equal to portCount, leave the loop and continue executing at the first step after the while loop.

Notice that the while logic checks the condition before the steps within the loop are executed, so you'll typically initialize the variable that is tested in the condition.

![screenshot](topics/images/loops_3.3.jpg) <!-- image_chunk: img_800cc0b83b4aa946 -->
