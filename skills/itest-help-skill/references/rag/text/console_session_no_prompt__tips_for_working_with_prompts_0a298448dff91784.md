---
{
  "chunk_id": "console_session_no_prompt__tips_for_working_with_prompts_0a298448dff91784",
  "source_file": "topics/console_session_no_prompt.htm",
  "source_original_path": "topics/console_session_no_prompt.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Tips for working with prompts"
  ],
  "heading_path": [
    "Tips for working with prompts",
    "Tips for working with prompts"
  ],
  "anchor": "1270513",
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
  "related_links": [
    "prompts.1.htm#1127496"
  ],
  "images": [],
  "content_hash": "0a298448dff91784",
  "level": 1
}
---

# Tips for working with prompts > Tips for working with prompts



What to do when iTest waits “forever” for a prompt during automated execution

During replay or automated execution, a session can return a prompt with a format that iTest does not expect (for example, the prompt might include an timestamp or error message or might reproduce a failed command as a hint for correcting the command text). In this situation, iTest waits “forever” for a defined prompt that will never come.

To enable the steps to replay without interruption in the future, you can “teach” iTest about the new prompt format by adding a prompt definition. iTest will recognize the prompt from then on.

See Learningexecution for details.



Connecting to a terminal server session where there is no prompt upon opening the session

If you open a Telnet session through a terminal server to a console input, then there will be no prompt. While testing manually, you submit a carriage return (CR) by entering an empty command after the session is opened.

During execution, iTest uses a prompt to know when to submit the next command, but if there is no prompt at the start of the session, then the CR step will timeout.

Follow this procedure to avoid the problem:

1. 1

1. In the Test Case editor, select the open step for the Telnet session.

1. 2

1. In the Step Properties section, click Telnet Step Defaults > Completion.

1. 3

1. Set Completion Criteria to Idle. This forces the step to end if there is too much time without activity and then starts the next step starts immediately (to send out the CR).



Preventing errors when a prompt is delayed or is not recognized

> **Note:** Note The following tip applies to any CLI session type (for example, Telnet, Serial, Command Prompt, SSH, and so on). After you have read the tip, you can find further details in the “Terminal > Replay > Step Defaults > Completion” section in the chapter on the particular session type.

Some commands return very large responses. In some cases, due to network delay or delay at the device, it takes so long for the response to arrive and the prompt to appear that the Completion time that is configured for the step is exceeded.

Here is another condition that can result in an error associated with prompts: Some sessions can return a variety of prompts. If Spirent iTest is not configured to recognize the prompt that was returned for a step, the step can time out while waiting for a known prompt (either a built‑in prompt or a prompt that you have defined).

To avoid both of these issues, you can configure settings that increase the time to wait for a known prompt and are more forgiving when unknown prompts are returned.
