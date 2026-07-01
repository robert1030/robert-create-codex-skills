---
{
  "chunk_id": "quickcalls_using_a_qc_to_open_connection__using_a_quickcall_to_open_a_connection_t_897a22cf230c606e",
  "source_file": "topics/quickcalls_using_a qc_to_open_connection_via_terminal.htm",
  "source_original_path": "topics/quickcalls_using_a qc_to_open_connection_via_terminal.htm",
  "toc_path": null,
  "heading_path": [
    "Using a QuickCall to open a connection through a terminal server",
    "Using a QuickCall to open a connection through a terminal server"
  ],
  "anchor": "1403662",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "897a22cf230c606e",
  "level": 1
}
---

# Using a QuickCall to open a connection through a terminal server > Using a QuickCall to open a connection through a terminal server

Using a QuickCall to open a connection to a terminal server is common because the QuickCall can accommodate the many possible states that a serial connection may have been left in (connected, logged in, logged out, and so on). Follow these guidelines:

- Open sessions locally (not in the definition of the QuickCall).

- Call an initialization QuickCall that does all the setup work.As a result, the calling test case has knowledge of the session type. Knowledge of session types is important for activities like right-click > Insert/Parameter, so you can specify session parameters.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
