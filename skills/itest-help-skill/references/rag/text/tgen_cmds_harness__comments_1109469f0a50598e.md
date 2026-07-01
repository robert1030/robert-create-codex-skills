---
{
  "chunk_id": "tgen_cmds_harness__comments_1109469f0a50598e",
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
    "av_create",
    "Comments"
  ],
  "anchor": "1305889",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "1109469f0a50598e",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_create > Comments

The av_create command creates one or more Avalanche Automation objects under the specified parent object. When you call the create function, you specify the type(s) of one or more objects to be created. You can specify:

- An object type name (such as the Project object or the Test object). For example:

- av_create project –under system1 -name Project1

- When you create an object, you must specify the handle of the parent object under which the new object is to be created.

- When you create an object, you can also set the object attributes at the same time. To set attributes, specify one or more attribute name/value pairs.

- If you specify attribute name/value pairs, together with an object type path, Avalanche Automation applies the attribute values to the object associated with the last name specified in the object type path. In the following example, Avalanche Automation creates a Project object. When Avalanche Automation creates the Project object, it sets the name attribute to Project1 and the path attribute to C:\Project\Project1.

av_create project –under system1 -name Project1 -path “C:\Projects\Project1”

- You can specify a Descendant Attribute Notation (DAN) path as part of the attribute reference. Avalanche Automation uses the specified object type to create the primary object, and the DAN path to create any additional objects. For information about path name specification, see section “Object, Attribute, and Relation References” in Avalanche™ Automation Programmers’ Reference guide.
