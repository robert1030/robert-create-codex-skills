---
{
  "chunk_id": "queries_view__example_how_an_xpath_query_works_946f104b41f6d0e6",
  "source_file": "topics/queries_view.htm",
  "source_original_path": "topics/queries_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Queries view"
  ],
  "heading_path": [
    "Queries view",
    "Queries view",
    "Example: How an XPath query works"
  ],
  "anchor": "1170326",
  "context_ids": [
    "queries_view"
  ],
  "index_keywords": [
    "Queries view"
  ],
  "index_keyword_paths": [
    "Queries view",
    "views > Queries view"
  ],
  "related_links": [],
  "images": [
    "topics/images/views_5.2.jpg"
  ],
  "content_hash": "946f104b41f6d0e6",
  "level": 2
}
---

# Queries view > Queries view > Example: How an XPath query works

A portion of the response to the show version command might be:

Image text-base: 0x00003000, data-base: 0x00C7FC04

We have defined a Regex map with two named two tokens Image_text_base and data_base. The Queries view displays each of the named regex groups as a query that can extract a value from a response.

Here is a portion of the XML of the response map that abstracts the two hex value tokens:

<mapped>

<Block id="com.fnfr.svt.mapping.block"/>

<Regex id="com.fnfr.svt.mapping.regex">

<Body>

<regex1 map:endcol="50" map:line="5" map:startcol="0">

<Image_text_base map:endcol="27" map:line="5" map:nodetype="token" map:startcol="17">0x00003000</Image_text_base>

<data_base map:endcol="50" map:line="5" map:nodetype="token" map:startcol="40">0x00C7FC04</data_base>

</regex1>

</Body>

</Regex>

<Tabular id="com.fnfr.svt.mapping.table"/>

</mapped>

The XPath query used to reference the data_base token is:

//data_base

The query returns everything contained between the <data_base> and </data_base> tags (in the sample response, the value 0x00C7FC04).

> **Note:** Note You cannot extract value of a hierarchical data structure in original response syntax. You can to get joined data of that structure. For exampe, if you have the following python response:

{

"key": [1, 2 ,3]

}

Then you can get the value of list by the following:

XPath: mapped/Python/item/item[1]/item.

> **Note:** But value will be “123” and not [1, 2, 3].

![screenshot](topics/images/views_5.2.jpg) <!-- image_chunk: img_310939f4965fcfd6 -->
