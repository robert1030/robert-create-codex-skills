---
{
  "chunk_id": "spirent_avalanche_06__limitations_63740eb7b6ecfd07",
  "source_file": "topics/spirent_avalanche.06.htm",
  "source_original_path": "topics/spirent_avalanche.06.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode)"
  ],
  "heading_path": [
    "Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode)",
    "Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode)",
    "Limitations"
  ],
  "anchor": "1297320",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_avalanche_3.1.jpg",
    "topics/images/spirent_avalanche.2.jpg"
  ],
  "content_hash": "63740eb7b6ecfd07",
  "level": 2
}
---

# Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) > Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) > Limitations

- Demo mode is not supported.

- The Abort, Stop, and Configure actions are disabled in this mode. Aborting a test can result in stale data in the Tcl test directory.

- Do not close the Avalanche session window while the test is running — wait until the test finishes. It can take several minutes to stop the test, shutdown the ABL server, and close the session.



To execute the Avalanche-generated ‘Tcl test’ scripts

1. Set the following environment variables:

- SPIRENT_TCLAPI_ROOT: Path to the directory holding the Tcl API

- SPIRENT_TCLAPI_LICENSEROOT: Path to the directory holding the license key file

1. 2

1. Define a test in Avalanche as you normally would and then use the Generate Tcl Test option to save the configuration script (config.tcl) and test.tcl script in a Tcl test folder.

Pay attention to the following values in config.tcl:

OutputDir — The directory that will contain the results. If the directory does not exist, Avalanche creates it in the folder that contains the Tcl files.

IsPortable — In Avalanche Commander, if the Portable Test option is checked when you generate the Tcl files, then the value of IsPortable is 1.

TclAPIRoot: — In Avalanche Commander, if the Portable Test option is not checked when you generate the Tcl files, then the value of the TclAPIRoot variable is used.

If API root directory does not exist or is not specified by the SPIRENT_TCLAPI_ROOT environment variable, then iTest will set the value of TclAPIRoot to the latest Avalanche API folder. You have the option to set the value as follows:

In the Session Profile editor, click to view the property tree and then select Tcl. Specify the path for the Avalanche Tcl API directory property.

> **Note:** If you move the Avalanche-generated “Tcl test directory” that holds the test.tcl and config.tcl scripts, then you must:

Move the entire folder

1. Edit test.tcl: Specify the new path in the “set testDirectory” line.

1. Specify the new path in the Tcl test folder property in the session profile.

1. 3

1. Configure the session profile. In the session profile editor:

Check the Use Avalanche Tcl test files check box

1. For the Tcl test folder property, specify the path to the test.tcl and config.tcl files.

1. 4

1. Save the session profile.

1. 5

1. Now, open the Avalanche session in iTest, either interactively or as part of an automated test.

When the session starts, iTest checks out libraries, connects to the device, and then starts the Avalanche test (checkout the license, configure and reserve ports, generate test files, upload the test to the server and client clusters, and then start test execution). iTest captures the real-time data and displays it in the Console view. The Avalanche test produces responses and data files that you can analyze when the test concludes.

The session window indicates that the session is executing the Avalanche Tcl test files. On the session window:

- The Configure and Stop buttons are disabled

- Read-only tables display the Server and Client clusters from test.tcl and the Provision List from config.tcl.

When test execution finishes, iTest displays the contents of the results directory as a tree in the Files section of the Avalanche session window. iTest supports multiple Avalanche sessions within a single instance of iTest (sessions must not use the same cards and ports).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/spirent_avalanche_3.1.jpg) <!-- image_chunk: img_6549e3bf144b52db -->

![unknown](topics/images/spirent_avalanche.2.jpg) <!-- image_chunk: img_b1661cc8366a6782 -->
