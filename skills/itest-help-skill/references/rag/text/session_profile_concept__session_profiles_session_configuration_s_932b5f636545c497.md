---
{
  "chunk_id": "session_profile_concept__session_profiles_session_configuration_s_932b5f636545c497",
  "source_file": "topics/session_profile_concept.htm",
  "source_original_path": "topics/session_profile_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Session profiles: Session configuration settings"
  ],
  "heading_path": [
    "Session profiles: Session configuration settings",
    "Session profiles: Session configuration settings"
  ],
  "anchor": "1304370",
  "context_ids": [
    "session_profile_concept"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "932b5f636545c497",
  "level": 1
}
---

# Session profiles: Session configuration settings > Session profiles: Session configuration settings

The collection of configuration settings that enable you to start a session is called its session profile (required settings like device IP address or hostname and port number, and optional settings like terminal text color, how to handle “more” line-continuation prompts, and so on). Each session profile is a document with file extension .ffsp.

Session profiles are used both to start manual (interactive) test sessions and to open sessions during automated testing (sessions can be with devices or applications). Each profile is of a particular type (Telnet, SSH, SNMP, Web, and so on) and a profile can inherit settings from another session profile.

> **Note:** Note Session profiles define how to start a new session (open a connection) and (except for knowing which prompts, break characters, or command‑completion characters to expect) do not store any information about what occurs during a session (commands and responses, for example). Actions that occur during interactive sessions appear in the Capture view and can be saved as steps in test cases or stored in Capture reports.
