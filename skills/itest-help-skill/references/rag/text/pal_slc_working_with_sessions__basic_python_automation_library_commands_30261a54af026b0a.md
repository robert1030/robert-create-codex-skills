---
{
  "chunk_id": "pal_slc_working_with_sessions__basic_python_automation_library_commands_30261a54af026b0a",
  "source_file": "topics/pal_slc_working_with_sessions.htm",
  "source_original_path": "topics/pal_slc_working_with_sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Working with Sessions"
  ],
  "heading_path": [
    "Working with Sessions",
    "Working with Sessions",
    "Basic Python Automation Library Commands"
  ],
  "anchor": "1469966",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "30261a54af026b0a",
  "level": 2
}
---

# Working with Sessions > Working with Sessions > Basic Python Automation Library Commands

| Basic Commands | Description |
| --- | --- |
| SLC.init() | Connects to an iTest instance (GUI or agent) |
| slc.list() | Displays the available projects in the SLC connection (where slc is the SpirentSLC connection object) |
| slc.open() | Imports a project to use during the SLC connection (where slc is the SpirentSLC connection object) |
| project.sessionProfile.open() | Opens a session within an opened project (where project is the opened project object and sessionProfile is a standalone session profile or one in a topology) |
| session.quickCall() | Invokes a quick call available in the opened session (where session is the opened session object and QuickCall is an available quick call associated with that session) |
| session.command(‘myCommand’) | Issues a command within an opened CLI session (where session is the opened session object and myCommand is the command sent to the session) |
| response.text() | Displays the text response from a quick call or command from an active session (where response is the command response object) |
| response.queries() | Lists the available queries (auto-mapped or explicitly mapped) from the response of a quick call or command in an active session (where response is the command response object) |
| response.json | Displays the dictionary object associated with a JSON response (where response is the command response object) |
| slc.sessions.sessionType. open() | Opens a ‘built-in’ session in the SLC connection (where slc is the SpirentSLC connection object) |
| builtInSession.command(‘myCommand’) | Issues a command in an opened built-in session (where builtInSession is the opened session object and myCommand is the command sent to the session) |
| session.action(‘argument’, properties={}) | Invokes a built-in action using custom step properties (where session is the opened session object, argument is the general argument, and properties contains a structure defining custom step properties) |
| session.session_properties() | Lists the available session property syntax that can be used to override settings on a session open operation (where session is the opened session object) |
| session.step_properties(“action”) | Lists the available step property syntax that can be used to override default settings on a step operation (where session is the opened session object and action is a built-in action on the session) |
