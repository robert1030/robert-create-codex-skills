---
{
  "chunk_id": "insert_parameter_dialog__advanced_users_inserting_a_session_profi_01927ff5f9dec89a",
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
    "Advanced users: Inserting a session profile parameter when the session profile is resolved at runtime"
  ],
  "anchor": "1136039",
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
  "images": [],
  "content_hash": "01927ff5f9dec89a",
  "level": 2
}
---

# Inserting a parameter into a property or test case step > Inserting a parameter into a property or test case step > Advanced users: Inserting a session profile parameter when the session profile is resolved at runtime

In some test case designs, session profile information for an open step is held in a parameter so that the identity of the session profile is determined at runtime. Later in the test case, a step might use a parameter that is defined in the — at design-time, unknown — session profile.

Follow this procedure to insert a parameter that is defined in the session profile—the session profile that will not be resolved until runtime.

> **Note:** Note You will have to know the name of the parameter before you start.

1. 1

1. Create an open step in the test case that uses a param command in the Description cell to specify the session profile.

1. 2

1. Later in the test case, for the step that will use the parameter, select the text or click in the field.

1. 3

1. In the Insert Parameter dialog box, select Session.

1. 4

1. In the Session text box, type the param command that appears in the Description cell for the open step. Notice that, because you cannot specify a particular session profile, no parameters appear in the list box. For this reason, you have to know the name of the parameter in the next step.

1. 5

1. Type the name of the parameter into the Parameter name text box.

1. 6

1. Click Insert. An appropriate param command is inserted.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
