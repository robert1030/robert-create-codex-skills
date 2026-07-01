---
{
  "chunk_id": "session_profile_concept__using_reference_session_profiles_in_topo_9ab92d14959aff40",
  "source_file": "topics/session_profile_concept.htm",
  "source_original_path": "topics/session_profile_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Session profiles: Session configuration settings"
  ],
  "heading_path": [
    "Session profiles: Session configuration settings",
    "Session profiles: Session configuration settings",
    "Using reference session profiles in topology definitions"
  ],
  "anchor": "1304146",
  "context_ids": [
    "session_profile_concept"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "9ab92d14959aff40",
  "level": 2
}
---

# Session profiles: Session configuration settings > Session profiles: Session configuration settings > Using reference session profiles in topology definitions

While an open step in a test case can refer to a session profile to start a session, we recommend that, instead, the step should refer to a device in a topology. The topology file lists all of the devices and session types that will be used while the test case executes. Because each device definition in the topology refers to a reference session profile, common properties are stored and maintained centrally — you benefit from the ongoing improvement to the session profile definitions and avoid the debugging headaches associated with trying to keep a lot of similar files in sync. For example, in the device definition for the particular RX5000 at 12.34.56.78, you would set the Inherit from property to the reference session profile and then specify an IP address property setting of 12.34.56.78.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
