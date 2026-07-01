---
{
  "chunk_id": "external_projects_view__external_projects_view_785cf18efdd156de",
  "source_file": "topics/external_projects_view.htm",
  "source_original_path": "topics/external_projects_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "External Projects view"
  ],
  "heading_path": [
    "External Projects view",
    "External Projects view"
  ],
  "anchor": "1101313",
  "context_ids": [
    "external_projects_view"
  ],
  "index_keywords": [
    "External Projects view",
    "managing"
  ],
  "index_keyword_paths": [
    "External Projects view",
    "documents > managing",
    "views > External Projects view"
  ],
  "related_links": [],
  "images": [
    "topics/images/sharing.1.jpg",
    "topics/images/sharing_2.2.jpg"
  ],
  "content_hash": "785cf18efdd156de",
  "level": 1
}
---

# External Projects view > External Projects view

For the directories that appear in the in the <workspaceName>/iTar directory or that are specified by the ITAR_PATH environment variable, the External Projects view displays all projects, folders, and files that are held in iTar files. Each iTar file is shown as a iTest project (the associated icon includes a zipper to indicate that it is “zipped”).

The External Projects view looks to the two locations in the following order. If there are multiple projects with the same name in multiple locations, then the External Projects view displays only the first project that it finds.

- The <workspaceName>/iTar directory

- The directories specified by the ITAR_PATH environment variable

> **Note:** Note If there is a project with the same name in both the current iTest workspace and in any location that iTest searches for iTar files, then the project will appear in the Project Explorer only and not in the External Projects view. That is, any project name will appear in only one view in the iTest window.

> **Caution:** CAUTION Keep in mind that there can be some confusing interactions when, in addition to the projects in your workspace, you make use of projects in iTar files. If you export a project to an iTar and then use the Project Explorer to delete the file, it is removed from the workspace but not from the file system. As a result, the iTar’ed project might now appear on the External Projects view. The next time that you start iTest, however, iTest auto‑imports the original project (because iTest discovered it in the workspace). The project now appears in the Project Explorer once again. To use only the iTar’ed version, you must use the operating system file management utility to remove the project from the workspace.

- To open the External Projects view, click in the main toolbar and then select External Projects.

- Notice that the familiar “hanging folder” icon for projects does not appear because the view displays the contents of the iTar files in the computer’s file system and not the contents of a workspace. The “zip folder” icon represents iTar files.

- Click Collapse All to collapse the directory tree for easier navigation.

- To view particular files, type a search string into the filter text box at the top. You can use * and ? wildcard characters. Only files with matching text appear in the view. Click Clear to remove the filter text.

- To execute a test case, select it and then click Start Execution in New Window in the main toolbar. By default, when you start a session using a session profile from the Favorites view, the Project Explorer view, the External Projects view, or the Session Profile editor, the session starts in a new session window.

- Double-click a file to open it in the appropriate editor. Alternatively, right-click it and select Open. Remember that any file in an iTar file is read-only — you will not be able to modify the file. You can, however, make changes and then save the file with a different name.

- To copy a files URI into the clipboard, right-click the file and select Copy URI

- In any folder, right-click a document to view a menu of options.

![screenshot](topics/images/sharing.1.jpg) <!-- image_chunk: img_b897a9e08c94ca3e -->

![unknown](topics/images/sharing_2.2.jpg) <!-- image_chunk: img_1ecf202fcbb65406 -->
