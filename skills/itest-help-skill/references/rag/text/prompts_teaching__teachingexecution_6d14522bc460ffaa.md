---
{
  "chunk_id": "prompts_teaching__teachingexecution_6d14522bc460ffaa",
  "source_file": "topics/prompts_teaching.htm",
  "source_original_path": "topics/prompts_teaching.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Teaching iTest the prompts to expect during execution"
  ],
  "heading_path": [
    "Teaching iTest the prompts to expect during execution",
    "Teaching iTest the prompts to expect during execution",
    "Teachingexecution"
  ],
  "anchor": "1270662",
  "context_ids": [
    "prompts_teaching"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_profile_update_wizard.htm#1294433"
  ],
  "images": [
    "topics/images/prompts_2.1.jpg"
  ],
  "content_hash": "6d14522bc460ffaa",
  "level": 2
}
---

# Teaching iTest the prompts to expect during execution > Teaching iTest the prompts to expect during execution > Teachingexecution

During test case execution, if the channel becomes idle and the text on the line is not a defined prompt, then the status bar presents a Learn this prompt link. When you click the link, the Learn Prompt dialog box enables you to tell iTest that the text is a prompt.

- If you click OK to identify the text as a prompt, then the test case result is unchanged and execution continues immediately with the next step.

If the text represent a “more” page continuation prompt, you can set the More settings in a similar way as in the Session Profile editor. default values: next page character is a space and quit is the letter q.

When execution finishes, iTest opens the Update Session Profile / Topology Device wizard so you can add the prompt definition to the session profile or tested device. See Using the ‘Update Session Profile’ wizard.

- If you click Cancel, then the step continues to wait for the prompt until it eventually times out. At that time, the step fails and execution continues.

![screenshot](topics/images/prompts_2.1.jpg) <!-- image_chunk: img_4e89f5681ca699ab -->
