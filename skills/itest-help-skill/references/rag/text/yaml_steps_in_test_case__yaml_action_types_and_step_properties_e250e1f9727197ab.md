---
{
  "chunk_id": "yaml_steps_in_test_case__yaml_action_types_and_step_properties_e250e1f9727197ab",
  "source_file": "topics/yaml_steps_in_test_case.htm",
  "source_original_path": "topics/yaml_steps_in_test_case.htm",
  "toc_path": [
    "iTest Online Help",
    "YAML Step Editor",
    "YAML Steps in Test Case"
  ],
  "heading_path": [
    "YAML Steps in Test Case",
    "YAML Steps in Test Case",
    "YAML Action Types and step properties"
  ],
  "anchor": "1349831",
  "context_ids": [
    "yaml_steps_in_test_case"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "yaml_step_wizard.htm#1368901"
  ],
  "images": [],
  "content_hash": "e250e1f9727197ab",
  "level": 2
}
---

# YAML Steps in Test Case > YAML Steps in Test Case > YAML Action Types and step properties

iTest supports five action types for the YAML step.

| YAML Action | Step Properties | Example |
| --- | --- | --- |
| yamlCreate | Go to Step Properties > EXEC yamlCreate Properties > YAMLCreate Step Properties to view the document contents or the document URI. Document Name: Name of the YAML document Global Scope: Indicates whether selected or not. See Global scope. File URL: When an existing document is selected, indicate the location of the file. Not applicable when content is pasted. Content: Displays the content of the YAML documented. Not available when a file URL is specified. | Creates new YAML document from file URI or YAML text. Reading from file: -documentName test_doc -globalScope false -fileURI project://yaml.zip_expanded/yaml_doc.txt Paste content: -documentName test_yaml -globalScope true -fileURI "" |
|  | Reading from file: |  |
|  | Paste content: -documentName test_yaml -globalScope true -fileURI "" |  |
| yamlGet | Go to Step Properties > EXEC yamlGet Properties > YAMLGet Step Properties to view the document name. Go to Step Properties > EXEC yamlGet Properties > YAMLGet Step Properties > Location to view the document index, node path and Key/index content value. |  |
|  | Go to Step Properties > EXEC yamlGet Properties > YAMLGet Step Properties to view the document name. |  |
|  | Go to Step Properties > EXEC yamlGet Properties > YAMLGet Step Properties > Location to view the document index, node path and Key/index content value. |  |
| yamlSet | Go to Step Properties > EXEC yamlSet Properties > YAMLSet Step Properties to view the document name and the value set. Go to Step Properties > EXEC yamlSet Properties > YAMLSet Step Properties > Location to view the document index, node path and Key/index content value. |  |
|  | Go to Step Properties > EXEC yamlSet Properties > YAMLSet Step Properties to view the document name and the value set. |  |
|  | Go to Step Properties > EXEC yamlSet Properties > YAMLSet Step Properties > Location to view the document index, node path and Key/index content value. |  |
| yamlDelete | Go to Step Properties > EXEC yamlDelete Properties > YAMLDelete Step Properties to view the document name. Go to Step Properties > EXEC yamlDelete Properties > YAMLDelete Step Properties > Location to view the document index, node path and Key/index content value. |  |
|  | Go to Step Properties > EXEC yamlDelete Properties > YAMLDelete Step Properties to view the document name. |  |
|  | Go to Step Properties > EXEC yamlDelete Properties > YAMLDelete Step Properties > Location to view the document index, node path and Key/index content value. |  |
| yamlAdd | Go to Step Properties > EXEC yamlAdd Properties > YAMLAdd Step Properties to view the document name and the value added. Go to Step Properties > EXEC yamlAdd Properties > YAMLAdd Step Properties > Location to view the document index, node path and Key/index content value. |  |
|  | Go to Step Properties > EXEC yamlAdd Properties > YAMLAdd Step Properties to view the document name and the value added. |  |
|  | Go to Step Properties > EXEC yamlAdd Properties > YAMLAdd Step Properties > Location to view the document index, node path and Key/index content value. |  |
