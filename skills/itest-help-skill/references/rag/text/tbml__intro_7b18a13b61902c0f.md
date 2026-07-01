---
{
  "chunk_id": "tbml__intro_7b18a13b61902c0f",
  "source_file": "topics/popups/tbml.html",
  "source_original_path": "topics/popups/tbml.html",
  "toc_path": null,
  "heading_path": [
    "tbml.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_tbml.html"
  ],
  "images": [],
  "content_hash": "7b18a13b61902c0f",
  "level": 0
}
---

# tbml.html

tbml subcommand arg ?arg?

The tbml property command returns the specified property value for a device or connection.

The tbml deviceList command returns a list of device IDs for the specified parent.

The tbml query command returns the value returned by the XPath query

The tbml endpoint command eturns the two resource IDs of endpoint resources that are directly connected to the specified link. If the link is connected to a port inside a device, then the endpoints will be resource IDs of the ports, not of the device.

The tbml parentList command returns the list of parent IDs for a specified resource starting from the root to the immediate parent. For a root resource, parentList returns an empty list. parentList also supports a combination of ID, name path and displayName path to determine the starting resource, like the deviceList and property subcommands.

The tbml linkList command returns the list of IDs of all link objects that are a link for the specified resource or children of the specified resource. linkList also supports a combination of ID, name path, and displayName path to determine the starting resource (as do the deviceList and property subcommands). Returns an empty list if the specified resource or its children do not have any links to other resources.

The tbml sessionList command takes a resource (that you specify using its device ID) and returns the list of session names attached to the resource (from the session profiles and from the sessions defined in the topology).

See the online help for details on syntax, arguments, and return values.
