---
{
  "chunk_id": "tgen_cmds_harness__comments_a87a4ac53881517e",
  "source_file": "topics/tgen_cmds_harness.htm",
  "source_original_path": "topics/tgen_cmds_harness.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Avalanche API Commands"
  ],
  "heading_path": [
    "Avalanche API Commands",
    "Avalanche API Commands",
    "av_config",
    "Comments"
  ],
  "anchor": "1305761",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a87a4ac53881517e",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_config > Comments

The av_config command modifies the value of one or more object attributes, if it meets the validation rules. Note: If you attempt to modify an attribute for a read-only object, or a specified value does not meet the validation rules, the av_config command raises an exception.

- When you modify object attributes, use attrName/value pairs. For example:

av_config project1 -name Project1

- You can use Direct Descendant Notation (DDN) to identify the object and Descendant Attribute Notation (DAN) to identify the attribute. For example:

av_config $project.test -name Test1

av_config $project -userprofile.name SSLv3

A DAN path is a dotted path name beginning with a sequence of one or more object types, and ending with an attribute name. Avalanche Automation combines the handle (or the DDNPath) with the DANPath to resolve the attribute reference. The path must identify a valid sequence of objects in the Avalanche Automation data model hierarchy.

In both DDN and DAN paths, an object type name may have an index suffix (an integer in parentheses) to reference one of multiple children of the same type.

For more information about these notations, see section “Referencing Objects: Object Paths” Avalanche Automation Programmers’ Reference guide.
