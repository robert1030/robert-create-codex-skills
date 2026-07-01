---
{
  "chunk_id": "sample__intro_010a6aa502e0ab3d",
  "source_file": "topics/popups/sample.html",
  "source_original_path": "topics/popups/sample.html",
  "toc_path": null,
  "heading_path": [
    "sample.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacement_char.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html",
    "help::/com.fnfr.svt.help/topics/command_syntax.html",
    "help::/com.fnfr.svt.help/topics/action_for.html"
  ],
  "images": [
    "images/for_loop_example.jpg"
  ],
  "content_hash": "010a6aa502e0ab3d",
  "level": 0
}
---

# sample.html

To insert a char command, right-click in the field and then select Insert > Non-Printing Character.

For details, see the online help: Placing non-printing characters into commands and properties.

Also, see: Field replacements: Substituting values into properties and commands.

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

A for loop executes a group of steps a specified number of times. For example, repeat the steps within the loop 10 times.

The Command of the for statement takes three clauses enclosed in { and } characters. The for loop is composed of all of the steps that are indented under the EXEC for clause.

Nested loops (if, for, foreach, and while) are supported.

See the online help for details.

Example

for���� {set i 1} {$i < 10} {incr i}

The for loop in the example follows this logic:

- Evaluate (execute) set i 1 one time upon entering the loop. This clause initializes the value that controls the loop. The default initial value of i is 0, but you can replace 0 with any value.
- Evaluate the expression $i < 10. (You can replace 10 with any value greater than the initial value of i.)
- Evaluate incr i after the last step in the for construct. The clause increments the value used to control the loop. (Use a negative value to decrement.)
- Repeat steps 2 and 3 until $i < 10 is False.

Here is an image of a comment:

Here is a link to the help page.

![screenshot](images/for_loop_example.jpg) <!-- image_chunk: img_f565b84b3e8b34e4 -->
