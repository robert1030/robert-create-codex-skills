---
{
  "chunk_id": "waitforprompt_web__intro_f20dc16670ab7f91",
  "source_file": "popups/waitforprompt_web.html",
  "source_original_path": "popups/waitforprompt_web.html",
  "toc_path": null,
  "heading_path": [
    "waitforprompt_web.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/web_prompts.html",
    "help::/com.fnfr.svt.help/topics/web_test_cases_creating.html"
  ],
  "images": [],
  "content_hash": "f20dc16670ab7f91",
  "level": 0
}
---

# waitforprompt_web.html

| Action Name | Target | Command property value | Description |
| --- | --- | --- | --- |
| waitForPrompt [timeout] | Not Required | Not Required | Waits for the appearance of a popup prompt dialog box. When a prompt appears, then execution immediately proceeds with the next step. The response is the most recently cached prompt text. There are two possible conditions: An immediately preceding clearPrompts command removed all prompts from the cache so that the waitForPrompt command will wait until a new prompt dialog box appears. A prompt exists in the cache, so the waitForPrompt command immediately proceeds with the next step. Specify properties in the Step Properties > Web waitForPrompt Properties page for the step. See Working with prompts (popups) for details on adding a waitForPrompt step. |

For details, see the online help: Creating Web test case steps.
