---
{
  "chunk_id": "writebytes__intro_e10f7d8585c7ed6b",
  "source_file": "popups/writebytes.html",
  "source_original_path": "popups/writebytes.html",
  "toc_path": null,
  "heading_path": [
    "writebytes.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/udp_session_editor_concept.html"
  ],
  "images": [],
  "content_hash": "e10f7d8585c7ed6b",
  "level": 0
}
---

# writebytes.html

("hexString1" "hexString2")

Sends the specified data, represented in hexadecimal notation, as raw bytes to the destination. The writebytes command bypasses any system encoding. Use quotation marks and a space to delimit strings. Returns confirmation of text sent. If the Flush receive buffer when data is sent session property is enabled, the writebytes command also clears the read buffer. Example writebytes "1a2b3c4d5e6f" sends the actual bytes represented by 1a, 2b, and so on.

For details, see the online help: UDP command reference section under the topic "UDP Session Editor Concept".
