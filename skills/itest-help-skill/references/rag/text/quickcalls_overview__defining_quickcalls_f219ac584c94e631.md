---
{
  "chunk_id": "quickcalls_overview__defining_quickcalls_f219ac584c94e631",
  "source_file": "topics/quickcalls_overview.htm",
  "source_original_path": "topics/quickcalls_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Overview: QuickCalls",
    "Overview: QuickCalls"
  ],
  "heading_path": [
    "Overview: QuickCalls",
    "Overview: QuickCalls",
    "Defining QuickCalls"
  ],
  "anchor": "1386924",
  "context_ids": [
    "quickcalls_overview"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "QuickCalls > defined"
  ],
  "related_links": [
    "quickcalls_new_quickcall_library_wizard.htm#1292200"
  ],
  "images": [
    "topics/images/quickcalls.4.jpg"
  ],
  "content_hash": "f219ac584c94e631",
  "level": 2
}
---

# Overview: QuickCalls > Overview: QuickCalls > Defining QuickCalls

Define QuickCalls the same way that you define procedures using the Test Case editor. You add a procedure definition, and add all of the steps into it as follows.

1. Add steps or save steps from captured interactive/manual sessions.

1. 2

1. Copy Test Case steps (not a QuickCall) and paste them into a QuickCall test case.

1. 3

1. Set the procedure as “public” (that is, include the QuickCall name whenever a user asks to see a list of available QuickCalls).

1. 4

1. Repeat for as many QuickCalls as needed.

When you save the test case that holds the QuickCall definitions, you are saving a QuickCall library. QuickCall libraries are “public” — the editor for any topology device or session profile enables you to specify that the QuickCall library is associated with the session configuration.

QuickCalls are associated with session profiles. To make the QuickCalls in the library available in a session, you specify the library on the Libraries properties page in the Testcase editor or on the Settings page of the Session Profile editor. As a result, the QuickCall is available:

- During interactive sessions. Click and select the action from the drop-down list. All of the steps in the QuickCall execute. (If the QuickCall requires parameter values, then iTest opens a dialog box to allow you to supply the values.)

- While you are editing the test case, as shown earlier.

- During automated execution. The QuickCall executes exactly like a procedure executes.

Limitation Global variables defined in one QuickCall in the library cannot be accessed by other QuickCalls in the library.

See Defining a QuickCall for details.

![unknown](topics/images/quickcalls.4.jpg) <!-- image_chunk: img_68a85b5d86148fe1 -->
