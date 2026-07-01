---
{
  "chunk_id": "insert_parameter_dialog__to_insert_a_param_or_profile_command_7e067e308b20ad4d",
  "source_file": "topics/insert_parameter_dialog.htm",
  "source_original_path": "topics/insert_parameter_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Using Parameters in Properties or Steps",
    "Inserting a parameter into a property or test case step"
  ],
  "heading_path": [
    "Inserting a parameter into a property or test case step",
    "Inserting a parameter into a property or test case step",
    "To insert a ‘param’ or ‘profile’ command"
  ],
  "anchor": "1136002",
  "context_ids": [
    "insert_parameter_dialog"
  ],
  "index_keywords": [
    "inserting",
    "param commands",
    "parameterizing in open steps",
    "parameterizing session profiles in",
    "parameters in",
    "parameters in open steps",
    "parameters into a property or test case step",
    "profile commands"
  ],
  "index_keyword_paths": [
    "adding > param commands",
    "adding > profile commands",
    "inserting > parameters into a property or test case step",
    "open steps > parameterizing session profiles in",
    "open steps > parameters in",
    "param commands > inserting",
    "parameters > inserting",
    "parameters in open steps",
    "profile commands > inserting",
    "session profiles > parameterizing in open steps"
  ],
  "related_links": [],
  "images": [
    "topics/images/param_insert_param_step1.png",
    "topics/images/insert_param_dialog_label.png",
    "topics/images/param_insert_param_step2.png"
  ],
  "content_hash": "7e067e308b20ad4d",
  "level": 2
}
---

# Inserting a parameter into a property or test case step > Inserting a parameter into a property or test case step > To insert a ‘param’ or ‘profile’ command

You can either insert the command at the cursor location or replace selected text. Follow this procedure:

1. 1

1. In the test case cell or property field, select the Description cell or click in the field. Replace with the required parameter at runtime. We select the number 4, right-click, and then select Insert > Parameter.

1. 2

1. The Insert Parameter dialog opens.

First, specify whether to insert a parameter that is defined in the test case or to use a parameter that is defined in the session profile associated with the current step's session.

Select either Test Case or Session. If you specify Session, then select the session profile from the list.

1. This tree view displays the structured list of parameters defined in the specified test case or session.

1. When you select a parameter from the list, the parameter's name and the field replacement for the param or profile command appear here.

This is the field replacement that will be inserted.

1. To help you select the correct parameter, the Parameter Properties section displays the value and description of the selected parameter.

> **Tip:** Tip Once the parameter appears in the list, you can double-click it to insert the field replacement.

1. 3

1. The param command field replacement now appears, as shown here. At runtime, the param command will be replaced with the value of the AUTOSERVER/username parameter.

![screenshot](topics/images/param_insert_param_step1.png) <!-- image_chunk: img_6b0bf68e6af23683 -->

![screenshot](topics/images/insert_param_dialog_label.png) <!-- image_chunk: img_b0eb52ec36db5eea -->

![screenshot](topics/images/param_insert_param_step2.png) <!-- image_chunk: img_443ab4e6ebab587d -->
