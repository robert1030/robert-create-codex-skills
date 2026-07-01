---
{
  "chunk_id": "session_profile_properties_testcenter__aion_authentication_and_itest_executions_e3ebcbe99391bee1",
  "source_file": "topics/session_profile_properties_testcenter.htm",
  "source_original_path": "topics/session_profile_properties_testcenter.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session profiles",
    "Session profile property settings for Spirent TestCenter sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter sessions",
    "Session profile property settings for Spirent TestCenter sessions",
    "AION Authentication and iTest executions"
  ],
  "anchor": "1465278",
  "context_ids": [
    "session_profile_properties_testcenter"
  ],
  "index_keywords": [
    "Spirent TestCenter GUI sessions",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter GUI > session profile property settings",
    "session profile property settings > Spirent TestCenter GUI sessions"
  ],
  "related_links": [
    "#1317028",
    "#1465170",
    "#1431370"
  ],
  "images": [
    "topics/images/stc_GUI_AION_logged-In.png"
  ],
  "content_hash": "e3ebcbe99391bee1",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter sessions > Session profile property settings for Spirent TestCenter sessions > AION Authentication and iTest executions

Spirent TestCenter application uses AION licensing, and for iTest executions to work, you are required to be logged into AION license server in the Spirent TestCenter application. In addition, you are required to have the Spirent TestCenter application open for the duration of the test execution.

For example:

- Create a new STC Session session profile. See Spirent TestCenter properties

- Click on AION Authentication page and complete as described in AION Authentication.

- Start session. See you are logged

- Close session.

- If Terminate session on disconnect is selected, the session closes and allows you to sign out successfully. See LabServer, Terminate Session on Disconnect.

- If Terminate session on disconnect is not selected, sign out is successful only when all reserved ports are released.

- Start another iTest session to connect to an existing STC session.

If the existing STC session is signed in with AION authentication:

- Sign in is a success if you sign in with the same user account as the existing session.

- Sign in fails if you sign in with a different user account.

1. If the existing STC session is not signed in with AION authentication:

- Sign in fails, if ports are reserved.

- Sign in is a success, if ports were not reserved or all ports were released.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/stc_GUI_AION_logged-In.png) <!-- image_chunk: img_1818f2fa71b60d1c -->
