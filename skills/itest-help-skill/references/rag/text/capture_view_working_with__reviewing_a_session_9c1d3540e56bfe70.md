---
{
  "chunk_id": "capture_view_working_with__reviewing_a_session_9c1d3540e56bfe70",
  "source_file": "topics/capture_view_working_with.htm",
  "source_original_path": "topics/capture_view_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Working in the Capture view"
  ],
  "heading_path": [
    "Working in the Capture view",
    "Working in the Capture view",
    "Reviewing a session"
  ],
  "anchor": "1132574",
  "context_ids": [
    "capture_view_working_with"
  ],
  "index_keywords": [
    "Capture view",
    "saving as Capture reports",
    "saving as procedures",
    "sessions as Capture reports"
  ],
  "index_keyword_paths": [
    "Capture view",
    "saving > sessions as Capture reports",
    "sessions > saving as Capture reports",
    "sessions > saving as procedures",
    "views > Capture view"
  ],
  "related_links": [
    "capture_preferences_capture_view.htm#1195191",
    "action_concept.htm#1527558"
  ],
  "images": [
    "topics/images/capture_tasks.06.jpg"
  ],
  "content_hash": "9c1d3540e56bfe70",
  "level": 2
}
---

# Working in the Capture view > Working in the Capture view > Reviewing a session

Expand a session row to display each captured item in the session. In this example, iTest captured:

- The Telnet session open action for session s5

- The password that you submitted (masked by ******** characters)

- The show version command that you submitted

- The show ip traffic command that you submitted

- Your exit command and the resulting session close action:

> **Tip:** Tip You can set preferences for capture. See Setting preferences for the Capture view.

| Session ID / Action ID | The value in the Session ID column identifies a captured item uniquely by the combination of Session ID and Action ID. The first session is named s.1, the second session is s.2, and so on. For each session, the actions are numbered 1, 2, and so on. So, s.3.5 represents action 5 in session s.3. Note The following exception applies: Before assigning the next Session ID, iTest checks to see whether a session that is still running already has the ID (perhaps it started yesterday or earlier today). iTest skips the duplicate ID and tries the next. | Note | The following exception applies: Before assigning the next Session ID, iTest checks to see whether a session that is still running already has the ID (perhaps it started yesterday or earlier today). iTest skips the duplicate ID and tries the next. |
| --- | --- | --- | --- |
| Note | The following exception applies: Before assigning the next Session ID, iTest checks to see whether a session that is still running already has the ID (perhaps it started yesterday or earlier today). iTest skips the duplicate ID and tries the next. |  |  |
| Action | The Action identifies the open and close actions as well as actions you perform with sessions, for example: Commands to the CLI interface on a device (for example, set routes) Web-based actions like button clicks or filling in and submitting a form field Performing a get or set on an SNMP MIB Submitting a command to a Tcl session See Actions. |  | Commands to the CLI interface on a device (for example, set routes) |
|  | Commands to the CLI interface on a device (for example, set routes) |  |  |
|  | Web-based actions like button clicks or filling in and submitting a form field |  |  |
|  | Performing a get or set on an SNMP MIB |  |  |
|  | Submitting a command to a Tcl session |  |  |
|  | See Actions. |  |  |
| Description | The Description column displays the description of the action that you took, for example the text of a command or the identifier of the button that you clicked on an HTML page. For actions of type open, the Description is the name of the session profile used to start the session. If the session was started without a session profile, then the Description is the combination of the session type and the device IP address or hostname (that is, the name that iTest creates for the session profile that it saves in the recent folder). For actions of type command, the Description is the text of the command (for example, set routes). When a session row is collapsed, its Description cell displays the Description for the session's open step. |  |  |
| Timestamp | Date and time timestamp in yyyy/mm/dd hh:mm format. For example, 2007/07/04 15:42 For sessions: The date and time that the session opened. For steps: The date and time that the step started. |  |  |

![screenshot](topics/images/capture_tasks.06.jpg) <!-- image_chunk: img_f25dbc59ddf8cb55 -->
