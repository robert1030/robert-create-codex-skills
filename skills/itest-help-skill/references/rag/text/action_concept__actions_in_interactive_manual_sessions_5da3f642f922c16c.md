---
{
  "chunk_id": "action_concept__actions_in_interactive_manual_sessions_5da3f642f922c16c",
  "source_file": "topics/action_concept.htm",
  "source_original_path": "topics/action_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions",
    "Actions"
  ],
  "heading_path": [
    "Actions",
    "Actions",
    "Actions in interactive (manual) sessions"
  ],
  "anchor": "1096920",
  "context_ids": [
    "action_concept"
  ],
  "index_keywords": [
    "EXEC actions",
    "defined"
  ],
  "index_keyword_paths": [
    "EXEC actions > defined",
    "actions > EXEC actions",
    "actions > defined",
    "captured items > defined"
  ],
  "related_links": [],
  "images": [
    "topics/images/actions.1.jpg"
  ],
  "content_hash": "5da3f642f922c16c",
  "level": 2
}
---

# Actions > Actions > Actions in interactive (manual) sessions

You perform actions in a session: send a CLI command to a Telnet session, send get or set actions on a MIB variable in an SNMP session, and so on.

For example, the most common action in Telnet sessions is the command action; that is, submit command text to the session. For step 2.4 in the example, the Action is command and the command text (in the Description cell) is show ip traffic. The device performs a show ip traffic command and returns a response.

- When you start a session, iTest captures an open action (open the connection).

- When a session ends (for example, when you send an exit command in a Telnet session), iTest captures a close action (close the connection).

- The actions that you perform occur between the open and close actions. The session typically returns a response for each action.

![screenshot](topics/images/actions.1.jpg) <!-- image_chunk: img_2bdc4e28100381cc -->
