---
{
  "chunk_id": "project_explorer_view__projects_that_are_added_to_or_deleted_fr_21d1e35aab86e25d",
  "source_file": "topics/project_explorer_view.htm",
  "source_original_path": "topics/project_explorer_view.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "Project Explorer"
  ],
  "heading_path": [
    "Project Explorer",
    "Project Explorer",
    "Projects that are added to or deleted from the workspace"
  ],
  "anchor": "1528494",
  "context_ids": [
    "project_explorer_view"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences_workspace.htm#1261126"
  ],
  "images": [],
  "content_hash": "21d1e35aab86e25d",
  "level": 2
}
---

# Project Explorer > Project Explorer > Projects that are added to or deleted from the workspace

By default, when iTest starts, it imports any new projects that it finds in the workspace so that they are visible in the Project Explorer. This is important when you share a workspace under revision control — new projects are automatically imported.

You can change the default behavior with a preference setting; see Setting preferences for the workspace.

> **Note:** Note Keep in mind that there can be some confusing interactions when, in addition to the projects in your workspace, you make use of projects in itar files. If you export a project to an itar and then use the Project Explorer to delete the file, it is removed from the workspace but not from the file system. As a result, the itar’ed project might now appear on the External Projects view. The next time that you start iTest, however, iTest auto‑imports the original project (because iTest discovered it in the workspace). The project now appears in the Project Explorer once again. To use only the itar’ed version, you must use the operating system file management utility to remove the project from the workspace.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
