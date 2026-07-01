---
{
  "chunk_id": "tc_template__creating_a_library_template_401223845aa71dd3",
  "source_file": "topics/tc_template.htm",
  "source_original_path": "topics/tc_template.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Library Template",
    "Creating a template from existing test cases"
  ],
  "heading_path": [
    "Creating a template from existing test cases",
    "Creating a template from existing test cases",
    "Creating a Library template"
  ],
  "anchor": "1921139",
  "context_ids": [
    "tc_template"
  ],
  "index_keywords": [
    "lib_template.fftc",
    "library templates",
    "template"
  ],
  "index_keyword_paths": [
    "lib_template.fftc",
    "library templates",
    "test cases > template"
  ],
  "related_links": [
    "tc_template_validation.htm#1922631"
  ],
  "images": [
    "topics/images/tc_templ_define_common_procdures.png",
    "topics/images/tc_templ_right-click-generate-library-template.png",
    "topics/images/tc_templ_TC_linked_to_library-template.png"
  ],
  "content_hash": "401223845aa71dd3",
  "level": 2
}
---

# Creating a template from existing test cases > Creating a template from existing test cases > Creating a Library template

1. Create a test case with procedures, and/or property settings commonly. See example shown below.

1. 2

1. Select the test case in the Project Explorer, right-click and then select Generate Library Template.

The Select library template destination displays.

Container: The default location is the same as the location of the test case. You may browse and navigate to a different existing folder.

1. File name: Default file name is lib_template. If the file name exists, an error displays saying the file name already exists. Provide a different file name, if required and click OK to save the library template.

In the original testcase, iTest adds a link to the new test case. That is, on the original TestCase > General tab, adds the library template location and name as shown in the screenshot below. If the original testcase already had this property filled, the value will be overwritten.

These public procedure definitions are copied to the new testcase from the original testcase.

- Procedure name

- Argument list, the order of the arguments, and properties for each argument: Name, Mandatory flag, and Default value

- Procedure response type and Sample

> **Note:** Note If original testcase was marked as a procedure library, the new testcase will also be marked as a procedure library.

Language of the testcase will be set to the default language selected in Windows > Preferences (as default when creating any new testcase).

XPath version of the newly created testcase will be set to 3.1 (as default when creating any new testcase).

Implementation

When you click Generate Library Template, a template is generated from the Testcase/QuickCall procedure library. The original test case will automatically have Library Template property (on Testcase > General tab) set to URL of the newly generated template. The original testcase is considered an implementation of the template. You can also manually set the Library Template URL to an existing template. The elements can be queried from the response structure of both template and the implementation of the template.

1. 3

1. iTest validates the testcase against the associated template and ensures that the procedure names, the arguments name, response structure, and sample data are the same as that defined in the template. See Validation of testcase against the associated template below.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/tc_templ_define_common_procdures.png) <!-- image_chunk: img_54b4a1358a099de0 -->

![screenshot](topics/images/tc_templ_right-click-generate-library-template.png) <!-- image_chunk: img_54c8d388a6bb27db -->

![screenshot](topics/images/tc_templ_TC_linked_to_library-template.png) <!-- image_chunk: img_43c8e9001f91858c -->
