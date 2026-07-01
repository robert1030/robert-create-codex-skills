---
{
  "chunk_id": "builder_5__updating_project_dependencies_e53f1430d3519c0f",
  "source_file": "topics/builder.5.htm",
  "source_original_path": "topics/builder.5.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Updating project dependencies"
  ],
  "heading_path": [
    "Updating project dependencies",
    "Updating project dependencies"
  ],
  "anchor": "1103394",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "builder.1.htm#1120608"
  ],
  "images": [
    "topics/images/rebuild_project_dependencies.png",
    "topics/images/builder_project_dependencies_not_declared_warning.png",
    "topics/images/builder_quick_fix_project_dependencies.png"
  ],
  "content_hash": "e53f1430d3519c0f",
  "level": 1
}
---

# Updating project dependencies > Updating project dependencies

During the builder process, iTest goes through each specified project. If a file in a project refers to another project, then the other project is declared as a dependent project. This is important when you are creating itar files, as described in Building projects.

1. 1

1. In the Project menu, select Update Project Dependencies.

1. 2

1. Select the appropriate option and then click OK.

- Rebuild all projects

- Rebuild selected projects: To speed the process, build only the selected projects.

When the dependent project is not declared in iTest Project Dependencies, iTest displays warnings, in the Problems View. Right click on the warning and select the Quick Fix option.

The Quick Fix wizard displays with the appropriate fix. Click Finish and iTest automatically adds the missing Dependencies.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/rebuild_project_dependencies.png) <!-- image_chunk: img_8c936c561202c2a6 -->

![screenshot](topics/images/builder_project_dependencies_not_declared_warning.png) <!-- image_chunk: img_9f8e717333749906 -->

![screenshot](topics/images/builder_quick_fix_project_dependencies.png) <!-- image_chunk: img_6d71f29e94817ee0 -->
