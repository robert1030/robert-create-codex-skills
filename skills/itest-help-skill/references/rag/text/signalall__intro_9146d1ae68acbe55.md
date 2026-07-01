---
{
  "chunk_id": "signalall__intro_9146d1ae68acbe55",
  "source_file": "popups/signalall.html",
  "source_original_path": "popups/signalall.html",
  "toc_path": null,
  "heading_path": [
    "signalall.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_signalall.html"
  ],
  "images": [],
  "content_hash": "9146d1ae68acbe55",
  "level": 0
}
---

# signalall.html

signalAll eventName

A signalAll eventName step wakes all of the threads that are waiting on eventName and causes them to continue execution. If no threads are waiting on eventName, then signalAll eventName step does nothing.

Tip: If no threads are currently waiting on eventName and you want the event to “stay around” until explicitly “told not to”, then use signalActivate instead.

In addition to configuring signalAll as an Action in a step, you can specify signalAll as an Action for an Event.

For details, see the online help: signalAll: Wake all threads that are waiting on an event.
