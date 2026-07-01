---
{
  "chunk_id": "yaml_step_wizard__replace_a_node_in_yaml_document_c692d56c4f1b23a2",
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
    "Replace a node in YAML document"
  ],
  "anchor": "1368554",
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
    "topics/images/yaml_replace_next.png"
  ],
  "content_hash": "c692d56c4f1b23a2",
  "level": 2
}
---

# Insert YAML Step Wizard > Insert YAML Step Wizard > Replace a node in YAML document

Allows to you set/replace a value in a YAML node. The Replace a node option allows you to select a node from an existing YAML document to replace the node contents and value.

| Document Name | Document name is a variable used during test execution to reference a yaml document. You can set document name manually or select document created in previous steps, or edit current procedure's response. The document name is automatically populated when you select an existing document in Created in yamlCreate step. |
| --- | --- |
| Global scope | See Global scope |
| Edit this procedure’s YAML response | Select this option and if the procedure has a YAML response, the content displays in the Sample section. |
| Created in createYAML step | Select option to edit an existing YAML document. The wizard displays a list of YAML document(s) created in yamlCreate, Select a document and the content displays in the Sample section. |
| Sample | If you select an existing YAML response or document created using yamlCreate, then the wizard displays the document contents. You may edit the content as required. |
| Next | Click Next to display the Replace YAML Node dialog. |

The Replace YAML node dialog displays the selected YAML document in the editor (in expand/collapse structure).

| Value | The YAML document selected may contain multiple documents, e.g., Document 0, Document 1, etc., and include information displayed as Key/index and value. Select the document, node location and enter a new YAML node value. |
| --- | --- |
| Finish | Click finish and the yamlSet command is inserted in the test case step. |
| Cancel | Click Cancel to discard your changes and exit Wizard. |

![screenshot](topics/images/yaml_query.png) <!-- image_chunk: img_034b6d480ce0a8c3 -->

![screenshot](topics/images/yaml_replace_next.png) <!-- image_chunk: img_0bdb70ae6c1e0c54 -->
