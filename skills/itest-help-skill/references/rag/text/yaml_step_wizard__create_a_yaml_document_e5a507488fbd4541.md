---
{
  "chunk_id": "yaml_step_wizard__create_a_yaml_document_e5a507488fbd4541",
  "source_file": "topics/yaml_step_wizard.htm",
  "source_original_path": "topics/yaml_step_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "YAML Step Editor",
    "Insert YAML Step Wizard"
  ],
  "heading_path": [
    "Insert YAML Step Wizard",
    "Insert YAML Step Wizard",
    "Create a YAML document"
  ],
  "anchor": "1326540",
  "context_ids": [
    "yaml_action_page",
    "yaml_add_page",
    "yaml_create_page",
    "yaml_document_page",
    "yaml_location_page",
    "yaml_replace_page",
    "yaml_step_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "yaml_steps_in_test_case.htm#1327517"
  ],
  "images": [
    "topics/images/yaml_create_a_yaml_doc_paste.png"
  ],
  "content_hash": "e5a507488fbd4541",
  "level": 2
}
---

# Insert YAML Step Wizard > Insert YAML Step Wizard > Create a YAML document

Allows you to define a new YAML document. Select the option Create a YAML document and click Next to display the Create a YAML document dialog. See https://yaml.org/refcard.html for YAML syntax.

| Document Name | Mandatory. Enter a document name. The name of the document should be unique when creating document using yamlCreate step. Note Only underscore (_) is allowed in the document name and not any other special characters (e.g., hyphen (-) is not allowed) | Note | Only underscore (_) is allowed in the document name and not any other special characters (e.g., hyphen (-) is not allowed) |
| --- | --- | --- | --- |
| Note | Only underscore (_) is allowed in the document name and not any other special characters (e.g., hyphen (-) is not allowed) |  |  |
| Global scope | Select to indicate whether the YAML command performs thread-safe operations on a document in local or global space. That is, to reference a simple variable name that either exists in local namespace (Global scope is un-checked) or global namespace (Global scope is checked). Important All operations on the same document should be performed in the same scope (global or local). That is, they should have the same value for 'Global Scope' option. For example, if a document was created with local scope using yamlCreate command, the operations yamlGet, yamlAdd, yamlSet, yamlDelete will fail if they are performed on a document with same name but in the global scope. | Important |  |
| Important |  |  |  |
| Read from file | Select to create a new YAML document by reading from an existing YAML document. Select file from your workspace or from the file system. Note The file content is not visible when create a new document from an existing file. The file content is visible in the Response view after the test command is executed. | Note | The file content is not visible when create a new document from an existing file. The file content is visible in the Response view after the test command is executed. |
| Note | The file content is not visible when create a new document from an existing file. The file content is visible in the Response view after the test command is executed. |  |  |
| Paste content | Create a new YAML document by pasting content. You may edit the pasted content as required |  |  |
| Finish | Click finish and the yamlCreate command is inserted in the test case step. Note A YAML document is a variable in iTest and the step yamlCreate creates this variable. | Note | A YAML document is a variable in iTest and the step yamlCreate creates this variable. |
| Note | A YAML document is a variable in iTest and the step yamlCreate creates this variable. |  |  |
| Cancel | Click Cancel to discard your changes and exit Wizard. |  |  |

After including all the information as required on the wizard, only one YAML command will be inserted into the test case. See YAML Steps in Test Case.

![screenshot](topics/images/yaml_create_a_yaml_doc_paste.png) <!-- image_chunk: img_2ddeabce8630d0b5 -->
