---
{
  "chunk_id": "capture_view_working_with__what_can_you_do_with_items_in_the_captur_f5894810818dd9bc",
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
    "What can you do with items in the Capture view?"
  ],
  "anchor": "1132634",
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
  "related_links": [
    "pal_python_automation_library_overview.htm#",
    "quickcalls_overview.htm#"
  ],
  "images": [],
  "content_hash": "f5894810818dd9bc",
  "level": 2
}
---

# Working in the Capture view > Working in the Capture view > What can you do with items in the Capture view?

- View or Save selected captured items or captured sessions as a Capture report in the Capture Report editor. (You can replay Capture reports.)

- Delete selection sessions

- Toggle to expand or collapse the captured steps.

- Add to Python Script. Includes the selected open steps and the import commands. Where applicable, includes the topology used. See “Python Script Generation”.

- Add selected sessions as in a iTest Test Case.

When you save a captured session as a test case, each QuickCall that you performed during the manual session becomes a single step in the test case (regardless of how many actions the QuickCall actually performed). This improves readability, portability, and consistency. See “QuickCalls: Defining and using a library of custom actions”.

- Copy as Python. iTest will render the selected steps (open steps, quickcall steps, and native command steps) in Pyhon syntax and copy the line(s) to the clipboard. The contents of the clipboard includes only the script lines associated with the selected steps. You may insert these as appropriate into your Python script. See “Python Script Generation”.

- Replay captured items or whole captured sessions by selecting them in the list and dropping them into an active session or by clicking the Replay Selected .

- All responses are captured, but responses do not appear in the Capture view. You can view responses in the Capture report. Double-click an item to display it in the Response view.

- The Capture view is a log of your session; it is not the place to edit steps. To edit steps, save the captured items into a test case and use the Test Case editor to modify the steps as needed.

- Use the Capture Comments view to add a comment to the current captured items list (for example, a note to a coworker describing the session's result).

- Add a marker to visually separate portions of the list.
