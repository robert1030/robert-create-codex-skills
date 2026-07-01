---
{
  "chunk_id": "dependencies_view__dependencies_view_b30ca68853c58f44",
  "source_file": "topics/dependencies_view.htm",
  "source_original_path": "topics/dependencies_view.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Dependencies view"
  ],
  "heading_path": [
    "Dependencies view",
    "Dependencies view"
  ],
  "anchor": "1121471",
  "context_ids": [
    "dependencies_view"
  ],
  "index_keywords": [
    "Dependencies view"
  ],
  "index_keyword_paths": [
    "Dependencies view",
    "views > Dependencies view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b30ca68853c58f44",
  "level": 1
}
---

# Dependencies view > Dependencies view

When an open step in test case “A” refers to a particular session profile, we say that the test case depends on the session profile — it has a dependency relationship with the session profile. Because we know about the dependencies, we can predict that if the either the session profile was moved, renamed, or deleted, then the test case could not execute (a file that the test case depends on would not be available at runtime).

In addition, dependency can go in the other direction: other files might depend on test case “A”. For example, test case “B” might include a call step that calls a procedure that is defined in test case “A” — test case “A” is referenced by test case “B”.

So, one file can both depend on other files and also be depended upon by (that is, be referenced by) yet other files.

The Dependencies view displays dependency relationships in both directions. The view displays the information for either the file in the active editor or the currently selected files in the Project Explorer or Favorites view. If you select multiple files, then the view displays dependency information for each file.
