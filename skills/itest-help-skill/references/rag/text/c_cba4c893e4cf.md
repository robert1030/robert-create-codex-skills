# YAML Step Editor > YAML Steps in Test Case > YAML Action Types and step properties > 第2段

| 欄位1 | 欄位2 | 欄位3 |
| --- | --- | --- |
| YAML Action | Step Properties | Example |
| yamlCreate | Go to Step Properties > EXEC yamlCreate Properties > YAMLCreate Step Properties to view the document contents or the document URI. Document Name: Name of the YAML document Global Scope: Indicates whether selected or not. See Global scope. File URL: When an existing document is selected, indicate the location of the file. Not applicable when content is pasted. Content: Displays the content of the YAML documented. Not available when a file URL is specified. | Creates new YAML document from file URI or YAML text. -documentName test_doc -globalScope false -fileURI project://yaml.zip_expanded/yaml_doc.txt |
| yamlGet |  | Get the value of the selected YAML node from an existing YAML document. -documentName query -globalScope false -procedureResponse false |
| yamlSet |  | Defines node value to be replaced within an existing YAML document. -documentName test_yaml -globalScope true -procedureResponse false |
| yamlDelete |  | Deletes the selected YAML node from an existing YAML document. -documentName test_yaml -globalScope true -procedureResponse false |
| yamlAdd |  | Add new node into an existing YAML document -documentName yaml_test -globalScope true -procedureResponse false |
