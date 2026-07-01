---
{
  "chunk_id": "tl1_1__for_hybrid_interfaces_follow_this_proced_7bd6c15d5bd44464",
  "source_file": "topics/tl1.1.htm",
  "source_original_path": "topics/tl1.1.htm",
  "toc_path": [
    "iTest Online Help",
    "TL1 Sessions",
    "Configuring sessions and test case steps for TL1 devices"
  ],
  "heading_path": [
    "Configuring sessions and test case steps for TL1 devices",
    "Configuring sessions and test case steps for TL1 devices",
    "For Hybrid interfaces, follow this procedure:"
  ],
  "anchor": "1154372",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "7bd6c15d5bd44464",
  "level": 2
}
---

# Configuring sessions and test case steps for TL1 devices > Configuring sessions and test case steps for TL1 devices > For Hybrid interfaces, follow this procedure:



Configure the testbed device or session profile

You will typically work on an Telnet, Serial, or SSH testbed device or session profile.

1. 1

1. Set the Style property (Terminal > Style) to TL1.

1. 2

1. On the Terminal > Replay > Step Defaults > Completion page, set the Completion criteria property to TL1 End of Message.



Configure the test case

- For steps that do not return TL1-format responses: Change the completion rule to Prompt matches AND device has not sent data during the Idle channel interval (the setting causes iTest to wait for a prompt in the response to the step).

> **Note:** Note If you see that you would change most steps in the test case to Prompt matches AND device has not sent data during the Idle channel interval, you might be better off changing the session profile default to Prompt matches AND device has not sent data during the Idle channel interval and changing the steps that have TL1 message bodies so that their completion rule is TL1 End of Message.

- For steps that have both a TL1 message body and a prompt: Leave the session profile completion rule unchanged (TL1 End of Message). In addition, as long as you have prompts defined in your session profile, iTest will check that the TL1 message is complete and that there is a prompt match.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
