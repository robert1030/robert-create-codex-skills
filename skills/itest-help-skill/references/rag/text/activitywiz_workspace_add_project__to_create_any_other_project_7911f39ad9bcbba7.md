---
{
  "chunk_id": "activitywiz_workspace_add_project__to_create_any_other_project_7911f39ad9bcbba7",
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
    "To create any other project"
  ],
  "anchor": "1425216",
  "context_ids": [
    "activitywiz_workspace_add_project"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1425188",
    "form_maps_concept.htm#",
    "response_map_concept.htm#"
  ],
  "images": [],
  "content_hash": "7911f39ad9bcbba7",
  "level": 3
}
---

# Creating a project > Creating a project > To create any other project

1. 1

1. Click File > New > Project to create a project other than iTest project.

1. 2

1. In the New Project Select a wizard dialog opens with the following options.

Select the required option.

- General: Select to create a project resource

- iTest: Select to create iTest Project (see To create an iTest project and the required resources. Example, Form Map Library or Response Map Library (see “Form Maps” and “Response Maps: Returning Data from Responses”)

- PyDev: Select the required option to indicate the type of project to be created in the Python Development project.

- PyDev Django Project

- PyDev Google App Engine Project

- PyDev Project

In the PyDev Project wizard type the new Project name to be created and complete the required options.

1. 3

1. Click Finish.

> **Caution:** Do not name projects project, resources, or my_project.

The table below lists the options on the New PyDev Project or Pydev Django Project wizard and the resulting folders created..

| New PyDev Project / Pydev Django Project wizard option... | Resulting folders created in the new project... |
| --- | --- |
| Add project directory to PYTHONPATH | Use the project directory itself as the main PYTHONPATH entry (the most common configuration). |
| Create ‘src’ folder and add it to the PYTHONPATH | Create a src folder and add it to the PYTHONPATH. |
| Create links to existing sources | Create links to existing source directories. |
| Do not configure PYTHONPATH (to be done manually later on) | Leave the PYTHONPATH unconfigured (in which case it must be configured manually later). |

> **Note:** Note You can complete the process on this screen, or proceed to the next screen, where you will be prompted to specify any referenced projects. See https://www.pydev.org/manual_101_project_conf.html for details.
