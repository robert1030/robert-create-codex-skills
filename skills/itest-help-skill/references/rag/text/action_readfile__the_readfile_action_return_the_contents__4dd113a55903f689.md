---
{
  "chunk_id": "action_readfile__the_readfile_action_return_the_contents__4dd113a55903f689",
  "source_file": "topics/action_readfile.htm",
  "source_original_path": "topics/action_readfile.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘readFile’ action: Return the contents of a file"
  ],
  "heading_path": [
    "The ‘readFile’ action: Return the contents of a file",
    "The ‘readFile’ action: Return the contents of a file"
  ],
  "anchor": "1597075",
  "context_ids": [
    "action_readfile"
  ],
  "index_keywords": [
    "readFile",
    "readFile action",
    "returning in test case"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > readFile",
    "actions > readFile",
    "file contents > returning in test case",
    "readFile action",
    "text > returning in test case"
  ],
  "related_links": [],
  "images": [
    "topics/images/actions_9.1.jpg"
  ],
  "content_hash": "4dd113a55903f689",
  "level": 1
}
---

# The ‘readFile’ action: Return the contents of a file > The ‘readFile’ action: Return the contents of a file

An EXEC readFile step returns the text or binary data of the file whose path is specified in the Description cell (the value of the Command property).

For example, the response to the following step is the text of the Test_list.txt file.

> **Tip:** Tip For text files you can use readFile to obtain data and then use analysis rules for the step to save appropriate data items into variables for use later in the test case (using get, ${varName}, gget, or ${/data/varName}, as appropriate). In the text of the file, you might use delimiter characters (for example, commas or colons) to delimit data values to make extraction easier in the analysis rule.

![screenshot](topics/images/actions_9.1.jpg) <!-- image_chunk: img_2a6eb79b1ad50e7d -->
