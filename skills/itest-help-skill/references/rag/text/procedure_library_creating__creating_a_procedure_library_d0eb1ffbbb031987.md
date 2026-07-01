---
{
  "chunk_id": "procedure_library_creating__creating_a_procedure_library_d0eb1ffbbb031987",
  "source_file": "topics/procedure_library_creating.htm",
  "source_original_path": "topics/procedure_library_creating.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Creating a procedure library"
  ],
  "heading_path": [
    "Creating a procedure library",
    "Creating a procedure library",
    "Creating a procedure library"
  ],
  "anchor": "1279372",
  "context_ids": [
    "procedure_library_creating"
  ],
  "index_keywords": [
    "adding",
    "creating",
    "procedure libraries"
  ],
  "index_keyword_paths": [
    "adding",
    "creating > procedure libraries",
    "procedure libraries",
    "procedure libraries > creating"
  ],
  "related_links": [
    "return_value_dialog.htm#1292200"
  ],
  "images": [],
  "content_hash": "d0eb1ffbbb031987",
  "level": 2
}
---

# Creating a procedure library > Creating a procedure library > Creating a procedure library

1. Create a new test case.

1. 2

1. On the Test Case editor's General page, check the Include this test case when listing procedure libraries for call steps and CallProcedure actions check box. This property identifies the test case as a procedure library that should be made easily available when creating test cases. As a result, when a test case developer adds a call step or a CallProcedure action to a test case, the URI for this test case appears in the drop-down list of procedure libraries and local and foreign procedures in the Description cell.

1. 3

1. Optional, but recommended: For the procedure named “main”, uncheck the Include this procedure when listing callable procedures property (in the General section of the Procedure Properties page). As a result, when a test case developer adds a call step or CallProcedure action, main does not appear in the drop-down list of available procedures in the Description cell.

1. 4

1. Now add procedures to the test case. See Defining a procedure for details.

1. 5

1. Perform this step for each procedure that should appear in the drop-down list foreign procedures in the Description cell while a test case developer adds a call step or a CallProcedure action: Check the Include this procedure when listing callable procedures property (in the General section of the Procedure Properties page).

1. 6

1. To make the procedures available to other test cases, you must save this test case.

iTest users can now call all the procedures in this procedure library.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
