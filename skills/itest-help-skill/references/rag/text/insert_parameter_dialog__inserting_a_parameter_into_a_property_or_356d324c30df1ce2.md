---
{
  "chunk_id": "insert_parameter_dialog__inserting_a_parameter_into_a_property_or_356d324c30df1ce2",
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
    "Inserting a parameter into a property or test case step"
  ],
  "anchor": "1135987",
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
  "related_links": [
    "parameters_page.htm#1135242"
  ],
  "images": [],
  "content_hash": "356d324c30df1ce2",
  "level": 1
}
---

# Inserting a parameter into a property or test case step > Inserting a parameter into a property or test case step

This topic describes the use of the Insert Parameter dialog box to insert a param or profile command into a test case step or property (that is, any field that supports field replacements).

- You can insert a param command or a profile command into the field.

- You can create a new parameter in the test case and then insert a param command that uses the new parameter (but you cannot set advanced properties for the new parameter).

- You cannot edit existing parameters using the Insert Parameter dialog box. Instead, use the Parameters page to set the value and advanced properties of a parameter. Parameters can be defined in the current test case, or in a different test case that loaded as a result of a foreign procedure, or in the session profile associated with the step. For instructions on defining parameters, see Working with parameters: The Parameters page.

Important If the session defined in the Open step uses secret parameters, the test case Open step output will be masked (as it is not possible to determine the content of Open step welcome message).
