---
{
  "chunk_id": "tcl_steps_adding__moving_data_back_from_the_tcl_interprete_ddc8648200f0271f",
  "source_file": "topics/tcl_steps_adding.htm",
  "source_original_path": "topics/tcl_steps_adding.htm",
  "toc_path": [
    "iTest Online Help",
    "Tcl Shell Sessions",
    "Creating Tcl test case steps"
  ],
  "heading_path": [
    "Creating Tcl test case steps",
    "Creating Tcl test case steps",
    "Moving data back from the Tcl interpreter to iTest"
  ],
  "anchor": "1090351",
  "context_ids": [
    "tcl_steps_adding"
  ],
  "index_keywords": [
    "Tcl Shell",
    "adding Tcl Shell",
    "test case steps"
  ],
  "index_keyword_paths": [
    "Tcl Shell sessions > test case steps",
    "steps > adding Tcl Shell",
    "test case steps > Tcl Shell"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ddc8648200f0271f",
  "level": 2
}
---

# Creating Tcl test case steps > Creating Tcl test case steps > Moving data back from the Tcl interpreter to iTest

Responses to Tcl Shell session steps have three parts:

- Result of the statement(s) evaluated

- Text (if any) output to STDOUT while evaluating those statements

- Text (if any) output to STDERR while evaluating those statements.

The parts are combined in the text response body of the iTest step. But they can also be independently accessed using queries on the response. For example, you could add an analysis rule on a Tcl Shell step that stores the result (using the query extractor configured with result()) in a iTest variable that you name. Depending on the situation, you might also want to create a iTest response map if the Tcl Shell statement produces a lot of textual output from which you want to harvest specific data.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
