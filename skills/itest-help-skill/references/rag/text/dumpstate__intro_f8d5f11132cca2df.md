---
{
  "chunk_id": "dumpstate__intro_f8d5f11132cca2df",
  "source_file": "popups/dumpstate.html",
  "source_original_path": "popups/dumpstate.html",
  "toc_path": null,
  "heading_path": [
    "dumpstate.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacement_response.html",
    "help::/com.fnfr.svt.help/topics/action_dumpstate.html"
  ],
  "images": [],
  "content_hash": "f8d5f11132cca2df",
  "level": 0
}
---

# dumpstate.html

The response to a dumpState step (commonly used for troubleshooting) can include any or all of the following information:

- Execution thread information (the data that would currently be displayed in the Threads view)
- The data that would currently be displayed in the Data view
- The identical content as is returned by a summarize step
- The response to a dumpState step appears in the Response view.
- The response is automatically mapped, so you do not have to create a response map.

The Description cell (the value of the Command property) for a dumpState step is blank.

Tip: Use a mail session and a response field replacement. to write the response to the dumpState step into the body of an email message.

For details and restrictions, see the online help: The dumpState action.
