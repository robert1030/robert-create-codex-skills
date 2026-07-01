---
{
  "chunk_id": "yaml_step_wizard__query_a_yaml_document_2fa8e18a1f213296",
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
    "Query a YAML document"
  ],
  "anchor": "1333188",
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
    "topics/images/yaml_query-next.png"
  ],
  "content_hash": "2fa8e18a1f213296",
  "level": 2
}
---

# Insert YAML Step Wizard > Insert YAML Step Wizard > Query a YAML document

Allows you to get/query a YAML node. The Query option allows you to select a node value from an existing YAML document which will be returned in the Response View after execution. Select the option Query a YAML document and click Next to display the dialog: Select a YAML Document - Selection of document to edit or query.

| Document Name | Document name is a variable used during test execution to reference a yaml document. You can set document name manually or select document created in previous steps, or edit current procedure's response. The document name is automatically populated when you select an existing document in Created in yamlCreate step. |
| --- | --- |
| Global scope | See Global scope |
| Edit this procedure’s YAML response | Select this option and if the procedure has a YAML response, the content displays in the Sample section. You may insert alternate YAML text and perform required operation on the document. |
| Created in createYAML step | Select option to edit an existing YAML document. The wizard displays a list of YAML document(s) created in yamlCreate, Select a document and the content displays in the Sample section. |
| Sample | If you select an existing YAML response or document created using yamlCreate, then the wizard displays the document contents. You may edit the content as required. You may also paste content you require to be in execution. For example if you manually set document name you'll have to manually paste the sample as well. |
| Next | Click Next to display the Query YAML dialog to select a node location. |

The Query YAML dialog displays the selected YAML document in the editor (in expand/collapse structure).

| Query a YAML document: Select node location |
| --- |

| Select a node location in YAML document | The YAML document selected may contain multiple documents, e.g., Document 0, Document 1, etc., and include information displayed as Key/index and value. Select the document and location as required for your query. |
| --- | --- |
| Finish | Click finish and the yamlGet command is inserted in the test case step. |
| Cancel | Click Cancel to discard your changes and exit Wizard. |

Important Once you have competed including all the information as required on the wizard, only one YAML command will be inserted into the test case. See YAML Steps in Test Case.

![screenshot](topics/images/yaml_query.png) <!-- image_chunk: img_034b6d480ce0a8c3 -->

![screenshot](topics/images/yaml_query-next.png) <!-- image_chunk: img_0aab64565b6cfc54 -->
