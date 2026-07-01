---
{
  "chunk_id": "action_summarize__the_summarize_action_summarize_the_curre_157dd9cde0392b4b",
  "source_file": "topics/action_summarize.htm",
  "source_original_path": "topics/action_summarize.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘summarize’ action: Summarize the current test case execution results"
  ],
  "heading_path": [
    "The ‘summarize’ action: Summarize the current test case execution results",
    "The ‘summarize’ action: Summarize the current test case execution results"
  ],
  "anchor": "1516733",
  "context_ids": [
    "action_summarize"
  ],
  "index_keywords": [
    "summarize",
    "summarize action",
    "summary",
    "summary test report",
    "summary using summarize action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > summarize",
    "actions > summarize",
    "pass/fail > summary",
    "summarize action",
    "summary test report",
    "test reports > summary using summarize action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "157dd9cde0392b4b",
  "level": 1
}
---

# The ‘summarize’ action: Summarize the current test case execution results > The ‘summarize’ action: Summarize the current test case execution results

The response to a summarize step lists the pass/fail result and identifying information on the test case and its child test cases and lists all execution messages for the run.The response to a summarize step is like the Overview section of a test report.

- The response to a summarize step appears in the Response view.

- The response is automatically mapped, so you do not have to create a response map.



Tip: Email the summary to your team

One popular use of the summarize action is to email the execution summary to your team.

1. Add a summarize step. Save the response to the step into a variable using the Store response in variable property for the step.

1. In a Mail session, use a response field replacement to write the summary into the body of an email message.
