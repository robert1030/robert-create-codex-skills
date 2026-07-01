---
{
  "chunk_id": "json_editor_wizard__create_a_json_document_e79a827436f9c31d",
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
    "Create a JSON document"
  ],
  "anchor": "1326540",
  "context_ids": [
    "json_editor_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "json_command_in_test_case.htm#1327517"
  ],
  "images": [
    "topics/images/json_wizard_create_01.png",
    "topics/images/jason_wizard_create_02.png"
  ],
  "content_hash": "e79a827436f9c31d",
  "level": 2
}
---

# JSON Editor Wizard > JSON Editor Wizard > Create a JSON document

Select the option Create a JSON document and click Next to create a new JSON document from an existing JSON document or create one manually from JSON string.

From file: Select to create a new JSON document from an existing project or file URI.

When creating a JSON document from file, if you choose a document that contains one or more JSON syntax errors, an error displays and you will not be able to click Next to view the document. The Next button is available only when a valid JSON file is chosen (when no syntax errors exist).

- Selected: When selected, the JSON editor displays the contents of the file (both in pretty print and expand/collapse structure).The file contents will be displayed in the JSON editor but no edits to the document will be allowed.

You will then be able to ’name’ your JSON document and the wizard will finish, adding one step to the test case, something like:

json -action -documentName myJsonDoc -fileURI -contents project://test/sample.json

- Not selected: (manually create JSON document from JSON string) The JSON editor will display empty text and structure, allowing you to paste text into the editor and make changes as required.

> **Note:** Note This options allows you to Create a JSON document, i.e., add, update, and delete json node.

You will then be able to name your JSON document and the wizard will finish, adds one step to the test case. For example:

json -action -documentName myJsonDoc -fromFile false -jsonString {’name1’:’value1’}).

> **Note:** Note If you insert custom (your required) JSON text on the text area and click the Import button, the JSON command will be generated with the structure of this text.

> **Note:** Note The resulting json command will appear in a preview area of the wizard. Click Reset to clear any change you made and put the wizard back to the when the editor opened (allowing you to perform a different operation on the JSON document).

Important Once you have competed including all the information as required on the wizard, only one JSON command will be inserted into the test case. See JSON Command in Test Case.

![screenshot](topics/images/json_wizard_create_01.png) <!-- image_chunk: img_2dfdff6eb54cc4ff -->

![screenshot](topics/images/jason_wizard_create_02.png) <!-- image_chunk: img_91bbc53f9d6de701 -->
