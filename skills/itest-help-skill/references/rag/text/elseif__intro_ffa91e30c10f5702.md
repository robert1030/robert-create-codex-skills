---
{
  "chunk_id": "elseif__intro_ffa91e30c10f5702",
  "source_file": "popups/elseif.html",
  "source_original_path": "popups/elseif.html",
  "toc_path": null,
  "heading_path": [
    "elseif.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/loops_wrap.html"
  ],
  "images": [
    "images/if_then_else_example.jpg"
  ],
  "content_hash": "ffa91e30c10f5702",
  "level": 0
}
---

# elseif.html

An optional EXEC elseif step is a part of an if-then-elseif-else construct.

An EXEC elseif step is legal only when it immediately follows an if statement or another elseif statement. The command for elseif contains an assertion. If no previous if or elseif step that is associated with the elseif was True and the elseif assertion is True, then its nested steps will be executed.

If a previous if or elseif assertion was True, then the elseif assertion not tested.

See the online help for tips on adding if-then constructs.

![screenshot](images/if_then_else_example.jpg) <!-- image_chunk: img_d209f9cbdb80e244 -->
