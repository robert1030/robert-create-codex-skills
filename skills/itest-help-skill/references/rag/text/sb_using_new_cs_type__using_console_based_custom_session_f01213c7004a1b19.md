---
{
  "chunk_id": "sb_using_new_cs_type__using_console_based_custom_session_f01213c7004a1b19",
  "source_file": "topics/sb_using_new_cs_type.htm",
  "source_original_path": "topics/sb_using_new_cs_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Using the new custom session type"
  ],
  "heading_path": [
    "Using the new custom session type",
    "Using the new custom session type",
    "Using console based custom session"
  ],
  "anchor": "1342026",
  "context_ids": [
    "sb_using_new_cs_type"
  ],
  "index_keywords": [
    "using console based custom session type",
    "using new custom session type"
  ],
  "index_keyword_paths": [
    "session builder > using console based custom session type",
    "session builder > using new custom session type"
  ],
  "related_links": [
    "sb_creating_a_cs_type.htm#1388239",
    "sb_creating_a_cs_type.htm#1325698",
    "sb_creating_a_cs_type.htm#1388021",
    "#1344231",
    "sb_verify_cs_type.htm#1334595"
  ],
  "images": [
    "topics/images/03-open-custom-sessiontype.png",
    "topics/images/03-custom-session-console-init-procedure.png",
    "topics/images/05-e-console-command.png",
    "topics/images/05-f-init-session-start-run-enter-arg.png"
  ],
  "content_hash": "f01213c7004a1b19",
  "level": 2
}
---

# Using the new custom session type > Using the new custom session type > Using console based custom session

The console based custom command hides the base session from the your end user, and allows you to run the session commands via command line interface.

These steps describe opening the new custom session you built with the Extends the existing session not selected on page 1032 (Step 4Define New Session Type wizard—Complete information and export session) and executing the session commands and customizing them.

Step 1

Create a new session profile

Create a new session profile, notice that the new session type listed (e.g., Custom_session).

If you specified an initial procedure when building the custom session (Session Initialization, page 1032), then a session profile page displays for you to update/input value for arguments defined in that initial QuickCall procedure. For example, a Telnet session that requires you to interact with terminal console and provide the username/password to login to the Telnet server is built into the quick-call (that is, enter the usernmae and password to login to the Telnet server).

You may add values or update the existing values (in the arguments) as required.

Start session

Enter the command and parameters as illustrated below. The session command executes and illustrated in the Response View.

If the session includes initialization settings, when the session starts, iTest will execute the initial method automatically and include its response in the open step’s response and console (if running with capture mode). .

The executed commands may be viewed in the Capture View and used to generate a test case as described in See also topic Verify the customized session type to see how the custom session type are used.. In addition, you may also add the saved commands with custom parameters to verify the custom session type as described in Verify the customized session type.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/03-open-custom-sessiontype.png) <!-- image_chunk: img_088f4cde07287548 -->

![screenshot](topics/images/03-custom-session-console-init-procedure.png) <!-- image_chunk: img_74bca471e87bb731 -->

![screenshot](topics/images/05-e-console-command.png) <!-- image_chunk: img_5af278f21defbd35 -->

![screenshot](topics/images/05-f-init-session-start-run-enter-arg.png) <!-- image_chunk: img_343832ec1f22e935 -->
