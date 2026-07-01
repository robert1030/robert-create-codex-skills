---
{
  "chunk_id": "wireshark_4__example_quickcall_that_starts_and_monito_233489e5efddd423",
  "source_file": "topics/wireshark.4.htm",
  "source_original_path": "topics/wireshark.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Wireshark sessions",
    "Example QuickCall that starts and monitors Wireshark capture"
  ],
  "heading_path": [
    "Example QuickCall that starts and monitors Wireshark capture",
    "Example QuickCall that starts and monitors Wireshark capture"
  ],
  "anchor": "1250891",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/wireshark_quickcall.png",
    "topics/images/wireshark.2.jpg"
  ],
  "content_hash": "233489e5efddd423",
  "level": 1
}
---

# Example QuickCall that starts and monitors Wireshark capture > Example QuickCall that starts and monitors Wireshark capture

In this QuickCall, we perform a capture start command and monitor its progress using a capture status command.We use a RepeatStep action in the analysis rule to execute the capture status command every 5 seconds. When the text “capture finished” appears in the response to the capture status command, the rule succeeds so that the capture stop command can execute, and the QuickCall finishes.

Here is an example execution:

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/wireshark_quickcall.png) <!-- image_chunk: img_9a87a5abe7b085f5 -->

![screenshot](topics/images/wireshark.2.jpg) <!-- image_chunk: img_7a01b10b2e8543ea -->
