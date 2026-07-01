---
{
  "chunk_id": "then__intro_e1eb080509b81d97",
  "source_file": "topics/popups/then.html",
  "source_original_path": "topics/popups/then.html",
  "toc_path": null,
  "heading_path": [
    "then.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/wrap.html"
  ],
  "images": [
    "images/if_then_else_example.jpg"
  ],
  "content_hash": "e1eb080509b81d97",
  "level": 0
}
---

# then.html

A then construct can appear only as the first construct within an if construct. The steps that are indented under the then step are executed only when the if condition (in the example, $port_count < 4) evaluates to True.

Note: A legal contiguous sequence of if, then, elseif, and else steps will have one if step, followed by one then step, followed by zero or more elseif steps followed by zero or one else step. Any other sequence is illegal. No other types of steps within the scope can be interleaved in these sequences.

See the online help for tips on adding if-then constructs.

![screenshot](images/if_then_else_example.jpg) <!-- image_chunk: img_d209f9cbdb80e244 -->
