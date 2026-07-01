---
{
  "chunk_id": "chat_action_reference__chat_action_reference_a8197b64a1510b2f",
  "source_file": "topics/chat_action_reference.htm",
  "source_original_path": "topics/chat_action_reference.htm",
  "toc_path": [
    "iTest Online Help",
    "Chat Sessions (XMPP chat)",
    "Chat action reference"
  ],
  "heading_path": [
    "Chat action reference",
    "Chat action reference"
  ],
  "anchor": "1384581",
  "context_ids": [
    "chat_action_reference"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a8197b64a1510b2f",
  "level": 1
}
---

# Chat action reference > Chat action reference

| flushMessages | Deletes the messages that are currently in the iTest message queue. Use this action to prepare for a readMessage step to ensure that the readMessage receives the next message from the sender and not a message that is currently in the queue. No configurable step properties. |
| --- | --- |
| sendMessage | Sends the current message text. Type the message into the Description cell. Field replacements are supported. To supply multiple lines of text, in the General property group, for the Command property, click Details . Type the text into the Command text box. Step properties: Chat (XMPP) sendMessage Properties Wait for response: Specify the maximum time to wait in seconds for a response. To specify no time limit, specify a negative integer. Default: 20 |
| readMessage | Read the most recent message in the iTest incoming message queue. See the Use pending response step property. Step properties: Chat (XMPP) readMessage Properties Use pending response: Check the box to read the most recent message in the iTest message queue. Uncheck to ensure that the readMessage receives the next message from the sender and not a message that is currently in the queue. See the flushMessages property. Default: checked Wait for response: Specify the maximum time to wait in seconds for a response. To specify no time limit, specify a negative integer. Default: 10 |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
