---
{
  "chunk_id": "return_value_dialog__words_and_characters_supported_in_json_r_bfc8f75131003559",
  "source_file": "topics/return_value_dialog.htm",
  "source_original_path": "topics/return_value_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Defining a procedure"
  ],
  "heading_path": [
    "Defining a procedure",
    "Defining a procedure",
    "Adding a procedure definition manually and modifying procedure properties (like arguments)",
    "Words and characters supported in JSON response"
  ],
  "anchor": "1535699",
  "context_ids": [
    "procedures_defining",
    "return_value_dialog"
  ],
  "index_keywords": [
    "defining",
    "enable json response",
    "procedure properties",
    "procedures"
  ],
  "index_keyword_paths": [
    "defining > procedures",
    "enable json response",
    "procedure > procedure properties",
    "procedures > defining"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "bfc8f75131003559",
  "level": 3
}
---

# Defining a procedure > Defining a procedure > Adding a procedure definition manually and modifying procedure properties (like arguments) > Words and characters supported in JSON response

The following lists the JOSN naming convention, special words, and characters supported a procedures' JSON response.

iTest supports the following JSON naming convention

- alphanumeric characters: a-z, A-Z

- numeric characters: 0 - 9

- The first character as a letter or an underscore "_"

- The characters that can be used to name an entity: "_" or "-"

- The name that is not any of the iTest reserved words: "any", "body", "empty", "expression", "mapgroup", "map", "parameter", "regex", "response", "tcl", "this", "token".

iTest will automatically convert any name that do not follow the JSON naming convention as follows.

- Replaces Blanks/spaces character with underscores (_)

- Replaces special characters (e.g.: <>?~!@#$%^&*=+/.,';][) with underscores (_).

- Adds “x” in front of a reserved word, e.g., replaces any as xany, body as xbody, and so on.

- Truncates long names to the maximum allowed length of 100 characters.

iTest synchronizes data between the Sample data and response tree in order to ensure the data is the same.

| Special characters | iTest uses XML structure to save data, when you use an invalid XML character, it is parsed to replace invalid characters with an under score (_). Example 1: If JSON key includes special characters such as {"a@b": 123} in the Sample data, then iTest converts JSON tree as {"a_b": 123} and updates the Sample data to be the same: {"a_b": 123} Example 2: If JSON key includes special characters such as { "key1": "value1", "key2": "value", "abc$@#%^&*!": "value2" } in the Sample data, then iTest converts JSON tree as {"abc_______": value2} and updates the Sample data to be the same Note: Each special character is replaced with an underscore character. |
| --- | --- |
| Reserved words | iTest includes these reserved words when building response: "any", "body", "empty", "expression", "mapgroup", "map", "parameter", "regex", "response", "tcl", "this", and "token". iTest converts keys containing these reserved words by adding a prefix "x" to it and updates Sample data and JSON tree. For example: Sample data and JSON tree will be updated as {"xresponse": 123} |
