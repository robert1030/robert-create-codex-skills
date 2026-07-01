---
{
  "chunk_id": "tc_template_validation__validation_of_testcase_against_the_assoc_883d8be31e114bcd",
  "source_file": "topics/tc_template_validation.htm",
  "source_original_path": "topics/tc_template_validation.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Library Template",
    "Validation of testcase against the associated template"
  ],
  "heading_path": [
    "Validation of testcase against the associated template",
    "Validation of testcase against the associated template"
  ],
  "anchor": "1922631",
  "context_ids": [
    "tc_template_validation"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tc_template.htm#1927468"
  ],
  "images": [
    "topics/images/tc_templ_change_proc_name_in_newTC.png",
    "topics/images/tc_templ_change_proc_ArgsNameOrder_in_newTC.png",
    "topics/images/tc_templ_change_proc_ResponseType_in_newTC.png"
  ],
  "content_hash": "883d8be31e114bcd",
  "level": 1
}
---

# Validation of testcase against the associated template > Validation of testcase against the associated template

iTest validates as follows to ensure that the test cases linked to the templates use the same set of procedures name, argument names (in their defined order), response type and sample data as those defined in the template.

> **Note:** Note You may define additional procedure name and relevant arguments and response type in the new test cases linked to an existing template.

1. Procedure names: The new test case linked to the template cannot modify the name of the procedures inherited from the template. For example, changing procedure name, indicates an error on the General tab. Go to the General tab and notice an error displayed saying the Procedure defined in the library template is missing in the testcase (as shown below).

Procedure properties Headline, Author, Description, etc., are not validated against the template.

1. 2

1. Arguments names and order: The new testcase based on the template cannot have different argument names and order.

The set of arguments defined for the procedures must be the same as in the template.

1. The order of arguments defined must be the same as in the template.

1. The option This Argument is required must be as defined in the template.

> **Note:** Note The default values and description of the arguments may be different than those defined in the template.

1. Description and Default value: You may modify these values as required in the new testcase.

1. 3

1. Response: The Block response type and Sample data is validated to ensure that it is the same as the template definition. Modifying these definitions displays an error as shown below.

> **Note:** Note The QuickCall or TestCase that links to the generated template (Implementation) and template should have the same response JSON/YAML keys and the values can be different.

![screenshot](topics/images/tc_templ_change_proc_name_in_newTC.png) <!-- image_chunk: img_44bcf749ef2a84ac -->

![screenshot](topics/images/tc_templ_change_proc_ArgsNameOrder_in_newTC.png) <!-- image_chunk: img_de9a9ef115f6399c -->

![screenshot](topics/images/tc_templ_change_proc_ResponseType_in_newTC.png) <!-- image_chunk: img_0152d483896bbcea -->
