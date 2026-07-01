---
{
  "chunk_id": "quickcalls_best_practices__quickcall_best_practices_015baa64e78e3049",
  "source_file": "topics/quickcalls_best_practices.htm",
  "source_original_path": "topics/quickcalls_best_practices.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Defining QuickCalls",
    "QuickCall ‘Best practices’"
  ],
  "heading_path": [
    "QuickCall ‘Best practices’",
    "QuickCall ‘Best practices’"
  ],
  "anchor": "1420623",
  "context_ids": [
    "quickcalls_best_practices"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "015baa64e78e3049",
  "level": 1
}
---

# QuickCall ‘Best practices’ > QuickCall ‘Best practices’

- Do not use the open action (open a session) in a QuickCall.

- When designing a procedure that should span multiple sessions (for example open a session on multiple devices or multiple sessions on a device), define a procedure. QuickCalls are inherently limited to procedures that are appropriate for the current session. Use QuickCalls only for procedures that should happen in a single session.

- Use a naming convention for QuickCalls and add a list of appropriate keywords as the last line in the Definition text for QuickCalls. During manual testing, the Execute a QuickCall wizard displays only QuickCalls that are appropriate for the current session. In addition, the manual tester can use a keyword to filter the list of QuickCalls even further. As a result, they can quickly find the appropriate QuickCall from what might be a very long list, simplifying their job.

- You define a QuickCall library for use by a broad class of devices. For particular device in the class, you can override a particular QuickCall definition by defining it in a session profile that inherits the base session profile. For example, a QuickCall named createNewUser in the base session profile is overwritten by a QuickCall named identically in the QuickCall library used by the inheriting session profile.

> **Note:** Note There is a potential confusion when a createNewUser step appears in the test report; you might ask “Which one ran, the one in the base or the other one?”. In this case, select the step and look in the Query view for the name of the QuickCall library in which the QuickCall is defined.

- Within a QuickCall library, you might design QuickCalls for use only within the library — utilities for use by other QuickCalls that are defined in the library. The typical QuickCall is meant to be public, that is, to be used by test developers and manual testers in actual tests.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
