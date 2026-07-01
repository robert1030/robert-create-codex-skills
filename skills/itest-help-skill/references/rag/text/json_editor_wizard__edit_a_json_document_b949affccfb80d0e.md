---
{
  "chunk_id": "json_editor_wizard__edit_a_json_document_b949affccfb80d0e",
  "source_file": "topics/json_editor_wizard.htm",
  "source_original_path": "topics/json_editor_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "JSON Editor",
    "JSON Editor Wizard"
  ],
  "heading_path": [
    "JSON Editor Wizard",
    "JSON Editor Wizard",
    "Edit a JSON document"
  ],
  "anchor": "1333188",
  "context_ids": [
    "json_editor_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1330217",
    "json_command_in_test_case.htm#1327517"
  ],
  "images": [
    "topics/images/json_02_wizard_edit_jason_doc.png",
    "topics/images/json_wizard_edit_01.png",
    "topics/images/json_wizard_edit_02.png"
  ],
  "content_hash": "b949affccfb80d0e",
  "level": 2
}
---

# JSON Editor Wizard > JSON Editor Wizard > Edit a JSON document

The Edit Allows you to edit an existing JSON document. Select option and click Next. The wizard displays a list of JSON document(s) created in the step above (createJson), and allows you to reference a custom variable via the Variable text box.

- If you select a JSON document created using createJson, then the wizard will display its initial contents (the document as it existed at creation time) in the editor (both in pretty print and expand/collapse structure). See JSON Editor Buttons.

When path is empty on Edit, the message displayed depends on the mode selected. For example:

- Select a location in the document and SET a new value

- Select a location in the document to GET the value of a JSON node

- Select a location in the document and click ADD

- Select a location in the document and click DELETE

- If you enter a custom variable, the wizard will display empty text and structure. You may paste raw text on the left pane, the editor will render the JSON structure on the right pane, and then allow one operation (read/write) on the JSON document. See JSON Editor Buttons.

Irrespective of whether you entered a custom variable or selected a document created by createJson, the JSON Editor Wizard allows you to insert alternate JSON in the text pane and perform one of these operations on the document: getJsonNode, setJsonValue, deleteJsonNode, or addJsonNode.

> **Note:** Note If you insert custom (your required) JSON text on the text area, the JSON command will be generated with the structure of this text.

> **Note:** Note The resulting json command will appear in a preview area of the wizard. Click Reset to clear any change you made and put the wizard back to the when the editor opened (allowing you to perform a different operation on the JSON document).

Important Once you have competed including all the information as required on the wizard, only one JSON command will be inserted into the test case. See JSON Command in Test Case.

![screenshot](topics/images/json_02_wizard_edit_jason_doc.png) <!-- image_chunk: img_09d1cf4261258339 -->

![screenshot](topics/images/json_wizard_edit_01.png) <!-- image_chunk: img_f3daec35823d834b -->

![screenshot](topics/images/json_wizard_edit_02.png) <!-- image_chunk: img_2766e219d28dc35c -->
