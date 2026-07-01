---
{
  "chunk_id": "signal__intro_7830713f7da4f2a2",
  "source_file": "topics/popups/signal.html",
  "source_original_path": "topics/popups/signal.html",
  "toc_path": null,
  "heading_path": [
    "signal.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_signal.html"
  ],
  "images": [],
  "content_hash": "7830713f7da4f2a2",
  "level": 0
}
---

# signal.html

signal eventName

- If several threads are waiting on eventName, then one randomly selected thread continues and the rest continue to wait.
- If no threads are waiting on eventName, then eventName remains signaled until a thread consumes the event or a signalClear action removes it.

For details, see the online help: signal: Wake a thread that is waiting on an event.
