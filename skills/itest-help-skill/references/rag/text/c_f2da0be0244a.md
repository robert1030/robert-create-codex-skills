# JSON Editor > JSON Command in Test Case > JSON Action Types

iTest supports five action types for the JSON step.

Note To modify a JSON key, you may delete an existing key and insert a new key.

Note pathValue is a string of the path. Gets value of only one JSONnode.

Note pathValue is an array of key paths (no need JSON object syntax is required).

- **JSON Action**：Example
- **createJson**：Creates new JSON document from file URI or JSON string. json -action createJson -documentName myJsonDocument -fileURI ’project://my_project/jsonFiles/json.txt’ Creates from JSON String: json -action createJson -documentName myJsonDocument -jsonString {’name1’:’value1’}
- **setJson**：Defines parameter with ’original json’ string and ’newValue’. json -action setJsonValue -documentName myJsonDocument -pathValue {’true’:true, ’false’:false, ’nullValue’: null}
- **getJsonNode**：Get the value of a JSON node json -action getJsonNode -documentName myJsonDocument -pathValue {’object/c/[1]’}
- **deleteJsonNode**：Deletes an existing JSON json -action deleteJsonNode -documentName myJsonDocument -pathValue {’key1/[0]’, ’array/[4]/[1]’, ’myKey1’, ’myKey2’}
- **addJsonNode**：Add new node into a JSON document json -action addJsonNode -documentName myJsonDocument -pathValue {’/’:{’newNode1’:’newValue1’, ’newNode2’:{’n2’:’V2’}}}
