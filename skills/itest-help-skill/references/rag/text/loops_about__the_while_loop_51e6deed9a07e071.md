---
{
  "chunk_id": "loops_about__the_while_loop_51e6deed9a07e071",
  "source_file": "topics/loops_about.htm",
  "source_original_path": "topics/loops_about.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic"
  ],
  "heading_path": [
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic",
    "The while loop"
  ],
  "anchor": "1085026",
  "context_ids": [
    "loops_about"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "for loop > defined",
    "foreach loop > defined",
    "if-then logic > defined",
    "while loop > defined"
  ],
  "related_links": [
    "action_while.htm#1518303"
  ],
  "images": [
    "topics/images/loops.4.jpg",
    "topics/images/while_python.png"
  ],
  "content_hash": "51e6deed9a07e071",
  "level": 2
}
---

# Overview: Loops and flow‑control logic > Overview: Loops and flow‑control logic > The while loop

A while loop repeats a group of steps until a specified condition is no longer true. The while loop consists of a group of steps and a condition. The condition is first evaluated. If the condition is true, then the steps are executed. This repeats until the condition becomes false.

For example in Tcl, while $port < [param portCount] means: While the value of the port variable is less than the number of ports on the card (the value of the portCount parameter), repeat the loop. As soon as the port number is greater than or equal to portCount, leave the loop and continue executing at the first step after the while loop.

For example in Python, while port < int(param('PortCount')) means: While the value of the port variable is less than the number of ports on the card (the value of the portCount parameter), repeat the loop. As soon as the port number is greater than or equal to portCount, leave the loop and continue executing at the first step after the while loop

See The while action: Repeat the steps in a ‘while’ loop for instructions on creating a while loop and a detailed description of how while loops operate.

![screenshot](topics/images/loops.4.jpg) <!-- image_chunk: img_25dfce68185a85c3 -->

![screenshot](topics/images/while_python.png) <!-- image_chunk: img_e016814096e0e563 -->
