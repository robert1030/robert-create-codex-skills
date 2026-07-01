---
{
  "chunk_id": "captured_item_concept__captured_items_a6a47ec0a80c604e",
  "source_file": "topics/captured_item_concept.htm",
  "source_original_path": "topics/captured_item_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Captured items"
  ],
  "heading_path": [
    "Captured items",
    "Captured items"
  ],
  "anchor": "1131834",
  "context_ids": [
    "captured_item_concept"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "captured items > defined"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks_9.1.jpg"
  ],
  "content_hash": "a6a47ec0a80c604e",
  "level": 1
}
---

# Captured items > Captured items

In both manual (interactive) sessions and automatically executed test cases, a session typically returns a response to each command that you send. iTest captures the command, response, and other identifying information (like the session and action identifiers and timestamp) as a captured item.

The Capture view displays basic information about each captured item and lists each item in the order in which it was captured. In this example, we have selected a single captured item (the show ip traffic command that we submitted to the device).

You can save any or all of the captured items that currently appear in the Capture view as a Capture report or a procedure in a test case. Capture reports preserve and display all of the information about all captured items.

The Capture view is a log of your session; it's not the place to edit steps. To edit steps, save the captured items into a test case and use the Test Case editor to modify the steps as needed.Captured items include the session's response, but the Capture view does not display responses. To view a response, open the Response view or view the items in a Capture report. Double-click an item to display it in the Response view.

On startup, iTest will automatically discard old captured sessions when the size of the capture database exceeds a certain limit. You can change this limit using Window > Preferences.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/capture_tasks_9.1.jpg) <!-- image_chunk: img_26d1613fab7f0399 -->
