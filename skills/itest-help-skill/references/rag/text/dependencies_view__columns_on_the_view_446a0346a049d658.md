---
{
  "chunk_id": "dependencies_view__columns_on_the_view_446a0346a049d658",
  "source_file": "topics/dependencies_view.htm",
  "source_original_path": "topics/dependencies_view.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Dependencies view"
  ],
  "heading_path": [
    "Dependencies view",
    "Dependencies view",
    "Columns on the view"
  ],
  "anchor": "1121534",
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
  "content_hash": "446a0346a049d658",
  "level": 2
}
---

# Dependencies view > Dependencies view > Columns on the view

| Resource | The Dependencies view displays dependency information for the top-level file or any resource that appears in the Resource column. If you select a single file or select an editor, then the single file appears at the top level in this column. In the example, only one file — the proclib test case — is at the top level. If you select multiple files in either the Project Explorer or Favorites view, then each of the files appears at the top level in this column, one file after the other. Expand any group by clicking to see the dependency information for the resource. Double-click any file in the view to open the file in an editor. The Dependencies view immediately refreshes to display the dependency information for the just-opened file. Depends on section For each dependent file, the view displays a Depends on section that lists each resource upon which the file depends. In the example, you can see that the proclib test case depends on three resources: a testbed, a session profile, and a response map library. The view can display any number of levels of dependency — in the example, the testbed depends on a session profile. Click for a file to view the resources that cause the dependencies. Is referenced by section The Is referenced by section lists all files that include a reference to the top-level file. In the example, the testcall test case refers to the proclib test case by calling procedures that are defined in proclib (that is, the proclib test case is depended upon by the testcall test case). |  | If you select a single file or select an editor, then the single file appears at the top level in this column. In the example, only one file — the proclib test case — is at the top level. |  | If you select multiple files in either the Project Explorer or Favorites view, then each of the files appears at the top level in this column, one file after the other. |
| --- | --- | --- | --- | --- | --- |
|  | If you select a single file or select an editor, then the single file appears at the top level in this column. In the example, only one file — the proclib test case — is at the top level. |  |  |  |  |
|  | If you select multiple files in either the Project Explorer or Favorites view, then each of the files appears at the top level in this column, one file after the other. |  |  |  |  |
| Type | In the Depends on section, the Type column displays the dependency relationship — why the dependent file depends on the file that causes the dependency. In the Is referenced by section, the Type column displays the reason that the file that references the original (dependent) file depends on the original file. |  |  |  |  |
| Trigger | The Trigger represents the kind of change that would either: Cause the system to perform a build (build the documents) to ensure that dependencies are maintained. In the example, web_testbed has a Device change Trigger. If there were a change to a device in the web_testbed testbed, then the system would perform a build to ensure that proclib would execute properly. or Cause the file to be unable to perform its function. In the example, web_testbed has an Existence Trigger. If the web_testbed response map were n longer in existence (it was deleted or renamed), then proclib could not execute. Existence: The dependent file is affected if the file is renamed, relocated, or deleted. Change: A change in the file would result in a system rebuild to ensure correct operation of the dependent file. Session type change: A change in the session type for the session profile could cause incorrect operation of the dependent test case Device change: A change to a device definition would require a rebuild to ensure proper test case execution. Procedure call: A change in the call step could affect the associated file. |  | Cause the system to perform a build (build the documents) to ensure that dependencies are maintained. In the example, web_testbed has a Device change Trigger. If there were a change to a device in the web_testbed testbed, then the system would perform a build to ensure that proclib would execute properly. |  | Cause the file to be unable to perform its function. In the example, web_testbed has an Existence Trigger. If the web_testbed response map were n longer in existence (it was deleted or renamed), then proclib could not execute. |
|  | Cause the system to perform a build (build the documents) to ensure that dependencies are maintained. In the example, web_testbed has a Device change Trigger. If there were a change to a device in the web_testbed testbed, then the system would perform a build to ensure that proclib would execute properly. |  |  |  |  |
|  | Cause the file to be unable to perform its function. In the example, web_testbed has an Existence Trigger. If the web_testbed response map were n longer in existence (it was deleted or renamed), then proclib could not execute. |  |  |  |  |
| Source Location | The location in the dependent file that results in the dependency (such as the EXEC call step that refers to a procedure in a foreign test case). When you double-click a resource (or select a resource and click Go to Resource), the editor opens the file to this location. |  |  |  |  |
| Target Location | Applies to call steps only. location in the dependent file (such as the procedure that is being called) |  |  |  |  |
