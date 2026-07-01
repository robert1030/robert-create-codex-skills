---
{
  "chunk_id": "action_elseif__the_elseif_elif_action_element_of_an_if__58c7852c317282cb",
  "source_file": "topics/action_elseif.htm",
  "source_original_path": "topics/action_elseif.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "If / then / else logic",
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct"
  ],
  "heading_path": [
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct",
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-elseconstruct"
  ],
  "anchor": "1519025",
  "context_ids": [
    "action_elseif"
  ],
  "index_keywords": [
    "Element of an if/then or if-else-elif construct” on page 325",
    "elseif or elif",
    "elseif or elif action"
  ],
  "index_keyword_paths": [
    "actions > elseif or elif",
    "elseif or elif action",
    "“The ‘if’ action > Element of an if/then or if-else-elif construct” on page 325"
  ],
  "related_links": [
    "action_if.htm#1518551"
  ],
  "images": [
    "topics/images/loops_9.1.jpg",
    "topics/images/loops_3.2.jpg"
  ],
  "content_hash": "58c7852c317282cb",
  "level": 1
}
---

# The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct > The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-elseconstruct

> **Note:** Note Python uses the if-elif-else construct. The ‘if’ action: Element of an if/then or if-elif-else construct.

An EXEC elseif/elif step is legal only when it immediately follows an if statement or another elseif/elif statement. The command for elseif /elif contains an assertion. If no previous if or elseif/elif step that is associated with the elseif/elif was True and the elseif/elif assertion is True, then its nested steps will be executed.

If a previous if or elseif/elif assertion was True, then the elseif/elif assertion not tested.

![screenshot](topics/images/loops_9.1.jpg) <!-- image_chunk: img_4690154141cc7a00 -->

![screenshot](topics/images/loops_3.2.jpg) <!-- image_chunk: img_8e3eb3304817f2b1 -->
