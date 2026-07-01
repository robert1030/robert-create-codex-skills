---
{
  "chunk_id": "action_artifactlink__the_artifactlink_command_view_test_artif_106655739827139a",
  "source_file": "topics/action_artifactLink.htm",
  "source_original_path": "topics/action_artifactLink.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Viewing Test Artifacts",
    "The artifactLink command: View test artifacts"
  ],
  "heading_path": [
    "The artifactLink command: View test artifacts",
    "The artifactLink command: View test artifacts"
  ],
  "anchor": "1712938",
  "context_ids": [
    "action_artifactLink"
  ],
  "index_keywords": [
    "artifactLink"
  ],
  "index_keyword_paths": [
    "action > artifactLink",
    "artifactLink"
  ],
  "related_links": [
    "command_for_info.htm#1763095",
    "commands_itest_interpreter.htm#"
  ],
  "images": [
    "topics/images/Tcl-artifactLink.png",
    "topics/images/Python-artifactLink.png",
    "topics/images/report-artifactLink.png"
  ],
  "content_hash": "106655739827139a",
  "level": 1
}
---

# The artifactLink command: View test artifacts > The artifactLink command: View test artifacts

The artifactLink command provides a link to view the test case artifacts generated during test execution and stored on an external file system.

For example, iTest and iTestRT stores the test artifact(s) created during test execution to an external file system and provides hyper links to these artifact(s) on the test execution reports.

The artifactLink command includes two properties: URL and Description.

> **Note:** Note iTest requires the description to be in double quotes: '$URL "$description"'. In addition, iTest does not support unescaped backslashes in URLs (RFC 2396). If you need to use backslashes, use double backslashes, as the second character is an escape character.

Example Tcl:

> **Note:** Note Replace backslash with double backslash or forward slash to ensure the ‘info’ commands (Commands for returning information: info, “iTest Commands”) return path with single backslash. It is recommended to use forward slash (/).

Example Python:

During execution, iTest generates a hyper link based on the URL and Description in the execution report. For example:

URL: http://myartifacts/testRun_12345/tcpip.pcap

Description: PCAP from test case

Link to the artifact (generated): <a href="http://myartifacts/testRun_12345/tcpip.pcap">PCAP from test case</a>.

Example Execution Report with hyper link to the generated artifacts.

iTest supports several flavors of CLI (command line interface) session types — we will describe the CLI command action and break action in this section.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/Tcl-artifactLink.png) <!-- image_chunk: img_f0f85ef199335c55 -->

![screenshot](topics/images/Python-artifactLink.png) <!-- image_chunk: img_1a66cf715bed7edf -->

![screenshot](topics/images/report-artifactLink.png) <!-- image_chunk: img_855d90c40c578ebd -->
