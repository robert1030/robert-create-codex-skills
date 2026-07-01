---
{
  "chunk_id": "queries_view__queries_view_cdd6d74d4efe106e",
  "source_file": "topics/queries_view.htm",
  "source_original_path": "topics/queries_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Queries view"
  ],
  "heading_path": [
    "Queries view",
    "Queries view"
  ],
  "anchor": "1170286",
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
    "topics/images/queries_structure_response_views.png"
  ],
  "content_hash": "cdd6d74d4efe106e",
  "level": 1
}
---

# Queries view > Queries view

When iTest searches a response for a value that a test case step has requested, it uses an XPath query to search for the specified value in an XML-format structured data representation of the response text. XPath is the foundation on which response mapping is built.

iTest auto-maps query that matches the entire line of text on a response so that you do not have to manually enter a regular expression in your analysis rule. This auto-mapping of the query that matches all the lines of text on a response, assists you with creating your test cases faster.

For JSON object response, iTest auto-maps queries of for keys at the root level of a JSON object response. No auto-mapped queries are created for nested keys of a JSON object response.

The Queries view lists the XPath queries and their results for the response that is displayed in the Response view. (Queries can be defined in a response map or in local analysis rules. In addition, iTest auto-generates queries for structured responses like Web, SNMP, traffic generator devices, and XML.)

When you select a test case step the associated Queries view, Response view and the Structures view displays..

> **Note:** Note The name that appears in the Query column is the friendly name for the token query; the actual XPath query appears in the XPath column. iTest auto-generates names for queries. You can modify the names and add custom aliases on the Queries page of the Response Map editor.

The responseLine() query applies the regex [^\r\n]+ to extract entire linesfrom response:

- For a multi-line response, the contents of responseLine() will be a list of lines

(xPath: .//responseLine/line).

- For a single-line response, the contents of responseLine() will be a response string

(xPath: .//responseLine).

The responseLine() query (unlike other auto-response mappings), does identify the value of this response within a grey box. For example, if the response of a command as shown below.

latency_us: 10

throughput_gbps: 40

Only the integers 10 and 40 would be enclosed in grey boxes, corresponding to the auto-mapped queries latency_us() and throughput_gbps().

In aditional, not all queries represent tokens in the response. iTest generates some other useful queries like RowCount for table maps.

> **Tip:** Tip To improve performance, iTest does not map all items in very long responses. If you notice that the “blue boxes” do not appear in the later text of a response, you can increase the setting so that iTest evaluates more queries. Click Window > Preferences. In the iTest group, go to Response Mapping and increase the Maximum number of queries to evaluate setting.

![screenshot](topics/images/queries_structure_response_views.png) <!-- image_chunk: img_f8696d00abbd3fd8 -->
