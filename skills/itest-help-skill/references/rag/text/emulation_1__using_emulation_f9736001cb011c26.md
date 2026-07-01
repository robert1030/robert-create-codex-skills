---
{
  "chunk_id": "emulation_1__using_emulation_f9736001cb011c26",
  "source_file": "topics/emulation.1.htm",
  "source_original_path": "topics/emulation.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Using emulation"
  ],
  "heading_path": [
    "Using emulation",
    "Using emulation"
  ],
  "anchor": "1191565",
  "context_ids": [],
  "index_keywords": [
    "emulating",
    "emulation",
    "simulating device responses",
    "virtual devices"
  ],
  "index_keyword_paths": [
    "emulation",
    "responses > emulating",
    "simulating device responses",
    "virtual devices"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "f9736001cb011c26",
  "level": 1
}
---

# Using emulation > Using emulation

You can have iTest emulate (“pretend to be”) any step or session. When you activate emulation for a step, iTest does not send the command to the session as usual; instead, iTest directly returns the response that you specify — the emulated response (typically, the response that the session returned the last time the test case executed. You can edit the response text as needed. No interaction with a session or device occurs — iTest returns the ‘canned’ response that you specify.

You can customize the behavior by editing the emulated response before executing the test case. For example, if the response text for the show version command for the last execution was “Version 8.4”, and you need to develop the test case for the next version before you get the device software update, you can activate emulation for the step and change the response text to “Version 8.5” rather than “Version 8.4”.
