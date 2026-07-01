---
{
  "chunk_id": "signalactivate__intro_7b01a9b2ffa573c8",
  "source_file": "popups/signalactivate.html",
  "source_original_path": "popups/signalactivate.html",
  "toc_path": null,
  "heading_path": [
    "signalactivate.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_signalactivate.html"
  ],
  "images": [],
  "content_hash": "7b01a9b2ffa573c8",
  "level": 0
}
---

# signalactivate.html

signalActivate eventName

A signalActivate eventName step turns on the event called eventName. While an event signal is activated, any threads currently waiting for the event will be allowed to continue and any threads that begin waiting for the event are allowed to continue until the event is deactivated by a signalClear action.

In addition to configuring signalActivate as an Action in a step, you can specify signalActivate as an Action for an Event.

For details, see the online help: signalActivate: Turn a signal on.
