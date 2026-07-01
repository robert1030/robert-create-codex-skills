---
{
  "chunk_id": "sp_properties_chat__capture_replay_bb69f63876f256ca",
  "source_file": "topics/sp_properties_chat.htm",
  "source_original_path": "topics/sp_properties_chat.htm",
  "toc_path": [
    "iTest Online Help",
    "Chat Sessions (XMPP chat)",
    "Session profile property settings for Chat (XMPP) sessions"
  ],
  "heading_path": [
    "Session profile property settings for Chat (XMPP) sessions",
    "Session profile property settings for Chat (XMPP) sessions",
    "Capture Replay"
  ],
  "anchor": "1396148",
  "context_ids": [
    "sp_properties_chat"
  ],
  "index_keywords": [
    "Chat session properties",
    "Chat sessions",
    "property settings"
  ],
  "index_keyword_paths": [
    "Chat session properties",
    "Chat sessions",
    "Chat sessions > property settings",
    "configuring > Chat sessions",
    "property settings > Chat sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "bb69f63876f256ca",
  "level": 2
}
---

# Session profile property settings for Chat (XMPP) sessions > Session profile property settings for Chat (XMPP) sessions > Capture Replay

| Treat first received message after send as response | Uncheck the box to ignore the first incoming message. Default: checked |
| --- | --- |
| Capture received messages | Check the box to cause iTest to capture all received messages. In some cases, you may want to speed processing and shorten reports by not capturing responses. Default: checked |
| Default response timeout | Specify the maximum time to wait for a response. The setting enables test cases to succeed even when the receiver is offline at execution time: The test case can send a message to an endpoint that is offline and wait until the receiver responds (or until the timeout expires) before it continues to execute at the next step. To specify no time limit, specify a negative integer. Default: 10 |
| Ignore incoming timeout | Specify the amount of time to wait before capturing responses. The setting enables you to ignore a first incoming message, for example, if it is of no use in the test. To specify no time limit, specify a negative integer. Default: 0 |
