---
{
  "chunk_id": "command_tbml__parentlist_subcommand_return_list_of_par_202ecc9763b0d325",
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
    "parentList subcommand: Return list of parent IDs for a resource"
  ],
  "anchor": "1335838",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1332363",
    "#1305493"
  ],
  "images": [],
  "content_hash": "202ecc9763b0d325",
  "level": 3
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > parentList subcommand: Return list of parent IDs for a resource

The parentList subcommand returns the list of parent IDs for a specified resource.

Parents are listed starting from the root and continuing down the chain to the immediate parent. For a root resource, parentList returns an empty list.

parentList supports a combination of ID, name path, and displayName path to determine the starting resource, (as described for the property subcommand in property subcommand: Return value of a property).

See tbml command syntax
