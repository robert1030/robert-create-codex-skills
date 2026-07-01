---
{
  "chunk_id": "rme_yaml_responses__mapping_yaml_response_d2aa125a67d230d1",
  "source_file": "topics/rme_yaml_responses.htm",
  "source_original_path": "topics/rme_yaml_responses.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Mapping YAML Response"
  ],
  "heading_path": [
    "Mapping YAML Response",
    "Mapping YAML Response"
  ],
  "anchor": "1750680",
  "context_ids": [
    "rme_yaml_responses"
  ],
  "index_keywords": [
    "YAML",
    "YAML, response mapping"
  ],
  "index_keyword_paths": [
    "YAML, response mapping",
    "response mapping > YAML"
  ],
  "related_links": [],
  "images": [
    "topics/images/rme_yaml_response_struct_query.png"
  ],
  "content_hash": "d2aa125a67d230d1",
  "level": 1
}
---

# Mapping YAML Response > Mapping YAML Response

iTest supports auto-mapper for YAML responses similar to JSON auto-mapper.

> **Note:** Note Response view provides YAML mapper option and automatically switches to the YAML mapper if the response was mapped as YAML.

iTest detects YAML syntax in a response and marks the response as YAML type compatible with YAML 1.1 (https://yaml.org/spec/1.1/).

YAML extracts the following YAML structures:

- Multiple documents: A document starts with three dashes (---) and ends with three periods.

- List: A list starts with a dash (-) or three dots (...)

- Arrays: Allows arrays or lists to be specified on a single line or on multiple lines.

---

items: [ 1, 2, 3, 4, 5 ]

names: [ "one", "two", "three", "four" ]

- Scalars and Block scalars: Scalars in YAML are basic values (like numbers or strings, as opposed to complex types like arrays or objects). Block scalars have more control over how they are interpreted, whereas flow scalars have more limited escaping support.

> **Note:** Note The type of a scalar is not identified or stored.

- Repeated nodes: Repeated nodes in each file denoted by an ampersand (&) and by an asterisk (*) mark.

> **Note:** Note YAML requires colons and commas used as list separators followed by space with scalar values.

Repeated nodes are expanded (replaced with their copied value. References are not stored).

- Response, Structure, and Queries View: iTest generates structured data that represents the hierarchical structure of YAML along with the name/value pairs of child nodes, under the “mapped/yaml”

Queries are auto-generated for all name/value pairs with the simple keys (not list/mapping keys) and with the values of scalar type, and all nested elements.

If the same node appears in multiple documents, parametrized query is generated with an argument that corresponds to the document number.

> **Note:** Note Some of single string (single scalar) responses even though valid YAML by definition, will not be auto-mapped as YAML, as this may break existing test cases that rely on auto-maps. Such responses will be auto-marked as YAML in the Response View and only if a YAML response map is applied to them.

> **Tip:** Tip YAML Response Mapping changes default queries and it is recommended that you modify the relevant analysis rules.

See Example YAML Response, Structure and Query views below.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/rme_yaml_response_struct_query.png) <!-- image_chunk: img_bff85c9bccefc68a -->
