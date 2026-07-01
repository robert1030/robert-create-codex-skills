---
{
  "chunk_id": "tce_general_page__local_topology_b855710543ad6b9c",
  "source_file": "topics/tce_general_page.htm",
  "source_original_path": "topics/tce_general_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "General page on the Test Case Editor",
    "Test Case editor: General page"
  ],
  "heading_path": [
    "Test Case editor: General page",
    "Test Case editor: General page",
    "Local Topology"
  ],
  "anchor": "1963152",
  "context_ids": [
    "tce_general_page"
  ],
  "index_keywords": [
    "General page",
    "Test Case editor",
    "messaging out",
    "run command responses",
    "specifying",
    "summary reports",
    "summary responses",
    "test suites"
  ],
  "index_keyword_paths": [
    "General page > Test Case editor",
    "Test Case editor > General page",
    "comments > messaging out",
    "run command responses",
    "summary reports",
    "summary responses",
    "test suites",
    "testbeds > specifying"
  ],
  "related_links": [
    "executing_tests_preferences_execution.htm#1155279",
    "global_topology.htm#1279553"
  ],
  "images": [],
  "content_hash": "b855710543ad6b9c",
  "level": 2
}
---

# Test Case editor: General page > Test Case editor: General page > Local Topology

| Local topology | Optional. Specify a topology to use for the sessions in the test case. Topologies define devices and specify a list of session profiles and can set parameter values. Topologies define devices and specify a list of session profiles. When you specify a topology, you can make the test case more flexible by using parameters defined in the associated session profiles to customize behavior at runtime. If the Local topology property is blank or no Global topology is specified, then device URIs are not supported in open steps. About Global topology If you have identified a Global topology and you also specify a Local topology, then, at runtime, you will be asked whether to use the Global topology or the Local topology during execution. You can configure whether the dialog box should or should not appear or that either the Local or Global topology should be used when this condition arises. See Setting preferences for execution. Also, see Global topology and Global testbed. Test documentation includes the topology When a topology is used for execution, to help you keep track of which topology was used, an informational execution message will appear immediately after the execution start message. The message identifies the fully qualified URI of the topology that is being used. In addition, the URI appears in the header section of the test report. |
| --- | --- |
