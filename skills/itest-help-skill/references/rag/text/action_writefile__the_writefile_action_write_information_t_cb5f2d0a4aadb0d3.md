---
{
  "chunk_id": "action_writefile__the_writefile_action_write_information_t_cb5f2d0a4aadb0d3",
  "source_file": "topics/action_writeFile.htm",
  "source_original_path": "topics/action_writeFile.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘writeFile’ action: Write information to a file"
  ],
  "heading_path": [
    "The ‘writeFile’ action: Write information to a file",
    "The ‘writeFile’ action: Write information to a file"
  ],
  "anchor": "1519763",
  "context_ids": [
    "action_writeFile"
  ],
  "index_keywords": [
    "EXEC writeFile Properties",
    "writeFile",
    "writeFile action",
    "writing from  test case",
    "writing from test case"
  ],
  "index_keyword_paths": [
    "EXEC writeFile Properties",
    "actions > writeFile",
    "file > writing from  test case",
    "text > writing from test case",
    "writeFile action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "cb5f2d0a4aadb0d3",
  "level": 1
}
---

# The ‘writeFile’ action: Write information to a file > The ‘writeFile’ action: Write information to a file

> **Note:** Note The writeFile action is supported in TCL and Python.

You can use a writeFile step to write information to a file while executing a test case. For example, create a file that stores variable values, or data that is extracted from a response, or the entire text of the response to a step. Here are some options for writeFile actions:

- You can overwrite or append to an existing file

- You can add a blank line to the end of the text file (after the end of the data)

- For multiline text data, you can specify the delimiter character to use to separate lines (cr, cr/lf and so on)

- When the text information consists of multiple values, you can specify the delimiter character (comma, newline, and so on) to use to separate values
