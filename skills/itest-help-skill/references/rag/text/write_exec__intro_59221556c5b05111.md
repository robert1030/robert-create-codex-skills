---
{
  "chunk_id": "write_exec__intro_59221556c5b05111",
  "source_file": "topics/popups/write_exec.html",
  "source_original_path": "topics/popups/write_exec.html",
  "toc_path": null,
  "heading_path": [
    "write_exec.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_write.html"
  ],
  "images": [],
  "content_hash": "59221556c5b05111",
  "level": 0
}
---

# write_exec.html

You'll use write steps in called procedures. A write step is a good way to provide a response for a call step.

A write step adds text into the response of the caller's call step. The text that appears in the Description cell (the value of the Command property) is appended to the response to the caller's call step.

You can configure:

- Whether to append a line terminator to the response
- An XML node (for example, "info/result") and value (for example, "true") to be inserted into the structured data associated with the caller's response. If these structured properties are used, then the new structured data will be linked to the unstructured text data appended to the response. (The "token" tags and others are added so that highlighting will work for them.) You can then define an analysis rule for the call step.

For details, see the online help: The write action.
