---
{
  "chunk_id": "tc_template_validation__response_structure_elements_comparison_a_9eabb7d63731e027",
  "source_file": "topics/tc_template_validation.htm",
  "source_original_path": "topics/tc_template_validation.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Library Template",
    "Validation of testcase against the associated template"
  ],
  "heading_path": [
    "Validation of testcase against the associated template",
    "Validation of testcase against the associated template",
    "Response structure elements comparison and validation"
  ],
  "anchor": "1946467",
  "context_ids": [
    "tc_template_validation"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tc_template.htm#1927468"
  ],
  "images": [],
  "content_hash": "9eabb7d63731e027",
  "level": 4
}
---

# Validation of testcase against the associated template > Validation of testcase against the associated template > Response structure elements comparison and validation

The elements can be queried from the response structure of both the template and testcase that links to the template (Implementation). The following lists how the values are compared and validated:

|  | Primitive value in template | Array in template | Map in template |
| --- | --- | --- | --- |
| Primitive value in “Implementation” | No validation error is produced. Values equality is not checked. | If array is empty no validation error is produced. Template: {devices: []} Implementation: {devices: null} - OK Otherwise, No validation error is displayed because it is not possible to query elements containing in the template array from the implementation response | If map is empty, no validation error is produced: Template: {props: {}} Implementation: {props: null} - OK Otherwise, because it is not possible to query elements containing in the template map from the implementation response Template: {props: {id: "", name: ""}} Implementation: {props: null} - Error |
| Map in “Implementation” | No validation error is displayed You are allowed to define more complex structures in the implementation Template: {devices: null} Implementation: {devices: {template: PC}} - OK | If array is empty, no validation error is produced. Template: {devices: []} Implementation: {devices: {template: PC}} - OK Otherwise, No validation error is displayed because it is not possible to query elements containing in the template array from the implementation response Template: {devices: ["PC", "SWITCH"]} Implementation: {devices: {template: PC}} - Error | No validation error is displayed if map in implementation misses keys defined in map in template: Template: {key1: value1, key2: value2} Implementation: {key1: value1} - Error because key2 is missing It is not forbidden for map in implementation to define more keys than the map in template: Template: {key1: value1} Implementation: {key1: value1, key2: value2} - OK Elements of maps with matching keys are compared individually using criteria defined in this table: Template: {key1: value1, key2: value2} Implementation: {key1: new_value1, key2: new_value2} - OK because different values are allowed |
| Array in “Implementation” | No validation error is displayed. You are allowed to define more complex structures in the implementation Template: {devices: null} Implementation: {devices: ["PC", "SWITCH"]} - OK | Validation error is displayed if array in implementation has less size than keys defined in array in template: Template: [a, b, c] Implementation: [a, b] - Error It is not forbidden for array in implementation to have more elements than the array in template: Template: [a, b] Implementation: [a, b, c] - OK Elements of arrays with matching indexes are compared individually using criteria defined in this table: Template: [a, b] Implementation: [a1, b1] - OK because different values are allowed | If map is empty, no validation error is produced: Template: {devices: {}} Implementation: {devices: ["PC1, "PC2"]} - OK Otherwise, No validation error is displayedbecause it is not possible to query elements containing in the template map from the implementation response Template: {devices: {template: PC}} Implementation: {devices: ["PC", "SWITCH"]} - Error |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
