# Actions > Viewing Test Artifacts > The artifactLink command: View test artifacts

The artifactLink command provides a link to view the test case artifacts generated during test execution and stored on an external file system.

For example, iTest and iTestRT stores the test artifact(s) created during test execution to an external file system and provides hyper links to these artifact(s) on the test execution reports.

The artifactLink command includes two properties: URL and Description.

> **Note：** Note iTest requires the description to be in double quotes: '$URL "$description"'. In addition, iTest does not support unescaped backslashes in URLs (RFC 2396). If you need to use backslashes, use double backslashes, as the second character is an escape character.

Example Tcl:

![](images/Tcl-artifactLink.png) <!-- image_ref -->

> **Note：** Note Replace backslash with double backslash or forward slash to ensure the ‘info’ commands (Commands for returning information: info, “iTest Commands”) return path with single backslash. It is recommended to use forward slash (/).

Example Python:

![](images/Python-artifactLink.png) <!-- image_ref -->

During execution, iTest generates a hyper link based on the URL and Description in the execution report. For example:

URL: http://myartifacts/testRun_12345/tcpip.pcap

Description: PCAP from test case

Link to the artifact (generated): <a href="http://myartifacts/testRun_12345/tcpip.pcap">PCAP from test case</a>.

Example Execution Report with hyper link to the generated artifacts.

![](images/report-artifactLink.png) <!-- image_ref -->

iTest supports several flavors of CLI (command line interface) session types — we will describe the CLI command action and break action in this section.
