---
{
  "chunk_id": "test_report_setting_preferences__examples_of_the_itest_gui_and_itestrt_sc_d76ccb6ad774bc8a",
  "source_file": "topics/test_report_setting_preferences.htm",
  "source_original_path": "topics/test_report_setting_preferences.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Setting preferences for Test Reports"
  ],
  "heading_path": [
    "Setting preferences for Test Reports",
    "Setting preferences for Test Reports",
    "Spirent > General > Test Reports > Auto-Export Test Reports",
    "Examples of the iTest GUI and iTestRT scenarios with Project schema and Absolute path:"
  ],
  "anchor": "998406",
  "context_ids": [
    "test_report_setting_preferences"
  ],
  "index_keywords": [
    "preference settings",
    "test reports"
  ],
  "index_keyword_paths": [
    "preference settings > test reports",
    "test reports > preference settings"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "d76ccb6ad774bc8a",
  "level": 4
}
---

# Setting preferences for Test Reports > Setting preferences for Test Reports > Spirent > General > Test Reports > Auto-Export Test Reports > Examples of the iTest GUI and iTestRT scenarios with Project schema and Absolute path:

The table below shows an example of the specified project schema - folder path, the tests executes and test reports saved as per the specified folder path.

> **Note:** Note Syntax to specify folder for test report:

- [project://]: 2 slashes indicates workspace

- [project://{project}]: 2 slashes + {project}, indicates workspace + project name which contain the running testcase

- [project:///]: 3 slashes, indicates workspace + master project name

| Syntax specified in: Folder for test reports | Running single testcase case: project1/testcases/demoA/tc1.fftc project2/testcases/demoB/tc2.fftc |  | project1/testcases/demoA/tc1.fftc |  | project2/testcases/demoB/tc2.fftc | Running nested testcase case: project1/testcases/demoA/mastertc.fftc project2/testcases/demoB/child1.fftc project3/testcases/demoC/child2.fftc |  | project1/testcases/demoA/mastertc.fftc |  | project2/testcases/demoB/child1.fftc |  | project3/testcases/demoC/child2.fftc |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | project1/testcases/demoA/tc1.fftc |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | project2/testcases/demoB/tc2.fftc |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | project1/testcases/demoA/mastertc.fftc |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | project2/testcases/demoB/child1.fftc |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | project3/testcases/demoC/child2.fftc |  |  |  |  |  |  |  |  |  |  |  |  |  |
| iTest GUI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| project:///save_folder (3 slashes) | project1/save_folder/tc1/tc1_<datetime>.html project2/save_folder/tc2/tc2_<datetime>.html | project1/save_folder/mastertc/mastertc_<datetime>.html project1/save_folder/mastertc/child1_<datetime>.html project1/save_folder/mastertc/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| project://{project} (2 slashes) | project1/tc1/tc1_<datetime>.html project2/tc2/tc2_<datetime>.html | project1/mastertc/mastertc_<datetime>.html project2/mastertc/child1/child1_<datetime>.html project3/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| project:///{path_in_project} (3 slashes) | project1/testcases/demoA/tc1/tc1_<datetime>.html project2/testcases/demoB/tc2/tc2_<datetime>.html | project1/testcases/demoA/mastertc/mastertc_<datetime>.html project1/testcases/demoB/mastertc/child1/child1_<datetime>.html project1/testcases/demoC/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| project:///{testcase} (3 slashes) | project1/tc1/tc1/tc1_<datetime>.html project2/tc2/tc2/tc2_<datetime>.html | project1/mastertc/mastertc/mastertc_<datetime>.html project1/child1/mastertc/child1/child1_<datetime>.html project1/child2/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| project:///{date} (3 slashes) | project1/yyyy-MM-dd/tc1/tc1_<datetime>.html project2/yyyy-MM-dd/tc2/tc2_<datetime>.html | project1/yyyy-MM-dd/mastertc/mastertc_<datetime>.html project1/yyyy-MM-dd/mastertc/child1/child1_<datetime>.html project1/yyyy-MM-dd/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| project://{project}/{date} (2 slashes) | project1/yyyy-MM-dd/tc1/tc1_<datetime>.html project2/tc2/tc2_<datetime>.html | project1/yyyy-MM-dd/mastertc/mastertc_<datetime>.html project2/yyyy-MM-dd/mastertc/child1/child1_<datetime>.html project3/yyyy-MM-dd/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder | .../save_folder/tc1/tc1_<datetime>.html .../save_folder/tc2/tc2_<datetime>.html | .../save_folder/mastertc/mastertc_<datetime>.html .../save_folder/mastertc/child1_<datetime>.html .../save_folder/mastertc/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder/{project} | .../save_folder/project1/tc1/tc1_<datetime>.html .../save_folder/project2/tc2/tc2_<datetime>.html | .../save_folder/project1/mastertc/mastertc_<datetime>.html .../save_folder/project2/mastertc/child1/child1_<datetime>.html .../save_folder/project3/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder/{path_in_project} | .../save_folder/testcases/demoA/tc1/tc1_<datetime>.html .../save_folder/testcases/demoB/tc2/tc2_<datetime>.html | .../save_folder/testcases/demoA/mastertc/mastertc_<datetime>.html .../save_folder/testcases/demoB/mastertc/child1/child1_<datetime>.html .../save_folder/testcases/demoC/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder/{testcase} | .../save_folder/tc1/tc1/tc1_<datetime>.html .../save_folder/tc2/tc2/tc2_<datetime>.html | .../save_folder/mastertc/mastertc/mastertc_<datetime>.html .../save_folder/child1/mastertc/child1/child1_<datetime>.html .../save_folder/child2/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder/{date} | .../save_folder/yyyy-MM-dd/tc1/tc1_<datetime>.html .../save_folder/yyyy-MM-dd/tc2/tc2_<datetime>.html | .../save_folder/yyyy-MM-dd/mastertc/mastertc_<datetime>.html .../save_folder/yyyy-MM-dd/mastertc/child1/child1_<datetime>.html .../save_folder/yyyy-MM-dd/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder/{project}/{date} | .../save_folder/project1/yyyy-MM-dd/tc1/tc1_<datetime>.html .../save_folder/project2/yyyy-MM-dd/tc2/tc2_<datetime>.html | .../save_folder/project1/yyyy-MM-dd/mastertc/mastertc_<datetime>.html .../save_folder/project2/yyyy-MM-dd/mastertc/child1/child1_<datetime>.html .../save_folder/project3/yyyy-MM-dd/mastertc/child2/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
| iTestRT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| project:// | Cannot save report | Cannot save report |  |  |  |  |  |  |  |  |  |  |  |  |
| project://{tcfilename} | Cannot save report | Cannot save report |  |  |  |  |  |  |  |  |  |  |  |  |
| file://.../save_folder | .../save_folder/tc1_<datetime>.html .../save_folder/tc2_<datetime>.html | .../save_folder/mastertc_<datetime>.html .../save_folder/child1_<datetime>.html .../save_folder/child2_<datetime>.html |  |  |  |  |  |  |  |  |  |  |  |  |
