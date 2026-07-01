---
{
  "chunk_id": "insert_query_on_stored_response_dialog__inserting_a_query_that_returns_a_value_f_abe53fd1ea8f6046",
  "source_file": "topics/insert_query_on_stored_response_dialog.htm",
  "source_original_path": "topics/insert_query_on_stored_response_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Applying queries to stored responses"
  ],
  "heading_path": [
    "Applying queries to stored responses",
    "Applying queries to stored responses",
    "Inserting a query that returns a value from a stored response"
  ],
  "anchor": "1246395",
  "context_ids": [
    "insert_query_on_stored_response_dialog"
  ],
  "index_keywords": [
    "Insert Query on Stored Response",
    "on stored responses",
    "queries",
    "queries on"
  ],
  "index_keyword_paths": [
    "Insert Query on Stored Response",
    "inserting > queries",
    "queries > on stored responses",
    "stored responses > queries on"
  ],
  "related_links": [
    "test_cases_store_response.htm#1320078"
  ],
  "images": [
    "topics/images/analysis_rules_6.2.jpg"
  ],
  "content_hash": "abe53fd1ea8f6046",
  "level": 2
}
---

# Applying queries to stored responses > Applying queries to stored responses > Inserting a query that returns a value from a stored response

1. 1

1. For the step whose response includes the value of interest, ensure that the response is mapped — by a response map, an analysis rule that you added manually, or because the response is structured (for example, SNMP, JSON, or TL1).

1. 2

1. For the step, store the response in a variable (as described in Storing a response into a variable (for use later in the test)). To ensure that the structured part of the response is stored, do not check the Store only the text of the response check box.

1. 3

1. Now, later in the test, create the step that will use the value (for example, a for statement or an eval comparison statement).

1. 4

1. Insert the query. In the Description cell or the Command field, place the cursor where the query should appear (you can select text that will be replaced), and then right-click and select Insert > Query on Stored Response.

The Insert Query on Stored Response dialog box opens.

All responses (for the test case) that are stored in variables appear in the Stored Responses list. Global variables are displayed as /data/varName.

Select a stored response.

1. When you select a stored response, all of the queries that are defined for the response appear in the Response Queries list. Select a query.

1. When you select a query, the text in the Field replacement text box is updated with the appropriate query command in the standard format: [query varName mapperQuery].

1. Double-click a Query in the list or select one and then click Insert. The text in the Field replacement text box is then added at the position of the cursor.

Mapper queries support field substitutions, but some queries may also contain special interpreter characters. So you may need to “escape” these special characters. For example,

- Tcl: query myResponse inputPktsByPort("$portName")

- Python: query('myResponse','inputPktsByPort("'+portName+'")')

In this case, $portName or portName will first be substituted to become, for example, FastEthernet1/0/1.

> **Note:** Note You must place double-quotes around portName because the query engine is XPATH, which requires strings around its arguments.

For a more complicated query:

Tcl: table/row[1]/fieldB

Python: query("myResponse", "table/row[1]/fieldB")

In this case, the square brackets will not be appropriate for interpreter substitution, use:

[query myResponse table/row[1]/fieldB]

> **Note:** Note Even though the response to the current step may appear in the Stored Responses list, it makes no sense to select it for this purpose – the step will not have been executed when the field replacements are made and there is therefore no response for the step.

> **Note:** If a special character (“ \ [ ] $ or the space character) appears in the query, then, in the Field replacement text box, the \ character is inserted to escape the special character. The result is a properly-formatted field replacement.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/analysis_rules_6.2.jpg) <!-- image_chunk: img_f938988bda8e3858 -->
