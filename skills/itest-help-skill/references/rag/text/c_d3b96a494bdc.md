# YAML Step Editor > Insert YAML Step Wizard > Delete a node from YAML document

Allows you to Delete a YAML node from the document. The Delete a node option allows you to select a node from an existing YAML document to be deleted.

- **Document Name**：Document name is a variable used during test execution to reference a yaml document. You can set document name manually or select document created in previous steps, or edit current procedure's response. The document name is automatically populated when you select an existing document in Created in yamlCreate step.
- **Global scope**：See Global scope
- **Edit this procedure’s YAML response**：Select this option and if the procedure has a YAML response, the content displays in the Sample section.
- **Created in createYAML step**：Select option to edit an existing YAML document. The wizard displays a list of YAML document(s) created in yamlCreate, Select a document and the content displays in the Sample section.
- **Sample**：If you select an existing YAML response or document created using yamlCreate, then the wizard displays the document contents. You may edit the content as required.
- **Next**：Click Next to display the Delete YAML dialog.

![](images/yaml_query.png) <!-- image_ref -->

The Delete YAML dialog displays the selected YAML document in the editor (in expand/collapse structure).

![](images/yaml_delete_next.png) <!-- image_ref -->

- **Select a node locate in YAML document**：The YAML document selected may contain multiple documents, e.g., Document 0, Document 1, etc., and include information displayed as Key/index and value. Select the document and the node location to be deleted.
- **Finish**：Click finish and the yamlDelete command is inserted in the test case step.
- **Cancel**：Click Cancel to discard your changes and exit Wizard.
