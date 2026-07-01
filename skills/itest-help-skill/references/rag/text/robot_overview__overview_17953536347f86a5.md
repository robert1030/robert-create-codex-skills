---
{
  "chunk_id": "robot_overview__overview_17953536347f86a5",
  "source_file": "topics/robot_overview.htm",
  "source_original_path": "topics/robot_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Export a QuickCall to Robot Library",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview"
  ],
  "anchor": "1343970",
  "context_ids": [
    "json_editor_overview",
    "robot_overview"
  ],
  "index_keywords": [
    "overview",
    "quickcalls export",
    "to robot library, quickcalls"
  ],
  "index_keyword_paths": [
    "export > to robot library, quickcalls",
    "robot library > overview",
    "robot library > quickcalls export"
  ],
  "related_links": [
    "pal_python_automation_library_overview.htm#",
    "robot_export_wizard.htm#1335822",
    "robot_verify_exported_library.htm#1346962",
    "robot_verify_keywords_itestcommon_file.htm#1364632",
    "robot_exported_library_in_ride.htm#1360606",
    "session_profile_concept.htm#",
    "quickcalls_overview.htm#"
  ],
  "images": [],
  "content_hash": "17953536347f86a5",
  "level": 1
}
---

# Overview > Overview

> **Note:** Note iTest installer includes PyDev (Python IDE) and RED (Robot Editor) plugins for ease of your work. See the following links for more details:

- PyDev: https://marketplace.eclipse.org/content/pydev-python-ide-eclipse

- RED: https://marketplace.eclipse.org/content/red-robot-editor

iTest export wizard creates a keyword library that allows a Robot Framework user to build robot test cases and test suites constructed with keywords that map to QuickCalls. These test case and test suites (constructed with keywords that map to QuickCalls) allows developers to leverage useful iTest QuickCalls and Response Maps in their robot tests.

The exported keywords library is a Python file, generated from QuickCall (.fftc) file. The definition of keywords follows the syntax of Robot Static library APIs as document: Robot test library APIs (http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#different-test-library-apis)

> **Note:** Note Robot Framework is a Python-based, extensible keyword-driven test automation framework for end-to-end acceptance testing and acceptance-test-driven development. See http://robotframework.org/ for details.

The keyword library depends on Spirent Automation Libraries to invoke QuickCalls from iTest session. Ensure that you have configured Python environment.

Python Spirent Automation Library as described in “Python Automation Library”

> **Note:** Note The exported Robot library supports Python 2.7 and Python 3.6.

iTest keyword libraries are compatible with Robot Framework IDE (RIDE), the integrated development environment to implement automated tests for the Robot Framework.

> **Note:** Note Using the iTest exported keywords and the support file in your Robot Framework test consumes iTest license.

This chapter includes the following topics that describes Robot key development using iTest, that is, exporting an existing QuickCall library as a Robot library, viewing the contents to understand how iTest maps the QuickCall procedures and keywords before using it in the Robot Framework test (developing Robot Script for using and executing in your environment).

- iTest Export Wizard—Export to Robot library

- Contents of the exported Robot library

- Exported keywords in iTestCommon.py

- Execute exported Robot library from an external environment

> **Note:** Note Any changes to a QuickCall (except argument changes) that has been exported to a keyword file, does not have to be exported again as the change affects only iTest QuickCalls.

See Session Profiles and QuickCalls: Defining and using a library of custom actions for details about creating iTest Sessions and defining QuickCall libraries.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
