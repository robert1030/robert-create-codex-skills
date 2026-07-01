---
{
  "chunk_id": "avalanche_session_window__parameters_available_when_you_click_conf_1dd96ee4fef915d8",
  "source_file": "topics/avalanche_session_window.htm",
  "source_original_path": "topics/avalanche_session_window.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Spirent Avalanche session window"
  ],
  "heading_path": [
    "Spirent Avalanche session window",
    "Spirent Avalanche session window",
    "Test Control section",
    "Parameters (Available when you click Configure)"
  ],
  "anchor": "1288469",
  "context_ids": [
    "avalanche_session_window"
  ],
  "index_keywords": [
    "Avalanche",
    "Spirent Avalanche",
    "interactive sessions"
  ],
  "index_keyword_paths": [
    "Avalanche > interactive sessions",
    "Spirent Avalanche > interactive sessions",
    "session windows > Spirent Avalanche",
    "sessions > Avalanche"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "1dd96ee4fef915d8",
  "level": 4
}
---

# Spirent Avalanche session window > Spirent Avalanche session window > Test Control section > Parameters (Available when you click Configure)

| OutputDir | Directory to output the test results to |
| --- | --- |
| TrialIfNoLicense - 0 | 1 | 0: Do not use a trial license in the case that no standard license is found 1: Use the trial license in the case that no standard license is found |
| TestFile | Filename of archived test |
| ProjectName | Used when IsCompact is 0 Name of the project to be created |
| TestName | Used when IsCompact is 0 Name of the test to be created |
| ProjectVersion | Used when IsCompact is 0 Version of project to be created |
| TestType | Used when IsCompact is 0 Type of test to be created |
| Ports | List of port addresses for client and server, separated by space characters. Note Ports specified in the session properties have higher priority Port addresses use the following format: ip/slot/port {ip/slot/port mode} (for performance modes) |
| Note | Ports specified in the session properties have higher priority |
| IsCompact - 0 | 1 | 0: Create and configure a new test 1: import the test from the spf file Note The spf file is generated in Avalanche Commander with compacted option |
| Note | The spf file is generated in Avalanche Commander with compacted option |
| License | Name of current license on the current chassis |
| Trial - 0 | 1 | 0: Run test in normal mode 1: Run test in trial mode |
| Username | Username to use when logging in. Leave blank to use default user name |
| ReserveForce - 0 | 1 | 0: Do not perform reserve force 1: Perform reserve force |
| KeepTest - 0 | 1 | 0: Delete imported test and project after test has finished 1: Do not delete imported test and project after test has finished |
| ShowInteractive - 0 | 1 | iTest displays interactive event messages in the Console view. You have the option to log the events to a file. 0: Do not show interactive event messages in log 1: Show interactive event messages in log |
| Profiles | Specify an IP address and slot to switch the profile Tcl syntax List {<IPAddress> {<slotNumber>, <profileName>; etc}} Note Spirent recommends that you do not change the profile using the scripts in the test.tcl file because using the script involves rebooting (which can take several minutes). |
| Note | Spirent recommends that you do not change the profile using the scripts in the test.tcl file because using the script involves rebooting (which can take several minutes). |
| SetProfileForce - 0 | 1 | 0: Do not force set profile 1: Force set profile |
