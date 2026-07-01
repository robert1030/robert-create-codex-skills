---
{
  "chunk_id": "action_dumpstate__the_dumpstate_action_return_threads_view_805615794ca096d3",
  "source_file": "topics/action_dumpstate.htm",
  "source_original_path": "topics/action_dumpstate.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘dumpState’ action: Return Threads view content, Data view content, and a summary of execution results"
  ],
  "heading_path": [
    "The ‘dumpState’ action: Return Threads view content, Data view content, and a summary of execution results",
    "The ‘dumpState’ action: Return Threads view content, Data view content, and a summary of execution results"
  ],
  "anchor": "1602824",
  "context_ids": [
    "action_dumpstate"
  ],
  "index_keywords": [
    "dumpState",
    "dumpState action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > dumpState",
    "actions > dumpState",
    "dumpState action"
  ],
  "related_links": [
    "action_summarize.htm#1516733"
  ],
  "images": [],
  "content_hash": "805615794ca096d3",
  "level": 1
}
---

# The ‘dumpState’ action: Return Threads view content, Data view content, and a summary of execution results > The ‘dumpState’ action: Return Threads view content, Data view content, and a summary of execution results

The response to a dumpState step (commonly used for troubleshooting) can include any or all of the following information:

- Execution thread information (the data that would currently be displayed in the Threads view)

- The data that would currently be displayed in the Data view

- The identical content as is returned by a summarize step

> **Note:** Note The response to a dumpState step appears in the Response view.

> **Note:** The response is automatically mapped, so you do not have to create a response map.



To add a dumpState step

1. Add a step and select an Action of dumpState.

1. 2

1. Leave the Description cell (the value of the Command property) blank.

1. 3

1. In the Step Properties section, open the EXEC dumpState Properties > dumpState step Properties group and specify the following settings:

| Append Threads view content | Check the box to add execution thread information (the data that would currently be displayed in the Threads view). The heading Threads View Summary: appears before the content. Default: checked |
| --- | --- |
| Append Data view content | Check the box to add the data that would currently be displayed in the Data view. The heading Data View Summary: appears before the content. Default: checked |
| Append summary | Check the box to add the identical content as is returned by a summarize step (as described in The ‘summarize’ action: Summarize the current test case execution results. The heading Execution Summary: appears before the content. The text appears in the default format for summarize steps: Display two tables: unexpected followed by all tests. Default: checked |



Tip: Email the ‘dumpState’ data to your team

One popular use of the dumpState action is to email the execution summary to your team.

1. Add a dumpState step. Save the response to the step into a variable using the Store response in variable property for the step.

1. In a Mail session, use a response field replacement to write the data into the body of an email message.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
