---
{
  "chunk_id": "activitywiz_workspace_add_project__caution_when_deleting_recreating_project_ba1ee7197479bc5f",
  "source_file": "topics/activitywiz_workspace_add_project.htm",
  "source_original_path": "topics/activitywiz_workspace_add_project.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "Creating a project"
  ],
  "heading_path": [
    "Creating a project",
    "Creating a project",
    "Deleting a project",
    "CAUTION: When deleting/recreating projects"
  ],
  "anchor": "1139022",
  "context_ids": [
    "activitywiz_workspace_add_project"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "ba1ee7197479bc5f",
  "level": 3
}
---

# Creating a project > Creating a project > Deleting a project > CAUTION: When deleting/recreating projects

When you delete a project, all other projects in the workspace get rebuilt to add error markers to the projects that reference the deleted project. If you then create a new project with the same name as the deleted project, iTest does not perform another build (for performance reasons), and the error markers in the projects remain (incorrectly).

To avoid this possible problem, when you add a new project or delete a project, perform a clean build (click Project > Clean) on the affected projects to ensure that only appropriate error markers appear.
