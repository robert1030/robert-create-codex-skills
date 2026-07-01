---
{
  "chunk_id": "command_tbml__query_subcommand_return_xpath_query_resu_5b64207f5071ad77",
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
    "query subcommand: Return XPath query result"
  ],
  "anchor": "1333359",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "5b64207f5071ad77",
  "level": 3
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > query subcommand: Return XPath query result

When evaluating a tbml query command, the XPath version is taken from the Topology file (and not from Test Case). TBML file’s property is used to determine the XPath version used to evaluate the tbml command.

| tbml XPath query | Returns valid XPath query. |
| --- | --- |
| tbml query XPath tbml("query", "XPath") | Returns the value returned by the specified valid XPath query. Example tbml query //tbml/body/resources/resource/@id] tbml("query", "//tbml/body/resources/resource/@id") returns IDs for all top-level devices tbml query //tbml/body/resources/resource\[@id="resource_0"\]/property\[@name="ipAddressV4"\] returns the ipAddressV4 property value on a resource with ID resource_0. Note You must use the backslash character to escape square brackets in the XPath expression. |
| Note | You must use the backslash character to escape square brackets in the XPath expression. |
