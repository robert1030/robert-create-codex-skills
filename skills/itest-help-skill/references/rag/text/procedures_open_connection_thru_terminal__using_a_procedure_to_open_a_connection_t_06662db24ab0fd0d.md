---
{
  "chunk_id": "procedures_open_connection_thru_terminal__using_a_procedure_to_open_a_connection_t_06662db24ab0fd0d",
  "source_file": "topics/procedures_open_connection_thru_terminal.htm",
  "source_original_path": "topics/procedures_open_connection_thru_terminal.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Using a procedure to open a connection through a terminal server"
  ],
  "heading_path": [
    "Using a procedure to open a connection through a terminal server",
    "Using a procedure to open a connection through a terminal server"
  ],
  "anchor": "1385279",
  "context_ids": [
    "procedures_open_connection_thru_terminal"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "06662db24ab0fd0d",
  "level": 1
}
---

# Using a procedure to open a connection through a terminal server > Using a procedure to open a connection through a terminal server

Using a procedure to open a connection to a terminal server is common because the procedure can accommodate the many possible states that a serial connection may have been left in (connected, logged in, logged out, and so on). Follow these guidelines:

- Open sessions locally.

- Call a procedure that does all the setup work. Specifically, do not open sessions in a foreign procedure. This is done so that the calling test case has knowledge of the session type. Knowledge of session types is important for things like right-click > Insert/Parameter, so you can pick session parameters.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
