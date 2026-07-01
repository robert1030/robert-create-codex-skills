---
{
  "chunk_id": "sb_creating_a_cs_type__building_a_new_session_type_547d2368cb6adf65",
  "source_file": "topics/sb_creating_a_cs_type.htm",
  "source_original_path": "topics/sb_creating_a_cs_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Creating a custom session type"
  ],
  "heading_path": [
    "Creating a custom session type",
    "Creating a custom session type",
    "Building a new Session type"
  ],
  "anchor": "1381030",
  "context_ids": [
    "sb_creating_a_cs_type"
  ],
  "index_keywords": [
    "build new session type",
    "create custom session type"
  ],
  "index_keyword_paths": [
    "session builder > build new session type",
    "session builder > create custom session type"
  ],
  "related_links": [
    "quickcalls_new_quickcall_library_wizard.htm#1292200",
    "sb_manually_installing_cs_type.htm#1443069",
    "sb_qc_definitions_validation_citeria.htm#1377103",
    "sb_using_new_cs_type.htm#1334365"
  ],
  "images": [
    "topics/images/session_builder.1.jpg",
    "topics/images/session_builder.2.jpg",
    "topics/images/session_builder.3.jpg",
    "topics/images/session_builder.4.jpg"
  ],
  "content_hash": "547d2368cb6adf65",
  "level": 2
}
---

# Creating a custom session type > Creating a custom session type > Building a new Session type

> **Note:** Note Make sure that you have QuickCall libraries defined (Defining a QuickCall) using the required session types, for example, using REST, Tcl, CMD and so on.

Follow these steps to build a custom session type based on the QuickCall library.

Step 1

Export QuickCall Library

These steps describes deriving new session type from native iTest session type and a QuickCall library using REST, Tcl, CMD and other session types.

- Select File > Export from iTest GUI, and the Select window opens.

- Select option ExportQuickCall Libraries to new session type and click Next.

- Click Next and the Select QuickCall Libraries window opens

Select QuickCall Libraries and location to save

When the Select QuickCall Libraries window opens, select the quick call libraries and specify the location to store the custom session package.

- Select the required QuickCall library from its location (All Projects, a specific project, my_project, or resource).

- Select the QuickCall library(s) and indicate the export location (Export To:) by selecting iTest resource or Export to directory.

- Selecting iTest Resource (default):

This is the default location. The custom session will be automatically installed and requires restarting iTest for the installation to take effect.

- Selecting location as Export to directory:

Browse and select the directory to copy the custom session type. This option does not require you to restart iTest as the custom session is not installed automatically. You are required to User need to install this session Browse to the manually for use. See Manually Installing Custom Session Type within iTest for details.

- Click Next and the Define New Session Type wizard displays.

Define New Session Type wizard—QuickCall definitions validation before export

When you click Export QuickCall Libraries to new session type to define custom sessions, iTest validates the QuickCall libraries for any mismatched datatype defined as an argument description and displays errors on the Define New Session Type window. iTest validates exported QuickCall libraries as per the criteria shown in QuickCall definitions validation criteria.

If validation fails, and the Procedure Name, File Path, Session Type, and an error message appears in red text, as shown below

Click the Details link under the Any Issue column to understand the error.

Define New Session Type wizard—Complete information and export session

Enter the following details when the Define New Session Type wizard displays:

- Session name: Enter a meaningful recognizable session type name.

- Version: Valid version number is: \d+(\.\d+)*, for example: 0.9, 0.9.1, 1.0, 1.0.2, 2.2, and so on.

- Session Description: Enter a description as required.

- Session icon: Browse to the location of the icon and select the icon to associate with the session type.

- Session Initialization: Displays selection options based on the procedures inluded in the QuickCall session and the option None. For example, Init, Main, and None (for the illustration above). Select Init to indicate that the custom session includes an initialization/main QuickCall, which initializes the environment settings, authentication, etc, and ensures that the subsequent QuickCalls (Steps) work as required.

For example, a Telnet session requires you to interact with terminal console and provide the username/password to login to Telnet server.

> **Note:** Note A QuickCall library based on iTest sessions (REST, Telnet, SSH, etc) require initialization of environment settings, authentication, etc.

- Extends the existing session: Generate the new Session type with these options.

- Not selected (default). When Extends the existing session is not selected, the custom Session Builder hides the native session type, and provides a command line interface and allows using the console.

> **Note:** Note Selecting Extends the existing session disables any selection in the Session Initialization option.

- Selected. When Extends the existing session is selected, the Session Builder extends the native session type (using the GUI). For example, use this option to extend REST API with custom commands tailored for a particular need.

> **Note:** Note Both options hide the native libraries.

- Inherits license from based session: Selected by default and re-uses license from the based session.

- License ID: Becomes available only when Inherits license from based session is not selected. This option allows you to add a new license to the new session type.

> **Tip:** Tip Contact Spirent customer support to request generating a custom license for your custom session and provide the license key string you wish to use. For example string iTESTOPENSTACK#33.10.2016 for custom OpenStack Neutron session.

- Select the required QuickCall or Select All from the list of usable session type in the Wizard.

When you also select a single procedure to export, from a list of displayed procedures, all the selected procedure’s dependencies will also be exported automatically as session specific commands in the custom session, if any and not selected.

For example, in a Quickcall with 3 procedures A, B, C, where C calls B, B calls A, and A contains a single step to display the Help command, selecting only procedure C to export, also exports procedures A and B as session specific commands.

- The Back, Next, Finish, and Cancel buttons become available only after you complete all the above information. The Next button allows you to attach a document to the new custom session.

Attach User document to the new custom session

If the Next button is available, click Next to select the Document for the new session type.

- Attach document as follows:

- Select Use Online document and provide a URL of the document location.

OR

- Select Attach a document, browse to the document location and select the required text or a PDF document.

Complete defining new session type

Click Finish to complete defining a new session type. It test validates QuickCall definitions as per the criterea described in QuickCall definitions validation criteria.

If the validation process completes sucessfull, a message displays saying that iTest needs to restart in order to apply the new session type and whether you wish to restart iTest. Click Yes to restart iTest.

iTest restarts and the newly installed session type appears in as one of the session types as illustrated in the Start a New Session window (on page 1040).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/session_builder.1.jpg) <!-- image_chunk: img_281071e3db097226 -->

![screenshot](topics/images/session_builder.2.jpg) <!-- image_chunk: img_49260f5bbb0cd174 -->

![screenshot](topics/images/session_builder.3.jpg) <!-- image_chunk: img_e6e6d3bfc03fc929 -->

![screenshot](topics/images/session_builder.4.jpg) <!-- image_chunk: img_ba2c71be3abe4ad6 -->
