---
{
  "chunk_id": "activity_review_test_reports__to_create_a_new_test_case_or_open_an_exi_7839327bae75b344",
  "source_file": "topics/activity_review_test_reports.htm",
  "source_original_path": "topics/activity_review_test_reports.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Activity View"
  ],
  "heading_path": [
    "Activity View",
    "Activity View",
    "Developing a test case",
    "To create a new test case or open an existing test case"
  ],
  "anchor": "1713345",
  "context_ids": [],
  "index_keywords": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor",
    "Work on a test case page",
    "adding session profiles to",
    "analysis rules",
    "defining for devices in topologies",
    "described",
    "editing",
    "examples",
    "find issues in",
    "importing",
    "in analysis rules defined",
    "issues in test reports",
    "preference settings",
    "project set files",
    "projects",
    "psf files",
    "session profiles in topologies",
    "setting criteria"
  ],
  "index_keyword_paths": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor > preference settings",
    "Work on a test case page",
    "adding > session profiles in topologies",
    "analysis rules > described",
    "analysis rules > examples",
    "configuring > session profiles in topologies",
    "devices in topologies > adding session profiles to",
    "editing > session profiles in topologies",
    "editor preferences > Session Profile editor",
    "examples > analysis rules",
    "extractors > in analysis rules defined",
    "find > issues in test reports",
    "importing > project set files",
    "importing > projects",
    "importing > psf files",
    "issues > finding in test reports test reports > find issues in",
    "pass/fail > setting criteria",
    "preference settings > Session Profile editor",
    "processors > in analysis rules defined",
    "project set files > importing",
    "projects > importing",
    "psf files > importing",
    "session profiles > defining for devices in topologies",
    "topologies > adding session profiles to",
    "topologies > editing",
    "validating responses > analysis rules",
    "views > Execution view"
  ],
  "related_links": [
    "test_cases_breakpoints.htm#1714021"
  ],
  "images": [],
  "content_hash": "7839327bae75b344",
  "level": 3
}
---

# Activity View > Activity View > Developing a test case > To create a new test case or open an existing test case

When you select the Develop a test case activity page, you first specify whether to work on an existing test case or to create a new test case.

1. On the Develop a test case dialog box, select either Select an existing test case or Create a new test case. The dialog box changes based on your selection.

- To work on an existing test case, navigate to the document and click OK.

- To create a new test case, specify the following settings and click OK.

| Save in | Navigate to the project and folder to create the test case in. Typically, you create a test case in the default project named my_project in the default folder named test_cases. |
| --- | --- |
| File name | Type a name for the new document. Test case files use the .fftc filename extension. |
| Owner | Optional. Type the unique identifier of the person responsible for developing and/or maintaining the test case (typically, the name, login name, or email address), Default: current username |
| Headline | Optional. Type a one-line description that documents the usage and function of the test case. In addition to the locations mentioned earlier, this text also appears in the Favorites view to help you when selecting a test case. |
| Description | Optional. Type additional text that describes the test case to make its usage clear to coworkers. Tip This is an excellent place to paste a copy of the test plan. |
| Tip | This is an excellent place to paste a copy of the test plan. |
| Use test case template | Check the box to add the steps and properties of the template test case into the new test case. For information on creating a template test case, see Breakpoints: Overview. Default: unchecked |
| Associate a topology with the test case | Optional. Specify a topology to use for the sessions in the test case. When you specify a topology, you can make the test case more flexible by using parameters defined in the associated session profiles to customize behavior at runtime. If the Associate a topology with the test cased property is blank or no Global topology is specified, then device URIs are not supported in open steps. Test documentation includes the topology When a topology is used for execution, to help you keep track of which topology was used, an informational execution message will appear immediately after the execution start message. The message identifies the fully qualified URI of the topology that is being used. In addition, the URI appears in the header section of the test report. |

1. 2

1. When you click OK, the Develop a test case activity page opens.
