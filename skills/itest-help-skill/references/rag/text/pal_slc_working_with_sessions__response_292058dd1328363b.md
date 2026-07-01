---
{
  "chunk_id": "pal_slc_working_with_sessions__response_292058dd1328363b",
  "source_file": "topics/pal_slc_working_with_sessions.htm",
  "source_original_path": "topics/pal_slc_working_with_sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Working with Sessions"
  ],
  "heading_path": [
    "Working with Sessions",
    "Working with Sessions",
    "Invoking Actions on Session",
    "Response"
  ],
  "anchor": "1454502",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "292058dd1328363b",
  "level": 3
}
---

# Working with Sessions > Working with Sessions > Invoking Actions on Session > Response

The resulting response object can be used to query details about the action execution and the response itself:

# duration of execution and any error status

>>>response.duration

3 # number of seconds

>>>response.result

'success' # may be success, failed, timeout

# textual rendering of the response

>>>response.text

'textual response data'

# if the response is json, it is easier to grab the json directly as a dictionary

>>>response.json

instance of dictionary # null if not available as json

# if the response is xml, memory location is printed in Python console when trying to access a http response in XML format

>>>response_http.xml

<Element 'Xml' at 0x062603F0>

>>>response.data

{ a structured data object with step structured data }

#Example of structure data object from 'command' session:

>>> response.data

[map: "*"

items {

name: "isEmpty"

value: "false" }

items {

name: "promptName" value: "defaultPrompt"

} items {

name: "echo"

value: "dir" }

items {

name: "prompt"

value: "C:\\Windows\\system32>"

} ]
