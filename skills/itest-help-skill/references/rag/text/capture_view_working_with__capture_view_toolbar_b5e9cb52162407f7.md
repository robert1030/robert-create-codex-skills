---
{
  "chunk_id": "capture_view_working_with__capture_view_toolbar_b5e9cb52162407f7",
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
    "Working in the Capture view",
    "Capture view toolbar"
  ],
  "anchor": "1132739",
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
    "topics/images/capture_tasks.20.jpg",
    "topics/images/capture_tasks.21.jpg"
  ],
  "content_hash": "b5e9cb52162407f7",
  "level": 2
}
---

# Working in the Capture view > Working in the Capture view > Capture view toolbar

|  | View the selected items in the Capture Report editor. This enables you to view the captured items in greater detail and gives you the option to save the items as a Capture report. You can view one or more captured items or one or more sessions. Selected comments and markers also appear in the report. |
| --- | --- |
|  | Save the selected items as a Capture report. You can save one or more captured items or one or more sessions. Selected comments and markers are also saved. |
|  | Add to Python Script. Create a new Python Script with the selected captured items or add captured items to an existing Python Script. |
|  | Save the currently selected items as a iTest Test Case. You can save one or more captured items or one or more sessions. Selected comments and markers are also saved. |
|  | Copy as Python. iTest will render the selected steps (open steps, quickcall steps, and native command steps) in Pyhon syntax and copy the line(s) to the clipboard. You may insert these as appropriate into your Python script. |
|  | Insert a marker into the list of captured items after the most recent item. Markers help you to visually break up the capture log. |
|  | Delete the selected sessions, comments, and markers. While preparing to save sessions as a Capture report or procedure, you may want to remove particular sessions, comments, or markers from the Capture view. Select the items (use Ctrl-click and Shift-click to select multiple items). Click Delete Selected Items . You can delete all sessions in one or more folders (Today, Last Week, and so on) by selecting the folders and clicking . Note This action does not delete selected captured items. Only sessions (and their included captured items), comments, and markers are deleted. |
| Note | This action does not delete selected captured items. Only sessions (and their included captured items), comments, and markers are deleted. |
|  | Group by Session or Group by Time. Use this button to toggle between the following ways of viewing captured items in the Capture view: Grouped by session so that all items from a particular session appear under the appropriate session heading. Sessions are ordered by the timestamp of the open Action for the session. In the order in which the captured items occur, without regard to the items' sessions (one item from one session and another item from another session mixed in a single chronological list). |
|  | Grouped by session so that all items from a particular session appear under the appropriate session heading. Sessions are ordered by the timestamp of the open Action for the session. |
|  | In the order in which the captured items occur, without regard to the items' sessions (one item from one session and another item from another session mixed in a single chronological list). |
|  | Collapse all open folders so that only the top-level folders (Today, Last Week, and so on) appear in the view. |
|  | Replay the selected captured items or any mix of the following items: Selected captured session or group of captured sessions All captured sessions in selected folders |
|  | Selected captured session or group of captured sessions |
|  | All captured sessions in selected folders |

- When you expand a session row, the view displays one row for each captured item in the session. Click expand row to view the captured items that make up the session. The captured items' properties are not editable.

- When you select an item, iTest updates the Response view to reflect the selection.

- Comments are identified by the series c1, c2, c3, and so on. (To add a comment after the latest captured item, type the text into the Capture Comments view and then press Enter.) When you save a comment to a test case, it is saved as a comment step.

- Markers are identified by the series m1, m2, m3, and so on. (To add a marker after the latest session, click Insert Marker in the toolbar.) When you save a marker to a test case, it is saved as a comment step.

![screenshot](topics/images/capture_tasks.20.jpg) <!-- image_chunk: img_41eae66e49598cfc -->

![screenshot](topics/images/capture_tasks.21.jpg) <!-- image_chunk: img_24af5d4e471910b2 -->
