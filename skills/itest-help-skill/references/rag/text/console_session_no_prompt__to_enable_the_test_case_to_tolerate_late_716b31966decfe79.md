---
{
  "chunk_id": "console_session_no_prompt__to_enable_the_test_case_to_tolerate_late_716b31966decfe79",
  "source_file": "topics/console_session_no_prompt.htm",
  "source_original_path": "topics/console_session_no_prompt.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Tips for working with prompts"
  ],
  "heading_path": [
    "Tips for working with prompts",
    "Tips for working with prompts",
    "To enable the test case to tolerate late or unknown prompts:"
  ],
  "anchor": "1290224",
  "context_ids": [
    "console_session_no_prompt",
    "troubleshoot_prompt"
  ],
  "index_keywords": [
    "adding definitions for",
    "console input from terminal server",
    "large responses",
    "late",
    "no prompt",
    "not recognized",
    "prompts",
    "terminal server to a console input",
    "waiting “forever” for",
    "waiting “forever” for a prompt",
    "waiting “forever” for a prompt during replay"
  ],
  "index_keyword_paths": [
    "console input from terminal server",
    "console sessions > no prompt",
    "defining > prompts",
    "large responses",
    "prompts > adding definitions for",
    "prompts > console input from terminal server",
    "prompts > late",
    "prompts > not recognized",
    "prompts > terminal server to a console input",
    "prompts > waiting “forever” for",
    "replay > waiting “forever” for a prompt",
    "responses > late",
    "terminal server to a console input",
    "waiting “forever” for a prompt during replay"
  ],
  "related_links": [],
  "images": [
    "topics/images/prompts_5.1.jpg"
  ],
  "content_hash": "716b31966decfe79",
  "level": 4
}
---

# Tips for working with prompts > Tips for working with prompts > To enable the test case to tolerate late or unknown prompts:

1. Select the step. In the Step Properties section, go to <Telnet or SSH or other> command Properties > Completion.

1. 2

1. As you know, iTest identifies possible prompts by noticing when the session returns text and then goes silent for a significant period of time (this time period is called the Idle Channel Interval). Increase the Idle Channel Interval to a value that is high enough to avoid errors, but not so high as to cause slow execution when there is a legitimate problem.

1. 3

1. Select Prompt matches OR device has not sent data during idle channel interval.

The setting results in the following processing order: The step is completed once one of the defined prompts is received. If none of the defined prompts is received or no prompt is defined (the situation that we are trying to allow for), then the system waits for the specified Idle Channel Interval time, completes the step, and then continues to the next step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/prompts_5.1.jpg) <!-- image_chunk: img_e0f2597f69e9d0c1 -->
