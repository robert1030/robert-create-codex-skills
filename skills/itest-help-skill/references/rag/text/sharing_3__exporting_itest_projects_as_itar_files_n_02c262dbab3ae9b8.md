---
{
  "chunk_id": "sharing_3__exporting_itest_projects_as_itar_files_n_02c262dbab3ae9b8",
  "source_file": "topics/sharing.3.htm",
  "source_original_path": "topics/sharing.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity"
  ],
  "heading_path": [
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity"
  ],
  "anchor": "1094115",
  "context_ids": [],
  "index_keywords": [
    "export projects to Itars",
    "signing artifact"
  ],
  "index_keyword_paths": [
    "export projects to Itars > signing artifact",
    "signing artifacts > export projects to Itars"
  ],
  "related_links": [
    "builder.5.htm#1103394",
    "#1244126",
    "#1121122",
    "#1244307",
    "#1251004"
  ],
  "images": [
    "topics/images/export_itar_select_projects.png"
  ],
  "content_hash": "02c262dbab3ae9b8",
  "level": 1
}
---

# Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity

You export projects to an iTar file in a folder that you specify.

1. 1

1. First ensure that all projects are properly built. The easiest way to ensure a current build is to click Project > Clean > Clean all projects.

1. 2

1. In the Project Explorer, right-click the project and then select Export.

1. 3

1. On the Select page, select iTest > Export iTest Projects to iTar files, Network DevOps Agent or Velocity and then click Next.

1. 4

1. On the Select Projects page, select Export Projects to itars, NDO or Velocity and click Next to display the Export Projects to Itars dialog.

Perform these tasks on the Export Projects to itars, NDO or Velocity dialog.

Select the project or projects to export. (If you started the wizard by right-clicking a project, then the project is selected for you).

You may click Select All, Unselect All, or Update Project Dependencies to rebuild project.

- Select All: Click to select the project and the listed project dependencies.

- Unselect All: Click to clear the current section.

- Update Project Dependencies: Click to rebuild existing or newly added project dependencies. The wizard automatically selects the dependent projects and rebuilds, if you have selected the Add Dependent Projects option.

When the dependent project is not declared in iTest Project Dependencies, iTest displays warnings, which you may fix. See Updating project dependencies.

1. Add Dependent Projects: To ensure that all referenced and dependent files are included the Add Dependent Projects option is selected by default and all declared dependent projects are selected in the list of projects to be exported.

If you un-select the Add Dependent Projects option, the dependent projects will not be automatically selected in the list of projects to be exported (and will not remove any projects previously selected).

You may manually add or remove projects you wish to export.

iTest exports each required project to an individual iTar file in the folder specified in Export to directory. (Projects that are already stored in iTar format are not compressed again).

> **Note:** Note To avoid dependent projects from being automatically added to exported iTar, unselect Add Dependent Projects, select only the required project dependencies and then click the Rebuild Project Dependencies button.

1. Select one of these options: “Export to Directory”, “Publish into Velocity”, or “Publish into Network DevOps Agent”. Then select “Encrypt exported iTars”, if required.

![screenshot](topics/images/export_itar_select_projects.png) <!-- image_chunk: img_32d764c67eb8fba9 -->
