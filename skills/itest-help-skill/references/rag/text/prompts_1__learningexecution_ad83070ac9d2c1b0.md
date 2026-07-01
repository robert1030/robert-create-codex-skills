---
{
  "chunk_id": "prompts_1__learningexecution_ad83070ac9d2c1b0",
  "source_file": "topics/prompts.1.htm",
  "source_original_path": "topics/prompts.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Overview: Prompts in iTest"
  ],
  "heading_path": [
    "Overview: Prompts in iTest",
    "Overview: Prompts in iTest",
    "How iTest distinguishes prompts from responses during execution",
    "Learningexecution"
  ],
  "anchor": "1127496",
  "context_ids": [],
  "index_keywords": [
    "how iTest notices"
  ],
  "index_keyword_paths": [
    "command prompts > how iTest notices",
    "prompts > how iTest notices"
  ],
  "related_links": [],
  "images": [
    "topics/images/prompts.3.jpg"
  ],
  "content_hash": "ad83070ac9d2c1b0",
  "level": 3
}
---

# Overview: Prompts in iTest > Overview: Prompts in iTest > How iTest distinguishes prompts from responses during execution > Learningexecution

During test case execution, if the session channel becomes idle and the text on the line is not a defined prompt, then the status bar presents a Learn this prompt link that opens a dialog box to enable you to tell iTest that the text is a prompt. If you do not click the link, the step eventually times out and the test case continues execution.

> **Note:** Note When executing a session that is application type (for example: application:com.fnfr.svt.applications.ssh), a warning dialog displays as shown below, since these learned prompts are currently not saved.

![screenshot](topics/images/prompts.3.jpg) <!-- image_chunk: img_59520e37d6fd01ed -->
