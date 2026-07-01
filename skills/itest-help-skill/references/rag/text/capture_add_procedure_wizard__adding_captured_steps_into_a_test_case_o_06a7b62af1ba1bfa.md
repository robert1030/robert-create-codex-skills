---
{
  "chunk_id": "capture_add_procedure_wizard__adding_captured_steps_into_a_test_case_o_06a7b62af1ba1bfa",
  "source_file": "topics/capture_add_procedure_wizard.htm",
  "source_original_path": "topics/capture_add_procedure_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Adding captured steps into a test case or Python Script"
  ],
  "heading_path": [
    "Adding captured steps into a test case or Python Script",
    "Adding captured steps into a test case or Python Script"
  ],
  "anchor": "1322536",
  "context_ids": [
    "capture_add_procedure_wizard"
  ],
  "index_keywords": [
    "Add Procedure wizard",
    "adding",
    "procedures",
    "saving as procedures"
  ],
  "index_keyword_paths": [
    "Add Procedure wizard",
    "adding > procedures",
    "captured items > saving as procedures",
    "captured sessions > saving as procedures",
    "creating > procedures",
    "procedures > adding"
  ],
  "related_links": [
    "pal_python_automation_library_overview.htm#",
    "quickcalls_overview.htm#"
  ],
  "images": [],
  "content_hash": "06a7b62af1ba1bfa",
  "level": 1
}
---

# Adding captured steps into a test case or Python Script > Adding captured steps into a test case or Python Script

> **Note:** Note For generating Python Scripts from the captured steps, see “Python Automation Library”, section Capturing Manual (Interactive) Sessions.

While you can add a procedure to a test case manually by typing it into the Test Case editor, the fastest way to add a procedure is to perform the steps manually, select the captured steps or sessions in the Capture view, and then use the Add to iTest Test Case wizard.

- If you select multiple sessions, they are saved together in capture order as a single procedure.

- Comments and makers are converted into EXEC comment actions.

- When you add a captured session to a iTest test case, each QuickCall that you performed during the manual session becomes a single step in the test case (regardless of how many actions the QuickCall actually performed). This improves readability, portability, and consistency. See “QuickCalls: Defining and using a library of custom actions”.
