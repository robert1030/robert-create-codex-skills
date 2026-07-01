---
{
  "chunk_id": "parameters_editor_include_page__including_a_parameter_file_into_a_parame_3b0123738085299b",
  "source_file": "topics/parameters_editor_include_page.htm",
  "source_original_path": "topics/parameters_editor_include_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Pages on the Parameter editor",
    "Parameter editor Include page: Including additional parameter files"
  ],
  "heading_path": [
    "Parameter editor Include page: Including additional parameter files",
    "Parameter editor Include page: Including additional parameter files",
    "Including a parameter file into a parameter file"
  ],
  "anchor": "1323813",
  "context_ids": [
    "parameters_editor_include_page"
  ],
  "index_keywords": [
    "Include page",
    "Parameter editor",
    "including in another parameter file"
  ],
  "index_keyword_paths": [
    "Include page > Parameter editor",
    "Parameter editor > Include page",
    "parameter files > including in another parameter file"
  ],
  "related_links": [
    "param_merge_how_it_works.htm#1120320",
    "#1323817",
    "parameters.07.htm#1351195"
  ],
  "images": [
    "topics/images/parameters_6.1.jpg",
    "topics/images/parameters_7.2.jpg",
    "topics/images/parameters_4.3.jpg",
    "topics/images/ParameterEditor_IncludePage.png",
    "topics/images/parameters_3.5.jpg"
  ],
  "content_hash": "3b0123738085299b",
  "level": 2
}
---

# Parameter editor Include page: Including additional parameter files > Parameter editor Include page: Including additional parameter files > Including a parameter file into a parameter file

1. 1

1. Click to add the URI of a parameter file to the list.

Any custom parameter types defined in the children Parameter files are available for use from within the parent Parameter file.

1. 2

1. The order of the files is important because the files are merged in the order in which they appear in the list. Select a URI and click or to move it. For a description of how parameter definitions are merged, see How parameter definitions from multiple sources are merged at run time.

1. 3

1. Click Show Hierarchy to display the hierarchy of the included parameter files on the Include Hierarchy page.

The Include Hierarchy page displays the parent Parameter file and a list of children parameter files that include settings from other files. (That is, files added in Step 1.)

| Command | Description |
| --- | --- |
| Refresh | Refresh the selected elements and their direct children. |
| Cancel Current Search | Cancels the current search (useful for long running searches). |
| Show Parent Hierarchy | Displays all parents of the selected element. |
| Show Child Hierarchy | Shows all parameter files used by the currently selected parameter file. |
| Show History List | Displays a history of previously displayed hierarchies. |
| Pin the Hierarchy View | Pins the current view and allows you to open multiple hierarchy views at the same time. |
| Righ-Click | Opens a context menu with these options: |
| Open: Open selected element in the default editor (Parameter Editor) |  |
| Refresh: Refresh the selected elements and their direct children. |  |
| Focus On: Focus Hierarchy View on the selected element. |  |

1. 4

1. Other actions:

- To delete a URI from the list, click .

- To edit the selected parameter file, right-click the URI and select Open Parameter File.

- To change the URI from a relative URI to another form, right-click the URI and select Edit File URI. (The default is relative to the parameter file that you are currently editing.)

In the Test Case editor or Session Profile editor, the Custom type tab allows you to define custom parameter types and their values See Quick Facts: Where you can define and use parameters.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/parameters_6.1.jpg) <!-- image_chunk: img_35506af80ecf54e7 -->

![inline_icon](topics/images/parameters_7.2.jpg) <!-- image_chunk: img_a62e14e0d1de5316 -->

![inline_icon](topics/images/parameters_4.3.jpg) <!-- image_chunk: img_24a243d97bee3f05 -->

![screenshot](topics/images/ParameterEditor_IncludePage.png) <!-- image_chunk: img_04a81876ea6e9068 -->

![inline_icon](topics/images/parameters_3.5.jpg) <!-- image_chunk: img_9ba3a4570d097620 -->
