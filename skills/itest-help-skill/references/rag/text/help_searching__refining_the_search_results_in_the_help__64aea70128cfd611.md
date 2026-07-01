---
{
  "chunk_id": "help_searching__refining_the_search_results_in_the_help__64aea70128cfd611",
  "source_file": "topics/help_searching.htm",
  "source_original_path": "topics/help_searching.htm",
  "toc_path": [
    "iTest Online Help",
    "Using iTest Help",
    "Searching help"
  ],
  "heading_path": [
    "Searching help",
    "Searching help",
    "Refining the search results in the help view"
  ],
  "anchor": "1164425",
  "context_ids": [
    "help_searching"
  ],
  "index_keywords": [
    "help",
    "searching"
  ],
  "index_keyword_paths": [
    "help > searching",
    "searching > help"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "64aea70128cfd611",
  "level": 2
}
---

# Searching help > Searching help > Refining the search results in the help view

If the search yields too many results, the information you are looking for may not appear in the top 10 or 15 results. You can then refine the search to reduce the number of results.

To refine a search:

1. Click the Search Scope link. to expand search scope section

1. 2

1. Click the Advanced Settings link. The Search Scope preference dialog will open

1. 3

1. Select Local Help from the list

1. 4

1. Click Search only the following topics to narrow down the search scope

1. 5

1. In the working set content tree, select the topics to which you want to narrow the search

1. 6

1. Click OK to activate the changes and return to search page in the Help view

1. 7

1. Click Go again. The new list of results will appear

Follow the following search expression rules for searching local help content:

- Unless otherwise stated, there is an implied AND between all search terms. In other words, topics that contain all the search terms will be returned. For example:

- Java project

- returns topics that contain the word Java and the word project, but does not return topics that contain only one of these words.

- Use OR before optional terms . For example:

- applet OR application

- returns topics that contain the word applet or the word application (or both).

- Use NOT before terms you want to exclude from search results. For example:

servlet NOT ejb

returns topics that contain the word servlet and do not contain the word ejb.

> **Note:** Note NOT works only as a binary operator (for example, “NOT servlet” is not a valid expression).

- Use ? for a single-character wildcard and * for a multi-character wildcard. For example:

par?

returns topics that contain part or park, but not participate. On the other hand:

par*

returns topics that contain part, park, participate, pardon, and so on. Note: The search engine does not accept terms with a wild card at first character position.

- Use double quotation marks around terms you want treated as a phrase. For example:

"creating projects"

returns topics that contain the entire phrase creating projects, and not creating or project on its own.

- Punctuation acts as term delimiters. For example:

plugin.xml

returns hits on topics that contain plugin.xml, plugin, and xml, which is likely broader than you want. If you want to find just those topics containing plugin.xml, use double quotes, as in:

"plugin.xml"

- The search engine ignores character case. For example:

Workbench

returns topics that contain 'workbench', 'Workbench', 'WorkBench', and 'WORKBENCH'.

- The following stop words are common English words which will be ignored (not searched for) if they appear in the search expression: a, and, are, as, at, be, but, by, in, into, is, it, no, not, of, on, or, s, such, t, that, the, their, then, there, these, they, to, was, will, with.

- The search engine does “fuzzy” searches and word stemming. If you enter create, it will return hits on topics that contain creates, creating, creator, and so on. To prevent search engine from stemming terms, enclose them in double quotes.
