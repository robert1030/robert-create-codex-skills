---
{
  "chunk_id": "command_tbml__specifying_arguments_acbfba6e91887506",
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
    "tbml command syntax",
    "Specifying arguments"
  ],
  "anchor": "1436097",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "acbfba6e91887506",
  "level": 3
}
---

# Commands that return information about topologies > Commands that return information about topologies > tbml command syntax > Specifying arguments

- In the command descriptions, “resource” means a device or any item in a nested device/subdevices/cards/ports structure.

- For many commands, to make it easy to specify a resource or link, you can specify it by its id, by its name, or by its displayName.

- When specifying a resource path as an argument, the parent is listed first, followed by the child. For example, “myRouter card1”

- Segments in a resource path are delimited (that is, a resource is separated from its child) using the space character. If there is more than one segment in the path, then you must surround the path with double quotes. For example, to refer to port1 on card1 on myRouter, use “myRouter card1 port1”

- If a resource name includes a space character, then pass the arguments as a list. For example:

| Tcl example | Python example |
| --- | --- |
| Pass a resource named blue Router as [list “blue Router”] | Pass a resource named blue Router as resource_name = 'blue Router' |
| Pass a resource named card1 on blue Router as [list “blue Router” card1] | Pass a resource named card1 on blue Router as resource_name + = 'card1' |
