---
{
  "chunk_id": "get__intro_8ccef1a9241c98b6",
  "source_file": "popups/GET.html",
  "source_original_path": "popups/GET.html",
  "toc_path": null,
  "heading_path": [
    "GET.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/rest_action_reference.html"
  ],
  "images": [],
  "content_hash": "8ccef1a9241c98b6",
  "level": 0
}
---

# GET.html

The GET method is used to read (or retrieve) a representation of a resource

| Action | GET- read (or retrieve) a representation of a resource |
| --- | --- |
| Returns | GET returns a representation in XML or JSON and an HTTP response code of 200 (OK). Entire List: HTTP 200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists. Specific Item: HTTP 200 (OK), single customer. 404 (Not Found), if ID not found or invalid. Error: HTTP 404 (NOT FOUND) or 400 (BAD REQUEST) |
| Method | GET (along with HEAD) requests when used to only read data this way, they are considered safe. Calling GET once has the same effect as calling it 10 times, or none at al. Additionally, GET (and HEAD) is idempotent, which means that making multiple identical requests ends up having the same result as a single request. |
| Example | GET http://www.example.com/customers/12345 GET http://www.example.com/customers/12345/orders GET http://www.example.com/buckets/sample |

For details, see the online help: REST action reference.
