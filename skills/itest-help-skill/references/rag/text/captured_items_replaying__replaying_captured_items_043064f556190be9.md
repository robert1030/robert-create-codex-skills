---
{
  "chunk_id": "captured_items_replaying__replaying_captured_items_043064f556190be9",
  "source_file": "topics/captured_items_replaying.htm",
  "source_original_path": "topics/captured_items_replaying.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Replaying captured items"
  ],
  "heading_path": [
    "Replaying captured items",
    "Replaying captured items"
  ],
  "anchor": "1106691",
  "context_ids": [
    "captured_items_replaying"
  ],
  "index_keywords": [
    "captured items",
    "replaying"
  ],
  "index_keyword_paths": [
    "captured items > replaying",
    "replaying > captured items"
  ],
  "related_links": [
    "quickcalls_overview.htm#"
  ],
  "images": [
    "topics/images/capture_tasks_13.1.jpg",
    "topics/images/capture_tasks_3.4.jpg"
  ],
  "content_hash": "043064f556190be9",
  "level": 1
}
---

# Replaying captured items > Replaying captured items

If the group of captured items is all in the same session and does not include an open item, then drop selected captured items from the Capture view into an active session window of the appropriate session type. The items execute immediately. (You cannot include session open items when dropping captured items.)

> **Tip:** Tip For a single item, Shift-drop the item into an active session window of the appropriate session type. iTest pastes the command into the session window, but does not execute it. This option enables you to edit the command before submitting it.

Alternatively, if a session window of the appropriate type is active, then select the items and click the Replay Selected Items on the Capture view.

If the group of captured items is all in the same session and does include an open step, then select the items and click on the Execution view.

To execute a group of captured items from different sessions, the open step for each session must precede the other steps in the session.



Tips

- Because iTest always captures commands and responses, it captures the commands and responses that are being executed. This means that you can create a new (more complex) Capture report or session that results from executing multiple original Capture reports or captured sessions.

- A simple and powerful way to execute a series of commands is to save the command text in a text file (for example, a Notepad text file). Copy the commands and Paste them into an active session. The commands execute immediately.

- During an interactive session, click in the toolbar and then select the QuickCall from the drop-down list. iTest then executes all of the steps in the QuickCall as if you had typed them yourself. With a single click (typically), you can execute a QuickCall that performs a complex initialization routine or executes a long sequence of related steps.

QuickCalls will save you a lot of time setting up and tearing down, and, for example, can quickly perform the 20 steps that you usually have to type to bring the device into the proper state for that single crucial test step. When you save a QuickCall to a test case, iTest saves it as a single step, regardless of how many steps the QuickCall executed (this makes the test case more modular and easier to read). See “QuickCalls: Defining and using a library of custom actions”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/capture_tasks_13.1.jpg) <!-- image_chunk: img_fed712cf9f5f0fd6 -->

![unknown](topics/images/capture_tasks_3.4.jpg) <!-- image_chunk: img_194ba6e51769edd5 -->
