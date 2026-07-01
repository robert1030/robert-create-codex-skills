---
{
  "chunk_id": "action_write__response_mapping_in_the_procedure_78ebdc6cfcba69fb",
  "source_file": "topics/action_write.htm",
  "source_original_path": "topics/action_write.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘write’ action: Adding text into the response of a call step"
  ],
  "heading_path": [
    "The ‘write’ action: Adding text into the response of a call step",
    "The ‘write’ action: Adding text into the response of a call step",
    "Tips on using ‘write’ and ‘return’ steps to prepare useful response data for called procedures",
    "Response mapping in the procedure"
  ],
  "anchor": "1427380",
  "context_ids": [
    "action_write"
  ],
  "index_keywords": [
    "returning from",
    "returning from procedures",
    "write",
    "write action"
  ],
  "index_keyword_paths": [
    "actions > write",
    "calls > returning from",
    "procedures > returning from",
    "returning from procedures",
    "write action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "78ebdc6cfcba69fb",
  "level": 3
}
---

# The ‘write’ action: Adding text into the response of a call step > The ‘write’ action: Adding text into the response of a call step > Tips on using ‘write’ and ‘return’ steps to prepare useful response data for called procedures > Response mapping in the procedure

- To make response mapping easier, you can use the format action to create more structure to the text that you write into the response. For example, if you are building a table of information to be returned to the caller, you could use something like this to produce a nicely formatted table that is easy to create a response map for:

eval set fmt "%-25s %5d"

write format $fmt "Description" "Count"

write format $fmt "-----------" "-----"

eval set count 0

foreach val $values

eval incr count

write format $fmt $val $count

- In cases where you want to return several individual values, response mapping can still help. Place each value on a line with the name, followed by a colon, followed by the value. In this format, you can even use automatic response mapping to generate a very powerful map.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
