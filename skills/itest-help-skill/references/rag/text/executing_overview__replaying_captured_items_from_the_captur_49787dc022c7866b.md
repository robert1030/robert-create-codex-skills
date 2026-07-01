---
{
  "chunk_id": "executing_overview__replaying_captured_items_from_the_captur_49787dc022c7866b",
  "source_file": "topics/executing_overview.htm",
  "source_original_path": "topics/executing_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Executing Tests",
    "Execution: Quick instructions"
  ],
  "heading_path": [
    "Execution: Quick instructions",
    "Execution: Quick instructions",
    "Replaying captured items from the Capture view"
  ],
  "anchor": "1189369",
  "context_ids": [
    "executing_overview"
  ],
  "index_keywords": [
    "in separate window",
    "multiple items",
    "quick instructions",
    "replaying"
  ],
  "index_keyword_paths": [
    "Capture reports > replaying",
    "captured items > replaying",
    "captured sessions > replaying",
    "executing > in separate window",
    "execution > in separate window",
    "execution > multiple items",
    "execution > quick instructions"
  ],
  "related_links": [
    "quickcalls_overview.htm#"
  ],
  "images": [
    "topics/images/executing_tests.11.jpg",
    "topics/images/executing_tests.12.jpg"
  ],
  "content_hash": "49787dc022c7866b",
  "level": 2
}
---

# Execution: Quick instructions > Execution: Quick instructions > Replaying captured items from the Capture view

In the Capture view: If the group of captured items is all in the same session and does not include an open step, then drop the items into an active session window of the appropriate session type. The items execute immediately. (You cannot include session open steps in the group of captured items.)

- A simple and powerful way to manually execute a series of CLI commands is to save the command text in a text file (for example, a Notepad text file). Copy the commands and then paste them into an active session. The commands execute immediately.

- During an interactive session, click in the toolbar and then select the QuickCall from the drop-down list. iTest then executes all of the steps in the QuickCall as if you had typed them yourself. With a single click (typically), you can execute a QuickCall that performs a complex initialization routine or executes a long sequence of related steps.

QuickCalls will save you a lot of time setting up and tearing down, and, for example, can quickly perform the 20 steps that you usually have to type to bring the device into the proper state for that single crucial test step. See “QuickCalls: Defining and using a library of custom actions”.

- Alternatively, if a session window of the appropriate type is open, then select the items and click .

- If the selected group of captured items include an open item for each session, then click .



For a single selected item:

- If the session from which the item was captured is still active, then the item is immediately executed in that session.

- If iTest determines that the item could be executed in any of multiple active sessions, then a dialog box asks you to specify the session in which to execute.

Shift-drop the item into an active session of the appropriate session type. iTest pastes the command into the session window, but does not execute it. This option enables you to edit the command before submitting it.

![screenshot](topics/images/executing_tests.11.jpg) <!-- image_chunk: img_49a861590ac4905b -->

![unknown](topics/images/executing_tests.12.jpg) <!-- image_chunk: img_03252c67c40f8056 -->
