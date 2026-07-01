---
{
  "chunk_id": "capture_view_working_with__working_in_the_capture_view_544cae92b9f22e8f",
  "source_file": "topics/capture_view_working_with.htm",
  "source_original_path": "topics/capture_view_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Working in the Capture view"
  ],
  "heading_path": [
    "Working in the Capture view",
    "Working in the Capture view"
  ],
  "anchor": "1132545",
  "context_ids": [
    "capture_view_working_with"
  ],
  "index_keywords": [
    "Capture view",
    "saving as Capture reports",
    "saving as procedures",
    "sessions as Capture reports"
  ],
  "index_keyword_paths": [
    "Capture view",
    "saving > sessions as Capture reports",
    "sessions > saving as Capture reports",
    "sessions > saving as procedures",
    "views > Capture view"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks.01.jpg"
  ],
  "content_hash": "544cae92b9f22e8f",
  "level": 1
}
---

# Working in the Capture view > Working in the Capture view

iTest always records your interactions with sessions — capturing session open and close actions, the actions that you send to sessions on devices, each session’s responses, and so on. iTest displays the ordered list of captured items in the Capture view.

> **Note:** Note iTest captures sessions regardless of whether the Capture view is open or not.

In a Telnet session, for example, when you type a command and press Enter, iTest captures both the command that you submitted (for example, show ip traffic) and the device's response (actually, the response from the session running on the device). The command/response pair (and some additional information like timestamp, prompt information, and the session and action identifiers) make up a captured item. As soon as the device responds, iTest adds the captured item as a row in the appropriate session in the Capture view.

The Capture view displays “today’s” captured items as they occur with the most recent item at the bottom of the list. You have the option to view the list of captured items grouped by session (as shown in the example — click Group By Session/Time ).

> **Tip:** Tip Double-click a tab to maximize the view. Double-click it again to minimize it.

Each top-level row represents one session, marker, or comment. The cells for a session row are populated if all captured items in the session share the same value for the cell. The cells are blank if the steps have different values.

- You can replay captured items or whole sessions by selecting them (use Ctrl-Click and Shift-Click for multi-select) and then clicking Replay Selected . You also have the option to replay selected captured items by dropping them into an active session window.

- The Capture view is a log of your session; it is not the place to edit steps. To edit steps, save the captured items into a test case and use the Test Case editor to modify the steps as needed.

- Save selected items as a Capture report by clicking Save As Capture Report

- Save selected items as a procedure by clicking Save As Test Case

- Insert comments by typing them into the Capture Comments view.

- All responses are captured, but responses do not appear in the Capture view. You can view responses in either the Response view, the Capture Report view, or the Capture report. Double-click an item in the Capture view to display the response in the Response view.

![screenshot](topics/images/capture_tasks.01.jpg) <!-- image_chunk: img_94d5f801a0037f18 -->
