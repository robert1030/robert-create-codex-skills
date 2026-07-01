---
{
  "chunk_id": "qc_template__creating_a_quickcall_library_template_368df430b3cb03e3",
  "source_file": "topics/qc_template.htm",
  "source_original_path": "topics/qc_template.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Library Template (QuickCalls)",
    "Creating a template from existing QuickCalls"
  ],
  "heading_path": [
    "Creating a template from existing QuickCalls",
    "Creating a template from existing QuickCalls",
    "Creating a QuickCall Library template"
  ],
  "anchor": "1520526",
  "context_ids": [
    "qc_template"
  ],
  "index_keywords": [
    "lib_template.fftc",
    "library templates",
    "template"
  ],
  "index_keyword_paths": [
    "QuickCalls > template",
    "lib_template.fftc",
    "library templates"
  ],
  "related_links": [
    "qc_validation_templates.htm#1522426"
  ],
  "images": [
    "topics/images/qc_templ_define_common.png",
    "topics/images/tc_templ_right-click-generate-library-template.png",
    "topics/images/qc_templ_created.png"
  ],
  "content_hash": "368df430b3cb03e3",
  "level": 2
}
---

# Creating a template from existing QuickCalls > Creating a template from existing QuickCalls > Creating a QuickCall Library template

1. Create a test case with procedures, and/or property settings you use often. See example shown below.

1. 2

1. Select the test case with the defined QuickCall procedures in the Project Explorer, right-click and then select Generate Library Template.

The Select library template destination dialog displays.

Container: The default location is the same as the location of the test case. You may browse and navigate to a different existing folder.

1. File name: Default file name is lib_template. If the file name exists, an error displays saying the file name already exists. Provide a different file name, if required and click OK to save the QuickCall library template.

1. 3

1. iTest creates a new testcase lib_template for QuickCalls in the provided destination.

- In the original testcase, iTest adds a link to the new test case. That is, on the original TestCase > General tab, adds the library template location and name as shown in the screenshot below. If the original testcase already had this property filled, the value will be overwritten.

- If original testcase was marked as a QC library, new testcase will also be marked as a QC library. That is, the checkbox QuickCall Library (on will be enabled, and the associated Session Profile will be blank.

- Other properties of the original testcase that are not copied: private procedures, steps in the public procedures, Parameters, etc.

- Language of the testcase will be set to the default language selected in Windows > Preferences (as default when creating any new testcase).

- XPath version of the newly created testcase will be set to 3.1 (as default when creating any new testcase).

- The entry point in the new test case will be set to main (by default when creating any new testcase) and an empty private main procedure will be generated.

These public procedure definitions are copied to the new testcase from the original testcase.

- Procedure name

- Argument list, the order of the arguments, and properties for each argument: Name, Mandatory flag, and Default value

- Procedure response type and Sample.

Implementation

When you click Generate Library Template, a template is generated from the Testcase/QuickCall procedure library. The original test case will automatically have Library Template property (on Testcase > General tab) set to URL of the newly generated template. The original testcase is considered an implementation of the template. You can also manually set the Library Template URL to an existing template. The elements can be queried from the response structure of both template and the implementation of the template.

1. 4

1. iTest validates the QuickCall testcase against the associated template and ensures that the procedure names, the arguments name, response structure, and sample data are the same as that defined in the template. See Validation of QuickCalls against the associated template below.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/qc_templ_define_common.png) <!-- image_chunk: img_02f2f4217032bd1d -->

![screenshot](topics/images/tc_templ_right-click-generate-library-template.png) <!-- image_chunk: img_54c8d388a6bb27db -->

![screenshot](topics/images/qc_templ_created.png) <!-- image_chunk: img_e78085aefb996f74 -->
