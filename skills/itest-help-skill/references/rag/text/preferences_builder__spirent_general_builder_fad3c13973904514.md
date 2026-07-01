---
{
  "chunk_id": "preferences_builder__spirent_general_builder_fad3c13973904514",
  "source_file": "topics/preferences_builder.htm",
  "source_original_path": "topics/preferences_builder.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Setting preferences for the builder"
  ],
  "heading_path": [
    "Setting preferences for the builder",
    "Setting preferences for the builder",
    "Spirent > General > Builder"
  ],
  "anchor": "1120412",
  "context_ids": [
    "preferences_builder"
  ],
  "index_keywords": [
    "builder",
    "preference settings"
  ],
  "index_keyword_paths": [
    "builder > preference settings",
    "preference settings > builder"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "fad3c13973904514",
  "level": 2
}
---

# Setting preferences for the builder > Setting preferences for the builder > Spirent > General > Builder

The builder process ensures that all files and resources that depend on each other are properly linked so that updates to one file are reflected in all of its dependent files. The builder “builds” projects to catch dependency errors before you try to execute a test that will probably fail due to the error.

Here is an example of how the builder detects a dependency problem: A test case refers to a particular response map (the test case has a dependency on the response map); when you delete the response map, the builder notices that a required document no longer exists and notifies you by creating an error message in the Problems.

By default, iTest builds projects automatically to update dependency declarations and to fix problems as needed. We strongly recommend that you leave automatic builds enabled (Project > Build Automatically).

| Suppress warnings for circular project dependencies | If your workspace includes many circular references, iTest might create so many warnings in the Error Log that the system cannot operate. Example: Project A includes file A that refers to file B in project B. File B in project B refers to file A in Project A. The iTest validator code goes into a loop to create an infinite number of warnings. For this case, check the box so that iTest does not generate the warnings. After you check the box, existing warnings will remain until you rebuild the projects (click Project > Clean > Clean all projects) Default: unchecked |
| --- | --- |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
