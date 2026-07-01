---
{
  "chunk_id": "quickcalls_arguments_in_quickcall_steps__fixing_quickcall_steps_with_empty_descri_d98a0f06f0991d2d",
  "source_file": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "source_original_path": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "About arguments in QuickCall steps"
  ],
  "heading_path": [
    "About arguments in QuickCall steps",
    "About arguments in QuickCall steps",
    "Fixing QuickCall steps with empty description in Python TestCases"
  ],
  "anchor": "1530955",
  "context_ids": [
    "quickcalls_arguments_in_quickcall_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/qc_tclSyntax_inPyhton_Warning.png",
    "topics/images/qc_tclSyntax_inPyhton_QuickFix.png",
    "topics/images/qc_tclSyntax_inPyhton_QuickFixDialog.png"
  ],
  "content_hash": "d98a0f06f0991d2d",
  "level": 3
}
---

# About arguments in QuickCall steps > About arguments in QuickCall steps > Fixing QuickCall steps with empty description in Python TestCases

Usage of TCL syntax for QuickCalls and call steps in Python test cases display a warning message in the Problems view if a step has empty description as shown below. QuickCall steps with empty descriptions, which correspond to empty argument list in TCL.

A fix requires manual input or using iTest provided option called Quick Fix to automatically fix QuickCall steps with empty descriptions.

In the Problem view, select a test case or multiple test cases with empty argument list, right-click and then press Quick Fix to display the Quick Fix dialog.

On the Quick Fix dialog, select the required test case listed in the Problems section and click Finish. The Quick Fix updates the relevant steps by adding the correct syntax ‘()’ in the previously empty step description.

![screenshot](topics/images/qc_tclSyntax_inPyhton_Warning.png) <!-- image_chunk: img_2760c6063637f40d -->

![screenshot](topics/images/qc_tclSyntax_inPyhton_QuickFix.png) <!-- image_chunk: img_d2f1c4b8452ae52c -->

![screenshot](topics/images/qc_tclSyntax_inPyhton_QuickFixDialog.png) <!-- image_chunk: img_b0ce1a430e0bb49a -->
