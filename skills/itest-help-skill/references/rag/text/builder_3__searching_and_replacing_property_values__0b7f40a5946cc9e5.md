---
{
  "chunk_id": "builder_3__searching_and_replacing_property_values__0b7f40a5946cc9e5",
  "source_file": "topics/builder.3.htm",
  "source_original_path": "topics/builder.3.htm",
  "toc_path": [
    "iTest Online Help",
    "The iTest Builder",
    "Searching and replacing property values in iTest files"
  ],
  "heading_path": [
    "Searching and replacing property values in iTest files",
    "Searching and replacing property values in iTest files"
  ],
  "anchor": "1169409",
  "context_ids": [],
  "index_keywords": [
    "property settings",
    "search  and replace"
  ],
  "index_keyword_paths": [
    "property settings > search  and replace",
    "replacing > property settings",
    "search  and replace > property settings"
  ],
  "related_links": [],
  "images": [
    "topics/images/itest_search_tab.png",
    "topics/images/builder.6.jpg"
  ],
  "content_hash": "0b7f40a5946cc9e5",
  "level": 1
}
---

# Searching and replacing property values in iTest files > Searching and replacing property values in iTest files

You can search for and (as needed) replace property settings across any type of iTest resource. For example, you can search/replace a hard-coded IP address setting with field replacement text that enables the IP address to be set at execution time — change the text 10.123.4.5 to [param routerIP]. You can update the following types of iTest resource:

- test case

- session profile

- response map

- topology

> **Note:** Note All searches are not sensitive to case (case-insensitive).



To Search and replace property values

1. On the iTest menu, click Search > Search. On the Search dialog box, click the iTest Search tab.

Search for

- To search for files of the type that you specify in the Search in section, leave the Search for field empty.

- To search for text in files, type the text search expression.

If you specify Match if as contains search string, then use any of the following wildcard characters:

* matches any set of characters, including the empty string

? matches any character

\ is the escape for a literal. To search for an asterisk, question mark, or backslash character, type a backslash before it to indicate that you are not using the character as a wildcard ("\*", "\?", or "\\")

Match if

Specify the type of search.

Search in

Select all of the resources (file types) to search through.

Scope

Specify the scope to search: the whole workspace, pre-defined working sets, previously selected resources, or projects enclosing the specified resources.

1. 2

1. Click a button to perform an action:

Customize

Click Customize to specify the types of files to search — iTest resources or all file types.

Replace

To replace the specified search text, click Replace. In the Replace Text Matches dialog box, specify the text to replace the search text with .

For global replacement, click OK. To select the instances of the text to replace, click Preview . By default, in the Replace Test Matches dialog box, all instances are selected for replacement . Uncheck instances that should not be replaced. Click OK to perform the replacements .

Search

Click Search to search for all instances of the text. The results of the search appear in the Search view. Double-click an instance to view the property setting in the appropriate editor.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/itest_search_tab.png) <!-- image_chunk: img_face6b86d2dff180 -->

![screenshot](topics/images/builder.6.jpg) <!-- image_chunk: img_7290c4b03594e901 -->
