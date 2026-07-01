---
{
  "chunk_id": "options__intro_babeaf05c108ee82",
  "source_file": "popups/OPTIONS.html",
  "source_original_path": "popups/OPTIONS.html",
  "toc_path": null,
  "heading_path": [
    "OPTIONS.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/rest_action_reference.html"
  ],
  "images": [],
  "content_hash": "babeaf05c108ee82",
  "level": 0
}
---

# OPTIONS.html

The OPTIONS method represents allows the client to determine the options and/or requirements associated with a resource, or the capabilities of a server, without implying a resource action or initiating a resource retrieval.

| Action | OPTIONS - determines the options and/or requirements associated with a resource, or the capabilities of a server. - If the Request-URI is an asterisk (*), the OPTIONS request applies to the server in general rather than to a specific resource. - If the Request-URI is not an asterisk (*), the OPTIONS request applies only to the options that are available when communicating with that resource. |
| --- | --- |
| Returns | HTTP200 response includes any header fields that indicate optional features implemented by the server and applicable to that resource (e.g., Allow). |
| Method | Is inherently idempotent as it has no side effects. |
| Example | OPTIONS /users/me returns: 200 OK Allow: HEAD,GET,PUT,DELETE,OPTIONS |

For details, see the online help: REST action reference.
