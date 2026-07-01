---
{
  "chunk_id": "http_session_editor_concept__http_session_window_09608188dbcfce77",
  "source_file": "topics/http_session_editor_concept.htm",
  "source_original_path": "topics/http_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "HTTP Sessions",
    "HTTP session window"
  ],
  "heading_path": [
    "HTTP session window",
    "HTTP session window"
  ],
  "anchor": "1292599",
  "context_ids": [
    "http_session_editor_concept"
  ],
  "index_keywords": [
    "//www.ietf.org/rfc/rfc2732.txt",
    "HTTP sessions",
    "session windows"
  ],
  "index_keyword_paths": [
    "HTTP sessions",
    "message URL http > //www.ietf.org/rfc/rfc2732.txt",
    "session windows",
    "session windows > HTTP sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "09608188dbcfce77",
  "level": 1
}
---

# HTTP session window > HTTP session window

Using an HTTP session, a test case can talk directly with a device using the HTTP protocol operations GET and POST.

HTTP GET commands are useful in cases where you are not testing a Web application, but rather are testing something like a device through which the HTTP is passing.

HTTP protocol properties and options appear in the Protocol-specific property group for devices and test case steps.

> **Note:** Note To use Microsoft Internet Explorer, you must turn on Compatibility View. (Click the Tools button and then click Compatibility View.)

To use a literal IPv6 address in a URL:

- Disable field replacement (substitution) for the property.

- As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html
