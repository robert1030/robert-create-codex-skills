---
{
  "chunk_id": "ui_specify_default_project__to_specify_the_default_project_ee6dbe3729449db2",
  "source_file": "topics/ui_specify_default_project.htm",
  "source_original_path": "topics/ui_specify_default_project.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "Specifying a default project for iTest"
  ],
  "heading_path": [
    "Specifying a default project for iTest",
    "Specifying a default project for iTest",
    "To specify the default project"
  ],
  "anchor": "1383547",
  "context_ids": [
    "ui_specify_default_project"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/project_natures.png"
  ],
  "content_hash": "ee6dbe3729449db2",
  "level": 2
}
---

# Specifying a default project for iTest > Specifying a default project for iTest > To specify the default project

The default project has a iTest Project Nature of iTest Default Project.

1. In the Project Explorer, select the project.

1. 2

1. On the Project menu, select Properties.

1. 3

1. In the Properties for [projectName] dialog box, on the iTest Project Natures list, check the iTest Default Project check box.

The Project Natures are added by virtue of the Eclipse plugins installed on your system. The Project Natures allows you to tag a project as a specific type of project (e.g., iTest project) and indicate that a certain tool is used to operate on that project. Select the following options to specify the Project Natures:

| iTest Default Project | Allows the framework to treat the files as required by iTest. |
| --- | --- |
| iTest Documentation Builder | Verifies files, checks for missing dependencies and other warnings that might exist. |
| iTest Response Map Library | Indicates that this project is a container of response maps that can be organized within a Response Map Library. |
| iTest Resource | Indicates a project that contains resources necessary for iTest to function. This includes templates for Test Report formats. |
| org,eclipse.core.resources.neture | This Eclipse resources plug-in provides services for accessing the projects, folders, and files with which you are working. For use iTest internal use. |
| Security Nature | For iTest internal use only. Security Nature is added by default to all new projects. Selected: iTest will automatically verify signatures of the test cases (.iTar files ) and test report archives (*.fftz files) located in that project, creates problem markers and displays indicators accordingly. Not Selected: iTest will not automatically verify signatures of the .iTar and ..fftz files. Note It is recommended to use this only in conjunction with Spirent Support ( https://support.spirent.com/SpirentCSC/). |
| Note | It is recommended to use this only in conjunction with Spirent Support ( https://support.spirent.com/SpirentCSC/). |
| Web Properties | For iTest internal use (this is an Eclipse artefact). |

> **Note:** Note You cannot directly add options to the Project Natures. However, it is possible for you to install additional Plugins, which may add relevant Natures to the list of Project Natures. For example, if you add Python development plugins, relevant Natures may be added to the list of Project Natures.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/project_natures.png) <!-- image_chunk: img_442b8d98fa935d6e -->
