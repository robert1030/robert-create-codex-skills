---
{
  "chunk_id": "sharing_4__working_with_encrypted_itars_in_itestrt__a6d64274979b14c4",
  "source_file": "topics/sharing.4.htm",
  "source_original_path": "topics/sharing.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Accessing iTest files that are held in iTar files"
  ],
  "heading_path": [
    "Accessing iTest files that are held in iTar files",
    "Accessing iTest files that are held in iTar files",
    "Working with encrypted iTars",
    "Working with encrypted iTars in iTestRT and Network DevOps Agent"
  ],
  "anchor": "1254247",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a6d64274979b14c4",
  "level": 3
}
---

# Accessing iTest files that are held in iTar files > Accessing iTest files that are held in iTar files > Working with encrypted iTars > Working with encrypted iTars in iTestRT and Network DevOps Agent

The following rules apply when executing encrypted iTars in iTestRT and Network DevOps Agent:

- Any encrypted content (test case files, session profiles, parameter files, etc.) are decrypted and used by iTestRT and Network DevOps Agent.

- Any project (encrypted or unencrypted) may depend on encrypted projects. That is, a dependent project can use encrypted project's artifacts for execution, such as:

- Response maps (to associate response map with the step)

- Session profiles (to use in the 'open' step)

- Topologies (to assign a topology to the testcase)

- Procedure libraries (to execute 'call' command)

- Test cases (to execute 'run' command)

- Other files used by different commands and sessions may be used, if the following applies:

- The command actions do not print out decrypted content into response.

- The command actions do not require extracting file contents from iTar (this can happen if the file is required by third party application to be on file system. For example, .app file for Appium session for Appium server application).

The table below lists the iTest commands that prevents you from reading encrypted content. These command actions will fail if an encrypted content is provided passed to them.

| Command | Notes |
| --- | --- |
| readFile action | Prints file to response |
| File session: 'read' command | Prints file to response |
| 'json jsonCreate' command | Prints input JSON file to response |
| 'yamlCreate' command | Prints input YAMLfile to response |
| 'file uriToPath' command | Extracts file from iTar to local system |
| Appium session: 'open' command if .app/.apk is provided via Appium → Application properties 'install'/'upgrade' command (requires .app/.apk file path) |  |
|  | 'open' command if .app/.apk is provided via Appium → Application properties |
|  | 'install'/'upgrade' command (requires .app/.apk file path) |
| Wireshark session: 'query load' command with .pcap file specified 'capture load' command with .pcap file specified |  |
|  | 'query load' command with .pcap file specified |
|  | 'capture load' command with .pcap file specified |
| PowerShell Session: 'open' command if 'Custom Profile property is specified' | Third party PowerShell interpreter requires configuration file to be extracted and contained on local system |
| SNMP session: 'open' command if Mib folder is specified in SNMP MIB Browser → MIBS properties | iReasoning library contains API for loading MIBs using Reader (to bypass extraction from iTar), but it cannot be used. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
