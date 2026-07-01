---
{
  "chunk_id": "stc_rest_session_profile_properties__aion_authentication_and_itest_executions_3c76577cce239135",
  "source_file": "topics/stc_rest_session_profile_properties.htm",
  "source_original_path": "topics/stc_rest_session_profile_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session profiles",
    "Session profile property settings for Spirent TestCenter REST sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Session profile property settings for Spirent TestCenter REST sessions",
    "AION Authentication and iTest executions"
  ],
  "anchor": "1442408",
  "context_ids": [
    "stc_rest_session_profile_properties"
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
    "#1440808",
    "#1317009"
  ],
  "images": [
    "topics/images/stc_REST_AION_logged-In.png"
  ],
  "content_hash": "3c76577cce239135",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter REST sessions > Session profile property settings for Spirent TestCenter REST sessions > AION Authentication and iTest executions

Spirent TestCenter application uses AION licensing, and for iTest executions to work, you are required to be logged into AION license server in the Spirent TestCenter application. In addition, you are required to have the Spirent TestCenter application open for the duration of the test execution.

For example:

- Create a new STC REST session profile. See Spirent TestCenter REST session properties

- Click on AION Authentication page and complete as described in AION Authentication.

- Start session. See you are logged

- Close session.

- If Terminate session on disconnect is selected, the session closes and allows you to sign out successfully. See Terminate session on disconnect.

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

![screenshot](topics/images/stc_REST_AION_logged-In.png) <!-- image_chunk: img_7b328562d4a63772 -->
