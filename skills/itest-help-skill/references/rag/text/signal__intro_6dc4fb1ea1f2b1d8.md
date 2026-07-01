---
{
  "chunk_id": "signal__intro_6dc4fb1ea1f2b1d8",
  "source_file": "popups/signal.html",
  "source_original_path": "popups/signal.html",
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
  "content_hash": "6dc4fb1ea1f2b1d8",
  "level": 0
}
---

# signal.html

signal eventName

A signal eventName step wakes one thread that is waiting on eventName and causes it to continue execution.

- If several threads are waiting on eventName, then one randomly selected thread continues and the rest continue to wait.
- If no threads are waiting on eventName, then eventName remains signaled until a thread consumes the event or a signalClear action removes it.

In addition to configuring signal as an Action in a step, you can specify signal as an Action for an Event.

For details, see the online help: signal: Wake a thread that is waiting on an event.
