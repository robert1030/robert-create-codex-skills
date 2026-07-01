---
{
  "chunk_id": "capture_command_concept__commands_in_interactive_sessions_172f2cba29096182",
  "source_file": "topics/capture_command_concept.htm",
  "source_original_path": "topics/capture_command_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Commands"
  ],
  "heading_path": [
    "Commands",
    "Commands",
    "Commands in interactive sessions"
  ],
  "anchor": "1131778",
  "context_ids": [
    "capture_command_concept"
  ],
  "index_keywords": [
    "CLI commands",
    "defined"
  ],
  "index_keyword_paths": [
    "CLI commands",
    "CLI sessions > defined",
    "commands > defined",
    "terminal-based sessions > defined"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks_8.1.jpg",
    "topics/images/capture_tasks_3.2.jpg"
  ],
  "content_hash": "172f2cba29096182",
  "level": 2
}
---

# Commands > Commands > Commands in interactive sessions

You send commands to a session and the session responds. (A command is a particular type of Action.)

Here's an example of a show interfaces command that was captured during a Telnet session (as displayed in the Response view):

For web-based actions, the Command is an optional argument for the Action. For example, the argument for the setText Action is the text to type into the text box (therefore the value of the Command property is the text that is typed).

Most Web Actions do not require Command values. For example, the click Action requires a Target (the name of the button to click), but not a Command.

![screenshot](topics/images/capture_tasks_8.1.jpg) <!-- image_chunk: img_37f11df7029b5745 -->

![screenshot](topics/images/capture_tasks_3.2.jpg) <!-- image_chunk: img_45c4c0be247241c5 -->
