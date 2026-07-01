---
{
  "chunk_id": "action_signalactivate__signalactivate_turn_a_signal_on_e04b0f8dbf70216a",
  "source_file": "topics/action_signalactivate.htm",
  "source_original_path": "topics/action_signalactivate.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalActivate: Turn a signal on"
  ],
  "heading_path": [
    "signalActivate: Turn a signal on",
    "signalActivate: Turn a signal on"
  ],
  "anchor": "1530343",
  "context_ids": [
    "action_signalactivate"
  ],
  "index_keywords": [
    "signalActivate",
    "signalActivate action"
  ],
  "index_keyword_paths": [
    "actions > signalActivate",
    "signalActivate action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e04b0f8dbf70216a",
  "level": 1
}
---

# signalActivate: Turn a signal on > signalActivate: Turn a signal on

A signalActivate eventName step turns on the event called eventName. While an event signal is activated, any threads currently waiting for the event will be allowed to continue and any threads that begin waiting for the event are allowed to continue until the event is deactivated by a signalClear action..

| Action | Command property value (in the Description cell) |
| --- | --- |
| signalActivate | eventName |

In addition to configuring signalActivate as an Action in a step, you can specify signalActivate as an Action for an Event.
