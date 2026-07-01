---
{
  "chunk_id": "command_tbml__property_subcommand_return_value_of_a_pr_4902c35000c03715",
  "source_file": "topics/command_tbml.htm",
  "source_original_path": "topics/command_tbml.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "\"tbml\" topology commands",
    "Commands that return information about topologies"
  ],
  "heading_path": [
    "Commands that return information about topologies",
    "Commands that return information about topologies",
    "Example topology",
    "property subcommand: Return value of a property"
  ],
  "anchor": "1332363",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1305493"
  ],
  "images": [],
  "content_hash": "4902c35000c03715",
  "level": 3
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > property subcommand: Return value of a property

The tbml property command returns the value of a property on a resource or on a link.

- The property subcommand can return multiple values if multiple properties match.

- Because the property subcommand applies to both resources and link elements, the resource element takes precedence over link elements. If a property is not found in a resource element, then the link element is searched.

- To identify a property, use its id or name or displayName or a combination of id and one of name or displayName.

See tbml command syntax

> **Note:** TBML usage syntax

When using tbml commands, any strings that include spaces need to be surrounded with curly braces.

The following examples show the correct and incorrect usage:

| Correct syntax | tbml property -id $deviceId {{System Identification} ipAddress} OR the following in Python tbml('property', '-id' , 'deviceId', '{System Identification}ipAddress') |
| --- | --- |
| Incorrect syntax | tbml property -id $deviceId {"System Identification" ipAddress} OR [tbml property -id $deviceId "System Identification" ipAddress] or tbml('property', '-id' , 'deviceId', ipAddress) Error: Unable to substitute " Device IP: tbml property -id $deviceId {"System Identification" ipAddress}": Cannot find property: com.fnfr.svt.iTestInterpreter.model.SubstString@e19679/ipAddress |
