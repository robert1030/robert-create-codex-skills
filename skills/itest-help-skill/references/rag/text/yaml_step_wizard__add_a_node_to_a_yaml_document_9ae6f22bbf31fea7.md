---
{
  "chunk_id": "yaml_step_wizard__add_a_node_to_a_yaml_document_9ae6f22bbf31fea7",
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
    "Add a node to a YAML document"
  ],
  "anchor": "1368607",
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
    "#1368901",
    "yaml_steps_in_test_case.htm#1327517"
  ],
  "images": [
    "topics/images/yaml_query.png",
    "topics/images/yaml_add_next.png"
  ],
  "content_hash": "9ae6f22bbf31fea7",
  "level": 2
}
---

# Insert YAML Step Wizard > Insert YAML Step Wizard > Add a node to a YAML document

Allows you to Insert a YAML node in the document. The Add a node option allows you to select a node value from an existing YAML document and add a child or sibling node.

| Document Name | Document name is a variable used during test execution to reference a yaml document. You can set document name manually or select document created in previous steps, or edit current procedure's response. The document name is automatically populated when you select an existing document in Created in yamlCreate step. |
| --- | --- |
| Global scope | See Global scope |
| Edit this procedure’s YAML response | Select this option and if the procedure has a YAML response, the content displays in the Sample section. |
| Created in createYAML step | Select option to edit an existing YAML document. The wizard displays a list of YAML document(s) created in yamlCreate. Select a document and the content displays in the Sample section. |
| Sample | If you select an existing YAML response or document created using yamlCreate, then the wizard displays the document contents. You may edit the content as required. |
| Next | Click Next to display the Add YAML Node dialog. |

The Add YAML node dialog displays the selected YAML document in the editor (in expand/collapse structure).

| Add sibling Add child | You may select to add a new node/sibling or child in an existing document. Select the document, node location, and selected Sibling or Child |
| --- | --- |
| New key/Index | The YAML document selected may contain multiple documents, e.g., Document 0, Document 1, etc., and include information displayed as Key/index and value. The index/key indicates the position of the new node within the existing node hierarchy. |
| Value | Enter a value for the new node key/index. |
| Finish | Click finish and the yamlAdd command is inserted in the test case step. |
| Cancel | Click Cancel to discard your changes and exit Wizard. |

Important Once you have competed including all the information as required on the wizard, only one YAML command will be inserted into the test case. See YAML Steps in Test Case.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/yaml_query.png) <!-- image_chunk: img_034b6d480ce0a8c3 -->

![screenshot](topics/images/yaml_add_next.png) <!-- image_chunk: img_9f2913140195ebf2 -->
