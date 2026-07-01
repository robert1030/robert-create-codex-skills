---
{
  "chunk_id": "tce_steps_page__session_95968a428316a396",
  "source_file": "topics/tce_steps_page.htm",
  "source_original_path": "topics/tce_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Test Case editor: Steps page"
  ],
  "heading_path": [
    "Test Case editor: Steps page",
    "Test Case editor: Steps page",
    "Session"
  ],
  "anchor": "1209203",
  "context_ids": [
    "tce_steps_page"
  ],
  "index_keywords": [
    "Python Action syntax, warnings",
    "Steps page",
    "Test Case editor",
    "editing"
  ],
  "index_keyword_paths": [
    "Python Action syntax, warnings",
    "Steps page",
    "Steps page > Test Case editor",
    "Test Case editor > Steps page",
    "step properties > editing",
    "steps > editing"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_case_editor_2.13.jpg"
  ],
  "content_hash": "95968a428316a396",
  "level": 2
}
---

# Test Case editor: Steps page > Test Case editor: Steps page > Session

The Session is a unique identifier for the session that is associated with the step. A test case can open any number of sessions. The first action for each session must be an open action.

iTest typically auto‑assigns the Session ID for a session in the open step for the session. All steps in the session must specify the value in the Session cell.

Important If the session defined in the Open step uses secret parameters, the test case Open step output will be masked (as it is not possible to determine the content of Open step welcome message). See About the Parameter Type ‘Secret’, in “Parameters”.

For devices with more than one session attached or for multiple captures that use the same session profile: To create the Session IDs that appear in the Session cells in the Test Case editor and in test reports, Spirent iTest uses the combination of Session name from the session profile (for example, myDUT) and a unique session number for the day. (for example, myDUT.1 and myDUT.2). If the session profile does not specify a Session name, then Spirent iTest uses the filename of the session profile in its place.

In this example, we named the two sessions t1 and t2 (we used t to represent Telnet). You can use more descriptive names if you like.

> **Tip:** Tip When you are ready to create dynamic QuickCalls or procedures, you can pass the Session ID as a variable. For example, use $my_session in the Session cell rather than the hard‑coded value t1.

This is the URI of the session profile that the open step uses to start session t1.

The session profile specifies the session type, the DUT to connect to, and the configuration of the session window (the terminal for CLI session types or the browser for graphical interfaces).

![screenshot](topics/images/test_case_editor_2.13.jpg) <!-- image_chunk: img_0d6284b6a4b73c05 -->
