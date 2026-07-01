---
{
  "chunk_id": "rme_block_properties__token_properties_7b5eaf3bfd61529e",
  "source_file": "topics/rme_block_properties.htm",
  "source_original_path": "topics/rme_block_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Block Map properties"
  ],
  "heading_path": [
    "Response Map editor: Block Map properties",
    "Response Map editor: Block Map properties",
    "Token properties"
  ],
  "anchor": "1107228",
  "context_ids": [
    "rme_block_properties"
  ],
  "index_keywords": [
    "Block Map properties",
    "Response Map editor",
    "block map"
  ],
  "index_keyword_paths": [
    "Block Map properties > Response Map editor",
    "Response Map editor > Block Map properties",
    "properties > block map"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "7b5eaf3bfd61529e",
  "level": 2
}
---

# Response Map editor: Block Map properties > Response Map editor: Block Map properties > Token properties

Values for tokens that are named will be returned and available for postprocessing. The Token properties specify how the token will appear in the response.

| Token name | Naming a token makes the field’s value available to be returned from any response. You can associate an analysis rules with a test case step to return the value of the named token and then make the appropriate comparisons (the value is not zero or is the same as another value, and so on). Naming a token is valuable in the case that the token’s value represents a Pass/Fail condition. For example, a step’s analysis rule can test whether the token named PortStatus (with allowed values up and down) can pass the test case if the value of PortStatus is up and fail the test case otherwise. Once you assign a name to a token, the token value is enclosed in a blue box in the Response view. In addition, once you generate a query for it (either manually or by having iTest auto-populate it) the token is listed by name (with its associated query) in the Queries view. |
| --- | --- |
| Wildcard | The token can represent any string (typically a fragment of a line) that you would like to parse as a single entity. This setting is useful when you want to allow for values that are not being parsed correctly by iTest’s built-in parsers. Wildcard tokens are restricted to one line, but can appear anywhere in the line. If a Wildcard token is encountered while mapping, it can map to zero or more tokens of any type in the same line from the actual response. You can use the Optional property on a Wildcard to indicate whether it needs to match to zero or more versus one or more. This token will match any number of contiguous tokens with any values on the line. iTest displays values for the following two items: Value: A string that contains a representative value that is displayed when showing the mapped response Parser: The name of the parser that identifies the token in the response string. For example, if the string “Thu 18-Sep-03 18:42” appears in a response, the Http Timestamp parser will identify the string as a timestamp. The parser associates a token with the identified timestamp value and uses the appropriate value representation to store its value. |
| Optional | This token may or may not be present in a line that matches Check Optional if it is acceptable for no value to appear for the token. This setting is useful for values that might or not appear in a response. |
| Variable | Check Variable if it is acceptable for a variety of values to appear for the token. The matching token can take other values that can be parsed with the same parser. This setting allows values like timers and statistics to vary without causing mapping failures. |
| Key | This token appears in a repeating block and should be used as a key when auto-generating token aliases When True, use the value of the token as the key to identify the instance of a repeating block in the response that contains the value that you want to return. For an example, see Configuring a Token as a Key (Index) to Other Tokens in the Response iTest generates a query for each combination of a key token and all other tokens in the response map. |
