---
{
  "chunk_id": "response_map_secret_type__incompatibilities_between_xpath_1_0_and__40849f6ab15d6630",
  "source_file": "topics/response_map_secret_type.htm",
  "source_original_path": "topics/response_map_secret_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Queries page"
  ],
  "heading_path": [
    "Response Map editor: Queries page",
    "Response Map editor: Queries page",
    "Creating a custom query",
    "XPath 3.1 syntax for custom queries format",
    "Incompatibilities between XPath 1.0 and XPath 3.1 expressions"
  ],
  "anchor": "1761046",
  "context_ids": [
    "response_map_secret_type",
    "rme_queries_page"
  ],
  "index_keywords": [
    "Queries page",
    "Response Map editor",
    "custom definitions",
    "in response maps",
    "queries"
  ],
  "index_keyword_paths": [
    "Queries page > Response Map editor",
    "Response Map editor > Queries page",
    "queries > custom definitions",
    "queries > in response maps",
    "response maps > queries"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "40849f6ab15d6630",
  "level": 4
}
---

# Response Map editor: Queries page > Response Map editor: Queries page > Creating a custom query > XPath 3.1 syntax for custom queries format > Incompatibilities between XPath 1.0 and XPath 3.1 expressions

iTest uses a compatibility mode in XPath 3.1 engine to prevent inconsistency between XPath 1.0 and XPath 3.1 expressions. However, a few incompatibilities still exist:

A list of incompatibilities are listed in: https://www.w3.org/TR/xpath-31/#id-backwards-compatibility, section H.3.1 (Incompatibilities relative to XPath 1.0 > Incompatibilities when Compatibility Mode is true).

- min(), max(), and avg() are now declared under default function namespace, so that they can be used inside the expressions without namespace prefix. (Previously they were declared under custom math {http://www.fnfr.com/svt/mapping/math} namespace).

- names() function is declared under itest {http://spirent.com/itest} namespace.

- Queries produced as a result of response mapping operation are registered as XPath 3.1 functions under default fn namespace. They may be referenced directly using only function name, no namespace prefix is required.

- If the response mapping operation produces a query which has the same name and number of arguments as the existing system function defined in the default fn namespace, then a new query function is declared under itest {http://spirent.com/itest} namespace, and can be referenced using namespace prefix: itest:shadowing_function()

- XPath 3.1 does not support @xmlns attribute node but is supported in XPath 1.0.

If a node is located under default namespace, but has no namespace, it cannot be referenced by its name. The structure view was updated to generate correct query using name() function for both 1.0 and 3.1. For example:

<root xmlns="https://example.com/xml">

<child>childText</child>

</root>

The root element declares a default XML namespace using xmlns attribute. All descending elements under root will have this namespace.

To query child element using XPath 3.1 engine a selector with name() function should be used:

//*[name() = "root"]/*[name() = "child"]

(//root/name will not work)
