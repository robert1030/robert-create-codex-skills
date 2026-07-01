---
{
  "chunk_id": "yaml_step_wizard__delete_a_node_from_yaml_document_c70231ea0ece1cc2",
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
    "Delete a node from YAML document"
  ],
  "anchor": "1326605",
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
    "#1368901"
  ],
  "images": [
    "topics/images/yaml_query.png",
    "topics/images/yaml_delete_next.png"
  ],
  "content_hash": "c70231ea0ece1cc2",
  "level": 2
}
---

# Insert YAML Step Wizard > Insert YAML Step Wizard > Delete a node from YAML document

Allows you to Delete a YAML node from the document. The Delete a node option allows you to select a node from an existing YAML document to be deleted.

| Document Name | Document name is a variable used during test execution to reference a yaml document. You can set document name manually or select document created in previous steps, or edit current procedure's response. The document name is automatically populated when you select an existing document in Created in yamlCreate step. |
| --- | --- |
| Global scope | See Global scope |
| Edit this procedure’s YAML response | Select this option and if the procedure has a YAML response, the content displays in the Sample section. |
| Created in createYAML step | Select option to edit an existing YAML document. The wizard displays a list of YAML document(s) created in yamlCreate, Select a document and the content displays in the Sample section. |
| Sample | If you select an existing YAML response or document created using yamlCreate, then the wizard displays the document contents. You may edit the content as required. |
| Next | Click Next to display the Delete YAML dialog. |

The Delete YAML dialog displays the selected YAML document in the editor (in expand/collapse structure).

| Select a node locate in YAML document | The YAML document selected may contain multiple documents, e.g., Document 0, Document 1, etc., and include information displayed as Key/index and value. Select the document and the node location to be deleted. |
| --- | --- |
| Finish | Click finish and the yamlDelete command is inserted in the test case step. |
| Cancel | Click Cancel to discard your changes and exit Wizard. |

![screenshot](topics/images/yaml_query.png) <!-- image_chunk: img_034b6d480ce0a8c3 -->

![screenshot](topics/images/yaml_delete_next.png) <!-- image_chunk: img_ff21b410dfc814bb -->
