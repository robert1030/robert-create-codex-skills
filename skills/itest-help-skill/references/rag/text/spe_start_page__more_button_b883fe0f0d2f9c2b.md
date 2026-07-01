---
{
  "chunk_id": "spe_start_page__more_button_b883fe0f0d2f9c2b",
  "source_file": "topics/spe_start_page.htm",
  "source_original_path": "topics/spe_start_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Session Profile editor: Start a New Session page"
  ],
  "heading_path": [
    "Session Profile editor: Start a New Session page",
    "Session Profile editor: Start a New Session page",
    "More button"
  ],
  "anchor": "1279473",
  "context_ids": [
    "spe_start_page"
  ],
  "index_keywords": [
    "New Session page",
    "Session Profile editor",
    "Start a New Session tab",
    "Start page",
    "defining",
    "editing",
    "opening sessions",
    "session profiles",
    "sessions",
    "starting",
    "starting sessions"
  ],
  "index_keyword_paths": [
    "New Session page",
    "Session Profile editor > Start page",
    "Start a New Session tab",
    "editing > session profiles",
    "editors > Session Profile editor",
    "launching > sessions",
    "opening sessions",
    "session profiles > defining",
    "session profiles > editing",
    "sessions > starting",
    "starting sessions"
  ],
  "related_links": [],
  "images": [
    "topics/images/session_profiles_5.1.jpg"
  ],
  "content_hash": "b883fe0f0d2f9c2b",
  "level": 2
}
---

# Session Profile editor: Start a New Session page > Session Profile editor: Start a New Session page > More button

Click to view the property settings that you configure when you launch a new session using the Start Session dialog. The navigator view enables you to select the property group to modify.

- To save your changes to the session profile document, click Save.

- To start the session as defined, click Start (you'll be asked to save the session profile first).

- To reset all property settings to default, click Reset.

> **Note:** Advanced Users Many of the property settings for session profiles support field replacements to enable you to parameterize settings so they can be determined dynamically before an automated test case starts the session. You might use param, profile, scriptEval, and tcl command field replacements to improve the flexibility and portability of automated test cases. Sometimes, to perform an interactive test, you might need to manually start a session that typically starts only for automated test sessions. To enable you to do this, if iTest encounters any param, profile, scriptEval, or tcl command field replacements while starting a session, iTest starts a Tcl interpreter so that the field replacement can be resolved before the session starts.

> **Note:** When the session ends, the Tcl interpreter is disposed. When the session is restarted by pressing Enter, the substitutions are not made again. If a Tcl interpreter service is requested on restart, however, a new interpreter will be created and returned.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/session_profiles_5.1.jpg) <!-- image_chunk: img_6021332060c90394 -->
