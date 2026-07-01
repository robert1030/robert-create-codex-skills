---
{
  "chunk_id": "tgen_cmds_harness__comments_53c9ac7d7b121d4d",
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
    "av_get",
    "Comments"
  ],
  "anchor": "1306023",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "53c9ac7d7b121d4d",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_get > Comments

The av_get command returns the value of one or more object attributes, or, in the case of relation references, one or more object handles.

- The handle identifies the object from which data will be retrieved. If you do not specify any attributes, Avalanche Automation returns the values for all attributes and all relations defined for the object.

- The attributeName identifies an attribute for the specified object.

- The DANPath (Descendant Attribute Notation path) is a dotted path name beginning with a sequence of one or more relation names, and ending with an attribute name. A relation name may have an index suffix (an integer in parenthesis) to reference one of multiple children of the same type. Avalanche Automation combines the handle (or the DDNPath) with the DANPath to resolve the attribute reference. The path must identify a valid sequence of objects in the test hierarchy. For example:

av_get $project test(1).name

- Avalanche Automation combines the object and attribute specifications to retrieve the value of the attribute for the first Test object child of the $project.

- The DDNPath (Direct Descendant Notation path) is a dotted path name sequence. The sequence begins with an object handle, followed by one or more relation names. The path must identify a valid sequence of objects in the data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. For example:

av_get $project1.test -name

- In this case, Avalanche Automation returns the value of the name attribute for the first Test child of the specified Project object.

- If there is more than one instance of a particular object type, as children of the specified object, use an index notation. (In the example above, the index value 1 is implied.) Avalanche Automation assigns index values in the order of object creation. For example:

av_get $project.test(2)

- Avalanche Automation returns the attributes and all relations for the second Test object child of the specified Project object.

- When you use a relation reference with the get function, it provides access to one or more objects connected to the object identified by a handle (or DDNPath). Specify a name for the relation reference, using relationName. For example:

av_get $hProject -Tests

- This function call returns the handle(s) for the Test child object(s) of the Project object.
