---
{
  "chunk_id": "session_profile_properties_process__example_process_session_on_microsoft_win_cca6b3249f0d9048",
  "source_file": "topics/session_profile_properties_process.htm",
  "source_original_path": "topics/session_profile_properties_process.htm",
  "toc_path": [
    "iTest Online Help",
    "Process Sessions",
    "Session profile property settings for Process sessions"
  ],
  "heading_path": [
    "Session profile property settings for Process sessions",
    "Session profile property settings for Process sessions",
    "Terminal > Font",
    "Example Process session on Microsoft Windows"
  ],
  "anchor": "1249610",
  "context_ids": [
    "session_profile_properties_process"
  ],
  "index_keywords": [
    "Process session properties",
    "Process sessions",
    "configuring",
    "configuring Process",
    "defining",
    "local processes",
    "starting"
  ],
  "index_keyword_paths": [
    "Process session properties",
    "Process sessions > configuring",
    "Process sessions > defining",
    "Process sessions > starting",
    "configuring > Process sessions",
    "local processes > starting",
    "property settings > Process sessions",
    "sessions > configuring Process",
    "starting > local processes"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "cca6b3249f0d9048",
  "level": 3
}
---

# Session profile property settings for Process sessions > Session profile property settings for Process sessions > Terminal > Font > Example Process session on Microsoft Windows

Spirent Process command interpreter.

Copyright (c) 2005 - 2011, Spirent Communications, Inc.

process>help

cd - Show current working directory

cd <working directory> - Change working directory

exit - Exit process application

help - Display application commands

help <prefix> - Display application commands

kill - Kill all running processes

kill <process ID list> - Kill the process

run <command> - Start the process and wait for termination. Use -q[uiet] to display only command output

show platform - Show platform information

show process - Show information about all processes

show process <process ID list> - Show process information

start <command> - Start the process

wait <process ID> - Wait for a process termination

process>show platform

name: Windows XP

ver: 5.1

arch: x86

type: win32

process>start notepad

Process started, ID: 0

process>show 0

Invalid arguments. Type "show ?" for a list of subcommands.

process>show process 0

ID | Command | State | Exit Code

----------------------------------------------------------------------------

0 | notepad | RUNNING | N/A

process>start cmd

Process started, ID: 1

process>show process 1

ID | Command | State | Exit Code

----------------------------------------------------------------------------

1 | cmd | RUNNING | N/A

process>kill 1

Process 1 terminated, exit code: 1

process>wait 0

Waiting for process 0 to terminate...

Process 0 terminated, exit code: 0

process>cd

Working directory: 'c:\'

process>cd c:\temp

process>cd

Working directory: 'c:\temp'

process>exit

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
