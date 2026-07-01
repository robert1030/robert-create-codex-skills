---
{
  "chunk_id": "tgen_cmds_ixiatraffic__specifying_the_ports_to_listen_to_8c6c1cc84f7cfb2c",
  "source_file": "topics/tgen_cmds_ixiatraffic.htm",
  "source_original_path": "topics/tgen_cmds_ixiatraffic.htm",
  "toc_path": [
    "iTest Online Help",
    "Syslog Sessions",
    "Syslog command set"
  ],
  "heading_path": [
    "Syslog command set",
    "Syslog command set",
    "Specifying the ports to listen to"
  ],
  "anchor": "1184509",
  "context_ids": [
    "tgen_cmds_ixiatraffic"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences_syslog.htm#1208064"
  ],
  "images": [],
  "content_hash": "8c6c1cc84f7cfb2c",
  "level": 2
}
---

# Syslog command set > Syslog command set > Specifying the ports to listen to

The ports that you specify on the Preferences page are the ports that the syslog server always listens to, regardless of whether Syslog sessions are running. The Syslog server listens on all network interfaces on the specified ports (port 514 by default). See Setting preferences for Syslog sessions.

The ports that you specify in a Syslog session profile determine additional ports for any session that started from the session profile. For example, if the preference setting is 514, and the session profile specifies port 600, then, when the session starts, the syslog server listens on both ports 514 and 600.
