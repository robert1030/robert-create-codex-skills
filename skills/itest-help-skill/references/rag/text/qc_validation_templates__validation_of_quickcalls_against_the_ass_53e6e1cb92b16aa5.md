---
{
  "chunk_id": "qc_validation_templates__validation_of_quickcalls_against_the_ass_53e6e1cb92b16aa5",
  "source_file": "topics/qc_validation_templates.htm",
  "source_original_path": "topics/qc_validation_templates.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Library Template (QuickCalls)",
    "Validation of QuickCalls against the associated template"
  ],
  "heading_path": [
    "Validation of QuickCalls against the associated template",
    "Validation of QuickCalls against the associated template"
  ],
  "anchor": "1522426",
  "context_ids": [
    "qc_validation_templates"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "qc_template.htm#1527324"
  ],
  "images": [
    "topics/images/qc_templ_changeProcName.png",
    "topics/images/qc_templ_changeArgNameMandatorChkBox.png",
    "topics/images/qc_templ_changeResponseBlockType.png"
  ],
  "content_hash": "53e6e1cb92b16aa5",
  "level": 1
}
---

# Validation of QuickCalls against the associated template > Validation of QuickCalls against the associated template

iTest validates as follows to ensure that the QuickCall testcase linked to the template use the same set of procedures name, argument names (in their defined order), response type and sample data as those defined in the template.

> **Note:** Note You may define additional procedure name and relevant arguments and response type in the new testcase linked to an existing template.

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

> **Note:** Note The QuickCall or TestCase that links to the generated template (see Implementation) and template should have the same response JSON/YAML keys and the values can be different.

![screenshot](topics/images/qc_templ_changeProcName.png) <!-- image_chunk: img_f219ddfe71b1d191 -->

![screenshot](topics/images/qc_templ_changeArgNameMandatorChkBox.png) <!-- image_chunk: img_8d8bfcfe70546aa6 -->

![screenshot](topics/images/qc_templ_changeResponseBlockType.png) <!-- image_chunk: img_8c3a62786b75e8df -->
