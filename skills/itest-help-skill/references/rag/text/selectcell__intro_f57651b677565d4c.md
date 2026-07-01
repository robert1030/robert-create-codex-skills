---
{
  "chunk_id": "selectcell__intro_f57651b677565d4c",
  "source_file": "popups/selectCell.html",
  "source_original_path": "popups/selectCell.html",
  "toc_path": null,
  "heading_path": [
    "selectCell.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/flex_action_reference.html"
  ],
  "images": [],
  "content_hash": "f57651b677565d4c",
  "level": 0
}
---

# selectCell.html

Selects the specified cell in the list or tree or table using the mouse or keyboard.

| Target | Required. |
| --- | --- |
| Controls | Grids (tables). |
| Command | Row and column identifiers for the cell. |
| Step Properties | Step Properties Ctrl: Indicates that the Control key is pressed when executing the action Shift: Indicates that the Shift key is pressed when executing the action Alt: Indicates that the Alt key is pressed when executing the action Default: [No key selected] Select column by Auto: Automatically identify the column. If the specified column identifier is text, then parse the value as the name of the column. If the specified column identifier is a number, then parse the value as the column index Index: Parse the specified value as the index of the column. Name: Parse the specified value as text (the column name). Default: Auto Select row by Auto: If the specified row identifier is text, then find the first row containing the text. If the specified row identifier is a number, then parse the value as the row index. Index: Parse the specified value as the row index. Key column: Parse the specified Key column property value as the name or index of the key column. If you specify Key column, then you must specify values for the Select key column by and Key column properties. Default: Auto Select key column by: If you specify Key column for the Select row by property, then specify whether the Key column property value is a column name or a column index. Key column: - If you specified Index for the Select key column by property, then specify the index of the key column. - If you specified Index for the Select key column by property, then specify the index of the key column. Trigger: Mouse or Keyboard Default: Mouse Step Properties > Target Maximum time to wait for target: Specify the maximum number of seconds to wait for the target to appear before performing an action on it. If the time is exceeded, iTest declares an execution issue for the step and then continues executing. Default: 15 |

For details, see the online help: Flex action reference.
