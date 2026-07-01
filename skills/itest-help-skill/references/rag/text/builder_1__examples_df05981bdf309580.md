---
{
  "chunk_id": "builder_1__examples_df05981bdf309580",
  "source_file": "topics/builder.1.htm",
  "source_original_path": "topics/builder.1.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Building projects"
  ],
  "heading_path": [
    "Building projects",
    "Building projects",
    "Examples"
  ],
  "anchor": "1112190",
  "context_ids": [],
  "index_keywords": [
    "Dependencies view"
  ],
  "index_keyword_paths": [
    "Dependencies view",
    "views > Dependencies view"
  ],
  "related_links": [
    "dependencies_view.htm#1121471"
  ],
  "images": [],
  "content_hash": "df05981bdf309580",
  "level": 2
}
---

# Building projects > Building projects > Examples

- A test case refers to a particular response map (the test case has a dependency on the response map). When you delete the response map, the builder notices that a required document no longer exists and notifies you by creating an error message in the Problems view.

- If a test case is dependent on a reusable procedure library that changes frequently, the builder updates the test case to stay current with the changes.

By default, iTest builds projects automatically to update dependency declarations as needed. We strongly recommend that you leave automatic builds enabled (Project > Build Automatically)

The Dependencies view displays dependency relationships in both directions. The view displays the information for either the file in the active editor or the currently selected files in the Project Explorer or Favorites view. If you select multiple files, then the view displays dependency information for each file. See Dependencies view.

Important When you delete a project, all other projects in the workspace are rebuilt to add error markers to the projects that reference resources that had previously existed in the deleted project. If you then create a new project with the same name as the deleted project, iTest does not perform another build (for performance reasons) and the error markers in the projects remain (incorrectly).To avoid this possible problem, when you add a new project or delete a project, perform a clean build (click Project > Clean > All).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
