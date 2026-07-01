---
{
  "chunk_id": "tce_steps_page__step_properties_re_direct_to_properties__d62c384bf0b6c676",
  "source_file": "topics/tce_steps_page.htm",
  "source_original_path": "topics/tce_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Test Case editor: Steps page"
  ],
  "heading_path": [
    "Test Case editor: Steps page",
    "Test Case editor: Steps page",
    "Description",
    "Step Properties (re-direct to properties configuration page)"
  ],
  "anchor": "1855457",
  "context_ids": [
    "tce_steps_page"
  ],
  "index_keywords": [
    "Python Action syntax, warnings",
    "Steps page",
    "Test Case editor",
    "editing"
  ],
  "index_keyword_paths": [
    "Python Action syntax, warnings",
    "Steps page",
    "Steps page > Test Case editor",
    "Test Case editor > Steps page",
    "step properties > editing",
    "steps > editing"
  ],
  "related_links": [
    "test_case_editor_steps_page.htm#1284516"
  ],
  "images": [
    "topics/images/test_case_editor_2.17.jpg",
    "topics/images/test_case_editor_2.18.jpg",
    "topics/images/test_case_editor_2.19.jpg",
    "topics/images/tce_open_session.png",
    "topics/images/test_case_editor_2.21.jpg"
  ],
  "content_hash": "d62c384bf0b6c676",
  "level": 3
}
---

# Test Case editor: Steps page > Test Case editor: Steps page > Description > Step Properties (re-direct to properties configuration page)

For ease of locating and changing property of some steps, click … is appended to the Description cell of some of the steps to easily navigate to the corresponding step property page. For example, see “POST” step below. Clicking ... expands the Step Properties section, selects POST Step Properties node on the property tree and also expands its children nodes.

| Note: You may open the context specific information—Step Properties section in the Properties pane as follows. Right-click to display the menu and select “Show Properties View”. OR Click the ellipsis on the step command, where applicable. |
| --- |

Being re-directed to properties configuration page (clicking ...) applies to all test case steps with the below exceptions.

1. If an existing test case step has a non-empty combo box, the … button is not available.

1. 2

1. If steps have no “Xxx Step Properties” node on the property tree, iTest does not display the … button (see the drop-down option available).

> **Note:** Note “Xxx” is the action name of the step and the first letter is not case-sensitive.

1. 3

1. For some steps (e.g., open step), the … (ellipsis) button displays a dialog or wizard rather than step properties.

1. 4

1. For all session types that involve GUI operation (e.g., Selenium, web, Flex, Swing and Ranorex), that is, for those session where the “Target” on “General” page is meaningful, if the form map is specified in the corresponding session profile, whether the current step (“close” step is excluded) uses form map or not, clicking … selects the Step Properties > General node to show Context and Target by default.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/test_case_editor_2.17.jpg) <!-- image_chunk: img_7def49cfe9e581ea -->

![screenshot](topics/images/test_case_editor_2.18.jpg) <!-- image_chunk: img_c27a88d3fed2ccb5 -->

![screenshot](topics/images/test_case_editor_2.19.jpg) <!-- image_chunk: img_00f7f2687e6eeae6 -->

![screenshot](topics/images/tce_open_session.png) <!-- image_chunk: img_85c9af1cf914786e -->

![screenshot](topics/images/test_case_editor_2.21.jpg) <!-- image_chunk: img_703cd27d1ee45c57 -->
