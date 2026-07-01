---
{
  "chunk_id": "overview_session_types__built_in_session_types_4dcb99a9976f25f6",
  "source_file": "topics/overview_session_types.htm",
  "source_original_path": "topics/overview_session_types.htm",
  "toc_path": [
    "iTest Online Help",
    "Welcome to iTest",
    "Session types"
  ],
  "heading_path": [
    "Session types",
    "Session types",
    "Built-in Session Types"
  ],
  "anchor": "1169468",
  "context_ids": [
    "overview_session_types"
  ],
  "index_keywords": [
    "Python",
    "Python sessions",
    "Ranorex",
    "Ranorex test sessions"
  ],
  "index_keyword_paths": [
    "Python sessions",
    "Ranorex test sessions",
    "sessions > Python",
    "sessions > Ranorex"
  ],
  "related_links": [
    "python.7.htm#1395866"
  ],
  "images": [],
  "content_hash": "4dcb99a9976f25f6",
  "level": 2
}
---

# Session types > Session types > Built-in Session Types

| Chat (XMPP Chat) | You can add steps that receive and send XMPP chat messages during execution. A test case can send and receive as many messages as are needed. Message text can contain both fixed text and response data |
| --- | --- |
| Command Prompt | You can run Microsoft Windows Command Prompt sessions (that is, run cmd terminal sessions). For each open session, the Command Prompt Session window displays your commands and the local PC's responses. |
| Database Client | The Database Client session window is an interactive browser where you perform database operations and monitor responses. iTest captures all commands and responses and you an save captured items as test case steps that start the session and set and request database records. Automated test cases open the same session window to perform database operations. iTest supports sessions with MySQL, SqlServer, Oracle, Szlite, Derby, or a custom database type that you specify. |
| File | The File session type enables an automated test case to work with text files during execution (open a file, go to a specified position in the file, read a line, write a line, and so on). |
| HTTP | Using an HTTP session, a test case can talk directly with a device using the HTTP protocol operations GET and POST. HTTP GET commands are useful in cases where you are not testing a Web application, but rather are testing something like a device through which the HTTP is passing. |
| SSH | A virtual terminal that communicates with a device using the SSH protocol (SSH-1 or SSH-2) defined in RFC 4250 Note Because Linux and Unix devices typically include Telnet and SSH servers, you can start a Telnet or SSH session to “localhost” to access a shell. |
| Note | Because Linux and Unix devices typically include Telnet and SSH servers, you can start a Telnet or SSH session to “localhost” to access a shell. |
| Swing | The Swing session type allows you to test Java applications with user interfaces that were developed using Swing. |
| Tcl Shell | You can type Tcl commands and expressions into the iTest Tcl Shell session window. iTest captures your commands and the interpreter's responses. |
| Telnet | A virtual terminal that communicates with a device using the Telnet protocol defined in RFC 854 Note Because Linux and Unix devices typically include Telnet and SSH servers, you can start a Telnet or SSH session to “localhost” to access a shell. |
| Note | Because Linux and Unix devices typically include Telnet and SSH servers, you can start a Telnet or SSH session to “localhost” to access a shell. |
| Python | iTest Python session is a terminal session, similar to Tcl Shell. The session uses native Python interpreter to getting responses. Supported versions of interpreters are: 2.4-2.7 and 3.0-3.6. iTest support an internal Python interpreter and also allows you to point to an external interpreter via Preferences settings (see Setting preferences for Python). |
| Bash | iTest supports Bash session on RHEL and Ubuntu environments and invokes the bash shell found in the system path. iTest also allows you to configure a specific bash path to invoke an alternate installation of bash interpreter. The iTest bash session includes two built-in prompts: $ and # |
